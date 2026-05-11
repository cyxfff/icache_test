# combo_linearity

## combo_000_s2

### Selected Cases
- `hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33`: `branch_pairs_per_unit=3`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=131072`, `data_pool_nodes=524288`, `data_stride_pages=33`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64`: `data_level=4m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1024`, `data_pool_nodes=524288`, `data_stride_lines=64`, `data_stride_nodes=64`, `data_template=cold`, `direct_run_len=4`, `funcs=4096`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33+itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64`

### Results
single_modules:
    id | module                                                     
    ---+------------------------------------------------------------
    s0 | hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33
    s1 | itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64
single_counts:
    metric             | s0        | s1         
    -------------------+-----------+------------
    cpu-cycles:u       | 218121746 | 11227520289
    instructions:u     | 11281013  | 850220723  
    br_retired:u       | 2021404   | 61511332   
    br_mis_pred:u      | 394       | 10238055   
    l1i_cache:u        | 1518638   | 253340637  
    l1i_cache_refill:u | 776       | 121343632  
    l1i_tlb:u          | 1518638   | 253340637  
    l1i_tlb_refill:u   | 41        | 41906725   
    l2i_cache:u        | 776       | 121343585  
    l2i_cache_refill:u | 738       | 121338940  
    l2i_tlb:u          | 76        | 41913294   
    l2i_tlb_refill:u   | 37        | 40938501   
    l1d_cache:u        | 778732    | 137419366  
    l1d_cache_refill:u | 640733    | 32562292   
    l1d_tlb:u          | 2174516   | 168820486  
    l1d_tlb_refill:u   | 665652    | 10599879   
    l2d_cache:u        | 3295736   | 554919564  
    l2d_cache_refill:u | 1754220   | 300501243  
    l2d_tlb:u          | 666511    | 10620143   
    l2d_tlb_refill:u   | 641305    | 10483740   
    ll_cache:u         | 1284302   | 175631492  
    ll_cache_miss:u    | 1206797   | 676873     
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33+itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64
    shuffle   | itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64+hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33
    sum       | hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33+itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 11567860507 | 11837692840 | 11445642035
    instructions:u     | 861491014   | 861491014   | 861501736  
    br_retired:u       | 63531531    | 63531531    | 63532736   
    br_mis_pred:u      | 10234686    | 10246915    | 10238449   
    l1i_cache:u        | 249614987   | 249910952   | 254859275  
    l1i_cache_refill:u | 121553478   | 121446858   | 121344408  
    l1i_tlb:u          | 249614987   | 249910952   | 254859275  
    l1i_tlb_refill:u   | 41916451    | 41916661    | 41906766   
    l2i_cache:u        | 121553435   | 121446835   | 121344361  
    l2i_cache_refill:u | 121548479   | 121434678   | 121339678  
    l2i_tlb:u          | 41928507    | 41930205    | 41913370   
    l2i_tlb_refill:u   | 40945501    | 40947867    | 40938538   
    l1d_cache:u        | 138371161   | 138556335   | 138198098  
    l1d_cache_refill:u | 35180039    | 34234718    | 33203025   
    l1d_tlb:u          | 170158519   | 170968422   | 170995002  
    l1d_tlb_refill:u   | 11267790    | 11268391    | 11265531   
    l2d_cache:u        | 566547368   | 570328290   | 558215300  
    l2d_cache_refill:u | 311810770   | 313386133   | 302255463  
    l2d_tlb:u          | 11277168    | 11279091    | 11286654   
    l2d_tlb_refill:u   | 11119482    | 11121529    | 11125045   
    ll_cache:u         | 185928614   | 187668854   | 176915794  
    ll_cache_miss:u    | 3323244     | 3611943     | 1883670    

### Combined Memory Layouts
#### canonical: `hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33+itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=541065216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=541134848 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f4096_l1_d4_cold_4m_ns_n524288_p1024_np512_l2_r100_sn64_hot_s4096_bp3_dtlb_512m_ps_n524288_p131072_np4_l1_r100_sp33: `itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64+hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=541065216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=541134848 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp3_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4194304 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4259840 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_001_s2

### Selected Cases
- `cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129`: `blocks=16000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17`: `branch_pairs_per_unit=3`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=8192`, `data_pool_nodes=32768`, `data_stride_pages=17`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129+hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17`

### Results
single_modules:
    id | module                                                       
    ---+--------------------------------------------------------------
    s0 | cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129
    s1 | hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17     
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 56208619214 | 1047889213
    instructions:u     | 4480312001  | 26000951  
    br_retired:u       | 480071603   | 3941393   
    br_mis_pred:u      | 160767453   | 493       
    l1i_cache:u        | 2528831491  | 3422163   
    l1i_cache_refill:u | 329402224   | 3116      
    l1i_tlb:u          | 2528831491  | 3422163   
    l1i_tlb_refill:u   | 5192624     | 49        
    l2i_cache:u        | 329401974   | 3116      
    l2i_cache_refill:u | 329344545   | 959       
    l2i_tlb:u          | 5204045     | 178       
    l2i_tlb_refill:u   | 5190611     | 44        
    l1d_cache:u        | 1032952431  | 5268733   
    l1d_cache_refill:u | 202056851   | 5113654   
    l1d_tlb:u          | 1914735550  | 15621779  
    l1d_tlb_refill:u   | 162622248   | 5145436   
    l2d_cache:u        | 1647917638  | 26161349  
    l2d_cache_refill:u | 848130389   | 10572589  
    l2d_tlb:u          | 164040577   | 5148384   
    l2d_tlb_refill:u   | 161861350   | 5111053   
    ll_cache:u         | 516575124   | 10380918  
    ll_cache_miss:u    | 144867084   | 2705749   
combined_orders:
    id        | modules                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------
    canonical | cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129+hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17
    shuffle   | hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17+cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129
    sum       | cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129+hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 58122887830 | 53899674325 | 57256508427
    instructions:u     | 4506302301  | 4506302290  | 4506312952 
    br_retired:u       | 484011803   | 484011800   | 484012996  
    br_mis_pred:u      | 160357678   | 160307126   | 160767946  
    l1i_cache:u        | 2302621427  | 2313590390  | 2532253654 
    l1i_cache_refill:u | 329549469   | 329330208   | 329405340  
    l1i_tlb:u          | 2302621427  | 2313590390  | 2532253654 
    l1i_tlb_refill:u   | 5202092     | 5201640     | 5192673    
    l2i_cache:u        | 329549234   | 329329936   | 329405090  
    l2i_cache_refill:u | 329514219   | 329295584   | 329345504  
    l2i_tlb:u          | 5216968     | 5211966     | 5204223    
    l2i_tlb_refill:u   | 5199456     | 5200047     | 5190655    
    l1d_cache:u        | 1022044900  | 1029586846  | 1038221164 
    l1d_cache_refill:u | 239137002   | 236994861   | 207170505  
    l1d_tlb:u          | 1864456199  | 1917741226  | 1930357329 
    l1d_tlb_refill:u   | 167794533   | 167793619   | 167767684  
    l2d_cache:u        | 1670333236  | 1675182764  | 1674078987 
    l2d_cache_refill:u | 862207640   | 862482636   | 858702978  
    l2d_tlb:u          | 169049844   | 168965890   | 169188961  
    l2d_tlb_refill:u   | 167062569   | 167026086   | 166972403  
    ll_cache:u         | 522749980   | 524077438   | 526956042  
    ll_cache_miss:u    | 163606241   | 133276699   | 147572833  

### Combined Memory Layouts
#### canonical: `cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129+hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67178496 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s8192_bp3_dtlb_32m_ps_n32768_p8192_np4_l4_r100_sp17_main_b16000_d1_lin_dtlb_32m_ps_n65536_p8192_np8_l1_r100_sp129: `hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17+cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67178496 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b16000_d1_linear_dtlb_32m_pstr_n65536_p8192_np8_l1_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp3_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_002_s2

### Selected Cases
- `cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65`: `blocks=13000`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=65`, `data_template=dtlb`, `direct_run_len=2`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4`: `branch_pairs_per_unit=3`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=16384`, `data_pool_nodes=16384`, `data_stride_pages=4`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65+hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4`

### Results
single_modules:
    id | module                                                        
    ---+---------------------------------------------------------------
    s0 | cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65
    s1 | hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4      
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 61648915542 | 1518425850
    instructions:u     | 2925311953  | 26000951  
    br_retired:u       | 260071597   | 3941393   
    br_mis_pred:u      | 65010100    | 541       
    l1i_cache:u        | 1228644012  | 3425832   
    l1i_cache_refill:u | 263662141   | 4008      
    l1i_tlb:u          | 1228644012  | 3425832   
    l1i_tlb_refill:u   | 4226602     | 41        
    l2i_cache:u        | 263661993   | 4008      
    l2i_cache_refill:u | 263641696   | 1101      
    l2i_tlb:u          | 8289631     | 152       
    l2i_tlb_refill:u   | 4226090     | 39        
    l1d_cache:u        | 466068036   | 5270839   
    l1d_cache_refill:u | 150031844   | 5117605   
    l1d_tlb:u          | 786395898   | 15646731  
    l1d_tlb_refill:u   | 131135067   | 5146363   
    l2d_cache:u        | 1177098830  | 25991839  
    l2d_cache_refill:u | 694174593   | 10373303  
    l2d_tlb:u          | 131177731   | 5149826   
    l2d_tlb_refill:u   | 130935634   | 5126374   
    ll_cache:u         | 361149565   | 10269358  
    ll_cache_miss:u    | 263249531   | 9291703   
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65+hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4
    shuffle   | hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4+cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65
    sum       | cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65+hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 63243158223 | 63126262952 | 63167341392
    instructions:u     | 2951302347  | 2951302274  | 2951312904 
    br_retired:u       | 264011809   | 264011799   | 264012990  
    br_mis_pred:u      | 65045426    | 65028372    | 65010641   
    l1i_cache:u        | 1111777935  | 1107477819  | 1232069844 
    l1i_cache_refill:u | 263870197   | 263854690   | 263666149  
    l1i_tlb:u          | 1111777935  | 1107477819  | 1232069844 
    l1i_tlb_refill:u   | 4226789     | 4226756     | 4226643    
    l2i_cache:u        | 263870054   | 263854570   | 263666001  
    l2i_cache_refill:u | 263851178   | 263828035   | 263642797  
    l2i_tlb:u          | 8295554     | 8287143     | 8289783    
    l2i_tlb_refill:u   | 4226380     | 4226502     | 4226129    
    l1d_cache:u        | 473138565   | 472556788   | 471338875  
    l1d_cache_refill:u | 159239836   | 159437734   | 155149449  
    l1d_tlb:u          | 805120414   | 803268663   | 802042629  
    l1d_tlb_refill:u   | 136298719   | 136265227   | 136281430  
    l2d_cache:u        | 1202796430  | 1202398292  | 1203090669 
    l2d_cache_refill:u | 708119552   | 705286770   | 704547896  
    l2d_tlb:u          | 136314034   | 136286573   | 136327557  
    l2d_tlb_refill:u   | 136033408   | 136033548   | 136062008  
    ll_cache:u         | 371917391   | 370800181   | 371418923  
    ll_cache_miss:u    | 273816079   | 273447730   | 272541234  

### Combined Memory Layouts
#### canonical: `cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65+hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1140850688 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1140920320 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s8192_bp3_dtlb_64m_ps_n16384_p16384_np1_l4_r100_sp4_main_b13000_d2_lin_dtlb_1g_ps_n262144_p262144_np1_l1_r100_sp65: `hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4+cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1140850688 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1140920320 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b13000_d2_linear_dtlb_1g_pstr_n262144_p262144_np1_l1_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp3_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_003_s2

### Selected Cases
- `hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5`: `branch_pairs_per_unit=2`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=5`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=8192`
- `itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3`: `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=65536`, `data_pool_nodes=524288`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=0`, `funcs=2048`, `fusion_ldr_per_unit=2`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5+itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3`

### Results
single_modules:
    id | module                                                     
    ---+------------------------------------------------------------
    s0 | hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5    
    s1 | itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3
single_counts:
    metric             | s0         | s1         
    -------------------+------------+------------
    cpu-cycles:u       | 1071785368 | 31104663113
    instructions:u     | 26000957   | 737692024  
    br_retired:u       | 2661391    | 20571605   
    br_mis_pred:u      | 441        | 4301       
    l1i_cache:u        | 3398228    | 92374206   
    l1i_cache_refill:u | 3114       | 82305549   
    l1i_tlb:u          | 3398228    | 92374206   
    l1i_tlb_refill:u   | 52         | 20590190   
    l2i_cache:u        | 3116       | 82305541   
    l2i_cache_refill:u | 1570       | 82182156   
    l2i_tlb:u          | 133        | 20591906   
    l2i_tlb_refill:u   | 48         | 20545685   
    l1d_cache:u        | 5260428    | 82071129   
    l1d_cache_refill:u | 5118423    | 81857821   
    l1d_tlb:u          | 15667592   | 246138500  
    l1d_tlb_refill:u   | 5157536    | 81960639   
    l2d_cache:u        | 26006314   | 522046464  
    l2d_cache_refill:u | 10395455   | 264026532  
    l2d_tlb:u          | 5160135    | 81967564   
    l2d_tlb_refill:u   | 5125983    | 81959457   
    ll_cache:u         | 10280029   | 165023962  
    ll_cache_miss:u    | 3039731    | 156513400  
combined_orders:
    id        | modules                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------
    canonical | hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5+itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3
    shuffle   | itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3+hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5
    sum       | hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5+itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 32767515575 | 32958318819 | 32176448481
    instructions:u     | 763682299   | 763682299   | 763692981  
    br_retired:u       | 23231803    | 23231803    | 23232996   
    br_mis_pred:u      | 5654        | 4660        | 4742       
    l1i_cache:u        | 95826121    | 95810331    | 95772434   
    l1i_cache_refill:u | 82368741    | 82364746    | 82308663   
    l1i_tlb:u          | 95826121    | 95810331    | 95772434   
    l1i_tlb_refill:u   | 20590613    | 20590842    | 20590242   
    l2i_cache:u        | 82368757    | 82364749    | 82308657   
    l2i_cache_refill:u | 82284272    | 82273113    | 82183726   
    l2i_tlb:u          | 20593237    | 20593292    | 20592039   
    l2i_tlb_refill:u   | 20539873    | 20546721    | 20545733   
    l1d_cache:u        | 87343869    | 87335238    | 87331557   
    l1d_cache_refill:u | 86962926    | 86973782    | 86976244   
    l1d_tlb:u          | 261826081   | 261894050   | 261806092  
    l1d_tlb_refill:u   | 87120061    | 87149453    | 87118175   
    l2d_cache:u        | 548234338   | 548873005   | 548052778  
    l2d_cache_refill:u | 277036779   | 281443991   | 274421987  
    l2d_tlb:u          | 87135331    | 87159369    | 87127699   
    l2d_tlb_refill:u   | 87092011    | 87114774    | 87085440   
    ll_cache:u         | 175460222   | 175512291   | 175303991  
    ll_cache_miss:u    | 166379285   | 166427353   | 159553131  

### Combined Memory Layouts
#### canonical: `hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5+itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=301989888 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=302059520 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f2048_l2_d0_dtlb_256m_ps_n524288_p65536_np8_l2_r100_sp3_hot_s8192_bp2_dtlb_32m_ps_n65536_p8192_np8_l4_r100_sp5: `itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3+hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=301989888 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=302059520 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b128_bp2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l2_r100_dtlb_256m_pstr_n524288_p65536_np8_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_004_s2

### Selected Cases
- `cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32`: `blocks=5000`, `data_level=1m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=256`, `data_pool_nodes=131072`, `data_stride_lines=32`, `data_stride_nodes=32`, `data_template=cold`, `direct_run_len=2`, `fusion_ldr_per_unit=2`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=0`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=16384`, `data_pool_nodes=32768`, `data_stride_pages=9`, `data_template=dtlb`, `direct_run_len=2`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32+fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32     
    s1 | fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9
single_counts:
    metric             | s0         | s1       
    -------------------+------------+----------
    cpu-cycles:u       | 2129603398 | 763227606
    instructions:u     | 274986730  | 30390942 
    br_retired:u       | 23414963   | 2631392  
    br_mis_pred:u      | 5849967    | 613702   
    l1i_cache:u        | 113148354  | 12353009 
    l1i_cache_refill:u | 24803567   | 3429     
    l1i_tlb:u          | 113147321  | 12353009 
    l1i_tlb_refill:u   | 524986     | 108      
    l2i_cache:u        | 24803142   | 3429     
    l2i_cache_refill:u | 24703495   | 1552     
    l2i_tlb:u          | 526951     | 177      
    l2i_tlb_refill:u   | 221        | 96       
    l1d_cache:u        | 52972015   | 5932221  
    l1d_cache_refill:u | 8250824    | 2556488  
    l1d_tlb:u          | 57154628   | 11342229 
    l1d_tlb_refill:u   | 1585878    | 2607850  
    l2d_cache:u        | 149517000  | 14802391 
    l2d_cache_refill:u | 75171587   | 6502886  
    l2d_tlb:u          | 1598140    | 2608840  
    l2d_tlb_refill:u   | 462        | 2568012  
    ll_cache:u         | 50466861   | 6379181  
    ll_cache_miss:u    | 4538316    | 5462258  
combined_orders:
    id        | modules                                                                                                                       
    ----------+-------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32+fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9
    shuffle   | fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9+cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32
    sum       | cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32+fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 8803886393 | 7032028182 | 2892831004
    instructions:u     | 1205691014 | 1200077514 | 305377672 
    br_retired:u       | 102701531  | 102223870  | 26046355  
    br_mis_pred:u      | 25736462   | 25670612   | 6463669   
    l1i_cache:u        | 473296727  | 470759816  | 125501363 
    l1i_cache_refill:u | 105991304  | 105576413  | 24806996  
    l1i_tlb:u          | 473296727  | 470758204  | 125500330 
    l1i_tlb_refill:u   | 2248194    | 2237591    | 525094    
    l2i_cache:u        | 105991251  | 105575826  | 24806571  
    l2i_cache_refill:u | 105630796  | 105199852  | 24705047  
    l2i_tlb:u          | 2256371    | 2248780    | 527128    
    l2i_tlb_refill:u   | 22046      | 20536      | 317       
    l1d_cache:u        | 232287323  | 231265393  | 58904236  
    l1d_cache_refill:u | 39423845   | 39530121   | 10807312  
    l1d_tlb:u          | 252872302  | 251414437  | 68496857  
    l1d_tlb_refill:u   | 9378787    | 9364654    | 4193728   
    l2d_cache:u        | 662867155  | 654599839  | 164319391 
    l2d_cache_refill:u | 332323215  | 327587338  | 81674473  
    l2d_tlb:u          | 9427163    | 9420146    | 4206980   
    l2d_tlb_refill:u   | 2606355    | 2594082    | 2568474   
    ll_cache:u         | 226313944  | 222107071  | 56846042  
    ll_cache_miss:u    | 10636647   | 10097267   | 10000574  

### Combined Memory Layouts
#### canonical: `cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32+fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=68157440 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=68227072 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d2_bp0_s16_dtlb_64m_ps_n32768_p16384_np2_l2_r100_sp9_main_b5000_d2_bitrev_cold_1m_ns_n131072_p256_np512_l2_r100_sn32: `fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9+cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=68157440 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=68227072 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b5000_d2_bitrev_cold_1m_nstr_n131072_p256_np512_l2_sn32`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1048576 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1114112 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d2_bp0_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_005_s2

### Selected Cases
- `cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257`: `blocks=12000`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=32768`, `data_pool_nodes=262144`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=2`, `data_level=2m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=512`, `data_pool_nodes=262144`, `data_stride_lines=2048`, `data_stride_nodes=2048`, `data_template=cold`, `direct_run_len=8`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048`

### Results
single_modules:
    id | module                                                              
    ---+---------------------------------------------------------------------
    s0 | cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257    
    s1 | fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048
single_counts:
    metric             | s0          | s1       
    -------------------+-------------+----------
    cpu-cycles:u       | 88526088118 | 209095956
    instructions:u     | 3480312071  | 25110998 
    br_retired:u       | 360071612   | 4231405  
    br_mis_pred:u      | 120592245   | 140612   
    l1i_cache:u        | 1907678781  | 4935151  
    l1i_cache_refill:u | 254406617   | 1224     
    l1i_tlb:u          | 1907678781  | 4935151  
    l1i_tlb_refill:u   | 4018923     | 68       
    l2i_cache:u        | 254406852   | 1223     
    l2i_cache_refill:u | 254345824   | 1212     
    l2i_tlb:u          | 4025713     | 121      
    l2i_tlb_refill:u   | 3807352     | 63       
    l1d_cache:u        | 872000447   | 3456951  
    l1d_cache_refill:u | 298881735   | 2560881  
    l1d_tlb:u          | 1762002023  | 6111073  
    l1d_tlb_refill:u   | 241926521   | 2580273  
    l2d_cache:u        | 1729694778  | 4461490  
    l2d_cache_refill:u | 870497421   | 532772   
    l2d_tlb:u          | 242842404   | 2582129  
    l2d_tlb_refill:u   | 241404562   | 1208     
    ll_cache:u         | 577067894   | 530073   
    ll_cache_miss:u    | 482766170   | 267226   
combined_orders:
    id        | modules                                                                                                                              
    ----------+--------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048
    shuffle   | fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048+cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257
    sum       | cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 90773266830 | 90012507802 | 88735184074
    instructions:u     | 3505412237  | 3505412362  | 3505423069 
    br_retired:u       | 364301794   | 364301811   | 364303017  
    br_mis_pred:u      | 120391906   | 120433606   | 120732857  
    l1i_cache:u        | 1747074808  | 1740655967  | 1912613932 
    l1i_cache_refill:u | 254456759   | 254458992   | 254407841  
    l1i_tlb:u          | 1747074808  | 1740655967  | 1912613932 
    l1i_tlb_refill:u   | 4019651     | 4020063     | 4018991    
    l2i_cache:u        | 254456705   | 254458822   | 254408075  
    l2i_cache_refill:u | 254425038   | 254417473   | 254347036  
    l2i_tlb:u          | 4029921     | 4028808     | 4025834    
    l2i_tlb_refill:u   | 3907023     | 3815517     | 3807415    
    l1d_cache:u        | 890831690   | 220077290   | 875457398  
    l1d_cache_refill:u | 278663072   | 224354      | 301442616  
    l1d_tlb:u          | 1778509547  | 220215027   | 1768113096 
    l1d_tlb_refill:u   | 244507827   | 5461        | 244506794  
    l2d_cache:u        | 1853938302  | 426987047   | 1734156268 
    l2d_cache_refill:u | 919355588   | 315456700   | 871030193  
    l2d_tlb:u          | 245510544   | 7239        | 245424533  
    l2d_tlb_refill:u   | 241302525   | 1143        | 241405770  
    ll_cache:u         | 630982580   | 911957      | 577597967  
    ll_cache_miss:u    | 496550085   | 13526       | 483033396  

### Combined Memory Layouts
#### canonical: `cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=136314880 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=136384512 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d8_bp2_s16_cold_2m_ns_n262144_p512_np512_l2_r100_sn2048_main_b12000_d1_lin_dtlb_128m_ps_n262144_p32768_np8_l2_r100_sp257: `fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048+cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257`

```text
===== memory layout =====
iters=1 active_data_regions=2 total_data_bytes=8192 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=77824 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b12000_d1_linear_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d8_bp2_s16_r100_cold_2m_nstr_n262144_p512_np512_l2_sn2048`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=2097152 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2162688 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_006_s2

### Selected Cases
- `hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5`: `branch_pairs_per_unit=4`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=262144`, `data_pool_nodes=1048576`, `data_stride_pages=5`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=4`, `funcs=4096`, `fusion_ldr_per_unit=4`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5+itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257`

### Results
single_modules:
    id | module                                                         
    ---+----------------------------------------------------------------
    s0 | hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5      
    s1 | itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257
single_counts:
    metric             | s0        | s1         
    -------------------+-----------+------------
    cpu-cycles:u       | 212793074 | 63995018668
    instructions:u     | 11281007  | 932142028  
    br_retired:u       | 2661406   | 61511607   
    br_mis_pred:u      | 482       | 10243187   
    l1i_cache:u        | 1511151   | 255964387  
    l1i_cache_refill:u | 947       | 126969315  
    l1i_tlb:u          | 1511151   | 255964387  
    l1i_tlb_refill:u   | 49        | 41989018   
    l2i_cache:u        | 947       | 126969272  
    l2i_cache_refill:u | 922       | 126606363  
    l2i_tlb:u          | 112       | 41994601   
    l2i_tlb_refill:u   | 47        | 40932446   
    l1d_cache:u        | 777992    | 219435038  
    l1d_cache_refill:u | 640222    | 167524475  
    l1d_tlb:u          | 2205604   | 554620056  
    l1d_tlb_refill:u   | 679815    | 164062186  
    l2d_cache:u        | 3253067   | 1142287070 
    l2d_cache_refill:u | 1684644   | 532270395  
    l2d_tlb:u          | 680367    | 164076887  
    l2d_tlb_refill:u   | 641859    | 164026819  
    ll_cache:u         | 1282901   | 356860305  
    ll_cache_miss:u    | 1211206   | 335353245  
combined_orders:
    id        | modules                                                                                                                  
    ----------+--------------------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5+itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257
    shuffle   | itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257+hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5
    sum       | hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5+itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 64126958157 | 64346787575 | 64207811742
    instructions:u     | 943412281   | 943412342   | 943423035  
    br_retired:u       | 64171799    | 64171809    | 64173013   
    br_mis_pred:u      | 10248190    | 10242747    | 10243669   
    l1i_cache:u        | 260060447   | 256492130   | 257475538  
    l1i_cache_refill:u | 126892670   | 126969583   | 126970262  
    l1i_tlb:u          | 260060447   | 256492130   | 257475538  
    l1i_tlb_refill:u   | 41997972    | 41997622    | 41989067   
    l2i_cache:u        | 126892658   | 126969613   | 126970219  
    l2i_cache_refill:u | 126467132   | 126517935   | 126607285  
    l2i_tlb:u          | 42011980    | 42009944    | 41994713   
    l2i_tlb_refill:u   | 40948920    | 40936837    | 40932493   
    l1d_cache:u        | 220011009   | 220047327   | 220213030  
    l1d_cache_refill:u | 168095792   | 168340141   | 168164697  
    l1d_tlb:u          | 556536555   | 556385892   | 556825660  
    l1d_tlb_refill:u   | 164742540   | 164742168   | 164742001  
    l2d_cache:u        | 1147754538  | 1150873992  | 1145540137 
    l2d_cache_refill:u | 537210540   | 538433080   | 533955039  
    l2d_tlb:u          | 164755602   | 164756374   | 164757254  
    l2d_tlb_refill:u   | 164669611   | 164671444   | 164668678  
    ll_cache:u         | 360433403   | 361349486   | 358143206  
    ll_cache_miss:u    | 340640551   | 340494922   | 336564451  

### Combined Memory Layouts
#### canonical: `hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5+itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1610612736 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1610682368 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f4096_l1_d4_dtlb_512m_ps_n1048576_p131072_np8_l4_r100_sp257_hot_s4096_bp4_dtlb_1g_ps_n1048576_p262144_np4_l1_r100_sp5: `itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257+hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1610612736 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1610682368 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp4_r100_dtlb_1g_pstr_n1048576_p262144_np4_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_007_s2

### Selected Cases
- `cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8`: `blocks=15000`, `data_level=4k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1`, `data_pool_nodes=512`, `data_stride_lines=8`, `data_stride_nodes=8`, `data_template=hot`, `direct_run_len=4`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17`: `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=16384`, `data_pool_nodes=65536`, `data_stride_pages=17`, `data_template=dtlb`, `direct_run_len=0`, `funcs=2048`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8+itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17`

### Results
single_modules:
    id | module                                                    
    ---+-----------------------------------------------------------
    s0 | cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8    
    s1 | itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17
single_counts:
    metric             | s0          | s1         
    -------------------+-------------+------------
    cpu-cycles:u       | 18224416673 | 17860553987
    instructions:u     | 3412810723  | 696730729  
    br_retired:u       | 225071332   | 20571330   
    br_mis_pred:u      | 37496993    | 2501       
    l1i_cache:u        | 942455823   | 87277844   
    l1i_cache_refill:u | 330395236   | 81888775   
    l1i_tlb:u          | 942455823   | 87277844   
    l1i_tlb_refill:u   | 5332270     | 20550043   
    l2i_cache:u        | 330395047   | 81888750   
    l2i_cache_refill:u | 330266644   | 81847717   
    l2i_tlb:u          | 9895279     | 20551197   
    l2i_tlb_refill:u   | 30550       | 19795886   
    l1d_cache:u        | 790793396   | 41104624   
    l1d_cache_refill:u | 21197358    | 40922956   
    l1d_tlb:u          | 806901583   | 123240416  
    l1d_tlb_refill:u   | 635247      | 41000645   
    l2d_cache:u        | 501163600   | 312351793  
    l2d_cache_refill:u | 381172001   | 167743696  
    l2d_tlb:u          | 636707      | 41005808   
    l2d_tlb_refill:u   | 76232       | 40999051   
    ll_cache:u         | 51746318    | 82462187   
    ll_cache_miss:u    | 1179666     | 75598171   
combined_orders:
    id        | modules                                                                                                          
    ----------+------------------------------------------------------------------------------------------------------------------
    canonical | cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8+itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17
    shuffle   | itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17+cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8
    sum       | cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8+itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 33442511722 | 33865544631 | 36084970660
    instructions:u     | 4109532325  | 4109532170  | 4109541452 
    br_retired:u       | 245641807   | 245641785   | 245642662  
    br_mis_pred:u      | 37505523    | 37557439    | 37499494   
    l1i_cache:u        | 972514490   | 1034377012  | 1029733667 
    l1i_cache_refill:u | 415036087   | 415228525   | 412284011  
    l1i_tlb:u          | 972514490   | 1034377012  | 1029733667 
    l1i_tlb_refill:u   | 25892350    | 25892251    | 25882313   
    l2i_cache:u        | 415035858   | 415228286   | 412283797  
    l2i_cache_refill:u | 414849198   | 415020070   | 412114361  
    l2i_tlb:u          | 25910233    | 25897457    | 30446476   
    l2i_tlb_refill:u   | 19863608    | 20029246    | 19826436   
    l1d_cache:u        | 831024121   | 830653082   | 831898020  
    l1d_cache_refill:u | 72820037    | 72092019    | 62120314   
    l1d_tlb:u          | 919956127   | 920038501   | 930141999  
    l1d_tlb_refill:u   | 41634905    | 41634776    | 41635892   
    l2d_cache:u        | 755918639   | 755261680   | 813515393  
    l2d_cache_refill:u | 554322479   | 556606627   | 548915697  
    l2d_tlb:u          | 41643724    | 41644130    | 41642515   
    l2d_tlb_refill:u   | 41004205    | 41007753    | 41075283   
    ll_cache:u         | 135665150   | 135023543   | 134208505  
    ll_cache_miss:u    | 80252426    | 81250566    | 76777837   

### Combined Memory Layouts
#### canonical: `cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8+itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=67112960 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67182592 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f2048_l2_d0_dtlb_64m_ps_n65536_p16384_np4_l1_r100_sp17_main_b15000_d4_lin_hot_4k_ns_n512_p1_np512_l4_r100_sn8: `itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17+cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=67112960 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67182592 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b15000_d4_linear_hot_4k_nstr_n512_p1_np512_l4_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4096 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=69632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_008_s2

### Selected Cases
- `cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2`: `blocks=1000`, `data_level=128k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=32`, `data_pool_nodes=16384`, `data_stride_lines=2`, `data_stride_nodes=2`, `data_template=cold`, `direct_run_len=8`, `fusion_ldr_per_unit=1`, `layout=in_page_shuffle`, `region_reps=100`
- `hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4`: `branch_pairs_per_unit=4`, `data_level=1m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=256`, `data_pool_nodes=131072`, `data_stride_lines=4`, `data_stride_nodes=4`, `data_template=cold`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=4096`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2+hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4`

### Results
single_modules:
    id | module                                                     
    ---+------------------------------------------------------------
    s0 | cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2
    s1 | hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4    
single_counts:
    metric             | s0        | s1      
    -------------------+-----------+---------
    cpu-cycles:u       | 265230094 | 14972660
    instructions:u     | 184061098 | 11921049
    br_retired:u       | 12571413  | 2661410 
    br_mis_pred:u      | 1250410   | 493     
    l1i_cache:u        | 42248555  | 1576576 
    l1i_cache_refill:u | 17076400  | 636     
    l1i_tlb:u          | 42248555  | 1576576 
    l1i_tlb_refill:u   | 683       | 53      
    l2i_cache:u        | 17076389  | 636     
    l2i_cache_refill:u | 3347      | 605     
    l2i_tlb:u          | 718       | 190     
    l2i_tlb_refill:u   | 13        | 23      
    l1d_cache:u        | 16358298  | 1415477 
    l1d_cache_refill:u | 521637    | 139384  
    l1d_tlb:u          | 16525254  | 1455547 
    l1d_tlb_refill:u   | 68766     | 13367   
    l2d_cache:u        | 33229052  | 2433077 
    l2d_cache_refill:u | 11858     | 602195  
    l2d_tlb:u          | 68838     | 13390   
    l2d_tlb_refill:u   | 9         | 30      
    ll_cache:u         | 8736      | 601499  
    ll_cache_miss:u    | 180       | 443     
combined_orders:
    id        | modules                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------
    canonical | cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2+hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4
    shuffle   | hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4+cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2
    sum       | cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2+hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 237217288 | 215994939 | 280202754
    instructions:u     | 195971313 | 195971307 | 195982147
    br_retired:u       | 15231604  | 15231606  | 15232823 
    br_mis_pred:u      | 1260215   | 1250850   | 1250903  
    l1i_cache:u        | 42964006  | 42255239  | 43825131 
    l1i_cache_refill:u | 11043117  | 11210216  | 17077036 
    l1i_tlb:u          | 42964006  | 42255239  | 43825131 
    l1i_tlb_refill:u   | 904       | 857       | 736      
    l2i_cache:u        | 11043110  | 11210209  | 17077025 
    l2i_cache_refill:u | 288383    | 37877     | 3952     
    l2i_tlb:u          | 1921      | 929       | 908      
    l2i_tlb_refill:u   | 42        | 63        | 36       
    l1d_cache:u        | 17786424  | 17783875  | 17773775 
    l1d_cache_refill:u | 722613    | 761606    | 661021   
    l1d_tlb:u          | 17987233  | 17986574  | 17980801 
    l1d_tlb_refill:u   | 82582     | 82585     | 82133    
    l2d_cache:u        | 25842112  | 27622925  | 35662129 
    l2d_cache_refill:u | 1039485   | 940154    | 614053   
    l2d_tlb:u          | 82609     | 82617     | 82228    
    l2d_tlb_refill:u   | 53        | 79        | 39       
    ll_cache:u         | 1002341   | 889233    | 610235   
    ll_cache_miss:u    | 240       | 1087      | 623      

### Combined Memory Layouts
#### canonical: `cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2+hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1179648 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1249280 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp4_cold_1m_ns_n131072_p256_np512_l2_r100_sn4_main_b1000_d8_bitrev_cold_128k_ns_n16384_p32_np512_l1_r100_sn2: `hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4+cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1179648 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1249280 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b1000_d8_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=131072 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=196608 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp4_r100_cold_1m_nstr_n131072_p256_np512_l2_sn4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1048576 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1114112 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_009_s2

### Selected Cases
- `cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2`: `blocks=11000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=8192`, `data_pool_nodes=32768`, `data_stride_pages=2`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=0`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=65536`, `data_pool_nodes=262144`, `data_stride_pages=65`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2+fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65`

### Results
single_modules:
    id | module                                                             
    ---+--------------------------------------------------------------------
    s0 | cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2        
    s1 | fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65
single_counts:
    metric             | s0          | s1       
    -------------------+-------------+----------
    cpu-cycles:u       | 36859941354 | 414764252
    instructions:u     | 3080311957  | 13590948 
    br_retired:u       | 330071597   | 1031390  
    br_mis_pred:u      | 110651664   | 130668   
    l1i_cache:u        | 1755879993  | 3562984  
    l1i_cache_refill:u | 226390400   | 963      
    l1i_tlb:u          | 1755879993  | 3562984  
    l1i_tlb_refill:u   | 3575316     | 41       
    l2i_cache:u        | 226390244   | 962      
    l2i_cache_refill:u | 226378851   | 859      
    l2i_tlb:u          | 3619421     | 89       
    l2i_tlb_refill:u   | 3573455     | 38       
    l1d_cache:u        | 700078897   | 2180565  
    l1d_cache_refill:u | 153391323   | 1278513  
    l1d_tlb:u          | 1278177627  | 4853971  
    l1d_tlb_refill:u   | 111746365   | 1305046  
    l2d_cache:u        | 1126789298  | 7327756  
    l2d_cache_refill:u | 580991321   | 3641313  
    l2d_tlb:u          | 112398521   | 1305113  
    l2d_tlb_refill:u   | 111186315   | 1282587  
    ll_cache:u         | 343002691   | 3188637  
    ll_cache_miss:u    | 93504451    | 2879123  
combined_orders:
    id        | modules                                                                                                                        
    ----------+--------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2+fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65
    shuffle   | fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65+cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2
    sum       | cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2+fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 39230492861 | 39333127903 | 37274705606
    instructions:u     | 3093892272  | 3093892299  | 3093902905 
    br_retired:u       | 331101799   | 331101803   | 331102987  
    br_mis_pred:u      | 110335922   | 110372271   | 110782332  
    l1i_cache:u        | 1621085863  | 1616317271  | 1759442977 
    l1i_cache_refill:u | 223074340   | 223101913   | 226391363  
    l1i_tlb:u          | 1621085863  | 1616317271  | 1759442977 
    l1i_tlb_refill:u   | 3566607     | 3566447     | 3575357    
    l2i_cache:u        | 223074160   | 223101751   | 226391206  
    l2i_cache_refill:u | 223049839   | 223077529   | 226379710  
    l2i_tlb:u          | 6990267     | 6988635     | 3619510    
    l2i_tlb_refill:u   | 3566002     | 3565499     | 3573493    
    l1d_cache:u        | 712036658   | 712644512   | 702259462  
    l1d_cache_refill:u | 147715251   | 150393191   | 154669836  
    l1d_tlb:u          | 1328580131  | 1328136979  | 1283031598 
    l1d_tlb_refill:u   | 113067460   | 113075496   | 113051411  
    l2d_cache:u        | 1125237935  | 1127547539  | 1134117054 
    l2d_cache_refill:u | 580304449   | 575934748   | 584632634  
    l2d_tlb:u          | 113843527   | 113816450   | 113703634  
    l2d_tlb_refill:u   | 112564324   | 112460641   | 112468902  
    ll_cache:u         | 349315613   | 344219368   | 346191328  
    ll_cache_miss:u    | 96552362    | 96056381    | 96383574   

