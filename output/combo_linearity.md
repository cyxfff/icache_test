# combo_linearity

## combo_000_s2

### Selected Cases
- `mix_b128_ld1_indir_p128_lp4_r100`: `data_mode=indirect`, `ldr_count_per_unit=1`, `lines_per_page=4`, `pages=128`, `region_reps=100`, `size=8192`
- `mix_b128_ld14_lin_p512_lp1_r100`: `data_mode=linear`, `ldr_count_per_unit=14`, `lines_per_page=1`, `pages=512`, `region_reps=100`, `size=8192`

### Combination Rule
- combo size: `2`
- rejected if every selected case is a hot booster template
- canonical order: `mix_b128_ld1_indir_p128_lp4_r100+mix_b128_ld14_lin_p512_lp1_r100`

### Results
single_modules:
    id | module                          
    ---+---------------------------------
    s0 | mix_b128_ld1_indir_p128_lp4_r100
    s1 | mix_b128_ld14_lin_p512_lp1_r100 
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 27429867 | 835571369
    instructions:u     | 20860952 | 20860914 
    br_retired:u       | 81392    | 81380    
    br_mis_pred:u      | 416      | 543      
    l1i_cache:u        | 2669192  | 2701187  
    l1i_cache_refill:u | 713      | 1623     
    l1i_tlb:u          | 2669192  | 2701187  
    l1i_tlb_refill:u   | 52       | 46       
    l2i_cache:u        | 714      | 1625     
    l2i_cache_refill:u | 632      | 712      
    l2i_tlb:u          | 115      | 108      
    l2i_tlb_refill:u   | 24       | 29       
    l1d_cache:u        | 1416506  | 18099848 
    l1d_cache_refill:u | 1185303  | 17945840 
    l1d_tlb:u          | 2541997  | 36189182 
    l1d_tlb_refill:u   | 1062828  | 17975881 
    l2d_cache:u        | 3326822  | 70894944 
    l2d_cache_refill:u | 665443   | 35872428 
    l2d_tlb:u          | 1063813  | 17978397 
    l2d_tlb_refill:u   | 14       | 161      
    ll_cache:u         | 664756   | 35869733 
    ll_cache_miss:u    | 7720     | 26038    
combined_orders:
    id        | modules                                                         
    ----------+-----------------------------------------------------------------
    canonical | mix_b128_ld1_indir_p128_lp4_r100+mix_b128_ld14_lin_p512_lp1_r100
    shuffle   | mix_b128_ld14_lin_p512_lp1_r100+mix_b128_ld1_indir_p128_lp4_r100
    sum       | mix_b128_ld1_indir_p128_lp4_r100+mix_b128_ld14_lin_p512_lp1_r100
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 913150246 | 938009813 | 863001236
    instructions:u     | 41711214  | 41711214  | 41721866 
    br_retired:u       | 161580    | 161580    | 162772   
    br_mis_pred:u      | 743       | 737       | 959      
    l1i_cache:u        | 5381914   | 5394732   | 5370379  
    l1i_cache_refill:u | 2760      | 2636      | 2336     
    l1i_tlb:u          | 5381914   | 5394732   | 5370379  
    l1i_tlb_refill:u   | 47        | 44        | 98       
    l2i_cache:u        | 2764      | 2641      | 2339     
    l2i_cache_refill:u | 934       | 892       | 1344     
    l2i_tlb:u          | 101       | 93        | 223      
    l2i_tlb_refill:u   | 28        | 29        | 53       
    l1d_cache:u        | 19515841  | 19518879  | 19516354 
    l1d_cache_refill:u | 19128416  | 19132523  | 19131143 
    l1d_tlb:u          | 38737748  | 38745253  | 38731179 
    l1d_tlb_refill:u   | 19041442  | 19044654  | 19038709 
    l2d_cache:u        | 74528195  | 74364698  | 74221766 
    l2d_cache_refill:u | 36795590  | 36699401  | 36537871 
    l2d_tlb:u          | 19044779  | 19047310  | 19042210 
    l2d_tlb_refill:u   | 287       | 296       | 175      
    ll_cache:u         | 36792704  | 36696693  | 36534489 
    ll_cache_miss:u    | 96542     | 111396    | 33758    

