/*
 * sparse_solver.c — C implementation of raw-count beam-search sparse solver.
 *
 * Usage:
 *   sparse_solver <config.json> <candidates.csv> <output_results.json> <output_best.json>
 *                 [--max-templates N] [--seed-beam N] [--beam-size N]
 *                 [--expand-per-state N] [--max-nnls-iter N] [--tolerance F]
 *                 [--top-k N] [--threads N]
 *
 * Reads fitter_config.json (target + fit_total_instructions + outer_iters),
 * reads the candidate CSV, runs beam search with NNLS scoring, writes JSON.
 */

#define _GNU_SOURCE
#include <assert.h>
#include <ctype.h>
#include <errno.h>
#include <float.h>
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#ifdef _OPENMP
#include <omp.h>
#endif

/* ── constants ─────────────────────────────────────────────────────────── */
#define MAX_METRICS   21
#define MAX_CANDS     8192
#define MAX_BEAM      256
#define MAX_TOP_K     200
#define MAX_SUBSET    32
#define EPS           1e-12

/* raw metric names in canonical order (matches DEFAULT_RAW_VECTOR_METRICS) */
static const char *METRIC_NAMES[MAX_METRICS] = {
    "instructions:u",
    "br_retired:u",
    "br_mis_pred:u",
    "l1i_cache:u",
    "l1i_cache_refill:u",
    "l1i_tlb:u",
    "l1i_tlb_refill:u",
    "l2i_cache:u",
    "l2i_cache_refill:u",
    "l2i_tlb:u",
    "l2i_tlb_refill:u",
    "l1d_cache:u",
    "l1d_cache_refill:u",
    "l1d_tlb:u",
    "l1d_tlb_refill:u",
    "l2d_cache:u",
    "l2d_cache_refill:u",
    "l2d_tlb:u",
    "l2d_tlb_refill:u",
    "ll_cache:u",
    "ll_cache_miss:u",
};

/* all 22 METRIC_KEYS from config.py (includes cpu-cycles:u) */
static const char *ALL_METRIC_KEYS[] = {
    "cpu-cycles:u",
    "instructions:u",
    "br_retired:u",
    "br_mis_pred:u",
    "l1i_cache:u",
    "l1i_cache_refill:u",
    "l1i_tlb:u",
    "l1i_tlb_refill:u",
    "l2i_cache:u",
    "l2i_cache_refill:u",
    "l2i_tlb:u",
    "l2i_tlb_refill:u",
    "l1d_cache:u",
    "l1d_cache_refill:u",
    "l1d_tlb:u",
    "l1d_tlb_refill:u",
    "l2d_cache:u",
    "l2d_cache_refill:u",
    "l2d_tlb:u",
    "l2d_tlb_refill:u",
    "ll_cache:u",
    "ll_cache_miss:u",
};
#define N_ALL_METRICS 22

/* ── search config ──────────────────────────────────────────────────────── */
typedef struct {
    int max_templates;
    int seed_beam;
    int beam_size;
    int expand_per_state;
    int max_nnls_iter;
    double tolerance;
    int top_k;
    int threads;
} SearchCfg;

static SearchCfg SCFG = {
    .max_templates   = 100,
    .seed_beam       = 96,
    .beam_size       = 128,
    .expand_per_state= 48,
    .max_nnls_iter   = 8000,
    .tolerance       = 0.01,
    .top_k           = 50,
    .threads         = 128,
};

/* ── candidate ──────────────────────────────────────────────────────────── */
typedef struct {
    char  module[256];
    char  case_name[512];
    char  source_csv[256];
    int   source_row;
    double unit_instructions;
    double unit_counts[MAX_METRICS];  /* indexed by active_dim */
    /* full row fields for JSON output */
    char  suite[128];
    char  order_tag[128];
    char  modules_field[512];
    /* params (non-metric fields) stored as raw strings for JSON */
    char  params_json[1024];
} Candidate;

static Candidate g_cands[MAX_CANDS];
static int       g_ncands = 0;

/* ── active metric dimensions ───────────────────────────────────────────── */
static int    g_dim = 0;
static int    g_active_idx[MAX_METRICS];   /* indices into METRIC_NAMES */
static double g_target_raw[MAX_METRICS];   /* target counts per 1B instructions */

/* ── result ─────────────────────────────────────────────────────────────── */
typedef struct {
    int    indices[MAX_SUBSET];
    int    n;
    double coeffs[MAX_SUBSET];
    int    int_repeats[MAX_SUBSET];
    double raw_pred[MAX_METRICS];
    double int_pred[MAX_METRICS];
    double raw_rel_err[MAX_METRICS];
    double int_rel_err[MAX_METRICS];
    double raw_box_viol[MAX_METRICS];
    double int_box_viol[MAX_METRICS];
    double max_box_viol;
    double int_max_box_viol;
    double mean_rel_err;
    double objective;
    int    feasible;
    int    int_feasible;
} Result;

/* ── tiny JSON writer ───────────────────────────────────────────────────── */
typedef struct { char *buf; size_t len; size_t cap; } JBuf;

static void jbuf_init(JBuf *j) { j->cap=4096; j->len=0; j->buf=malloc(j->cap); j->buf[0]=0; }
static void jbuf_free(JBuf *j) { free(j->buf); }
static void jbuf_grow(JBuf *j, size_t need) {
    while (j->len + need + 1 > j->cap) { j->cap *= 2; j->buf = realloc(j->buf, j->cap); }
}
static void jbuf_raw(JBuf *j, const char *s) {
    size_t n = strlen(s); jbuf_grow(j, n);
    memcpy(j->buf + j->len, s, n); j->len += n; j->buf[j->len] = 0;
}
static void jbuf_str(JBuf *j, const char *s) {
    jbuf_raw(j, "\"");
    for (; *s; s++) {
        if (*s == '"')  { jbuf_raw(j, "\\\""); }
        else if (*s == '\\') { jbuf_raw(j, "\\\\"); }
        else if (*s == '\n') { jbuf_raw(j, "\\n"); }
        else { char tmp[2]={*s,0}; jbuf_raw(j, tmp); }
    }
    jbuf_raw(j, "\"");
}
static void jbuf_dbl(JBuf *j, double v) {
    char tmp[64]; snprintf(tmp, sizeof(tmp), "%.10g", v); jbuf_raw(j, tmp);
}
static void jbuf_int(JBuf *j, int v) {
    char tmp[32]; snprintf(tmp, sizeof(tmp), "%d", v); jbuf_raw(j, tmp);
}