### Combined Memory Layouts
#### canonical: `cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2+fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=301989888 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=302059520 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d4_bp0_s16_dtlb_256m_ps_n262144_p65536_np4_l2_r100_sp65_main_b11000_d1_lin_dtlb_32m_ps_n32768_p8192_np4_l1_r100_sp2: `fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65+cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=301989888 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=302059520 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b11000_d1_linear_dtlb_32m_pstr_n32768_p8192_np4_l1_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b64_d4_bp0_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l2_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_010_s2

### Selected Cases
- `hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2`: `branch_pairs_per_unit=2`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=16384`, `data_pool_nodes=32768`, `data_stride_pages=2`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=8192`
- `itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4`: `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=4096`, `data_pool_nodes=4096`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=0`, `funcs=256`, `fusion_ldr_per_unit=4`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2+itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4`

### Results
single_modules:
    id | module                                                  
    ---+---------------------------------------------------------
    s0 | hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2
    s1 | itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4  
single_counts:
    metric             | s0        | s1        
    -------------------+-----------+-----------
    cpu-cycles:u       | 384083333 | 1950354203
    instructions:u     | 22160951  | 51610951  
    br_retired:u       | 2661393   | 2651393   
    br_mis_pred:u      | 456       | 589       
    l1i_cache:u        | 2891966   | 6521297   
    l1i_cache_refill:u | 1024      | 7001935   
    l1i_tlb:u          | 2891966   | 6521297   
    l1i_tlb_refill:u   | 42        | 2590044   
    l2i_cache:u        | 1023      | 7001930   
    l2i_cache_refill:u | 700       | 6223432   
    l2i_tlb:u          | 135       | 2590117   
    l2i_tlb_refill:u   | 39        | 1614626   
    l1d_cache:u        | 1419111   | 10376035  
    l1d_cache_refill:u | 1278567   | 10236681  
    l1d_tlb:u          | 4113325   | 30925790  
    l1d_tlb_refill:u   | 1307188   | 10266866  
    l2d_cache:u        | 6519561   | 60412854  
    l2d_cache_refill:u | 2608030   | 26932486  
    l2d_tlb:u          | 1308306   | 10267121  
    l2d_tlb_refill:u   | 1283059   | 10208816  
    ll_cache:u         | 2586087   | 20524323  
    ll_cache_miss:u    | 2358445   | 6688      
combined_orders:
    id        | modules                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------
    canonical | hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2+itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4
    shuffle   | itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4+hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2
    sum       | hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2+itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 2379833973 | 2383620628 | 2334437536
    instructions:u     | 73761242   | 73761242   | 73771902  
    br_retired:u       | 5311592    | 5311592    | 5312786   
    br_mis_pred:u      | 521        | 506        | 1045      
    l1i_cache:u        | 9402009    | 9434412    | 9413263   
    l1i_cache_refill:u | 7149541    | 7148146    | 7002959   
    l1i_tlb:u          | 9402009    | 9434412    | 9413263   
    l1i_tlb_refill:u   | 2590256    | 2590267    | 2590086   
    l2i_cache:u        | 7149532    | 7148141    | 7002953   
    l2i_cache_refill:u | 6326846    | 6255411    | 6224132   
    l2i_tlb:u          | 2590423    | 2590353    | 2590252   
    l2i_tlb_refill:u   | 1629254    | 1641802    | 1614665   
    l1d_cache:u        | 11791010   | 11790682   | 11795146  
    l1d_cache_refill:u | 11512911   | 11513001   | 11515248  
    l1d_tlb:u          | 35029580   | 35022390   | 35039115  
    l1d_tlb_refill:u   | 11571083   | 11571101   | 11574054  
    l2d_cache:u        | 67423231   | 67427772   | 66932415  
    l2d_cache_refill:u | 29830017   | 29803329   | 29540516  
    l2d_tlb:u          | 11572140   | 11572060   | 11575427  
    l2d_tlb_refill:u   | 11496019   | 11494118   | 11491875  
    ll_cache:u         | 23215760   | 23248836   | 23110410  
    ll_cache_miss:u    | 2721741    | 2727048    | 2365133   

### Combined Memory Layouts
#### canonical: `hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2+itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=83886080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=83955712 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l1_d0_dtlb_16m_ps_n4096_p4096_np1_l4_r100_sp4_hot_s8192_bp2_dtlb_64m_ps_n32768_p16384_np2_l1_r100_sp2: `itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4+hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=83886080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=83955712 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l1_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_011_s2

### Selected Cases
- `cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17`: `blocks=11000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=17`, `data_template=dtlb`, `direct_run_len=16`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7`: `branch_pairs_per_unit=4`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=7`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=4096`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17+hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7`

### Results
single_modules:
    id | module                                                      
    ---+-------------------------------------------------------------
    s0 | cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17
    s1 | hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7       
single_counts:
    metric             | s0          | s1       
    -------------------+-------------+----------
    cpu-cycles:u       | 58073619475 | 261828498
    instructions:u     | 2055992071  | 11921098 
    br_retired:u       | 123831612   | 2661413  
    br_mis_pred:u      | 6890899     | 401      
    l1i_cache:u        | 448889599   | 1593084  
    l1i_cache_refill:u | 226066080   | 817      
    l1i_tlb:u          | 448889599   | 1593084  
    l1i_tlb_refill:u   | 3682503     | 41       
    l2i_cache:u        | 226065962   | 817      
    l2i_cache_refill:u | 225804868   | 537      
    l2i_tlb:u          | 6982062     | 84       
    l2i_tlb_refill:u   | 3680763     | 40       
    l1d_cache:u        | 254507116   | 1418903  
    l1d_cache_refill:u | 228395140   | 1279744  
    l1d_tlb:u          | 695299040   | 4102137  
    l1d_tlb_refill:u   | 220314071   | 1309624  
    l2d_cache:u        | 1395888630  | 6497331  
    l2d_cache_refill:u | 722124271   | 2601624  
    l2d_tlb:u          | 220320980   | 1310220  
    l2d_tlb_refill:u   | 219926542   | 1282822  
    ll_cache:u         | 481250864   | 2565205  
    ll_cache_miss:u    | 134929869   | 648864   
combined_orders:
    id        | modules                                                                                                           
    ----------+-------------------------------------------------------------------------------------------------------------------
    canonical | cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17+hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7
    shuffle   | hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7+cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17
    sum       | cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17+hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 59011490238 | 58949672550 | 58335447973
    instructions:u     | 2067902328  | 2067902344  | 2067913169 
    br_retired:u       | 126491807   | 126491808   | 126493025  
    br_mis_pred:u      | 6888116     | 6890325     | 6891300    
    l1i_cache:u        | 443814174   | 443813201   | 450482683  
    l1i_cache_refill:u | 227535858   | 227540008   | 226066897  
    l1i_tlb:u          | 443814174   | 443813201   | 450482683  
    l1i_tlb_refill:u   | 3682571     | 3682503     | 3682544    
    l2i_cache:u        | 227535712   | 227539881   | 226066779  
    l2i_cache_refill:u | 227367424   | 227306543   | 225805405  
    l2i_tlb:u          | 6975103     | 6975776     | 6982146    
    l2i_tlb_refill:u   | 3681679     | 3681764     | 3680803    
    l1d_cache:u        | 255945668   | 255932303   | 255926019  
    l1d_cache_refill:u | 227569094   | 229406001   | 229674884  
    l1d_tlb:u          | 699541480   | 699445440   | 699401177  
    l1d_tlb_refill:u   | 221624577   | 221624642   | 221623695  
    l2d_cache:u        | 1406112768  | 1400115194  | 1402385961 
    l2d_cache_refill:u | 718992285   | 723712938   | 724725895  
    l2d_tlb:u          | 221635097   | 221635979   | 221631200  
    l2d_tlb_refill:u   | 221170584   | 221225073   | 221209364  
    ll_cache:u         | 476595342   | 481341158   | 483816069  
    ll_cache_miss:u    | 139040970   | 139168972   | 135578733  

### Combined Memory Layouts
#### canonical: `cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17+hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67178496 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp4_dtlb_32m_ps_n8192_p8192_np1_l2_r100_sp7_main_b11000_d16_lin_dtlb_32m_ps_n8192_p8192_np1_l2_r100_sp17: `hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7+cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67178496 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b11000_d16_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_012_s2

### Selected Cases
- `cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2`: `blocks=19000`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=2`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=131072`, `data_pool_nodes=524288`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=0`, `funcs=1024`, `fusion_ldr_per_unit=2`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2+itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3`

### Results
single_modules:
    id | module                                                       
    ---+--------------------------------------------------------------
    s0 | cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2
    s1 | itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3 
single_counts:
    metric             | s0           | s1         
    -------------------+--------------+------------
    cpu-cycles:u       | 148944795000 | 15991170482
    instructions:u     | 3942811953   | 369050729  
    br_retired:u       | 285071597    | 10331330   
    br_mis_pred:u      | 47512661     | 2726       
    l1i_cache:u        | 1224597691   | 46281479   
    l1i_cache_refill:u | 397139864    | 40930599   
    l1i_tlb:u          | 1224597691   | 46281479   
    l1i_tlb_refill:u   | 6367830      | 10310094   
    l2i_cache:u        | 397139652    | 40930611   
    l2i_cache_refill:u | 397129290    | 40929109   
    l2i_tlb:u          | 12160019     | 10311404   
    l2i_tlb_refill:u   | 6356153      | 10065658   
    l1d_cache:u        | 621228818    | 41111471   
    l1d_cache_refill:u | 407666757    | 40935117   
    l1d_tlb:u          | 1405632596   | 123240133  
    l1d_tlb_refill:u   | 381004776    | 41000361   
    l2d_cache:u        | 2578142933   | 260598137  
    l2d_cache_refill:u | 1388359028   | 138809368  
    l2d_tlb:u          | 381017115    | 41008255   
    l2d_tlb_refill:u   | 380841853    | 40994582   
    ll_cache:u         | 852509850    | 82513600   
    ll_cache_miss:u    | 739504102    | 78118356   
combined_orders:
    id        | modules                                                                                                                   
    ----------+---------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2+itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3
    shuffle   | itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3+cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2
    sum       | cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2+itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 162564430652 | 164109684872 | 164935965482
    instructions:u     | 4311852363   | 4311852285   | 4311862682  
    br_retired:u       | 295401820    | 295401809    | 295402927   
    br_mis_pred:u      | 47519920     | 47514939     | 47515387    
    l1i_cache:u        | 1203883288   | 1170980042   | 1270879170  
    l1i_cache_refill:u | 439949431    | 439902257    | 438070463   
    l1i_tlb:u          | 1203883288   | 1170980042   | 1270879170  
    l1i_tlb_refill:u   | 16673789     | 16674406     | 16677924    
    l2i_cache:u        | 439949217    | 439902089    | 438070263   
    l2i_cache_refill:u | 439874051    | 439826951    | 438058399   
    l2i_tlb:u          | 16693027     | 16690600     | 22471423    
    l2i_tlb_refill:u   | 16441400     | 16431020     | 16421811    
    l1d_cache:u        | 661756938    | 661703054    | 662340289   
    l1d_cache_refill:u | 460456320    | 460345201    | 448601874   
    l1d_tlb:u          | 1524300340   | 1524142348   | 1528872729  
    l1d_tlb_refill:u   | 422026008    | 422026419    | 422005137   
    l2d_cache:u        | 2812339850   | 2812772004   | 2838741070  
    l2d_cache_refill:u | 1528370213   | 1528223252   | 1527168396  
    l2d_tlb:u          | 422061760    | 422067263    | 422025370   
    l2d_tlb_refill:u   | 421862042    | 421863219    | 421836435   
    ll_cache:u         | 930201114    | 930070268    | 935023450   
    ll_cache_miss:u    | 812982172    | 815024565    | 817622458   

### Combined Memory Layouts
#### canonical: `cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2+itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1610612736 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1610682368 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f1024_l2_d0_dtlb_512m_ps_n524288_p131072_np4_l2_r100_sp3_main_b19000_d4_lin_dtlb_1g_ps_n262144_p262144_np1_l2_r100_sp2: `itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3+cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1610612736 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1610682368 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b19000_d4_linear_dtlb_1g_pstr_n262144_p262144_np1_l2_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f1024_l2_r100_dtlb_512m_pstr_n524288_p131072_np4_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_013_s2

### Selected Cases
- `hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1`: `branch_pairs_per_unit=4`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=1`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=131072`, `data_pool_nodes=262144`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=4`, `funcs=512`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1+itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4`

### Results
single_modules:
    id | module                                                     
    ---+------------------------------------------------------------
    s0 | hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1
    s1 | itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4
single_counts:
    metric             | s0        | s1        
    -------------------+-----------+-----------
    cpu-cycles:u       | 187134326 | 4158956045
    instructions:u     | 11280997  | 106540723 
    br_retired:u       | 2661404   | 7751332   
    br_mis_pred:u      | 411       | 1274003   
    l1i_cache:u        | 1509334   | 27760947  
    l1i_cache_refill:u | 748       | 15072077  
    l1i_tlb:u          | 1509334   | 27760947  
    l1i_tlb_refill:u   | 49        | 5248128   
    l2i_cache:u        | 749       | 15072070  
    l2i_cache_refill:u | 605       | 14515683  
    l2i_tlb:u          | 142       | 5259259   
    l2i_tlb_refill:u   | 48        | 3219624   
    l1d_cache:u        | 777872    | 16899987  
    l1d_cache_refill:u | 640342    | 10402661  
    l1d_tlb:u          | 2181492   | 37862399  
    l1d_tlb_refill:u   | 669789    | 10300092  
    l2d_cache:u        | 3289232   | 75566771  
    l2d_cache_refill:u | 1384882   | 45644962  
    l2d_tlb:u          | 670206    | 10300882  
    l2d_tlb_refill:u   | 641419    | 10265666  
    ll_cache:u         | 1305128   | 24872202  
    ll_cache_miss:u    | 1236217   | 22722594  
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1+itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4
    shuffle   | itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4+hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1
    sum       | hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1+itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 4409982907 | 4420056189 | 4346090371
    instructions:u     | 117811020  | 117811020  | 117821720 
    br_retired:u       | 10411529   | 10411529   | 10412736  
    br_mis_pred:u      | 1274807    | 1273443    | 1274414   
    l1i_cache:u        | 29421158   | 29768039   | 29270281  
    l1i_cache_refill:u | 15050290   | 15047159   | 15072825  
    l1i_tlb:u          | 29421158   | 29768039   | 29270281  
    l1i_tlb_refill:u   | 5267770    | 5267712    | 5248177   
    l2i_cache:u        | 15050282   | 15047152   | 15072819  
    l2i_cache_refill:u | 14559708   | 14494116   | 14516288  
    l2i_tlb:u          | 5279700    | 5278308    | 5259401   
    l2i_tlb_refill:u   | 3207524    | 3202434    | 3219672   
    l1d_cache:u        | 17692388   | 17685251   | 17677859  
    l1d_cache_refill:u | 10971725   | 10960862   | 11043003  
    l1d_tlb:u          | 40354336   | 40246517   | 40043891  
    l1d_tlb_refill:u   | 11000396   | 10979081   | 10969881  
    l2d_cache:u        | 76819996   | 76774625   | 78856003  
    l2d_cache_refill:u | 45263587   | 45136605   | 47029844  
    l2d_tlb:u          | 11003895   | 10981444   | 10971088  
    l2d_tlb_refill:u   | 10927251   | 10913856   | 10907085  
    ll_cache:u         | 24334207   | 24300954   | 26177330  
    ll_cache_miss:u    | 22470952   | 22444939   | 23958811  

### Combined Memory Layouts
#### canonical: `hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1+itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073811456 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f512_l1_d4_dtlb_512m_ps_n262144_p131072_np2_l2_r100_sp4_hot_s4096_bp4_dtlb_512m_ps_n1048576_p131072_np8_l1_r100_sp1: `itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4+hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073811456 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l1_r100_dtlb_512m_pstr_n262144_p131072_np2_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_014_s2

### Selected Cases
- `cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257`: `blocks=5000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=1`, `layout=in_page_shuffle`, `region_reps=100`
- `hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33`: `branch_pairs_per_unit=2`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=32768`, `data_pool_nodes=262144`, `data_stride_pages=33`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257+hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33`

### Results
single_modules:
    id | module                                                      
    ---+-------------------------------------------------------------
    s0 | cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257
    s1 | hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33  
single_counts:
    metric             | s0          | s1       
    -------------------+-------------+----------
    cpu-cycles:u       | 15155343758 | 196592465
    instructions:u     | 919060729   | 11281003 
    br_retired:u       | 62571330    | 1381402  
    br_mis_pred:u      | 6253917     | 488      
    l1i_cache:u        | 255480957   | 1514513  
    l1i_cache_refill:u | 99225541    | 896      
    l1i_tlb:u          | 255480957   | 1514513  
    l1i_tlb_refill:u   | 2213696     | 40       
    l2i_cache:u        | 99225459    | 895      
    l2i_cache_refill:u | 82013787    | 656      
    l2i_tlb:u          | 2216691     | 97       
    l2i_tlb_refill:u   | 1362543     | 37       
    l1d_cache:u        | 81362430    | 777730   
    l1d_cache_refill:u | 54874433    | 640035   
    l1d_tlb:u          | 181818197   | 2189644  
    l1d_tlb_refill:u   | 50181354    | 667182   
    l2d_cache:u        | 392237708   | 3253705  
    l2d_cache_refill:u | 209181929   | 1317040  
    l2d_tlb:u          | 50189579    | 667820   
    l2d_tlb_refill:u   | 49851196    | 641330   
    ll_cache:u         | 126062013   | 1285214  
    ll_cache_miss:u    | 35956806    | 1219913  
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257+hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33
    shuffle   | hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33+cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257
    sum       | cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257+hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 15657872304 | 15283982076 | 15351936223
    instructions:u     | 930331023   | 930331036   | 930341732  
    br_retired:u       | 63951532    | 63951532    | 63952732   
    br_mis_pred:u      | 6253728     | 6258389     | 6254405    
    l1i_cache:u        | 263754041   | 254528350   | 256995470  
    l1i_cache_refill:u | 98772436    | 98869326    | 99226437   
    l1i_tlb:u          | 263754041   | 254528350   | 256995470  
    l1i_tlb_refill:u   | 2213595     | 2213639     | 2213736    
    l2i_cache:u        | 98772369    | 98869258    | 99226354   
    l2i_cache_refill:u | 83015623    | 74835178    | 82014443   
    l2i_tlb:u          | 2863387     | 2850900     | 2216788    
    l2i_tlb_refill:u   | 1355400     | 1383935     | 1362580    
    l1d_cache:u        | 82145367    | 82148221    | 82140160   
    l1d_cache_refill:u | 55467167    | 56183192    | 55514468   
    l1d_tlb:u          | 183985101   | 184089035   | 184007841  
    l1d_tlb_refill:u   | 50860643    | 50860309    | 50848536   
    l2d_cache:u        | 393321214   | 390910113   | 395491413  
    l2d_cache_refill:u | 210823135   | 206872533   | 210498969  
    l2d_tlb:u          | 50867698    | 50867308    | 50857399   
    l2d_tlb_refill:u   | 50437381    | 50605839    | 50492526   
    ll_cache:u         | 126804915   | 128382534   | 127347227  
    ll_cache_miss:u    | 39058071    | 39268515    | 37176719   

### Combined Memory Layouts
#### canonical: `cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257+hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=167772160 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=167841792 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp2_dtlb_128m_ps_n262144_p32768_np8_l1_r100_sp33_main_b5000_d8_bitrev_dtlb_32m_ps_n65536_p8192_np8_l1_r100_sp257: `hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33+cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=167772160 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=167841792 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b5000_d8_bitrev_dtlb_32m_pstr_n65536_p8192_np8_l1_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_015_s2

### Selected Cases
- `fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=4`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=16384`, `data_pool_nodes=16384`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3`: `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=4096`, `data_pool_nodes=4096`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=0`, `funcs=512`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4+itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3`

### Results
single_modules:
    id | module                                                          
    ---+-----------------------------------------------------------------
    s0 | fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4
    s1 | itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3          
single_counts:
    metric             | s0        | s1        
    -------------------+-----------+-----------
    cpu-cycles:u       | 774130420 | 2324874189
    instructions:u     | 20150942  | 92570951  
    br_retired:u       | 4551392   | 5211393   
    br_mis_pred:u      | 593007    | 623       
    l1i_cache:u        | 8780438   | 11703943  
    l1i_cache_refill:u | 1359      | 14587886  
    l1i_tlb:u          | 8780438   | 11703943  
    l1i_tlb_refill:u   | 52        | 5160048   
    l2i_cache:u        | 1358      | 14587876  
    l2i_cache_refill:u | 724       | 13984372  
    l2i_tlb:u          | 108       | 5160386   
    l2i_tlb_refill:u   | 41        | 3766840   
    l1d_cache:u        | 6049115   | 10381177  
    l1d_cache_refill:u | 2565267   | 10235865  
    l1d_tlb:u          | 13354800  | 31013112  
    l1d_tlb_refill:u   | 2602557   | 10280030  
    l2d_cache:u        | 14375312  | 70528809  
    l2d_cache_refill:u | 6234879   | 34729166  
    l2d_tlb:u          | 2610247   | 10282710  
    l2d_tlb_refill:u   | 2567624   | 10252522  
    ll_cache:u         | 6180998   | 20546192  
    ll_cache_miss:u    | 5243410   | 12338     
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4+itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3
    shuffle   | itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3+fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4
    sum       | fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4+itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 3201922402 | 3200872656 | 3099004609
    instructions:u     | 112711023  | 112711038  | 112721893 
    br_retired:u       | 9761532    | 9761531    | 9762785   
    br_mis_pred:u      | 630319     | 608233     | 593630    
    l1i_cache:u        | 21850347   | 21909313   | 20484381  
    l1i_cache_refill:u | 14589391   | 14634785   | 14589245  
    l1i_tlb:u          | 21850347   | 21909313   | 20484381  
    l1i_tlb_refill:u   | 5170255    | 5170247    | 5160100   
    l2i_cache:u        | 14589402   | 14634817   | 14589234  
    l2i_cache_refill:u | 13907739   | 13968873   | 13985096  
    l2i_tlb:u          | 5172047    | 5172713    | 5160494   
    l2i_tlb_refill:u   | 3730855    | 3709376    | 3766881   
    l1d_cache:u        | 16376346   | 16330972   | 16430292  
    l1d_cache_refill:u | 12794184   | 12790039   | 12801132  
    l1d_tlb:u          | 44347978   | 44090091   | 44367912  
    l1d_tlb_refill:u   | 12899156   | 12901966   | 12882587  
    l2d_cache:u        | 84898309   | 84831601   | 84904121  
    l2d_cache_refill:u | 40997499   | 41019001   | 40964045  
    l2d_tlb:u          | 12907901   | 12908236   | 12892957  
    l2d_tlb_refill:u   | 12824092   | 12831866   | 12820146  
    ll_cache:u         | 26835820   | 26715531   | 26727190  
    ll_cache_miss:u    | 6374203    | 6339393    | 5255748   

### Combined Memory Layouts
#### canonical: `fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4+itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=83886080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=83955712 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f512_l1_d0_dtlb_16m_ps_n4096_p4096_np1_l2_r100_sp3_fetch_b64_d1_bp4_s16_dtlb_64m_ps_n16384_p16384_np1_l4_r100_sp4: `itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3+fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=83886080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=83955712 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d1_bp4_s16_r100_dtlb_64m_pstr_n16384_p16384_np1_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_016_s2

### Selected Cases
- `hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3`: `branch_pairs_per_unit=4`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=131072`, `data_pool_nodes=262144`, `data_stride_pages=3`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5`: `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=16384`, `data_pool_nodes=65536`, `data_stride_pages=5`, `data_template=dtlb`, `direct_run_len=4`, `funcs=4096`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3+itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5`

### Results
single_modules:
    id | module                                                    
    ---+-----------------------------------------------------------
    s0 | hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3
    s1 | itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5 
single_counts:
    metric             | s0        | s1         
    -------------------+-----------+------------
    cpu-cycles:u       | 203174037 | 38361876873
    instructions:u     | 11280997  | 1505581954 
    br_retired:u       | 2661404   | 61511596   
    br_mis_pred:u      | 425       | 10235688   
    l1i_cache:u        | 1510746   | 318232057  
    l1i_cache_refill:u | 799       | 163423943  
    l1i_tlb:u          | 1510746   | 318232057  
    l1i_tlb_refill:u   | 42        | 41908029   
    l2i_cache:u        | 796       | 163423921  
    l2i_cache_refill:u | 764       | 162977537  
    l2i_tlb:u          | 81        | 41916214   
    l2i_tlb_refill:u   | 38        | 41075824   
    l1d_cache:u        | 778321    | 133225378  
    l1d_cache_refill:u | 641246    | 84496982   
    l1d_tlb:u          | 2212274   | 298187659  
    l1d_tlb_refill:u   | 679867    | 82139323   
    l2d_cache:u        | 3260827   | 650926543  
    l2d_cache_refill:u | 1527196   | 348454952  
    l2d_tlb:u          | 680409    | 82142479   
    l2d_tlb_refill:u   | 642483    | 82114160   
    ll_cache:u         | 1285668   | 180252228  
    ll_cache_miss:u    | 1216035   | 160473986  
combined_orders:
    id        | modules                                                                                                             
    ----------+---------------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3+itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5
    shuffle   | itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5+hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3
    sum       | hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3+itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 38755517398 | 38772057154 | 38565050910
    instructions:u     | 1516852248  | 1516852224  | 1516862951 
    br_retired:u       | 64171796    | 64171793    | 64173000   
    br_mis_pred:u      | 10233816    | 10234309    | 10236113   
    l1i_cache:u        | 322983991   | 322089612   | 319742803  
    l1i_cache_refill:u | 163280595   | 163330923   | 163424742  
    l1i_tlb:u          | 322983991   | 322089612   | 319742803  
    l1i_tlb_refill:u   | 41917470    | 41917313    | 41908071   
    l2i_cache:u        | 163280528   | 163330850   | 163424717  
    l2i_cache_refill:u | 162912765   | 162962537   | 162978301  
    l2i_tlb:u          | 41923329    | 41922470    | 41916295   
    l2i_tlb_refill:u   | 41108865    | 41110179    | 41075862   
    l1d_cache:u        | 134013753   | 134006326   | 134003699  
    l1d_cache_refill:u | 85179459    | 85156950    | 85138228   
    l1d_tlb:u          | 300421920   | 300274651   | 300399933  
    l1d_tlb_refill:u   | 82820599    | 82838918    | 82819190   
    l2d_cache:u        | 654313885   | 658194281   | 654187370  
    l2d_cache_refill:u | 350379654   | 354599678   | 349982148  
    l2d_tlb:u          | 82829281    | 82844829    | 82822888   
    l2d_tlb_refill:u   | 82756197    | 82767724    | 82756643   
    ll_cache:u         | 181653838   | 186051694   | 181537896  
    ll_cache_miss:u    | 162038412   | 165199565   | 161690021  

### Combined Memory Layouts
#### canonical: `hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3+itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=603979776 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=604049408 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f4096_l2_d4_dtlb_64m_ps_n65536_p16384_np4_l1_r100_sp5_hot_s4096_bp4_dtlb_512m_ps_n262144_p131072_np2_l1_r100_sp3: `itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5+hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=603979776 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=604049408 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l2_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_017_s2

### Selected Cases
- `cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4`: `blocks=6000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=2`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4`: `branch_pairs_per_unit=3`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=65536`, `data_pool_nodes=262144`, `data_stride_pages=4`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4`

### Results
single_modules:
    id | module                                                    
    ---+-----------------------------------------------------------
    s0 | cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4 
    s1 | hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 30981047556 | 1588051185
    instructions:u     | 1410311957  | 26000951  
    br_retired:u       | 120071597   | 3941393   
    br_mis_pred:u      | 30192590    | 555       
    l1i_cache:u        | 578870767   | 3433872   
    l1i_cache_refill:u | 126576512   | 4025      
    l1i_tlb:u          | 578870767   | 3433872   
    l1i_tlb_refill:u   | 2023758     | 46        
    l2i_cache:u        | 126576480   | 4024      
    l2i_cache_refill:u | 122763062   | 4004      
    l2i_tlb:u          | 2031282     | 173       
    l2i_tlb_refill:u   | 2022614     | 43        
    l1d_cache:u        | 271753236   | 5270438   
    l1d_cache_refill:u | 131327009   | 5118189   
    l1d_tlb:u          | 521963884   | 15641496  
    l1d_tlb_refill:u   | 120430334   | 5145399   
    l2d_cache:u        | 830097454   | 26044141  
    l2d_cache_refill:u | 403124931   | 11672011  
    l2d_tlb:u          | 120492484   | 5148608   
    l2d_tlb_refill:u   | 120277854   | 5127330   
    ll_cache:u         | 275204810   | 10306423  
    ll_cache_miss:u    | 83465367    | 9755777   
combined_orders:
    id        | modules                                                                                                             
    ----------+---------------------------------------------------------------------------------------------------------------------
    canonical | cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4
    shuffle   | hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4+cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4
    sum       | cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 32318956760 | 32606886089 | 32569098741
    instructions:u     | 1436302297  | 1436302351  | 1436312908 
    br_retired:u       | 124011801   | 124011809   | 124012990  
    br_mis_pred:u      | 30022376    | 30002832    | 30193145   
    l1i_cache:u        | 508994825   | 505570557   | 582304639  
    l1i_cache_refill:u | 126958526   | 126754153   | 126580537  
    l1i_tlb:u          | 508994825   | 505570557   | 582304639  
    l1i_tlb_refill:u   | 2028565     | 2029108     | 2023804    
    l2i_cache:u        | 126958459   | 126754106   | 126580504  
    l2i_cache_refill:u | 119683171   | 123821057   | 122767066  
    l2i_tlb:u          | 2038825     | 2035582     | 2031455    
    l2i_tlb_refill:u   | 2027243     | 2027822     | 2022657    
    l1d_cache:u        | 279423140   | 277177422   | 277023674  
    l1d_cache_refill:u | 134531534   | 138229677   | 136445198  
    l1d_tlb:u          | 552692069   | 536051457   | 537605380  
    l1d_tlb_refill:u   | 125585138   | 125593272   | 125575733  
    l2d_cache:u        | 849432130   | 854144620   | 856141595  
    l2d_cache_refill:u | 410620963   | 418378971   | 414796942  
    l2d_tlb:u          | 125599423   | 125654336   | 125641092  
    l2d_tlb_refill:u   | 125399683   | 125414914   | 125405184  
    ll_cache:u         | 280608131   | 286785049   | 285511233  
    ll_cache_miss:u    | 90449739    | 91925326    | 93221144   

### Combined Memory Layouts
#### canonical: `cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=301989888 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=302059520 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s8192_bp3_dtlb_256m_ps_n262144_p65536_np4_l4_r100_sp4_main_b6000_d2_lin_dtlb_32m_ps_n8192_p8192_np1_l2_r100_sp4: `hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4+cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=301989888 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=302059520 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b6000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp3_r100_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_018_s2

### Selected Cases
- `hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65`: `branch_pairs_per_unit=2`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=16384`, `data_pool_nodes=16384`, `data_stride_pages=65`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9`: `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=16384`, `data_pool_nodes=131072`, `data_stride_pages=9`, `data_template=dtlb`, `direct_run_len=4`, `funcs=1024`, `fusion_ldr_per_unit=4`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65+itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9`

### Results
single_modules:
    id | module                                                    
    ---+-----------------------------------------------------------
    s0 | hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65  
    s1 | itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9
single_counts:
    metric             | s0        | s1         
    -------------------+-----------+------------
    cpu-cycles:u       | 193629585 | 14019918526
    instructions:u     | 11280997  | 233260729  
    br_retired:u       | 1381404   | 15431330   
    br_mis_pred:u      | 450       | 2570734    
    l1i_cache:u        | 1517153   | 58039193   
    l1i_cache_refill:u | 835       | 30426093   
    l1i_tlb:u          | 1517153   | 58039193   
    l1i_tlb_refill:u   | 40        | 10514238   
    l2i_cache:u        | 835       | 30426087   
    l2i_cache_refill:u | 600       | 30326458   
    l2i_tlb:u          | 145       | 10529628   
    l2i_tlb_refill:u   | 36        | 10291382   
    l1d_cache:u        | 776828    | 54200799   
    l1d_cache_refill:u | 639816    | 41069866   
    l1d_tlb:u          | 2209754   | 137260918  
    l1d_tlb_refill:u   | 677423    | 41050747   
    l2d_cache:u        | 3252202   | 258046402  
    l2d_cache_refill:u | 1307632   | 120846858  
    l2d_tlb:u          | 678051    | 41068970   
    l2d_tlb_refill:u   | 642299    | 41030572   
    ll_cache:u         | 1284568   | 87871351   
    ll_cache_miss:u    | 1174481   | 77052150   
combined_orders:
    id        | modules                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65+itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9
    shuffle   | itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9+hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65
    sum       | hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65+itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 14273982852 | 14374228064 | 14213548111
    instructions:u     | 244531014   | 244531014   | 244541726  
    br_retired:u       | 16811531    | 16811531    | 16812734   
    br_mis_pred:u      | 2561438     | 2567921     | 2571184    
    l1i_cache:u        | 59782298    | 60117404    | 59556346   
    l1i_cache_refill:u | 30225527    | 30353961    | 30426928   
    l1i_tlb:u          | 59782298    | 60117404    | 59556346   
    l1i_tlb_refill:u   | 10516878    | 10516750    | 10514278   
    l2i_cache:u        | 30225517    | 30353965    | 30426922   
    l2i_cache_refill:u | 30167376    | 30270100    | 30327058   
    l2i_tlb:u          | 10535495    | 10531024    | 10529773   
    l2i_tlb_refill:u   | 10277848    | 10282486    | 10291418   
    l1d_cache:u        | 54992517    | 54991225    | 54977627   
    l1d_cache_refill:u | 41712147    | 41704949    | 41709682   
    l1d_tlb:u          | 139431170   | 139595916   | 139470672  
    l1d_tlb_refill:u   | 41719532    | 41740463    | 41728170   
    l2d_cache:u        | 261114143   | 266452902   | 261298604  
    l2d_cache_refill:u | 121999695   | 126431048   | 122154490  
    l2d_tlb:u          | 41728607    | 41750348    | 41747021   
    l2d_tlb_refill:u   | 41662349    | 41673469    | 41672871   
    ll_cache:u         | 89067578    | 93301988    | 89155919   
    ll_cache_miss:u    | 78646293    | 80129583    | 78226631   

### Combined Memory Layouts
#### canonical: `hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65+itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134287360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f1024_l1_d4_dtlb_64m_ps_n131072_p16384_np8_l4_r100_sp9_hot_s4096_bp2_dtlb_64m_ps_n16384_p16384_np1_l1_r100_sp65: `itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9+hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134287360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l1_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f1024_l1_r100_dtlb_64m_pstr_n131072_p16384_np8_l4_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_019_s2

### Selected Cases
- `hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129`: `branch_pairs_per_unit=3`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=65536`, `data_pool_nodes=131072`, `data_stride_pages=129`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64`: `data_level=4m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1024`, `data_pool_nodes=524288`, `data_stride_lines=64`, `data_stride_nodes=64`, `data_template=cold`, `direct_run_len=4`, `funcs=256`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129+itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64`

### Results
single_modules:
    id | module                                                     
    ---+------------------------------------------------------------
    s0 | hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129
    s1 | itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64 
single_counts:
    metric             | s0        | s1       
    -------------------+-----------+----------
    cpu-cycles:u       | 808332677 | 508414311
    instructions:u     | 13200957  | 53420951 
    br_retired:u       | 2021391   | 3911393  
    br_mis_pred:u      | 458       | 634644   
    l1i_cache:u        | 1803125   | 13797500 
    l1i_cache_refill:u | 1670      | 7328054  
    l1i_tlb:u          | 1803125   | 13797500 
    l1i_tlb_refill:u   | 39        | 2633381  
    l2i_cache:u        | 1669      | 7328046  
    l2i_cache_refill:u | 920       | 6224959  
    l2i_tlb:u          | 112       | 2634118  
    l2i_tlb_refill:u   | 36        | 81808    
    l1d_cache:u        | 2705868   | 8435198  
    l1d_cache_refill:u | 2558291   | 1716222  
    l1d_tlb:u          | 7949452   | 9745113  
    l1d_tlb_refill:u   | 2585431   | 680115   
    l2d_cache:u        | 13143703  | 33196936 
    l2d_cache_refill:u | 5909523   | 19170413 
    l2d_tlb:u          | 2587804   | 680154   
    l2d_tlb_refill:u   | 2564259   | 314669   
    ll_cache:u         | 5178343   | 12955074 
    ll_cache_miss:u    | 4906644   | 79820    
combined_orders:
    id        | modules                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129+itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64
    shuffle   | itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64+hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129
    sum       | hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129+itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 1420784578 | 1412714077 | 1316746988
    instructions:u     | 66611248   | 66611242   | 66621908  
    br_retired:u       | 5931590    | 5931592    | 5932784   
    br_mis_pred:u      | 631017     | 631090     | 635102    
    l1i_cache:u        | 15590450   | 15441882   | 15600625  
    l1i_cache_refill:u | 7365176    | 7397297    | 7329724   
    l1i_tlb:u          | 15590450   | 15441882   | 15600625  
    l1i_tlb_refill:u   | 2633525    | 2633546    | 2633420   
    l2i_cache:u        | 7365176    | 7397296    | 7329715   
    l2i_cache_refill:u | 6294232    | 6481109    | 6225879   
    l2i_tlb:u          | 2643618    | 2643690    | 2634230   
    l2i_tlb_refill:u   | 124011     | 126114     | 81844     
    l1d_cache:u        | 11147291   | 11143282   | 11141066  
    l1d_cache_refill:u | 4227520    | 4211905    | 4274513   
    l1d_tlb:u          | 17868516   | 17801218   | 17694565  
    l1d_tlb_refill:u   | 3266671    | 3256611    | 3265546   
    l2d_cache:u        | 48804996   | 48956922   | 46340639  
    l2d_cache_refill:u | 27959279   | 28072926   | 25079936  
    l2d_tlb:u          | 3269292    | 3259281    | 3267958   
    l2d_tlb_refill:u   | 2957739    | 2957339    | 2878928   
    ll_cache:u         | 20398202   | 20348764   | 18133417  
    ll_cache_miss:u    | 7121565    | 7137103    | 4986464   