### Combined Memory Layouts
#### canonical: `mix_b128_ld1_indir_p128_lp4_r100+mix_b128_ld14_lin_p512_lp1_r100`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=2621440
data_region kind=mixed-data name=mixed_region_loop_6 start=0xffff8fe8a000 end=0xffff9008a000 bytes=2097152 pages=512 nodes=512 reps=100
data_region kind=mixed-data name=mixed_region_loop_4 start=0xffff9008c000 end=0xffff9010c000 bytes=524288 pages=128 nodes=512 reps=100
code_region kind=mixed-code name=mixed_region_loop_4 symbol=mixed_region_4_kernel entry=0x4011c0 end=0x403210 bytes=8272 cache_lines=130 ldr_per_unit=1 reps=100 source=nm+objdump
code_region kind=mixed-code name=mixed_region_loop_6 symbol=mixed_region_6_kernel entry=0x403240 end=0x405290 bytes=8272 cache_lines=130 ldr_per_unit=14 reps=100 source=nm+objdump
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### shuffle_mixslot6_mix_s8192_l14_mlin_p512_lp1_r100_mixslot4_mix_s8192_l1_mindir_p128_lp4_r100: `mix_b128_ld14_lin_p512_lp1_r100+mix_b128_ld1_indir_p128_lp4_r100`

```text
===== memory layout =====
iters=100 active_data_regions=2 total_data_bytes=2621440
data_region kind=mixed-data name=mixed_region_loop_6 start=0xffffa6764000 end=0xffffa6964000 bytes=2097152 pages=512 nodes=512 reps=100
data_region kind=mixed-data name=mixed_region_loop_4 start=0xffffa6966000 end=0xffffa69e6000 bytes=524288 pages=128 nodes=512 reps=100
code_region kind=mixed-code name=mixed_region_loop_4 symbol=mixed_region_4_kernel entry=0x4011c0 end=0x403210 bytes=8272 cache_lines=130 ldr_per_unit=1 reps=100 source=nm+objdump
code_region kind=mixed-code name=mixed_region_loop_6 symbol=mixed_region_6_kernel entry=0x403240 end=0x405290 bytes=8272 cache_lines=130 ldr_per_unit=14 reps=100 source=nm+objdump
```

Captured `2` layout snapshots across perf event groups; showing the first one.

### Single-Case Memory Layouts
#### `mix_b128_ld1_indir_p128_lp4_r100`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=524288
data_region kind=mixed-data name=mixed_region_loop_4 start=0xffffa8a95000 end=0xffffa8b15000 bytes=524288 pages=128 nodes=512 reps=100
code_region kind=mixed-code name=mixed_region_loop_4 symbol=mixed_region_4_kernel entry=0x4011c0 end=0x403210 bytes=8272 cache_lines=130 ldr_per_unit=1 reps=100 source=nm+objdump
```

Captured `2` layout snapshots across perf event groups; showing the first one.

#### `mix_b128_ld14_lin_p512_lp1_r100`

```text
===== memory layout =====
iters=100 active_data_regions=1 total_data_bytes=2097152
data_region kind=mixed-data name=mixed_region_loop_6 start=0xffff9e860000 end=0xffff9ea60000 bytes=2097152 pages=512 nodes=512 reps=100
code_region kind=mixed-code name=mixed_region_loop_6 symbol=mixed_region_6_kernel entry=0x4011c0 end=0x403210 bytes=8272 cache_lines=130 ldr_per_unit=14 reps=100 source=nm+objdump
```

Captured `2` layout snapshots across perf event groups; showing the first one.