/* ── simple JSON parser (minimal, for config) ───────────────────────────── */
static char *skip_ws(char *p) { while (*p && isspace((unsigned char)*p)) p++; return p; }

static char *parse_json_string(char *p, char *out, int maxlen) {
    if (*p != '"') return NULL;
    p++;
    int i = 0;
    while (*p && *p != '"') {
        if (*p == '\\') { p++; if (*p == '"' || *p == '\\') { if(i<maxlen-1) out[i++]=*p; p++; } continue; }
        if (i < maxlen-1) out[i++] = *p;
        p++;
    }
    out[i] = 0;
    if (*p == '"') p++;
    return p;
}

static char *parse_json_number(char *p, double *out) {
    char *end; *out = strtod(p, &end);
    return (end == p) ? NULL : end;
}

/* find key in flat JSON object, return pointer to value start */
static char *json_find_key(char *json, const char *key) {
    char needle[256]; snprintf(needle, sizeof(needle), "\"%s\"", key);
    char *p = strstr(json, needle);
    if (!p) return NULL;
    p += strlen(needle);
    p = skip_ws(p);
    if (*p != ':') return NULL;
    p++; p = skip_ws(p);
    return p;
}

/* parse target object from config JSON */
static int parse_target(char *json, double fit_inst) {
    /* find "target": { ... } */
    char *p = json_find_key(json, "target");
    if (!p || *p != '{') { fprintf(stderr, "no target object in config\n"); return -1; }
    p++;

    /* miss_rate specs: (rate_key, numerator_metric_idx, denominator_metric_idx) */
    struct { const char *rate; const char *num; const char *den; } MISS_RATES[] = {
        {"br_miss_rate",      "br_mis_pred:u",      "br_retired:u"},
        {"l1i_miss_rate",     "l1i_cache_refill:u", "l1i_cache:u"},
        {"l2i_miss_rate",     "l2i_cache_refill:u", "l2i_cache:u"},
        {"l1i_tlb_miss_rate", "l1i_tlb_refill:u",   "l1i_tlb:u"},
        {"l2i_tlb_miss_rate", "l2i_tlb_refill:u",   "l2i_tlb:u"},
        {"l1d_miss_rate",     "l1d_cache_refill:u", "l1d_cache:u"},
        {"l2d_miss_rate",     "l2d_cache_refill:u", "l2d_cache:u"},
        {"l1d_tlb_miss_rate", "l1d_tlb_refill:u",   "l1d_tlb:u"},
        {"l2d_tlb_miss_rate", "l2d_tlb_refill:u",   "l2d_tlb:u"},
        {"ll_miss_rate",      "ll_cache_miss:u",     "ll_cache:u"},
    };
    int n_miss = (int)(sizeof(MISS_RATES)/sizeof(MISS_RATES[0]));

    /* metric index lookup */
    int metric_idx(const char *name) {
        for (int i = 0; i < MAX_METRICS; i++)
            if (strcmp(METRIC_NAMES[i], name) == 0) return i;
        return -1;
    }

    double raw[MAX_METRICS]; int has[MAX_METRICS];
    memset(raw, 0, sizeof(raw)); memset(has, 0, sizeof(has));
    raw[0] = fit_inst; has[0] = 1; /* instructions:u */

    /* scan key:value pairs */
    while (*p && *p != '}') {
        p = skip_ws(p);
        if (*p == '}') break;
        if (*p == ',') { p++; continue; }
        if (*p != '"') { p++; continue; }
        char key[128]; p = parse_json_string(p, key, sizeof(key));
        if (!p) break;
        p = skip_ws(p); if (*p == ':') p++; p = skip_ws(p);
        double val; char *np = parse_json_number(p, &val);
        if (!np) { /* skip non-number */ while (*p && *p != ',' && *p != '}') p++; continue; }
        p = np;

        /* _mpki → raw count */
        int klen = strlen(key);
        if (klen > 5 && strcmp(key+klen-5, "_mpki") == 0) {
            char raw_key[128]; snprintf(raw_key, sizeof(raw_key), "%.*s:u", klen-5, key);
            int idx = metric_idx(raw_key);
            if (idx > 0 && !has[idx]) { raw[idx] = val * fit_inst / 1000.0; has[idx] = 1; }
        }
        /* store miss rates for later derivation */
        for (int r = 0; r < n_miss; r++) {
            if (strcmp(key, MISS_RATES[r].rate) == 0) {
                int ni = metric_idx(MISS_RATES[r].num);
                int di = metric_idx(MISS_RATES[r].den);
                if (ni >= 0 && di >= 0) {
                    if (!has[ni] && has[di]) { raw[ni] = raw[di] * val; has[ni] = 1; }
                    else if (!has[di] && has[ni] && val > EPS) { raw[di] = raw[ni] / val; has[di] = 1; }
                }
            }
        }
    }

    /* second pass: derive remaining from miss rates */
    int changed = 1;
    while (changed) {
        changed = 0;
        for (int r = 0; r < n_miss; r++) {
            int ni = metric_idx(MISS_RATES[r].num);
            int di = metric_idx(MISS_RATES[r].den);
            if (ni < 0 || di < 0) continue;
            /* re-scan JSON for this rate */
            char needle[256]; snprintf(needle, sizeof(needle), "\"%s\"", MISS_RATES[r].rate);
            char *rp = strstr(json, needle);
            if (!rp) continue;
            rp += strlen(needle); rp = skip_ws(rp);
            if (*rp != ':') continue; rp++; rp = skip_ws(rp);
            double rate; if (!parse_json_number(rp, &rate)) continue;
            if (!has[ni] && has[di]) { raw[ni] = raw[di] * rate; has[ni] = 1; changed = 1; }
            else if (!has[di] && has[ni] && rate > EPS) { raw[di] = raw[ni] / rate; has[di] = 1; changed = 1; }
        }
    }

    /* build active dimension list */
    g_dim = 0;
    for (int i = 0; i < MAX_METRICS; i++) {
        if (has[i]) {
            g_active_idx[g_dim] = i;
            g_target_raw[g_dim] = raw[i];
            g_dim++;
        }
    }
    return 0;
}