### Combined Memory Layouts
#### canonical: `hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129+itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=272629760 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=272699392 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l1_d4_cold_4m_ns_n524288_p1024_np512_l2_r100_sn64_hot_s4096_bp3_dtlb_256m_ps_n131072_p65536_np2_l4_r100_sp129: `itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64+hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=272629760 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=272699392 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4194304 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4259840 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_020_s2

### Selected Cases
- `fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=0`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=262144`, `data_pool_nodes=524288`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4`: `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=16384`, `data_pool_nodes=65536`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=4`, `funcs=256`, `fusion_ldr_per_unit=1`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257+itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4`

### Results
single_modules:
    id | module                                                              
    ---+---------------------------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257
    s1 | itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4            
single_counts:
    metric             | s0        | s1        
    -------------------+-----------+-----------
    cpu-cycles:u       | 488544638 | 1080891514
    instructions:u     | 36150942  | 50860951  
    br_retired:u       | 3911392   | 3911393   
    br_mis_pred:u      | 1236909   | 637581    
    l1i_cache:u        | 16951221  | 13094112  
    l1i_cache_refill:u | 1752      | 7344113   
    l1i_tlb:u          | 16951221  | 13094112  
    l1i_tlb_refill:u   | 45        | 2623446   
    l2i_cache:u        | 1757      | 7344110   
    l2i_cache_refill:u | 1723      | 6405662   
    l2i_tlb:u          | 100       | 2626333   
    l2i_tlb_refill:u   | 41        | 596369    
    l1d_cache:u        | 7949383   | 5895313   
    l1d_cache_refill:u | 1290140   | 2581465   
    l1d_tlb:u          | 14439053  | 11216023  
    l1d_tlb_refill:u   | 1322443   | 2602572   
    l2d_cache:u        | 7954350   | 23042661  
    l2d_cache_refill:u | 3872336   | 13351840  
    l2d_tlb:u          | 1331676   | 2602675   
    l2d_tlb_refill:u   | 1280592   | 2568817   
    ll_cache:u         | 3142409   | 6817449   
    ll_cache_miss:u    | 3023384   | 5700745   
combined_orders:
    id        | modules                                                                                                                      
    ----------+------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257+itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4
    shuffle   | itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4+fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257
    sum       | fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257+itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 1607157909 | 1596402686 | 1569436152
    instructions:u     | 87001257   | 87001251   | 87011893  
    br_retired:u       | 7821591    | 7821593    | 7822785   
    br_mis_pred:u      | 1868453    | 1868041    | 1874490   
    l1i_cache:u        | 32505882   | 32378621   | 30045333  
    l1i_cache_refill:u | 7447655    | 7387536    | 7345865   
    l1i_tlb:u          | 32505882   | 32378621   | 30045333  
    l1i_tlb_refill:u   | 2633757    | 2633784    | 2623491   
    l2i_cache:u        | 7447655    | 7387533    | 7345867   
    l2i_cache_refill:u | 6481264    | 6450865    | 6407385   
    l2i_tlb:u          | 2637288    | 2637909    | 2626433   
    l2i_tlb_refill:u   | 609307     | 606101     | 596410    
    l1d_cache:u        | 13795294   | 13801689   | 13844696  
    l1d_cache_refill:u | 3864220    | 3837504    | 3871605   
    l1d_tlb:u          | 25564487   | 25604642   | 25655076  
    l1d_tlb_refill:u   | 3920303    | 3909764    | 3925015   
    l2d_cache:u        | 30081352   | 29991841   | 30997011  
    l2d_cache_refill:u | 16724619   | 16528289   | 17224176  
    l2d_tlb:u          | 3929905    | 3919946    | 3934351   
    l2d_tlb_refill:u   | 3848419    | 3847174    | 3849409   
    ll_cache:u         | 9202347    | 8985663    | 9959858   
    ll_cache_miss:u    | 8395066    | 8261811    | 8724129   

### Combined Memory Layouts
#### canonical: `fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257+itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1140850688 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1140920320 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l1_d4_dtlb_64m_ps_n65536_p16384_np4_l1_r100_sp4_fetch_b128_d1_bp0_s16_dtlb_1g_ps_n524288_p262144_np2_l1_r100_sp257: `itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4+fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1140850688 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1140920320 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d1_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l1_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_dtlb_64m_pstr_n65536_p16384_np4_l1_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_021_s2

### Selected Cases
- `fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=1`, `data_level=4m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1024`, `data_pool_nodes=524288`, `data_stride_lines=256`, `data_stride_nodes=256`, `data_template=cold`, `direct_run_len=8`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8`: `data_level=16k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=4`, `data_pool_nodes=2048`, `data_stride_lines=8`, `data_stride_nodes=8`, `data_template=hot`, `direct_run_len=4`, `funcs=2048`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256+itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8`

### Results
single_modules:
    id | module                                                              
    ---+---------------------------------------------------------------------
    s0 | fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256
    s1 | itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8               
single_counts:
    metric             | s0       | s1        
    -------------------+----------+-----------
    cpu-cycles:u       | 74208940 | 5362461938
    instructions:u     | 23830988 | 752940714 
    br_retired:u       | 2951403  | 30791331  
    br_mis_pred:u      | 140590   | 5111079   
    l1i_cache:u        | 4717521  | 157763452 
    l1i_cache_refill:u | 1081     | 81518981  
    l1i_tlb:u          | 4717521  | 157763452 
    l1i_tlb_refill:u   | 44       | 20968599  
    l2i_cache:u        | 1080     | 81518974  
    l2i_cache_refill:u | 1064     | 81459657  
    l2i_tlb:u          | 99       | 20978770  
    l2i_tlb_refill:u   | 40       | 16964807  
    l1d_cache:u        | 2175938  | 66662003  
    l1d_cache_refill:u | 857501   | 551580    
    l1d_tlb:u          | 2987842  | 66758327  
    l1d_tlb_refill:u   | 662565   | 7365      
    l2d_cache:u        | 4966525  | 106721566 
    l2d_cache_refill:u | 2093093  | 82879232  
    l2d_tlb:u          | 663082   | 7391      
    l2d_tlb_refill:u   | 4553     | 7348      
    ll_cache:u         | 2091210  | 788363    
    ll_cache_miss:u    | 5841     | 12449     
combined_orders:
    id        | modules                                                                                                                   
    ----------+---------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256+itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8
    shuffle   | itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8+fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256
    sum       | fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256+itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 5514713861 | 5474785278 | 5436670878
    instructions:u     | 776761023  | 776761023  | 776771702 
    br_retired:u       | 33741532   | 33741532   | 33742734  
    br_mis_pred:u      | 5251431    | 5251973    | 5251669   
    l1i_cache:u        | 161033192  | 162988886  | 162480973 
    l1i_cache_refill:u | 81415984   | 81591002   | 81520062  
    l1i_tlb:u          | 161033192  | 162988886  | 162480973 
    l1i_tlb_refill:u   | 20968815   | 20969079   | 20968643  
    l2i_cache:u        | 81415955   | 81590986   | 81520054  
    l2i_cache_refill:u | 81373341   | 81549108   | 81460721  
    l2i_tlb:u          | 20979227   | 20979577   | 20978869  
    l2i_tlb_refill:u   | 17018218   | 17018188   | 16964847  
    l1d_cache:u        | 68839538   | 68844349   | 68837941  
    l1d_cache_refill:u | 1851890    | 1844047    | 1409081   
    l1d_tlb:u          | 69869092   | 69862692   | 69746169  
    l1d_tlb_refill:u   | 680916     | 680904     | 669930    
    l2d_cache:u        | 111455518  | 111790676  | 111688091 
    l2d_cache_refill:u | 85297901   | 85438150   | 84972325  
    l2d_tlb:u          | 681679     | 681471     | 670473    
    l2d_tlb_refill:u   | 222671     | 217938     | 11901     
    ll_cache:u         | 3175789    | 3237462    | 2879573   
    ll_cache_miss:u    | 88380      | 23096      | 18290     

### Combined Memory Layouts
#### canonical: `fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256+itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=4210688 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4280320 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f2048_l2_d4_hot_16k_ns_n2048_p4_np512_l1_r100_sn8_fetch_b128_d8_bp1_s16_cold_4m_ns_n524288_p1024_np512_l1_r100_sn256: `itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8+fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=4210688 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4280320 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d8_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn256`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4194304 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4259840 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l2_r100_hot_16k_nstr_n2048_p4_np512_l1_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16384 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=81920 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_022_s2

### Selected Cases
- `hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17`: `branch_pairs_per_unit=4`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=17`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=4096`
- `itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3`: `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=4096`, `data_pool_nodes=4096`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=0`, `funcs=512`, `fusion_ldr_per_unit=1`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17+itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3`

### Results
single_modules:
    id | module                                                
    ---+-------------------------------------------------------
    s0 | hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17
    s1 | itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3
single_counts:
    metric             | s0        | s1        
    -------------------+-----------+-----------
    cpu-cycles:u       | 262356175 | 1490420446
    instructions:u     | 11921098  | 87450957  
    br_retired:u       | 2661413   | 5211391   
    br_mis_pred:u      | 412       | 548       
    l1i_cache:u        | 1595078   | 11049711  
    l1i_cache_refill:u | 850       | 14686442  
    l1i_tlb:u          | 1595078   | 11049711  
    l1i_tlb_refill:u   | 41        | 5160042   
    l2i_cache:u        | 849       | 14686432  
    l2i_cache_refill:u | 537       | 13888237  
    l2i_tlb:u          | 74        | 5160269   
    l2i_tlb_refill:u   | 36        | 2580297   
    l1d_cache:u        | 1418778   | 5261202   
    l1d_cache_refill:u | 1279382   | 5117402   
    l1d_tlb:u          | 4096530   | 15650513  
    l1d_tlb_refill:u   | 1309632   | 5160164   
    l2d_cache:u        | 6499268   | 43292142  
    l2d_cache_refill:u | 2614990   | 24303627  
    l2d_tlb:u          | 1310181   | 5162430   
    l2d_tlb_refill:u   | 1278764   | 5134335   
    ll_cache:u         | 2571282   | 10292259  
    ll_cache_miss:u    | 659783    | 15861     
combined_orders:
    id        | modules                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17+itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3
    shuffle   | itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3+hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17
    sum       | hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17+itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 1928320693 | 1922375558 | 1752776621
    instructions:u     | 99361248   | 99361248   | 99372055  
    br_retired:u       | 7871590    | 7871590    | 7872804   
    br_mis_pred:u      | 629        | 647        | 960       
    l1i_cache:u        | 12667837   | 12662240   | 12644789  
    l1i_cache_refill:u | 14576198   | 14523410   | 14687292  
    l1i_tlb:u          | 12667837   | 12662240   | 12644789  
    l1i_tlb_refill:u   | 5160155    | 5160157    | 5160083   
    l2i_cache:u        | 14576198   | 14523414   | 14687281  
    l2i_cache_refill:u | 13985963   | 13795974   | 13888774  
    l2i_tlb:u          | 5160357    | 5160341    | 5160343   
    l2i_tlb_refill:u   | 2624195    | 2589408    | 2580333   
    l1d_cache:u        | 6678079    | 6677541    | 6679980   
    l1d_cache_refill:u | 6396609    | 6396250    | 6396784   
    l1d_tlb:u          | 19757536   | 19755530   | 19747043  
    l1d_tlb_refill:u   | 6479012    | 6479341    | 6469796   
    l2d_cache:u        | 49899074   | 49823745   | 49791410  
    l2d_cache_refill:u | 27156325   | 26937208   | 26918617  
    l2d_tlb:u          | 6483479    | 6483453    | 6472611   
    l2d_tlb_refill:u   | 6417075    | 6416843    | 6413099   
    ll_cache:u         | 12862172   | 12907212   | 12863541  
    ll_cache_miss:u    | 2871617    | 2891677    | 675644    

### Combined Memory Layouts
#### canonical: `hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17+itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=50331648 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=50401280 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f512_l1_d0_dtlb_16m_ps_n4096_p4096_np1_l1_r100_sp3_hot_s4096_bp4_dtlb_32m_ps_n8192_p8192_np1_l2_r100_sp17: `itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3+hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=50331648 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=50401280 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp4_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l1_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_023_s2

### Selected Cases
- `fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=1`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=8192`, `data_pool_nodes=32768`, `data_stride_pages=17`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129`: `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=32768`, `data_pool_nodes=131072`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=4`, `funcs=2048`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17+itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17
    s1 | itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129    
single_counts:
    metric             | s0         | s1         
    -------------------+------------+------------
    cpu-cycles:u       | 1080389907 | 16389369799
    instructions:u     | 39990948   | 425260723  
    br_retired:u       | 5191390    | 30791332   
    br_mis_pred:u      | 1256303    | 5132752    
    l1i_cache:u        | 17865589   | 109439111  
    l1i_cache_refill:u | 2981       | 60564384   
    l1i_tlb:u          | 17865589   | 109439111  
    l1i_tlb_refill:u   | 43         | 20967869   
    l2i_cache:u        | 2982       | 60564358   
    l2i_cache_refill:u | 1552       | 60519625   
    l2i_tlb:u          | 85         | 21013831   
    l2i_tlb_refill:u   | 41         | 20576540   
    l1d_cache:u        | 11868219   | 67229795   
    l1d_cache_refill:u | 5099723    | 41597919   
    l1d_tlb:u          | 26278207   | 150322135  
    l1d_tlb_refill:u   | 5162288    | 41092767   
    l2d_cache:u        | 28256309   | 306862872  
    l2d_cache_refill:u | 11860182   | 159056013  
    l2d_tlb:u          | 5172038    | 41101383   
    l2d_tlb_refill:u   | 5114813    | 41065207   
    ll_cache:u         | 11670186   | 94318354   
    ll_cache_miss:u    | 3340299    | 85824570   
combined_orders:
    id        | modules                                                                                                                        
    ----------+--------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17+itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129
    shuffle   | itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129+fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17
    sum       | fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17+itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 17960857858 | 17979859420 | 17469759706
    instructions:u     | 465241023   | 465241029   | 465251671  
    br_retired:u       | 35981532    | 35981530    | 35982722   
    br_mis_pred:u      | 6413500     | 6350928     | 6389055    
    l1i_cache:u        | 132226126   | 129887111   | 127304700  
    l1i_cache_refill:u | 60467574    | 60395401    | 60567365   
    l1i_tlb:u          | 132226126   | 129887111   | 127304700  
    l1i_tlb_refill:u   | 20972389    | 20972214    | 20967912   
    l2i_cache:u        | 60467551    | 60395375    | 60567340   
    l2i_cache_refill:u | 60434202    | 60350760    | 60521177   
    l2i_tlb:u          | 20991003    | 20989159    | 21013916   
    l2i_tlb_refill:u   | 20576187    | 20585868    | 20576581   
    l1d_cache:u        | 79482995    | 79313796    | 79098014   
    l1d_cache_refill:u | 46729683    | 46684231    | 46697642   
    l1d_tlb:u          | 177831798   | 177093485   | 176600342  
    l1d_tlb_refill:u   | 46288982    | 46271508    | 46255055   
    l2d_cache:u        | 339696794   | 337195743   | 335119181  
    l2d_cache_refill:u | 175770439   | 172765941   | 170916195  
    l2d_tlb:u          | 46306510    | 46286498    | 46273421   
    l2d_tlb_refill:u   | 46205168    | 46190200    | 46180020   
    ll_cache:u         | 109889823   | 107742797   | 105988540  
    ll_cache_miss:u    | 97071076    | 95944679    | 89164869   

### Combined Memory Layouts
#### canonical: `fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17+itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=167772160 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=167841792 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f2048_l1_d4_dtlb_128m_ps_n131072_p32768_np4_l2_r100_sp129_fetch_b128_d1_bp1_s16_dtlb_32m_ps_n32768_p8192_np4_l4_r100_sp17: `itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129+fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=167772160 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=167841792 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l1_r100_dtlb_128m_pstr_n131072_p32768_np4_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_024_s2

### Selected Cases
- `hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1`: `branch_pairs_per_unit=4`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=131072`, `data_pool_nodes=262144`, `data_stride_pages=1`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2`: `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=16384`, `data_pool_nodes=131072`, `data_stride_pages=2`, `data_template=dtlb`, `direct_run_len=4`, `funcs=256`, `fusion_ldr_per_unit=2`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1+itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2`

### Results
single_modules:
    id | module                                                    
    ---+-----------------------------------------------------------
    s0 | hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1
    s1 | itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2 
single_counts:
    metric             | s0        | s1        
    -------------------+-----------+-----------
    cpu-cycles:u       | 185281726 | 3666364688
    instructions:u     | 11280997  | 99500729  
    br_retired:u       | 2661404   | 3911330   
    br_mis_pred:u      | 428       | 633707    
    l1i_cache:u        | 1510824   | 20009753  
    l1i_cache_refill:u | 770       | 9880413   
    l1i_tlb:u          | 1510824   | 20009753  
    l1i_tlb_refill:u   | 48        | 2633387   
    l2i_cache:u        | 767       | 9880408   
    l2i_cache_refill:u | 612       | 9707092   
    l2i_tlb:u          | 96        | 2643150   
    l2i_tlb_refill:u   | 46        | 1729165   
    l1d_cache:u        | 777173    | 13560650  
    l1d_cache_refill:u | 642420    | 10257682  
    l1d_tlb:u          | 2181887   | 34226236  
    l1d_tlb_refill:u   | 669903    | 10281936  
    l2d_cache:u        | 3312176   | 64011704  
    l2d_cache_refill:u | 1383926   | 30793503  
    l2d_tlb:u          | 670294    | 10283201  
    l2d_tlb_refill:u   | 641581    | 10260770  
    ll_cache:u         | 1303022   | 20668771  
    ll_cache_miss:u    | 1229987   | 18881540  
combined_orders:
    id        | modules                                                                                                             
    ----------+---------------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1+itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2
    shuffle   | itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2+hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1
    sum       | hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1+itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 3849890793 | 3810780509 | 3851646414
    instructions:u     | 110771027  | 110771020  | 110781726 
    br_retired:u       | 6571531    | 6571529    | 6572734   
    br_mis_pred:u      | 647832     | 631212     | 634135    
    l1i_cache:u        | 21881693   | 21461787   | 21520577  
    l1i_cache_refill:u | 9919818    | 9833859    | 9881183   
    l1i_tlb:u          | 21881693   | 21461787   | 21520577  
    l1i_tlb_refill:u   | 2636093    | 2636041    | 2633435   
    l2i_cache:u        | 9919811    | 9833858    | 9881175   
    l2i_cache_refill:u | 9621233    | 8856040    | 9707704   
    l2i_tlb:u          | 2652129    | 2647572    | 2643246   
    l2i_tlb_refill:u   | 1749609    | 1755438    | 1729211   
    l1d_cache:u        | 14330106   | 14330292   | 14337823  
    l1d_cache_refill:u | 10902243   | 10929501   | 10900102  
    l1d_tlb:u          | 36344349   | 36375451   | 36408123  
    l1d_tlb_refill:u   | 10939467   | 10950241   | 10951839  
    l2d_cache:u        | 67055930   | 67765055   | 67323880  
    l2d_cache_refill:u | 31899468   | 31578898   | 32177429  
    l2d_tlb:u          | 10943950   | 10954668   | 10953495  
    l2d_tlb_refill:u   | 10897518   | 10901692   | 10902351  
    ll_cache:u         | 21873788   | 22317892   | 21971793  
    ll_cache_miss:u    | 19969487   | 20265459   | 20111527  

### Combined Memory Layouts
#### canonical: `hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1+itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=603979776 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=604049408 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l2_d4_dtlb_64m_ps_n131072_p16384_np8_l2_r100_sp2_hot_s4096_bp4_dtlb_512m_ps_n262144_p131072_np2_l1_r100_sp1: `itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2+hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=603979776 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=604049408 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp4_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l2_r100_dtlb_64m_pstr_n131072_p16384_np8_l2_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_025_s2

### Selected Cases
- `hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3`: `branch_pairs_per_unit=2`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=32768`, `data_pool_nodes=32768`, `data_stride_pages=3`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=8192`
- `itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=65`, `data_template=dtlb`, `direct_run_len=0`, `funcs=256`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3+itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65`

### Results
single_modules:
    id | module                                                       
    ---+--------------------------------------------------------------
    s0 | hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3    
    s1 | itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65
single_counts:
    metric             | s0        | s1        
    -------------------+-----------+-----------
    cpu-cycles:u       | 392034292 | 1958985076
    instructions:u     | 22160951  | 46490951  
    br_retired:u       | 2661393   | 2651393   
    br_mis_pred:u      | 503       | 541       
    l1i_cache:u        | 2894463   | 6078152   
    l1i_cache_refill:u | 1295      | 6974709   
    l1i_tlb:u          | 2894463   | 6078152   
    l1i_tlb_refill:u   | 55        | 2590065   
    l2i_cache:u        | 1295      | 6974707   
    l2i_cache_refill:u | 787       | 5847259   
    l2i_tlb:u          | 167       | 2590144   
    l2i_tlb_refill:u   | 51        | 1079718   
    l1d_cache:u        | 1419317   | 5257576   
    l1d_cache_refill:u | 1279513   | 5116272   
    l1d_tlb:u          | 4113895   | 15616071  
    l1d_tlb_refill:u   | 1307239   | 5146036   
    l2d_cache:u        | 6503361   | 35088498  
    l2d_cache_refill:u | 2596781   | 17816205  
    l2d_tlb:u          | 1308391   | 5146483   
    l2d_tlb_refill:u   | 1282707   | 5130661   
    ll_cache:u         | 2569182   | 10323687  
    ll_cache_miss:u    | 2436497   | 9784493   
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3+itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65
    shuffle   | itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65+hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3
    sum       | hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3+itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 2356187088 | 2363066998 | 2351019368
    instructions:u     | 68641242   | 68641242   | 68651902  
    br_retired:u       | 5311592    | 5311592    | 5312786   
    br_mis_pred:u      | 626        | 516        | 1044      
    l1i_cache:u        | 8930441    | 8878290    | 8972615   
    l1i_cache_refill:u | 7014383    | 7035598    | 6976004   
    l1i_tlb:u          | 8930441    | 8878290    | 8972615   
    l1i_tlb_refill:u   | 2590263    | 2590264    | 2590120   
    l2i_cache:u        | 7014379    | 7035589    | 6976002   
    l2i_cache_refill:u | 5946390    | 6126122    | 5848046   
    l2i_tlb:u          | 2590404    | 2590410    | 2590311   
    l2i_tlb_refill:u   | 1092521    | 1100854    | 1079769   
    l1d_cache:u        | 6673311    | 6673557    | 6676893   
    l1d_cache_refill:u | 6394144    | 6396201    | 6395785   
    l1d_tlb:u          | 19732862   | 19725391   | 19729966  
    l1d_tlb_refill:u   | 6455560    | 6453711    | 6453275   
    l2d_cache:u        | 41579362   | 41788026   | 41591859  
    l2d_cache_refill:u | 21171097   | 21414425   | 20412986  
    l2d_tlb:u          | 6457280    | 6455408    | 6454874   
    l2d_tlb_refill:u   | 6412125    | 6413031    | 6413368   
    ll_cache:u         | 12931003   | 13028231   | 12892869  
    ll_cache_miss:u    | 12239764   | 12311111   | 12220990  

### Combined Memory Layouts
#### canonical: `hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3+itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=671088640 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=671158272 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l1_d0_dtlb_512m_ps_n1048576_p131072_np8_l2_r100_sp65_hot_s8192_bp2_dtlb_128m_ps_n32768_p32768_np1_l1_r100_sp3: `itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65+hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=671088640 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=671158272 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l1_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_026_s2

### Selected Cases
- `cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2`: `blocks=7000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=2`, `data_template=dtlb`, `direct_run_len=16`, `fusion_ldr_per_unit=4`, `layout=in_page_shuffle`, `region_reps=100`
- `hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9`: `branch_pairs_per_unit=3`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=9`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2+hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9`

### Results
single_modules:
    id | module                                                      
    ---+-------------------------------------------------------------
    s0 | cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2  
    s1 | hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9
single_counts:
    metric             | s0          | s1       
    -------------------+-------------+----------
    cpu-cycles:u       | 64485145214 | 460397229
    instructions:u     | 1448492023  | 22160951 
    br_retired:u       | 78831606    | 3941393  
    br_mis_pred:u      | 4391933     | 448      
    l1i_cache:u        | 293173492   | 2897675  
    l1i_cache_refill:u | 153679174   | 1261     
    l1i_tlb:u          | 293173492   | 2897675  
    l1i_tlb_refill:u   | 3404822     | 41       
    l2i_cache:u        | 153679121   | 1260     
    l2i_cache_refill:u | 151106503   | 1222     
    l2i_tlb:u          | 3409568     | 109      
    l2i_tlb_refill:u   | 2502629     | 38       
    l1d_cache:u        | 302011812   | 1421532  
    l1d_cache_refill:u | 283453385   | 1283452  
    l1d_tlb:u          | 862839068   | 4098960  
    l1d_tlb_refill:u   | 280211897   | 1305150  
    l2d_cache:u        | 1611158468  | 6580378  
    l2d_cache_refill:u | 740196851   | 4029348  
    l2d_tlb:u          | 280220019   | 1306657  
    l2d_tlb_refill:u   | 280150032   | 1283035  
    ll_cache:u         | 584436995   | 2599287  
    ll_cache_miss:u    | 167728232   | 2465118  
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2+hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9
    shuffle   | hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9+cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2
    sum       | cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2+hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 65182252848 | 65937980243 | 64945542443
    instructions:u     | 1470642301  | 1470642328  | 1470652974 
    br_retired:u       | 82771803    | 82771807    | 82772999   
    br_mis_pred:u      | 4390692     | 4400594     | 4392381    
    l1i_cache:u        | 295630884   | 297579499   | 296071167  
    l1i_cache_refill:u | 153852766   | 154024823   | 153680435  
    l1i_tlb:u          | 295630884   | 297579499   | 296071167  
    l1i_tlb_refill:u   | 3405327     | 3406097     | 3404863    
    l2i_cache:u        | 153852691   | 154024744   | 153680381  
    l2i_cache_refill:u | 152118949   | 152085303   | 151107725  
    l2i_tlb:u          | 3422806     | 3428382     | 3409677    
    l2i_tlb_refill:u   | 2502789     | 2507611     | 2502667    
    l1d_cache:u        | 303440463   | 303436781   | 303433344  
    l1d_cache_refill:u | 285196567   | 286595731   | 284736837  
    l1d_tlb:u          | 866891895   | 866891072   | 866938028  
    l1d_tlb_refill:u   | 281518151   | 281518184   | 281517047  
    l2d_cache:u        | 1614643057  | 1612770289  | 1617738846 
    l2d_cache_refill:u | 744203761   | 747390966   | 744226199  
    l2d_tlb:u          | 281530595   | 281530492   | 281526676  
    l2d_tlb_refill:u   | 281398245   | 281457947   | 281433067  
    ll_cache:u         | 586529574   | 588579553   | 587036282  
    ll_cache_miss:u    | 169171387   | 159618837   | 170193350  

### Combined Memory Layouts
#### canonical: `cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2+hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=570425344 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=570494976 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s8192_bp3_dtlb_512m_ps_n1048576_p131072_np8_l1_r100_sp9_main_b7000_d16_bitrev_dtlb_32m_ps_n8192_p8192_np1_l4_r100_sp2: `hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9+cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=570425344 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=570494976 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b7000_d16_bitrev_dtlb_32m_pstr_n8192_p8192_np1_l4_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp3_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_027_s2

### Selected Cases
- `hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4`: `branch_pairs_per_unit=2`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=16384`, `data_pool_nodes=32768`, `data_stride_pages=4`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=8192`
- `itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17`: `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=17`, `data_template=dtlb`, `direct_run_len=4`, `funcs=4096`, `fusion_ldr_per_unit=1`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4+itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17`

### Results
single_modules:
    id | module                                                  
    ---+---------------------------------------------------------
    s0 | hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4
    s1 | itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17
single_counts:
    metric             | s0        | s1         
    -------------------+-----------+------------
    cpu-cycles:u       | 762771061 | 23501475998
    instructions:u     | 23440951  | 809260940  
    br_retired:u       | 2661393   | 61511388   
    br_mis_pred:u      | 473       | 10273158   
    l1i_cache:u        | 3078672   | 216848746  
    l1i_cache_refill:u | 1653      | 120702430  
    l1i_tlb:u          | 3078672   | 216848746  
    l1i_tlb_refill:u   | 49        | 41866801   
    l2i_cache:u        | 1652      | 120702908  
    l2i_cache_refill:u | 767       | 120645623  
    l2i_tlb:u          | 125       | 41878430   
    l2i_tlb_refill:u   | 45        | 40979467   
    l1d_cache:u        | 2701579   | 93630445   
    l1d_cache_refill:u | 2558208   | 42691045   
    l1d_tlb:u          | 7957575   | 179196747  
    l1d_tlb_refill:u   | 2586943   | 41193944   
    l2d_cache:u        | 13012106  | 389370551  
    l2d_cache_refill:u | 5207996   | 214550420  
    l2d_tlb:u          | 2588697   | 41206367   
    l2d_tlb_refill:u   | 2565527   | 41162645   
    ll_cache:u         | 5147384   | 90560961   
    ll_cache_miss:u    | 4684260   | 75803193   
combined_orders:
    id        | modules                                                                                                          
    ----------+------------------------------------------------------------------------------------------------------------------
    canonical | hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4+itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17
    shuffle   | itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17+hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4
    sum       | hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4+itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 24447771657 | 24459705517 | 24264247059
    instructions:u     | 832691237   | 832691237   | 832701891  
    br_retired:u       | 64171585    | 64171585    | 64172781   
    br_mis_pred:u      | 10271799    | 10268687    | 10273631   
    l1i_cache:u        | 220233195   | 221014802   | 219927418  
    l1i_cache_refill:u | 120799888   | 120662060   | 120704083  
    l1i_tlb:u          | 220233195   | 221014802   | 219927418  
    l1i_tlb_refill:u   | 41876619    | 41876543    | 41866850   
    l2i_cache:u        | 120800161   | 120662278   | 120704560  
    l2i_cache_refill:u | 120745911   | 120624230   | 120646390  
    l2i_tlb:u          | 41890356    | 41889851    | 41878555   
    l2i_tlb_refill:u   | 41011941    | 41034809    | 40979512   
    l1d_cache:u        | 96205708    | 96268908    | 96332024   
    l1d_cache_refill:u | 45496292    | 45357334    | 45249253   
    l1d_tlb:u          | 185771710   | 187028667   | 187154322  
    l1d_tlb_refill:u   | 43784754    | 43784484    | 43780887   
    l2d_cache:u        | 408992177   | 405361472   | 402382657  
    l2d_cache_refill:u | 226407228   | 221592246   | 219758416  
    l2d_tlb:u          | 43804107    | 43790219    | 43795064   
    l2d_tlb_refill:u   | 43717636    | 43716908    | 43728172   
    ll_cache:u         | 102230699   | 97540262    | 95708345   
    ll_cache_miss:u    | 82971725    | 81392011    | 80487453   

### Combined Memory Layouts
#### canonical: `hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4+itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=100663296 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=100732928 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f4096_l1_d4_dtlb_32m_ps_n8192_p8192_np1_l1_r100_sp17_hot_s8192_bp2_dtlb_64m_ps_n32768_p16384_np2_l2_r100_sp4: `itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17+hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=100663296 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=100732928 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b128_bp2_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_028_s2

### Selected Cases
- `fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=2`, `data_level=2k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1`, `data_pool_nodes=256`, `data_stride_lines=32`, `data_stride_nodes=32`, `data_template=hot`, `direct_run_len=4`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=131072`, `data_pool_nodes=131072`, `data_stride_pages=5`, `data_template=dtlb`, `direct_run_len=0`, `funcs=512`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32+itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5`

### Results
single_modules:
    id | module                                                     
    ---+------------------------------------------------------------
    s0 | fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32
    s1 | itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5
single_counts:
    metric             | s0       | s1        
    -------------------+----------+-----------
    cpu-cycles:u       | 16595417 | 5195785661
    instructions:u     | 14871049 | 174490750 
    br_retired:u       | 2311410  | 5211336   
    br_mis_pred:u      | 130636   | 659       
    l1i_cache:u        | 3975258  | 21931596  
    l1i_cache_refill:u | 703      | 20015594  
    l1i_tlb:u          | 3975258  | 21931596  
    l1i_tlb_refill:u   | 54       | 5160053   
    l2i_cache:u        | 702      | 20015581  
    l2i_cache_refill:u | 646      | 20015338  
    l2i_tlb:u          | 99       | 5160210   
    l2i_tlb_refill:u   | 35       | 3231823   
    l1d_cache:u        | 3455347  | 10380958  
    l1d_cache_refill:u | 171      | 10235618  
    l1d_tlb:u          | 3457302  | 31020385  
    l1d_tlb_refill:u   | 58       | 10279035  
    l2d_cache:u        | 1516     | 75513780  
    l2d_cache_refill:u | 1060     | 46911071  
    l2d_tlb:u          | 86       | 10281940  
    l2d_tlb_refill:u   | 26       | 10261736  
    ll_cache:u         | 385      | 20617601  
    ll_cache_miss:u    | 48       | 19455297  
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32+itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5
    shuffle   | itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5+fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32
    sum       | fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32+itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 4831674590 | 4829549939 | 5212381078
    instructions:u     | 189351036  | 189351023  | 189361799 
    br_retired:u       | 7521532    | 7521532    | 7522746   
    br_mis_pred:u      | 131098     | 130825     | 131295    
    l1i_cache:u        | 25888318   | 25912306   | 25906854  
    l1i_cache_refill:u | 20009310   | 19996349   | 20016297  
    l1i_tlb:u          | 25888318   | 25912306   | 25906854  
    l1i_tlb_refill:u   | 5170249    | 5170252    | 5160107   
    l2i_cache:u        | 20009299   | 19996338   | 20016283  
    l2i_cache_refill:u | 20008990   | 19996074   | 20015984  
    l2i_tlb:u          | 5172294    | 5175205    | 5160309   
    l2i_tlb_refill:u   | 3168662    | 3179625    | 3231858   
    l1d_cache:u        | 13832472   | 13832691   | 13836305  
    l1d_cache_refill:u | 10237909   | 10233347   | 10235789  
    l1d_tlb:u          | 34508395   | 34471966   | 34477687  
    l1d_tlb_refill:u   | 10293165   | 10280357   | 10279093  
    l2d_cache:u        | 75675304   | 75617643   | 75515296  
    l2d_cache_refill:u | 47057505   | 47110423   | 46912131  
    l2d_tlb:u          | 10293614   | 10280818   | 10282026  
    l2d_tlb_refill:u   | 10257426   | 10265790   | 10261762  
    ll_cache:u         | 20789512   | 20786342   | 20617986  
    ll_cache_miss:u    | 19675117   | 19521635   | 19455345  

### Combined Memory Layouts
#### canonical: `fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32+itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=536875008 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536944640 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f512_l2_d0_dtlb_512m_ps_n131072_p131072_np1_l1_r100_sp5_fetch_b64_d4_bp2_s16_hot_2k_ns_n256_p1_np512_l4_r100_sn32: `itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5+fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=536875008 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536944640 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l4_sn32`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4096 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=69632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_029_s2

### Selected Cases
- `hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8`: `branch_pairs_per_unit=3`, `data_level=2m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=512`, `data_pool_nodes=262144`, `data_stride_lines=8`, `data_stride_nodes=8`, `data_template=cold`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=8192`
- `itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048`: `data_level=512k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=128`, `data_pool_nodes=65536`, `data_stride_lines=2048`, `data_stride_nodes=2048`, `data_template=cold`, `direct_run_len=0`, `funcs=2048`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8+itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048`

### Results
single_modules:
    id | module                                                       
    ---+--------------------------------------------------------------
    s0 | hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8     
    s1 | itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048
single_counts:
    metric             | s0       | s1        
    -------------------+----------+-----------
    cpu-cycles:u       | 37988047 | 5803342875
    instructions:u     | 23440997 | 696730729 
    br_retired:u       | 3941404  | 20571330  
    br_mis_pred:u      | 477      | 1153      
    l1i_cache:u        | 3019610  | 87306990  
    l1i_cache_refill:u | 741      | 81633902  
    l1i_tlb:u          | 3019610  | 87306990  
    l1i_tlb_refill:u   | 50       | 20550066  
    l2i_cache:u        | 740      | 81633871  
    l2i_cache_refill:u | 722      | 81625277  
    l2i_tlb:u          | 106      | 20550497  
    l2i_tlb_refill:u   | 41       | 17493873  
    l1d_cache:u        | 2695629  | 41112247  
    l1d_cache_refill:u | 285650   | 40947600  
    l1d_tlb:u          | 2791905  | 44908191  
    l1d_tlb_refill:u   | 47926    | 2593082   
    l2d_cache:u        | 10364955 | 192619173 
    l2d_cache_refill:u | 2770788  | 91468781  
    l2d_tlb:u          | 48092    | 2601698   
    l2d_tlb_refill:u   | 601      | 1154557   
    ll_cache:u         | 2769681  | 9083746   
    ll_cache_miss:u    | 2979     | 132286    
