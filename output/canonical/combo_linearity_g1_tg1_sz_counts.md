== combo_linearity ==
source=/home/tchen/icache_test/output/combo_linearity_g1_tg1_sz.csv
mode=csv_render_only
errors=not_computed
layout_snapshots=not_available_from_csv
cases=1
rows=5
metrics=22
metric_set=raw

== combo_000_s2 ==
single_modules:
    id | module                                           
    ---+--------------------------------------------------
    s0 | hot_b64_bp2_r100_hot_s_nstr_n512_p1_np512_l1_sn1 
    s1 | itlb_f256_l1_r100_hot_s_nstr_n512_p1_np512_l1_sn1
single_counts:
    metric             | s0     | s1     
    -------------------+--------+--------
    cpu-cycles:u       | 106563 | 1794038
    instructions:u     | 117795 | 444241 
    br_retired:u       | 14803  | 27492  
    br_mis_pred:u      | 297    | 296    
    l1i_cache:u        | 17790  | 58911  
    l1i_cache_refill:u | 601    | 69319  
    l1i_tlb:u          | 17790  | 58911  
    l1i_tlb_refill:u   | 53     | 25856  
    l2i_cache:u        | 600    | 69319  
    l2i_cache_refill:u | 528    | 54892  
    l2i_tlb:u          | 96     | 25899  
    l2i_tlb_refill:u   | 21     | 189    
    l1d_cache:u        | 9780   | 28924  
    l1d_cache_refill:u | 150    | 289    
    l1d_tlb:u          | 10492  | 29685  
    l1d_tlb_refill:u   | 60     | 61     
    l2d_cache:u        | 1607   | 74462  
    l2d_cache_refill:u | 1002   | 55122  
    l2d_tlb:u          | 88     | 81     
    l2d_tlb_refill:u   | 28     | 11     
    ll_cache:u         | 406    | 656    
    ll_cache_miss:u    | 43     | 91     
combined_orders:
    id        | modules                                                                                           
    ----------+---------------------------------------------------------------------------------------------------
    canonical | hot_b64_bp2_r100_hot_s_nstr_n512_p1_np512_l1_sn1+itlb_f256_l1_r100_hot_s_nstr_n512_p1_np512_l1_sn1
    shuffle   | itlb_f256_l1_r100_hot_s_nstr_n512_p1_np512_l1_sn1+hot_b64_bp2_r100_hot_s_nstr_n512_p1_np512_l1_sn1
    sum       | hot_b64_bp2_r100_hot_s_nstr_n512_p1_np512_l1_sn1+itlb_f256_l1_r100_hot_s_nstr_n512_p1_np512_l1_sn1
combined_counts:
    metric             | canonical | shuffle | sum    
    -------------------+-----------+---------+--------
    cpu-cycles:u       | 2099643   | 1899230 | 1900601
    instructions:u     | 556938    | 556938  | 562036 
    br_retired:u       | 41296     | 41296   | 42295  
    br_mis_pred:u      | 311       | 306     | 593    
    l1i_cache:u        | 74759     | 74257   | 76701  
    l1i_cache_refill:u | 71272     | 69963   | 69920  
    l1i_tlb:u          | 74759     | 74257   | 76701  
    l1i_tlb_refill:u   | 25955     | 25957   | 25909  
    l2i_cache:u        | 71269     | 69961   | 69919  
    l2i_cache_refill:u | 54504     | 54892   | 55420  
    l2i_tlb:u          | 26008     | 26018   | 25995  
    l2i_tlb_refill:u   | 302       | 304     | 210    
    l1d_cache:u        | 36825     | 36779   | 38704  
    l1d_cache_refill:u | 256       | 179     | 439    
    l1d_tlb:u          | 37724     | 37695   | 40177  
    l1d_tlb_refill:u   | 57        | 61      | 121    
    l2d_cache:u        | 75282     | 75454   | 76069  
    l2d_cache_refill:u | 54877     | 56375   | 56124  
    l2d_tlb:u          | 84        | 85      | 169    
    l2d_tlb_refill:u   | 29        | 34      | 39     
    ll_cache:u         | 656       | 750     | 1062   
    ll_cache_miss:u    | 173       | 153     | 134    