/* ── CSV parser ─────────────────────────────────────────────────────────── */
/* returns newly allocated buffer; caller must free */
static char *read_file(const char *path) {
    FILE *f = fopen(path, "rb");
    if (!f) { fprintf(stderr, "cannot open %s: %s\n", path, strerror(errno)); return NULL; }
    fseek(f, 0, SEEK_END); long sz = ftell(f); rewind(f);
    char *buf = malloc(sz + 1);
    fread(buf, 1, sz, f); buf[sz] = 0; fclose(f);
    return buf;
}

/* split one CSV line into fields; modifies line in-place */
static int csv_split(char *line, char **fields, int maxf) {
    int n = 0;
    char *p = line;
    while (n < maxf) {
        fields[n++] = p;
        while (*p && *p != ',') p++;
        if (!*p) break;
        *p++ = 0;
    }
    return n;
}

static int find_col(char **hdr, int nhdr, const char *name) {
    for (int i = 0; i < nhdr; i++)
        if (strcmp(hdr[i], name) == 0) return i;
    return -1;
}

static int load_candidates_csv(const char *path, double outer_iters) {
    char *buf = read_file(path);
    if (!buf) return -1;

    char *line = buf;
    /* header */
    char *nl = strchr(line, '\n');
    if (!nl) { free(buf); return -1; }
    *nl = 0;
    /* strip \r */
    if (nl > line && *(nl-1) == '\r') *(nl-1) = 0;

    char *hdr_fields[256]; int nhdr = csv_split(line, hdr_fields, 256);
    /* duplicate header strings since we'll overwrite later lines */
    char *hdr_copy[256];
    for (int i = 0; i < nhdr; i++) hdr_copy[i] = strdup(hdr_fields[i]);

    /* column indices */
    int col_suite    = find_col(hdr_copy, nhdr, "suite");
    int col_case     = find_col(hdr_copy, nhdr, "case");
    int col_order    = find_col(hdr_copy, nhdr, "order_tag");
    int col_modules  = find_col(hdr_copy, nhdr, "modules");
    int col_metrics[N_ALL_METRICS];
    for (int i = 0; i < N_ALL_METRICS; i++)
        col_metrics[i] = find_col(hdr_copy, nhdr, ALL_METRIC_KEYS[i]);

    int row_idx = 0;
    line = nl + 1;
    while (*line && g_ncands < MAX_CANDS) {
        nl = strchr(line, '\n');
        if (nl) { *nl = 0; if (nl > line && *(nl-1)=='\r') *(nl-1)=0; }

        char *fields[256]; int nf = csv_split(line, fields, 256);
        if (nf < 2) goto next_row;

        /* get instructions:u */
        int inst_col = col_metrics[1]; /* instructions:u is index 1 in ALL_METRIC_KEYS */
        if (inst_col < 0 || inst_col >= nf) goto next_row;
        double inst_raw = atof(fields[inst_col]);
        if (inst_raw <= 0.0) goto next_row;
        double unit_inst = (inst_raw / 10000.0) / outer_iters;
        if (unit_inst <= EPS) goto next_row;

        Candidate *c = &g_cands[g_ncands];
        memset(c, 0, sizeof(*c));

        /* module name: use "modules" field if present, else "case" */
        if (col_modules >= 0 && col_modules < nf && fields[col_modules][0])
            snprintf(c->module, sizeof(c->module), "%s", fields[col_modules]);
        else if (col_case >= 0 && col_case < nf)
            snprintf(c->module, sizeof(c->module), "%s", fields[col_case]);

        if (col_case >= 0 && col_case < nf)
            snprintf(c->case_name, sizeof(c->case_name), "%s", fields[col_case]);
        if (col_suite >= 0 && col_suite < nf)
            snprintf(c->suite, sizeof(c->suite), "%s", fields[col_suite]);
        if (col_order >= 0 && col_order < nf)
            snprintf(c->order_tag, sizeof(c->order_tag), "%s", fields[col_order]);
        if (col_modules >= 0 && col_modules < nf)
            snprintf(c->modules_field, sizeof(c->modules_field), "%s", fields[col_modules]);

        snprintf(c->source_csv, sizeof(c->source_csv), "%s", path);
        c->source_row = row_idx;
        c->unit_instructions = unit_inst;

        /* fill unit_counts for active dimensions */
        for (int d = 0; d < g_dim; d++) {
            int mi = g_active_idx[d]; /* index into METRIC_NAMES */
            /* find this metric in ALL_METRIC_KEYS */
            int col = -1;
            for (int k = 0; k < N_ALL_METRICS; k++)
                if (strcmp(ALL_METRIC_KEYS[k], METRIC_NAMES[mi]) == 0) { col = col_metrics[k]; break; }
            double v = 0.0;
            if (col >= 0 && col < nf && fields[col][0]) v = atof(fields[col]);
            c->unit_counts[d] = (v / 10000.0) / outer_iters;
        }

        /* build params_json from non-metric, non-special fields */
        JBuf pj; jbuf_init(&pj); jbuf_raw(&pj, "{");
        int first = 1;
        for (int i = 0; i < nhdr; i++) {
            const char *h = hdr_copy[i];
            if (!h || !h[0] || strcmp(h," ")==0 || strcmp(h,"  ")==0) continue;
            /* skip metric/derived fields */
            int skip = 0;
            for (int k = 0; k < N_ALL_METRICS; k++) if (strcmp(h, ALL_METRIC_KEYS[k])==0) { skip=1; break; }
            if (skip) continue;
            if (strcmp(h,"suite")==0||strcmp(h,"case")==0||strcmp(h,"order_tag")==0||
                strcmp(h,"modules")==0||strcmp(h,"ipc")==0) continue;
            int hlen = strlen(h);
            if (hlen>5 && strcmp(h+hlen-5,"_mpki")==0) continue;
            if (hlen>5 && strcmp(h+hlen-5,"_rate")==0) continue;
            if (i >= nf || !fields[i][0]) continue;
            if (!first) jbuf_raw(&pj, ",");
            first = 0;
            jbuf_str(&pj, h); jbuf_raw(&pj, ":");
            /* try number */
            char *end; double nv = strtod(fields[i], &end);
            if (end != fields[i] && *end == 0) jbuf_dbl(&pj, nv);
            else jbuf_str(&pj, fields[i]);
        }
        jbuf_raw(&pj, "}");
        snprintf(c->params_json, sizeof(c->params_json), "%s", pj.buf);
        jbuf_free(&pj);

        g_ncands++;
next_row:
        row_idx++;
        if (!nl) break;
        line = nl + 1;
    }

    for (int i = 0; i < nhdr; i++) free(hdr_copy[i]);
    free(buf);
    return 0;
}