combined_orders:
    id        | modules                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8+itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048
    shuffle   | itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048+hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8
    sum       | hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8+itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 6013251189 | 5851374038 | 5841330922
    instructions:u     | 720161014  | 720161027  | 720171726 
    br_retired:u       | 24511531   | 24511531   | 24512734  
    br_mis_pred:u      | 1313       | 1224       | 1630      
    l1i_cache:u        | 90265234   | 90261938   | 90326600  
    l1i_cache_refill:u | 81672247   | 81662694   | 81634643  
    l1i_tlb:u          | 90265234   | 90261938   | 90326600  
    l1i_tlb_refill:u   | 20550343   | 20550360   | 20550116  
    l2i_cache:u        | 81672197   | 81662652   | 81634611  
    l2i_cache_refill:u | 81668445   | 81656861   | 81625999  
    l2i_tlb:u          | 20551243   | 20551585   | 20550603  
    l2i_tlb_refill:u   | 17513457   | 17515197   | 17493914  
    l1d_cache:u        | 43805817   | 43805345   | 43807876  
    l1d_cache_refill:u | 41022516   | 41028041   | 41233250  
    l1d_tlb:u          | 47744901   | 47741402   | 47700096  
    l1d_tlb_refill:u   | 2641938    | 2641823    | 2641008   
    l2d_cache:u        | 210875772  | 207796250  | 202984128 
    l2d_cache_refill:u | 100509183  | 97447663   | 94239569  
    l2d_tlb:u          | 2651865    | 2651761    | 2649790   
    l2d_tlb_refill:u   | 1198515    | 1197139    | 1155158   
    ll_cache:u         | 17987470   | 15043133   | 11853427  
    ll_cache_miss:u    | 52918      | 340588     | 135265    

### Combined Memory Layouts
#### canonical: `hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8+itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=2621440 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2691072 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f2048_l2_d0_cold_512k_ns_n65536_p128_np512_l1_r100_sn2048_hot_s8192_bp3_cold_2m_ns_n262144_p512_np512_l2_r100_sn8: `itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048+hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=2621440 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2691072 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l2_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=2097152 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2162688 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l2_r100_cold_512k_nstr_n65536_p128_np512_l1_sn2048`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=524288 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=589824 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_030_s2

### Selected Cases
- `cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512`: `blocks=10000`, `data_level=128k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=32`, `data_pool_nodes=16384`, `data_stride_lines=512`, `data_stride_nodes=512`, `data_template=cold`, `direct_run_len=16`, `fusion_ldr_per_unit=1`, `layout=in_page_shuffle`, `region_reps=100`
- `itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17`: `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=262144`, `data_pool_nodes=1048576`, `data_stride_pages=17`, `data_template=dtlb`, `direct_run_len=0`, `funcs=4096`, `fusion_ldr_per_unit=4`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512+itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17`

### Results
single_modules:
    id | module                                                         
    ---+----------------------------------------------------------------
    s0 | cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512
    s1 | itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17   
single_counts:
    metric             | s0          | s1         
    -------------------+-------------+------------
    cpu-cycles:u       | 10659341607 | 78245236034
    instructions:u     | 1769060732  | 819611974  
    br_retired:u       | 112571333   | 41051599   
    br_mis_pred:u      | 6266694     | 9435       
    l1i_cache:u        | 393388175   | 102655478  
    l1i_cache_refill:u | 203102328   | 128309624  
    l1i_tlb:u          | 393388175   | 102655478  
    l1i_tlb_refill:u   | 4550205     | 41140239   
    l2i_cache:u        | 203102222   | 128309575  
    l2i_cache_refill:u | 201735053   | 128306444  
    l2i_tlb:u          | 4551390     | 41143186   
    l2i_tlb_refill:u   | 781         | 41102730   
    l1d_cache:u        | 131355487   | 163996249  
    l1d_cache_refill:u | 20564677    | 163737890  
    l1d_tlb:u          | 132538834   | 492022010  
    l1d_tlb_refill:u   | 622035      | 163896621  
    l2d_cache:u        | 288606253   | 1009395610 
    l2d_cache_refill:u | 227009145   | 644504084  
    l2d_tlb:u          | 624806      | 163905164  
    l2d_tlb_refill:u   | 155         | 163894043  
    ll_cache:u         | 24970509    | 328387657  
    ll_cache_miss:u    | 372212      | 306774506  
combined_orders:
    id        | modules                                                                                                                     
    ----------+-----------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512+itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17
    shuffle   | itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17+cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512
    sum       | cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512+itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 89390111637 | 89847932594 | 88904577641
    instructions:u     | 2588662295  | 2588662362  | 2588672706 
    br_retired:u       | 153621803   | 153621811   | 153622932  
    br_mis_pred:u      | 6273831     | 6273926     | 6276129    
    l1i_cache:u        | 495374173   | 496082498   | 496043653  
    l1i_cache_refill:u | 332020330   | 331881288   | 331411952  
    l1i_tlb:u          | 495374173   | 496082498   | 496043653  
    l1i_tlb_refill:u   | 45699880    | 45700212    | 45690444   
    l2i_cache:u        | 332020174   | 331881173   | 331411797  
    l2i_cache_refill:u | 331234893   | 330947646   | 330041497  
    l2i_tlb:u          | 45712266    | 45708532    | 45694576   
    l2i_tlb_refill:u   | 41144717    | 41142718    | 41103511   
    l1d_cache:u        | 295384143   | 295372516   | 295351736  
    l1d_cache_refill:u | 184382306   | 184590655   | 184302567  
    l1d_tlb:u          | 624568305   | 624673349   | 624560844  
    l1d_tlb_refill:u   | 164516217   | 164534306   | 164518656  
    l2d_cache:u        | 1296146204  | 1297032086  | 1298001863 
    l2d_cache_refill:u | 874425584   | 873845108   | 871513229  
    l2d_tlb:u          | 164542734   | 164560458   | 164529970  
    l2d_tlb_refill:u   | 163889755   | 163930503   | 163894198  
    ll_cache:u         | 355353490   | 356058215   | 353358166  
    ll_cache_miss:u    | 308041816   | 308451459   | 307146718  

### Combined Memory Layouts
#### canonical: `cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512+itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1073872896 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073942528 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f4096_l1_d0_dtlb_1g_ps_n1048576_p262144_np4_l4_r100_sp17_main_b10000_d16_bitrev_cold_128k_ns_n16384_p32_np512_l1_r100_sn512: `itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17+cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1073872896 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073942528 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b10000_d16_bitrev_cold_128k_nstr_n16384_p32_np512_l1_sn512`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=131072 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=196608 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l1_r100_dtlb_1g_pstr_n1048576_p262144_np4_l4_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_031_s2

### Selected Cases
- `fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=4`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=16384`, `data_pool_nodes=32768`, `data_stride_pages=9`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129`: `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=4`, `funcs=256`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9+itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9
    s1 | itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129      
single_counts:
    metric             | s0         | s1        
    -------------------+------------+-----------
    cpu-cycles:u       | 1533170105 | 2212804038
    instructions:u     | 27670948   | 53420951  
    br_retired:u       | 6791390    | 3911393   
    br_mis_pred:u      | 140618     | 645887    
    l1i_cache:u        | 5280280    | 13876044  
    l1i_cache_refill:u | 3964       | 7439769   
    l1i_tlb:u          | 5280280    | 13876044  
    l1i_tlb_refill:u   | 58         | 2633392   
    l2i_cache:u        | 3965       | 7439759   
    l2i_cache_refill:u | 1689       | 6536371   
    l2i_tlb:u          | 114        | 2640211   
    l2i_tlb_refill:u   | 56         | 1113395   
    l1d_cache:u        | 6021563    | 8466143   
    l1d_cache_refill:u | 5112165    | 5138189   
    l1d_tlb:u          | 16377519   | 19046762  
    l1d_tlb_refill:u   | 5145035    | 5163270   
    l2d_cache:u        | 28391678   | 36830141  
    l2d_cache_refill:u | 12457720   | 23513454  
    l2d_tlb:u          | 5148091    | 5163723   
    l2d_tlb_refill:u   | 5128649    | 5136769   
    ll_cache:u         | 12261858   | 11167408  
    ll_cache_miss:u    | 10589766   | 10517740  
combined_orders:
    id        | modules                                                                                                                      
    ----------+------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9+itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129
    shuffle   | itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129+fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9
    sum       | fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9+itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 3852613003 | 4051772212 | 3745974143
    instructions:u     | 81081029   | 81081023   | 81091899  
    br_retired:u       | 10701530   | 10701532   | 10702783  
    br_mis_pred:u      | 775351     | 772298     | 786505    
    l1i_cache:u        | 18852154   | 18900463   | 19156324  
    l1i_cache_refill:u | 7395623    | 7365246    | 7443733   
    l1i_tlb:u          | 18852154   | 18900463   | 19156324  
    l1i_tlb_refill:u   | 2633808    | 2633880    | 2633450   
    l2i_cache:u        | 7395625    | 7365243    | 7443724   
    l2i_cache_refill:u | 6574473    | 6521734    | 6538060   
    l2i_tlb:u          | 2645153    | 2645389    | 2640325   
    l2i_tlb_refill:u   | 1216999    | 1217873    | 1113451   
    l1d_cache:u        | 14486286   | 14476096   | 14487706  
    l1d_cache_refill:u | 10244026   | 10248370   | 10250354  
    l1d_tlb:u          | 35506317   | 35367894   | 35424281  
    l1d_tlb_refill:u   | 10320124   | 10315803   | 10308305  
    l2d_cache:u        | 65668624   | 64372872   | 65221819  
    l2d_cache_refill:u | 36578746   | 35490656   | 35971174  
    l2d_tlb:u          | 10323159   | 10319967   | 10311814  
    l2d_tlb_refill:u   | 10271565   | 10267780   | 10265418  
    ll_cache:u         | 23818363   | 22749729   | 23429266  
    ll_cache_miss:u    | 21757539   | 21086756   | 21107506  

### Combined Memory Layouts
#### canonical: `fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9+itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1140850688 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1140920320 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l1_d4_dtlb_1g_ps_n262144_p262144_np1_l2_r100_sp129_fetch_b128_d8_bp4_s16_dtlb_64m_ps_n32768_p16384_np2_l4_r100_sp9: `itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129+fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=1140850688 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1140920320 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d8_bp4_s16_r100_dtlb_64m_pstr_n32768_p16384_np2_l4_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_032_s2

### Selected Cases
- `hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16`: `branch_pairs_per_unit=2`, `data_level=4k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1`, `data_pool_nodes=512`, `data_stride_lines=16`, `data_stride_nodes=16`, `data_template=hot`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3`: `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=32768`, `data_pool_nodes=65536`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=4`, `funcs=512`, `fusion_ldr_per_unit=4`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16+itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3`

### Results
single_modules:
    id | module                                                   
    ---+----------------------------------------------------------
    s0 | hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16       
    s1 | itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3
single_counts:
    metric             | s0       | s1         
    -------------------+----------+------------
    cpu-cycles:u       | 12958834 | 13937200724
    instructions:u     | 13201040 | 219180723  
    br_retired:u       | 1381409  | 7751332    
    br_mis_pred:u      | 393      | 1271937    
    l1i_cache:u        | 1735851  | 44682368   
    l1i_cache_refill:u | 605      | 20354142   
    l1i_tlb:u          | 1735851  | 44682368   
    l1i_tlb_refill:u   | 48       | 5287608    
    l2i_cache:u        | 605      | 20354247   
    l2i_cache_refill:u | 514      | 20317193   
    l2i_tlb:u          | 90       | 5302862    
    l2i_tlb_refill:u   | 13       | 5033262    
    l1d_cache:u        | 2695296  | 47480079   
    l1d_cache_refill:u | 168      | 41029780   
    l1d_tlb:u          | 2697290  | 129633356  
    l1d_tlb_refill:u   | 58       | 41021687   
    l2d_cache:u        | 1382     | 242471797  
    l2d_cache_refill:u | 933      | 114060051  
    l2d_tlb:u          | 82       | 41023459   
    l2d_tlb_refill:u   | 7        | 41002394   
    ll_cache:u         | 371      | 90064828   
    ll_cache_miss:u    | 20       | 84101340   
combined_orders:
    id        | modules                                                                                                     
    ----------+-------------------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16+itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3
    shuffle   | itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3+hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16
    sum       | hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16+itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 13871000003 | 13891668141 | 13950159558
    instructions:u     | 232371014   | 232371020   | 232381763  
    br_retired:u       | 9131531     | 9131529     | 9132741    
    br_mis_pred:u      | 1271854     | 1273336     | 1272330    
    l1i_cache:u        | 44554248    | 44747009    | 46418219   
    l1i_cache_refill:u | 20318522    | 20339189    | 20354747   
    l1i_tlb:u          | 44554248    | 44747009    | 46418219   
    l1i_tlb_refill:u   | 5291291     | 5291295     | 5287656    
    l2i_cache:u        | 20318641    | 20339276    | 20354852   
    l2i_cache_refill:u | 20287717    | 20301882    | 20317707   
    l2i_tlb:u          | 5308085     | 5307482     | 5302952    
    l2i_tlb_refill:u   | 5041236     | 5025238     | 5033275    
    l1d_cache:u        | 50160163    | 50161156    | 50175375   
    l1d_cache_refill:u | 40994431    | 41014430    | 41029948   
    l1d_tlb:u          | 132324694   | 132321798   | 132330646  
    l1d_tlb_refill:u   | 41016602    | 41016800    | 41021745   
    l2d_cache:u        | 234728766   | 242931587   | 242473179  
    l2d_cache_refill:u | 104743120   | 112394462   | 114060984  
    l2d_tlb:u          | 41026960    | 41027024    | 41023541   
    l2d_tlb_refill:u   | 40998963    | 40996369    | 41002401   
    ll_cache:u         | 83038791    | 90535139    | 90065199   
    ll_cache_miss:u    | 78724244    | 84461502    | 84101360   

### Combined Memory Layouts
#### canonical: `hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16+itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=134221824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134291456 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f512_l2_d4_dtlb_128m_ps_n65536_p32768_np2_l4_r100_sp3_hot_s4096_bp2_hot_4k_ns_n512_p1_np512_l4_r100_sn16: `itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3+hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=134221824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134291456 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `hot_b64_bp2_r100_hot_4k_nstr_n512_p1_np512_l4_sn16`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4096 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=69632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_033_s2

### Selected Cases
- `cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8`: `blocks=18000`, `data_level=4k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1`, `data_pool_nodes=512`, `data_stride_lines=8`, `data_stride_nodes=8`, `data_template=hot`, `direct_run_len=4`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=4`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=1`, `data_template=dtlb`, `direct_run_len=2`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8+fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1`

### Results
single_modules:
    id | module                                                          
    ---+-----------------------------------------------------------------
    s0 | cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8          
    s1 | fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 16194214665 | 1039956143
    instructions:u     | 3555310723  | 32950942  
    br_retired:u       | 270071332   | 7751392   
    br_mis_pred:u      | 45010098    | 611188    
    l1i_cache:u        | 1011659842  | 12784584  
    l1i_cache_refill:u | 366928269   | 2917      
    l1i_tlb:u          | 1011659842  | 12784584  
    l1i_tlb_refill:u   | 5832732     | 57        
    l2i_cache:u        | 366928104   | 2914      
    l2i_cache_refill:u | 366798535   | 1981      
    l2i_tlb:u          | 5837800     | 116       
    l2i_tlb_refill:u   | 5163        | 48        
    l1d_cache:u        | 407663825   | 8542119   
    l1d_cache_refill:u | 35899074    | 5102248   
    l1d_tlb:u          | 416496041   | 19188065  
    l1d_tlb_refill:u   | 791584      | 5162671   
    l2d_cache:u        | 504972349   | 28793874  
    l2d_cache_refill:u | 431361410   | 12183978  
    l2d_tlb:u          | 794404      | 5167548   
    l2d_tlb_refill:u   | 12330       | 5135030   
    ll_cache:u         | 64549005    | 12138757  
    ll_cache_miss:u    | 3169116     | 3073967   
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8+fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1
    shuffle   | fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1+cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8
    sum       | cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8+fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 21020195038 | 21159984341 | 17234170808
    instructions:u     | 3588251231  | 3588251231  | 3588261665 
    br_retired:u       | 277821587   | 277821587   | 277822724  
    br_mis_pred:u      | 45612027    | 45626583    | 45621286   
    l1i_cache:u        | 1064677803  | 1074673277  | 1024444426 
    l1i_cache_refill:u | 364005413   | 363991747   | 366931186  
    l1i_tlb:u          | 1064677803  | 1074673277  | 1024444426 
    l1i_tlb_refill:u   | 5832386     | 5832665     | 5832789    
    l2i_cache:u        | 364005635   | 363991990   | 366931018  
    l2i_cache_refill:u | 363875737   | 363863655   | 366800516  
    l2i_tlb:u          | 11322628    | 11333285    | 5837916    
    l2i_tlb_refill:u   | 84305       | 86640       | 5211       
    l1d_cache:u        | 417136546   | 417869713   | 416205944  
    l1d_cache_refill:u | 41149414    | 30682704    | 41001322   
    l1d_tlb:u          | 443856710   | 446397093   | 435684106  
    l1d_tlb_refill:u   | 5986092     | 5966392     | 5954255    
    l2d_cache:u        | 581174832   | 596692436   | 533766223  
    l2d_cache_refill:u | 443906522   | 440937578   | 443545388  
    l2d_tlb:u          | 5995752     | 5971785     | 5961952    
    l2d_tlb_refill:u   | 5151541     | 5161209     | 5147360    
    ll_cache:u         | 81084475    | 78461303    | 76687762   
    ll_cache_miss:u    | 10020952    | 8804211     | 6243083    

### Combined Memory Layouts
#### canonical: `cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8+fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=33558528 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33628160 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d2_bp4_s16_dtlb_32m_ps_n65536_p8192_np8_l4_r100_sp1_main_b18000_d4_lin_hot_4k_ns_n512_p1_np512_l1_r100_sn8: `fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1+cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=33558528 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33628160 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b18000_d4_linear_hot_4k_nstr_n512_p1_np512_l1_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4096 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=69632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d2_bp4_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_034_s3

### Selected Cases
- `cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129`: `blocks=12000`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=131072`, `data_pool_nodes=524288`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=2`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=0`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=16384`, `data_pool_nodes=65536`, `data_stride_pages=33`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5`: `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=4096`, `data_pool_nodes=4096`, `data_stride_pages=5`, `data_template=dtlb`, `direct_run_len=0`, `funcs=1024`, `fusion_ldr_per_unit=2`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129+fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33+itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5`

### Results
single_modules:
    id | module                                                            
    ---+-------------------------------------------------------------------
    s0 | cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129 
    s1 | fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33
    s2 | itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5           
single_counts:
    metric             | s0           | s1         | s2        
    -------------------+--------------+------------+-----------
    cpu-cycles:u       | 108361738589 | 1541678542 | 9015904584
    instructions:u     | 2325312071   | 29430948   | 369050723 
    br_retired:u       | 150071612    | 1991390    | 10331332  
    br_mis_pred:u      | 15006114     | 290824     | 1479      
    l1i_cache:u        | 656216044    | 7588263    | 46313295  
    l1i_cache_refill:u | 251868508    | 3931       | 40863002  
    l1i_tlb:u          | 656216044    | 7588263    | 46313295  
    l1i_tlb_refill:u   | 5583889      | 43         | 10310047  
    l2i_cache:u        | 251868369    | 3931       | 40862980  
    l2i_cache_refill:u | 251337993    | 1880       | 40841328  
    l2i_tlb:u          | 5599470      | 90         | 10311121  
    l2i_tlb_refill:u   | 4118021      | 41         | 10275084  
    l1d_cache:u        | 315110241    | 6833734    | 41116061  
    l1d_cache_refill:u | 262007670    | 5116370    | 40945320  
    l1d_tlb:u          | 796860077    | 17208826   | 123083156 
    l1d_tlb_refill:u   | 240413703    | 5145120    | 41000467  
    l2d_cache:u        | 1615762765   | 28812443   | 259833194 
    l2d_cache_refill:u | 1029302251   | 12612486   | 124065457 
    l2d_tlb:u          | 240425111    | 5145353    | 41010749  
    l2d_tlb_refill:u   | 240382497    | 5127539    | 40874664  
    ll_cache:u         | 538997083    | 12406225   | 82113649  
    ll_cache_miss:u    | 475393181    | 10488409   | 57239     
combined_orders:
    id        | modules                                                                                                                                                                                     
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129+fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33+itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5
    shuffle   | itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5+cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129+fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33
    sum       | cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129+fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33+itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 120195146155 | 119536344395 | 118919321715
    instructions:u     | 2723772502   | 2723772623   | 2723793742  
    br_retired:u       | 162391990    | 162392006    | 162394334   
    br_mis_pred:u      | 15318708     | 15310418     | 15298417    
    l1i_cache:u        | 683934402    | 687890860    | 710117602   
    l1i_cache_refill:u | 293071755    | 293012257    | 292735441   
    l1i_tlb:u          | 683934402    | 687890860    | 710117602   
    l1i_tlb_refill:u   | 15894667     | 15894582     | 15893979    
    l2i_cache:u        | 293071559    | 293012072    | 292735280   
    l2i_cache_refill:u | 292464323    | 292377106    | 292181201   
    l2i_tlb:u          | 15905347     | 15908637     | 15910681    
    l2i_tlb_refill:u   | 14406161     | 14458103     | 14393146    
    l1d_cache:u        | 363073405    | 363051083    | 363060036   
    l1d_cache_refill:u | 299761032    | 308421993    | 308069360   
    l1d_tlb:u          | 937578287    | 937166714    | 937152059   
    l1d_tlb_refill:u   | 286599217    | 286580256    | 286559290   
    l2d_cache:u        | 1924302774   | 1905544932   | 1904408402  
    l2d_cache_refill:u | 1162346671   | 1167851853   | 1165980194  
    l2d_tlb:u          | 286624518    | 286604786    | 286581213   
    l2d_tlb_refill:u   | 286388748    | 286389280    | 286384700   
    ll_cache:u         | 631684493    | 634727090    | 633516957   
    ll_cache_miss:u    | 480875337    | 490662688    | 485938829   

### Combined Memory Layouts
#### canonical: `cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129+fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33+itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=620756992 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=620830720 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f1024_l2_d0_dtlb_16m_ps_n4096_p4096_np1_l2_r100_sp5_main_b12000_d8_bitrev_dtlb_512m_ps_n524288_p131072_np4_l2_r100_sp129_fetch_b128_d4_bp0_s16_dtlb_64m_ps_n65536_p16384_np4_l4_r100_sp33: `itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5+cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129+fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=620756992 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=620830720 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b12000_d8_bitrev_dtlb_512m_pstr_n524288_p131072_np4_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d4_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f1024_l2_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_035_s3

### Selected Cases
- `cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7`: `blocks=3000`, `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=4096`, `data_pool_nodes=8192`, `data_stride_pages=7`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=2`, `layout=in_page_shuffle`, `region_reps=100`
- `hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257`: `branch_pairs_per_unit=2`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=131072`, `data_pool_nodes=262144`, `data_stride_pages=257`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3`: `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=16384`, `data_pool_nodes=32768`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=4`, `funcs=256`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7+hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257+itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3`

### Results
single_modules:
    id | module                                                      
    ---+-------------------------------------------------------------
    s0 | cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7   
    s1 | hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257
    s2 | itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3    
single_counts:
    metric             | s0          | s1        | s2        
    -------------------+-------------+-----------+-----------
    cpu-cycles:u       | 10895290708 | 208642429 | 1868736034
    instructions:u     | 581560729   | 11281007  | 53420957  
    br_retired:u       | 37571330    | 1381406   | 3911391   
    br_mis_pred:u      | 3750921     | 467       | 645152    
    l1i_cache:u        | 146432459   | 1519428   | 13895562  
    l1i_cache_refill:u | 59814735    | 872       | 7398471   
    l1i_tlb:u          | 146432459   | 1519428   | 13895562  
    l1i_tlb_refill:u   | 1152433     | 39        | 2633425   
    l2i_cache:u        | 59814732    | 869       | 7398466   
    l2i_cache_refill:u | 21308517    | 773       | 6465671   
    l2i_tlb:u          | 1310973     | 115       | 2640224   
    l2i_tlb_refill:u   | 1024056     | 36        | 1132910   
    l1d_cache:u        | 78874912    | 777833    | 8457624   
    l1d_cache_refill:u | 60986882    | 639922    | 5131455   
    l1d_tlb:u          | 198681929   | 2189545   | 18897594  
    l1d_tlb_refill:u   | 60130394    | 667255    | 5162300   
    l2d_cache:u        | 393112727   | 3602180   | 36224502  
    l2d_cache_refill:u | 163656336   | 1463678   | 18369178  
    l2d_tlb:u          | 60142124    | 667928    | 5162498   
    l2d_tlb_refill:u   | 59428268    | 640863    | 5136350   
    ll_cache:u         | 143685201   | 1282809   | 11726237  
    ll_cache_miss:u    | 7208671     | 1266028   | 10474586  
combined_orders:
    id        | modules                                                                                                                                                                        
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7+hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257+itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3
    shuffle   | hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257+cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7+itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3
    sum       | cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7+hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257+itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 13244606443 | 13089124717 | 12972669171
    instructions:u     | 646241327   | 646241320   | 646262693  
    br_retired:u       | 42861731    | 42861729    | 42864127   
    br_mis_pred:u      | 4382561     | 4385838     | 4396540    
    l1i_cache:u        | 150161058   | 149493699   | 161847449  
    l1i_cache_refill:u | 66815942    | 66748618    | 67214078   
    l1i_tlb:u          | 150161058   | 149493699   | 161847449  
    l1i_tlb_refill:u   | 3813880     | 3813854     | 3785897    
    l2i_cache:u        | 66815911    | 66748579    | 67214067   
    l2i_cache_refill:u | 32093294    | 26705974    | 27774961   
    l2i_tlb:u          | 3831512     | 3832276     | 3951312    
    l2i_tlb_refill:u   | 2185341     | 2190830     | 2157002    
    l1d_cache:u        | 88097097    | 88103424    | 88110369   
    l1d_cache_refill:u | 67311345    | 66509226    | 66758259   
    l1d_tlb:u          | 219730814   | 219956779   | 219769068  
    l1d_tlb_refill:u   | 65967958    | 65984381    | 65959949   
    l2d_cache:u        | 433257033   | 428490280   | 432939409  
    l2d_cache_refill:u | 195426337   | 180059142   | 183489192  
    l2d_tlb:u          | 65974380    | 65989604    | 65972550   
    l2d_tlb_refill:u   | 65191453    | 65177966    | 65205481   
    ll_cache:u         | 158081584   | 153312468   | 156694247  
    ll_cache_miss:u    | 26532730    | 23435051    | 18949285   

### Combined Memory Layouts
#### canonical: `cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7+hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257+itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=620756992 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=620830720 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp2_dtlb_512m_ps_n262144_p131072_np2_l1_r100_sp257_main_b3000_d8_bitrev_dtlb_16m_ps_n8192_p4096_np2_l2_r100_sp7_itlb_f256_l1_d4_dtlb_64m_ps_n32768_p16384_np2_l2_r100_sp3: `hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257+cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7+itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=620756992 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=620830720 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b3000_d8_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l2_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_dtlb_64m_pstr_n32768_p16384_np2_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_036_s3

### Selected Cases
- `fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=1`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=131072`, `data_pool_nodes=262144`, `data_stride_pages=33`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256`: `branch_pairs_per_unit=3`, `data_level=2m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=512`, `data_pool_nodes=262144`, `data_stride_lines=256`, `data_stride_nodes=256`, `data_template=cold`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=8192`
- `itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129`: `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=32768`, `data_pool_nodes=65536`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=0`, `funcs=256`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33+hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256+itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129`

### Results
single_modules:
    id | module                                                               
    ---+----------------------------------------------------------------------
    s0 | fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33
    s1 | hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256           
    s2 | itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129          
single_counts:
    metric             | s0        | s1       | s2        
    -------------------+-----------+----------+-----------
    cpu-cycles:u       | 457811265 | 38623541 | 1901830243
    instructions:u     | 25590955  | 22160997 | 46490951  
    br_retired:u       | 3271392   | 3941404  | 2651393   
    br_mis_pred:u      | 290730    | 373      | 532       
    l1i_cache:u        | 7033349   | 2860032  | 5945297   
    l1i_cache_refill:u | 1621      | 690      | 7033290   
    l1i_tlb:u          | 7033349   | 2860032  | 5945297   
    l1i_tlb_refill:u   | 42        | 43       | 2590069   
    l2i_cache:u        | 1618      | 690      | 7033295   
    l2i_cache_refill:u | 1589      | 677      | 5997998   
    l2i_tlb:u          | 92        | 83       | 2590210   
    l2i_tlb_refill:u   | 39        | 29       | 1205519   
    l1d_cache:u        | 2991533   | 1416229  | 5257473   
    l1d_cache_refill:u | 1280049   | 705846   | 5114937   
    l1d_tlb:u          | 5686037   | 2297535  | 15610365  
    l1d_tlb_refill:u   | 1306202   | 672568   | 5145133   
    l2d_cache:u        | 7589758   | 3077830  | 34427654  
    l2d_cache_refill:u | 4330011   | 700808   | 16696685  
    l2d_tlb:u          | 1306353   | 674849   | 5145476   
    l2d_tlb_refill:u   | 1282741   | 101      | 5130930   
    ll_cache:u         | 3348267   | 700068   | 10319472  
    ll_cache_miss:u    | 2981909   | 391      | 9839447   
combined_orders:
    id        | modules                                                                                                                                                                                     
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33+hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256+itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129
    shuffle   | itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129+hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256+fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33
    sum       | fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33+hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256+itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 2482028855 | 2482060106 | 2398265049
    instructions:u     | 94221542   | 94221548   | 94242903  
    br_retired:u       | 9861792    | 9861790    | 9864189   
    br_mis_pred:u      | 291628     | 291213     | 291635    
    l1i_cache:u        | 16450885   | 16447009   | 15838678  
    l1i_cache_refill:u | 7117315    | 7126861    | 7035601   
    l1i_tlb:u          | 16450885   | 16447009   | 15838678  
    l1i_tlb_refill:u   | 2580755    | 2580752    | 2590154   
    l2i_cache:u        | 7117310    | 7126857    | 7035603   
    l2i_cache_refill:u | 6299934    | 6302054    | 6000264   
    l2i_tlb:u          | 2580971    | 2580996    | 2590385   
    l2i_tlb_refill:u   | 1232129    | 1230380    | 1205587   
    l1d_cache:u        | 9644145    | 9644643    | 9665235   
    l1d_cache_refill:u | 7058998    | 7074978    | 7100832   
    l1d_tlb:u          | 23632592   | 23624546   | 23593937  
    l1d_tlb_refill:u   | 7117674    | 7117806    | 7123903   
    l2d_cache:u        | 45597233   | 45882249   | 45095242  
    l2d_cache_refill:u | 23114725   | 23282131   | 21727504  
    l2d_tlb:u          | 7120108    | 7120244    | 7126678   
    l2d_tlb_refill:u   | 6474153    | 6473015    | 6413772   
    ll_cache:u         | 14998854   | 15005305   | 14367807  
    ll_cache_miss:u    | 13326581   | 13373556   | 12821747  

### Combined Memory Layouts
#### canonical: `fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33+hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256+itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=673185792 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=673259520 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l1_d0_dtlb_128m_ps_n65536_p32768_np2_l2_r100_sp129_hot_s8192_bp3_cold_2m_ns_n262144_p512_np512_l1_r100_sn256_fetch_b128_d4_bp1_s16_dtlb_512m_ps_n262144_p131072_np2_l1_r100_sp33: `itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129+hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256+fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=673185792 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=673259520 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d4_bp1_s16_r100_dtlb_512m_pstr_n262144_p131072_np2_l1_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp3_r100_cold_2m_nstr_n262144_p512_np512_l1_sn256`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=2097152 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2162688 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_037_s3

### Selected Cases
- `cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64`: `blocks=3000`, `data_level=16k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=4`, `data_pool_nodes=2048`, `data_stride_lines=64`, `data_stride_nodes=64`, `data_template=hot`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17`: `branch_pairs_per_unit=3`, `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=4096`, `data_pool_nodes=4096`, `data_stride_pages=17`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=131072`, `data_pool_nodes=131072`, `data_stride_pages=9`, `data_template=dtlb`, `direct_run_len=0`, `funcs=4096`, `fusion_ldr_per_unit=2`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64+hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9`

### Results
single_modules:
    id | module                                                      
    ---+-------------------------------------------------------------
    s0 | cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64    
    s1 | hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17      
    s2 | itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9
single_counts:
    metric             | s0         | s1        | s2         
    -------------------+------------+-----------+------------
    cpu-cycles:u       | 2819134175 | 401852424 | 95341896608
    instructions:u     | 930310729  | 13200951  | 1474972044 
    br_retired:u       | 90071330   | 2021393   | 41051608   
    br_mis_pred:u      | 30072623   | 434       | 10008      
    l1i_cache:u        | 448936324  | 1762568   | 184751307  
    l1i_cache_refill:u | 64426302   | 1067      | 171841300  
    l1i_tlb:u          | 448936324  | 1762568   | 184751307  
    l1i_tlb_refill:u   | 1073749    | 42        | 41140106   
    l2i_cache:u        | 64426508   | 1067      | 171841229  
    l2i_cache_refill:u | 28467771   | 615       | 171831785  
    l2i_tlb:u          | 1946904    | 141       | 41143731   
    l2i_tlb_refill:u   | 21         | 35        | 41140121   
    l1d_cache:u        | 278269286  | 2701352   | 164003657  
    l1d_cache_refill:u | 15852568   | 2559139   | 163751773  
    l1d_tlb:u          | 363631604  | 7913382   | 491950897  
    l1d_tlb_refill:u   | 362088     | 2586435   | 163883329  
    l2d_cache:u        | 108178549  | 12958259  | 1050837855 
    l2d_cache_refill:u | 31779841   | 5218380   | 688312853  
    l2d_tlb:u          | 479267     | 2588055   | 163893098  
    l2d_tlb_refill:u   | 10         | 2530303   | 163883270  
    ll_cache:u         | 1290683    | 5133355   | 328663246  
    ll_cache_miss:u    | 44737      | 2258      | 309024740  
combined_orders:
    id        | modules                                                                                                                                                                     
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64+hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9
    shuffle   | hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17+cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9
    sum       | cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64+hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 99089478950 | 99253604422 | 98562883207
    instructions:u     | 2418462611  | 2418462662  | 2418483724 
    br_retired:u       | 133142004   | 133142011   | 133144331  
    br_mis_pred:u      | 30002328    | 30031632    | 30083065   
    l1i_cache:u        | 621614644   | 625156827   | 635450199  
    l1i_cache_refill:u | 237236905   | 237283761   | 236268669  
    l1i_tlb:u          | 621614644   | 625156827   | 635450199  
    l1i_tlb_refill:u   | 42223012    | 42223092    | 42213897   
    l2i_cache:u        | 237236774   | 237283636   | 236268804  
    l2i_cache_refill:u | 204900602   | 207669052   | 200300171  
    l2i_tlb:u          | 42232044    | 42237473    | 43090776   
    l2i_tlb_refill:u   | 41151488    | 41151827    | 41140177   
    l1d_cache:u        | 450688298   | 449665748   | 444974295  
    l1d_cache_refill:u | 178526894   | 178893851   | 182163480  
    l1d_tlb:u          | 877714322   | 875524876   | 863495883  
    l1d_tlb_refill:u   | 166854115   | 166854450   | 166831852  
    l2d_cache:u        | 1184436341  | 1182448808  | 1171974663 
    l2d_cache_refill:u | 735603701   | 731976796   | 725311074  
    l2d_tlb:u          | 166995735   | 167074046   | 166960420  
    l2d_tlb_refill:u   | 166432128   | 166425121   | 166413583  
    ll_cache:u         | 339291272   | 338016429   | 335087284  
    ll_cache_miss:u    | 311426408   | 309726631   | 309071735  

### Combined Memory Layouts
#### canonical: `cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64+hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=553664512 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=553738240 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp3_dtlb_16m_ps_n4096_p4096_np1_l4_r100_sp17_main_b3000_d1_lin_hot_16k_ns_n2048_p4_np512_l4_r100_sn64_itlb_f4096_l2_d0_dtlb_512m_ps_n131072_p131072_np1_l2_r100_sp9: `hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17+cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=553664512 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=553738240 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b3000_d1_linear_hot_16k_nstr_n2048_p4_np512_l4_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16384 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=81920 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp3_r100_dtlb_16m_pstr_n4096_p4096_np1_l4_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l2_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_038_s3

### Selected Cases
- `fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=2`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=262144`, `data_pool_nodes=524288`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=2`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128`: `branch_pairs_per_unit=2`, `data_level=64k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=16`, `data_pool_nodes=8192`, `data_stride_lines=128`, `data_stride_nodes=128`, `data_template=cold`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=131072`, `data_pool_nodes=131072`, `data_stride_pages=5`, `data_template=dtlb`, `direct_run_len=0`, `funcs=4096`, `fusion_ldr_per_unit=4`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4+hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4
    s1 | hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128          
    s2 | itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5     
single_counts:
    metric             | s0        | s1       | s2          
    -------------------+-----------+----------+-------------
    cpu-cycles:u       | 862417083 | 5314584  | 146122820629
    instructions:u     | 16630948  | 11281055 | 1638812071  
    br_retired:u       | 2631390   | 1381408  | 41051612    
    br_mis_pred:u      | 298968    | 392      | 11212       
    l1i_cache:u        | 6371353   | 1495870  | 205351549   
    l1i_cache_refill:u | 1587      | 580      | 184092201   
    l1i_tlb:u          | 6371353   | 1495870  | 205351549   
    l1i_tlb_refill:u   | 52        | 42       | 41310065    
    l2i_cache:u        | 1587      | 580      | 184092174   
    l2i_cache_refill:u | 1560      | 527      | 184080520   
    l2i_tlb:u          | 104       | 73       | 41314642    
    l2i_tlb_refill:u   | 48        | 11       | 41308913    
    l1d_cache:u        | 4307387   | 775180   | 327842574   
    l1d_cache_refill:u | 2554286   | 2464     | 327535909   
    l1d_tlb:u          | 9660555   | 777048   | 983496202   
    l1d_tlb_refill:u   | 2590038   | 87       | 327723545   
    l2d_cache:u        | 14869376  | 6280     | 1894879504  
    l2d_cache_refill:u | 8224589   | 1455     | 1050497931  
    l2d_tlb:u          | 2590418   | 111      | 327741239   
    l2d_tlb_refill:u   | 2563528   | 7        | 327723424   
    ll_cache:u         | 6617924   | 930      | 657363641   
    ll_cache_miss:u    | 6006391   | 40       | 624243379   
combined_orders:
    id        | modules                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4+hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5
    shuffle   | fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5+hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128
    sum       | fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4+hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 146863671666 | 146650748046 | 146990552296
    instructions:u     | 1666702547   | 1666702611   | 1666724074  
    br_retired:u       | 45061997     | 45062004     | 45064410    
    br_mis_pred:u      | 329513       | 319939       | 310572      
    l1i_cache:u        | 213826138    | 213757197    | 213218772   
    l1i_cache_refill:u | 184018206    | 184074978    | 184094368   
    l1i_tlb:u          | 213826138    | 213757197    | 213218772   
    l1i_tlb_refill:u   | 41310534     | 41310838     | 41310159    
    l2i_cache:u        | 184018146    | 184074927    | 184094341   
    l2i_cache_refill:u | 184007892    | 184063936    | 184082607   
    l2i_tlb:u          | 41313264     | 41313908     | 41314819    
    l2i_tlb_refill:u   | 41310473     | 41310849     | 41308972    
    l1d_cache:u        | 332921355    | 332928696    | 332925141   
    l1d_cache_refill:u | 330263597    | 330264780    | 330092659   
    l1d_tlb:u          | 994001328    | 993958378    | 993933805   
    l1d_tlb_refill:u   | 330325191    | 330325152    | 330313670   
    l2d_cache:u        | 1906162200   | 1906128878   | 1909755160  
    l2d_cache_refill:u | 1057758903   | 1054675278   | 1058723975  
    l2d_tlb:u          | 330343216    | 330341321    | 330331768   
    l2d_tlb_refill:u   | 330291880    | 330291952    | 330286959   
    ll_cache:u         | 661445624    | 661263053    | 663982495   
    ll_cache_miss:u    | 628572468    | 628660911    | 630249810   

### Combined Memory Layouts
#### canonical: `fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4+hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1610678272 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1610752000 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d2_bp2_s16_dtlb_1g_ps_n524288_p262144_np2_l4_r100_sp4_itlb_f4096_l2_d0_dtlb_512m_ps_n131072_p131072_np1_l4_r100_sp5_hot_s4096_bp2_cold_64k_ns_n8192_p16_np512_l1_r100_sn128: `fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4+itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5+hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1610678272 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1610752000 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d2_bp2_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_cold_64k_nstr_n8192_p16_np512_l1_sn128`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=65536 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=131072 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l2_r100_dtlb_512m_pstr_n131072_p131072_np1_l4_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_039_s3

