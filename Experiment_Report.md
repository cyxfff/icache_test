# Experiment Report

base) chentao@ChentaodeMacBook-Air icache_hiperf % python3 fit/validate_fitted_bench.py  
Loading plan from /Users/chentao/Desktop/tmp/icache_hiperf/output/raw_count_sparse_solver_best.json...
[validate_fitted_bench] warning: resolved candidate by module/case/source_csv fallback for ('itlb', 'itlb_f512_l1_r1', 'itlb.csv')
[validate_fitted_bench] warning: resolved candidate by module/case/source_csv fallback for ('itlb', 'itlb_f4096_l1_r1', 'itlb.csv')
plan_json: /Users/chentao/Desktop/tmp/icache_hiperf/output/raw_count_sparse_solver_best.json
== Validation Compare ==
  repeat_plan: cold_b11000_d2_linear x 14 | fetch_b128_d4_bp0_s4_r1000 x 29 | hot_s8192_b3_r1000 x 35 | itlb_f512_l1_r1 x 205 | itlb_f4096_l1_r1 x 8
  exec_instructions: 2105033903
  miss_rate:
    metric            | target   | exec     | delta    | rel_err
    ------------------+----------+----------+----------+--------
    br_miss_rate      | 2.8141%  | 3.0550%  | 0.2409%  | 8.56%  
    l1i_miss_rate     | 5.5394%  | 7.5868%  | 2.0474%  | 36.96% 
    l2i_miss_rate     | 62.2989% | 58.5756% | -3.7233% | 5.98%  
    l1i_tlb_miss_rate | 0.4984%  | 0.5822%  | 0.0838%  | 16.81% 
    l2i_tlb_miss_rate | 16.1292% | 20.9795% | 4.8503%  | 30.07% 
  mpki_and_raw:
    metric                      | target     | exec       | delta       | rel_err
    ----------------------------+------------+------------+-------------+--------
    br_mis_pred_mpki            | 5.554000   | 5.826509   | 0.272509    | 4.91%  
    br_retired_mpki             | 197.462000 | 190.720153 | -6.741847   | 3.41%  
    l1i_cache_mpki              | 344.559000 | 233.548785 | -111.010215 | 32.22% 
    l1i_cache_refill_mpki       | 19.088000  | 17.718902  | -1.369098   | 7.17%  
    l2i_cache_mpki              | 17.860000  | 17.625797  | -0.234203   | 1.31%  
    l2i_cache_refill_mpki       | 11.123000  | 10.324416  | -0.798584   | 7.18%  
    l1i_tlb_mpki                | 246.990000 | 228.963625 | -18.026375  | 7.30%  
    l1i_tlb_refill_mpki         | 1.231000   | 1.332943   | 0.101943    | 8.28%  
    l2i_tlb_mpki                | 1.846000   | 1.360169   | -0.485831   | 26.32% 
    l2i_tlb_refill_mpki         | 0.298000   | 0.285356   | -0.012644   | 4.24%  
    l2i_cache_access_proxy_mpki | 17.854248  | 17.625797  | -0.228451   | 1.28%  
    l2i_tlb_access_proxy_mpki   | 1.847581   | 1.360169   | -0.487412   | 26.38% 
===== round 1/1 =====
===== perf group =====
events=raw-cpu-cycles:u,raw-instruction-retired:u,raw-br-mis-pred:u,raw-br-retired:u
iters=1
cpu_mask=800
PID is 36501
Profiling duration is 10000.000 seconds.
Start Profiling...
tracked processes have exited (total 923 ms)
                    count  name                           | comment                          | coverage
               12,264,999  raw-br-mis-pred:u              |                                  | (100%)
              401,472,387  raw-br-retired:u               |                                  | (100%)
              886,779,760  raw-cpu-cycles:u               |                                  | (100%)
            2,105,033,903  raw-instruction-retired:u      |                                  | (100%)
PROXYBENCH_READY
completed_iters=1
bench_seconds=0.762711875

===== perf group =====
events=raw-instruction-retired:u,raw-l1-icache:u,raw-l1-icache-refill:u,raw-l2-icache:u,raw-l2-icache-refill:u
iters=1
cpu_mask=800
PID is 36526
Profiling duration is 10000.000 seconds.
Start Profiling...
tracked processes have exited (total 948 ms)
                    count  name                           | comment                          | coverage
            2,105,031,684  raw-instruction-retired:u      |                                  | (100%)
               37,298,850  raw-l1-icache-refill:u         |                                  | (100%)
              491,627,593  raw-l1-icache:u                |                                  | (100%)
               21,733,222  raw-l2-icache-refill:u         |                                  | (100%)
               37,102,861  raw-l2-icache:u                |                                  | (100%)
PROXYBENCH_READY
completed_iters=1
bench_seconds=0.755941250

===== perf group =====
events=raw-instruction-retired:u,raw-l1-itlb:u,raw-l1-itlb-refill:u,raw-l2-itlb:u,raw-l2-itlb-refill:u
iters=1
cpu_mask=800
PID is 36548
Profiling duration is 10000.000 seconds.
Start Profiling...
tracked processes have exited (total 958 ms)
                    count  name                           | comment                          | coverage
            2,105,042,814  raw-instruction-retired:u      |                                  | (100%)
                2,805,902  raw-l1-itlb-refill:u           |                                  | (100%)
              481,978,234  raw-l1-itlb:u                  |                                  | (100%)
                  600,687  raw-l2-itlb-refill:u           |                                  | (100%)
                2,863,213  raw-l2-itlb:u                  |                                  | (100%)
PROXYBENCH_READY
completed_iters=1
bench_seconds=0.760561563


validation written to /Users/chentao/Desktop/tmp/icache_hiperf/output/fitted_bench_validation.csv
(base) chentao@ChentaodeMacBook-Air icache_hiperf % 