/* ── NNLS (projected gradient) ──────────────────────────────────────────── */
/* Solve min ||A*x - y||^2  s.t. x >= 0
 * A: dim × n  (column-major: A[d*n + j] = A[d][j])
 * y: dim
 * x: n (output)
 */
static void nnls(const double *A, const double *y, int dim, int n,
                 double *x, int max_iter) {
    if (n == 0) return;
    /* gram = A^T A, rhs = A^T y */
    double *gram = calloc(n * n, sizeof(double));
    double *rhs  = calloc(n,     sizeof(double));
    for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
            double s = 0.0;
            for (int d = 0; d < dim; d++) s += A[d*n+j] * A[d*n+k];
            gram[j*n+k] = s;
        }
        double r = 0.0;
        for (int d = 0; d < dim; d++) r += A[d*n+j] * y[d];
        rhs[j] = r;
    }
    /* spectral norm of gram (power iteration, 20 steps) */
    double *v = calloc(n, sizeof(double)); v[0] = 1.0;
    for (int it = 0; it < 20; it++) {
        double *w = calloc(n, sizeof(double));
        for (int j = 0; j < n; j++) for (int k = 0; k < n; k++) w[j] += gram[j*n+k]*v[k];
        double norm = 0.0; for (int j = 0; j < n; j++) norm += w[j]*w[j]; norm = sqrt(norm);
        if (norm < EPS) break;
        for (int j = 0; j < n; j++) v[j] = w[j]/norm;
        free(w);
    }
    double step_denom = 0.0;
    for (int j = 0; j < n; j++) { double t=0; for(int k=0;k<n;k++) t+=gram[j*n+k]*v[k]; step_denom+=t*v[j]; }
    free(v);
    double step = (step_denom > EPS) ? 1.0/step_denom : 1.0;

    memset(x, 0, n * sizeof(double));
    double *grad = malloc(n * sizeof(double));
    for (int it = 0; it < max_iter; it++) {
        /* grad = gram*x - rhs */
        double diff = 0.0;
        for (int j = 0; j < n; j++) {
            double g = -rhs[j];
            for (int k = 0; k < n; k++) g += gram[j*n+k]*x[k];
            grad[j] = g;
        }
        double max_diff = 0.0;
        for (int j = 0; j < n; j++) {
            double nx = x[j] - step * grad[j];
            if (nx < 0.0) nx = 0.0;
            double d = fabs(nx - x[j]);
            if (d > max_diff) max_diff = d;
            diff += (x[j] > 0.0 ? x[j] : 0.0);
            x[j] = nx;
        }
        double scale = 0.0; for(int j=0;j<n;j++) scale+=x[j]*x[j]; scale=sqrt(scale);
        if (max_diff <= 1e-9 * fmax(1.0, scale)) break;
    }
    free(grad); free(gram); free(rhs);
    for (int j = 0; j < n; j++) if (x[j] < 1e-10) x[j] = 0.0;
}

/* ── evaluate one subset ────────────────────────────────────────────────── */
static void eval_subset(const int *idxs, int n, Result *out) {
    memset(out, 0, sizeof(*out));
    out->n = 0;

    if (n == 0) { out->max_box_viol = 1.0; out->objective = 1e9; return; }

    /* build scaled matrix A (dim × n) and target y */
    double *A = malloc(g_dim * n * sizeof(double));
    double *y = malloc(g_dim * sizeof(double));
    double scales[MAX_METRICS];
    for (int d = 0; d < g_dim; d++) {
        scales[d] = fmax(fabs(g_target_raw[d]), 1.0);
        y[d] = g_target_raw[d] / scales[d];
    }
    for (int j = 0; j < n; j++)
        for (int d = 0; d < g_dim; d++)
            A[d*n+j] = g_cands[idxs[j]].unit_counts[d] / scales[d];

    double *coeffs = calloc(n, sizeof(double));
    nnls(A, y, g_dim, n, coeffs, SCFG.max_nnls_iter);
    free(A); free(y);

    /* collect active */
    int active[MAX_SUBSET]; int na = 0;
    for (int j = 0; j < n; j++) if (coeffs[j] > 0.0) active[na++] = j;

    if (na == 0) {
        free(coeffs);
        out->max_box_viol = 1.0; out->objective = 1e9; return;
    }

    /* refine on active subset if smaller */
    double *coeffs2 = coeffs;
    double *coeffs_active = NULL;
    if (na < n) {
        double *Aa = malloc(g_dim * na * sizeof(double));
        double *ya = malloc(g_dim * sizeof(double));
        for (int d = 0; d < g_dim; d++) {
            ya[d] = g_target_raw[d] / fmax(fabs(g_target_raw[d]), 1.0);
            for (int j = 0; j < na; j++)
                Aa[d*na+j] = g_cands[idxs[active[j]]].unit_counts[d] / fmax(fabs(g_target_raw[d]), 1.0);
        }
        coeffs_active = calloc(na, sizeof(double));
        nnls(Aa, ya, g_dim, na, coeffs_active, SCFG.max_nnls_iter / 2);
        free(Aa); free(ya);
        coeffs2 = calloc(n, sizeof(double));
        for (int j = 0; j < na; j++) coeffs2[active[j]] = coeffs_active[j];
        free(coeffs_active);
        /* recompute active */
        na = 0;
        for (int j = 0; j < n; j++) if (coeffs2[j] > 1e-10) active[na++] = j;
    }

    out->n = na;
    for (int j = 0; j < na; j++) {
        out->indices[j] = idxs[active[j]];
        out->coeffs[j]  = coeffs2[active[j]];
    }

    /* raw prediction */
    for (int d = 0; d < g_dim; d++) {
        double s = 0.0;
        for (int j = 0; j < na; j++)
            s += out->coeffs[j] * g_cands[out->indices[j]].unit_counts[d];
        out->raw_pred[d] = s;
    }

    /* integer repeats */
    for (int j = 0; j < na; j++) {
        int r = (int)round(out->coeffs[j]);
        if (out->coeffs[j] > 0.0 && r < 1) r = 1;
        out->int_repeats[j] = r;
    }
    for (int d = 0; d < g_dim; d++) {
        double s = 0.0;
        for (int j = 0; j < na; j++)
            s += out->int_repeats[j] * g_cands[out->indices[j]].unit_counts[d];
        out->int_pred[d] = s;
    }

    /* errors */
    double tol = SCFG.tolerance;
    double sum_sq = 0.0;
    out->max_box_viol = 0.0; out->int_max_box_viol = 0.0;
    for (int d = 0; d < g_dim; d++) {
        double tv = g_target_raw[d];
        double denom = fmax(fabs(tv), 1.0);
        double rel = (out->raw_pred[d] - tv) / denom;
        out->raw_rel_err[d] = rel;
        sum_sq += rel * rel;
        double lo = (1.0 - tol) * tv, hi = (1.0 + tol) * tv;
        double under = fmax(0.0, lo - out->raw_pred[d]) / denom;
        double over  = fmax(0.0, out->raw_pred[d] - hi) / denom;
        out->raw_box_viol[d] = fmax(under, over);
        if (out->raw_box_viol[d] > out->max_box_viol) out->max_box_viol = out->raw_box_viol[d];

        double irel = (out->int_pred[d] - tv) / denom;
        out->int_rel_err[d] = irel;
        double iunder = fmax(0.0, lo - out->int_pred[d]) / denom;
        double iover  = fmax(0.0, out->int_pred[d] - hi) / denom;
        out->int_box_viol[d] = fmax(iunder, iover);
        if (out->int_box_viol[d] > out->int_max_box_viol) out->int_max_box_viol = out->int_box_viol[d];
    }
    out->mean_rel_err = sqrt(sum_sq / g_dim);
    out->feasible     = (out->max_box_viol <= EPS);
    out->int_feasible = (out->int_max_box_viol <= EPS);
    out->objective    = out->max_box_viol * 1000.0 + out->mean_rel_err;

    if (coeffs2 != coeffs) free(coeffs2);
    free(coeffs);
}