### Selected Cases
- `fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=0`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=16384`, `data_pool_nodes=65536`, `data_stride_pages=9`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1`: `branch_pairs_per_unit=2`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=8192`, `data_pool_nodes=32768`, `data_stride_pages=1`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64`: `data_level=16k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=4`, `data_pool_nodes=2048`, `data_stride_lines=64`, `data_stride_nodes=64`, `data_template=hot`, `direct_run_len=4`, `funcs=4096`, `fusion_ldr_per_unit=4`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9+hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1+itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9
    s1 | hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1           
    s2 | itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64           
single_counts:
    metric             | s0        | s1        | s2        
    -------------------+-----------+-----------+-----------
    cpu-cycles:u       | 798706896 | 518212327 | 7821359168
    instructions:u     | 37430948  | 13200957  | 932140720 
    br_retired:u       | 3911390   | 1381391   | 61511329  
    br_mis_pred:u      | 1244401   | 476       | 10232706  
    l1i_cache:u        | 17293553  | 1775671   | 237794362 
    l1i_cache_refill:u | 2592      | 1342      | 122427033 
    l1i_tlb:u          | 17293553  | 1775671   | 237794362 
    l1i_tlb_refill:u   | 43        | 42        | 41986963  
    l2i_cache:u        | 2589      | 1340      | 122426968 
    l2i_cache_refill:u | 1564      | 688       | 121318106 
    l2i_tlb:u          | 86        | 146       | 41990953  
    l2i_tlb_refill:u   | 40        | 37        | 40623361  
    l1d_cache:u        | 9248256   | 2700552   | 215908609 
    l1d_cache_refill:u | 2564133   | 2557694   | 5535814   
    l1d_tlb:u          | 18436996  | 7957912   | 217578358 
    l1d_tlb_refill:u   | 2602529   | 2587239   | 16711     
    l2d_cache:u        | 14507017  | 13061071  | 185942150 
    l2d_cache_refill:u | 6179912   | 5186813   | 124491041 
    l2d_tlb:u          | 2612357   | 2588728   | 17437     
    l2d_tlb_refill:u   | 2566728   | 2565732   | 16681     
    ll_cache:u         | 6078076   | 5165833   | 1644691   
    ll_cache_miss:u    | 5126917   | 1331001   | 5626      
combined_orders:
    id        | modules                                                                                                                                                                        
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9+hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1+itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64
    shuffle   | hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1+itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64+fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9
    sum       | fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9+hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1+itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 9456350073 | 9433609827 | 9138278391
    instructions:u     | 982751314  | 982751314  | 982772625 
    br_retired:u       | 66801731   | 66801731   | 66804110  
    br_mis_pred:u      | 11474782   | 11465245   | 11477583  
    l1i_cache:u        | 260169679  | 259705506  | 256863586 
    l1i_cache_refill:u | 122780642  | 122583324  | 122430967 
    l1i_tlb:u          | 260169679  | 259705506  | 256863586 
    l1i_tlb_refill:u   | 41997733   | 41997543   | 41987048  
    l2i_cache:u        | 122780632  | 122583301  | 122430897 
    l2i_cache_refill:u | 121800031  | 121496716  | 121320358 
    l2i_tlb:u          | 42003248   | 41999161   | 41991185  
    l2i_tlb_refill:u   | 40637950   | 40638114   | 40623438  
    l1d_cache:u        | 228033204  | 227981859  | 227857417 
    l1d_cache_refill:u | 10846350   | 10932236   | 10657641  
    l1d_tlb:u          | 244167574  | 244074697  | 243973266 
    l1d_tlb_refill:u   | 5233253    | 5256582    | 5206479   
    l2d_cache:u        | 216115623  | 215183751  | 213510238 
    l2d_cache_refill:u | 138038957  | 137428704  | 135857766 
    l2d_tlb:u          | 5245747    | 5274797    | 5218522   
    l2d_tlb_refill:u   | 5155226    | 5160926    | 5149141   
    ll_cache:u         | 14283976   | 14101683   | 12888600  
    ll_cache_miss:u    | 10540592   | 10481422   | 6463544   

### Combined Memory Layouts
#### canonical: `fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9+hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1+itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=100679680 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=100753408 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp2_dtlb_32m_ps_n32768_p8192_np4_l4_r100_sp1_itlb_f4096_l1_d4_hot_16k_ns_n2048_p4_np512_l4_r100_sn64_fetch_b128_d1_bp0_s16_dtlb_64m_ps_n65536_p16384_np4_l2_r100_sp9: `hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1+itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64+fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=100679680 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=100753408 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d1_bp0_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l2_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l1_r100_hot_16k_nstr_n2048_p4_np512_l4_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16384 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=81920 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_040_s3

### Selected Cases
- `cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4`: `blocks=4000`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=65536`, `data_pool_nodes=262144`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7`: `branch_pairs_per_unit=2`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=32768`, `data_pool_nodes=32768`, `data_stride_pages=7`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128`: `data_level=4m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1024`, `data_pool_nodes=524288`, `data_stride_lines=128`, `data_stride_nodes=128`, `data_template=cold`, `direct_run_len=0`, `funcs=4096`, `fusion_ldr_per_unit=2`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4+hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7+itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128`

### Results
single_modules:
    id | module                                                       
    ---+--------------------------------------------------------------
    s0 | cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4
    s1 | hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7     
    s2 | itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128 
single_counts:
    metric             | s0          | s1        | s2         
    -------------------+-------------+-----------+------------
    cpu-cycles:u       | 58082697184 | 776463932 | 18685685067
    instructions:u     | 1240312044  | 13200951  | 1474970723 
    br_retired:u       | 120071608   | 1381393   | 41051332   
    br_mis_pred:u      | 40095253    | 457       | 2522       
    l1i_cache:u        | 639292091   | 1798167   | 184827431  
    l1i_cache_refill:u | 88647123    | 1656      | 164893215  
    l1i_tlb:u          | 639292091   | 1798167   | 184827431  
    l1i_tlb_refill:u   | 1440408     | 40        | 41140054   
    l2i_cache:u        | 88647068    | 1657      | 164893115  
    l2i_cache_refill:u | 88615487    | 699       | 164891750  
    l2i_tlb:u          | 1443849     | 99        | 41140993   
    l2i_tlb_refill:u   | 1437461     | 36        | 41116658   
    l1d_cache:u        | 376194136   | 2701981   | 163994700  
    l1d_cache_refill:u | 171541811   | 2559022   | 61899922   
    l1d_tlb:u          | 825572521   | 7956302   | 246981003  
    l1d_tlb_refill:u   | 160514383   | 2586629   | 41312343   
    l2d_cache:u        | 1042874799  | 13007257  | 871717784  
    l2d_cache_refill:u | 557455578   | 5215725   | 482709751  
    l2d_tlb:u          | 160790669   | 2588507   | 41319541   
    l2d_tlb_refill:u   | 160410842   | 2565658   | 19472604   
    ll_cache:u         | 381328770   | 5139269   | 310365773  
    ll_cache_miss:u    | 329534736   | 4875991   | 466583     
combined_orders:
    id        | modules                                                                                                                                                                            
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4+hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7+itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128
    shuffle   | cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4+itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128+hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7
    sum       | cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4+hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7+itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 81099675196 | 81152592250 | 77544846183
    instructions:u     | 2728462611  | 2728462645  | 2728483718 
    br_retired:u       | 162502004   | 162502010   | 162504333  
    br_mis_pred:u      | 40105581    | 40214703    | 40098232   
    l1i_cache:u        | 782566125   | 794220245   | 825917689  
    l1i_cache_refill:u | 254758959   | 254381947   | 253541994  
    l1i_tlb:u          | 782566125   | 794220245   | 825917689  
    l1i_tlb_refill:u   | 42580900    | 42581574    | 42580502   
    l2i_cache:u        | 254758813   | 254381793   | 253541840  
    l2i_cache_refill:u | 254700934   | 254359290   | 253507936  
    l2i_tlb:u          | 42603865    | 42585461    | 42584941   
    l2i_tlb_refill:u   | 42553047    | 42533872    | 42554155   
    l1d_cache:u        | 542449459   | 544440290   | 542890817  
    l1d_cache_refill:u | 243229826   | 239543839   | 236000755  
    l1d_tlb:u          | 1076512761  | 1085481166  | 1080509826 
    l1d_tlb_refill:u   | 204439156   | 204414428   | 204413355  
    l2d_cache:u        | 1935197432  | 1935778230  | 1927599840 
    l2d_cache_refill:u | 1055411735  | 1050351550  | 1045381054 
    l2d_tlb:u          | 204747589   | 204711452   | 204698717  
    l2d_tlb_refill:u   | 182547925   | 182549286   | 182449104  
    ll_cache:u         | 706424907   | 700309275   | 696833812  
    ll_cache_miss:u    | 337460882   | 333446477   | 334877310  

### Combined Memory Layouts
#### canonical: `cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4+hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7+itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=406847488 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=406921216 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_main_b4000_d1_lin_dtlb_256m_ps_n262144_p65536_np4_l4_r100_sp4_itlb_f4096_l2_d0_cold_4m_ns_n524288_p1024_np512_l2_r100_sn128_hot_s4096_bp2_dtlb_128m_ps_n32768_p32768_np1_l4_r100_sp7: `cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4+itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128+hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=406847488 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=406921216 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b4000_d1_linear_dtlb_256m_pstr_n262144_p65536_np4_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l4_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l2_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn128`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4194304 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4259840 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_041_s3

### Selected Cases
- `fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=1`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=32768`, `data_pool_nodes=262144`, `data_stride_pages=33`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9`: `branch_pairs_per_unit=4`, `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=4096`, `data_pool_nodes=4096`, `data_stride_pages=9`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=8192`
- `itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=5`, `data_template=dtlb`, `direct_run_len=4`, `funcs=256`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33+hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9+itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5`

### Results
single_modules:
    id | module                                                              
    ---+---------------------------------------------------------------------
    s0 | fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33
    s1 | hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9              
    s2 | itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5        
single_counts:
    metric             | s0         | s1        | s2        
    -------------------+------------+-----------+-----------
    cpu-cycles:u       | 1594624416 | 206786334 | 2241081299
    instructions:u     | 39990948   | 22161010  | 94380957  
    br_retired:u       | 5191390    | 5221404   | 3911391   
    br_mis_pred:u      | 1238374    | 655       | 640398    
    l1i_cache:u        | 17649964   | 2859883   | 19578660  
    l1i_cache_refill:u | 3800       | 872       | 9930937   
    l1i_tlb:u          | 17649964   | 2859883   | 19578660  
    l1i_tlb_refill:u   | 41         | 45        | 2633429   
    l2i_cache:u        | 3800       | 872       | 9930938   
    l2i_cache_refill:u | 2026       | 656       | 9658962   
    l2i_tlb:u          | 94         | 88        | 2639653   
    l2i_tlb_refill:u   | 38         | 39        | 1001109   
    l1d_cache:u        | 11834169   | 1417928   | 8440040   
    l1d_cache_refill:u | 5122374    | 1279429   | 5172206   
    l1d_tlb:u          | 26223176   | 4082771   | 18862742  
    l1d_tlb_refill:u   | 5176481    | 1309960   | 5161330   
    l2d_cache:u        | 28950904   | 6625891   | 38041273  
    l2d_cache_refill:u | 12723055   | 2673447   | 23996485  
    l2d_tlb:u          | 5193426    | 1311526   | 5162720   
    l2d_tlb_refill:u   | 5137460    | 1267318   | 5135307   
    ll_cache:u         | 12419649   | 2630359   | 11099101  
    ll_cache_miss:u    | 10945500   | 42867     | 10252400  
combined_orders:
    id        | modules                                                                                                                                                                                 
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33+hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9+itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5
    shuffle   | itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5+hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9+fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33
    sum       | fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33+hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9+itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 4129590743 | 3985311457 | 4042492049
    instructions:u     | 156511329  | 156511320  | 156532915 
    br_retired:u       | 14321730   | 14321729   | 14324185  
    br_mis_pred:u      | 1889490    | 1903627    | 1879427   
    l1i_cache:u        | 42518857   | 43218682   | 40088507  
    l1i_cache_refill:u | 9840263    | 9779399    | 9935609   
    l1i_tlb:u          | 42518857   | 43218682   | 40088507  
    l1i_tlb_refill:u   | 2634177    | 2634133    | 2633515   
    l2i_cache:u        | 9840258    | 9779397    | 9935610   
    l2i_cache_refill:u | 9527900    | 9472440    | 9661644   
    l2i_tlb:u          | 2644523    | 2644113    | 2639835   
    l2i_tlb_refill:u   | 1011379    | 1004996    | 1001186   
    l1d_cache:u        | 21631918   | 21648398   | 21692137  
    l1d_cache_refill:u | 11584193   | 11563736   | 11574009  
    l1d_tlb:u          | 48964225   | 48955292   | 49168689  
    l1d_tlb_refill:u   | 11629910   | 11613747   | 11647771  
    l2d_cache:u        | 74486748   | 73656375   | 73618068  
    l2d_cache_refill:u | 40603399   | 39818259   | 39392987  
    l2d_tlb:u          | 11632634   | 11625144   | 11667672  
    l2d_tlb_refill:u   | 11538269   | 11534624   | 11540085  
    ll_cache:u         | 27090203   | 26465534   | 26149109  
    ll_cache_miss:u    | 22176112   | 21752692   | 21240767  

### Combined Memory Layouts
#### canonical: `fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33+hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9+itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=687865856 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=687939584 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l2_d4_dtlb_512m_ps_n1048576_p131072_np8_l1_r100_sp5_hot_s8192_bp4_dtlb_16m_ps_n4096_p4096_np1_l1_r100_sp9_fetch_b128_d1_bp1_s16_dtlb_128m_ps_n262144_p32768_np8_l4_r100_sp33: `itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5+hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9+fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=687865856 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=687939584 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d1_bp1_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp4_r100_dtlb_16m_pstr_n4096_p4096_np1_l1_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l2_r100_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_042_s3

### Selected Cases
- `cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`: `blocks=7000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=4`, `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=4096`, `data_pool_nodes=4096`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`: `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=4`, `funcs=1024`, `fusion_ldr_per_unit=4`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3+fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4+itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

### Results
single_modules:
    id | module                                                        
    ---+---------------------------------------------------------------
    s0 | cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3    
    s1 | fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4
    s2 | itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3      
single_counts:
    metric             | s0          | s1        | s2         
    -------------------+-------------+-----------+------------
    cpu-cycles:u       | 66442882821 | 219755666 | 10246235899
    instructions:u     | 1496562044  | 18870998  | 233260729  
    br_retired:u       | 87571608    | 4551405   | 15431330   
    br_mis_pred:u      | 8752568     | 591852    | 2551802    
    l1i_cache:u        | 395721604   | 8610318   | 56530959   
    l1i_cache_refill:u | 152527090   | 840       | 30370873   
    l1i_tlb:u          | 395721604   | 8610318   | 56530959   
    l1i_tlb_refill:u   | 2500897     | 42        | 10514348   
    l2i_cache:u        | 152526966   | 839       | 30370854   
    l2i_cache_refill:u | 152140922   | 624       | 30261743   
    l2i_tlb:u          | 2510982     | 95        | 10530250   
    l2i_tlb_refill:u   | 2500045     | 39        | 10232557   
    l1d_cache:u        | 323857110   | 4724020   | 54152389   
    l1d_cache_refill:u | 290422608   | 1275812   | 41008902   
    l1d_tlb:u          | 884688273   | 9247444   | 136781168  
    l1d_tlb_refill:u   | 280242911   | 1310061   | 41040915   
    l2d_cache:u        | 1625167583  | 6728598   | 262200789  
    l2d_cache_refill:u | 758025367   | 2736954   | 120825790  
    l2d_tlb:u          | 280250919   | 1310952   | 41050034   
    l2d_tlb_refill:u   | 280151020   | 1271004   | 41020186   
    ll_cache:u         | 598834859   | 2710927   | 89378213   
    ll_cache_miss:u    | 184217734   | 37279     | 26022874   
combined_orders:
    id        | modules                                                                                                                                                                           
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3+fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4+itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3
    shuffle   | fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4+itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3+cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3
    sum       | cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3+fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4+itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 79475241104 | 79917953017 | 76908874386
    instructions:u     | 1748672574  | 1748672601  | 1748693771 
    br_retired:u       | 107551999   | 107552003   | 107554343  
    br_mis_pred:u      | 11908836    | 11915261    | 11896222   
    l1i_cache:u        | 457380450   | 464045953   | 460862881  
    l1i_cache_refill:u | 182256233   | 181967855   | 182898803  
    l1i_tlb:u          | 457380450   | 464045953   | 460862881  
    l1i_tlb_refill:u   | 13025901    | 13025938    | 13015287   
    l2i_cache:u        | 182256134   | 181967731   | 182898659  
    l2i_cache_refill:u | 178425705   | 180813513   | 182403289  
    l2i_tlb:u          | 15071328    | 15060039    | 13041327   
    l2i_tlb_refill:u   | 12763824    | 12759309    | 12732641   
    l1d_cache:u        | 382672961   | 382731390   | 382733519  
    l1d_cache_refill:u | 332886621   | 332880793   | 332707322  
    l1d_tlb:u          | 1030521210  | 1030822651  | 1030716885 
    l1d_tlb_refill:u   | 322635399   | 322635373   | 322593887  
    l2d_cache:u        | 1895700819  | 1895728265  | 1894096970 
    l2d_cache_refill:u | 880959050   | 882905059   | 881588111  
    l2d_tlb:u          | 322651695   | 322656300   | 322611905  
    l2d_tlb_refill:u   | 322378349   | 322480515   | 322442210  
    ll_cache:u         | 694916321   | 694993704   | 690923999  
    ll_cache_miss:u    | 240601042   | 244846223   | 210277887  

### Combined Memory Layouts
#### canonical: `cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3+fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4+itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=83886080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=83959808 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d1_bp4_s16_dtlb_16m_ps_n4096_p4096_np1_l2_r100_sp4_itlb_f1024_l1_d4_dtlb_32m_ps_n65536_p8192_np8_l4_r100_sp3_main_b7000_d8_lin_dtlb_32m_ps_n65536_p8192_np8_l4_r100_sp3: `fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4+itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3+cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=83886080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=83959808 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b7000_d8_linear_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b64_d1_bp4_s16_r100_dtlb_16m_pstr_n4096_p4096_np1_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f1024_l1_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_043_s3

### Selected Cases
- `cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3`: `blocks=15000`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=65536`, `data_pool_nodes=262144`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=16`, `fusion_ldr_per_unit=2`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=1`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`: `branch_pairs_per_unit=2`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=1`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3+fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4+hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`

### Results
single_modules:
    id | module                                                              
    ---+---------------------------------------------------------------------
    s0 | cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3     
    s1 | fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4
    s2 | hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1            
single_counts:
    metric             | s0           | s1        | s2       
    -------------------+--------------+-----------+----------
    cpu-cycles:u       | 111721669943 | 850517481 | 187058172
    instructions:u     | 2803492028   | 14870942  | 11281003 
    br_retired:u       | 168831607    | 1671392   | 1381402  
    br_mis_pred:u      | 9387803      | 131105    | 479      
    l1i_cache:u        | 604819339    | 3791205   | 1512067  
    l1i_cache_refill:u | 315481148    | 1340      | 894      
    l1i_tlb:u          | 604819339    | 3791205   | 1512067  
    l1i_tlb_refill:u   | 7050585      | 41        | 40       
    l2i_cache:u        | 315480992    | 1337      | 894      
    l2i_cache_refill:u | 314826752    | 1323      | 825      
    l2i_tlb:u          | 9099116      | 87        | 119      
    l2i_tlb_refill:u   | 5231905      | 37        | 37       
    l1d_cache:u        | 347009714    | 3469822   | 776576   
    l1d_cache_refill:u | 312901617    | 2559856   | 640119   
    l1d_tlb:u          | 948873520    | 8755230   | 2212363  
    l1d_tlb_refill:u   | 300424030    | 2598808   | 678483   
    l2d_cache:u        | 1905043297   | 14596168  | 3265692  
    l2d_cache_refill:u | 1067120949   | 8000637   | 1371215  
    l2d_tlb:u          | 300435420    | 2599124   | 679060   
    l2d_tlb_refill:u   | 300401599    | 2567625   | 641936   
    ll_cache:u         | 650177595    | 6411796   | 1290127  
    ll_cache_miss:u    | 598521525    | 5690581   | 1217216  
combined_orders:
    id        | modules                                                                                                                                                                                      
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3+fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4+hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1
    shuffle   | fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4+cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3+hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1
    sum       | cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3+fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4+hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 116125305125 | 115091982255 | 112759245596
    instructions:u     | 2829622541   | 2829622581   | 2829643973  
    br_retired:u       | 171881995    | 171881999    | 171884401   
    br_mis_pred:u      | 9526280      | 9524272      | 9519387     
    l1i_cache:u        | 599439289    | 603640102    | 610122611   
    l1i_cache_refill:u | 316354847    | 316374977    | 315483382   
    l1i_tlb:u          | 599439289    | 603640102    | 610122611   
    l1i_tlb_refill:u   | 7059791      | 7057910      | 7050666     
    l2i_cache:u        | 316354684    | 316374813    | 315483223   
    l2i_cache_refill:u | 315663105    | 315706286    | 314828900   
    l2i_tlb:u          | 7084245      | 7077500      | 9099322     
    l2i_tlb_refill:u   | 5217861      | 5230065      | 5231979     
    l1d_cache:u        | 351256383    | 351254609    | 351256112   
    l1d_cache_refill:u | 313694195    | 312874519    | 316101592   
    l1d_tlb:u          | 959972366    | 960085322    | 959841113   
    l1d_tlb_refill:u   | 303712681    | 303711779    | 303701321   
    l2d_cache:u        | 1922913434   | 1921316211   | 1922905157  
    l2d_cache_refill:u | 1058962097   | 1056651596   | 1076492801  
    l2d_tlb:u          | 303724547    | 303724098    | 303713604   
    l2d_tlb_refill:u   | 303614400    | 303621148    | 303611160   
    ll_cache:u         | 642375665    | 639312061    | 657879518   
    ll_cache_miss:u    | 589425311    | 587814225    | 605429322   

### Combined Memory Layouts
#### canonical: `cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3+fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4+hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1879048192 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1879121920 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d4_bp1_s16_dtlb_512m_ps_n1048576_p131072_np8_l4_r100_sp4_main_b15000_d16_bitrev_dtlb_256m_ps_n262144_p65536_np4_l2_r100_sp3_hot_s4096_bp2_dtlb_1g_ps_n262144_p262144_np1_l1_r100_sp1: `fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4+cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3+hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1879048192 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1879121920 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b15000_d16_bitrev_dtlb_256m_pstr_n262144_p65536_np4_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b64_d4_bp1_s16_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_044_s3

### Selected Cases
- `cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2`: `blocks=16000`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=16384`, `data_pool_nodes=16384`, `data_stride_pages=2`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=0`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=9`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33`: `branch_pairs_per_unit=3`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=65536`, `data_pool_nodes=131072`, `data_stride_pages=33`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2+fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9+hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2     
    s1 | fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9
    s2 | hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33      
single_counts:
    metric             | s0           | s1        | s2        
    -------------------+--------------+-----------+-----------
    cpu-cycles:u       | 111879746962 | 463099705 | 1572902672
    instructions:u     | 3320311977   | 18870942  | 26000951  
    br_retired:u       | 240071600    | 1991392   | 3941393   
    br_mis_pred:u      | 40005104     | 596716    | 499       
    l1i_cache:u        | 993304275    | 8702779   | 3426710   
    l1i_cache_refill:u | 334990100    | 880       | 4032      
    l1i_tlb:u          | 993304275    | 8702779   | 3426710   
    l1i_tlb_refill:u   | 5353522      | 41        | 42        
    l2i_cache:u        | 334989908    | 879       | 4030      
    l2i_cache_refill:u | 334972782    | 831       | 3985      
    l2i_tlb:u          | 5367312      | 85        | 160       
    l2i_tlb_refill:u   | 5351589      | 36        | 41        
    l1d_cache:u        | 522542897    | 4696759   | 5270470   
    l1d_cache_refill:u | 352721767    | 1279869   | 5116791   
    l1d_tlb:u          | 1172423950   | 9211998   | 15643232  
    l1d_tlb_refill:u   | 320823020    | 1310039   | 5145308   
    l2d_cache:u        | 2113080447   | 6800719   | 26111841  
    l2d_cache_refill:u | 1080717375   | 4264853   | 10980053  
    l2d_tlb:u          | 320850365    | 1310218   | 5148551   
    l2d_tlb_refill:u   | 320701908    | 1282757   | 5129447   
    ll_cache:u         | 721209776    | 2823291   | 10310028  
    ll_cache_miss:u    | 605369770    | 2681872   | 9791741   
combined_orders:
    id        | modules                                                                                                                                                                                   
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2+fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9+hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33
    shuffle   | hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33+fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9+cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2
    sum       | cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2+fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9+hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 119534828530 | 111318323088 | 113915749339
    instructions:u     | 3365162638   | 3365162662   | 3365183870  
    br_retired:u       | 246002008    | 246002011    | 246004385   
    br_mis_pred:u      | 40625966     | 40670729     | 40602319    
    l1i_cache:u        | 1013797317   | 975750607    | 1005433764  
    l1i_cache_refill:u | 333648635    | 333704037    | 334995012   
    l1i_tlb:u          | 1013797317   | 975750607    | 1005433764  
    l1i_tlb_refill:u   | 5359903      | 5357658      | 5353605     
    l2i_cache:u        | 333648457    | 333703862    | 334994817   
    l2i_cache_refill:u | 333561831    | 333608325    | 334977598   
    l2i_tlb:u          | 10217971     | 10211976     | 5367557     
    l2i_tlb_refill:u   | 5353631      | 5351473      | 5351666     
    l1d_cache:u        | 533179141    | 531688415    | 532510126   
    l1d_cache_refill:u | 361199660    | 357734238    | 359118427   
    l1d_tlb:u          | 1205836136   | 1193997642   | 1197279180  
    l1d_tlb_refill:u   | 327335560    | 327299613    | 327278367   
    l2d_cache:u        | 2168140959   | 2137832928   | 2145993007  
    l2d_cache_refill:u | 1085960191   | 1085514432   | 1095962281  
    l2d_tlb:u          | 327359743    | 327315922    | 327309134   
    l2d_tlb_refill:u   | 327126847    | 327135287    | 327114112   
    ll_cache:u         | 726055177    | 724250544    | 734343095   
    ll_cache_miss:u    | 614465496    | 607874793    | 617843383   

### Combined Memory Layouts
#### canonical: `cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2+fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9+hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1409286144 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1409359872 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s8192_bp3_dtlb_256m_ps_n131072_p65536_np2_l4_r100_sp33_fetch_b64_d1_bp0_s16_dtlb_1g_ps_n262144_p262144_np1_l2_r100_sp9_main_b16000_d4_lin_dtlb_64m_ps_n16384_p16384_np1_l2_r100_sp2: `hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33+fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9+cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1409286144 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1409359872 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b16000_d4_linear_dtlb_64m_pstr_n16384_p16384_np1_l2_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b64_d1_bp0_s16_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp3_r100_dtlb_256m_pstr_n131072_p65536_np2_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_045_s3

### Selected Cases
- `cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256`: `blocks=11000`, `data_level=1m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=256`, `data_pool_nodes=131072`, `data_stride_lines=256`, `data_stride_nodes=256`, `data_template=cold`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=2`, `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=4096`, `data_pool_nodes=8192`, `data_stride_pages=2`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4`: `branch_pairs_per_unit=4`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=4`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256+fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2+hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4`

### Results
single_modules:
    id | module                                                        
    ---+---------------------------------------------------------------
    s0 | cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256
    s1 | fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2
    s2 | hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4       
single_counts:
    metric             | s0          | s1        | s2        
    -------------------+-------------+-----------+-----------
    cpu-cycles:u       | 22233102274 | 412774034 | 1037518053
    instructions:u     | 3410310940  | 20150942  | 26000957  
    br_retired:u       | 330071388   | 3271392   | 5221391   
    br_mis_pred:u      | 110057628   | 594693    | 470       
    l1i_cache:u        | 1746892636  | 8789683   | 3389183   
    l1i_cache_refill:u | 248476113   | 1022      | 2979      
    l1i_tlb:u          | 1746892636  | 8789683   | 3389183   
    l1i_tlb_refill:u   | 5305513     | 41        | 43        
    l2i_cache:u        | 248475994   | 1021      | 2980      
    l2i_cache_refill:u | 247993412   | 659       | 1456      
    l2i_tlb:u          | 5309216     | 95        | 156       
    l2i_tlb_refill:u   | 29159       | 38        | 39        
    l1d_cache:u        | 1024326580  | 5976113   | 5264606   
    l1d_cache_refill:u | 101014386   | 2535102   | 5121667   
    l1d_tlb:u          | 1776650366  | 13126053  | 15625311  
    l1d_tlb_refill:u   | 222591177   | 2601881   | 5148643   
    l2d_cache:u        | 982719422   | 14079836  | 26022504  
    l2d_cache_refill:u | 485954913   | 5769729   | 10410236  
    l2d_tlb:u          | 222829440   | 2612531   | 5149698   
    l2d_tlb_refill:u   | 3576        | 2539810   | 5122859   
    ll_cache:u         | 238441879   | 5734106   | 10293684  
    ll_cache_miss:u    | 417091      | 272263    | 2559423   
combined_orders:
    id        | modules                                                                                                                                                                              
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256+fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2+hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4
    shuffle   | fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2+hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4+cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256
    sum       | cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256+fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2+hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 24741217765 | 24721040777 | 23683394361
    instructions:u     | 3456441537  | 3456441531  | 3456462839 
    br_retired:u       | 338561785   | 338561787   | 338564171  
    br_mis_pred:u      | 110647146   | 110750349   | 110652791  
    l1i_cache:u        | 1659989155  | 1668637692  | 1759071502 
    l1i_cache_refill:u | 248884021   | 248981099   | 248480114  
    l1i_tlb:u          | 1659989155  | 1668637692  | 1759071502 
    l1i_tlb_refill:u   | 5297072     | 5304054     | 5305597    
    l2i_cache:u        | 248883786   | 248980919   | 248479995  
    l2i_cache_refill:u | 248382226   | 248470914   | 247995527  
    l2i_tlb:u          | 5308971     | 5311629     | 5309467    
    l2i_tlb_refill:u   | 300636      | 127481      | 29236      
    l1d_cache:u        | 1038503235  | 1038259704  | 1035567299 
    l1d_cache_refill:u | 117642533   | 121216175   | 108671155  
    l1d_tlb:u          | 1800232213  | 1797514743  | 1805401730 
    l1d_tlb_refill:u   | 230352013   | 230367613   | 230341701  
    l2d_cache:u        | 1012925785  | 1019964356  | 1022821762 
    l2d_cache_refill:u | 504680534   | 503592626   | 502134878  
    l2d_tlb:u          | 231171860   | 231135749   | 230591669  
    l2d_tlb_refill:u   | 7813505     | 8030828     | 7666245    
    ll_cache:u         | 257025688   | 255150645   | 254469669  
    ll_cache_miss:u    | 8356546     | 8478119     | 3248777    

### Combined Memory Layouts
#### canonical: `cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256+fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2+hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=51380224 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=51453952 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d1_bp2_s16_dtlb_16m_ps_n8192_p4096_np2_l4_r100_sp2_hot_s8192_bp4_dtlb_32m_ps_n65536_p8192_np8_l4_r100_sp4_main_b11000_d1_bitrev_cold_1m_ns_n131072_p256_np512_l4_r100_sn256: `fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2+hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4+cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=51380224 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=51453952 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b11000_d1_bitrev_cold_1m_nstr_n131072_p256_np512_l4_sn256`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1048576 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1114112 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b64_d1_bp2_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp4_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_046_s3

### Selected Cases
- `cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257`: `blocks=13000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=8192`, `data_pool_nodes=16384`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=16`, `fusion_ldr_per_unit=4`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=2`, `data_level=2k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1`, `data_pool_nodes=256`, `data_stride_lines=128`, `data_stride_nodes=128`, `data_template=hot`, `direct_run_len=4`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2`: `branch_pairs_per_unit=2`, `data_level=128m`, `data_mode=random`, `data_nodes_per_page=2`, `data_pages=32768`, `data_pool_nodes=65536`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257+fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128+hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2`

### Results
single_modules:
    id | module                                                        
    ---+---------------------------------------------------------------
    s0 | cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257
    s1 | fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128 
    s2 | hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2         
single_counts:
    metric             | s0           | s1       | s2       
    -------------------+--------------+----------+----------
    cpu-cycles:u       | 124686777732 | 18757942 | 786747179
    instructions:u     | 2689741977   | 25591049 | 23440942 
    br_retired:u       | 146331600    | 4551410  | 2661392  
    br_mis_pred:u      | 8142301      | 290613   | 471      
    l1i_cache:u        | 531449447    | 7617586  | 3071754  
    l1i_cache_refill:u | 289495624    | 835      | 1913     
    l1i_tlb:u          | 531449447    | 7617586  | 3071754  
    l1i_tlb_refill:u   | 6481453      | 56       | 42       
    l2i_cache:u        | 289495498    | 835      | 1912     
    l2i_cache_refill:u | 288746802    | 715      | 1689     
    l2i_tlb:u          | 6491090      | 105      | 92       
    l2i_tlb_refill:u   | 4839127      | 48       | 38       
    l1d_cache:u        | 560761361    | 2975241  | 2702324  
    l1d_cache_refill:u | 530295203    | 197      | 2557482  
    l1d_tlb:u          | 1599008267   | 2976993  | 7914929  
    l1d_tlb_refill:u   | 520355670    | 63       | 2585483  
    l2d_cache:u        | 2985486690   | 1459     | 13007515 
    l2d_cache_refill:u | 1403576012   | 939      | 5336019  
    l2d_tlb:u          | 520368429    | 83       | 2587372  
    l2d_tlb_refill:u   | 517203808    | 4        | 2524698  
    ll_cache:u         | 1087680080   | 251      | 5168694  
    ll_cache_miss:u    | 326714596    | 27       | 4910472  
combined_orders:
    id        | modules                                                                                                                                                                           
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257+fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128+hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2
    shuffle   | fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128+cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257+hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2
    sum       | cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257+fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128+hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 126656119083 | 126519638373 | 125492282853
    instructions:u     | 2738752560   | 2738752568   | 2738773968  
    br_retired:u       | 153541997    | 153541999    | 153544402   
    br_mis_pred:u      | 8438020      | 8447276      | 8433385     
    l1i_cache:u        | 583356807    | 572012805    | 542138787   
    l1i_cache_refill:u | 289965657    | 290060911    | 289498372   
    l1i_tlb:u          | 583356807    | 572012805    | 542138787   
    l1i_tlb_refill:u   | 6482260      | 6478762      | 6481551     
    l2i_cache:u        | 289965524    | 290060778    | 289498245   
    l2i_cache_refill:u | 289236514    | 289423179    | 288749206   
    l2i_tlb:u          | 6493474      | 6499259      | 6491287     
    l2i_tlb_refill:u   | 4738420      | 4785443      | 4839213     
    l1d_cache:u        | 566442332    | 566446935    | 566438926   
    l1d_cache_refill:u | 530328623    | 530429490    | 532852882   
    l1d_tlb:u          | 1610168532   | 1609431877   | 1609900189  
    l1d_tlb_refill:u   | 522971540    | 522953556    | 522941216   
    l2d_cache:u        | 3010415343   | 3009383305   | 2998495664  
    l2d_cache_refill:u | 1406055060   | 1405983466   | 1408912970  
    l2d_tlb:u          | 522990438    | 522973360    | 522955884   
    l2d_tlb_refill:u   | 519722748    | 519055740    | 519728510   
    ll_cache:u         | 1089997973   | 1090003078   | 1092849025  
    ll_cache_miss:u    | 326062565    | 330279844    | 331625095   

### Combined Memory Layouts
#### canonical: `cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257+fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128+hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=167776256 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=167849984 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d4_bp2_s16_hot_2k_ns_n256_p1_np512_l1_r100_sn128_main_b13000_d16_bitrev_dtlb_32m_ps_n16384_p8192_np2_l4_r100_sp257_hot_s8192_bp2_dtlb_128m_rnd_n65536_p32768_np2_l2_r100: `fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128+cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257+hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=167776256 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=167849984 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b13000_d16_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l4_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d4_bp2_s16_r100_hot_2k_nstr_n256_p1_np512_l1_sn128`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4096 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=69632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp2_r100_dtlb_128m_rand_n65536_p32768_np2_l2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_047_s3

### Selected Cases
- `cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4`: `blocks=3000`, `data_level=8k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=2`, `data_pool_nodes=1024`, `data_stride_lines=4`, `data_stride_nodes=4`, `data_template=hot`, `direct_run_len=2`, `fusion_ldr_per_unit=1`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=1`, `data_level=512m`, `data_mode=random`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3`: `branch_pairs_per_unit=4`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=3`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4+fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4+hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4           
    s1 | fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4
    s2 | hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3     
single_counts:
    metric             | s0         | s1         | s2        
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 1917761529 | 1873606361 | 1602485828
    instructions:u     | 675310951  | 39990948   | 26000951  
    br_retired:u       | 60071393   | 5191390    | 5221393   
    br_mis_pred:u      | 15009482   | 1240542    | 531       
    l1i_cache:u        | 266205467  | 18021862   | 3397755   
    l1i_cache_refill:u | 59872571   | 4060       | 3775      
    l1i_tlb:u          | 266205467  | 18021862   | 3397755   
    l1i_tlb_refill:u   | 1095297    | 53         | 43        
    l2i_cache:u        | 59872535   | 4059       | 3774      
    l2i_cache_refill:u | 18623861   | 3833       | 3752      
    l2i_tlb:u          | 1098046    | 98         | 169       
    l2i_tlb_refill:u   | 23         | 49         | 40        
    l1d_cache:u        | 105803477  | 11899120   | 5268275   
    l1d_cache_refill:u | 3022380    | 5178174    | 5117115   
    l1d_tlb:u          | 110504835  | 26108851   | 15642144  
    l1d_tlb_refill:u   | 4195       | 5161455    | 5148551   
    l2d_cache:u        | 78623478   | 33042504   | 26479200  
    l2d_cache_refill:u | 21561366   | 16301544   | 12601022  
    l2d_tlb:u          | 4495       | 5171746    | 5150374   
    l2d_tlb_refill:u   | 7          | 5097141    | 5130025   
    ll_cache:u         | 1468829    | 12373096   | 10671433  
    ll_cache_miss:u    | 8844       | 11357478   | 9984599   
combined_orders:
    id        | modules                                                                                                                                                                              
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4+fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4+hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3
    shuffle   | fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4+cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4+hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3
    sum       | cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4+fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4+hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 5660026938 | 5082688871 | 5393853718
    instructions:u     | 741281314  | 741281320  | 741302850 
    br_retired:u       | 70481731   | 70481729   | 70484176  
    br_mis_pred:u      | 16285444   | 16269809   | 16250555  
    l1i_cache:u        | 287889655  | 287387556  | 287625084 
    l1i_cache_refill:u | 59932329   | 60049215   | 59880406  
    l1i_tlb:u          | 287889655  | 287387556  | 287625084 
    l1i_tlb_refill:u   | 1118488    | 1115542    | 1095393   
    l2i_cache:u        | 59932299   | 60049201   | 59880368  
    l2i_cache_refill:u | 20648900   | 15923015   | 18631446  
    l2i_tlb:u          | 1120471    | 1124165    | 1098313   
    l2i_tlb_refill:u   | 11339      | 11644      | 112       
    l1d_cache:u        | 122857130  | 123150560  | 122970872 
    l1d_cache_refill:u | 13010155   | 13999558   | 13317669  
    l1d_tlb:u          | 152421810  | 152852474  | 152255830 
    l1d_tlb_refill:u   | 10357734   | 10334567   | 10314201  
    l2d_cache:u        | 136591436  | 138396272  | 138145182 
    l2d_cache_refill:u | 52231127   | 50793053   | 50463932  
    l2d_tlb:u          | 10373638   | 10355935   | 10326615  
    l2d_tlb_refill:u   | 10245385   | 10237507   | 10227173  
    ll_cache:u         | 25558722   | 27428570   | 24513358  
    ll_cache_miss:u    | 22379742   | 23236964   | 21350921  

### Combined Memory Layouts
#### canonical: `cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4+fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4+hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1073750016 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073823744 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d1_bp1_s16_dtlb_512m_rnd_n1048576_p131072_np8_l4_r100_main_b3000_d2_bitrev_hot_8k_ns_n1024_p2_np512_l1_r100_sn4_hot_s8192_bp4_dtlb_512m_ps_n1048576_p131072_np8_l4_r100_sp3: `fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4+cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4+hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1073750016 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073823744 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b3000_d2_bitrev_hot_8k_nstr_n1024_p2_np512_l1_sn4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=8192 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=73728 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d1_bp1_s16_r100_dtlb_512m_rand_n1048576_p131072_np8_l4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp4_r100_dtlb_512m_pstr_n1048576_p131072_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_048_s3

### Selected Cases
- `cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2`: `blocks=1000`, `data_level=8k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=2`, `data_pool_nodes=1024`, `data_stride_lines=2`, `data_stride_nodes=2`, `data_template=hot`, `direct_run_len=1`, `fusion_ldr_per_unit=2`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=0`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=32768`, `data_pool_nodes=262144`, `data_stride_pages=7`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129`: `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=0`, `funcs=256`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2+fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7+itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129`

### Results
single_modules:
    id | module                                                             
    ---+--------------------------------------------------------------------
    s0 | cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2             
    s1 | fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7
    s2 | itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129        
single_counts:
    metric             | s0        | s1        | s2        
    -------------------+-----------+-----------+-----------
    cpu-cycles:u       | 503948348 | 400387981 | 2176508078
    instructions:u     | 290310957 | 23830942  | 46490957  
    br_retired:u       | 30071391  | 1671392   | 2651391   
    br_mis_pred:u      | 9941174   | 140615    | 547       
    l1i_cache:u        | 165080047 | 4751548   | 5914490   
    l1i_cache_refill:u | 11844919  | 1401      | 7037579   
    l1i_tlb:u          | 165080047 | 4751548   | 5914490   
    l1i_tlb_refill:u   | 1729      | 44        | 2590075   
    l2i_cache:u        | 11844907  | 1401      | 7037573   
    l2i_cache_refill:u | 2361      | 1106      | 6149216   
    l2i_tlb:u          | 1782      | 86        | 2590159   
    l2i_tlb_refill:u   | 18        | 40        | 1122331   
    l1d_cache:u        | 78595049  | 2178031   | 5257330   
    l1d_cache_refill:u | 3689      | 1281003   | 5116840   
    l1d_tlb:u          | 99944883  | 4906549   | 15612320  
    l1d_tlb_refill:u   | 747       | 1319418   | 5145643   
    l2d_cache:u        | 11346953  | 7367461   | 35532655  
    l2d_cache_refill:u | 3430      | 3299914   | 22252897  
    l2d_tlb:u          | 980       | 1320430   | 5146041   
    l2d_tlb_refill:u   | 8         | 1283847   | 5131390   
    ll_cache:u         | 1189      | 3208469   | 10213362  
    ll_cache_miss:u    | 79        | 2809985   | 9750405   
combined_orders:
    id        | modules                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2+fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7+itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129
    shuffle   | itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129+cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2+fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7
    sum       | cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2+fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7+itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 3196331549 | 3203583004 | 3080844407
    instructions:u     | 360611329  | 360611323  | 360632856 
    br_retired:u       | 34391730   | 34391732   | 34394174  
    br_mis_pred:u      | 10087024   | 10091338   | 10082336  
    l1i_cache:u        | 180206249  | 180442856  | 175746085 
    l1i_cache_refill:u | 18295823   | 18239790   | 18883899  
    l1i_tlb:u          | 180206249  | 180442856  | 175746085 
    l1i_tlb_refill:u   | 2596050    | 2595947    | 2591848   
    l2i_cache:u        | 18295811   | 18239777   | 18883881  
    l2i_cache_refill:u | 6426903    | 6469622    | 6152683   
    l2i_tlb:u          | 2597888    | 2597674    | 2592027   
    l2i_tlb_refill:u   | 1217263    | 1215223    | 1122389   
    l1d_cache:u        | 86737154   | 86678920   | 86030410  
    l1d_cache_refill:u | 6405649    | 6389181    | 6401532   
    l1d_tlb:u          | 120749613  | 120689298  | 120463752 
    l1d_tlb_refill:u   | 6479729    | 6479979    | 6465808   
    l2d_cache:u        | 54735859   | 55016059   | 54247069  
    l2d_cache_refill:u | 26744044   | 26947678   | 25556241  
    l2d_tlb:u          | 6487367    | 6486124    | 6467451   
    l2d_tlb_refill:u   | 6422293    | 6421646    | 6415245   
    ll_cache:u         | 13922231   | 14170671   | 13423020  
    ll_cache_miss:u    | 12930808   | 13223258   | 12560469  

### Combined Memory Layouts
#### canonical: `cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2+fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7+itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1207967744 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1208041472 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f256_l1_d0_dtlb_1g_ps_n262144_p262144_np1_l2_r100_sp129_main_b1000_d1_bitrev_hot_8k_ns_n1024_p2_np512_l2_r100_sn2_fetch_b128_d8_bp0_s16_dtlb_128m_ps_n262144_p32768_np8_l1_r100_sp7: `itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129+cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2+fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1207967744 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1208041472 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b1000_d1_bitrev_hot_8k_nstr_n1024_p2_np512_l2_sn2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=8192 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=73728 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d8_bp0_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l1_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_dtlb_1g_pstr_n262144_p262144_np1_l2_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_049_s3

### Selected Cases
- `fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=4`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=32768`, `data_pool_nodes=262144`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1`: `branch_pairs_per_unit=2`, `data_level=64m`, `data_mode=random`, `data_nodes_per_page=8`, `data_pages=16384`, `data_pool_nodes=131072`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=8192`
- `itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1`: `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=4096`, `data_pool_nodes=8192`, `data_stride_pages=1`, `data_template=dtlb`, `direct_run_len=4`, `funcs=2048`, `fusion_ldr_per_unit=1`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1+itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1`

### Results
single_modules:
    id | module                                                              
    ---+---------------------------------------------------------------------
    s0 | fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257
    s1 | hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1               
    s2 | itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1             
single_counts:
    metric             | s0        | s1        | s2        
    -------------------+-----------+-----------+-----------
    cpu-cycles:u       | 409179318 | 396094802 | 6628510960
    instructions:u     | 18870942  | 22160942  | 404780729 
    br_retired:u       | 4551392   | 2661392   | 30791330  
    br_mis_pred:u      | 593757    | 455       | 5130172   
    l1i_cache:u        | 8642611   | 2887685   | 106975264 
    l1i_cache_refill:u | 772       | 995       | 60452786  
    l1i_tlb:u          | 8642611   | 2887685   | 106975264 
    l1i_tlb_refill:u   | 41        | 41        | 20948161  
    l2i_cache:u        | 773       | 995       | 60452754  
    l2i_cache_refill:u | 650       | 686       | 60438245  
    l2i_tlb:u          | 86        | 135       | 20965886  
    l2i_tlb_refill:u   | 35        | 36        | 20490492  
    l1d_cache:u        | 4717773   | 1420600   | 46649749  
    l1d_cache_refill:u | 1285469   | 1277995   | 20880439  
    l1d_tlb:u          | 9236528   | 4039735   | 88780537  
    l1d_tlb_refill:u   | 1310056   | 1304364   | 20622439  
    l2d_cache:u        | 7224085   | 7024222   | 195888240 
    l2d_cache_refill:u | 3174165   | 3239554   | 107815005 
    l2d_tlb:u          | 1310132   | 1305604   | 20623924  
    l2d_tlb_refill:u   | 1280757   | 1211443   | 20598327  
    ll_cache:u         | 3099631   | 3075659   | 46641875  
    ll_cache_miss:u    | 2861682   | 2614523   | 2862286   
combined_orders:
    id        | modules                                                                                                                                                                           
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1+itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1
    shuffle   | fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1+hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1
    sum       | fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1+itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 7828722316 | 7804271209 | 7433785080
    instructions:u     | 445791320  | 445791320  | 445812613 
    br_retired:u       | 38001729   | 38001729   | 38004114  
    br_mis_pred:u      | 5719866    | 5710649    | 5724384   
    l1i_cache:u        | 120106913  | 118197526  | 118505560 
    l1i_cache_refill:u | 60464178   | 60439744   | 60454553  
    l1i_tlb:u          | 120106913  | 118197526  | 118505560 
    l1i_tlb_refill:u   | 20958551   | 20958533   | 20948243  
    l2i_cache:u        | 60464151   | 60439717   | 60454522  
    l2i_cache_refill:u | 60450254   | 60425853   | 60439581  
    l2i_tlb:u          | 20974105   | 20976664   | 20966107  
    l2i_tlb_refill:u   | 20561281   | 20561423   | 20490563  
    l1d_cache:u        | 52819932   | 52810948   | 52788122  
    l1d_cache_refill:u | 23343920   | 23405957   | 23443903  
    l1d_tlb:u          | 102755288  | 102074567  | 102056800 
    l1d_tlb_refill:u   | 23247022   | 23264921   | 23236859  
    l2d_cache:u        | 210737190  | 211424831  | 210136547 
    l2d_cache_refill:u | 114230063  | 115317010  | 114228724 
    l2d_tlb:u          | 23249490   | 23276406   | 23239660  
    l2d_tlb_refill:u   | 23085745   | 23086072   | 23090527  
    ll_cache:u         | 52547912   | 53680631   | 52817165  
    ll_cache_miss:u    | 9475514    | 10080542   | 8338491   

### Combined Memory Layouts
#### canonical: `fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1+itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=218103808 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=218177536 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d1_bp4_s16_dtlb_128m_ps_n262144_p32768_np8_l2_r100_sp257_itlb_f2048_l1_d4_dtlb_16m_ps_n8192_p4096_np2_l1_r100_sp1_hot_s8192_bp2_dtlb_64m_rnd_n131072_p16384_np8_l1_r100: `fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257+itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1+hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=218103808 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=218177536 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d1_bp4_s16_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp2_r100_dtlb_64m_rand_n131072_p16384_np8_l1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_050_s3

### Selected Cases
- `cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33`: `blocks=4000`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=131072`, `data_pool_nodes=524288`, `data_stride_pages=33`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4`: `branch_pairs_per_unit=4`, `data_level=128k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=32`, `data_pool_nodes=16384`, `data_stride_lines=4`, `data_stride_nodes=4`, `data_template=cold`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=8192`
- `itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64`: `data_level=2k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1`, `data_pool_nodes=256`, `data_stride_lines=64`, `data_stride_nodes=64`, `data_template=hot`, `direct_run_len=4`, `funcs=2048`, `fusion_ldr_per_unit=4`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33+hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4+itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64`

### Results
single_modules:
    id | module                                                         
    ---+----------------------------------------------------------------
    s0 | cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33
    s1 | hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4       
    s2 | itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64           
single_counts:
    metric             | s0          | s1       | s2        
    -------------------+-------------+----------+-----------
    cpu-cycles:u       | 63479292146 | 22435087 | 3583272349
    instructions:u     | 1240312044  | 23441049 | 466220720 
    br_retired:u       | 120071608   | 5221410  | 30791329  
    br_mis_pred:u      | 40154595    | 426      | 5111769   
    l1i_cache:u        | 655235716   | 3017336  | 112978092 
    l1i_cache_refill:u | 88683822    | 694      | 60584892  
    l1i_tlb:u          | 655235716   | 3017336  | 112978092 
    l1i_tlb_refill:u   | 1440419     | 45       | 21008874  
    l2i_cache:u        | 88683804    | 693      | 60584855  
    l2i_cache_refill:u | 88660974    | 623      | 60532567  
    l2i_tlb:u          | 1445950     | 130      | 21019916  
    l2i_tlb_refill:u   | 1439916     | 12       | 17022011  
    l1d_cache:u        | 378648587   | 2695433  | 107897151 
    l1d_cache_refill:u | 168363358   | 290529   | 345664    
    l1d_tlb:u          | 835769044   | 2747484  | 108809878 
    l1d_tlb_refill:u   | 160512741   | 26601    | 3874      
    l2d_cache:u        | 1046356342  | 3743564  | 82712074  
    l2d_cache_refill:u | 593049671   | 2167     | 61682834  
    l2d_tlb:u          | 160780966   | 26625    | 3970      
    l2d_tlb_refill:u   | 160410685   | 5        | 3846      
    ll_cache:u         | 376718700   | 1543     | 634163    
    ll_cache_miss:u    | 322792918   | 69       | 7723      
combined_orders:
    id        | modules                                                                                                                                                                      
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33+hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4+itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64
    shuffle   | hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4+itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64+cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33
    sum       | cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33+hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4+itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 68089504973 | 67818792517 | 67084999582
    instructions:u     | 1729952662  | 1729952635  | 1729973813 
    br_retired:u       | 156082011   | 156082007   | 156084347  
    br_mis_pred:u      | 45204787    | 45371778    | 45266790   
    l1i_cache:u        | 717805927   | 735045397   | 771231144  
    l1i_cache_refill:u | 148181126   | 148208170   | 149269408  
    l1i_tlb:u          | 717805927   | 735045397   | 771231144  
    l1i_tlb_refill:u   | 22451013    | 22451128    | 22449338   
    l2i_cache:u        | 148181057   | 148208128   | 149269352  
    l2i_cache_refill:u | 148112152   | 148153955   | 149194164  
    l2i_tlb:u          | 23670873    | 23672928    | 22465996   
    l2i_tlb_refill:u   | 18512441    | 18515178    | 18461939   
    l1d_cache:u        | 485755865   | 486542902   | 489241171  
    l1d_cache_refill:u | 178048463   | 176269542   | 168999551  
    l1d_tlb:u          | 934478714   | 938115420   | 947326406  
    l1d_tlb_refill:u   | 160553421   | 160538080   | 160543216  
    l2d_cache:u        | 1140513791  | 1143864686  | 1132811980 
    l2d_cache_refill:u | 662791535   | 661447135   | 654734672  
    l2d_tlb:u          | 160850417   | 160774474   | 160811561  
    l2d_tlb_refill:u   | 160443189   | 160419279   | 160414536  
    ll_cache:u         | 384487214   | 386679672   | 377354406  
    ll_cache_miss:u    | 331762164   | 331329549   | 322800710  

### Combined Memory Layouts
#### canonical: `cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33+hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4+itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=537006080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=537079808 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s8192_bp4_cold_128k_ns_n16384_p32_np512_l2_r100_sn4_itlb_f2048_l1_d4_hot_2k_ns_n256_p1_np512_l4_r100_sn64_main_b4000_d1_lin_dtlb_512m_ps_n524288_p131072_np4_l4_r100_sp33: `hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4+itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64+cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=537006080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=537079808 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b4000_d1_linear_dtlb_512m_pstr_n524288_p131072_np4_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp4_r100_cold_128k_nstr_n16384_p32_np512_l2_sn4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=131072 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=196608 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l1_r100_hot_2k_nstr_n256_p1_np512_l4_sn64`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4096 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=69632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_051_s3

### Selected Cases
- `fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=1`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=8192`, `data_pool_nodes=32768`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1`: `branch_pairs_per_unit=3`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=32768`, `data_pool_nodes=65536`, `data_stride_pages=1`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=4096`
- `itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16`: `data_level=4m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1024`, `data_pool_nodes=524288`, `data_stride_lines=16`, `data_stride_nodes=16`, `data_template=cold`, `direct_run_len=4`, `funcs=256`, `fusion_ldr_per_unit=4`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257+hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1+itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257
    s1 | hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1         
    s2 | itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16       
single_counts:
    metric             | s0        | s1        | s2       
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 539813952 | 387143872 | 990745721
    instructions:u     | 20150942  | 11920957  | 109740951
    br_retired:u       | 2631392   | 2021391   | 3911393  
    br_mis_pred:u      | 597842    | 435       | 631002   
    l1i_cache:u        | 8932064   | 1612244   | 21676335 
    l1i_cache_refill:u | 1144      | 1143      | 9924376  
    l1i_tlb:u          | 8932064   | 1612244   | 21676335 
    l1i_tlb_refill:u   | 60        | 41        | 2636036  
    l2i_cache:u        | 1144      | 1143      | 9924370  
    l2i_cache_refill:u | 875       | 674       | 9782824  
    l2i_tlb:u          | 114       | 90        | 2636790  
    l2i_tlb_refill:u   | 56        | 36        | 86307    
    l1d_cache:u        | 6011918   | 1421020   | 23795666 
    l1d_cache_refill:u | 2559775   | 1278386   | 4054097  
    l1d_tlb:u          | 13124697  | 4100825   | 25138889 
    l1d_tlb_refill:u   | 2602588   | 1305665   | 700067   
    l2d_cache:u        | 14336039  | 6656339   | 116016196
    l2d_cache_refill:u | 6172002   | 2738981   | 51974475 
    l2d_tlb:u          | 2604721   | 1306993   | 701049   
    l2d_tlb_refill:u   | 2549930   | 1283061   | 330191   
    ll_cache:u         | 6081575   | 2702123   | 41968289 
    ll_cache_miss:u    | 1688929   | 2534006   | 113132   
combined_orders:
    id        | modules                                                                                                                                                                              
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257+hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1+itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16
    shuffle   | hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1+itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16+fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257
    sum       | fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257+hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1+itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 2147505237 | 2132140116 | 1917703545
    instructions:u     | 141791548  | 141791542  | 141812850 
    br_retired:u       | 8561790    | 8561792    | 8564176   
    br_mis_pred:u      | 1225299    | 1225124    | 1229279   
    l1i_cache:u        | 34185138   | 33176157   | 32220643  
    l1i_cache_refill:u | 9960260    | 9970668    | 9926663   
    l1i_tlb:u          | 34185138   | 33176157   | 32220643  
    l1i_tlb_refill:u   | 2654460    | 2654463    | 2636137   
    l2i_cache:u        | 9960253    | 9970662    | 9926657   
    l2i_cache_refill:u | 9667573    | 9792988    | 9784373   
    l2i_tlb:u          | 2664661    | 2664636    | 2636994   
    l2i_tlb_refill:u   | 132938     | 132905     | 86399     
    l1d_cache:u        | 31181784   | 31232239   | 31228604  
    l1d_cache_refill:u | 7862798    | 7937833    | 7892258   
    l1d_tlb:u          | 42509350   | 42626521   | 42364411  
    l1d_tlb_refill:u   | 4623671    | 4615607    | 4608320   
    l2d_cache:u        | 143342724  | 143478897  | 137008574 
    l2d_cache_refill:u | 62311605   | 62691141   | 60885458  
    l2d_tlb:u          | 4639400    | 4628077    | 4612763   
    l2d_tlb_refill:u   | 4248678    | 4247927    | 4163182   
    ll_cache:u         | 52160243   | 52308330   | 50751987  
    ll_cache_miss:u    | 8003774    | 7949469    | 4336067   

### Combined Memory Layouts
#### canonical: `fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257+hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1+itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=171966464 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=172040192 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp3_dtlb_128m_ps_n65536_p32768_np2_l2_r100_sp1_itlb_f256_l2_d4_cold_4m_ns_n524288_p1024_np512_l4_r100_sn16_fetch_b64_d1_bp1_s16_dtlb_32m_ps_n32768_p8192_np4_l4_r100_sp257: `hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1+itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16+fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=171966464 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=172040192 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d1_bp1_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l4_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp3_r100_dtlb_128m_pstr_n65536_p32768_np2_l2_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l2_r100_cold_4m_nstr_n524288_p1024_np512_l4_sn16`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4194304 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4259840 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_052_s3

### Selected Cases
- `cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7`: `blocks=6000`, `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=4096`, `data_pool_nodes=8192`, `data_stride_pages=7`, `data_template=dtlb`, `direct_run_len=16`, `fusion_ldr_per_unit=4`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=2`, `data_level=8k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=2`, `data_pool_nodes=1024`, `data_stride_lines=2`, `data_stride_nodes=2`, `data_template=hot`, `direct_run_len=2`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1`: `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=16384`, `data_pool_nodes=16384`, `data_stride_pages=1`, `data_template=dtlb`, `direct_run_len=0`, `funcs=512`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2+itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1`

### Results
single_modules:
    id | module                                                     
    ---+------------------------------------------------------------
    s0 | cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7 
    s1 | fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2
    s2 | itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1   
single_counts:
    metric             | s0          | s1       | s2        
    -------------------+-------------+----------+-----------
    cpu-cycles:u       | 42392650679 | 15827428 | 3995475614
    instructions:u     | 1241562071  | 15351049 | 92570723  
    br_retired:u       | 67571612    | 2631410  | 5211332   
    br_mis_pred:u      | 3762462     | 290407   | 625       
    l1i_cache:u        | 252324646   | 6337369  | 11652331  
    l1i_cache_refill:u | 130903773   | 667      | 14748997  
    l1i_tlb:u          | 252324646   | 6337369  | 11652331  
    l1i_tlb_refill:u   | 2872875     | 48       | 5160060   
    l2i_cache:u        | 130903737   | 666      | 14749043  
    l2i_cache_refill:u | 121696148   | 612      | 13921159  
    l2i_tlb:u          | 2876027     | 78       | 5160210   
    l2i_tlb_refill:u   | 2160178     | 14       | 4144505   
    l1d_cache:u        | 258868234   | 2995491  | 10378226  
    l1d_cache_refill:u | 242348603   | 197      | 10234596  
    l1d_tlb:u          | 736659121   | 3062131  | 31015644  
    l1d_tlb_refill:u   | 240181273   | 63       | 10279887  
    l2d_cache:u        | 1382425194  | 1592     | 71390796  
    l2d_cache_refill:u | 634529890   | 911      | 34574665  
    l2d_tlb:u          | 240190862   | 83       | 10281172  
    l2d_tlb_refill:u   | 237197489   | 5        | 10268437  
    ll_cache:u         | 507662580   | 350      | 20568479  
    ll_cache_miss:u    | 10892822    | 22       | 19076542  
combined_orders:
    id        | modules                                                                                                                                                                        
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2+itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1
    shuffle   | fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2+itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1+cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7
    sum       | cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2+itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 46892949439 | 47074065212 | 46403953721
    instructions:u     | 1349462620  | 1349462553  | 1349483843 
    br_retired:u       | 75412005    | 75411997    | 75414354   
    br_mis_pred:u      | 4061961     | 4073853     | 4053494    
    l1i_cache:u        | 277625706   | 272695542   | 270314346  
    l1i_cache_refill:u | 146436244   | 146612787   | 145653437  
    l1i_tlb:u          | 277625706   | 272695542   | 270314346  
    l1i_tlb_refill:u   | 8049649     | 8049581     | 8032983    
    l2i_cache:u        | 146436221   | 146612747   | 145653446  
    l2i_cache_refill:u | 140639107   | 137370799   | 135617919  
    l2i_tlb:u          | 8053587     | 8056735     | 8036315    
    l2i_tlb_refill:u   | 7009081     | 7033539     | 6304697    
    l1d_cache:u        | 272230449   | 272235335   | 272241951  
    l1d_cache_refill:u | 252970520   | 252535063   | 252583396  
    l1d_tlb:u          | 770780852   | 770728856   | 770736896  
    l1d_tlb_refill:u   | 250471807   | 250471911   | 250461223  
    l2d_cache:u        | 1458305916  | 1456801571  | 1453817582 
    l2d_cache_refill:u | 678801012   | 673950133   | 669105466  
    l2d_tlb:u          | 250485195   | 250485714   | 250472117  
    l2d_tlb_refill:u   | 247453780   | 247441438   | 247465931  
    ll_cache:u         | 531103153   | 530366708   | 528231409  
    ll_cache_miss:u    | 33436717    | 35460751    | 29969386   

### Combined Memory Layouts
#### canonical: `cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2+itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=83894272 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=83968000 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d2_bp2_s16_hot_8k_ns_n1024_p2_np512_l2_r100_sn2_itlb_f512_l1_d0_dtlb_64m_ps_n16384_p16384_np1_l2_r100_sp1_main_b6000_d16_bitrev_dtlb_16m_ps_n8192_p4096_np2_l4_r100_sp7: `fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2+itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1+cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=83894272 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=83968000 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b6000_d16_bitrev_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b64_d2_bp2_s16_r100_hot_8k_nstr_n1024_p2_np512_l2_sn2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=8192 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=73728 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l1_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_053_s3

### Selected Cases
- `fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=4`, `data_level=64k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=16`, `data_pool_nodes=8192`, `data_stride_lines=4`, `data_stride_nodes=4`, `data_template=cold`, `direct_run_len=8`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129`: `branch_pairs_per_unit=2`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=65536`, `data_pool_nodes=524288`, `data_stride_pages=129`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65`: `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=4096`, `data_pool_nodes=8192`, `data_stride_pages=65`, `data_template=dtlb`, `direct_run_len=0`, `funcs=1024`, `fusion_ldr_per_unit=4`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4+hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129+itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65`

### Results
single_modules:
    id | module                                                        
    ---+---------------------------------------------------------------
    s0 | fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4
    s1 | hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129   
    s2 | itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65      
single_counts:
    metric             | s0       | s1        | s2        
    -------------------+----------+-----------+-----------
    cpu-cycles:u       | 7056782  | 819659935 | 7962293173
    instructions:u     | 12071046 | 13200951  | 205210723 
    br_retired:u       | 3431407  | 1381393   | 10331332  
    br_mis_pred:u      | 60478    | 446       | 1432      
    l1i_cache:u        | 2360723  | 1797361   | 25798452  
    l1i_cache_refill:u | 629      | 1661      | 30261957  
    l1i_tlb:u          | 2360723  | 1797361   | 25798452  
    l1i_tlb_refill:u   | 48       | 39        | 10310043  
    l2i_cache:u        | 629      | 1663      | 30261941  
    l2i_cache_refill:u | 589      | 1639      | 30181518  
    l2i_tlb:u          | 85       | 88        | 10311186  
    l2i_tlb_refill:u   | 17       | 35        | 10300940  
    l1d_cache:u        | 1135268  | 2701671   | 41111705  
    l1d_cache_refill:u | 4754     | 2558469   | 40941152  
    l1d_tlb:u          | 1137442  | 7956172   | 123249478 
    l1d_tlb_refill:u   | 94       | 2586868   | 41015072  
    l2d_cache:u        | 78885    | 13203371  | 249566199 
    l2d_cache_refill:u | 1718     | 5951609   | 112818604 
    l2d_tlb:u          | 115      | 2588693   | 41019069  
    l2d_tlb_refill:u   | 6        | 2563931   | 40980900  
    ll_cache:u         | 1130     | 5205982   | 82170970  
    ll_cache_miss:u    | 82       | 4939559   | 112236    
combined_orders:
    id        | modules                                                                                                                                                                            
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4+hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129+itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65
    shuffle   | hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129+fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4+itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65
    sum       | fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4+hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129+itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 9029682156 | 8999081462 | 8789009890
    instructions:u     | 230461314  | 230461314  | 230482720 
    br_retired:u       | 15141731   | 15141731   | 15144132  
    br_mis_pred:u      | 62363      | 62635      | 62356     
    l1i_cache:u        | 30067243   | 30087373   | 29956536  
    l1i_cache_refill:u | 30195471   | 30238039   | 30264247  
    l1i_tlb:u          | 30067243   | 30087373   | 29956536  
    l1i_tlb_refill:u   | 10310444   | 10310521   | 10310130  
    l2i_cache:u        | 30195460   | 30238030   | 30264233  
    l2i_cache_refill:u | 30049112   | 30146698   | 30183746  
    l2i_tlb:u          | 10311660   | 10311879   | 10311359  
    l2i_tlb_refill:u   | 10293222   | 10292719   | 10300992  
    l1d_cache:u        | 44940643   | 44942945   | 44948644  
    l1d_cache_refill:u | 43483293   | 43492514   | 43504375  
    l1d_tlb:u          | 132335983  | 132240731  | 132343092 
    l1d_tlb_refill:u   | 43628915   | 43599582   | 43602034  
    l2d_cache:u        | 264540289  | 264838139  | 262848455 
    l2d_cache_refill:u | 120056952  | 120161312  | 118771931 
    l2d_tlb:u          | 43633173   | 43612630   | 43607877  
    l2d_tlb_refill:u   | 43502671   | 43476398   | 43544837  
    ll_cache:u         | 88277115   | 88348646   | 87378082  
    ll_cache_miss:u    | 6020074    | 5694771    | 5051877   

### Combined Memory Layouts
#### canonical: `fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4+hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129+itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=285278208 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=285351936 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp2_dtlb_256m_ps_n524288_p65536_np8_l4_r100_sp129_fetch_b64_d8_bp4_s16_cold_64k_ns_n8192_p16_np512_l1_r100_sn4_itlb_f1024_l1_d0_dtlb_16m_ps_n8192_p4096_np2_l4_r100_sp65: `hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129+fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4+itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=285278208 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=285351936 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d8_bp4_s16_r100_cold_64k_nstr_n8192_p16_np512_l1_sn4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=65536 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=131072 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_dtlb_256m_pstr_n524288_p65536_np8_l4_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f1024_l1_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_054_s3

### Selected Cases
- `cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65`: `blocks=10000`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=32768`, `data_pool_nodes=131072`, `data_stride_pages=65`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=0`, `data_level=16k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=4`, `data_pool_nodes=2048`, `data_stride_lines=32`, `data_stride_nodes=32`, `data_template=hot`, `direct_run_len=4`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17`: `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=131072`, `data_pool_nodes=524288`, `data_stride_pages=17`, `data_template=dtlb`, `direct_run_len=4`, `funcs=4096`, `fusion_ldr_per_unit=1`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65+fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32+itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17`

### Results
single_modules:
    id | module                                                         
    ---+----------------------------------------------------------------
    s0 | cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65
    s1 | fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32 
    s2 | itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17  
single_counts:
    metric             | s0           | s1       | s2         
    -------------------+--------------+----------+------------
    cpu-cycles:u       | 134209997506 | 34150064 | 24756794313
    instructions:u     | 2275312020   | 29431012 | 809260940  
    br_retired:u       | 150071605    | 1991403  | 61511388   
    br_mis_pred:u      | 25002329     | 290628   | 10235806   
    l1i_cache:u        | 631348788    | 8088135  | 224260865  
    l1i_cache_refill:u | 219760191    | 838      | 120843593  
    l1i_tlb:u          | 631348788    | 8088135  | 224260865  
    l1i_tlb_refill:u   | 3562287      | 51       | 41866491   
    l2i_cache:u        | 219760106    | 836      | 120843523  
    l2i_cache_refill:u | 219744916    | 726      | 120825407  
    l2i_tlb:u          | 3577746      | 97       | 41875364   
    l2i_tlb_refill:u   | 3552371      | 14       | 40873642   
    l1d_cache:u        | 527257691    | 6815311  | 94972686   
    l1d_cache_refill:u | 419529924    | 359      | 43221250   
    l1d_tlb:u          | 1333685566   | 6817127  | 182011892  
    l1d_tlb_refill:u   | 400484274    | 82       | 41182191   
    l2d_cache:u        | 2356753089   | 2122     | 405222570  
    l2d_cache_refill:u | 1140788894   | 1184     | 263497283  
    l2d_tlb:u          | 400505271    | 100      | 41188323   
    l2d_tlb_refill:u   | 400431092    | 4        | 41148391   
    ll_cache:u         | 865006646    | 467      | 100073800  
    ll_cache_miss:u    | 788862680    | 15       | 88150753   
combined_orders:
    id        | modules                                                                                                                                                                                     
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65+fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32+itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17
    shuffle   | fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32+cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65+itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17
    sum       | cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65+fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32+itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 163605937581 | 163066850545 | 159000941883
    instructions:u     | 3113982580   | 3113982651   | 3114003972  
    br_retired:u       | 213572001    | 213572010    | 213574396   
    br_mis_pred:u      | 35567867     | 35576922     | 35528763    
    l1i_cache:u        | 860627795    | 887244833    | 863697788   
    l1i_cache_refill:u | 340314708    | 340493835    | 340604622   
    l1i_tlb:u          | 860627795    | 887244833    | 863697788   
    l1i_tlb_refill:u   | 45453592     | 45467163     | 45428829    
    l2i_cache:u        | 340314500    | 340493713    | 340604465   
    l2i_cache_refill:u | 340220036    | 340379935    | 340571049   
    l2i_tlb:u          | 48438373     | 48449842     | 45453207    
    l2i_tlb_refill:u   | 44468020     | 44512751     | 44426027    
    l1d_cache:u        | 630723595    | 630680806    | 629045688   
    l1d_cache_refill:u | 464482062    | 464834995    | 462751533   
    l1d_tlb:u          | 1524515072   | 1524440794   | 1522514585  
    l1d_tlb_refill:u   | 441693030    | 441693144    | 441666547   
    l2d_cache:u        | 2771685811   | 2772850315   | 2761977781  
    l2d_cache_refill:u | 1420269633   | 1419576037   | 1404287361  
    l2d_tlb:u          | 441716068    | 441718457    | 441693694   
    l2d_tlb_refill:u   | 441584344    | 441598675    | 441579487   
    ll_cache:u         | 974418097    | 973771519    | 965080913   
    ll_cache_miss:u    | 887321902    | 886629897    | 877013448   

### Combined Memory Layouts
#### canonical: `cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65+fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32+itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=671105024 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=671178752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d4_bp0_s16_hot_16k_ns_n2048_p4_np512_l4_r100_sn32_main_b10000_d4_lin_dtlb_128m_ps_n131072_p32768_np4_l4_r100_sp65_itlb_f4096_l1_d4_dtlb_512m_ps_n524288_p131072_np4_l1_r100_sp17: `fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32+cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65+itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=671105024 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=671178752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b10000_d4_linear_dtlb_128m_pstr_n131072_p32768_np4_l4_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d4_bp0_s16_r100_hot_16k_nstr_n2048_p4_np512_l4_sn32`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16384 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=81920 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l1_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_055_s3