/* ── result ordering ────────────────────────────────────────────────────── */
static int result_cmp(const void *a, const void *b) {
    const Result *ra = (const Result *)a, *rb = (const Result *)b;
    if (ra->feasible != rb->feasible) return rb->feasible - ra->feasible;
    if (ra->max_box_viol != rb->max_box_viol)
        return (ra->max_box_viol < rb->max_box_viol) ? -1 : 1;
    if (ra->mean_rel_err != rb->mean_rel_err)
        return (ra->mean_rel_err < rb->mean_rel_err) ? -1 : 1;
    return 0;
}

/* ── subset signature (sorted indices) ─────────────────────────────────── */
static int sig_cmp(const void *a, const void *b) { return *(int*)a - *(int*)b; }

typedef struct { int idx[MAX_SUBSET]; int n; } Sig;
static Sig make_sig(const int *idxs, int n) {
    Sig s; s.n = n;
    memcpy(s.idx, idxs, n * sizeof(int));
    qsort(s.idx, n, sizeof(int), sig_cmp);
    return s;
}
static int sig_eq(const Sig *a, const Sig *b) {
    if (a->n != b->n) return 0;
    return memcmp(a->idx, b->idx, a->n * sizeof(int)) == 0;
}

/* ── seen-set (open-addressing hash) ───────────────────────────────────── */
#define SEEN_CAP (1<<20)
static Sig *g_seen = NULL;
static int  g_seen_used = 0;

static void seen_init(void) {
    if (!g_seen) g_seen = calloc(SEEN_CAP, sizeof(Sig));
    memset(g_seen, 0xff, SEEN_CAP * sizeof(Sig)); /* -1 = empty */
    g_seen_used = 0;
}
static uint32_t sig_hash(const Sig *s) {
    uint32_t h = 2166136261u;
    for (int i = 0; i < s->n; i++) { h ^= (uint32_t)s->idx[i]; h *= 16777619u; }
    return h;
}
static int seen_contains(const Sig *s) {
    uint32_t h = sig_hash(s) & (SEEN_CAP-1);
    for (int i = 0; i < SEEN_CAP; i++) {
        uint32_t slot = (h + i) & (SEEN_CAP-1);
        if (g_seen[slot].n == -1) return 0;
        if (sig_eq(&g_seen[slot], s)) return 1;
    }
    return 0;
}
static void seen_insert(const Sig *s) {
    if (g_seen_used * 2 >= SEEN_CAP) return; /* full */
    uint32_t h = sig_hash(s) & (SEEN_CAP-1);
    for (int i = 0; i < SEEN_CAP; i++) {
        uint32_t slot = (h + i) & (SEEN_CAP-1);
        if (g_seen[slot].n == -1) { g_seen[slot] = *s; g_seen_used++; return; }
        if (sig_eq(&g_seen[slot], s)) return;
    }
}

/* ── expand scores ──────────────────────────────────────────────────────── */
typedef struct { double score; int idx; } ScoreIdx;
static int score_cmp_desc(const void *a, const void *b) {
    double da = ((ScoreIdx*)a)->score, db = ((ScoreIdx*)b)->score;
    return (da > db) ? -1 : (da < db) ? 1 : 0;
}