### Selected Cases
- `cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17`: `blocks=18000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=8192`, `data_pool_nodes=16384`, `data_stride_pages=17`, `data_template=dtlb`, `direct_run_len=2`, `fusion_ldr_per_unit=2`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=4`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=8192`, `data_pool_nodes=32768`, `data_stride_pages=65`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1`: `branch_pairs_per_unit=3`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=65536`, `data_pool_nodes=65536`, `data_stride_pages=1`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17+fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1`

### Results
single_modules:
    id | module                                                          
    ---+-----------------------------------------------------------------
    s0 | cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17    
    s1 | fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65
    s2 | hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1        
single_counts:
    metric             | s0           | s1        | s2       
    -------------------+--------------+-----------+----------
    cpu-cycles:u       | 100922767751 | 139120770 | 194708576
    instructions:u     | 4230312085   | 12950988  | 11281003 
    br_retired:u       | 360071616    | 3591403   | 2021402  
    br_mis_pred:u      | 90430986     | 130704    | 418      
    l1i_cache:u        | 1756283224   | 3523356   | 1515858  
    l1i_cache_refill:u | 384325953    | 784       | 836      
    l1i_tlb:u          | 1756283224   | 3523356   | 1515858  
    l1i_tlb_refill:u   | 8595693      | 43        | 39       
    l2i_cache:u        | 384325715    | 783       | 837      
    l2i_cache_refill:u | 383589375    | 682       | 651      
    l2i_tlb:u          | 8611249      | 84        | 125      
    l2i_tlb_refill:u   | 6436775      | 39        | 35       
    l1d_cache:u        | 823089928    | 1538457   | 778194   
    l1d_cache_refill:u | 381852623    | 640498    | 639949   
    l1d_tlb:u          | 1614312377   | 2935812   | 2171078  
    l1d_tlb_refill:u   | 361616395    | 665075    | 665244   
    l2d_cache:u        | 2540098856   | 3611990   | 3250191  
    l2d_cache_refill:u | 1261727970   | 1547344   | 1333632  
    l2d_tlb:u          | 361638507    | 665115    | 665959   
    l2d_tlb_refill:u   | 360579110    | 641320    | 641536   
    ll_cache:u         | 854947543    | 1533326   | 1283045  
    ll_cache_miss:u    | 252813483    | 441325    | 1217410  
combined_orders:
    id        | modules                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17+fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1
    shuffle   | fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65+cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1
    sum       | cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17+fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 104310817382 | 103157878706 | 101256597097
    instructions:u     | 4254522608   | 4254522592   | 4254544076  
    br_retired:u       | 365682003    | 365682002    | 365684421   
    br_mis_pred:u      | 90650038     | 90805168     | 90562108    
    l1i_cache:u        | 1637191528   | 1641770970   | 1761322438  
    l1i_cache_refill:u | 384573200    | 384535566    | 384327573   
    l1i_tlb:u          | 1637191528   | 1641770970   | 1761322438  
    l1i_tlb_refill:u   | 8617683      | 8617346      | 8595775     
    l2i_cache:u        | 384572961    | 384535326    | 384327335   
    l2i_cache_refill:u | 383811909    | 383741091    | 383590708   
    l2i_tlb:u          | 8628054      | 8626367      | 8611458     
    l2i_tlb_refill:u   | 6436580      | 6416873      | 6436849     
    l1d_cache:u        | 817448888    | 818041887    | 825406579   
    l1d_cache_refill:u | 418761560    | 416239947    | 383133070   
    l1d_tlb:u          | 1567495808   | 1571070617   | 1619419267  
    l1d_tlb_refill:u   | 362970141    | 363010244    | 362946714   
    l2d_cache:u        | 2548768943   | 2531126234   | 2546961037  
    l2d_cache_refill:u | 1267142777   | 1270809762   | 1264608946  
    l2d_tlb:u          | 363373128    | 363234902    | 362969581   
    l2d_tlb_refill:u   | 361618326    | 361894466    | 361861966   
    ll_cache:u         | 859370057    | 862532349    | 857763914   
    ll_cache_miss:u    | 270357397    | 266072388    | 254472218   

### Combined Memory Layouts
#### canonical: `cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17+fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=335544320 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=335618048 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d4_bp4_s16_dtlb_32m_ps_n32768_p8192_np4_l1_r100_sp65_main_b18000_d2_bitrev_dtlb_32m_ps_n16384_p8192_np2_l2_r100_sp17_hot_s4096_bp3_dtlb_256m_ps_n65536_p65536_np1_l1_r100_sp1: `fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65+cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=335544320 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=335618048 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b18000_d2_bitrev_dtlb_32m_pstr_n16384_p8192_np2_l2_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b64_d4_bp4_s16_r100_dtlb_32m_pstr_n32768_p8192_np4_l1_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_056_s3

### Selected Cases
- `cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16`: `blocks=6000`, `data_level=16k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=4`, `data_pool_nodes=2048`, `data_stride_lines=16`, `data_stride_nodes=16`, `data_template=hot`, `direct_run_len=16`, `fusion_ldr_per_unit=1`, `layout=in_page_shuffle`, `region_reps=100`
- `hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129`: `branch_pairs_per_unit=3`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=65536`, `data_pool_nodes=65536`, `data_stride_pages=129`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`
- `itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17`: `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=262144`, `data_pool_nodes=2097152`, `data_stride_pages=17`, `data_template=dtlb`, `direct_run_len=0`, `funcs=256`, `fusion_ldr_per_unit=1`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129+itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17`

### Results
single_modules:
    id | module                                                     
    ---+------------------------------------------------------------
    s0 | cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16  
    s1 | hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129 
    s2 | itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17
single_counts:
    metric             | s0         | s1        | s2        
    -------------------+------------+-----------+-----------
    cpu-cycles:u       | 5641771369 | 205250907 | 1282449751
    instructions:u     | 1061560723 | 11280997  | 43930951  
    br_retired:u       | 67571332   | 2021404   | 2651393   
    br_mis_pred:u      | 3766080    | 429       | 515       
    l1i_cache:u        | 224473615  | 1517756   | 5778162   
    l1i_cache_refill:u | 120923040  | 815       | 6995937   
    l1i_tlb:u          | 224473615  | 1517756   | 5778162   
    l1i_tlb_refill:u   | 2694107    | 42        | 2580054   
    l2i_cache:u        | 120922985  | 814       | 6995934   
    l2i_cache_refill:u | 105204761  | 619       | 5681714   
    l2i_tlb:u          | 2696257    | 118       | 2580148   
    l2i_tlb_refill:u   | 240        | 39        | 432354    
    l1d_cache:u        | 78861619   | 778353    | 2696882   
    l1d_cache_refill:u | 3229106    | 640351    | 2559474   
    l1d_tlb:u          | 78922334   | 2170987   | 7943139   
    l1d_tlb_refill:u   | 10905      | 665242    | 2586687   
    l2d_cache:u        | 137201171  | 3278345   | 20307870  
    l2d_cache_refill:u | 107005421  | 1509854   | 13585528  
    l2d_tlb:u          | 10923      | 666020    | 2586953   
    l2d_tlb_refill:u   | 50         | 641013    | 2564191   
    ll_cache:u         | 3606880    | 1283877   | 5100354   
    ll_cache_miss:u    | 132981     | 1235188   | 4910791   
combined_orders:
    id        | modules                                                                                                                                                                         
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129+itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17
    shuffle   | hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129+cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16+itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17
    sum       | cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129+itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 7083469652 | 7022026809 | 7129472027
    instructions:u     | 1116751320 | 1116751320 | 1116772671
    br_retired:u       | 72241729   | 72241729   | 72244129  
    br_mis_pred:u      | 3762922    | 3767578    | 3767024   
    l1i_cache:u        | 242482962  | 242638031  | 231769533 
    l1i_cache_refill:u | 128078267  | 127648727  | 127919792 
    l1i_tlb:u          | 242482962  | 242638031  | 231769533 
    l1i_tlb_refill:u   | 5282082    | 5282376    | 5274203   
    l2i_cache:u        | 128078202  | 127648679  | 127919733 
    l2i_cache_refill:u | 109946179  | 106310532  | 110887094 
    l2i_tlb:u          | 5285056    | 5290276    | 5276523   
    l2i_tlb_refill:u   | 482548     | 483268     | 432633    
    l1d_cache:u        | 82333524   | 82332756   | 82336854  
    l1d_cache_refill:u | 7015387    | 6054219    | 6428931   
    l1d_tlb:u          | 89082365   | 89098374   | 89036460  
    l1d_tlb_refill:u   | 3288273    | 3287899    | 3262834   
    l2d_cache:u        | 160250827  | 162282596  | 160787386 
    l2d_cache_refill:u | 126168689  | 119551604  | 122100803 
    l2d_tlb:u          | 3296898    | 3296592    | 3263896   
    l2d_tlb_refill:u   | 3209704    | 3210004    | 3205254   
    ll_cache:u         | 12601792   | 12417179   | 9991111   
    ll_cache_miss:u    | 8553182    | 8709311    | 6278960   

### Combined Memory Layouts
#### canonical: `cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16+hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129+itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1342193664 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1342267392 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp3_dtlb_256m_ps_n65536_p65536_np1_l1_r100_sp129_main_b6000_d16_bitrev_hot_16k_ns_n2048_p4_np512_l1_r100_sn16_itlb_f256_l1_d0_dtlb_1g_ps_n2097152_p262144_np8_l1_r100_sp17: `hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129+cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16+itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1342193664 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1342267392 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b6000_d16_bitrev_hot_16k_nstr_n2048_p4_np512_l1_sn16`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16384 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=81920 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp3_r100_dtlb_256m_pstr_n65536_p65536_np1_l1_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l1_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_057_s3

### Selected Cases
- `cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048`: `blocks=13000`, `data_level=1m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=256`, `data_pool_nodes=131072`, `data_stride_lines=2048`, `data_stride_nodes=2048`, `data_template=cold`, `direct_run_len=4`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4`: `branch_pairs_per_unit=3`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=4`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=4096`
- `itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`: `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=1`, `data_template=dtlb`, `direct_run_len=0`, `funcs=512`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048+hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`

### Results
single_modules:
    id | module                                                         
    ---+----------------------------------------------------------------
    s0 | cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048
    s1 | hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4          
    s2 | itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1      
single_counts:
    metric             | s0          | s1        | s2        
    -------------------+-------------+-----------+-----------
    cpu-cycles:u       | 17106282314 | 259731896 | 4837118800
    instructions:u     | 2567810729  | 11921103  | 174490723 
    br_retired:u       | 195071330   | 2021414   | 5211332   
    br_mis_pred:u      | 32498728    | 388       | 778       
    l1i_cache:u        | 827543576   | 1600714   | 21926290  
    l1i_cache_refill:u | 259390527   | 975       | 19939471  
    l1i_tlb:u          | 827543576   | 1600714   | 21926290  
    l1i_tlb_refill:u   | 4222869     | 40        | 5160065   
    l2i_cache:u        | 259390374   | 974       | 19939481  
    l2i_cache_refill:u | 259386003   | 602       | 19938636  
    l2i_tlb:u          | 8181780     | 104       | 5160359   
    l2i_tlb_refill:u   | 34981       | 35        | 4247347   
    l1d_cache:u        | 295650714   | 1419301   | 10378097  
    l1d_cache_refill:u | 146279866   | 1279837   | 10236377  
    l1d_tlb:u          | 440068650   | 4093376   | 31017489  
    l1d_tlb_refill:u   | 130636951   | 1305156   | 10279773  
    l2d_cache:u        | 748494318   | 6495384   | 76443405  
    l2d_cache_refill:u | 381804632   | 2590524   | 41814239  
    l2d_tlb:u          | 130643428   | 1306105   | 10281435  
    l2d_tlb_refill:u   | 146734      | 1282073   | 10269508  
    ll_cache:u         | 123397590   | 2564156   | 20537471  
    ll_cache_miss:u    | 986261      | 632035    | 19411249  
combined_orders:
    id        | modules                                                                                                                                                                        
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048+hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1
    shuffle   | hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048+itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1
    sum       | cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048+hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 17095104157 | 21225665892 | 22203133010
    instructions:u     | 2754201327  | 2754201537  | 2754222555 
    br_retired:u       | 202301731   | 202301785   | 202304076  
    br_mis_pred:u      | 32501556    | 32505011    | 32499894   
    l1i_cache:u        | 720299910   | 772882489   | 851070580  
    l1i_cache_refill:u | 283812132   | 283998122   | 279330973  
    l1i_tlb:u          | 720299910   | 772882489   | 851070580  
    l1i_tlb_refill:u   | 9392465     | 9393695     | 9382974    
    l2i_cache:u        | 283811958   | 283997969   | 279330829  
    l2i_cache_refill:u | 283701549   | 283883042   | 279325241  
    l2i_tlb:u          | 9405308     | 9406287     | 13342243   
    l2i_tlb_refill:u   | 4961820     | 4955076     | 4282363    
    l1d_cache:u        | 306093946   | 306882326   | 307448112  
    l1d_cache_refill:u | 149863504   | 168947814   | 157796080  
    l1d_tlb:u          | 466080080   | 466849135   | 475179515  
    l1d_tlb_refill:u   | 142269580   | 142268821   | 142221880  
    l2d_cache:u        | 831053495   | 780458268   | 831433107  
    l2d_cache_refill:u | 441950349   | 427467900   | 426209395  
    l2d_tlb:u          | 142276012   | 142278475   | 142230968  
    l2d_tlb_refill:u   | 11626346    | 11814888    | 11698315   
    ll_cache:u         | 157845672   | 142017913   | 146499217  
    ll_cache_miss:u    | 25987900    | 27727153    | 21029545   

### Combined Memory Layouts
#### canonical: `cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048+hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1108344832 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1108418560 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s4096_bp3_dtlb_32m_ps_n8192_p8192_np1_l2_r100_sp4_main_b13000_d4_lin_cold_1m_ns_n131072_p256_np512_l1_r100_sn2048_itlb_f512_l2_d0_dtlb_1g_ps_n262144_p262144_np1_l1_r100_sp1: `hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048+itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1108344832 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1108418560 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b13000_d4_linear_cold_1m_nstr_n131072_p256_np512_l1_sn2048`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1048576 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1114112 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l2_r100_dtlb_1g_pstr_n262144_p262144_np1_l1_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_058_s3

### Selected Cases
- `cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5`: `blocks=19000`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=5`, `data_template=dtlb`, `direct_run_len=2`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=2`, `data_level=256m`, `data_mode=random`, `data_nodes_per_page=8`, `data_pages=65536`, `data_pool_nodes=524288`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7`: `branch_pairs_per_unit=4`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=131072`, `data_pool_nodes=524288`, `data_stride_pages=7`, `data_template=dtlb`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5+fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2+hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7`

### Results
single_modules:
    id | module                                                         
    ---+----------------------------------------------------------------
    s0 | cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5     
    s1 | fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2
    s2 | hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7    
single_counts:
    metric             | s0           | s1        | s2       
    -------------------+--------------+-----------+----------
    cpu-cycles:u       | 102250866714 | 888434775 | 431718613
    instructions:u     | 4465311956   | 37430955  | 22160951 
    br_retired:u       | 380071598    | 6471392   | 5221393  
    br_mis_pred:u      | 95025191     | 1239038   | 445      
    l1i_cache:u        | 1833085381   | 17428447  | 2880852  
    l1i_cache_refill:u | 397710975    | 2459      | 1191     
    l1i_tlb:u          | 1833085381   | 17428447  | 2880852  
    l1i_tlb_refill:u   | 6367121      | 45        | 43       
    l2i_cache:u        | 397710756    | 2459      | 1190     
    l2i_cache_refill:u | 397667630    | 2434      | 1161     
    l2i_tlb:u          | 12315259     | 95        | 152      
    l2i_tlb_refill:u   | 6360984      | 43        | 37       
    l1d_cache:u        | 872223739    | 9216447   | 1420540  
    l1d_cache_refill:u | 412149360    | 2624666   | 1280212  
    l1d_tlb:u          | 1728272085   | 18115147  | 4136305  
    l1d_tlb_refill:u   | 381707044    | 2600519   | 1319568  
    l2d_cache:u        | 2661857716   | 15161600  | 6520925  
    l2d_cache_refill:u | 1312577670   | 6864956   | 3597600  
    l2d_tlb:u          | 381727664    | 2614631   | 1320569  
    l2d_tlb_refill:u   | 380969808    | 2531480   | 1284204  
    ll_cache:u         | 896884352    | 5766662   | 2570488  
    ll_cache_miss:u    | 220781705    | 5324936   | 2381674  
combined_orders:
    id        | modules                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5+fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2+hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7
    shuffle   | hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7+fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2+cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5
    sum       | cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5+fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2+hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 101566985597 | 101785013444 | 103571020102
    instructions:u     | 4524882541   | 4524882592   | 4524903862  
    br_retired:u       | 391761995    | 391762002    | 391764383   
    br_mis_pred:u      | 96337497     | 96346567     | 96264674    
    l1i_cache:u        | 1609275455   | 1610324737   | 1853394680  
    l1i_cache_refill:u | 403322616    | 403289342    | 397714625   
    l1i_tlb:u          | 1609275455   | 1610324737   | 1853394680  
    l1i_tlb_refill:u   | 6381895      | 6382719      | 6367209     
    l2i_cache:u        | 403322349    | 403289094    | 397714405   
    l2i_cache_refill:u | 403233122    | 403204040    | 397671225   
    l2i_tlb:u          | 6403527      | 6409802      | 12315506    
    l2i_tlb_refill:u   | 6374420      | 6371803      | 6361064     
    l1d_cache:u        | 879908241    | 879477028    | 882860726   
    l1d_cache_refill:u | 411148332    | 410573529    | 416054238   
    l1d_tlb:u          | 1727810224   | 1726443260   | 1750523537  
    l1d_tlb_refill:u   | 385642847    | 385642092    | 385627131   
    l2d_cache:u        | 2685982042   | 2685163955   | 2683540241  
    l2d_cache_refill:u | 1329433636   | 1328555202   | 1323040226  
    l2d_tlb:u          | 385681800    | 385674122    | 385662864   
    l2d_tlb_refill:u   | 384776856    | 384789056    | 384785492   
    ll_cache:u         | 910949266    | 909884275    | 905221502   
    ll_cache_miss:u    | 239874714    | 239270563    | 228488315   

### Combined Memory Layouts
#### canonical: `cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5+fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2+hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=838860800 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=838934528 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_hot_s8192_bp4_dtlb_512m_ps_n524288_p131072_np4_l1_r100_sp7_fetch_b128_d1_bp2_s16_dtlb_256m_rnd_n524288_p65536_np8_l2_r100_main_b19000_d2_lin_dtlb_32m_ps_n8192_p8192_np1_l2_r100_sp5: `hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7+fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2+cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=838860800 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=838934528 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b19000_d2_linear_dtlb_32m_pstr_n8192_p8192_np1_l2_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d1_bp2_s16_r100_dtlb_256m_rand_n524288_p65536_np8_l2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp4_r100_dtlb_512m_pstr_n524288_p131072_np4_l1_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_059_s3

### Selected Cases
- `fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=0`, `data_level=4k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1`, `data_pool_nodes=512`, `data_stride_lines=8`, `data_stride_nodes=8`, `data_template=hot`, `direct_run_len=2`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512`: `branch_pairs_per_unit=4`, `data_level=2m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=512`, `data_pool_nodes=262144`, `data_stride_lines=512`, `data_stride_nodes=512`, `data_template=cold`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=4096`
- `itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32`: `data_level=16k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=4`, `data_pool_nodes=2048`, `data_stride_lines=32`, `data_stride_nodes=32`, `data_template=hot`, `direct_run_len=0`, `funcs=4096`, `fusion_ldr_per_unit=2`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8+hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512+itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32`

### Results
single_modules:
    id | module                                                    
    ---+-----------------------------------------------------------
    s0 | fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8
    s1 | hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512 
    s2 | itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32    
single_counts:
    metric             | s0       | s1       | s2         
    -------------------+----------+----------+------------
    cpu-cycles:u       | 20963510 | 22516026 | 11444554051
    instructions:u     | 16631049 | 11921049 | 1474970727 
    br_retired:u       | 1351410  | 2661410  | 41051331   
    br_mis_pred:u      | 290821   | 442      | 1577       
    l1i_cache:u        | 6579738  | 1578856  | 184643146  
    l1i_cache_refill:u | 672      | 616      | 165325534  
    l1i_tlb:u          | 6579738  | 1578856  | 184643146  
    l1i_tlb_refill:u   | 52       | 49       | 41140057   
    l2i_cache:u        | 671      | 615      | 165326074  
    l2i_cache_refill:u | 591      | 596      | 164017186  
    l2i_tlb:u          | 99       | 127      | 41141222   
    l2i_tlb_refill:u   | 43       | 42       | 40590955   
    l1d_cache:u        | 4275396  | 1415713  | 163978295  
    l1d_cache_refill:u | 177      | 164470   | 83413      
    l1d_tlb:u          | 4339692  | 2788043  | 164014149  
    l1d_tlb_refill:u   | 58       | 1300176  | 7653       
    l2d_cache:u        | 1252     | 499235   | 213554407  
    l2d_cache_refill:u | 826      | 172047   | 166173950  
    l2d_tlb:u          | 75       | 1300939  | 8053       
    l2d_tlb_refill:u   | 3        | 92       | 7627       
    ll_cache:u         | 241      | 171391   | 164331     
    ll_cache_miss:u    | 47       | 697      | 341        
combined_orders:
    id        | modules                                                                                                                                                                    
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8+hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512+itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32
    shuffle   | itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32+hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512+fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8
    sum       | fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8+hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512+itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 11343517847 | 11633963413 | 11488033587
    instructions:u     | 1503501314  | 1503501314  | 1503522825 
    br_retired:u       | 45061731    | 45061731    | 45064151   
    br_mis_pred:u      | 299363      | 296889      | 292840     
    l1i_cache:u        | 192792269   | 192813225   | 192801740  
    l1i_cache_refill:u | 165077175   | 165261526   | 165326822  
    l1i_tlb:u          | 192792269   | 192813225   | 192801740  
    l1i_tlb_refill:u   | 41140444    | 41140463    | 41140158   
    l2i_cache:u        | 165077129   | 165261465   | 165327360  
    l2i_cache_refill:u | 163747293   | 163910580   | 164018373  
    l2i_tlb:u          | 41141077    | 41141436    | 41141448   
    l2i_tlb_refill:u   | 40591415    | 40593501    | 40591040   
    l1d_cache:u        | 169660360   | 169660812   | 169669404  
    l1d_cache_refill:u | 323282      | 323780      | 248060     
    l1d_tlb:u          | 171223789   | 171229529   | 171141884  
    l1d_tlb_refill:u   | 1320321     | 1322328     | 1307887    
    l2d_cache:u        | 214305819   | 214704898   | 214054894  
    l2d_cache_refill:u | 166382311   | 166557661   | 166346823  
    l2d_tlb:u          | 1322592     | 1325882     | 1309067    
    l2d_tlb_refill:u   | 68721       | 69344       | 7722       
    ll_cache:u         | 520409      | 538438      | 335963     
    ll_cache_miss:u    | 9137        | 26715       | 1085       

### Combined Memory Layouts
#### canonical: `fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8+hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512+itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=2117632 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2191360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f4096_l2_d0_hot_16k_ns_n2048_p4_np512_l2_r100_sn32_hot_s4096_bp4_cold_2m_ns_n262144_p512_np512_l2_r100_sn512_fetch_b64_d2_bp0_s16_hot_4k_ns_n512_p1_np512_l4_r100_sn8: `itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32+hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512+fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=2117632 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2191360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d2_bp0_s16_r100_hot_4k_nstr_n512_p1_np512_l4_sn8`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4096 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=69632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp4_r100_cold_2m_nstr_n262144_p512_np512_l2_sn512`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=2097152 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2162688 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l2_r100_hot_16k_nstr_n2048_p4_np512_l2_sn32`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16384 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=81920 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_060_s3

### Selected Cases
- `fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=4`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=65536`, `data_pool_nodes=262144`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7`: `branch_pairs_per_unit=4`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=8192`, `data_pool_nodes=16384`, `data_stride_pages=7`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5`: `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=32768`, `data_pool_nodes=65536`, `data_stride_pages=5`, `data_template=dtlb`, `direct_run_len=4`, `funcs=2048`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129+hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7+itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5`

### Results
single_modules:
    id | module                                                               
    ---+----------------------------------------------------------------------
    s0 | fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129
    s1 | hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7               
    s2 | itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5           
single_counts:
    metric             | s0        | s1        | s2         
    -------------------+-----------+-----------+------------
    cpu-cycles:u       | 417159254 | 514565893 | 18743434150
    instructions:u     | 23830942  | 13200951  | 752940729  
    br_retired:u       | 6791392   | 2661393   | 30791330   
    br_mis_pred:u      | 140594    | 421       | 5115735    
    l1i_cache:u        | 4765217   | 1765878   | 162604617  
    l1i_cache_refill:u | 1530      | 1243      | 81534569   
    l1i_tlb:u          | 4765217   | 1765878   | 162604617  
    l1i_tlb_refill:u   | 45        | 45        | 20968337   
    l2i_cache:u        | 1529      | 1241      | 81534649   
    l2i_cache_refill:u | 1205      | 628       | 81482300   
    l2i_tlb:u          | 83        | 139       | 20982781   
    l2i_tlb_refill:u   | 43        | 40        | 20253970   
    l1d_cache:u        | 2177836   | 2701174   | 66684808   
    l1d_cache_refill:u | 1281295   | 2555664   | 41763024   
    l1d_tlb:u          | 4844688   | 7946051   | 149167819  
    l1d_tlb_refill:u   | 1305104   | 2589373   | 41086866   
    l2d_cache:u        | 7442281   | 13224791  | 325942796  
    l2d_cache_refill:u | 3641966   | 5349675   | 177820739  
    l2d_tlb:u          | 1306087   | 2590178   | 41089119   
    l2d_tlb_refill:u   | 1280428   | 2565157   | 41062453   
    ll_cache:u         | 3222352   | 5272393   | 92738450   
    ll_cache_miss:u    | 2882227   | 1301549   | 85362587   
combined_orders:
    id        | modules                                                                                                                                                                                
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129+hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7+itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5
    shuffle   | fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129+itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5+hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7
    sum       | fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129+hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7+itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 20116250866 | 20152167573 | 19675159297
    instructions:u     | 789951314   | 789951314   | 789972622  
    br_retired:u       | 40241731    | 40241731    | 40244115   
    br_mis_pred:u      | 5264727     | 5263227     | 5256750    
    l1i_cache:u        | 164490191   | 167366671   | 169135712  
    l1i_cache_refill:u | 81373400    | 81509849    | 81537342   
    l1i_tlb:u          | 164490191   | 167366671   | 169135712  
    l1i_tlb_refill:u   | 20972505    | 20972681    | 20968427   
    l2i_cache:u        | 81373492    | 81509943    | 81537419   
    l2i_cache_refill:u | 81326252    | 81467677    | 81484133   
    l2i_tlb:u          | 20988424    | 20984600    | 20983003   
    l2i_tlb_refill:u   | 20396714    | 20309241    | 20254053   
    l1d_cache:u        | 71540308    | 71555951    | 71563818   
    l1d_cache_refill:u | 45662996    | 45473448    | 45599983   
    l1d_tlb:u          | 162051889   | 162052387   | 161958558  
    l1d_tlb_refill:u   | 45038239    | 45022998    | 44981343   
    l2d_cache:u        | 350157278   | 346870189   | 346609868  
    l2d_cache_refill:u | 191282403   | 187090278   | 186812380  
    l2d_tlb:u          | 45044977    | 45028506    | 44985384   
    l2d_tlb_refill:u   | 44924725    | 44915504    | 44908038   
    ll_cache:u         | 105373936   | 101597134   | 101233195  
    ll_cache_miss:u    | 95943349    | 93067121    | 89546363   

### Combined Memory Layouts
#### canonical: `fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129+hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7+itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=436207616 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=436281344 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d8_bp4_s16_dtlb_256m_ps_n262144_p65536_np4_l1_r100_sp129_itlb_f2048_l2_d4_dtlb_128m_ps_n65536_p32768_np2_l1_r100_sp5_hot_s4096_bp4_dtlb_32m_ps_n16384_p8192_np2_l4_r100_sp7: `fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129+itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5+hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=436207616 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=436281344 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d8_bp4_s16_r100_dtlb_256m_pstr_n262144_p65536_np4_l1_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp4_r100_dtlb_32m_pstr_n16384_p8192_np2_l4_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l2_r100_dtlb_128m_pstr_n65536_p32768_np2_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_061_s3

### Selected Cases
- `cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257`: `blocks=4000`, `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=65536`, `data_pool_nodes=262144`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3`: `branch_pairs_per_unit=2`, `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=4096`, `data_pool_nodes=8192`, `data_stride_pages=3`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=8192`
- `itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5`: `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=5`, `data_template=dtlb`, `direct_run_len=0`, `funcs=2048`, `fusion_ldr_per_unit=1`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257+hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3+itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5`

### Results
single_modules:
    id | module                                                         
    ---+----------------------------------------------------------------
    s0 | cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257
    s1 | hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3         
    s2 | itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5        
single_counts:
    metric             | s0          | s1        | s2        
    -------------------+-------------+-----------+-----------
    cpu-cycles:u       | 28410103733 | 409817692 | 9711568207
    instructions:u     | 830311946   | 23440957  | 348570729 
    br_retired:u       | 60071594    | 2661391   | 20571330  
    br_mis_pred:u      | 10001158    | 463       | 1628      
    l1i_cache:u        | 242884648   | 3056034   | 43713562  
    l1i_cache_refill:u | 79862826    | 1237      | 60375991  
    l1i_tlb:u          | 242884648   | 3056034   | 43713562  
    l1i_tlb_refill:u   | 1351522     | 43        | 20530262  
    l2i_cache:u        | 79862779    | 1237      | 60376124  
    l2i_cache_refill:u | 64415556    | 671       | 60364890  
    l2i_tlb:u          | 1352951     | 133       | 20531289  
    l2i_tlb_refill:u   | 660715      | 37        | 19943751  
    l1d_cache:u        | 130697803   | 2699943   | 20627454  
    l1d_cache_refill:u | 81679271    | 2559050   | 20468476  
    l1d_tlb:u          | 292906005   | 7927070   | 61835209  
    l1d_tlb_refill:u   | 80192289    | 2586440   | 20534812  
    l2d_cache:u        | 537468180   | 12970568  | 186487081 
    l2d_cache_refill:u | 267738481   | 5171291   | 102683221 
    l2d_tlb:u          | 80197900    | 2587603   | 20536612  
    l2d_tlb_refill:u   | 80085535    | 2540459   | 20531720  
    ll_cache:u         | 188605534   | 5135038   | 41150789  
    ll_cache_miss:u    | 180839262   | 6805      | 26530547  
combined_orders:
    id        | modules                                                                                                                                                                       
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257+hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3+itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5
    shuffle   | itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5+cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257+hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3
    sum       | cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257+hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3+itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 39112067206 | 39436378891 | 38531489632
    instructions:u     | 1202302551  | 1202302618  | 1202323632 
    br_retired:u       | 83301997    | 83302005    | 83304315   
    br_mis_pred:u      | 9999909     | 10037773    | 10003249   
    l1i_cache:u        | 278768649   | 286272886   | 289654244  
    l1i_cache_refill:u | 139846549   | 139902379   | 140240054  
    l1i_tlb:u          | 278768649   | 286272886   | 289654244  
    l1i_tlb_refill:u   | 21881827    | 21881749    | 21881827   
    l2i_cache:u        | 139846613   | 139902453   | 140240140  
    l2i_cache_refill:u | 123824255   | 126486132   | 124781117  
    l2i_tlb:u          | 22965978    | 22969671    | 21884373   
    l2i_tlb_refill:u   | 20604081    | 20513806    | 20604503   
    l1d_cache:u        | 154020688   | 154254516   | 154025200  
    l1d_cache_refill:u | 105971456   | 105387859   | 104706797  
    l1d_tlb:u          | 361758872   | 363720691   | 362668284  
    l1d_tlb_refill:u   | 103323730   | 103348860   | 103313541  
    l2d_cache:u        | 740630368   | 737190110   | 736925829  
    l2d_cache_refill:u | 378363759   | 378261586   | 375592993  
    l2d_tlb:u          | 103329118   | 103357196   | 103322115  
    l2d_tlb_refill:u   | 103134236   | 103153895   | 103157714  
    ll_cache:u         | 240459996   | 236878060   | 234891361  
    ll_cache_miss:u    | 214010816   | 211870391   | 207376614  

### Combined Memory Layouts
#### canonical: `cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257+hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3+itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=318767104 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=318840832 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f2048_l1_d0_dtlb_32m_ps_n8192_p8192_np1_l1_r100_sp5_main_b4000_d4_lin_dtlb_256m_ps_n262144_p65536_np4_l2_r100_sp257_hot_s8192_bp2_dtlb_16m_ps_n8192_p4096_np2_l2_r100_sp3: `itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5+cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257+hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=318767104 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=318840832 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b4000_d4_linear_dtlb_256m_pstr_n262144_p65536_np4_l2_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp2_r100_dtlb_16m_pstr_n8192_p4096_np2_l2_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l1_r100_dtlb_32m_pstr_n8192_p8192_np1_l1_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_062_s3

### Selected Cases
- `fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=0`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=262144`, `data_pool_nodes=524288`, `data_stride_pages=33`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5`: `branch_pairs_per_unit=2`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=16384`, `data_pool_nodes=16384`, `data_stride_pages=5`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=4096`
- `itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33`: `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=32768`, `data_pool_nodes=262144`, `data_stride_pages=33`, `data_template=dtlb`, `direct_run_len=4`, `funcs=512`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33+hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5+itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33`

### Results
single_modules:
    id | module                                                            
    ---+-------------------------------------------------------------------
    s0 | fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33
    s1 | hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5           
    s2 | itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33       
single_counts:
    metric             | s0         | s1        | s2        
    -------------------+------------+-----------+-----------
    cpu-cycles:u       | 1000376441 | 381361158 | 3963262809
    instructions:u     | 13990948   | 11920957  | 106540723 
    br_retired:u       | 871390     | 1381391   | 7751332   
    br_mis_pred:u      | 60535      | 509       | 1275359   
    l1i_cache:u        | 2664982    | 1605933   | 27119974  
    l1i_cache_refill:u | 1492       | 1105      | 15028331  
    l1i_tlb:u          | 2664982    | 1605933   | 27119974  
    l1i_tlb_refill:u   | 41         | 40        | 5248089   
    l2i_cache:u        | 1492       | 1103      | 15028331  
    l2i_cache_refill:u | 1462       | 644       | 14399425  
    l2i_tlb:u          | 97         | 91        | 5260193   
    l2i_tlb_refill:u   | 39         | 35        | 3816396   
    l1d_cache:u        | 3059847    | 1419384   | 16956569  
    l1d_cache_refill:u | 2555715    | 1279581   | 10334121  
    l1d_tlb:u          | 8292080    | 4111592   | 38224787  
    l1d_tlb_refill:u   | 2585631    | 1306848   | 10300109  
    l2d_cache:u        | 14637572   | 6501389   | 75193907  
    l2d_cache_refill:u | 9244834    | 2595482   | 39235366  
    l2d_tlb:u          | 2587734    | 1308005   | 10301393  
    l2d_tlb_refill:u   | 2565016    | 1282579   | 10273502  
    ll_cache:u         | 6439800    | 2568459   | 23711206  
    ll_cache_miss:u    | 6001207    | 2336895   | 21588896  
combined_orders:
    id        | modules                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33+hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5+itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33
    shuffle   | itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33+hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5+fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33
    sum       | fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33+hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5+itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 5479250080 | 5491934760 | 5345000408
    instructions:u     | 132431314  | 132431320  | 132452628 
    br_retired:u       | 10001731   | 10001729   | 10004113  
    br_mis_pred:u      | 1334691    | 1335332    | 1336403   
    l1i_cache:u        | 31948652   | 32006629   | 31390889  
    l1i_cache_refill:u | 15034008   | 15025150   | 15030928  
    l1i_tlb:u          | 31948652   | 32006629   | 31390889  
    l1i_tlb_refill:u   | 5268080    | 5268064    | 5248170   
    l2i_cache:u        | 15033998   | 15025148   | 15030926  
    l2i_cache_refill:u | 14509141   | 14552000   | 14401531  
    l2i_tlb:u          | 5280309    | 5280672    | 5260381   
    l2i_tlb_refill:u   | 3841777    | 3836791    | 3816470   
    l1d_cache:u        | 21320554   | 21323602   | 21435800  
    l1d_cache_refill:u | 14164459   | 14148032   | 14169417  
    l1d_tlb:u          | 50157327   | 50158798   | 50628459  
    l1d_tlb_refill:u   | 14217724   | 14217945   | 14192588  
    l2d_cache:u        | 97234978   | 96668070   | 96332868  
    l2d_cache_refill:u | 52632962   | 52271801   | 51075682  
    l2d_tlb:u          | 14220558   | 14221441   | 14197132  
    l2d_tlb_refill:u   | 14123437   | 14124087   | 14121097  
    ll_cache:u         | 33644044   | 33188475   | 32719465  
    ll_cache_miss:u    | 30001422   | 29968754   | 29926998  

### Combined Memory Layouts
#### canonical: `fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33+hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5+itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1275068416 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1275142144 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f512_l1_d4_dtlb_128m_ps_n262144_p32768_np8_l2_r100_sp33_hot_s4096_bp2_dtlb_64m_ps_n16384_p16384_np1_l2_r100_sp5_fetch_b64_d8_bp0_s16_dtlb_1g_ps_n524288_p262144_np2_l4_r100_sp33: `itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33+hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5+fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1275068416 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1275142144 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d8_bp0_s16_r100_dtlb_1g_pstr_n524288_p262144_np2_l4_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_dtlb_64m_pstr_n16384_p16384_np1_l2_sp5`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l1_r100_dtlb_128m_pstr_n262144_p32768_np8_l2_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_063_s3

### Selected Cases
- `fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=2`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=32768`, `data_pool_nodes=131072`, `data_stride_pages=4`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17`: `branch_pairs_per_unit=2`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=262144`, `data_pool_nodes=2097152`, `data_stride_pages=17`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9`: `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=4096`, `data_pool_nodes=8192`, `data_stride_pages=9`, `data_template=dtlb`, `direct_run_len=0`, `funcs=2048`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4+hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17+itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9`

### Results
single_modules:
    id | module                                                             
    ---+--------------------------------------------------------------------
    s0 | fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4
    s1 | hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17         
    s2 | itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9            
single_counts:
    metric             | s0         | s1        | s2         
    -------------------+------------+-----------+------------
    cpu-cycles:u       | 1563931147 | 998742365 | 11707337466
    instructions:u     | 27670942   | 13200951  | 696730723  
    br_retired:u       | 4231392    | 1381393   | 20571332   
    br_mis_pred:u      | 140631     | 456       | 1922       
    l1i_cache:u        | 5318888    | 1800367   | 87240905   
    l1i_cache_refill:u | 3735       | 1903      | 81757482   
    l1i_tlb:u          | 5318888    | 1800367   | 87240905   
    l1i_tlb_refill:u   | 61         | 41        | 20550226   
    l2i_cache:u        | 3736       | 1901      | 81757429   
    l2i_cache_refill:u | 1973       | 1846      | 81727248   
    l2i_tlb:u          | 103        | 116       | 20551467   
    l2i_tlb_refill:u   | 48         | 36        | 20548252   
    l1d_cache:u        | 6021367    | 2701703   | 41106390   
    l1d_cache_refill:u | 5119325    | 2559670   | 40934600   
    l1d_tlb:u          | 16459733   | 7955794   | 123208462  
    l1d_tlb_refill:u   | 5160635    | 2587120   | 41000585   
    l2d_cache:u        | 28515860   | 12886255  | 312928732  
    l2d_cache_refill:u | 12527736   | 7926137   | 166323523  
    l2d_tlb:u          | 5161809    | 2589329   | 41006151   
    l2d_tlb_refill:u   | 5131992    | 2562127   | 40982544   
    ll_cache:u         | 12320631   | 5053952   | 82279949   
    ll_cache_miss:u    | 11132692   | 4873105   | 487408     
combined_orders:
    id        | modules                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4+hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17+itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9
    shuffle   | itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9+hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17+fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4
    sum       | fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4+hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17+itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 14563391259 | 14604942171 | 14270010978
    instructions:u     | 737581320   | 737581329   | 737602616  
    br_retired:u       | 26181729    | 26181730    | 26184117   
    br_mis_pred:u      | 147765      | 143582      | 143009     
    l1i_cache:u        | 94765016    | 94664118    | 94360160   
    l1i_cache_refill:u | 81835696    | 81865697    | 81763120   
    l1i_tlb:u          | 94765016    | 94664118    | 94360160   
    l1i_tlb_refill:u   | 20550678    | 20550652    | 20550328   
    l2i_cache:u        | 81835653    | 81865668    | 81763066   
    l2i_cache_refill:u | 81808674    | 81838734    | 81731067   
    l2i_tlb:u          | 20551915    | 20551992    | 20551686   
    l2i_tlb_refill:u   | 20538038    | 20540540    | 20548336   
    l1d_cache:u        | 49827026    | 49825120    | 49829460   
    l1d_cache_refill:u | 48599553    | 48591956    | 48613595   
    l1d_tlb:u          | 147554368   | 147552571   | 147623989  
    l1d_tlb_refill:u   | 48758603    | 48760797    | 48748340   
    l2d_cache:u        | 354590194   | 354789827   | 354330847  
    l2d_cache_refill:u | 188024782   | 188019164   | 186777396  
    l2d_tlb:u          | 48772462    | 48774991    | 48757289   
    l2d_tlb_refill:u   | 48670893    | 48661186    | 48676663   
    ll_cache:u         | 100114366   | 100248346   | 99654532   
    ll_cache_miss:u    | 18080495    | 17826762    | 16493205   

### Combined Memory Layouts
#### canonical: `fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4+hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17+itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1224736768 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1224810496 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f2048_l2_d0_dtlb_16m_ps_n8192_p4096_np2_l1_r100_sp9_hot_s4096_bp2_dtlb_1g_ps_n2097152_p262144_np8_l4_r100_sp17_fetch_b128_d8_bp2_s16_dtlb_128m_ps_n131072_p32768_np4_l4_r100_sp4: `itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9+hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17+fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=1224736768 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1224810496 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b128_d8_bp2_s16_r100_dtlb_128m_pstr_n131072_p32768_np4_l4_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l4_sp17`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l2_r100_dtlb_16m_pstr_n8192_p4096_np2_l1_sp9`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_064_s3

### Selected Cases
- `fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2`: `block_slots=16`, `blocks=64`, `branch_pairs_per_block=1`, `data_level=64m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=16384`, `data_pool_nodes=65536`, `data_stride_pages=2`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7`: `branch_pairs_per_unit=2`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=32768`, `data_pool_nodes=32768`, `data_stride_pages=7`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=8192`
- `itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3`: `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=65536`, `data_pool_nodes=65536`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=4`, `funcs=4096`, `fusion_ldr_per_unit=4`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2+hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7+itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3`

### Results
single_modules:
    id | module                                                          
    ---+-----------------------------------------------------------------
    s0 | fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2
    s1 | hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7       
    s2 | itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3      
single_counts:
    metric             | s0        | s1        | s2          
    -------------------+-----------+-----------+-------------
    cpu-cycles:u       | 773894222 | 782768929 | 137112825390
    instructions:u     | 20150942  | 23440957  | 1751342001  
    br_retired:u       | 2631392   | 2661391   | 61511603    
    br_mis_pred:u      | 596506    | 491       | 10252503    
    l1i_cache:u        | 8904771   | 3066424   | 383369992   
    l1i_cache_refill:u | 1382      | 1779      | 183604025   
    l1i_tlb:u          | 8904771   | 3066424   | 383369992   
    l1i_tlb_refill:u   | 53        | 40        | 42176386    
    l2i_cache:u        | 1381      | 1776      | 183603951   
    l2i_cache_refill:u | 954       | 1569      | 181695460   
    l2i_tlb:u          | 119       | 78        | 42205702    
    l2i_tlb_refill:u   | 37        | 35        | 41363507    
    l1d_cache:u        | 6042125   | 2702256   | 378984688   
    l1d_cache_refill:u | 2561691   | 2558004   | 337704631   
    l1d_tlb:u          | 13241289  | 7955482   | 1035601795  
    l1d_tlb_refill:u   | 2603367   | 2586430   | 327936451   
    l2d_cache:u        | 14602119  | 13012555  | 1931636219  
    l2d_cache_refill:u | 6354921   | 5233968   | 967557969   
    l2d_tlb:u          | 2611808   | 2588295   | 327950701   
    l2d_tlb_refill:u   | 2568417   | 2565098   | 327902421   
    ll_cache:u         | 6305659   | 5145959   | 687218560   
    ll_cache_miss:u    | 5251226   | 4886171   | 638092461   
combined_orders:
    id        | modules                                                                                                                                                                              
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2+hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7+itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3
    shuffle   | fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2+itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3+hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7
    sum       | fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2+hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7+itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 140717565849 | 140189169101 | 138669488541
    instructions:u     | 1794912608   | 1794912662   | 1794933900  
    br_retired:u       | 66802003     | 66802011     | 66804386    
    br_mis_pred:u      | 10864528     | 10860613     | 10849500    
    l1i_cache:u        | 413763071    | 413890954    | 395341187   
    l1i_cache_refill:u | 183908646    | 183976559    | 183607186   
    l1i_tlb:u          | 413763071    | 413890954    | 395341187   
    l1i_tlb_refill:u   | 42185756     | 42187286     | 42176479    
    l2i_cache:u        | 183908605    | 183976499    | 183607108   
    l2i_cache_refill:u | 181927447    | 183342352    | 181697983   
    l2i_tlb:u          | 42199573     | 42200951     | 42205899    
    l2i_tlb_refill:u   | 41382289     | 41373628     | 41363579    
    l1d_cache:u        | 387709720    | 387658869    | 387729069   
    l1d_cache_refill:u | 342693540    | 342558441    | 342824326   
    l1d_tlb:u          | 1056860383   | 1056764326   | 1056798566  
    l1d_tlb_refill:u   | 333142553    | 333154643    | 333126248   
    l2d_cache:u        | 1959130258   | 1959777230   | 1959250893  
    l2d_cache_refill:u | 976788327    | 985536730    | 979146858   
    l2d_tlb:u          | 333162117    | 333179965    | 333150804   
    l2d_tlb_refill:u   | 333033429    | 333045166    | 333035936   
    ll_cache:u         | 697220486    | 698679274    | 698670178   
    ll_cache_miss:u    | 649272619    | 651098431    | 648229858   

### Combined Memory Layouts
#### canonical: `fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2+hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7+itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=469762048 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=469835776 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b64_d1_bp1_s16_dtlb_64m_ps_n65536_p16384_np4_l4_r100_sp2_itlb_f4096_l2_d4_dtlb_256m_ps_n65536_p65536_np1_l4_r100_sp3_hot_s8192_bp2_dtlb_128m_ps_n32768_p32768_np1_l2_r100_sp7: `fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2+itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3+hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=469762048 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=469835776 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `fetch_b64_d1_bp1_s16_r100_dtlb_64m_pstr_n65536_p16384_np4_l4_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=67108864 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=67174400 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp2_r100_dtlb_128m_pstr_n32768_p32768_np1_l2_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f4096_l2_r100_dtlb_256m_pstr_n65536_p65536_np1_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_065_s3

### Selected Cases
- `cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129`: `blocks=18000`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=1`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=2`, `data_level=1m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=256`, `data_pool_nodes=131072`, `data_stride_lines=1024`, `data_stride_nodes=1024`, `data_template=cold`, `direct_run_len=2`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33`: `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=4`, `data_pages=4096`, `data_pool_nodes=16384`, `data_stride_pages=33`, `data_template=dtlb`, `direct_run_len=0`, `funcs=2048`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129+fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024+itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33`

### Results
single_modules:
    id | module                                                              
    ---+---------------------------------------------------------------------
    s0 | cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129  
    s1 | fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024
    s2 | itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33           
single_counts:
    metric             | s0          | s1       | s2         
    -------------------+-------------+----------+------------
    cpu-cycles:u       | 94184209407 | 42056223 | 11894943333
    instructions:u     | 3307812051  | 29110988 | 696730729  
    br_retired:u       | 225071610   | 5191403  | 20571330   
    br_mis_pred:u      | 22511038    | 619626   | 1838       
    l1i_cache:u        | 992212440   | 12284049 | 87286263   
    l1i_cache_refill:u | 369423522   | 854      | 81794247   
    l1i_tlb:u          | 992212440   | 12284049 | 87286263   
    l1i_tlb_refill:u   | 8460473     | 49       | 20550050   
    l2i_cache:u        | 369423332   | 852      | 81794205   
    l2i_cache_refill:u | 368692386   | 843      | 81768903   
    l2i_tlb:u          | 8483344     | 96       | 20550697   
    l2i_tlb_refill:u   | 6144763     | 20       | 20548708   
    l1d_cache:u        | 292612106   | 4636362  | 41097210   
    l1d_cache_refill:u | 199838490   | 474855   | 40939822   
    l1d_tlb:u          | 655953806   | 6094824  | 123265153  
    l1d_tlb_refill:u   | 180653705   | 1300202  | 41011150   
    l2d_cache:u        | 1474991831  | 1267995  | 312959252  
    l2d_cache_refill:u | 983215263   | 191698   | 166040888  
    l2d_tlb:u          | 180664329   | 1302888  | 41012312   
    l2d_tlb_refill:u   | 180582855   | 21       | 40988916   
    ll_cache:u         | 436101135   | 190794   | 82283661   
    ll_cache_miss:u    | 358011284   | 1499     | 308229     
combined_orders:
    id        | modules                                                                                                                                                                                          
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129+fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024+itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33
    shuffle   | itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33+fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024+cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129
    sum       | cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129+fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024+itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 106155978005 | 106109249054 | 106121208963
    instructions:u     | 4033632553   | 4033632593   | 4033653768  
    br_retired:u       | 250831997    | 250832001    | 250834343   
    br_mis_pred:u      | 23138489     | 23145272     | 23132502    
    l1i_cache:u        | 1052884994   | 1004054111   | 1091782752  
    l1i_cache_refill:u | 451125183    | 451280909    | 451218623   
    l1i_tlb:u          | 1052884994   | 1004054111   | 1091782752  
    l1i_tlb_refill:u   | 29016663     | 29019116     | 29010572    
    l2i_cache:u        | 451124886    | 451280607    | 451218389   
    l2i_cache_refill:u | 450392895    | 450439112    | 450462132   
    l2i_tlb:u          | 29037113     | 29048078     | 29034137    
    l2i_tlb_refill:u   | 26727448     | 26754163     | 26693491    
    l1d_cache:u        | 338387392    | 338307791    | 338345678   
    l1d_cache_refill:u | 243671794    | 255406967    | 241253167   
    l1d_tlb:u          | 785814809    | 785616203    | 785313783   
    l1d_tlb_refill:u   | 223010592    | 223013014    | 222965057   
    l2d_cache:u        | 1784441322   | 1757243411   | 1789219078  
    l2d_cache_refill:u | 1150805246   | 1155646695   | 1149447849  
    l2d_tlb:u          | 223034989    | 223032760    | 222979529   
    l2d_tlb_refill:u   | 221580531    | 221642587    | 221571792   
    ll_cache:u         | 519400686    | 519728101    | 518575590   
    ll_cache_miss:u    | 364268042    | 370090760    | 358321012   

### Combined Memory Layouts
#### canonical: `cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129+fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024+itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=554696704 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=554770432 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_itlb_f2048_l2_d0_dtlb_16m_ps_n16384_p4096_np4_l1_r100_sp33_fetch_b128_d2_bp2_s16_cold_1m_ns_n131072_p256_np512_l1_r100_sn1024_main_b18000_d8_bitrev_dtlb_512m_ps_n1048576_p131072_np8_l1_r100_sp129: `itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33+fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024+cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=554696704 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=554770432 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b18000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l1_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d2_bp2_s16_r100_cold_1m_nstr_n131072_p256_np512_l1_sn1024`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1048576 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1114112 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f2048_l2_r100_dtlb_16m_pstr_n16384_p4096_np4_l1_sp33`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_066_s3

### Selected Cases
- `cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128`: `blocks=19000`, `data_level=512k`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=128`, `data_pool_nodes=65536`, `data_stride_lines=128`, `data_stride_nodes=128`, `data_template=cold`, `direct_run_len=4`, `fusion_ldr_per_unit=1`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=1`, `data_level=16m`, `data_mode=page_stride`, `data_nodes_per_page=2`, `data_pages=4096`, `data_pool_nodes=8192`, `data_stride_pages=7`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4`: `branch_pairs_per_unit=2`, `data_level=4m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1024`, `data_pool_nodes=524288`, `data_stride_lines=4`, `data_stride_nodes=4`, `data_template=cold`, `fusion_ldr_per_unit=1`, `region_reps=100`, `size=4096`

### Combination Rule
- combo size: `3`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128+fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4`

### Results
single_modules:
    id | module                                                         
    ---+----------------------------------------------------------------
    s0 | cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128
    s1 | fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7
    s2 | hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4       
single_counts:
    metric             | s0          | s1        | s2      
    -------------------+-------------+-----------+---------
    cpu-cycles:u       | 25035577697 | 807132257 | 11055075
    instructions:u     | 3752810940  | 27670942  | 11281049
    br_retired:u       | 285071388   | 2951392   | 1381410 
    br_mis_pred:u      | 47556802    | 140614    | 411     
    l1i_cache:u        | 1244794389  | 5311681   | 1496794 
    l1i_cache_refill:u | 390103023   | 2268      | 596     
    l1i_tlb:u          | 1244794389  | 5311681   | 1496794 
    l1i_tlb_refill:u   | 9000294     | 46        | 50      
    l2i_cache:u        | 390102866   | 2268      | 595     
    l2i_cache_refill:u | 389526457   | 1134      | 584     
    l2i_tlb:u          | 9003372     | 94        | 129     
    l2i_tlb_refill:u   | 316210      | 42        | 48      
    l1d_cache:u        | 434299230   | 6018684   | 775314  
    l1d_cache_refill:u | 89625618    | 5098137   | 71534   
    l1d_tlb:u          | 511197669   | 16369615  | 801469  
    l1d_tlb_refill:u   | 48876225    | 5160144   | 6724    
    l2d_cache:u        | 926220298   | 28188710  | 1184023 
    l2d_cache_refill:u | 564954634   | 11797270  | 403462  
    l2d_tlb:u          | 48877452    | 5161822   | 6868    
    l2d_tlb_refill:u   | 45026       | 5065028   | 1185    
    ll_cache:u         | 175350292   | 11653102  | 402352  
    ll_cache_miss:u    | 1883062     | 841782    | 1879    
combined_orders:
    id        | modules                                                                                                                                                                                 
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128+fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4
    shuffle   | fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128+hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4
    sum       | cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128+fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 24749344667 | 26180146907 | 25853765029
    instructions:u     | 3791741540  | 3791742450  | 3791762931 
    br_retired:u       | 289401788   | 289401983   | 289404190  
    br_mis_pred:u      | 47643642    | 47803285    | 47697827   
    l1i_cache:u        | 1131011531  | 1199018374  | 1251602864 
    l1i_cache_refill:u | 390449768   | 390513573   | 390105887  
    l1i_tlb:u          | 1131011531  | 1199018374  | 1251602864 
    l1i_tlb_refill:u   | 8938332     | 8939008     | 9000390    
    l2i_cache:u        | 390449644   | 390513442   | 390105729  
    l2i_cache_refill:u | 389747365   | 389684664   | 389528175  
    l2i_tlb:u          | 8944840     | 8941406     | 9003595    
    l2i_tlb_refill:u   | 387525      | 202347      | 316300     
    l1d_cache:u        | 438637776   | 439292716   | 441093228  
    l1d_cache_refill:u | 96501828    | 94749271    | 94795289   
    l1d_tlb:u          | 533722311   | 533749865   | 528368753  
    l1d_tlb_refill:u   | 54040974    | 54041474    | 54043093   
    l2d_cache:u        | 1007790649  | 1014009726  | 955593031  
    l2d_cache_refill:u | 577685475   | 578989179   | 577155366  
    l2d_tlb:u          | 54045696    | 54044717    | 54046142   
    l2d_tlb_refill:u   | 5426578     | 5222509     | 5111239    
    ll_cache:u         | 189302636   | 192554757   | 187405746  
    ll_cache_miss:u    | 4062435     | 2767743     | 2726723    

### Combined Memory Layouts
#### canonical: `cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128+fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=21495808 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=21569536 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d8_bp1_s16_dtlb_16m_ps_n8192_p4096_np2_l4_r100_sp7_main_b19000_d4_bitrev_cold_512k_ns_n65536_p128_np512_l1_r100_sn128_hot_s4096_bp2_cold_4m_ns_n524288_p1024_np512_l1_r100_sn4: `fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7+cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128+hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4`

```text
===== memory layout =====
iters=100 active_data_regions=3 total_data_bytes=21495808 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=21569536 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b19000_d4_bitrev_cold_512k_nstr_n65536_p128_np512_l1_sn128`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=524288 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=589824 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d8_bp1_s16_r100_dtlb_16m_pstr_n8192_p4096_np2_l4_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=16777216 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=16842752 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp2_r100_cold_4m_nstr_n524288_p1024_np512_l1_sn4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4194304 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4259840 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_067_s4

### Selected Cases
- `cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2`: `blocks=10000`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=2`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=4`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=2`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=4`, `fusion_ldr_per_unit=1`, `layout=linear`, `region_reps=100`
- `hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4`: `branch_pairs_per_unit=2`, `data_level=256m`, `data_mode=random`, `data_nodes_per_page=8`, `data_pages=65536`, `data_pool_nodes=524288`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=8192`
- `itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7`: `data_level=256m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=65536`, `data_pool_nodes=65536`, `data_stride_pages=7`, `data_template=dtlb`, `direct_run_len=4`, `funcs=512`, `fusion_ldr_per_unit=2`, `lines_per_page=1`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `4`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2+fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3+hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4+itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7`

### Results
single_modules:
    id | module                                                          
    ---+-----------------------------------------------------------------
    s0 | cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2   
    s1 | fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3
    s2 | hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4          
    s3 | itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7       
single_counts:
    metric             | s0           | s1        | s2         | s3        
    -------------------+--------------+-----------+------------+-----------
    cpu-cycles:u       | 143924301571 | 279546397 | 1692540448 | 4260074482
    instructions:u     | 2275311993   | 25591089  | 26000942   | 106540729 
    br_retired:u       | 150071601    | 4551412   | 2661392    | 7751330   
    br_mis_pred:u      | 25007650     | 290740    | 451        | 1274162   
    l1i_cache:u        | 696307267    | 7030631   | 3409133    | 27350502  
    l1i_cache_refill:u | 221552920    | 1305      | 3874       | 15043164  
    l1i_tlb:u          | 696307267    | 7030631   | 3409133    | 27350502  
    l1i_tlb_refill:u   | 4846103      | 42        | 51         | 5248105   
    l2i_cache:u        | 221552882    | 1302      | 3885       | 15043157  
    l2i_cache_refill:u | 221019713    | 1063      | 2850       | 14543165  
    l2i_tlb:u          | 4862420      | 90        | 139        | 5259796   
    l2i_tlb_refill:u   | 3655986      | 40        | 41         | 3877705   
    l1d_cache:u        | 527128988    | 2980245   | 5261076    | 16819071  
    l1d_cache_refill:u | 414071644    | 1278620   | 5118697    | 10340294  
    l1d_tlb:u          | 1339487812   | 5661995   | 15599450   | 37639505  
    l1d_tlb_refill:u   | 400483630    | 1305122   | 5154445    | 10300061  
    l2d_cache:u        | 2397904508   | 7319335   | 26261798   | 75658830  
    l2d_cache_refill:u | 1227497055   | 3140989   | 12318608   | 43443679  
    l2d_tlb:u          | 400496544    | 1305203   | 5157581    | 10300399  
    l2d_tlb_refill:u   | 400431250    | 1282779   | 5061968    | 10275001  
    ll_cache:u         | 857685227    | 3120223   | 10327257   | 24546468  
    ll_cache_miss:u    | 779750483    | 878974    | 9853275    | 22456552  
combined_orders:
    id        | modules                                                                                                                                                                                                                                        
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2+fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3+hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4+itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7
    shuffle   | fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3+cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2+itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7+hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4
    sum       | cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2+fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3+hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4+itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 149893936200 | 149143433857 | 150156462898
    instructions:u     | 2433412901   | 2433412880   | 2433444753  
    br_retired:u       | 165032203    | 165032201    | 165035735   
    br_mis_pred:u      | 26608520     | 26588542     | 26573003    
    l1i_cache:u        | 686390770    | 670944600    | 734097533   
    l1i_cache_refill:u | 236762717    | 236414822    | 236601263   
    l1i_tlb:u          | 686390770    | 670944600    | 734097533   
    l1i_tlb_refill:u   | 10136074     | 10135326     | 10094301    
    l2i_cache:u        | 236762686    | 236414755    | 236601226   
    l2i_cache_refill:u | 235724199    | 235347295    | 235566791   
    l2i_tlb:u          | 10158194     | 10163835     | 10122445    
    l2i_tlb_refill:u   | 7487606      | 7477087      | 7533772     
    l1d_cache:u        | 552477758    | 553931420    | 552189380   
    l1d_cache_refill:u | 437334918    | 438283436    | 430809255   
    l1d_tlb:u          | 1398318371   | 1397194877   | 1398388762  
    l1d_tlb_refill:u   | 417316703    | 417309270    | 417243258   
    l2d_cache:u        | 2487258345   | 2464545095   | 2507144471  
    l2d_cache_refill:u | 1285437047   | 1290249072   | 1286400331  
    l2d_tlb:u          | 417353839    | 417327796    | 417259727   
    l2d_tlb_refill:u   | 417085299    | 417083928    | 417050998   
    ll_cache:u         | 892434048    | 896428632    | 895679175   
    ll_cache_miss:u    | 813392622    | 815641910    | 812939284   

### Combined Memory Layouts
#### canonical: `cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2+fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3+hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4+itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=4 total_data_bytes=1644167168 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1644244992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d4_bp2_s16_dtlb_32m_ps_n65536_p8192_np8_l1_r100_sp3_main_b10000_d4_bitrev_dtlb_1g_ps_n262144_p262144_np1_l4_r100_sp2_itlb_f512_l1_d4_dtlb_256m_ps_n65536_p65536_np1_l2_r100_sp7_hot_s8192_bp2_dtlb_256m_rnd_n524288_p65536_np8_l4_r100: `fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3+cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2+itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7+hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4`

```text
===== memory layout =====
iters=100 active_data_regions=4 total_data_bytes=1644167168 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1644244992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b10000_d4_bitrev_dtlb_1g_pstr_n262144_p262144_np1_l4_sp2`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d4_bp2_s16_r100_dtlb_32m_pstr_n65536_p8192_np8_l1_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp2_r100_dtlb_256m_rand_n524288_p65536_np8_l4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l1_r100_dtlb_256m_pstr_n65536_p65536_np1_l2_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=268435456 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=268500992 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_068_s4

### Selected Cases
- `cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7`: `blocks=20000`, `data_level=128m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=32768`, `data_pool_nodes=32768`, `data_stride_pages=7`, `data_template=dtlb`, `direct_run_len=1`, `fusion_ldr_per_unit=1`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=0`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=129`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=4`, `layout=linear`, `region_reps=100`
- `hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65`: `branch_pairs_per_unit=4`, `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=262144`, `data_pool_nodes=262144`, `data_stride_pages=65`, `data_template=dtlb`, `fusion_ldr_per_unit=4`, `region_reps=100`, `size=4096`
- `itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257`: `data_level=1g`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=262144`, `data_pool_nodes=2097152`, `data_stride_pages=257`, `data_template=dtlb`, `direct_run_len=0`, `funcs=512`, `fusion_ldr_per_unit=1`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `4`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7+fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129+hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65+itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257`

### Results
single_modules:
    id | module                                                           
    ---+------------------------------------------------------------------
    s0 | cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7    
    s1 | fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129
    s2 | hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65        
    s3 | itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257     
single_counts:
    metric             | s0          | s1         | s2        | s3        
    -------------------+-------------+------------+-----------+-----------
    cpu-cycles:u       | 89955750336 | 1037970135 | 801317673 | 4634052473
    instructions:u     | 5600312004  | 27670948   | 13200951  | 174490736 
    br_retired:u       | 600071604   | 1671390    | 2661393   | 5211332   
    br_mis_pred:u      | 200199480   | 140801     | 408       | 596       
    l1i_cache:u        | 3105509336  | 5255122    | 1774766   | 22026730  
    l1i_cache_refill:u | 414963427   | 3058       | 1674      | 19998225  
    l1i_tlb:u          | 3105509336  | 5255122    | 1774766   | 22026730  
    l1i_tlb_refill:u   | 9275923     | 56         | 39        | 5160043   
    l2i_cache:u        | 414963065   | 3057       | 1674      | 19998224  
    l2i_cache_refill:u | 414369812   | 1087       | 1581      | 19997671  
    l2i_tlb:u          | 9345432     | 108        | 89        | 5160170   
    l2i_tlb_refill:u   | 6900235     | 47         | 35        | 779732    
    l1d_cache:u        | 1290899360  | 6019219    | 2703477   | 10385000  
    l1d_cache_refill:u | 251512166   | 5103350    | 2559181   | 10233473  
    l1d_tlb:u          | 2430354627  | 16376898   | 7950219   | 31017793  
    l1d_tlb_refill:u   | 203340367   | 5146147    | 2589146   | 10279791  
    l2d_cache:u        | 2056328236  | 28040287   | 13360519  | 78417466  
    l2d_cache_refill:u | 1092407660  | 12021458   | 5892503   | 46725737  
    l2d_tlb:u          | 205081181   | 5148173    | 2590252   | 10282639  
    l2d_tlb_refill:u   | 202372588   | 5128913    | 2564821   | 10243852  
    ll_cache:u         | 631685075   | 11970067   | 5140143   | 20555710  
    ll_cache_miss:u    | 393367019   | 3472849    | 4866808   | 20214957  
combined_orders:
    id        | modules                                                                                                                                                                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7+fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129+hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65+itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257
    shuffle   | cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7+hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65+itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257+fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129
    sum       | cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7+fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129+hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65+itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257
combined_counts:
    metric             | canonical    | shuffle      | sum        
    -------------------+--------------+--------------+------------
    cpu-cycles:u       | 100007256685 | 100783834509 | 96429090617
    instructions:u     | 5815642917   | 5815642928   | 5815674639 
    br_retired:u       | 609612204    | 609612207    | 609615719  
    br_mis_pred:u      | 200310868    | 200453036    | 200341285  
    l1i_cache:u        | 2884001601   | 2943600717   | 3134565954 
    l1i_cache_refill:u | 435060619    | 435046579    | 434966384  
    l1i_tlb:u          | 2884001601   | 2943600717   | 3134565954 
    l1i_tlb_refill:u   | 14448617     | 14448542     | 14436061   
    l2i_cache:u        | 435060292    | 435046262    | 434966020  
    l2i_cache_refill:u | 434440755    | 434385825    | 434370151  
    l2i_tlb:u          | 14467202     | 14460313     | 14505799   
    l2i_tlb_refill:u   | 7741143      | 7877766      | 7680049    
    l1d_cache:u        | 1276530485   | 1270437791   | 1310007056 
    l1d_cache_refill:u | 317301182    | 325875265    | 269408170  
    l1d_tlb:u          | 2379071169   | 2357719546   | 2485699537 
    l1d_tlb_refill:u   | 221404188    | 221388070    | 221355451  
    l2d_cache:u        | 2150550859   | 2144586100   | 2176146508 
    l2d_cache_refill:u | 1162582393   | 1167731298   | 1157047358 
    l2d_tlb:u          | 222983650    | 222757432    | 223102245  
    l2d_tlb_refill:u   | 220462584    | 220318840    | 220310174  
    ll_cache:u         | 668730244    | 669787869    | 669350995  
    ll_cache_miss:u    | 428939128    | 429765181    | 421921633  

### Combined Memory Layouts
#### canonical: `cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7+fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129+hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65+itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=4 total_data_bytes=2315255808 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2315333632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_main_b20000_d1_bitrev_dtlb_128m_ps_n32768_p32768_np1_l1_r100_sp7_hot_s4096_bp4_dtlb_1g_ps_n262144_p262144_np1_l4_r100_sp65_itlb_f512_l2_d0_dtlb_1g_ps_n2097152_p262144_np8_l1_r100_sp257_fetch_b128_d8_bp0_s16_dtlb_32m_ps_n8192_p8192_np1_l4_r100_sp129: `cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7+hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65+itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257+fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=4 total_data_bytes=2315255808 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=2315333632 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b20000_d1_bitrev_dtlb_128m_pstr_n32768_p32768_np1_l1_sp7`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=134217728 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=134283264 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d8_bp0_s16_r100_dtlb_32m_pstr_n8192_p8192_np1_l4_sp129`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b64_bp4_r100_dtlb_1g_pstr_n262144_p262144_np1_l4_sp65`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f512_l2_r100_dtlb_1g_pstr_n2097152_p262144_np8_l1_sp257`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=1073741824 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=1073807360 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

## combo_069_s4

### Selected Cases
- `cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1`: `blocks=19000`, `data_level=512m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=131072`, `data_pool_nodes=1048576`, `data_stride_pages=1`, `data_template=dtlb`, `direct_run_len=8`, `fusion_ldr_per_unit=2`, `layout=in_page_shuffle`, `region_reps=100`
- `fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1`: `block_slots=16`, `blocks=128`, `branch_pairs_per_block=1`, `data_level=4m`, `data_mode=node_stride`, `data_nodes_per_page=512`, `data_pages=1024`, `data_pool_nodes=524288`, `data_stride_lines=1`, `data_stride_nodes=1`, `data_template=cold`, `direct_run_len=2`, `fusion_ldr_per_unit=2`, `layout=linear`, `region_reps=100`
- `hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4`: `branch_pairs_per_unit=3`, `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=1`, `data_pages=8192`, `data_pool_nodes=8192`, `data_stride_pages=4`, `data_template=dtlb`, `fusion_ldr_per_unit=2`, `region_reps=100`, `size=8192`
- `itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`: `data_level=32m`, `data_mode=page_stride`, `data_nodes_per_page=8`, `data_pages=8192`, `data_pool_nodes=65536`, `data_stride_pages=3`, `data_template=dtlb`, `direct_run_len=0`, `funcs=256`, `fusion_ldr_per_unit=4`, `lines_per_page=2`, `mode=chain`, `region_reps=100`

### Combination Rule
- combo size: `4`
- rejected if every selected case is a hot booster template
- canonical order: `cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1+fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1+hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

### Results
single_modules:
    id | module                                                            
    ---+-------------------------------------------------------------------
    s0 | cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1  
    s1 | fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1
    s2 | hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4            
    s3 | itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3           
single_counts:
    metric             | s0           | s1       | s2        | s3        
    -------------------+--------------+----------+-----------+-----------
    cpu-cycles:u       | 127200375611 | 34552724 | 519081546 | 4798825768
    instructions:u     | 3681562001   | 30390988 | 23440951  | 102810723 
    br_retired:u       | 237571603    | 3911403  | 3941393   | 2651332   
    br_mis_pred:u      | 23752602     | 614196   | 473       | 529       
    l1i_cache:u        | 1019786175   | 12337428 | 3064119   | 12947833  
    l1i_cache_refill:u | 401042175    | 813      | 1496      | 9873331   
    l1i_tlb:u          | 1019786175   | 12337428 | 3064119   | 12947833  
    l1i_tlb_refill:u   | 9203934      | 54       | 45        | 2600055   
    l2i_cache:u        | 401042137    | 810      | 1496      | 9873324   
    l2i_cache_refill:u | 400391451    | 790      | 746       | 9539794   
    l2i_tlb:u          | 10464585     | 104      | 163       | 2600252   
    l2i_tlb_refill:u   | 6725775      | 50       | 41        | 2324064   
    l1d_cache:u        | 498853136    | 5897192  | 2702398   | 20615949  
    l1d_cache_refill:u | 414556964    | 69350    | 2559259   | 20469674  
    l1d_tlb:u          | 1262023499   | 5981235  | 7981179   | 61687463  
    l1d_tlb_refill:u   | 380690815    | 5566     | 2597904   | 20504862  
    l2d_cache:u        | 2433259592   | 1115510  | 12992578  | 116512148 
    l2d_cache_refill:u | 1278869387   | 323639   | 5182522   | 51250954  
    l2d_tlb:u          | 380703692    | 5593     | 2599332   | 20505316  
    l2d_tlb_refill:u   | 380612213    | 1637     | 2565861   | 20497849  
    ll_cache:u         | 829683764    | 322266   | 5130673   | 41128408  
    ll_cache_miss:u    | 745366196    | 8187     | 1309371   | 10670103  
combined_orders:
    id        | modules                                                                                                                                                                                                                                           
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1+fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1+hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3
    shuffle   | fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1+cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1+hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3
    sum       | cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1+fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1+hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 142970883036 | 133640678403 | 132552835649
    instructions:u     | 3838172971   | 3838172944   | 3838204663  
    br_retired:u       | 248072212    | 248072208    | 248075731   
    br_mis_pred:u      | 24372791     | 24379093     | 24367800    
    l1i_cache:u        | 1071406209   | 1018901196   | 1048135555  
    l1i_cache_refill:u | 412061470    | 412189073    | 410917815   
    l1i_tlb:u          | 1071406209   | 1018901196   | 1048135555  
    l1i_tlb_refill:u   | 11802936     | 11798977     | 11804088    
    l2i_cache:u        | 412061308    | 412188979    | 410917767   
    l2i_cache_refill:u | 411287542    | 411452209    | 409932781   
    l2i_tlb:u          | 11818999     | 11812125     | 13065104    
    l2i_tlb_refill:u   | 9045796      | 9013925      | 9049930     
    l1d_cache:u        | 528072850    | 528092674    | 528068675   
    l1d_cache_refill:u | 438843318    | 439593674    | 437655247   
    l1d_tlb:u          | 1338357270   | 1338176456   | 1337673376  
    l1d_tlb_refill:u   | 403828978    | 403816869    | 403799147   
    l2d_cache:u        | 2569669904   | 2566476877   | 2563879828  
    l2d_cache_refill:u | 1341503670   | 1340702923   | 1335626502  
    l2d_tlb:u          | 403851705    | 403840253    | 403813933   
    l2d_tlb_refill:u   | 403720821    | 403717314    | 403677560   
    ll_cache:u         | 881038857    | 880192020    | 876265111   
    ll_cache_miss:u    | 777466386    | 775285136    | 757353857   

### Combined Memory Layouts
#### canonical: `cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1+fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1+hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=4 total_data_bytes=608174080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=608251904 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_fetch_b128_d2_bp1_s16_cold_4m_ns_n524288_p1024_np512_l2_r100_sn1_main_b19000_d8_bitrev_dtlb_512m_ps_n1048576_p131072_np8_l2_r100_sp1_hot_s8192_bp3_dtlb_32m_ps_n8192_p8192_np1_l2_r100_sp4_itlb_f256_l2_d0_dtlb_32m_ps_n65536_p8192_np8_l4_r100_sp3: `fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1+cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1+hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4+itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=4 total_data_bytes=608174080 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=608251904 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `cold_b19000_d8_bitrev_dtlb_512m_pstr_n1048576_p131072_np8_l2_sp1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=536870912 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=536936448 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `fetch_b128_d2_bp1_s16_r100_cold_4m_nstr_n524288_p1024_np512_l2_sn1`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=4194304 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=4259840 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `hot_b128_bp3_r100_dtlb_32m_pstr_n8192_p8192_np1_l2_sp4`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `itlb_f256_l2_r100_dtlb_32m_pstr_n65536_p8192_np8_l4_sp3`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=33554432 allocator=arena advice=default arena_gap_bytes=0 arena_bytes=33619968 arena_hint=0x0 prefault=1 warmup_iters=1
```

Captured `2` layout snapshots across perf event groups; showing the first one.