static void expand_scores(const Result *res, ScoreIdx *scores, int *nscores) {
    double deficits[MAX_METRICS], overs[MAX_METRICS];
    for (int d = 0; d < g_dim; d++) {
        double tv = g_target_raw[d], denom = fmax(fabs(tv), 1.0);
        deficits[d] = fmax(0.0, tv - res->raw_pred[d]) / denom;
        overs[d]    = fmax(0.0, res->raw_pred[d] - tv) / denom;
    }
    /* current set */
    int in_set[MAX_CANDS]; memset(in_set, 0, g_ncands * sizeof(int));
    for (int j = 0; j < res->n; j++) in_set[res->indices[j]] = 1;

    *nscores = 0;
    for (int i = 0; i < g_ncands; i++) {
        if (in_set[i]) continue;
        double gain = 0.0, penalty = 0.0;
        for (int d = 0; d < g_dim; d++) {
            double v = g_cands[i].unit_counts[d] / fmax(fabs(g_target_raw[d]), 1.0);
            gain    += deficits[d] * v;
            penalty += overs[d]    * v;
        }
        scores[(*nscores)].score = gain - 1.5 * penalty;
        scores[(*nscores)].idx   = i;
        (*nscores)++;
    }
    qsort(scores, *nscores, sizeof(ScoreIdx), score_cmp_desc);
}

/* ── top-k list ─────────────────────────────────────────────────────────── */
static Result g_topk[MAX_TOP_K]; static int g_ntopk = 0;
static Result g_beam[MAX_BEAM];  static int g_nbeam = 0;

static void topk_insert(Result *r, int k) {
    /* check duplicate signature */
    Sig rs = make_sig(r->indices, r->n);
    for (int i = 0; i < g_ntopk; i++) {
        Sig es = make_sig(g_topk[i].indices, g_topk[i].n);
        if (sig_eq(&rs, &es)) {
            if (result_cmp(r, &g_topk[i]) < 0) g_topk[i] = *r;
            qsort(g_topk, g_ntopk, sizeof(Result), result_cmp);
            return;
        }
    }
    if (g_ntopk < k) { g_topk[g_ntopk++] = *r; }
    else if (result_cmp(r, &g_topk[g_ntopk-1]) < 0) { g_topk[g_ntopk-1] = *r; }
    qsort(g_topk, g_ntopk, sizeof(Result), result_cmp);
}

static void beam_insert(Result *r, int k) {
    if (g_nbeam < k) { g_beam[g_nbeam++] = *r; }
    else if (result_cmp(r, &g_beam[g_nbeam-1]) < 0) { g_beam[g_nbeam-1] = *r; }
    qsort(g_beam, g_nbeam, sizeof(Result), result_cmp);
}

/* ── JSON output ────────────────────────────────────────────────────────── */
static void emit_result_json(JBuf *j, int rank, const Result *r,
                             const char *csv_basename) {
    jbuf_raw(j, "{");
    jbuf_raw(j, "\"rank\":"); jbuf_int(j, rank); jbuf_raw(j, ",");
    jbuf_raw(j, "\"feasible\":"); jbuf_raw(j, r->feasible ? "true" : "false"); jbuf_raw(j, ",");
    jbuf_raw(j, "\"max_box_violation\":"); jbuf_dbl(j, r->max_box_viol); jbuf_raw(j, ",");
    jbuf_raw(j, "\"mean_rel_error\":"); jbuf_dbl(j, r->mean_rel_err); jbuf_raw(j, ",");
    jbuf_raw(j, "\"objective\":"); jbuf_dbl(j, r->objective); jbuf_raw(j, ",");
    jbuf_raw(j, "\"selected_templates\":"); jbuf_int(j, r->n); jbuf_raw(j, ",");

    /* coefficients */
    jbuf_raw(j, "\"coefficients\":[");
    for (int i = 0; i < r->n; i++) {
        if (i) jbuf_raw(j, ",");
        const Candidate *c = &g_cands[r->indices[i]];
        jbuf_raw(j, "{");
        jbuf_raw(j, "\"module\":"); jbuf_str(j, c->module); jbuf_raw(j, ",");
        jbuf_raw(j, "\"case\":"); jbuf_str(j, c->case_name); jbuf_raw(j, ",");
        jbuf_raw(j, "\"coefficient\":"); jbuf_dbl(j, r->coeffs[i]); jbuf_raw(j, ",");
        jbuf_raw(j, "\"repeat_count\":"); jbuf_int(j, r->int_repeats[i]); jbuf_raw(j, ",");
        jbuf_raw(j, "\"unit_instructions\":"); jbuf_dbl(j, c->unit_instructions); jbuf_raw(j, ",");
        jbuf_raw(j, "\"source_csv\":"); jbuf_str(j, csv_basename); jbuf_raw(j, ",");
        jbuf_raw(j, "\"source_row\":"); jbuf_int(j, c->source_row);
        jbuf_raw(j, "}");
    }
    jbuf_raw(j, "],");

    /* raw_target */
    jbuf_raw(j, "\"raw_target\":{");
    for (int d = 0; d < g_dim; d++) {
        if (d) jbuf_raw(j, ",");
        jbuf_str(j, METRIC_NAMES[g_active_idx[d]]); jbuf_raw(j, ":");
        jbuf_dbl(j, g_target_raw[d]);
    }
    jbuf_raw(j, "},");

    /* raw_prediction */
    jbuf_raw(j, "\"raw_prediction\":{");
    for (int d = 0; d < g_dim; d++) {
        if (d) jbuf_raw(j, ",");
        jbuf_str(j, METRIC_NAMES[g_active_idx[d]]); jbuf_raw(j, ":");
        jbuf_dbl(j, r->raw_pred[d]);
    }
    jbuf_raw(j, "},");

    /* raw_rel_errors */
    jbuf_raw(j, "\"raw_rel_errors\":{");
    for (int d = 0; d < g_dim; d++) {
        if (d) jbuf_raw(j, ",");
        jbuf_str(j, METRIC_NAMES[g_active_idx[d]]); jbuf_raw(j, ":");
        jbuf_dbl(j, r->raw_rel_err[d]);
    }
    jbuf_raw(j, "},");

    /* repeat_plan_integer */
    jbuf_raw(j, "\"repeat_plan_integer\":[");
    for (int i = 0; i < r->n; i++) {
        if (r->int_repeats[i] <= 0) continue;
        if (i) jbuf_raw(j, ",");
        const Candidate *c = &g_cands[r->indices[i]];
        jbuf_raw(j, "{");
        jbuf_raw(j, "\"module\":"); jbuf_str(j, c->module); jbuf_raw(j, ",");
        jbuf_raw(j, "\"case\":"); jbuf_str(j, c->case_name); jbuf_raw(j, ",");
        jbuf_raw(j, "\"repeat_count\":"); jbuf_int(j, r->int_repeats[i]); jbuf_raw(j, ",");
        jbuf_raw(j, "\"unit_instructions\":"); jbuf_dbl(j, c->unit_instructions); jbuf_raw(j, ",");
        jbuf_raw(j, "\"source_csv\":"); jbuf_str(j, csv_basename); jbuf_raw(j, ",");
        jbuf_raw(j, "\"source_row\":"); jbuf_int(j, c->source_row);
        jbuf_raw(j, "}");
    }
    jbuf_raw(j, "],");

    /* integer_prediction */
    jbuf_raw(j, "\"integer_prediction\":{");
    for (int d = 0; d < g_dim; d++) {
        if (d) jbuf_raw(j, ",");
        jbuf_str(j, METRIC_NAMES[g_active_idx[d]]); jbuf_raw(j, ":");
        jbuf_dbl(j, r->int_pred[d]);
    }
    jbuf_raw(j, "},");

    /* integer_rel_errors */
    jbuf_raw(j, "\"integer_rel_errors\":{");
    for (int d = 0; d < g_dim; d++) {
        if (d) jbuf_raw(j, ",");
        jbuf_str(j, METRIC_NAMES[g_active_idx[d]]); jbuf_raw(j, ":");
        jbuf_dbl(j, r->int_rel_err[d]);
    }
    jbuf_raw(j, "},");

    /* integer_box_violation */
    jbuf_raw(j, "\"integer_box_violation\":{");
    for (int d = 0; d < g_dim; d++) {
        if (d) jbuf_raw(j, ",");
        jbuf_str(j, METRIC_NAMES[g_active_idx[d]]); jbuf_raw(j, ":");
        jbuf_dbl(j, r->int_box_viol[d]);
    }
    jbuf_raw(j, "},");

    jbuf_raw(j, "\"integer_feasible\":"); jbuf_raw(j, r->int_feasible ? "true" : "false"); jbuf_raw(j, ",");
    jbuf_raw(j, "\"integer_max_box_violation\":"); jbuf_dbl(j, r->int_max_box_viol); jbuf_raw(j, ",");

    /* target_metrics (empty dict — Python side fills derived metrics) */
    jbuf_raw(j, "\"target_metrics\":{}");
    jbuf_raw(j, "}");
}

static void write_json_file(const char *path, const char *content) {
    FILE *f = fopen(path, "w");
    if (!f) { fprintf(stderr, "cannot write %s: %s\n", path, strerror(errno)); return; }
    fputs(content, f); fclose(f);
}

/* ── main ───────────────────────────────────────────────────────────────── */
int main(int argc, char **argv) {
    if (argc < 5) {
        fprintf(stderr,
            "Usage: sparse_solver <config.json> <candidates.csv> "
            "<results.json> <best.json> [options]\n"
            "Options:\n"
            "  --max-templates N   (default %d)\n"
            "  --seed-beam N       (default %d)\n"
            "  --beam-size N       (default %d)\n"
            "  --expand-per-state N(default %d)\n"
            "  --max-nnls-iter N   (default %d)\n"
            "  --tolerance F       (default %.3f)\n"
            "  --top-k N           (default %d)\n"
            "  --threads N         (default %d)\n",
            SCFG.max_templates, SCFG.seed_beam, SCFG.beam_size,
            SCFG.expand_per_state, SCFG.max_nnls_iter, SCFG.tolerance,
            SCFG.top_k, SCFG.threads);
        return 1;
    }

    const char *cfg_path     = argv[1];
    const char *csv_path     = argv[2];
    const char *results_path = argv[3];
    const char *best_path    = argv[4];

    for (int i = 5; i < argc; i++) {
        if (!strcmp(argv[i],"--max-templates")    && i+1<argc) { SCFG.max_templates    = atoi(argv[++i]); }
        else if (!strcmp(argv[i],"--seed-beam")   && i+1<argc) { SCFG.seed_beam        = atoi(argv[++i]); }
        else if (!strcmp(argv[i],"--beam-size")   && i+1<argc) { SCFG.beam_size        = atoi(argv[++i]); }
        else if (!strcmp(argv[i],"--expand-per-state") && i+1<argc) { SCFG.expand_per_state = atoi(argv[++i]); }
        else if (!strcmp(argv[i],"--max-nnls-iter") && i+1<argc) { SCFG.max_nnls_iter  = atoi(argv[++i]); }
        else if (!strcmp(argv[i],"--tolerance")   && i+1<argc) { SCFG.tolerance        = atof(argv[++i]); }
        else if (!strcmp(argv[i],"--top-k")       && i+1<argc) { SCFG.top_k            = atoi(argv[++i]); }
        else if (!strcmp(argv[i],"--threads")     && i+1<argc) { SCFG.threads          = atoi(argv[++i]); }
    }

    /* clamp */
    if (SCFG.beam_size  > MAX_BEAM)  SCFG.beam_size  = MAX_BEAM;
    if (SCFG.top_k      > MAX_TOP_K) SCFG.top_k      = MAX_TOP_K;

#ifdef _OPENMP
    omp_set_num_threads(SCFG.threads);
#endif

    /* load config */
    char *cfg_buf = read_file(cfg_path);
    if (!cfg_buf) return 1;

    char *p = json_find_key(cfg_buf, "fit_total_instructions");
    double fit_inst = 1e9;
    if (p) parse_json_number(p, &fit_inst);

    double outer_iters = 1000.0;
    p = json_find_key(cfg_buf, "outer_iters");
    if (p) parse_json_number(p, &outer_iters);

    if (parse_target(cfg_buf, fit_inst) < 0) { free(cfg_buf); return 1; }
    free(cfg_buf);

    fprintf(stderr, "[sparse_solver] dim=%d fit_inst=%.3e outer_iters=%.0f\n",
            g_dim, fit_inst, outer_iters);

    /* load candidates */
    if (load_candidates_csv(csv_path, outer_iters) < 0) return 1;
    fprintf(stderr, "[sparse_solver] loaded %d candidates\n", g_ncands);

    /* csv basename for JSON */
    const char *csv_base = strrchr(csv_path, '/');
    csv_base = csv_base ? csv_base+1 : csv_path;

    /* ── seed phase: evaluate each candidate alone ── */
    seen_init();
    int seed_n = g_ncands;
    Result *seed_results = malloc(seed_n * sizeof(Result));

#pragma omp parallel for schedule(dynamic, 16)
    for (int i = 0; i < seed_n; i++) {
        int idx[1] = {i};
        eval_subset(idx, 1, &seed_results[i]);
    }

    qsort(seed_results, seed_n, sizeof(Result), result_cmp);

    g_nbeam = 0; g_ntopk = 0;
    int actual_seed = (seed_n < SCFG.seed_beam) ? seed_n : SCFG.seed_beam;
    for (int i = 0; i < actual_seed; i++) {
        beam_insert(&seed_results[i], SCFG.beam_size);
        topk_insert(&seed_results[i], SCFG.top_k);
        Sig s = make_sig(seed_results[i].indices, seed_results[i].n);
        seen_insert(&s);
    }
    free(seed_results);

    int best_feasible_idx = -1;
    for (int i = 0; i < g_ntopk; i++)
        if (g_topk[i].feasible) { best_feasible_idx = i; break; }

    fprintf(stderr, "[sparse_solver] seed done, beam=%d topk=%d\n", g_nbeam, g_ntopk);

    /* ── beam search ── */
    ScoreIdx *scores = malloc(g_ncands * sizeof(ScoreIdx));

    for (int depth = 2; depth <= SCFG.max_templates && best_feasible_idx < 0; depth++) {
        /* collect candidate subsets to evaluate */
        int max_new = g_nbeam * SCFG.expand_per_state;
        Sig  *new_sigs    = malloc(max_new * sizeof(Sig));
        int **new_idx_arr = malloc(max_new * sizeof(int*));
        int  *new_ns      = malloc(max_new * sizeof(int));
        int   n_new = 0;

        for (int b = 0; b < g_nbeam && n_new < max_new; b++) {
            int nsc = 0;
            expand_scores(&g_beam[b], scores, &nsc);
            int added = 0;
            for (int s = 0; s < nsc && added < SCFG.expand_per_state && n_new < max_new; s++) {
                int ci = scores[s].idx;
                /* build new index array */
                int nn = g_beam[b].n + 1;
                if (nn > MAX_SUBSET) continue;
                int tmp[MAX_SUBSET];
                memcpy(tmp, g_beam[b].indices, g_beam[b].n * sizeof(int));
                tmp[g_beam[b].n] = ci;
                Sig sig = make_sig(tmp, nn);
                if (seen_contains(&sig)) continue;
                seen_insert(&sig);
                new_sigs[n_new] = sig;
                new_idx_arr[n_new] = malloc(nn * sizeof(int));
                memcpy(new_idx_arr[n_new], sig.idx, nn * sizeof(int));
                new_ns[n_new] = nn;
                n_new++; added++;
            }
        }

        if (n_new == 0) { free(new_sigs); free(new_idx_arr); free(new_ns); break; }

        Result *batch = malloc(n_new * sizeof(Result));
#pragma omp parallel for schedule(dynamic, 8)
        for (int i = 0; i < n_new; i++)
            eval_subset(new_idx_arr[i], new_ns[i], &batch[i]);

        /* reset beam for this depth */
        g_nbeam = 0;
        for (int i = 0; i < n_new; i++) {
            beam_insert(&batch[i], SCFG.beam_size);
            topk_insert(&batch[i], SCFG.top_k);
            if (batch[i].feasible && best_feasible_idx < 0) best_feasible_idx = 0;
        }

        for (int i = 0; i < n_new; i++) free(new_idx_arr[i]);
        free(batch); free(new_sigs); free(new_idx_arr); free(new_ns);

        fprintf(stderr, "[sparse_solver] depth=%d beam=%d topk=%d feasible=%s\n",
                depth, g_nbeam, g_ntopk, best_feasible_idx >= 0 ? "yes" : "no");
    }
    free(scores);

    /* find best feasible */
    const Result *best = NULL;
    for (int i = 0; i < g_ntopk; i++) if (g_topk[i].feasible) { best = &g_topk[i]; break; }
    if (!best && g_ntopk > 0) best = &g_topk[0];

    /* ── write results JSON ── */
    JBuf jout; jbuf_init(&jout);
    jbuf_raw(&jout, "{\"config\":{");
    jbuf_raw(&jout, "\"candidate_pool_size\":"); jbuf_int(&jout, g_ncands); jbuf_raw(&jout, ",");
    jbuf_raw(&jout, "\"max_templates\":"); jbuf_int(&jout, SCFG.max_templates); jbuf_raw(&jout, ",");
    jbuf_raw(&jout, "\"tolerance\":"); jbuf_dbl(&jout, SCFG.tolerance);
    jbuf_raw(&jout, "},\"results\":[");
    for (int i = 0; i < g_ntopk; i++) {
        if (i) jbuf_raw(&jout, ",");
        emit_result_json(&jout, i+1, &g_topk[i], csv_base);
    }
    jbuf_raw(&jout, "]}");
    write_json_file(results_path, jout.buf);
    jbuf_free(&jout);

    /* ── write best JSON ── */
    if (best) {
        JBuf jbest; jbuf_init(&jbest);
        jbuf_raw(&jbest, "{\"config\":{");
        jbuf_raw(&jbest, "\"candidate_pool_size\":"); jbuf_int(&jbest, g_ncands); jbuf_raw(&jbest, ",");
        jbuf_raw(&jbest, "\"max_templates\":"); jbuf_int(&jbest, SCFG.max_templates); jbuf_raw(&jbest, ",");
        jbuf_raw(&jbest, "\"tolerance\":"); jbuf_dbl(&jbest, SCFG.tolerance);
        jbuf_raw(&jbest, "},\"best_result\":");
        emit_result_json(&jbest, 1, best, csv_base);
        jbuf_raw(&jbest, "}");
        write_json_file(best_path, jbest.buf);
        jbuf_free(&jbest);
    }

    fprintf(stderr, "[sparse_solver] done. results -> %s  best -> %s\n",
            results_path, best_path);
    if (best)
        fprintf(stderr, "[sparse_solver] best: feasible=%s max_box_viol=%.6f mean_rel_err=%.6f n=%d\n",
                best->feasible ? "yes" : "no", best->max_box_viol, best->mean_rel_err, best->n);

    free(g_seen);
    return 0;
}
