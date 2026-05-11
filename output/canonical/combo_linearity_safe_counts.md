== combo_linearity ==
source=/home/tchen/icache_test/output/combo_linearity_safe.csv
mode=csv_render_only
errors=not_computed
layout_snapshots=not_available_from_csv
cases=51
rows=306
metrics=22
metric_set=raw

== combo_000_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | hot_b128_bp3_r100_pstr_p128_np1_l4_sp3
    s1 | itlb_f64_l1_r100_lshuf_p512_np4_l2    
single_counts:
    metric             | s0        | s1      
    -------------------+-----------+---------
    cpu-cycles:u       | 219283571 | 70171077
    instructions:u     | 26000998  | 11930988
    br_retired:u       | 3941405   | 731403  
    br_mis_pred:u      | 482       | 471     
    l1i_cache:u        | 3340509   | 1594406 
    l1i_cache_refill:u | 1276      | 1182245 
    l1i_tlb:u          | 3340509   | 1594406 
    l1i_tlb_refill:u   | 50        | 660046  
    l2i_cache:u        | 1276      | 1182245 
    l2i_cache_refill:u | 727       | 42641   
    l2i_tlb:u          | 90        | 660082  
    l2i_tlb_refill:u   | 17        | 41      
    l1d_cache:u        | 5257314   | 1415516 
    l1d_cache_refill:u | 5020259   | 767956  
    l1d_tlb:u          | 10459169  | 1923630 
    l1d_tlb_refill:u   | 5140068   | 340056  
    l2d_cache:u        | 14550746  | 6674594 
    l2d_cache_refill:u | 4306029   | 2408716 
    l2d_tlb:u          | 5140492   | 340228  
    l2d_tlb_refill:u   | 95        | 748     
    ll_cache:u         | 4305262   | 2375306 
    ll_cache_miss:u    | 60        | 1739    
combined_orders:
    id        | modules                                                                  
    ----------+--------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_pstr_p128_np1_l4_sp3+itlb_f64_l1_r100_lshuf_p512_np4_l2
    shuffle   | itlb_f64_l1_r100_lshuf_p512_np4_l2+hot_b128_bp3_r100_pstr_p128_np1_l4_sp3
    sum       | hot_b128_bp3_r100_pstr_p128_np1_l4_sp3+itlb_f64_l1_r100_lshuf_p512_np4_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 247947348 | 319556002 | 289454648
    instructions:u     | 37921313  | 37921398  | 37931986 
    br_retired:u       | 4671604   | 4671613   | 4672808  
    br_mis_pred:u      | 617       | 577       | 953      
    l1i_cache:u        | 4939492   | 4956885   | 4934915  
    l1i_cache_refill:u | 975033    | 950671    | 1183521  
    l1i_tlb:u          | 4939492   | 4956885   | 4934915  
    l1i_tlb_refill:u   | 660369    | 660357    | 660096   
    l2i_cache:u        | 975031    | 950670    | 1183521  
    l2i_cache_refill:u | 116371    | 207958    | 43368    
    l2i_tlb:u          | 660435    | 660435    | 660172   
    l2i_tlb_refill:u   | 133       | 642       | 58       
    l1d_cache:u        | 6668788   | 6668820   | 6672830  
    l1d_cache_refill:u | 5782913   | 5720156   | 5788215  
    l1d_tlb:u          | 12370039  | 12336103  | 12382799 
    l1d_tlb_refill:u   | 5484465   | 5480095   | 5480124  
    l2d_cache:u        | 22183026  | 21984779  | 21225340 
    l2d_cache_refill:u | 7690365   | 7770887   | 6714745  
    l2d_tlb:u          | 5485096   | 5480879   | 5480720  
    l2d_tlb_refill:u   | 1719      | 1661      | 843      
    ll_cache:u         | 7571303   | 7544413   | 6680568  
    ll_cache_miss:u    | 14149     | 7436      | 1799     

== combo_001_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | hot_b128_bp3_r100_lin_p128_np4_l1
    s1 | itlb_f64_l1_r100_lin_p128_np4_l2 
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 30210190 | 51345437
    instructions:u     | 22160988 | 11930988
    br_retired:u       | 3941403  | 731403  
    br_mis_pred:u      | 432      | 504     
    l1i_cache:u        | 2848454  | 1589625 
    l1i_cache_refill:u | 736      | 1795432 
    l1i_tlb:u          | 2848454  | 1589625 
    l1i_tlb_refill:u   | 43       | 660076  
    l2i_cache:u        | 736      | 1795426 
    l2i_cache_refill:u | 603      | 133817  
    l2i_tlb:u          | 82       | 660157  
    l2i_tlb_refill:u   | 18       | 109     
    l1d_cache:u        | 1415496  | 1415459 
    l1d_cache_refill:u | 533460   | 374966  
    l1d_tlb:u          | 1973389  | 2043788 
    l1d_tlb_refill:u   | 340070   | 340063  
    l2d_cache:u        | 2854745  | 4268683 
    l2d_cache_refill:u | 474279   | 889396  
    l2d_tlb:u          | 341221   | 341344  
    l2d_tlb_refill:u   | 14       | 150     
    ll_cache:u         | 473585   | 731758  
    ll_cache_miss:u    | 2791     | 218     
combined_orders:
    id        | modules                                                           
    ----------+-------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_lin_p128_np4_l1+itlb_f64_l1_r100_lin_p128_np4_l2
    shuffle   | itlb_f64_l1_r100_lin_p128_np4_l2+hot_b128_bp3_r100_lin_p128_np4_l1
    sum       | hot_b128_bp3_r100_lin_p128_np4_l1+itlb_f64_l1_r100_lin_p128_np4_l2
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 80600882  | 75655476 | 81555627
    instructions:u     | 34081297  | 34081297 | 34091976
    br_retired:u       | 4671604   | 4671604  | 4672806 
    br_mis_pred:u      | 636       | 576      | 936     
    l1i_cache:u        | 4440871   | 4442513  | 4438079 
    l1i_cache_refill:u | 1493816   | 968508   | 1796168 
    l1i_tlb:u          | 4440871   | 4442513  | 4438079 
    l1i_tlb_refill:u   | 670280    | 670284   | 660119  
    l2i_cache:u        | 1493816   | 968508   | 1796162 
    l2i_cache_refill:u | 72762     | 30341    | 134420  
    l2i_tlb:u          | 670421    | 670457   | 660239  
    l2i_tlb_refill:u   | 36        | 46       | 127     
    l1d_cache:u        | 2826877   | 2826574  | 2830955 
    l1d_cache_refill:u | 878921    | 862330   | 908426  
    l1d_tlb:u          | 4037577   | 4072606  | 4017177 
    l1d_tlb_refill:u   | 680070    | 700062   | 680133  
    l2d_cache:u        | 7881710   | 7460885  | 7123428 
    l2d_cache_refill:u | 1823426   | 1610213  | 1363675 
    l2d_tlb:u          | 680784    | 700539   | 682565  
    l2d_tlb_refill:u   | 43        | 25       | 164     
    ll_cache:u         | 1737581   | 1578243  | 1205343 
    ll_cache_miss:u    | 444       | 660      | 3009    

== combo_002_s2 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | hot_b64_bp3_r100_lin_p128_np1_l1     
    s1 | itlb_f64_l1_r100_lstr_p512_np2_l1_sl3
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 27276694 | 57522534
    instructions:u     | 11280988 | 11290994
    br_retired:u       | 2021403  | 731401  
    br_mis_pred:u      | 403      | 505     
    l1i_cache:u        | 1487465  | 1504215 
    l1i_cache_refill:u | 627      | 1383744 
    l1i_tlb:u          | 1487465  | 1504215 
    l1i_tlb_refill:u   | 42       | 660095  
    l2i_cache:u        | 626      | 1383744 
    l2i_cache_refill:u | 514      | 64123   
    l2i_tlb:u          | 72       | 660184  
    l2i_tlb_refill:u   | 17       | 119     
    l1d_cache:u        | 775688   | 775414  
    l1d_cache_refill:u | 609900   | 655296  
    l1d_tlb:u          | 1497820  | 1520885 
    l1d_tlb_refill:u   | 660078   | 664893  
    l2d_cache:u        | 1761822  | 4122056 
    l2d_cache_refill:u | 465493   | 1368837 
    l2d_tlb:u          | 660241   | 664926  
    l2d_tlb_refill:u   | 20       | 118     
    ll_cache:u         | 464969   | 1282027 
    ll_cache_miss:u    | 40       | 260     
combined_orders:
    id        | modules                                                               
    ----------+-----------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_lin_p128_np1_l1+itlb_f64_l1_r100_lstr_p512_np2_l1_sl3
    shuffle   | itlb_f64_l1_r100_lstr_p512_np2_l1_sl3+hot_b64_bp3_r100_lin_p128_np1_l1
    sum       | hot_b64_bp3_r100_lin_p128_np1_l1+itlb_f64_l1_r100_lstr_p512_np2_l1_sl3
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 79105603  | 75364077 | 84799228
    instructions:u     | 22561297  | 22561297 | 22571982
    br_retired:u       | 2751604   | 2751604  | 2752804 
    br_mis_pred:u      | 618       | 565      | 908     
    l1i_cache:u        | 2995025   | 3007111  | 2991680 
    l1i_cache_refill:u | 1337115   | 1060712  | 1384371 
    l1i_tlb:u          | 2995025   | 3007111  | 2991680 
    l1i_tlb_refill:u   | 670146    | 670191   | 660137  
    l2i_cache:u        | 1337115   | 1060709  | 1384370 
    l2i_cache_refill:u | 37281     | 40249    | 64637   
    l2i_tlb:u          | 670235    | 670336   | 660256  
    l2i_tlb_refill:u   | 83        | 142      | 136     
    l1d_cache:u        | 1546596   | 1547009  | 1551102 
    l1d_cache_refill:u | 1245823   | 1249362  | 1265196 
    l1d_tlb:u          | 3032204   | 3031012  | 3018705 
    l1d_tlb_refill:u   | 1326696   | 1327554  | 1324971 
    l2d_cache:u        | 5785083   | 5588733  | 5883878 
    l2d_cache_refill:u | 1811617   | 2090260  | 1834330 
    l2d_tlb:u          | 1326870   | 1327833  | 1325167 
    l2d_tlb_refill:u   | 1065      | 320      | 138     
    ll_cache:u         | 1774966   | 2059846  | 1746996 
    ll_cache_miss:u    | 2865      | 2273     | 300     

== combo_003_s2 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp3       
    s1 | fetch_b64_d1_bp0_s16_r100_lstr_p512_np1_l1_sl3
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 35198327 | 60213112
    instructions:u     | 12950988 | 18231003
    br_retired:u       | 1031403  | 1991402 
    br_mis_pred:u      | 130663   | 591996  
    l1i_cache:u        | 3505558  | 9226415 
    l1i_cache_refill:u | 682      | 640     
    l1i_tlb:u          | 3505558  | 9226415 
    l1i_tlb_refill:u   | 49       | 45      
    l2i_cache:u        | 681      | 640     
    l2i_cache_refill:u | 602      | 571     
    l2i_tlb:u          | 90       | 85      
    l2i_tlb_refill:u   | 15       | 21      
    l1d_cache:u        | 1536186  | 4005359 
    l1d_cache_refill:u | 615215   | 653513  
    l1d_tlb:u          | 2287251  | 6592736 
    l1d_tlb_refill:u   | 660081   | 682069  
    l2d_cache:u        | 2177657  | 2766076 
    l2d_cache_refill:u | 811508   | 1306225 
    l2d_tlb:u          | 660346   | 685543  
    l2d_tlb_refill:u   | 17       | 72      
    ll_cache:u         | 810894   | 1305577 
    ll_cache_miss:u    | 3576     | 4942    
combined_orders:
    id        | modules                                                                               
    ----------+---------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp3+fetch_b64_d1_bp0_s16_r100_lstr_p512_np1_l1_sl3
    shuffle   | fetch_b64_d1_bp0_s16_r100_lstr_p512_np1_l1_sl3+cold_b64_d4_bitrev_pstr_p128_np4_l1_sp3
    sum       | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp3+fetch_b64_d1_bp0_s16_r100_lstr_p512_np1_l1_sl3
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 74841925  | 99839538 | 95411439
    instructions:u     | 31171297  | 31171303 | 31181991
    br_retired:u       | 3021604   | 3021602  | 3022805 
    br_mis_pred:u      | 727055    | 721556   | 722659  
    l1i_cache:u        | 12106780  | 11936224 | 12731973
    l1i_cache_refill:u | 892       | 893      | 1322    
    l1i_tlb:u          | 12106780  | 11936224 | 12731973
    l1i_tlb_refill:u   | 46        | 54       | 94      
    l2i_cache:u        | 892       | 892      | 1321    
    l2i_cache_refill:u | 726       | 761      | 1173    
    l2i_tlb:u          | 74        | 116      | 175     
    l2i_tlb_refill:u   | 26        | 36       | 36      
    l1d_cache:u        | 5617396   | 5605922  | 5541545 
    l1d_cache_refill:u | 1234334   | 1232805  | 1268728 
    l1d_tlb:u          | 9098154   | 9044532  | 8879987 
    l1d_tlb_refill:u   | 1342932   | 1350719  | 1342150 
    l2d_cache:u        | 4702071   | 4802508  | 4943733 
    l2d_cache_refill:u | 1883556   | 1946609  | 2117733 
    l2d_tlb:u          | 1358308   | 1363626  | 1345889 
    l2d_tlb_refill:u   | 691       | 133      | 89      
    ll_cache:u         | 1882645   | 1945812  | 2116471 
    ll_cache_miss:u    | 3378      | 7565     | 8518    

== combo_004_s2 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | hot_b128_bp3_r100_lshuf_p1_np1_l4    
    s1 | itlb_f64_l1_r100_pstr_p512_np4_l2_sp3
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 25723644 | 85138776
    instructions:u     | 26001040 | 11930988
    br_retired:u       | 3941409  | 731403  
    br_mis_pred:u      | 496      | 473     
    l1i_cache:u        | 3327280  | 1588557 
    l1i_cache_refill:u | 760      | 1155553 
    l1i_tlb:u          | 3327280  | 1588557 
    l1i_tlb_refill:u   | 53       | 660049  
    l2i_cache:u        | 759      | 1155552 
    l2i_cache_refill:u | 646      | 63289   
    l2i_tlb:u          | 95       | 660093  
    l2i_tlb_refill:u   | 25       | 44      
    l1d_cache:u        | 5255326  | 1415478 
    l1d_cache_refill:u | 143      | 1280457 
    l1d_tlb:u          | 5257269  | 2801707 
    l1d_tlb_refill:u   | 60       | 1304709 
    l2d_cache:u        | 1213     | 6402844 
    l2d_cache_refill:u | 804      | 2644514 
    l2d_tlb:u          | 123      | 1304738 
    l2d_tlb_refill:u   | 8        | 215     
    ll_cache:u         | 203      | 2565260 
    ll_cache_miss:u    | 28       | 253     
combined_orders:
    id        | modules                                                                
    ----------+------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_lshuf_p1_np1_l4+itlb_f64_l1_r100_pstr_p512_np4_l2_sp3
    shuffle   | itlb_f64_l1_r100_pstr_p512_np4_l2_sp3+hot_b128_bp3_r100_lshuf_p1_np1_l4
    sum       | hot_b128_bp3_r100_lshuf_p1_np1_l4+itlb_f64_l1_r100_pstr_p512_np4_l2_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 110808921 | 110768179 | 110862420
    instructions:u     | 37921288  | 37921288  | 37932028 
    br_retired:u       | 4671603   | 4671603   | 4672812  
    br_mis_pred:u      | 636       | 619       | 969      
    l1i_cache:u        | 4919793   | 4924081   | 4915837  
    l1i_cache_refill:u | 949790    | 917233    | 1156313  
    l1i_tlb:u          | 4919793   | 4924081   | 4915837  
    l1i_tlb_refill:u   | 660358    | 660356    | 660102   
    l2i_cache:u        | 949788    | 917233    | 1156311  
    l2i_cache_refill:u | 48815     | 37512     | 63935    
    l2i_tlb:u          | 660421    | 660423    | 660188   
    l2i_tlb_refill:u   | 80        | 74        | 69       
    l1d_cache:u        | 6665940   | 6665793   | 6670804  
    l1d_cache_refill:u | 1279152   | 1281047   | 1280600  
    l1d_tlb:u          | 8040449   | 8106328   | 8058976  
    l1d_tlb_refill:u   | 1303399   | 1320232   | 1304769  
    l2d_cache:u        | 6197523   | 5934442   | 6404057  
    l2d_cache_refill:u | 2623095   | 2604323   | 2645318  
    l2d_tlb:u          | 1303432   | 1320269   | 1304861  
    l2d_tlb_refill:u   | 306       | 600       | 223      
    ll_cache:u         | 2572535   | 2566707   | 2565463  
    ll_cache_miss:u    | 368       | 413       | 281      

== combo_005_s2 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | hot_b64_bp3_r100_pstr_p512_np1_l1_sp3
    s1 | itlb_f64_l1_r100_lstr_p1_np2_l1_sl5  
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 29653628 | 19178829
    instructions:u     | 11281003 | 11291040
    br_retired:u       | 2021402  | 731409  
    br_mis_pred:u      | 429      | 502     
    l1i_cache:u        | 1488999  | 1496012 
    l1i_cache_refill:u | 615      | 1057889 
    l1i_tlb:u          | 1488999  | 1496012 
    l1i_tlb_refill:u   | 41       | 660184  
    l2i_cache:u        | 614      | 1057887 
    l2i_cache_refill:u | 529      | 842     
    l2i_tlb:u          | 130      | 660251  
    l2i_tlb_refill:u   | 26       | 81      
    l1d_cache:u        | 775989   | 775150  
    l1d_cache_refill:u | 640114   | 147     
    l1d_tlb:u          | 1517120  | 776753  
    l1d_tlb_refill:u   | 663676   | 61      
    l2d_cache:u        | 2528478  | 1047289 
    l2d_cache_refill:u | 1281721  | 1136    
    l2d_tlb:u          | 663923   | 82      
    l2d_tlb_refill:u   | 171      | 14      
    ll_cache:u         | 1281062  | 255     
    ll_cache_miss:u    | 42       | 56      
combined_orders:
    id        | modules                                                                  
    ----------+--------------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_pstr_p512_np1_l1_sp3+itlb_f64_l1_r100_lstr_p1_np2_l1_sl5
    shuffle   | itlb_f64_l1_r100_lstr_p1_np2_l1_sl5+hot_b64_bp3_r100_pstr_p512_np1_l1_sp3
    sum       | hot_b64_bp3_r100_pstr_p512_np1_l1_sp3+itlb_f64_l1_r100_lstr_p1_np2_l1_sl5
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 65631194  | 75433000 | 48832457
    instructions:u     | 22561288  | 22561288 | 22572043
    br_retired:u       | 2751603   | 2751603  | 2752811 
    br_mis_pred:u      | 558       | 599      | 931     
    l1i_cache:u        | 2976434   | 2977664  | 2985011 
    l1i_cache_refill:u | 1398319   | 1434752  | 1058504 
    l1i_tlb:u          | 2976434   | 2977664  | 2985011 
    l1i_tlb_refill:u   | 670152    | 670171   | 660225  
    l2i_cache:u        | 1398316   | 1434752  | 1058501 
    l2i_cache_refill:u | 11489     | 12351    | 1371    
    l2i_tlb:u          | 670203    | 670237   | 660381  
    l2i_tlb_refill:u   | 64        | 63       | 107     
    l1d_cache:u        | 1546216   | 1546665  | 1551139 
    l1d_cache_refill:u | 640212    | 640129   | 640261  
    l1d_tlb:u          | 2307442   | 2308212  | 2293873 
    l1d_tlb_refill:u   | 666618    | 666527   | 663737  
    l2d_cache:u        | 3671069   | 3524294  | 3575767 
    l2d_cache_refill:u | 1292759   | 1293009  | 1282857 
    l2d_tlb:u          | 666755    | 666753   | 664005  
    l2d_tlb_refill:u   | 174       | 640      | 185     
    ll_cache:u         | 1282295   | 1282159  | 1281317 
    ll_cache_miss:u    | 506       | 1780     | 98      

== combo_006_s2 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl3
    s1 | hot_b128_bp3_r100_pstr_p128_np4_l2_sp3  
single_counts:
    metric             | s0        | s1      
    -------------------+-----------+---------
    cpu-cycles:u       | 157973648 | 86905973
    instructions:u     | 29430988  | 23440988
    br_retired:u       | 1991403   | 3941403 
    br_mis_pred:u      | 290677    | 455     
    l1i_cache:u        | 7531278   | 3009863 
    l1i_cache_refill:u | 1220      | 810     
    l1i_tlb:u          | 7531278   | 3009863 
    l1i_tlb_refill:u   | 54        | 43      
    l2i_cache:u        | 1219      | 809     
    l2i_cache_refill:u | 787       | 630     
    l2i_tlb:u          | 97        | 156     
    l2i_tlb_refill:u   | 46        | 11      
    l1d_cache:u        | 6836578   | 2696842 
    l1d_cache_refill:u | 4136747   | 2437532 
    l1d_tlb:u          | 11216292  | 5352809 
    l1d_tlb_refill:u   | 3860063   | 2582316 
    l2d_cache:u        | 14915353  | 7869945 
    l2d_cache_refill:u | 4163339   | 2417842 
    l2d_tlb:u          | 3860249   | 2582669 
    l2d_tlb_refill:u   | 161       | 166     
    ll_cache:u         | 4162267   | 2417053 
    ll_cache_miss:u    | 23075     | 651     
combined_orders:
    id        | modules                                                                        
    ----------+--------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl3+hot_b128_bp3_r100_pstr_p128_np4_l2_sp3
    shuffle   | hot_b128_bp3_r100_pstr_p128_np4_l2_sp3+cold_b128_d4_bitrev_lstr_p128_np4_l4_sl3
    sum       | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl3+hot_b128_bp3_r100_pstr_p128_np4_l2_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 318443908 | 231108094 | 244879621
    instructions:u     | 52861389  | 52861298  | 52871976 
    br_retired:u       | 5931612   | 5931605   | 5932806  
    br_mis_pred:u      | 291036    | 291015    | 291132   
    l1i_cache:u        | 10554073  | 10612984  | 10541141 
    l1i_cache_refill:u | 3040      | 2733      | 2030     
    l1i_tlb:u          | 10554073  | 10612984  | 10541141 
    l1i_tlb_refill:u   | 61        | 62        | 97       
    l2i_cache:u        | 3041      | 2733      | 2028     
    l2i_cache_refill:u | 1414      | 1352      | 1417     
    l2i_tlb:u          | 109       | 107       | 253      
    l2i_tlb_refill:u   | 30        | 49        | 57       
    l1d_cache:u        | 9520687   | 9509942   | 9533420  
    l1d_cache_refill:u | 7035470   | 7070135   | 6574279  
    l1d_tlb:u          | 16321119  | 16255105  | 16569101 
    l1d_tlb_refill:u   | 6446537   | 6445863   | 6442379  
    l2d_cache:u        | 23508090  | 22670867  | 22785298 
    l2d_cache_refill:u | 7006599   | 6294316   | 6581181  
    l2d_tlb:u          | 6449292   | 6446375   | 6442918  
    l2d_tlb_refill:u   | 300       | 289       | 327      
    ll_cache:u         | 7005025   | 6292864   | 6579320  
    ll_cache_miss:u    | 9554      | 3284      | 23726    

== combo_007_s2 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | cold_b128_d4_bitrev_lin_p512_np1_l2
    s1 | itlb_f64_l1_r100_lshuf_p1_np2_l4   
single_counts:
    metric             | s0        | s1      
    -------------------+-----------+---------
    cpu-cycles:u       | 149859393 | 29551789
    instructions:u     | 26870988  | 13210988
    br_retired:u       | 1991403   | 731403  
    br_mis_pred:u      | 290729    | 467     
    l1i_cache:u        | 7143886   | 1726025 
    l1i_cache_refill:u | 1076      | 1839372 
    l1i_tlb:u          | 7143886   | 1726025 
    l1i_tlb_refill:u   | 55        | 670056  
    l2i_cache:u        | 1075      | 1839371 
    l2i_cache_refill:u | 795       | 814     
    l2i_tlb:u          | 114       | 670136  
    l2i_tlb_refill:u   | 52        | 99      
    l1d_cache:u        | 4257831   | 2695275 
    l1d_cache_refill:u | 2534689   | 144     
    l1d_tlb:u          | 7019281   | 2697061 
    l1d_tlb_refill:u   | 2600060   | 64      
    l2d_cache:u        | 11107332  | 1569930 
    l2d_cache_refill:u | 5302743   | 1174    
    l2d_tlb:u          | 2610070   | 85      
    l2d_tlb_refill:u   | 663       | 33      
    ll_cache:u         | 5301706   | 319     
    ll_cache_miss:u    | 6251      | 41      
combined_orders:
    id        | modules                                                             
    ----------+---------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lin_p512_np1_l2+itlb_f64_l1_r100_lshuf_p1_np2_l4
    shuffle   | itlb_f64_l1_r100_lshuf_p1_np2_l4+cold_b128_d4_bitrev_lin_p512_np1_l2
    sum       | cold_b128_d4_bitrev_lin_p512_np1_l2+itlb_f64_l1_r100_lshuf_p1_np2_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 169735662 | 286319637 | 179411182
    instructions:u     | 40071288  | 40071389  | 40081976 
    br_retired:u       | 2721603   | 2721612   | 2722806  
    br_mis_pred:u      | 290949    | 291095    | 291196   
    l1i_cache:u        | 9013477   | 8909439   | 8869911  
    l1i_cache_refill:u | 1086987   | 1323667   | 1840448  
    l1i_tlb:u          | 9013477   | 8909439   | 8869911  
    l1i_tlb_refill:u   | 670499    | 670458    | 670111   
    l2i_cache:u        | 1086987   | 1323662   | 1840446  
    l2i_cache_refill:u | 94102     | 102908    | 1609     
    l2i_tlb:u          | 670624    | 670551    | 670250   
    l2i_tlb_refill:u   | 146       | 176       | 151      
    l1d_cache:u        | 6957979   | 6947520   | 6953106  
    l1d_cache_refill:u | 2547199   | 2535683   | 2534833  
    l1d_tlb:u          | 9756005   | 9629505   | 9716342  
    l1d_tlb_refill:u   | 2600259   | 2583103   | 2600124  
    l2d_cache:u        | 12086587  | 12201205  | 12677262 
    l2d_cache_refill:u | 5440030   | 5512818   | 5303917  
    l2d_tlb:u          | 2600292   | 2583139   | 2610155  
    l2d_tlb_refill:u   | 208       | 149       | 696      
    ll_cache:u         | 5344230   | 5410054   | 5302025  
    ll_cache_miss:u    | 34332     | 6456      | 6292     

== combo_008_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p1_np4_l4      
    s1 | hot_b128_bp3_r100_pstr_p512_np1_l2_sp3
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 16433548 | 193311894
    instructions:u     | 14871040 | 23440994 
    br_retired:u       | 1031409  | 3941401  
    br_mis_pred:u      | 130646   | 509      
    l1i_cache:u        | 3733121  | 3024364  
    l1i_cache_refill:u | 703      | 1215     
    l1i_tlb:u          | 3733121  | 3024364  
    l1i_tlb_refill:u   | 57       | 53       
    l2i_cache:u        | 702      | 1214     
    l2i_cache_refill:u | 639      | 753      
    l2i_tlb:u          | 100      | 103      
    l2i_tlb_refill:u   | 25       | 41       
    l1d_cache:u        | 3455363  | 2698627  
    l1d_cache_refill:u | 143      | 2558685  
    l1d_tlb:u          | 3457592  | 5352357  
    l1d_tlb_refill:u   | 65       | 2581891  
    l2d_cache:u        | 1456     | 10138260 
    l2d_cache_refill:u | 1007     | 5124680  
    l2d_tlb:u          | 86       | 2582519  
    l2d_tlb_refill:u   | 31       | 551      
    ll_cache:u         | 344      | 5123745  
    ll_cache_miss:u    | 49       | 504      
combined_orders:
    id        | modules                                                                
    ----------+------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p1_np4_l4+hot_b128_bp3_r100_pstr_p512_np1_l2_sp3
    shuffle   | hot_b128_bp3_r100_pstr_p512_np1_l2_sp3+cold_b64_d4_bitrev_lin_p1_np4_l4
    sum       | cold_b64_d4_bitrev_lin_p1_np4_l4+hot_b128_bp3_r100_pstr_p512_np1_l2_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 133214111 | 182440162 | 209745442
    instructions:u     | 38301288  | 38301294  | 38312034 
    br_retired:u       | 4971603   | 4971601   | 4972810  
    br_mis_pred:u      | 131194    | 130899    | 131155   
    l1i_cache:u        | 6746315   | 6746939   | 6757485  
    l1i_cache_refill:u | 1619      | 1458      | 1918     
    l1i_tlb:u          | 6746315   | 6746939   | 6757485  
    l1i_tlb_refill:u   | 53        | 52        | 110      
    l2i_cache:u        | 1618      | 1458      | 1916     
    l2i_cache_refill:u | 847       | 833       | 1392     
    l2i_tlb:u          | 111       | 86        | 203      
    l2i_tlb_refill:u   | 46        | 21        | 66       
    l1d_cache:u        | 6147891   | 6149296   | 6153990  
    l1d_cache_refill:u | 2559831   | 2559613   | 2558828  
    l1d_tlb:u          | 8819052   | 8821616   | 8809949  
    l1d_tlb_refill:u   | 2584851   | 2584792   | 2581956  
    l2d_cache:u        | 10196314  | 10249204  | 10139716 
    l2d_cache_refill:u | 5168330   | 5199413   | 5125687  
    l2d_tlb:u          | 2585253   | 2585295   | 2582605  
    l2d_tlb_refill:u   | 521       | 662       | 582      
    ll_cache:u         | 5167302   | 5198216   | 5124089  
    ll_cache_miss:u    | 7245      | 32539     | 553      

== combo_009_s2 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl5         
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p512_np2_l2_sp3
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 16415986 | 81460382
    instructions:u     | 14871049 | 18871003
    br_retired:u       | 1031410  | 1991402 
    br_mis_pred:u      | 130656   | 592137  
    l1i_cache:u        | 3735160  | 9245067 
    l1i_cache_refill:u | 742      | 685     
    l1i_tlb:u          | 3735160  | 9245067 
    l1i_tlb_refill:u   | 59       | 51      
    l2i_cache:u        | 742      | 683     
    l2i_cache_refill:u | 645      | 598     
    l2i_tlb:u          | 94       | 103     
    l2i_tlb_refill:u   | 22       | 26      
    l1d_cache:u        | 3455345  | 4666774 
    l1d_cache_refill:u | 162      | 1268805 
    l1d_tlb:u          | 3457556  | 7951519 
    l1d_tlb_refill:u   | 60       | 1320754 
    l2d_cache:u        | 1356     | 5553183 
    l2d_cache_refill:u | 868      | 2676118 
    l2d_tlb:u          | 85       | 1330780 
    l2d_tlb_refill:u   | 32       | 156     
    ll_cache:u         | 213      | 2675372 
    ll_cache_miss:u    | 32       | 18484   
combined_orders:
    id        | modules                                                                             
    ----------+-------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl5+fetch_b64_d1_bp0_s16_r100_pstr_p512_np2_l2_sp3
    shuffle   | fetch_b64_d1_bp0_s16_r100_pstr_p512_np2_l2_sp3+cold_b64_d4_bitrev_lstr_p1_np2_l4_sl5
    sum       | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl5+fetch_b64_d1_bp0_s16_r100_pstr_p512_np2_l2_sp3
combined_counts:
    metric             | canonical | shuffle   | sum     
    -------------------+-----------+-----------+---------
    cpu-cycles:u       | 127006261 | 129430028 | 97876368
    instructions:u     | 33731288  | 33731288  | 33742052
    br_retired:u       | 3021603   | 3021603   | 3022812 
    br_mis_pred:u      | 722462    | 721547    | 722793  
    l1i_cache:u        | 12379311  | 12385713  | 12980227
    l1i_cache_refill:u | 986       | 929       | 1427    
    l1i_tlb:u          | 12379311  | 12385713  | 12980227
    l1i_tlb_refill:u   | 53        | 56        | 110     
    l2i_cache:u        | 985       | 928       | 1425    
    l2i_cache_refill:u | 799       | 778       | 1243    
    l2i_tlb:u          | 101       | 92        | 197     
    l2i_tlb_refill:u   | 32        | 30        | 48      
    l1d_cache:u        | 8149754   | 8151916   | 8122119 
    l1d_cache_refill:u | 1266434   | 1269023   | 1268967 
    l1d_tlb:u          | 11442066  | 11427818  | 11409075
    l1d_tlb_refill:u   | 1323038   | 1312228   | 1320814 
    l2d_cache:u        | 5595451   | 5706487   | 5554539 
    l2d_cache_refill:u | 2685205   | 2677317   | 2676986 
    l2d_tlb:u          | 1325353   | 1312876   | 1330865 
    l2d_tlb_refill:u   | 113       | 88        | 188     
    ll_cache:u         | 2684360   | 2676492   | 2675585 
    ll_cache_miss:u    | 10355     | 18502     | 18516   

== combo_010_s2 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lstr_p512_np4_l1_sl5
    s1 | itlb_f64_l1_r100_lstr_p128_np4_l4_sl3          
single_counts:
    metric             | s0        | s1       
    -------------------+-----------+----------
    cpu-cycles:u       | 125315699 | 115682158
    instructions:u     | 36150997  | 13210988 
    br_retired:u       | 3911404   | 731403   
    br_mis_pred:u      | 1231838   | 504      
    l1i_cache:u        | 18281287  | 1803741  
    l1i_cache_refill:u | 1582      | 1398680  
    l1i_tlb:u          | 18281287  | 1803741  
    l1i_tlb_refill:u   | 47        | 670071   
    l2i_cache:u        | 1582      | 1398680  
    l2i_cache_refill:u | 886       | 235453   
    l2i_tlb:u          | 89        | 670141   
    l2i_tlb_refill:u   | 26        | 117      
    l1d_cache:u        | 7867294   | 2695873  
    l1d_cache_refill:u | 1298971   | 2032443  
    l1d_tlb:u          | 13026971  | 5087815  
    l1d_tlb_refill:u   | 1323296   | 1950070  
    l2d_cache:u        | 6122682   | 8288585  
    l2d_cache_refill:u | 2704082   | 2628514  
    l2d_tlb:u          | 1337296   | 1950103  
    l2d_tlb_refill:u   | 543       | 136      
    ll_cache:u         | 2703245   | 2411490  
    ll_cache_miss:u    | 37695     | 295      
combined_orders:
    id        | modules                                                                              
    ----------+--------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lstr_p512_np4_l1_sl5+itlb_f64_l1_r100_lstr_p128_np4_l4_sl3
    shuffle   | itlb_f64_l1_r100_lstr_p128_np4_l4_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p512_np4_l1_sl5
    sum       | fetch_b128_d1_bp0_s16_r100_lstr_p512_np4_l1_sl5+itlb_f64_l1_r100_lstr_p128_np4_l4_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 246879558 | 281033078 | 240997857
    instructions:u     | 49351298  | 49351389  | 49361985 
    br_retired:u       | 4641605   | 4641612   | 4642807  
    br_mis_pred:u      | 1236675   | 1238071   | 1232342  
    l1i_cache:u        | 18835681  | 18906356  | 20085028 
    l1i_cache_refill:u | 1218589   | 1065279   | 1400262  
    l1i_tlb:u          | 18835681  | 18906356  | 20085028 
    l1i_tlb_refill:u   | 670454    | 670457    | 670118   
    l2i_cache:u        | 1218589   | 1065279   | 1400262  
    l2i_cache_refill:u | 348577    | 309565    | 236339   
    l2i_tlb:u          | 670657    | 670615    | 670230   
    l2i_tlb_refill:u   | 135       | 554       | 143      
    l1d_cache:u        | 10662680  | 10601568  | 10563167 
    l1d_cache_refill:u | 3554835   | 3588850   | 3331414  
    l1d_tlb:u          | 18045109  | 17904632  | 18114786 
    l1d_tlb_refill:u   | 3262325   | 3263203   | 3273366  
    l2d_cache:u        | 14988591  | 15111453  | 14411267 
    l2d_cache_refill:u | 5624315   | 6082079   | 5332596  
    l2d_tlb:u          | 3274571   | 3267566   | 3287399  
    l2d_tlb_refill:u   | 1845      | 519       | 679      
    ll_cache:u         | 5342576   | 5796458   | 5114735  
    ll_cache_miss:u    | 19263     | 33082     | 37990    

== combo_011_s2 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | cold_b64_d4_bitrev_lshuf_p1_np4_l4
    s1 | hot_b128_bp3_r100_rand_p128_np2_l4
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 16407259 | 150427842
    instructions:u     | 14871040 | 26000988 
    br_retired:u       | 1031409  | 3941403  
    br_mis_pred:u      | 130589   | 483      
    l1i_cache:u        | 3735560  | 3341267  
    l1i_cache_refill:u | 702      | 1168     
    l1i_tlb:u          | 3735560  | 3341267  
    l1i_tlb_refill:u   | 44       | 50       
    l2i_cache:u        | 701      | 1168     
    l2i_cache_refill:u | 615      | 697      
    l2i_tlb:u          | 73       | 187      
    l2i_tlb_refill:u   | 12       | 39       
    l1d_cache:u        | 3455393  | 5257718  
    l1d_cache_refill:u | 160      | 4894838  
    l1d_tlb:u          | 3457341  | 9862088  
    l1d_tlb_refill:u   | 56       | 4520114  
    l2d_cache:u        | 1264     | 14586392 
    l2d_cache_refill:u | 836      | 4342675  
    l2d_tlb:u          | 73       | 4520650  
    l2d_tlb_refill:u   | 31       | 13       
    ll_cache:u         | 228      | 4341865  
    ll_cache_miss:u    | 23       | 2764     
combined_orders:
    id        | modules                                                              
    ----------+----------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lshuf_p1_np4_l4+hot_b128_bp3_r100_rand_p128_np2_l4
    shuffle   | hot_b128_bp3_r100_rand_p128_np2_l4+cold_b64_d4_bitrev_lshuf_p1_np4_l4
    sum       | cold_b64_d4_bitrev_lshuf_p1_np4_l4+hot_b128_bp3_r100_rand_p128_np2_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 161081263 | 157627756 | 166835101
    instructions:u     | 40861288  | 40861288  | 40872028 
    br_retired:u       | 4971603   | 4971603   | 4972812  
    br_mis_pred:u      | 130828    | 131021    | 131072   
    l1i_cache:u        | 7062958   | 7064847   | 7076827  
    l1i_cache_refill:u | 1573      | 1604      | 1870     
    l1i_tlb:u          | 7062958   | 7064847   | 7076827  
    l1i_tlb_refill:u   | 56        | 53        | 94       
    l2i_cache:u        | 1572      | 1603      | 1869     
    l2i_cache_refill:u | 864       | 847       | 1312     
    l2i_tlb:u          | 197       | 87        | 260      
    l2i_tlb_refill:u   | 49        | 15        | 51       
    l1d_cache:u        | 8707328   | 8707346   | 8713111  
    l1d_cache_refill:u | 4957404   | 4937545   | 4894998  
    l1d_tlb:u          | 13252006  | 13274534  | 13319429 
    l1d_tlb_refill:u   | 4490392   | 4490409   | 4520170  
    l2d_cache:u        | 14463861  | 14904561  | 14587656 
    l2d_cache_refill:u | 4128731   | 4609730   | 4343511  
    l2d_tlb:u          | 4490772   | 4490743   | 4520723  
    l2d_tlb_refill:u   | 152       | 145       | 44       
    ll_cache:u         | 4127762   | 4608682   | 4342093  
    ll_cache_miss:u    | 1449      | 395       | 2787     

== combo_012_s2 ==
single_modules:
    id | module                                   
    ---+------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p128_np2_l2_sp33
    s1 | hot_b64_bp3_r100_lstr_p512_np2_l4_sl3    
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 88339814 | 144149248
    instructions:u     | 26870988 | 13200988 
    br_retired:u       | 1991403  | 2021403  
    br_mis_pred:u      | 290679   | 452      
    l1i_cache:u        | 7138125  | 1740404  
    l1i_cache_refill:u | 864      | 894      
    l1i_tlb:u          | 7138125  | 1740404  
    l1i_tlb_refill:u   | 46       | 56       
    l2i_cache:u        | 863      | 892      
    l2i_cache_refill:u | 708      | 647      
    l2i_tlb:u          | 85       | 132      
    l2i_tlb_refill:u   | 16       | 43       
    l1d_cache:u        | 4266952  | 2697547  
    l1d_cache_refill:u | 2400239  | 2559225  
    l1d_tlb:u          | 7001480  | 5363406  
    l1d_tlb_refill:u   | 2590361  | 2584254  
    l2d_cache:u        | 7880709  | 10140279 
    l2d_cache_refill:u | 2372275  | 5133643  
    l2d_tlb:u          | 2590488  | 2584772  
    l2d_tlb_refill:u   | 161      | 623      
    ll_cache:u         | 2371380  | 5132851  
    ll_cache_miss:u    | 24824    | 1860     
combined_orders:
    id        | modules                                                                        
    ----------+--------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p128_np2_l2_sp33+hot_b64_bp3_r100_lstr_p512_np2_l4_sl3
    shuffle   | hot_b64_bp3_r100_lstr_p512_np2_l4_sl3+cold_b128_d4_bitrev_pstr_p128_np2_l2_sp33
    sum       | cold_b128_d4_bitrev_pstr_p128_np2_l2_sp33+hot_b64_bp3_r100_lstr_p512_np2_l4_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 223599693 | 243571526 | 232489062
    instructions:u     | 40061304  | 40061298  | 40071976 
    br_retired:u       | 4011603   | 4011605   | 4012806  
    br_mis_pred:u      | 291195    | 290912    | 291131   
    l1i_cache:u        | 8884309   | 8851175   | 8878529  
    l1i_cache_refill:u | 1645      | 1774      | 1758     
    l1i_tlb:u          | 8884309   | 8851175   | 8878529  
    l1i_tlb_refill:u   | 48        | 49        | 102      
    l2i_cache:u        | 1646      | 1774      | 1755     
    l2i_cache_refill:u | 924       | 955       | 1355     
    l2i_tlb:u          | 190       | 94        | 217      
    l2i_tlb_refill:u   | 26        | 30        | 59       
    l1d_cache:u        | 6948710   | 6967523   | 6964499  
    l1d_cache_refill:u | 4907365   | 4960524   | 4959464  
    l1d_tlb:u          | 12385215  | 12411514  | 12364886 
    l1d_tlb_refill:u   | 5194635   | 5184986   | 5174615  
    l2d_cache:u        | 18262799  | 18280588  | 18020988 
    l2d_cache_refill:u | 7456219   | 7543462   | 7505918  
    l2d_tlb:u          | 5196746   | 5185759   | 5175260  
    l2d_tlb_refill:u   | 694       | 139       | 784      
    ll_cache:u         | 7454949   | 7542352   | 7504231  
    ll_cache_miss:u    | 22837     | 16801     | 26684    

== combo_013_s2 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p128_np4_l1_sl3
    s1 | itlb_f64_l1_r100_pstr_p128_np2_l2_sp33  
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 56941581 | 60878797
    instructions:u     | 25590988 | 11930988
    br_retired:u       | 1991403  | 731403  
    br_mis_pred:u      | 290733   | 446     
    l1i_cache:u        | 7109645  | 1634693 
    l1i_cache_refill:u | 940      | 1115246 
    l1i_tlb:u          | 7109645  | 1634693 
    l1i_tlb_refill:u   | 56       | 660054  
    l2i_cache:u        | 938      | 1115244 
    l2i_cache_refill:u | 787      | 209100  
    l2i_tlb:u          | 110      | 660086  
    l2i_tlb_refill:u   | 48       | 17      
    l1d_cache:u        | 2984396  | 1415381 
    l1d_cache_refill:u | 1206102  | 1222883 
    l1d_tlb:u          | 4076529  | 2797539 
    l1d_tlb_refill:u   | 980065   | 1304236 
    l2d_cache:u        | 3824788  | 5613373 
    l2d_cache_refill:u | 1069066  | 1538814 
    l2d_tlb:u          | 980855   | 1304261 
    l2d_tlb_refill:u   | 137      | 159     
    ll_cache:u         | 1068192  | 1380592 
    ll_cache_miss:u    | 9429     | 554     
combined_orders:
    id        | modules                                                                        
    ----------+--------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p128_np4_l1_sl3+itlb_f64_l1_r100_pstr_p128_np2_l2_sp33
    shuffle   | itlb_f64_l1_r100_pstr_p128_np2_l2_sp33+cold_b128_d4_bitrev_lstr_p128_np4_l1_sl3
    sum       | cold_b128_d4_bitrev_lstr_p128_np4_l1_sl3+itlb_f64_l1_r100_pstr_p128_np2_l2_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 139408778 | 107062609 | 117820378
    instructions:u     | 37511297  | 37511297  | 37521976 
    br_retired:u       | 2721604   | 2721604   | 2722806  
    br_mis_pred:u      | 290981    | 290819    | 291179   
    l1i_cache:u        | 8663600   | 8687889   | 8744338  
    l1i_cache_refill:u | 1184942   | 1187409   | 1116186  
    l1i_tlb:u          | 8663600   | 8687889   | 8744338  
    l1i_tlb_refill:u   | 660597    | 660554    | 660110   
    l2i_cache:u        | 1184941   | 1187407   | 1116182  
    l2i_cache_refill:u | 251858    | 190484    | 209887   
    l2i_tlb:u          | 660707    | 660597    | 660196   
    l2i_tlb_refill:u   | 23        | 26        | 65       
    l1d_cache:u        | 4386778   | 4388313   | 4399777  
    l1d_cache_refill:u | 2416754   | 2419085   | 2428985  
    l1d_tlb:u          | 6845723   | 6845909   | 6874068  
    l1d_tlb_refill:u   | 2282123   | 2282864   | 2284301  
    l2d_cache:u        | 9348448   | 9506965   | 9438161  
    l2d_cache_refill:u | 2560539   | 2743987   | 2607880  
    l2d_tlb:u          | 2284367   | 2285394   | 2285116  
    l2d_tlb_refill:u   | 52        | 46        | 296      
    ll_cache:u         | 2346057   | 2562263   | 2448784  
    ll_cache_miss:u    | 13208     | 4646      | 9983     

== combo_014_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | hot_b128_bp3_r100_lstr_p512_np2_l1_sl9
    s1 | itlb_f64_l1_r100_pstr_p512_np2_l2_sp3 
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 99131642 | 82657183
    instructions:u     | 22160988 | 11930988
    br_retired:u       | 3941403  | 731403  
    br_mis_pred:u      | 458      | 458     
    l1i_cache:u        | 2856079  | 1585319 
    l1i_cache_refill:u | 896      | 1335525 
    l1i_tlb:u          | 2856079  | 1585319 
    l1i_tlb_refill:u   | 42       | 660068  
    l2i_cache:u        | 895      | 1335524 
    l2i_cache_refill:u | 654      | 90213   
    l2i_tlb:u          | 137      | 660128  
    l2i_tlb_refill:u   | 18       | 46      
    l1d_cache:u        | 1416570  | 1415684 
    l1d_cache_refill:u | 1280107  | 1279368 
    l1d_tlb:u          | 2795461  | 2796859 
    l1d_tlb_refill:u   | 1303163  | 1303900 
    l2d_cache:u        | 5058826  | 5990992 
    l2d_cache_refill:u | 2564516  | 2639264 
    l2d_tlb:u          | 1303552  | 1303935 
    l2d_tlb_refill:u   | 92       | 649     
    ll_cache:u         | 2563854  | 2566014 
    ll_cache_miss:u    | 412      | 2626    
combined_orders:
    id        | modules                                                                     
    ----------+-----------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_lstr_p512_np2_l1_sl9+itlb_f64_l1_r100_pstr_p512_np2_l2_sp3
    shuffle   | itlb_f64_l1_r100_pstr_p512_np2_l2_sp3+hot_b128_bp3_r100_lstr_p512_np2_l1_sl9
    sum       | hot_b128_bp3_r100_lstr_p512_np2_l1_sl9+itlb_f64_l1_r100_pstr_p512_np2_l2_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 233981295 | 191867086 | 181788825
    instructions:u     | 34081307  | 34081303  | 34091976 
    br_retired:u       | 4671606   | 4671602   | 4672806  
    br_mis_pred:u      | 613       | 589       | 916      
    l1i_cache:u        | 4471120   | 4464578   | 4441398  
    l1i_cache_refill:u | 954558    | 1077080   | 1336421  
    l1i_tlb:u          | 4471120   | 4464578   | 4441398  
    l1i_tlb_refill:u   | 670259    | 670247    | 660110   
    l2i_cache:u        | 954558    | 1077078   | 1336419  
    l2i_cache_refill:u | 165786    | 165848    | 90867    
    l2i_tlb:u          | 670340    | 670402    | 660265   
    l2i_tlb_refill:u   | 4864      | 4746      | 64       
    l1d_cache:u        | 2827969   | 2828385   | 2832254  
    l1d_cache_refill:u | 2557121   | 2562494   | 2559475  
    l1d_tlb:u          | 5635504   | 5603766   | 5592320  
    l1d_tlb_refill:u   | 2611074   | 2606104   | 2607063  
    l2d_cache:u        | 11489286  | 11165161  | 11049818 
    l2d_cache_refill:u | 5339892   | 5252893   | 5203780  
    l2d_tlb:u          | 2611429   | 2606524   | 2607487  
    l2d_tlb_refill:u   | 21900     | 22365     | 741      
    ll_cache:u         | 5158492   | 5132694   | 5129868  
    ll_cache_miss:u    | 6705      | 1364      | 3038     

== combo_015_s2 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p512_np1_l1_sl3        
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l4_sp33
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 57854793 | 203869503
    instructions:u     | 12950988 | 20151003 
    br_retired:u       | 1031403  | 1991402  
    br_mis_pred:u      | 130685   | 595405   
    l1i_cache:u        | 3451989  | 9549609  
    l1i_cache_refill:u | 809      | 860      
    l1i_tlb:u          | 3451989  | 9549609  
    l1i_tlb_refill:u   | 45       | 51       
    l2i_cache:u        | 807      | 859      
    l2i_cache_refill:u | 618      | 689      
    l2i_tlb:u          | 84       | 109      
    l2i_tlb_refill:u   | 23       | 44       
    l1d_cache:u        | 1536651  | 5954346  
    l1d_cache_refill:u | 640210   | 2522526  
    l1d_tlb:u          | 2348182  | 10540006 
    l1d_tlb_refill:u   | 675381   | 2600545  
    l2d_cache:u        | 2529298  | 11201914 
    l2d_cache_refill:u | 1282048  | 5367143  
    l2d_tlb:u          | 675474   | 2614939  
    l2d_tlb_refill:u   | 543      | 59       
    ll_cache:u         | 1281278  | 5366347  
    ll_cache_miss:u    | 404      | 124163   
combined_orders:
    id        | modules                                                                                
    ----------+----------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p512_np1_l1_sl3+fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l4_sp33
    shuffle   | fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l4_sp33+cold_b64_d4_bitrev_lstr_p512_np1_l1_sl3
    sum       | cold_b64_d4_bitrev_lstr_p512_np1_l1_sl3+fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l4_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 235516712 | 206483926 | 261724296
    instructions:u     | 33091307  | 33091297  | 33101991 
    br_retired:u       | 3021606   | 3021604   | 3022805  
    br_mis_pred:u      | 724638    | 723639    | 726090   
    l1i_cache:u        | 12277033  | 12327331  | 13001598 
    l1i_cache_refill:u | 1050      | 1022      | 1669     
    l1i_tlb:u          | 12277033  | 12327331  | 13001598 
    l1i_tlb_refill:u   | 52        | 52        | 96       
    l2i_cache:u        | 1049      | 1021      | 1666     
    l2i_cache_refill:u | 826       | 828       | 1307     
    l2i_tlb:u          | 108       | 98        | 193      
    l2i_tlb_refill:u   | 44        | 43        | 67       
    l1d_cache:u        | 7533437   | 7544972   | 7490997  
    l1d_cache_refill:u | 3155449   | 3161448   | 3162736  
    l1d_tlb:u          | 12973479  | 12983966  | 12888188 
    l1d_tlb_refill:u   | 3275755   | 3268114   | 3275926  
    l2d_cache:u        | 14008779  | 13909799  | 13731212 
    l2d_cache_refill:u | 6732372   | 6633867   | 6649191  
    l2d_tlb:u          | 3282291   | 3278465   | 3290413  
    l2d_tlb_refill:u   | 4997      | 4640      | 602      
    ll_cache:u         | 6730857   | 6632305   | 6647625  
    ll_cache_miss:u    | 65752     | 43081     | 124567   

== combo_016_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b128_d4_bitrev_rand_p512_np1_l1  
    s1 | itlb_f64_l1_r100_pstr_p512_np1_l1_sp17
single_counts:
    metric             | s0        | s1      
    -------------------+-----------+---------
    cpu-cycles:u       | 105431077 | 60027793
    instructions:u     | 25590994  | 11290988
    br_retired:u       | 1991401   | 731403  
    br_mis_pred:u      | 290642    | 474     
    l1i_cache:u        | 6988593   | 1490733 
    l1i_cache_refill:u | 1342      | 1523184 
    l1i_tlb:u          | 6988593   | 1490733 
    l1i_tlb_refill:u   | 55        | 660070  
    l2i_cache:u        | 1341      | 1523184 
    l2i_cache_refill:u | 820       | 77583   
    l2i_tlb:u          | 111       | 660112  
    l2i_tlb_refill:u   | 45        | 44      
    l1d_cache:u        | 2976986   | 775525  
    l1d_cache_refill:u | 1263969   | 638846  
    l1d_tlb:u          | 4386234   | 1524057 
    l1d_tlb_refill:u   | 1303867   | 665154  
    l2d_cache:u        | 5497271   | 3538905 
    l2d_cache_refill:u | 2717480   | 1354893 
    l2d_tlb:u          | 1303899   | 665191  
    l2d_tlb_refill:u   | 503       | 637     
    ll_cache:u         | 2716527   | 1296896 
    ll_cache_miss:u    | 27562     | 12272   
combined_orders:
    id        | modules                                                                    
    ----------+----------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_rand_p512_np1_l1+itlb_f64_l1_r100_pstr_p512_np1_l1_sp17
    shuffle   | itlb_f64_l1_r100_pstr_p512_np1_l1_sp17+cold_b128_d4_bitrev_rand_p512_np1_l1
    sum       | cold_b128_d4_bitrev_rand_p512_np1_l1+itlb_f64_l1_r100_pstr_p512_np1_l1_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 163424429 | 175340293 | 165458870
    instructions:u     | 36871297  | 36871303  | 36881982 
    br_retired:u       | 2721604   | 2721602   | 2722804  
    br_mis_pred:u      | 290836    | 291029    | 291116   
    l1i_cache:u        | 8516980   | 8508307   | 8479326  
    l1i_cache_refill:u | 1216221   | 1071246   | 1524526  
    l1i_tlb:u          | 8516980   | 8508307   | 8479326  
    l1i_tlb_refill:u   | 660556    | 660549    | 660125   
    l2i_cache:u        | 1216219   | 1071246   | 1524525  
    l2i_cache_refill:u | 202347    | 124406    | 78403    
    l2i_tlb:u          | 660802    | 660667    | 660223   
    l2i_tlb_refill:u   | 4921      | 4814      | 89       
    l1d_cache:u        | 3747364   | 3747799   | 3752511  
    l1d_cache_refill:u | 1903509   | 1906424   | 1902815  
    l1d_tlb:u          | 5933809   | 6018196   | 5910291  
    l1d_tlb_refill:u   | 1978521   | 2001056   | 1969021  
    l2d_cache:u        | 9362348   | 9040305   | 9036176  
    l2d_cache_refill:u | 4202392   | 4179731   | 4072373  
    l2d_tlb:u          | 1980259   | 2002338   | 1969090  
    l2d_tlb_refill:u   | 22812     | 21981     | 1140     
    ll_cache:u         | 3970460   | 4090256   | 4013423  
    ll_cache_miss:u    | 34697     | 47642     | 39834    

== combo_017_s3 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lin_p128_np4_l4
    s1 | hot_b64_bp3_r100_lshuf_p512_np2_l1        
    s2 | itlb_f64_l1_r100_lstr_p1_np4_l1_sl3       
single_counts:
    metric             | s0        | s1       | s2      
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 135714864 | 47975404 | 24109784
    instructions:u     | 39990997  | 11280994 | 11291049
    br_retired:u       | 3911404   | 2021401  | 731410  
    br_mis_pred:u      | 1237794   | 487      | 461     
    l1i_cache:u        | 18887480  | 1491001  | 1527046 
    l1i_cache_refill:u | 996       | 759      | 950204  
    l1i_tlb:u          | 18887480  | 1491001  | 1527046 
    l1i_tlb_refill:u   | 48        | 54       | 660101  
    l2i_cache:u        | 994       | 759      | 950203  
    l2i_cache_refill:u | 757       | 589      | 62618   
    l2i_tlb:u          | 90        | 128      | 660193  
    l2i_tlb_refill:u   | 16        | 46       | 33      
    l1d_cache:u        | 11830343  | 776022   | 775387  
    l1d_cache_refill:u | 1013246   | 606943   | 139     
    l1d_tlb:u          | 17934740  | 1237754  | 777246  
    l1d_tlb_refill:u   | 1310067   | 340062   | 61      
    l2d_cache:u        | 13911287  | 2580305  | 1083680 
    l2d_cache_refill:u | 2535892   | 1274512  | 63264   
    l2d_tlb:u          | 1320105   | 340088   | 81      
    l2d_tlb_refill:u   | 152       | 556      | 36      
    ll_cache:u         | 2535053   | 1273814  | 426     
    ll_cache_miss:u    | 179281    | 1202     | 119     
combined_orders:
    id        | modules                                                                                                          
    ----------+------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lin_p128_np4_l4+hot_b64_bp3_r100_lshuf_p512_np2_l1+itlb_f64_l1_r100_lstr_p1_np4_l1_sl3
    shuffle   | hot_b64_bp3_r100_lshuf_p512_np2_l1+itlb_f64_l1_r100_lstr_p1_np4_l1_sl3+fetch_b128_d1_bp0_s16_r100_lin_p128_np4_l4
    sum       | fetch_b128_d1_bp0_s16_r100_lin_p128_np4_l4+hot_b64_bp3_r100_lshuf_p512_np2_l1+itlb_f64_l1_r100_lstr_p1_np4_l1_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 243491845 | 209564276 | 207800052
    instructions:u     | 62541607  | 62541607  | 62563040 
    br_retired:u       | 6661806   | 6661806   | 6664215  
    br_mis_pred:u      | 1251142   | 1234232   | 1238742  
    l1i_cache:u        | 20655245  | 20585283  | 21905527 
    l1i_cache_refill:u | 1080467   | 1423526   | 951959   
    l1i_tlb:u          | 20655245  | 20585283  | 21905527 
    l1i_tlb_refill:u   | 660658    | 660649    | 660203   
    l2i_cache:u        | 1080465   | 1423524   | 951956   
    l2i_cache_refill:u | 209505    | 14670     | 63964    
    l2i_tlb:u          | 660756    | 660704    | 660411   
    l2i_tlb_refill:u   | 627       | 78        | 95       
    l1d_cache:u        | 13377966  | 13319592  | 13381752 
    l1d_cache_refill:u | 2444283   | 2273614   | 1620328  
    l1d_tlb:u          | 20062594  | 19659837  | 19949740 
    l1d_tlb_refill:u   | 1650171   | 1650166   | 1650190  
    l2d_cache:u        | 16347760  | 19069830  | 17575272 
    l2d_cache_refill:u | 4574060   | 5175676   | 3873668  
    l2d_tlb:u          | 1656249   | 1659397   | 1660274  
    l2d_tlb_refill:u   | 1371      | 609       | 744      
    ll_cache:u         | 4382939   | 5161228   | 3809293  
    ll_cache_miss:u    | 25944     | 157814    | 180602   

== combo_018_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np1_l2_sp3
    s1 | hot_b128_bp3_r100_lin_p1_np2_l4                
    s2 | itlb_f64_l1_r100_rand_p512_np1_l1              
single_counts:
    metric             | s0        | s1       | s2      
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 156144603 | 25732652 | 68259472
    instructions:u     | 37430997  | 26001040 | 11290988
    br_retired:u       | 3911404   | 3941409  | 731403  
    br_mis_pred:u      | 1231302   | 484      | 484     
    l1i_cache:u        | 18306825  | 3337177  | 1514910 
    l1i_cache_refill:u | 1172      | 759      | 1546010 
    l1i_tlb:u          | 18306825  | 3337177  | 1514910 
    l1i_tlb_refill:u   | 47        | 52       | 660050  
    l2i_cache:u        | 1172      | 759      | 1546010 
    l2i_cache_refill:u | 733       | 646      | 234297  
    l2i_tlb:u          | 97        | 116      | 660122  
    l2i_tlb_refill:u   | 27        | 44       | 124     
    l1d_cache:u        | 9129459   | 5255509  | 775500  
    l1d_cache_refill:u | 2544284   | 140      | 640056  
    l1d_tlb:u          | 15606954  | 5257679  | 1580077 
    l1d_tlb_refill:u   | 2602977   | 62       | 680064  
    l2d_cache:u        | 11154639  | 1267     | 3475306 
    l2d_cache_refill:u | 5198730   | 821      | 1426213 
    l2d_tlb:u          | 2618804   | 84       | 680094  
    l2d_tlb_refill:u   | 83        | 4        | 104     
    ll_cache:u         | 5197825   | 205      | 1282635 
    ll_cache_miss:u    | 433       | 20       | 80      
combined_orders:
    id        | modules                                                                                                          
    ----------+------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_pstr_p512_np1_l2_sp3+hot_b128_bp3_r100_lin_p1_np2_l4+itlb_f64_l1_r100_rand_p512_np1_l1
    shuffle   | hot_b128_bp3_r100_lin_p1_np2_l4+fetch_b128_d1_bp0_s16_r100_pstr_p512_np1_l2_sp3+itlb_f64_l1_r100_rand_p512_np1_l1
    sum       | fetch_b128_d1_bp0_s16_r100_pstr_p512_np1_l2_sp3+hot_b128_bp3_r100_lin_p1_np2_l4+itlb_f64_l1_r100_rand_p512_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 302816661 | 373695587 | 250136727
    instructions:u     | 74701689  | 74701542  | 74723025 
    br_retired:u       | 8581812   | 8581792   | 8584216  
    br_mis_pred:u      | 1237449   | 1232047   | 1232270  
    l1i_cache:u        | 21978290  | 21966413  | 23158912 
    l1i_cache_refill:u | 1128131   | 1011766   | 1547941  
    l1i_tlb:u          | 21978290  | 21966413  | 23158912 
    l1i_tlb_refill:u   | 660741    | 660747    | 660149   
    l2i_cache:u        | 1128129   | 1011764   | 1547941  
    l2i_cache_refill:u | 203860    | 171898    | 235676   
    l2i_tlb:u          | 665195    | 660938    | 660335   
    l2i_tlb_refill:u   | 5101      | 5223      | 195      
    l1d_cache:u        | 15212746  | 15226910  | 15160468 
    l1d_cache_refill:u | 3188851   | 3176069   | 3184480  
    l1d_tlb:u          | 22597611  | 22516542  | 22444710 
    l1d_tlb_refill:u   | 3275081   | 3273289   | 3283103  
    l2d_cache:u        | 14574557  | 14682332  | 14631212 
    l2d_cache_refill:u | 6820707   | 7128737   | 6625764  
    l2d_tlb:u          | 3275339   | 3277280   | 3298982  
    l2d_tlb_refill:u   | 23538     | 23273     | 191      
    ll_cache:u         | 6654358   | 6970148   | 6480665  
    ll_cache_miss:u    | 44307     | 69453     | 533      

== combo_019_s3 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | cold_b128_d4_bitrev_lin_p1_np4_l4  
    s1 | hot_b128_bp3_r100_lshuf_p128_np1_l4
    s2 | itlb_f64_l1_r100_lin_p512_np2_l1   
single_counts:
    metric             | s0       | s1        | s2      
    -------------------+----------+-----------+---------
    cpu-cycles:u       | 33520950 | 164957336 | 57112673
    instructions:u     | 29430988 | 26000988  | 11290988
    br_retired:u       | 1991403  | 3941403   | 731403  
    br_mis_pred:u      | 290637   | 618       | 490     
    l1i_cache:u        | 7478530  | 3339532   | 1483022 
    l1i_cache_refill:u | 876      | 1065      | 1333840 
    l1i_tlb:u          | 7478530  | 3339532   | 1483022 
    l1i_tlb_refill:u   | 48       | 53        | 660052  
    l2i_cache:u        | 876      | 1063      | 1333839 
    l2i_cache_refill:u | 701      | 689       | 12044   
    l2i_tlb:u          | 83       | 111       | 660117  
    l2i_tlb_refill:u   | 15       | 42        | 51      
    l1d_cache:u        | 6815380  | 5256829   | 775416  
    l1d_cache_refill:u | 158      | 4886801   | 620995  
    l1d_tlb:u          | 6817459  | 10512865  | 1211639 
    l1d_tlb_refill:u   | 69       | 5148553   | 340058  
    l2d_cache:u        | 1586     | 15138693  | 3525859 
    l2d_cache_refill:u | 1004     | 4891051   | 1296123 
    l2d_tlb:u          | 101      | 5149020   | 340247  
    l2d_tlb_refill:u   | 6        | 10        | 585     
    ll_cache:u         | 300      | 4890337   | 1280796 
    ll_cache_miss:u    | 28       | 137       | 278     
combined_orders:
    id        | modules                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lin_p1_np4_l4+hot_b128_bp3_r100_lshuf_p128_np1_l4+itlb_f64_l1_r100_lin_p512_np2_l1
    shuffle   | cold_b128_d4_bitrev_lin_p1_np4_l4+itlb_f64_l1_r100_lin_p512_np2_l1+hot_b128_bp3_r100_lshuf_p128_np1_l4
    sum       | cold_b128_d4_bitrev_lin_p1_np4_l4+hot_b128_bp3_r100_lshuf_p128_np1_l4+itlb_f64_l1_r100_lin_p512_np2_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 293895831 | 313036897 | 255590959
    instructions:u     | 66701698  | 66701698  | 66722964 
    br_retired:u       | 6661813   | 6661813   | 6664209  
    br_mis_pred:u      | 290975    | 291353    | 291745   
    l1i_cache:u        | 12329911  | 12340403  | 12301084 
    l1i_cache_refill:u | 1088871   | 1134041   | 1335781  
    l1i_tlb:u          | 12329911  | 12340403  | 12301084 
    l1i_tlb_refill:u   | 660860    | 660860    | 660153   
    l2i_cache:u        | 1088871   | 1134040   | 1335778  
    l2i_cache_refill:u | 85227     | 121998    | 13434    
    l2i_tlb:u          | 660937    | 660970    | 660311   
    l2i_tlb_refill:u   | 212       | 305       | 108      
    l1d_cache:u        | 12839547  | 12838616  | 12847625 
    l1d_cache_refill:u | 5459713   | 5419380   | 5507954  
    l1d_tlb:u          | 18559893  | 18484202  | 18541963 
    l1d_tlb_refill:u   | 5509144   | 5480268   | 5488680  
    l2d_cache:u        | 19563964  | 18791283  | 18666138 
    l2d_cache_refill:u | 6797127   | 5889469   | 6188178  
    l2d_tlb:u          | 5510043   | 5481050   | 5489368  
    l2d_tlb_refill:u   | 950       | 2733      | 601      
    ll_cache:u         | 6703975   | 5766859   | 6171433  
    ll_cache_miss:u    | 35962     | 16859     | 443      

== combo_020_s3 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | cold_b64_d4_bitrev_lshuf_p128_np2_l2 
    s1 | hot_b64_bp3_r100_rand_p512_np4_l2    
    s2 | itlb_f64_l1_r100_lstr_p128_np2_l2_sl3
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 42242091 | 67319687 | 68842839
    instructions:u     | 13590988 | 11920988 | 11930988
    br_retired:u       | 1031403  | 2021403  | 731403  
    br_mis_pred:u      | 130688   | 457      | 461     
    l1i_cache:u        | 3553044  | 1580788  | 1682226 
    l1i_cache_refill:u | 730      | 695      | 1347640 
    l1i_tlb:u          | 3553044  | 1580788  | 1682226 
    l1i_tlb_refill:u   | 53       | 40       | 660125  
    l2i_cache:u        | 729      | 695      | 1347638 
    l2i_cache_refill:u | 629      | 566      | 296367  
    l2i_tlb:u          | 101      | 168      | 660230  
    l2i_tlb_refill:u   | 44       | 15       | 29      
    l1d_cache:u        | 2175873  | 1416403  | 1415387 
    l1d_cache_refill:u | 1093544  | 1279100  | 1254142 
    l1d_tlb:u          | 2997568  | 2725789  | 2769150 
    l1d_tlb_refill:u   | 660062   | 1248312  | 1300207 
    l2d_cache:u        | 4223123  | 5079601  | 5442914 
    l2d_cache_refill:u | 1302528  | 2570720  | 1994772 
    l2d_tlb:u          | 660096   | 1248511  | 1300240 
    l2d_tlb_refill:u   | 151      | 71       | 27      
    ll_cache:u         | 1301822  | 2570103  | 1680594 
    ll_cache_miss:u    | 187      | 691      | 248     
combined_orders:
    id        | modules                                                                                                     
    ----------+-------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lshuf_p128_np2_l2+hot_b64_bp3_r100_rand_p512_np4_l2+itlb_f64_l1_r100_lstr_p128_np2_l2_sl3
    shuffle   | hot_b64_bp3_r100_rand_p512_np4_l2+itlb_f64_l1_r100_lstr_p128_np2_l2_sl3+cold_b64_d4_bitrev_lshuf_p128_np2_l2
    sum       | cold_b64_d4_bitrev_lshuf_p128_np2_l2+hot_b64_bp3_r100_rand_p512_np4_l2+itlb_f64_l1_r100_lstr_p128_np2_l2_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 264178996 | 226576497 | 178404617
    instructions:u     | 37421698  | 37421607  | 37442964 
    br_retired:u       | 3781813   | 3781806   | 3784209  
    br_mis_pred:u      | 131124    | 131093    | 131606   
    l1i_cache:u        | 6840388   | 6876318   | 6816058  
    l1i_cache_refill:u | 1336436   | 1005586   | 1349065  
    l1i_tlb:u          | 6840388   | 6876318   | 6816058  
    l1i_tlb_refill:u   | 660456    | 660450    | 660218   
    l2i_cache:u        | 1336432   | 1005585   | 1349062  
    l2i_cache_refill:u | 403606    | 216550    | 297562   
    l2i_tlb:u          | 660525    | 660492    | 660499   
    l2i_tlb_refill:u   | 591       | 573       | 88       
    l1d_cache:u        | 4998753   | 4998639   | 5007663  
    l1d_cache_refill:u | 3681042   | 3688249   | 3626786  
    l1d_tlb:u          | 8462695   | 8555792   | 8492507  
    l1d_tlb_refill:u   | 3216645   | 3250863   | 3208581  
    l2d_cache:u        | 14760410  | 15312865  | 14745638 
    l2d_cache_refill:u | 5631093   | 6026439   | 5868020  
    l2d_tlb:u          | 3219316   | 3251365   | 3208847  
    l2d_tlb_refill:u   | 2807      | 3221      | 249      
    ll_cache:u         | 5327551   | 5773887   | 5552519  
    ll_cache_miss:u    | 70557     | 52977     | 1126     

== combo_021_s3 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | fetch_b64_d1_bp0_s16_r100_lstr_p128_np2_l4_sl3
    s1 | hot_b64_bp3_r100_lin_p512_np1_l2              
    s2 | itlb_f64_l1_r100_pstr_p128_np4_l1_sp17        
single_counts:
    metric             | s0        | s1        | s2      
    -------------------+-----------+-----------+---------
    cpu-cycles:u       | 107890267 | 107293455 | 53772985
    instructions:u     | 20151003  | 11920988  | 11290988
    br_retired:u       | 1991402   | 2021403   | 731403  
    br_mis_pred:u      | 592114    | 490       | 531     
    l1i_cache:u        | 9281571   | 1576843   | 1535922 
    l1i_cache_refill:u | 710       | 854       | 901897  
    l1i_tlb:u          | 9281571   | 1576843   | 1535922 
    l1i_tlb_refill:u   | 46        | 52        | 660058  
    l2i_cache:u        | 709       | 855       | 901897  
    l2i_cache_refill:u | 633       | 615       | 36145   
    l2i_tlb:u          | 75        | 181       | 660099  
    l2i_tlb_refill:u   | 19        | 46        | 24      
    l1d_cache:u        | 5987758   | 1416775   | 775422  
    l1d_cache_refill:u | 2364424   | 1280094   | 613424  
    l1d_tlb:u          | 10513812  | 2787332   | 1502778 
    l1d_tlb_refill:u   | 2590058   | 1301543   | 662279  
    l2d_cache:u        | 7914418   | 5057511   | 3535266 
    l2d_cache_refill:u | 2265570   | 2562656   | 701862  
    l2d_tlb:u          | 2590153   | 1301880   | 662322  
    l2d_tlb_refill:u   | 149       | 628       | 18      
    ll_cache:u         | 2264811   | 2561933   | 674755  
    ll_cache_miss:u    | 13881     | 1387      | 237     
combined_orders:
    id        | modules                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp0_s16_r100_lstr_p128_np2_l4_sl3+hot_b64_bp3_r100_lin_p512_np1_l2+itlb_f64_l1_r100_pstr_p128_np4_l1_sp17
    shuffle   | hot_b64_bp3_r100_lin_p512_np1_l2+fetch_b64_d1_bp0_s16_r100_lstr_p128_np2_l4_sl3+itlb_f64_l1_r100_pstr_p128_np4_l1_sp17
    sum       | fetch_b64_d1_bp0_s16_r100_lstr_p128_np2_l4_sl3+hot_b64_bp3_r100_lin_p512_np1_l2+itlb_f64_l1_r100_pstr_p128_np4_l1_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 248307128 | 236700676 | 268956707
    instructions:u     | 43341607  | 43341607  | 43362979 
    br_retired:u       | 4741806   | 4741806   | 4744208  
    br_mis_pred:u      | 592826    | 591874    | 593135   
    l1i_cache:u        | 11781711  | 11793422  | 12394336 
    l1i_cache_refill:u | 1302704   | 1056642   | 903461   
    l1i_tlb:u          | 11781711  | 11793422  | 12394336 
    l1i_tlb_refill:u   | 660455    | 660447    | 660156   
    l2i_cache:u        | 1302703   | 1056641   | 903461   
    l2i_cache_refill:u | 40155     | 33109     | 37393    
    l2i_tlb:u          | 663258    | 660535    | 660355   
    l2i_tlb_refill:u   | 681       | 491       | 89       
    l1d_cache:u        | 8150401   | 8161087   | 8179955  
    l1d_cache_refill:u | 4305897   | 4268595   | 4257942  
    l1d_tlb:u          | 14933171  | 14810187  | 14803922 
    l1d_tlb_refill:u   | 4578691   | 4567521   | 4553880  
    l2d_cache:u        | 16290934  | 15472945  | 16507195 
    l2d_cache_refill:u | 5528719   | 4946536   | 5530088  
    l2d_tlb:u          | 4599205   | 4572192   | 4554355  
    l2d_tlb_refill:u   | 3305      | 2662      | 795      
    ll_cache:u         | 5496662   | 4922958   | 5501499  
    ll_cache_miss:u    | 2392      | 3491      | 15505    

== combo_022_s3 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p128_np4_l2         
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l1_sp3
    s2 | hot_b64_bp3_r100_lshuf_p512_np1_l4            
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 78022591 | 50328242 | 148986567
    instructions:u     | 26870988 | 18230997 | 13200988 
    br_retired:u       | 1991403  | 1991404  | 2021403  
    br_mis_pred:u      | 290747   | 590513   | 465      
    l1i_cache:u        | 7242373  | 9059876  | 1740069  
    l1i_cache_refill:u | 1191     | 762      | 963      
    l1i_tlb:u          | 7242373  | 9059876  | 1740069  
    l1i_tlb_refill:u   | 61       | 47       | 52       
    l2i_cache:u        | 1189     | 762      | 961      
    l2i_cache_refill:u | 853      | 597      | 638      
    l2i_tlb:u          | 117      | 95       | 178      
    l2i_tlb_refill:u   | 48       | 15       | 48       
    l1d_cache:u        | 4256385  | 4065846  | 2697355  
    l1d_cache_refill:u | 1609375  | 614445   | 2560023  
    l1d_tlb:u          | 5245141  | 6715961  | 5364198  
    l1d_tlb_refill:u   | 670063   | 682615   | 2584501  
    l2d_cache:u        | 7461542  | 1947895  | 10104913 
    l2d_cache_refill:u | 1418521  | 533845   | 5123458  
    l2d_tlb:u          | 670135   | 693341   | 2585014  
    l2d_tlb_refill:u   | 153      | 145      | 591      
    ll_cache:u         | 1417555  | 533148   | 5122679  
    ll_cache_miss:u    | 1378     | 37       | 122      
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p128_np4_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l1_sp3+hot_b64_bp3_r100_lshuf_p512_np1_l4
    shuffle   | fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l1_sp3+hot_b64_bp3_r100_lshuf_p512_np1_l4+cold_b128_d4_bitrev_lshuf_p128_np4_l2
    sum       | cold_b128_d4_bitrev_lshuf_p128_np4_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l1_sp3+hot_b64_bp3_r100_lshuf_p512_np1_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 254856636 | 255810376 | 277337400
    instructions:u     | 58281607  | 58281613  | 58302973 
    br_retired:u       | 6001806   | 6001804   | 6004210  
    br_mis_pred:u      | 883649    | 881666    | 881725   
    l1i_cache:u        | 17391627  | 17356850  | 18042318 
    l1i_cache_refill:u | 2357      | 2659      | 2916     
    l1i_tlb:u          | 17391627  | 17356850  | 18042318 
    l1i_tlb_refill:u   | 50        | 49        | 160      
    l2i_cache:u        | 2356      | 2659      | 2912     
    l2i_cache_refill:u | 1235      | 1301      | 2088     
    l2i_tlb:u          | 180       | 93        | 390      
    l2i_tlb_refill:u   | 29        | 31        | 111      
    l1d_cache:u        | 10999750  | 10980372  | 11019586 
    l1d_cache_refill:u | 4738352   | 4802637   | 4783843  
    l1d_tlb:u          | 17166193  | 17172274  | 17325300 
    l1d_tlb_refill:u   | 3912437   | 3939869   | 3937179  
    l2d_cache:u        | 20993468  | 21205187  | 19514350 
    l2d_cache_refill:u | 7053091   | 7698515   | 7075824  
    l2d_tlb:u          | 3914775   | 3947831   | 3948490  
    l2d_tlb_refill:u   | 394       | 283       | 889      
    ll_cache:u         | 7051677   | 7696970   | 7073382  
    ll_cache_miss:u    | 21971     | 40759     | 1537     

== combo_023_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p512_np4_l1_sp33      
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l4_sp3
    s2 | hot_b64_bp3_r100_lstr_p128_np4_l1_sl3          
single_counts:
    metric             | s0        | s1        | s2      
    -------------------+-----------+-----------+---------
    cpu-cycles:u       | 109220878 | 336078185 | 19118309
    instructions:u     | 25590988  | 39990951  | 11281040
    br_retired:u       | 1991403   | 3911393   | 2021409 
    br_mis_pred:u      | 293537    | 1233787   | 466     
    l1i_cache:u        | 7068832   | 18737198  | 1487591 
    l1i_cache_refill:u | 874       | 1413      | 648     
    l1i_tlb:u          | 7068832   | 18737198  | 1487591 
    l1i_tlb_refill:u   | 50        | 53        | 52      
    l2i_cache:u        | 873       | 1411      | 646     
    l2i_cache_refill:u | 736       | 902       | 568     
    l2i_tlb:u          | 97        | 107       | 164     
    l2i_tlb_refill:u   | 23        | 45        | 42      
    l1d_cache:u        | 2977897   | 11758555  | 775769  
    l1d_cache_refill:u | 1272733   | 5054402   | 617501  
    l1d_tlb:u          | 4393906   | 20866480  | 1332317 
    l1d_tlb_refill:u   | 1305503   | 5163213   | 500091  
    l2d_cache:u        | 5624911   | 22743155  | 1827648 
    l2d_cache_refill:u | 2642477   | 10858656  | 546091  
    l2d_tlb:u          | 1305539   | 5172899   | 500258  
    l2d_tlb_refill:u   | 627       | 691       | 22      
    ll_cache:u         | 2641551   | 10857258  | 545503  
    ll_cache_miss:u    | 17792     | 152033    | 351     
combined_orders:
    id        | modules                                                                                                                        
    ----------+--------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p512_np4_l1_sp33+fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l4_sp3+hot_b64_bp3_r100_lstr_p128_np4_l1_sl3
    shuffle   | cold_b128_d4_bitrev_pstr_p512_np4_l1_sp33+hot_b64_bp3_r100_lstr_p128_np4_l1_sl3+fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l4_sp3
    sum       | cold_b128_d4_bitrev_pstr_p512_np4_l1_sp33+fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l4_sp3+hot_b64_bp3_r100_lstr_p128_np4_l1_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 645118912 | 584435219 | 464417372
    instructions:u     | 76841557  | 76841564  | 76862979 
    br_retired:u       | 7921791   | 7921793   | 7924205  
    br_mis_pred:u      | 1543453   | 1546935   | 1527790  
    l1i_cache:u        | 26250544  | 26290537  | 27293621 
    l1i_cache_refill:u | 5956      | 5549      | 2935     
    l1i_tlb:u          | 26250544  | 26290537  | 27293621 
    l1i_tlb_refill:u   | 52        | 53        | 155      
    l2i_cache:u        | 5956      | 5546      | 2930     
    l2i_cache_refill:u | 2157      | 2038      | 2206     
    l2i_tlb:u          | 94        | 99        | 368      
    l2i_tlb_refill:u   | 45        | 47        | 110      
    l1d_cache:u        | 15549810  | 15531130  | 15512221 
    l1d_cache_refill:u | 6919552   | 6921536   | 6944636  
    l1d_tlb:u          | 26756298  | 26911459  | 26592703 
    l1d_tlb_refill:u   | 6971048   | 7009306   | 6968807  
    l2d_cache:u        | 30253240  | 30094661  | 30195714 
    l2d_cache_refill:u | 14209056  | 14257155  | 14047224 
    l2d_tlb:u          | 6980607   | 7024865   | 6978696  
    l2d_tlb_refill:u   | 38363     | 37403     | 1340     
    ll_cache:u         | 14204456  | 14252725  | 14044312 
    ll_cache_miss:u    | 160462    | 253097    | 170176   

== combo_024_s3 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p512_np2_l2_sp33
    s1 | fetch_b64_d1_bp0_s16_r100_lin_p1_np4_l4 
    s2 | hot_b64_bp3_r100_lstr_p128_np2_l2_sl9   
single_counts:
    metric             | s0        | s1       | s2      
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 100051044 | 28481536 | 39515577
    instructions:u     | 13590994  | 20150988 | 11920988
    br_retired:u       | 1031401   | 1991403  | 2021403 
    br_mis_pred:u      | 130686    | 591051   | 457     
    l1i_cache:u        | 3544057   | 8683221  | 1570023 
    l1i_cache_refill:u | 867       | 801      | 703     
    l1i_tlb:u          | 3544057   | 8683221  | 1570023 
    l1i_tlb_refill:u   | 44        | 44       | 52      
    l2i_cache:u        | 867       | 802      | 701     
    l2i_cache_refill:u | 657       | 613      | 606     
    l2i_tlb:u          | 79        | 80       | 93      
    l2i_tlb_refill:u   | 23        | 12       | 44      
    l1d_cache:u        | 2176752   | 5925605  | 1415958 
    l1d_cache_refill:u | 1263661   | 149      | 1222599 
    l1d_tlb:u          | 3579845   | 7689178  | 2799980 
    l1d_tlb_refill:u   | 1306397   | 64       | 1302356 
    l2d_cache:u        | 5614502   | 1512     | 3622064 
    l2d_cache_refill:u | 2736814   | 1026     | 1057260 
    l2d_tlb:u          | 1306433   | 93       | 1302544 
    l2d_tlb_refill:u   | 567       | 26       | 160     
    ll_cache:u         | 2735989   | 358      | 1056691 
    ll_cache_miss:u    | 118842    | 85       | 270     
combined_orders:
    id        | modules                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p512_np2_l2_sp33+fetch_b64_d1_bp0_s16_r100_lin_p1_np4_l4+hot_b64_bp3_r100_lstr_p128_np2_l2_sl9
    shuffle   | fetch_b64_d1_bp0_s16_r100_lin_p1_np4_l4+hot_b64_bp3_r100_lstr_p128_np2_l2_sl9+cold_b64_d4_bitrev_pstr_p512_np2_l2_sp33
    sum       | cold_b64_d4_bitrev_pstr_p512_np2_l2_sp33+fetch_b64_d1_bp0_s16_r100_lin_p1_np4_l4+hot_b64_bp3_r100_lstr_p128_np2_l2_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 148258913 | 157064407 | 168048157
    instructions:u     | 45641597  | 45641597  | 45662970 
    br_retired:u       | 5041804   | 5041804   | 5044207  
    br_mis_pred:u      | 721531    | 721512    | 722194   
    l1i_cache:u        | 13760091  | 13752230  | 13797301 
    l1i_cache_refill:u | 1373      | 1381      | 2371     
    l1i_tlb:u          | 13760091  | 13752230  | 13797301 
    l1i_tlb_refill:u   | 48        | 48        | 140      
    l2i_cache:u        | 1372      | 1380      | 2370     
    l2i_cache_refill:u | 838       | 863       | 1876     
    l2i_tlb:u          | 179       | 83        | 252      
    l2i_tlb_refill:u   | 32        | 35        | 79       
    l1d_cache:u        | 9509794   | 9509727   | 9518315  
    l1d_cache_refill:u | 2453060   | 2474406   | 2486409  
    l1d_tlb:u          | 14035879  | 14042509  | 14069003 
    l1d_tlb_refill:u   | 2604554   | 2605104   | 2608817  
    l2d_cache:u        | 9819516   | 9413658   | 9238078  
    l2d_cache_refill:u | 3916721   | 3818605   | 3795100  
    l2d_tlb:u          | 2604937   | 2605441   | 2609070  
    l2d_tlb_refill:u   | 242       | 170       | 753      
    ll_cache:u         | 3915647   | 3817639   | 3793038  
    ll_cache_miss:u    | 31375     | 8279      | 119197   

== combo_025_s3 ==
single_modules:
    id | module                                      
    ---+---------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p512_np1_l4_sp33   
    s1 | fetch_b128_d1_bp0_s16_r100_lshuf_p512_np4_l1
    s2 | itlb_f64_l1_r100_pstr_p512_np4_l2_sp17      
single_counts:
    metric             | s0        | s1       | s2      
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 300785872 | 93361149 | 94007497
    instructions:u     | 29431089  | 36150997 | 11931001
    br_retired:u       | 1991412   | 3911404  | 731403  
    br_mis_pred:u      | 290712    | 1231163  | 456     
    l1i_cache:u        | 7463501   | 18262095 | 1583380 
    l1i_cache_refill:u | 1608      | 1071     | 1466251 
    l1i_tlb:u          | 7463501   | 18262095 | 1583380 
    l1i_tlb_refill:u   | 59        | 48       | 660083  
    l2i_cache:u        | 1607      | 1069     | 1466250 
    l2i_cache_refill:u | 875       | 765      | 99771   
    l2i_tlb:u          | 111       | 85       | 660148  
    l2i_tlb_refill:u   | 52        | 24       | 53      
    l1d_cache:u        | 6817967   | 7887387  | 1415694 
    l1d_cache_refill:u | 5035783   | 887511   | 1282799 
    l1d_tlb:u          | 12063442  | 12102261 | 2812332 
    l1d_tlb_refill:u   | 5143158   | 350067   | 1306189 
    l2d_cache:u        | 22131906  | 5923909  | 5985720 
    l2d_cache_refill:u | 10728233  | 2488655  | 2637301 
    l2d_tlb:u          | 5143208   | 358199   | 1306223 
    l2d_tlb_refill:u   | 543       | 77       | 1124    
    ll_cache:u         | 10727206  | 2487715  | 2565584 
    ll_cache_miss:u    | 9214      | 12135    | 773     
combined_orders:
    id        | modules                                                                                                                      
    ----------+------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p512_np1_l4_sp33+fetch_b128_d1_bp0_s16_r100_lshuf_p512_np4_l1+itlb_f64_l1_r100_pstr_p512_np4_l2_sp17
    shuffle   | cold_b128_d4_bitrev_pstr_p512_np1_l4_sp33+itlb_f64_l1_r100_pstr_p512_np4_l2_sp17+fetch_b128_d1_bp0_s16_r100_lshuf_p512_np4_l1
    sum       | cold_b128_d4_bitrev_pstr_p512_np1_l4_sp33+fetch_b128_d1_bp0_s16_r100_lshuf_p512_np4_l1+itlb_f64_l1_r100_pstr_p512_np4_l2_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 524420853 | 542191493 | 488154518
    instructions:u     | 77491542  | 77491548  | 77513087 
    br_retired:u       | 6631792   | 6631790   | 6634219  
    br_mis_pred:u      | 1524355   | 1524775   | 1522331  
    l1i_cache:u        | 26150847  | 26154592  | 27308976 
    l1i_cache_refill:u | 1086456   | 1027005   | 1468930  
    l1i_tlb:u          | 26150847  | 26154592  | 27308976 
    l1i_tlb_refill:u   | 660968    | 660984    | 660190   
    l2i_cache:u        | 1086452   | 1027004   | 1468926  
    l2i_cache_refill:u | 94942     | 77864     | 101411   
    l2i_tlb:u          | 661401    | 661224    | 660344   
    l2i_tlb_refill:u   | 8837      | 8834      | 129      
    l1d_cache:u        | 16160090  | 16237355  | 16121048 
    l1d_cache_refill:u | 7498821   | 7496145   | 7206093  
    l1d_tlb:u          | 27056605  | 27372219  | 26978035 
    l1d_tlb_refill:u   | 6799669   | 6815108   | 6799414  
    l2d_cache:u        | 34707820  | 34692342  | 34041535 
    l2d_cache_refill:u | 16002635  | 15995527  | 15854189 
    l2d_tlb:u          | 6806859   | 6827620   | 6807630  
    l2d_tlb_refill:u   | 135760    | 136373    | 1744     
    ll_cache:u         | 15906324  | 15918133  | 15780505 
    ll_cache_miss:u    | 81025     | 98074     | 22122    

== combo_026_s3 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p512_np1_l4_sl3       
    s1 | fetch_b64_d1_bp0_s16_r100_lstr_p512_np2_l4_sl9
    s2 | itlb_f64_l1_r100_rand_p512_np2_l4             
single_counts:
    metric             | s0        | s1        | s2       
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 127168406 | 175141697 | 217637519
    instructions:u     | 14870988  | 20150997  | 13211004 
    br_retired:u       | 1031403   | 1991404   | 731403   
    br_mis_pred:u      | 130707    | 593743    | 502      
    l1i_cache:u        | 3701382   | 9407962   | 1845146  
    l1i_cache_refill:u | 798       | 791       | 1188495  
    l1i_tlb:u          | 3701382   | 9407962   | 1845146  
    l1i_tlb_refill:u   | 51        | 42        | 670061   
    l2i_cache:u        | 797       | 791       | 1188494  
    l2i_cache_refill:u | 606       | 635       | 569522   
    l2i_tlb:u          | 97        | 87        | 670136   
    l2i_tlb_refill:u   | 43        | 21        | 169      
    l1d_cache:u        | 3456882   | 5949067   | 2695726  
    l1d_cache_refill:u | 2517823   | 2530462   | 2559664  
    l1d_tlb:u          | 6140629   | 10474113  | 5242344  
    l1d_tlb_refill:u   | 2584706   | 2590058   | 2482298  
    l2d_cache:u        | 11132688  | 11244702  | 11217563 
    l2d_cache_refill:u | 5438130   | 5457089   | 5696151  
    l2d_tlb:u          | 2584743   | 2594546   | 2482331  
    l2d_tlb_refill:u   | 267       | 265       | 105      
    ll_cache:u         | 5437347   | 5456215   | 5125906  
    ll_cache_miss:u    | 11937     | 184540    | 732      
combined_orders:
    id        | modules                                                                                                                 
    ----------+-------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p512_np1_l4_sl3+fetch_b64_d1_bp0_s16_r100_lstr_p512_np2_l4_sl9+itlb_f64_l1_r100_rand_p512_np2_l4
    shuffle   | cold_b64_d4_bitrev_lstr_p512_np1_l4_sl3+itlb_f64_l1_r100_rand_p512_np2_l4+fetch_b64_d1_bp0_s16_r100_lstr_p512_np2_l4_sl9
    sum       | cold_b64_d4_bitrev_lstr_p512_np1_l4_sl3+fetch_b64_d1_bp0_s16_r100_lstr_p512_np2_l4_sl9+itlb_f64_l1_r100_rand_p512_np2_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 678840720 | 707662179 | 519947622
    instructions:u     | 48211548  | 48211542  | 48232989 
    br_retired:u       | 3751790   | 3751792   | 3754210  
    br_mis_pred:u      | 723697    | 732728    | 724952   
    l1i_cache:u        | 14265685  | 14359639  | 14954490 
    l1i_cache_refill:u | 882409    | 889960    | 1190084  
    l1i_tlb:u          | 14265685  | 14359639  | 14954490 
    l1i_tlb_refill:u   | 660558    | 660548    | 670154   
    l2i_cache:u        | 882407    | 889960    | 1190082  
    l2i_cache_refill:u | 518630    | 594235    | 570763   
    l2i_tlb:u          | 660811    | 660695    | 670320   
    l2i_tlb_refill:u   | 8641      | 8643      | 233      
    l1d_cache:u        | 12127987  | 12146409  | 12101675 
    l1d_cache_refill:u | 7594717   | 7607934   | 7607949  
    l1d_tlb:u          | 22047778  | 22109510  | 21857086 
    l1d_tlb_refill:u   | 7662191   | 7671000   | 7657062  
    l2d_cache:u        | 33920352  | 33865605  | 33594953 
    l2d_cache_refill:u | 16496704  | 16667036  | 16591370 
    l2d_tlb:u          | 7663054   | 7678240   | 7661620  
    l2d_tlb_refill:u   | 135871    | 136045    | 637      
    ll_cache:u         | 15969405  | 16083614  | 16019468 
    ll_cache_miss:u    | 90350     | 144322    | 197209   

== combo_027_s3 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p128_np2_l1           
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l4_sp33
    s2 | hot_b128_bp3_r100_rand_p512_np1_l1              
single_counts:
    metric             | s0       | s1        | s2      
    -------------------+----------+-----------+---------
    cpu-cycles:u       | 42017976 | 216680331 | 92788955
    instructions:u     | 25590988 | 39991007  | 22160988
    br_retired:u       | 1991403  | 3911406   | 3941403 
    br_mis_pred:u      | 290666   | 1252863   | 430     
    l1i_cache:u        | 6989580  | 18859987  | 2864279 
    l1i_cache_refill:u | 1073     | 1597      | 900     
    l1i_tlb:u          | 6989580  | 18859987  | 2864279 
    l1i_tlb_refill:u   | 54       | 57        | 40      
    l2i_cache:u        | 1072     | 1597      | 900     
    l2i_cache_refill:u | 794      | 928       | 603     
    l2i_tlb:u          | 106      | 102       | 154     
    l2i_tlb_refill:u   | 46       | 19        | 26      
    l1d_cache:u        | 2975874  | 11866090  | 1416901 
    l1d_cache_refill:u | 1113359  | 4837905   | 1280056 
    l1d_tlb:u          | 3817541  | 21063618  | 2799509 
    l1d_tlb_refill:u   | 670069   | 5160094   | 1303823 
    l2d_cache:u        | 3714498  | 15189724  | 5057429 
    l2d_cache_refill:u | 854908   | 3768539   | 2563238 
    l2d_tlb:u          | 671986   | 5160130   | 1304199 
    l2d_tlb_refill:u   | 29       | 18        | 639     
    ll_cache:u         | 854154   | 3767741   | 2562437 
    ll_cache_miss:u    | 147      | 12898     | 275     
combined_orders:
    id        | modules                                                                                                                  
    ----------+--------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p128_np2_l1+fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l4_sp33+hot_b128_bp3_r100_rand_p512_np1_l1
    shuffle   | hot_b128_bp3_r100_rand_p512_np1_l1+fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l4_sp33+cold_b128_d4_bitrev_lshuf_p128_np2_l1
    sum       | cold_b128_d4_bitrev_lshuf_p128_np2_l1+fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l4_sp33+hot_b128_bp3_r100_rand_p512_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 300764557 | 310860450 | 351487262
    instructions:u     | 87721698  | 87721698  | 87742983 
    br_retired:u       | 9841813   | 9841813   | 9844212  
    br_mis_pred:u      | 1529116   | 1543150   | 1543959  
    l1i_cache:u        | 27472961  | 27559039  | 28713846 
    l1i_cache_refill:u | 4055      | 4137      | 3570     
    l1i_tlb:u          | 27472961  | 27559039  | 28713846 
    l1i_tlb_refill:u   | 65        | 52        | 151      
    l2i_cache:u        | 4055      | 4136      | 3569     
    l2i_cache_refill:u | 1658      | 1616      | 2325     
    l2i_tlb:u          | 203       | 100       | 362      
    l2i_tlb_refill:u   | 59        | 30        | 91       
    l1d_cache:u        | 16181520  | 16315267  | 16258865 
    l1d_cache_refill:u | 7208746   | 7288968   | 7231320  
    l1d_tlb:u          | 27474917  | 27690934  | 27680668 
    l1d_tlb_refill:u   | 7123967   | 7129836   | 7133986  
    l2d_cache:u        | 24063048  | 24778675  | 23961651 
    l2d_cache_refill:u | 7139417   | 8088952   | 7186685  
    l2d_tlb:u          | 7144309   | 7130619   | 7136315  
    l2d_tlb_refill:u   | 1268      | 372       | 686      
    ll_cache:u         | 7137158   | 8086931   | 7184332  
    ll_cache_miss:u    | 3597      | 4681      | 13320    

== combo_028_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l4_sp3
    s1 | hot_b64_bp3_r100_pstr_p512_np4_l2_sp17         
    s2 | itlb_f64_l1_r100_lstr_p128_np4_l4_sl3          
single_counts:
    metric             | s0        | s1       | s2       
    -------------------+-----------+----------+----------
    cpu-cycles:u       | 369394394 | 68920164 | 102585950
    instructions:u     | 39990951  | 11920988 | 13210988 
    br_retired:u       | 3911393   | 2021403  | 731403   
    br_mis_pred:u      | 1231536   | 429      | 479      
    l1i_cache:u        | 18721773  | 1572862  | 1781460  
    l1i_cache_refill:u | 1858      | 652      | 1145605  
    l1i_tlb:u          | 18721773  | 1572862  | 1781460  
    l1i_tlb_refill:u   | 65        | 39       | 670058   
    l2i_cache:u        | 1856      | 652      | 1145603  
    l2i_cache_refill:u | 1043      | 531      | 204369   
    l2i_tlb:u          | 125       | 75       | 670122   
    l2i_tlb_refill:u   | 49        | 18       | 112      
    l1d_cache:u        | 11752376  | 1416682  | 2695630  
    l1d_cache_refill:u | 5044762   | 1280075  | 1993864  
    l1d_tlb:u          | 20868866  | 2805550  | 5051518  
    l1d_tlb_refill:u   | 5163873   | 1305089  | 1940065  
    l2d_cache:u        | 22782369  | 5081056  | 8185929  
    l2d_cache_refill:u | 10956142  | 2563734  | 2408303  
    l2d_tlb:u          | 5175206   | 1305421  | 1940094  
    l2d_tlb_refill:u   | 81        | 563      | 171      
    ll_cache:u         | 10954920  | 2562999  | 2186550  
    ll_cache_miss:u    | 92952     | 444      | 233      
combined_orders:
    id        | modules                                                                                                                     
    ----------+-----------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l4_sp3+hot_b64_bp3_r100_pstr_p512_np4_l2_sp17+itlb_f64_l1_r100_lstr_p128_np4_l4_sl3
    shuffle   | hot_b64_bp3_r100_pstr_p512_np4_l2_sp17+itlb_f64_l1_r100_lstr_p128_np4_l4_sl3+fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l4_sp3
    sum       | fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l4_sp3+hot_b64_bp3_r100_pstr_p512_np4_l2_sp17+itlb_f64_l1_r100_lstr_p128_np4_l4_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 648421927 | 731998223 | 540900508
    instructions:u     | 65101551  | 65101557  | 65122927 
    br_retired:u       | 6661793   | 6661791   | 6664199  
    br_mis_pred:u      | 1239243   | 1232386   | 1232444  
    l1i_cache:u        | 20939905  | 20845773  | 22076095 
    l1i_cache_refill:u | 1035574   | 1098950   | 1148115  
    l1i_tlb:u          | 20939905  | 20845773  | 22076095 
    l1i_tlb_refill:u   | 660654    | 660658    | 670162   
    l2i_cache:u        | 1035576   | 1098949   | 1148111  
    l2i_cache_refill:u | 212498    | 155292    | 205943   
    l2i_tlb:u          | 660824    | 660806    | 670322   
    l2i_tlb_refill:u   | 5690      | 4302      | 179      
    l1d_cache:u        | 15911235  | 15899251  | 15864688 
    l1d_cache_refill:u | 8676261   | 8632176   | 8318701  
    l1d_tlb:u          | 28664603  | 28582794  | 28725934 
    l1d_tlb_refill:u   | 8404566   | 8411516   | 8409027  
    l2d_cache:u        | 37361813  | 36916227  | 36049354 
    l2d_cache_refill:u | 17031775  | 16498702  | 15928179 
    l2d_tlb:u          | 8416980   | 8420073   | 8420721  
    l2d_tlb_refill:u   | 49117     | 48432     | 815      
    ll_cache:u         | 16686509  | 16302856  | 15704469 
    ll_cache_miss:u    | 99132     | 168695    | 93629    

== combo_029_s3 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b64_d4_bitrev_lshuf_p512_np1_l1            
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l2_sp33
    s2 | hot_b64_bp3_r100_lstr_p1_np2_l2_sl5             
single_counts:
    metric             | s0       | s1        | s2      
    -------------------+----------+-----------+---------
    cpu-cycles:u       | 37108402 | 111193726 | 7803353 
    instructions:u     | 12950988 | 37430997  | 11921040
    br_retired:u       | 1031403  | 3911404   | 2021409 
    br_mis_pred:u      | 130679   | 1239929   | 369     
    l1i_cache:u        | 3478205  | 18344408  | 1575526 
    l1i_cache_refill:u | 801      | 1081      | 622     
    l1i_tlb:u          | 3478205  | 18344408  | 1575526 
    l1i_tlb_refill:u   | 52       | 47        | 41      
    l2i_cache:u        | 800      | 1080      | 622     
    l2i_cache_refill:u | 640      | 770       | 535     
    l2i_tlb:u          | 100      | 85        | 81      
    l2i_tlb_refill:u   | 45       | 18        | 15      
    l1d_cache:u        | 1538139  | 9130740   | 1415213 
    l1d_cache_refill:u | 649133   | 2441616   | 150     
    l1d_tlb:u          | 2404560  | 15533566  | 1417181 
    l1d_tlb_refill:u   | 680071   | 2602590   | 64      
    l2d_cache:u        | 2548543  | 7714699   | 1118    
    l2d_cache_refill:u | 1285145  | 2067765   | 748     
    l2d_tlb:u          | 680174   | 2609658   | 91      
    l2d_tlb_refill:u   | 569      | 16        | 4       
    ll_cache:u         | 1284390  | 2067001   | 226     
    ll_cache_miss:u    | 88       | 796       | 13      
combined_orders:
    id        | modules                                                                                                                  
    ----------+--------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lshuf_p512_np1_l1+fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l2_sp33+hot_b64_bp3_r100_lstr_p1_np2_l2_sl5
    shuffle   | fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l2_sp33+hot_b64_bp3_r100_lstr_p1_np2_l2_sl5+cold_b64_d4_bitrev_lshuf_p512_np1_l1
    sum       | cold_b64_d4_bitrev_lshuf_p512_np1_l1+fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l2_sp33+hot_b64_bp3_r100_lstr_p1_np2_l2_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 189435554 | 206966975 | 156105481
    instructions:u     | 62281594  | 62281588  | 62303025 
    br_retired:u       | 6961801   | 6961803   | 6964216  
    br_mis_pred:u      | 1367581   | 1365052   | 1370977  
    l1i_cache:u        | 22159088  | 22165677  | 23398139 
    l1i_cache_refill:u | 2415      | 2468      | 2504     
    l1i_tlb:u          | 22159088  | 22165677  | 23398139 
    l1i_tlb_refill:u   | 51        | 60        | 140      
    l2i_cache:u        | 2415      | 2468      | 2502     
    l2i_cache_refill:u | 1086      | 1278      | 1945     
    l2i_tlb:u          | 188       | 119       | 266      
    l2i_tlb_refill:u   | 30        | 44        | 78       
    l1d_cache:u        | 12182803  | 12116464  | 12084092 
    l1d_cache_refill:u | 3014569   | 3090146   | 3090899  
    l1d_tlb:u          | 19568635  | 19387504  | 19355307 
    l1d_tlb_refill:u   | 3286591   | 3279834   | 3282725  
    l2d_cache:u        | 10596336  | 11185954  | 10264360 
    l2d_cache_refill:u | 3314158   | 3832563   | 3353658  
    l2d_tlb:u          | 3292789   | 3295639   | 3289923  
    l2d_tlb_refill:u   | 854       | 255       | 589      
    ll_cache:u         | 3312767   | 3831232   | 3351617  
    ll_cache_miss:u    | 59705     | 57495     | 897      

== combo_030_s3 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p512_np4_l1_sp3         
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l2_sp33
    s2 | hot_b128_bp3_r100_pstr_p512_np2_l2_sp17         
single_counts:
    metric             | s0       | s1        | s2       
    -------------------+----------+-----------+----------
    cpu-cycles:u       | 57034765 | 156912611 | 160385034
    instructions:u     | 12950988 | 37430997  | 23440988 
    br_retired:u       | 1031403  | 3911404   | 3941403  
    br_mis_pred:u      | 130731   | 1231883   | 433      
    l1i_cache:u        | 3464564  | 18381357  | 3020843  
    l1i_cache_refill:u | 801      | 1371      | 1065     
    l1i_tlb:u          | 3464564  | 18381357  | 3020843  
    l1i_tlb_refill:u   | 56       | 56        | 50       
    l2i_cache:u        | 800      | 1369      | 1065     
    l2i_cache_refill:u | 654      | 776       | 685      
    l2i_tlb:u          | 107      | 112       | 156      
    l2i_tlb_refill:u   | 46       | 18        | 25       
    l1d_cache:u        | 1536392  | 9159415   | 2697877  
    l1d_cache_refill:u | 639943   | 2427507   | 2560895  
    l1d_tlb:u          | 2302243  | 15606777  | 5359710  
    l1d_tlb_refill:u   | 664857   | 2601688   | 2583183  
    l2d_cache:u        | 2603881  | 8284150   | 10197428 
    l2d_cache_refill:u | 1283925  | 2395499   | 5129558  
    l2d_tlb:u          | 664893   | 2606740   | 2583699  
    l2d_tlb_refill:u   | 548      | 128       | 114      
    ll_cache:u         | 1283173  | 2394574   | 5128752  
    ll_cache_miss:u    | 1655     | 17161     | 6355     
combined_orders:
    id        | modules                                                                                                                         
    ----------+---------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p512_np4_l1_sp3+fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l2_sp33+hot_b128_bp3_r100_pstr_p512_np2_l2_sp17
    shuffle   | cold_b64_d4_bitrev_pstr_p512_np4_l1_sp3+hot_b128_bp3_r100_pstr_p512_np2_l2_sp17+fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l2_sp33
    sum       | cold_b64_d4_bitrev_pstr_p512_np4_l1_sp3+fetch_b128_d1_bp0_s16_r100_pstr_p128_np4_l2_sp33+hot_b128_bp3_r100_pstr_p512_np2_l2_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 456529398 | 391022172 | 374332410
    instructions:u     | 73801551  | 73801551  | 73822973 
    br_retired:u       | 8881793   | 8881793   | 8884210  
    br_mis_pred:u      | 1361830   | 1370384   | 1363047  
    l1i_cache:u        | 23574840  | 23713629  | 24866764 
    l1i_cache_refill:u | 4694      | 4267      | 3237     
    l1i_tlb:u          | 23574840  | 23713629  | 24866764 
    l1i_tlb_refill:u   | 51        | 64        | 162      
    l2i_cache:u        | 4694      | 4266      | 3234     
    l2i_cache_refill:u | 1883      | 1569      | 2115     
    l2i_tlb:u          | 173       | 101       | 375      
    l2i_tlb_refill:u   | 45        | 60        | 89       
    l1d_cache:u        | 13454149  | 13411951  | 13393684 
    l1d_cache_refill:u | 5615213   | 5610086   | 5628345  
    l1d_tlb:u          | 23450784  | 23337750  | 23268730 
    l1d_tlb_refill:u   | 5852059   | 5847862   | 5849728  
    l2d_cache:u        | 21418735  | 20880873  | 21085459 
    l2d_cache_refill:u | 8913943   | 8497255   | 8808982  
    l2d_tlb:u          | 5862411   | 5856559   | 5855332  
    l2d_tlb_refill:u   | 37231     | 35708     | 790      
    ll_cache:u         | 8909525   | 8493275   | 8806499  
    ll_cache_miss:u    | 123434    | 149117    | 25171    

== combo_031_s3 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl9     
    s1 | fetch_b64_d1_bp0_s16_r100_rand_p512_np2_l2
    s2 | hot_b64_bp3_r100_lstr_p128_np4_l1_sl5     
single_counts:
    metric             | s0       | s1        | s2      
    -------------------+----------+-----------+---------
    cpu-cycles:u       | 8750345  | 102977817 | 28515528
    instructions:u     | 12951049 | 18870997  | 11280988
    br_retired:u       | 1031410  | 1991404   | 2021403 
    br_mis_pred:u      | 130636   | 593651    | 457     
    l1i_cache:u        | 3492763  | 9258045   | 1488480 
    l1i_cache_refill:u | 694      | 739       | 615     
    l1i_tlb:u          | 3492763  | 9258045   | 1488480 
    l1i_tlb_refill:u   | 54       | 46        | 44      
    l2i_cache:u        | 694      | 738       | 615     
    l2i_cache_refill:u | 631      | 612       | 520     
    l2i_tlb:u          | 104      | 88        | 165     
    l2i_tlb_refill:u   | 40       | 27        | 13      
    l1d_cache:u        | 1535183  | 4691510   | 775845  
    l1d_cache_refill:u | 163      | 1270827   | 618143  
    l1d_tlb:u          | 1537189  | 8009570   | 1526304 
    l1d_tlb_refill:u   | 60       | 1290699   | 664538  
    l2d_cache:u        | 1362     | 5491619   | 1934639 
    l2d_cache_refill:u | 856      | 2648386   | 652966  
    l2d_tlb:u          | 78       | 1302063   | 664811  
    l2d_tlb_refill:u   | 31       | 646       | 6       
    ll_cache:u         | 260      | 2647624   | 652435  
    ll_cache_miss:u    | 22       | 72457     | 1108    
combined_orders:
    id        | modules                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl9+fetch_b64_d1_bp0_s16_r100_rand_p512_np2_l2+hot_b64_bp3_r100_lstr_p128_np4_l1_sl5
    shuffle   | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl9+hot_b64_bp3_r100_lstr_p128_np4_l1_sl5+fetch_b64_d1_bp0_s16_r100_rand_p512_np2_l2
    sum       | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl9+fetch_b64_d1_bp0_s16_r100_rand_p512_np2_l2+hot_b64_bp3_r100_lstr_p128_np4_l1_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 138335445 | 151535871 | 140243690
    instructions:u     | 43081588  | 43081594  | 43103034 
    br_retired:u       | 5041803   | 5041801   | 5044217  
    br_mis_pred:u      | 724219    | 723066    | 724744   
    l1i_cache:u        | 13566354  | 13569282  | 14239288 
    l1i_cache_refill:u | 1117      | 1199      | 2048     
    l1i_tlb:u          | 13566354  | 13569282  | 14239288 
    l1i_tlb_refill:u   | 52        | 55        | 144      
    l2i_cache:u        | 1117      | 1197      | 2047     
    l2i_cache_refill:u | 855       | 936       | 1763     
    l2i_tlb:u          | 191       | 108       | 357      
    l2i_tlb_refill:u   | 37        | 52        | 80       
    l1d_cache:u        | 6996867   | 7020954   | 7002538  
    l1d_cache_refill:u | 1885396   | 1880640   | 1889133  
    l1d_tlb:u          | 11013362  | 11093591  | 11073063 
    l1d_tlb_refill:u   | 1950272   | 1950611   | 1955297  
    l2d_cache:u        | 7309653   | 7450777   | 7427620  
    l2d_cache_refill:u | 3196513   | 3272607   | 3302208  
    l2d_tlb:u          | 1953484   | 1964024   | 1966952  
    l2d_tlb_refill:u   | 216       | 686       | 683      
    ll_cache:u         | 3195476   | 3271561   | 3300319  
    ll_cache_miss:u    | 108934    | 57269     | 73587    

== combo_032_s3 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | cold_b64_d4_bitrev_rand_p128_np2_l1
    s1 | hot_b128_bp3_r100_rand_p128_np2_l2 
    s2 | itlb_f64_l1_r100_lstr_p1_np4_l2_sl3
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 28316380 | 94987964 | 24482243
    instructions:u     | 12950988 | 23440988 | 11931049
    br_retired:u       | 1031403  | 3941403  | 731410  
    br_mis_pred:u      | 130650   | 497      | 486     
    l1i_cache:u        | 3470137  | 3018964  | 1565914 
    l1i_cache_refill:u | 781      | 922      | 1825618 
    l1i_tlb:u          | 3470137  | 3018964  | 1565914 
    l1i_tlb_refill:u   | 46       | 55       | 660168  
    l2i_cache:u        | 780      | 920      | 1825617 
    l2i_cache_refill:u | 639      | 646      | 744     
    l2i_tlb:u          | 83       | 162      | 660240  
    l2i_tlb_refill:u   | 14       | 16       | 111     
    l1d_cache:u        | 1548497  | 2696483  | 1415354 
    l1d_cache_refill:u | 625901   | 2435108  | 175     
    l1d_tlb:u          | 2227060  | 5019011  | 1417298 
    l1d_tlb_refill:u   | 550434   | 2260089  | 64      
    l2d_cache:u        | 1896094  | 6893702  | 1164237 
    l2d_cache_refill:u | 587309   | 1765592  | 1233    
    l2d_tlb:u          | 553704   | 2260403  | 86      
    l2d_tlb_refill:u   | 15       | 156      | 34      
    ll_cache:u         | 586706   | 1764848  | 350     
    ll_cache_miss:u    | 453      | 901      | 126     
combined_orders:
    id        | modules                                                                                                   
    ----------+-----------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_rand_p128_np2_l1+hot_b128_bp3_r100_rand_p128_np2_l2+itlb_f64_l1_r100_lstr_p1_np4_l2_sl3
    shuffle   | hot_b128_bp3_r100_rand_p128_np2_l2+itlb_f64_l1_r100_lstr_p1_np4_l2_sl3+cold_b64_d4_bitrev_rand_p128_np2_l1
    sum       | cold_b64_d4_bitrev_rand_p128_np2_l1+hot_b128_bp3_r100_rand_p128_np2_l2+itlb_f64_l1_r100_lstr_p1_np4_l2_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 134163072 | 125276355 | 147786587
    instructions:u     | 48301597  | 48301597  | 48323025 
    br_retired:u       | 5701804   | 5701804   | 5704216  
    br_mis_pred:u      | 130884    | 130907    | 131633   
    l1i_cache:u        | 8106864   | 8072833   | 8055015  
    l1i_cache_refill:u | 1204002   | 1241325   | 1827321  
    l1i_tlb:u          | 8106864   | 8072833   | 8055015  
    l1i_tlb_refill:u   | 660550    | 660556    | 660269   
    l2i_cache:u        | 1204000   | 1241325   | 1827317  
    l2i_cache_refill:u | 15737     | 16610     | 2029     
    l2i_tlb:u          | 660592    | 660595    | 660485   
    l2i_tlb_refill:u   | 29        | 113       | 141      
    l1d_cache:u        | 5638571   | 5638202   | 5660334  
    l1d_cache_refill:u | 3035110   | 3032355   | 3061184  
    l1d_tlb:u          | 8571785   | 8566880   | 8663369  
    l1d_tlb_refill:u   | 2798099   | 2798098   | 2810587  
    l2d_cache:u        | 10736053  | 10503860  | 9954033  
    l2d_cache_refill:u | 2779880   | 2745179   | 2354134  
    l2d_tlb:u          | 2802168   | 2799771   | 2814193  
    l2d_tlb_refill:u   | 290       | 31        | 205      
    ll_cache:u         | 2763735   | 2728361   | 2351904  
    ll_cache_miss:u    | 1048      | 425       | 1480     

== combo_033_s3 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lstr_p1_np2_l4_sl5
    s1 | hot_b64_bp3_r100_lstr_p512_np4_l1_sl3        
    s2 | itlb_f64_l1_r100_lin_p512_np1_l1             
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 58151485 | 44116857 | 53997734
    instructions:u     | 39990997 | 11280988 | 11290988
    br_retired:u       | 3911404  | 2021403  | 731403  
    br_mis_pred:u      | 1231060  | 421      | 474     
    l1i_cache:u        | 17272409 | 1490584  | 1517650 
    l1i_cache_refill:u | 877      | 666      | 1073429 
    l1i_tlb:u          | 17272409 | 1490584  | 1517650 
    l1i_tlb_refill:u   | 48       | 50       | 660065  
    l2i_cache:u        | 877      | 666      | 1073427 
    l2i_cache_refill:u | 689      | 565      | 142102  
    l2i_tlb:u          | 80       | 156      | 660126  
    l2i_tlb_refill:u   | 13       | 46       | 114     
    l1d_cache:u        | 11685208 | 775970   | 775375  
    l1d_cache_refill:u | 160      | 640227   | 639891  
    l1d_tlb:u          | 15348991 | 1372488  | 1522289 
    l1d_tlb_refill:u   | 70       | 510065   | 664855  
    l2d_cache:u        | 1685     | 2530020  | 3901589 
    l2d_cache_refill:u | 993      | 1282400  | 1472828 
    l2d_tlb:u          | 91       | 510272   | 664886  
    l2d_tlb_refill:u   | 5        | 659      | 564     
    ll_cache:u         | 287      | 1281715  | 1296207 
    ll_cache_miss:u    | 15       | 262      | 3785    
combined_orders:
    id        | modules                                                                                                             
    ----------+---------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lstr_p1_np2_l4_sl5+hot_b64_bp3_r100_lstr_p512_np4_l1_sl3+itlb_f64_l1_r100_lin_p512_np1_l1
    shuffle   | itlb_f64_l1_r100_lin_p512_np1_l1+fetch_b128_d1_bp0_s16_r100_lstr_p1_np2_l4_sl5+hot_b64_bp3_r100_lstr_p512_np4_l1_sl3
    sum       | fetch_b128_d1_bp0_s16_r100_lstr_p1_np2_l4_sl5+hot_b64_bp3_r100_lstr_p512_np4_l1_sl3+itlb_f64_l1_r100_lin_p512_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 164867206 | 154560139 | 156266076
    instructions:u     | 62541588  | 62541588  | 62562973 
    br_retired:u       | 6661803   | 6661803   | 6664210  
    br_mis_pred:u      | 1233877   | 1231414   | 1231955  
    l1i_cache:u        | 20284117  | 20232924  | 20280643 
    l1i_cache_refill:u | 1116781   | 1055381   | 1074972  
    l1i_tlb:u          | 20284117  | 20232924  | 20280643 
    l1i_tlb_refill:u   | 660653    | 660647    | 660163   
    l2i_cache:u        | 1116780   | 1055379   | 1074970  
    l2i_cache_refill:u | 198285    | 87608     | 143356   
    l2i_tlb:u          | 660805    | 660834    | 660362   
    l2i_tlb_refill:u   | 5211      | 4996      | 173      
    l1d_cache:u        | 13229074  | 13227355  | 13236553 
    l1d_cache_refill:u | 1276442   | 1276185   | 1280278  
    l1d_tlb:u          | 18360101  | 18254859  | 18243768 
    l1d_tlb_refill:u   | 1190372   | 1165202   | 1174990  
    l2d_cache:u        | 6434902   | 6540638   | 6433294  
    l2d_cache_refill:u | 2859627   | 2722626   | 2756221  
    l2d_tlb:u          | 1190606   | 1165420   | 1175249  
    l2d_tlb_refill:u   | 22928     | 21870     | 1228     
    ll_cache:u         | 2639912   | 2647337   | 2578209  
    ll_cache_miss:u    | 41429     | 9742      | 4062     

== combo_034_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np1_l1_sl3          
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p512_np2_l4_sl3
    s2 | hot_b128_bp3_r100_pstr_p512_np1_l1_sp17        
    s3 | itlb_f64_l1_r100_pstr_p128_np4_l2_sp33         
single_counts:
    metric             | s0       | s1        | s2        | s3      
    -------------------+----------+-----------+-----------+---------
    cpu-cycles:u       | 8747621  | 299878450 | 104286642 | 59420707
    instructions:u     | 12951049 | 39991098  | 22160994  | 11930988
    br_retired:u       | 1031410  | 3911413   | 3941401   | 731403  
    br_mis_pred:u      | 130623   | 1246529   | 439       | 468     
    l1i_cache:u        | 3480699  | 18876633  | 2855091   | 1563865 
    l1i_cache_refill:u | 769      | 1671      | 891       | 1607199 
    l1i_tlb:u          | 3480699  | 18876633  | 2855091   | 1563865 
    l1i_tlb_refill:u   | 54       | 55        | 40        | 660070  
    l2i_cache:u        | 769      | 1670      | 892       | 1607196 
    l2i_cache_refill:u | 625      | 908       | 619       | 22006   
    l2i_tlb:u          | 109      | 100       | 149       | 660127  
    l2i_tlb_refill:u   | 42       | 28        | 18        | 28      
    l1d_cache:u        | 1535291  | 11760488  | 1416093   | 1415421 
    l1d_cache_refill:u | 149      | 5061620   | 1294004   | 1223931 
    l1d_tlb:u          | 1537270  | 20879054  | 2806910   | 2775270 
    l1d_tlb_refill:u   | 58       | 5162617   | 1305736   | 1301922 
    l2d_cache:u        | 1281     | 22817831  | 5102286   | 5768874 
    l2d_cache_refill:u | 861      | 10816876  | 2562500   | 1275635 
    l2d_tlb:u          | 73       | 5169958   | 1306000   | 1301945 
    l2d_tlb_refill:u   | 3        | 81        | 90        | 25      
    ll_cache:u         | 293      | 10815772  | 2561825   | 1254445 
    ll_cache_miss:u    | 27       | 67244     | 113       | 319     
combined_orders:
    id        | modules                                                                                                                                                             
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np1_l1_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p512_np2_l4_sl3+hot_b128_bp3_r100_pstr_p512_np1_l1_sp17+itlb_f64_l1_r100_pstr_p128_np4_l2_sp33
    shuffle   | hot_b128_bp3_r100_pstr_p512_np1_l1_sp17+fetch_b128_d1_bp0_s16_r100_lstr_p512_np2_l4_sl3+itlb_f64_l1_r100_pstr_p128_np4_l2_sp33+cold_b64_d4_bitrev_lstr_p1_np1_l1_sl3
    sum       | cold_b64_d4_bitrev_lstr_p1_np1_l1_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p512_np2_l4_sl3+hot_b128_bp3_r100_pstr_p512_np1_l1_sp17+itlb_f64_l1_r100_pstr_p128_np4_l2_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 700593429 | 640947998 | 472333420
    instructions:u     | 87001851  | 87001851  | 87034129 
    br_retired:u       | 9611993   | 9611993   | 9615627  
    br_mis_pred:u      | 1367988   | 1367250   | 1378059  
    l1i_cache:u        | 25722094  | 25556398  | 26776288 
    l1i_cache_refill:u | 939820    | 936353    | 1610530  
    l1i_tlb:u          | 25722094  | 25556398  | 26776288 
    l1i_tlb_refill:u   | 660992    | 660992    | 660219   
    l2i_cache:u        | 939821    | 936353    | 1610527  
    l2i_cache_refill:u | 41083     | 56916     | 24158    
    l2i_tlb:u          | 661138    | 661131    | 660485   
    l2i_tlb_refill:u   | 4537      | 4717      | 116      
    l1d_cache:u        | 16215900  | 16237095  | 16127293 
    l1d_cache_refill:u | 7551921   | 7553570   | 7579704  
    l1d_tlb:u          | 28220561  | 28452504  | 27998504 
    l1d_tlb_refill:u   | 7765906   | 7817531   | 7770333  
    l2d_cache:u        | 33053115  | 33209019  | 33690272 
    l2d_cache_refill:u | 14794809  | 14636601  | 14655872 
    l2d_tlb:u          | 7767325   | 7824127   | 7777976  
    l2d_tlb_refill:u   | 52788     | 51149     | 199      
    ll_cache:u         | 14749382  | 14569838  | 14632335 
    ll_cache_miss:u    | 267579    | 314882    | 67703    

== combo_035_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p128_np1_l1_sp33       
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p128_np1_l2_sl3
    s2 | hot_b64_bp3_r100_lstr_p512_np2_l4_sl5          
    s3 | itlb_f64_l1_r100_pstr_p128_np1_l1_sp17         
single_counts:
    metric             | s0       | s1        | s2        | s3      
    -------------------+----------+-----------+-----------+---------
    cpu-cycles:u       | 24671308 | 114767299 | 124290904 | 54316818
    instructions:u     | 12951040 | 37430997  | 13200988  | 11290988
    br_retired:u       | 1031409  | 3911404   | 2021403   | 731403  
    br_mis_pred:u      | 130625   | 1241110   | 456       | 499     
    l1i_cache:u        | 3453250  | 18330785  | 1733409   | 1512167 
    l1i_cache_refill:u | 676      | 930       | 844       | 1054852 
    l1i_tlb:u          | 3453250  | 18330785  | 1733409   | 1512167 
    l1i_tlb_refill:u   | 45       | 48        | 40        | 660113  
    l2i_cache:u        | 675      | 930       | 843       | 1054851 
    l2i_cache_refill:u | 588      | 710       | 584       | 115767  
    l2i_tlb:u          | 87       | 80        | 159       | 660221  
    l2i_tlb_refill:u   | 13       | 15        | 24        | 87      
    l1d_cache:u        | 1536020  | 9160436   | 2696760   | 775449  
    l1d_cache_refill:u | 616366   | 2411685   | 2573084   | 628247  
    l1d_tlb:u          | 2325903  | 15575731  | 5361803   | 1505011 
    l1d_tlb_refill:u   | 665074   | 2600079   | 2584422   | 663061  
    l2d_cache:u        | 1886936  | 7944494   | 10218430  | 3903655 
    l2d_cache_refill:u | 605516   | 2308040   | 5128638   | 1290989 
    l2d_tlb:u          | 675044   | 2619510   | 2584802   | 663084  
    l2d_tlb_refill:u   | 19       | 11        | 87        | 28      
    ll_cache:u         | 604913   | 2307259   | 5127955   | 1065896 
    ll_cache_miss:u    | 63       | 42        | 973       | 42      
combined_orders:
    id        | modules                                                                                                                                                              
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p128_np1_l1_sp33+fetch_b128_d1_bp0_s16_r100_lstr_p128_np1_l2_sl3+hot_b64_bp3_r100_lstr_p512_np2_l4_sl5+itlb_f64_l1_r100_pstr_p128_np1_l1_sp17
    shuffle   | cold_b64_d4_bitrev_pstr_p128_np1_l1_sp33+hot_b64_bp3_r100_lstr_p512_np2_l4_sl5+fetch_b128_d1_bp0_s16_r100_lstr_p128_np1_l2_sl3+itlb_f64_l1_r100_pstr_p128_np1_l1_sp17
    sum       | cold_b64_d4_bitrev_pstr_p128_np1_l1_sp33+fetch_b128_d1_bp0_s16_r100_lstr_p128_np1_l2_sl3+hot_b64_bp3_r100_lstr_p512_np2_l4_sl5+itlb_f64_l1_r100_pstr_p128_np1_l1_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 430614018 | 455945387 | 318046329
    instructions:u     | 74841842  | 74841842  | 74874013 
    br_retired:u       | 7691992   | 7691992   | 7695619  
    br_mis_pred:u      | 1362420   | 1364585   | 1372690  
    l1i_cache:u        | 23859089  | 23779282  | 25029611 
    l1i_cache_refill:u | 1039156   | 991962    | 1057302  
    l1i_tlb:u          | 23859089  | 23779282  | 25029611 
    l1i_tlb_refill:u   | 660853    | 660850    | 660246   
    l2i_cache:u        | 1039153   | 991961    | 1057299  
    l2i_cache_refill:u | 167518    | 377672    | 117649   
    l2i_tlb:u          | 661022    | 661008    | 660547   
    l2i_tlb_refill:u   | 5587      | 2004      | 139      
    l1d_cache:u        | 14142946  | 14157488  | 14168665 
    l1d_cache_refill:u | 6221890   | 6163635   | 6229382  
    l1d_tlb:u          | 24805907  | 24864128  | 24768448 
    l1d_tlb_refill:u   | 6517959   | 6512115   | 6512636  
    l2d_cache:u        | 24310771  | 24059956  | 23953515 
    l2d_cache_refill:u | 10110844  | 9813382   | 9333183  
    l2d_tlb:u          | 6539019   | 6523341   | 6542440  
    l2d_tlb_refill:u   | 15201     | 4709      | 145      
    ll_cache:u         | 9756299   | 9447542   | 9106023  
    ll_cache_miss:u    | 19399     | 126567    | 1120     

== combo_036_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p128_np2_l4          
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np1_l1_sp3
    s2 | hot_b64_bp3_r100_lshuf_p1_np1_l4               
    s3 | itlb_f64_l1_r100_lstr_p128_np2_l1_sl5          
single_counts:
    metric             | s0        | s1        | s2       | s3      
    -------------------+-----------+-----------+----------+---------
    cpu-cycles:u       | 118440297 | 115579710 | 12918829 | 41693569
    instructions:u     | 29430988  | 36150997  | 13201040 | 11290988
    br_retired:u       | 1991403   | 3911404   | 2021409  | 731403  
    br_mis_pred:u      | 290680    | 1230765   | 380      | 442     
    l1i_cache:u        | 7474760   | 18197677  | 1726068  | 1473524 
    l1i_cache_refill:u | 1085      | 972       | 618      | 1719534 
    l1i_tlb:u          | 7474760   | 18197677  | 1726068  | 1473524 
    l1i_tlb_refill:u   | 44        | 47        | 42       | 660076  
    l2i_cache:u        | 1086      | 972       | 617      | 1719532 
    l2i_cache_refill:u | 736       | 690       | 539      | 8441    
    l2i_tlb:u          | 88        | 177       | 75       | 660132  
    l2i_tlb_refill:u   | 16        | 26        | 13       | 21      
    l1d_cache:u        | 6816802   | 7893229   | 2695401  | 775338  
    l1d_cache_refill:u | 4303638   | 1274421   | 136      | 620690  
    l1d_tlb:u          | 9776346   | 13141995  | 2697457  | 1563334 
    l1d_tlb_refill:u   | 2580068   | 1321900   | 60       | 676472  
    l2d_cache:u        | 13932325  | 5554446   | 1277     | 2952583 
    l2d_cache_refill:u | 3238491   | 2738444   | 821      | 792798  
    l2d_tlb:u          | 2586055   | 1333961   | 146      | 676513  
    l2d_tlb_refill:u   | 15        | 168       | 3        | 22      
    ll_cache:u         | 3237669   | 2737614   | 266      | 782640  
    ll_cache_miss:u    | 11298     | 42179     | 21       | 115     
combined_orders:
    id        | modules                                                                                                                                                     
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p128_np2_l4+fetch_b128_d1_bp0_s16_r100_pstr_p512_np1_l1_sp3+hot_b64_bp3_r100_lshuf_p1_np1_l4+itlb_f64_l1_r100_lstr_p128_np2_l1_sl5
    shuffle   | cold_b128_d4_bitrev_lshuf_p128_np2_l4+itlb_f64_l1_r100_lstr_p128_np2_l1_sl5+hot_b64_bp3_r100_lshuf_p1_np1_l4+fetch_b128_d1_bp0_s16_r100_pstr_p512_np1_l1_sp3
    sum       | cold_b128_d4_bitrev_lshuf_p128_np2_l4+fetch_b128_d1_bp0_s16_r100_pstr_p512_np1_l1_sp3+hot_b64_bp3_r100_lshuf_p1_np1_l4+itlb_f64_l1_r100_lstr_p128_np2_l1_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 313804030 | 294164499 | 288632405
    instructions:u     | 90041998  | 90041998  | 90074013 
    br_retired:u       | 8652013   | 8652013   | 8655619  
    br_mis_pred:u      | 1525308   | 1522067   | 1522267  
    l1i_cache:u        | 27757654  | 27684728  | 28872029 
    l1i_cache_refill:u | 1003148   | 1010198   | 1722209  
    l1i_tlb:u          | 27757654  | 27684728  | 28872029 
    l1i_tlb_refill:u   | 661074    | 661069    | 660209   
    l2i_cache:u        | 1003148   | 1010196   | 1722207  
    l2i_cache_refill:u | 87441     | 66286     | 10406    
    l2i_tlb:u          | 661137    | 661189    | 660472   
    l2i_tlb_refill:u   | 765       | 1070      | 76       
    l1d_cache:u        | 18202494  | 18198816  | 18180770 
    l1d_cache_refill:u | 5939688   | 5855313   | 6198885  
    l1d_tlb:u          | 27133265  | 27063985  | 27179132 
    l1d_tlb_refill:u   | 4607880   | 4568278   | 4578500  
    l2d_cache:u        | 23798258  | 24688152  | 22440631 
    l2d_cache_refill:u | 7377658   | 7956429   | 6770554  
    l2d_tlb:u          | 4626004   | 4581076   | 4596675  
    l2d_tlb_refill:u   | 5182      | 2474      | 208      
    ll_cache:u         | 7241529   | 7886813   | 6758189  
    ll_cache_miss:u    | 33616     | 21475     | 53613    

== combo_037_s4 ==
single_modules:
    id | module                                   
    ---+------------------------------------------
    s0 | cold_b64_d4_bitrev_lshuf_p1_np2_l2       
    s1 | fetch_b64_d1_bp0_s16_r100_lin_p128_np2_l1
    s2 | hot_b64_bp3_r100_lshuf_p512_np2_l2       
    s3 | itlb_f64_l1_r100_pstr_p512_np2_l4_sp17   
single_counts:
    metric             | s0       | s1       | s2       | s3       
    -------------------+----------+----------+----------+----------
    cpu-cycles:u       | 11285894 | 38403233 | 84946845 | 206330273
    instructions:u     | 13591049 | 18230997 | 11920988 | 13210988 
    br_retired:u       | 1031410  | 1991404  | 2021403  | 731403   
    br_mis_pred:u      | 130494   | 591107   | 498      | 501      
    l1i_cache:u        | 3577075  | 9051917  | 1573036  | 1773893  
    l1i_cache_refill:u | 701      | 704      | 812      | 946038   
    l1i_tlb:u          | 3577075  | 9051917  | 1573036  | 1773893  
    l1i_tlb_refill:u   | 55       | 60       | 48       | 670054   
    l2i_cache:u        | 700      | 703      | 811      | 946035   
    l2i_cache_refill:u | 613      | 616      | 555      | 318418   
    l2i_tlb:u          | 91       | 101      | 104      | 670103   
    l2i_tlb_refill:u   | 15       | 17       | 31       | 84       
    l1d_cache:u        | 2175299  | 4017038  | 1416006  | 2695721  
    l1d_cache_refill:u | 156      | 607295   | 1111784  | 2559840  
    l1d_tlb:u          | 2177366  | 6253863  | 2174280  | 5381680  
    l1d_tlb_refill:u   | 61       | 340063   | 660065   | 2587671  
    l2d_cache:u        | 1262     | 2095335  | 5180698  | 11172263 
    l2d_cache_refill:u | 847      | 561148   | 2533237  | 5470390  
    l2d_tlb:u          | 83       | 340141   | 660123   | 2587709  
    l2d_tlb_refill:u   | 32       | 165      | 128      | 208      
    ll_cache:u         | 250      | 560510   | 2532489  | 5130280  
    ll_cache_miss:u    | 16       | 2730     | 3608     | 3148     
combined_orders:
    id        | modules                                                                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lshuf_p1_np2_l2+fetch_b64_d1_bp0_s16_r100_lin_p128_np2_l1+hot_b64_bp3_r100_lshuf_p512_np2_l2+itlb_f64_l1_r100_pstr_p512_np2_l4_sp17
    shuffle   | hot_b64_bp3_r100_lshuf_p512_np2_l2+itlb_f64_l1_r100_pstr_p512_np2_l4_sp17+fetch_b64_d1_bp0_s16_r100_lin_p128_np2_l1+cold_b64_d4_bitrev_lshuf_p1_np2_l2
    sum       | cold_b64_d4_bitrev_lshuf_p1_np2_l2+fetch_b64_d1_bp0_s16_r100_lin_p128_np2_l1+hot_b64_bp3_r100_lshuf_p512_np2_l2+itlb_f64_l1_r100_pstr_p512_np2_l4_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 408675404 | 415154021 | 340966245
    instructions:u     | 56921851  | 56921851  | 56954022 
    br_retired:u       | 5771993   | 5771993   | 5775620  
    br_mis_pred:u      | 730655    | 722610    | 722600   
    l1i_cache:u        | 15573289  | 15411266  | 15975921 
    l1i_cache_refill:u | 1108971   | 1172856   | 948255   
    l1i_tlb:u          | 15573289  | 15411266  | 15975921 
    l1i_tlb_refill:u   | 660660    | 660644    | 670217   
    l2i_cache:u        | 1108971   | 1172856   | 948249   
    l2i_cache_refill:u | 348675    | 367830    | 320202   
    l2i_tlb:u          | 660809    | 660786    | 670399   
    l2i_tlb_refill:u   | 7361      | 5842      | 147      
    l1d_cache:u        | 10334456  | 10351390  | 10304064 
    l1d_cache_refill:u | 4300224   | 4292402   | 4279075  
    l1d_tlb:u          | 16126082  | 16140251  | 15987189 
    l1d_tlb_refill:u   | 3587359   | 3592398   | 3587860  
    l2d_cache:u        | 19362262  | 19491219  | 18449558 
    l2d_cache_refill:u | 8927561   | 8993709   | 8565622  
    l2d_tlb:u          | 3587974   | 3604963   | 3588056  
    l2d_tlb_refill:u   | 49409     | 54679     | 533      
    ll_cache:u         | 8585210   | 8604077   | 8223529  
    ll_cache_miss:u    | 111835    | 120436    | 9502     

== combo_038_s4 ==
single_modules:
    id | module                                   
    ---+------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl9 
    s1 | fetch_b64_d1_bp0_s16_r100_lin_p128_np2_l2
    s2 | hot_b128_bp3_r100_lshuf_p1_np2_l4        
    s3 | itlb_f64_l1_r100_lin_p128_np4_l1         
single_counts:
    metric             | s0        | s1       | s2       | s3      
    -------------------+-----------+----------+----------+---------
    cpu-cycles:u       | 178618867 | 59019188 | 25725414 | 34785705
    instructions:u     | 29430988  | 18870997 | 26001040 | 11290988
    br_retired:u       | 1991403   | 1991404  | 3941409  | 731403  
    br_mis_pred:u      | 290691    | 591127   | 418      | 454     
    l1i_cache:u        | 7489911   | 9118074  | 3336871  | 1524598 
    l1i_cache_refill:u | 1107      | 691      | 769      | 1041121 
    l1i_tlb:u          | 7489911   | 9118074  | 3336871  | 1524598 
    l1i_tlb_refill:u   | 48        | 48       | 49       | 660057  
    l2i_cache:u        | 1107      | 689      | 767      | 1041121 
    l2i_cache_refill:u | 758       | 602      | 605      | 22171   
    l2i_tlb:u          | 82        | 89       | 90       | 660120  
    l2i_tlb_refill:u   | 14        | 19       | 13       | 105     
    l1d_cache:u        | 6826922   | 4669080  | 5255388  | 775434  
    l1d_cache_refill:u | 4810460   | 1077987  | 158      | 326957  
    l1d_tlb:u          | 12202910  | 7353909  | 5257510  | 1091056 
    l1d_tlb_refill:u   | 5160063   | 670067   | 62       | 175063  
    l2d_cache:u        | 15454328  | 3767324  | 1284     | 2571966 
    l2d_cache_refill:u | 4344423   | 1079812  | 866      | 470464  
    l2d_tlb:u          | 5163918   | 670090   | 101      | 175350  
    l2d_tlb_refill:u   | 15        | 20       | 7        | 54      
    ll_cache:u         | 4343502   | 1079159  | 222      | 450529  
    ll_cache_miss:u    | 21272     | 560      | 60       | 3943    
combined_orders:
    id        | modules                                                                                                                                              
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl9+fetch_b64_d1_bp0_s16_r100_lin_p128_np2_l2+hot_b128_bp3_r100_lshuf_p1_np2_l4+itlb_f64_l1_r100_lin_p128_np4_l1
    shuffle   | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl9+itlb_f64_l1_r100_lin_p128_np4_l1+hot_b128_bp3_r100_lshuf_p1_np2_l4+fetch_b64_d1_bp0_s16_r100_lin_p128_np2_l2
    sum       | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl9+fetch_b64_d1_bp0_s16_r100_lin_p128_np2_l2+hot_b128_bp3_r100_lshuf_p1_np2_l4+itlb_f64_l1_r100_lin_p128_np4_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 263185744 | 275990785 | 298149174
    instructions:u     | 85561998  | 85561998  | 85594013 
    br_retired:u       | 8652013   | 8652013   | 8655619  
    br_mis_pred:u      | 888345    | 881903    | 882690   
    l1i_cache:u        | 21136380  | 20987831  | 21469454 
    l1i_cache_refill:u | 1279331   | 935326    | 1043688  
    l1i_tlb:u          | 21136380  | 20987831  | 21469454 
    l1i_tlb_refill:u   | 661061    | 661076    | 660202   
    l2i_cache:u        | 1279329   | 935327    | 1043684  
    l2i_cache_refill:u | 73215     | 20997     | 24136    
    l2i_tlb:u          | 661226    | 661159    | 660381   
    l2i_tlb_refill:u   | 69        | 92        | 151      
    l1d_cache:u        | 17557261  | 17523633  | 17526824 
    l1d_cache_refill:u | 6125539   | 6133802   | 6215562  
    l1d_tlb:u          | 25770394  | 25665136  | 25905385 
    l1d_tlb_refill:u   | 5980539   | 5970252   | 6005255  
    l2d_cache:u        | 22945521  | 23060976  | 21794902 
    l2d_cache_refill:u | 6148791   | 6919564   | 5895565  
    l2d_tlb:u          | 6000295   | 5978318   | 6009459  
    l2d_tlb_refill:u   | 202       | 275       | 96       
    ll_cache:u         | 6057716   | 6898027   | 5873412  
    ll_cache_miss:u    | 13722     | 20380     | 25835    

== combo_039_s4 ==
single_modules:
    id | module                                 
    ---+----------------------------------------
    s0 | cold_b128_d4_bitrev_lin_p128_np4_l1    
    s1 | fetch_b64_d1_bp0_s16_r100_lin_p1_np1_l1
    s2 | hot_b128_bp3_r100_pstr_p512_np1_l4_sp17
    s3 | itlb_f64_l1_r100_lin_p128_np1_l2       
single_counts:
    metric             | s0       | s1       | s2        | s3       
    -------------------+----------+----------+-----------+----------
    cpu-cycles:u       | 35904977 | 20757622 | 240617266 | 115368163
    instructions:u     | 25590988 | 18231049 | 26000998  | 11930988 
    br_retired:u       | 1991403  | 1991410  | 3941405   | 731403   
    br_mis_pred:u      | 290674   | 590427   | 467       | 467      
    l1i_cache:u        | 7118752  | 8489399  | 3347553   | 1620739  
    l1i_cache_refill:u | 1014     | 638      | 1338      | 1556755  
    l1i_tlb:u          | 7118752  | 8489399  | 3347553   | 1620739  
    l1i_tlb_refill:u   | 47       | 39       | 48        | 660074   
    l2i_cache:u        | 1012     | 638      | 1337      | 1556753  
    l2i_cache_refill:u | 762      | 566      | 691       | 869168   
    l2i_tlb:u          | 93       | 66       | 87        | 660135   
    l2i_tlb_refill:u   | 14       | 11       | 19        | 24       
    l1d_cache:u        | 2975966  | 4005360  | 5259107   | 1415497  
    l1d_cache_refill:u | 481283   | 144      | 5119962   | 1254809  
    l1d_tlb:u          | 3587032  | 5768999  | 10492678  | 2805917  
    l1d_tlb_refill:u   | 350060   | 60       | 5145656   | 1305513  
    l2d_cache:u        | 3842579  | 1241     | 20212036  | 5388571  
    l2d_cache_refill:u | 777270   | 864      | 10245540  | 2476764  
    l2d_tlb:u          | 352388   | 79       | 5146523   | 1305535  
    l2d_tlb_refill:u   | 16       | 10       | 299       | 14       
    ll_cache:u         | 776537   | 273      | 10244620  | 1738417  
    ll_cache_miss:u    | 31051    | 32       | 209       | 530      
combined_orders:
    id        | modules                                                                                                                                             
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lin_p128_np4_l1+fetch_b64_d1_bp0_s16_r100_lin_p1_np1_l1+hot_b128_bp3_r100_pstr_p512_np1_l4_sp17+itlb_f64_l1_r100_lin_p128_np1_l2
    shuffle   | itlb_f64_l1_r100_lin_p128_np1_l2+fetch_b64_d1_bp0_s16_r100_lin_p1_np1_l1+cold_b128_d4_bitrev_lin_p128_np4_l1+hot_b128_bp3_r100_pstr_p512_np1_l4_sp17
    sum       | cold_b128_d4_bitrev_lin_p128_np4_l1+fetch_b64_d1_bp0_s16_r100_lin_p1_np1_l1+hot_b128_bp3_r100_pstr_p512_np1_l4_sp17+itlb_f64_l1_r100_lin_p128_np1_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 477518156 | 584614894 | 412648028
    instructions:u     | 81721851  | 81721851  | 81754023 
    br_retired:u       | 8651993   | 8651993   | 8655621  
    br_mis_pred:u      | 884385    | 882137    | 882035   
    l1i_cache:u        | 20385233  | 20395346  | 20576443 
    l1i_cache_refill:u | 1072294   | 989276    | 1559745  
    l1i_tlb:u          | 20385233  | 20395346  | 20576443 
    l1i_tlb_refill:u   | 660982    | 660986    | 660208   
    l2i_cache:u        | 1072293   | 989276    | 1559740  
    l2i_cache_refill:u | 693397    | 688693    | 871187   
    l2i_tlb:u          | 661060    | 661138    | 660381   
    l2i_tlb_refill:u   | 858       | 958       | 68       
    l1d_cache:u        | 13641750  | 13642208  | 13655930 
    l1d_cache_refill:u | 6959148   | 6983436   | 6856198  
    l1d_tlb:u          | 22591952  | 22616763  | 22654626 
    l1d_tlb_refill:u   | 6793896   | 6795187   | 6801289  
    l2d_cache:u        | 31311397  | 31617307  | 29444427 
    l2d_cache_refill:u | 14369973  | 14557242  | 13500438 
    l2d_tlb:u          | 6795345   | 6796064   | 6804525  
    l2d_tlb_refill:u   | 3041      | 3307      | 339      
    ll_cache:u         | 13709080  | 13802940  | 12759847 
    ll_cache_miss:u    | 228277    | 292669    | 31822    

== combo_040_s4 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b64_d4_bitrev_lshuf_p1_np1_l4              
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l4_sp33
    s2 | hot_b128_bp3_r100_lstr_p128_np4_l2_sl3          
    s3 | itlb_f64_l1_r100_pstr_p512_np4_l2_sp17          
single_counts:
    metric             | s0       | s1        | s2       | s3       
    -------------------+----------+-----------+----------+----------
    cpu-cycles:u       | 16457262 | 244710485 | 93536203 | 130225621
    instructions:u     | 14871055 | 39991007  | 23440994 | 11930988 
    br_retired:u       | 1031408  | 3911406   | 3941401  | 731403   
    br_mis_pred:u      | 130653   | 1237109   | 489      | 503      
    l1i_cache:u        | 3723647  | 18664898  | 3011047  | 1614233  
    l1i_cache_refill:u | 745      | 1183      | 857      | 950464   
    l1i_tlb:u          | 3723647  | 18664898  | 3011047  | 1614233  
    l1i_tlb_refill:u   | 56       | 54        | 52       | 660073   
    l2i_cache:u        | 746      | 1183      | 858      | 950463   
    l2i_cache_refill:u | 645      | 768       | 661      | 124875   
    l2i_tlb:u          | 99       | 96        | 105      | 660149   
    l2i_tlb_refill:u   | 33       | 23        | 38       | 156      
    l1d_cache:u        | 3455395  | 11711268  | 2697285  | 1415635  
    l1d_cache_refill:u | 147      | 4770344   | 2295290  | 1279920  
    l1d_tlb:u          | 3457615  | 20736909  | 4769192  | 2806754  
    l1d_tlb_refill:u   | 61       | 5160145   | 1940063  | 1305377  
    l2d_cache:u        | 1441     | 15073511  | 7476631  | 6106017  
    l2d_cache_refill:u | 982      | 3927477   | 2367561  | 2653743  
    l2d_tlb:u          | 83       | 5174666   | 1940484  | 1305419  
    l2d_tlb_refill:u   | 26       | 165       | 129      | 722      
    ll_cache:u         | 299      | 3926527   | 2366752  | 2564692  
    ll_cache_miss:u    | 79       | 49257     | 1367     | 5173     
combined_orders:
    id        | modules                                                                                                                                                          
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lshuf_p1_np1_l4+fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l4_sp33+hot_b128_bp3_r100_lstr_p128_np4_l2_sl3+itlb_f64_l1_r100_pstr_p512_np4_l2_sp17
    shuffle   | cold_b64_d4_bitrev_lshuf_p1_np1_l4+hot_b128_bp3_r100_lstr_p128_np4_l2_sl3+itlb_f64_l1_r100_pstr_p512_np4_l2_sp17+fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l4_sp33
    sum       | cold_b64_d4_bitrev_lshuf_p1_np1_l4+fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l4_sp33+hot_b128_bp3_r100_lstr_p128_np4_l2_sl3+itlb_f64_l1_r100_pstr_p512_np4_l2_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 522553474 | 531084232 | 484929571
    instructions:u     | 90201851  | 90201851  | 90234044 
    br_retired:u       | 9611993   | 9611993   | 9615618  
    br_mis_pred:u      | 1373169   | 1381652   | 1368754  
    l1i_cache:u        | 25860380  | 26102773  | 27013825 
    l1i_cache_refill:u | 997676    | 1065498   | 953249   
    l1i_tlb:u          | 25860380  | 26102773  | 27013825 
    l1i_tlb_refill:u   | 661091    | 661088    | 660235   
    l2i_cache:u        | 997674    | 1065498   | 953250   
    l2i_cache_refill:u | 83145     | 70472     | 126949   
    l2i_tlb:u          | 661162    | 661149    | 660449   
    l2i_tlb_refill:u   | 1018      | 930       | 250      
    l1d_cache:u        | 19282813  | 19282253  | 19279583 
    l1d_cache_refill:u | 8341951   | 8378522   | 8345701  
    l1d_tlb:u          | 31738331  | 31709111  | 31770470 
    l1d_tlb_refill:u   | 8411501   | 8411557   | 8405646  
    l2d_cache:u        | 29980407  | 29704860  | 28657600 
    l2d_cache_refill:u | 10095648  | 10070538  | 8949763  
    l2d_tlb:u          | 8431833   | 8416268   | 8420652  
    l2d_tlb_refill:u   | 2916      | 5028      | 1042     
    ll_cache:u         | 10010254  | 9991129   | 8858270  
    ll_cache_miss:u    | 70951     | 47089     | 55876    

== combo_041_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p1_np1_l2_sl3         
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l4_sp3
    s2 | hot_b128_bp3_r100_pstr_p512_np4_l4_sp3         
    s3 | itlb_f64_l1_r100_lstr_p512_np2_l4_sl3          
single_counts:
    metric             | s0       | s1        | s2        | s3       
    -------------------+----------+-----------+-----------+----------
    cpu-cycles:u       | 23323277 | 258046613 | 270558254 | 201456238
    instructions:u     | 26871049 | 39991007  | 26001089  | 13210988 
    br_retired:u       | 1991410  | 3911406   | 3941412   | 731403   
    br_mis_pred:u      | 290405   | 1241150   | 454       | 505      
    l1i_cache:u        | 7157523  | 18666777  | 3350583   | 1871751  
    l1i_cache_refill:u | 840      | 1410      | 1558      | 1104277  
    l1i_tlb:u          | 7157523  | 18666777  | 3350583   | 1871751  
    l1i_tlb_refill:u   | 48       | 56        | 53        | 670071   
    l2i_cache:u        | 839      | 1408      | 1558      | 1104275  
    l2i_cache_refill:u | 704      | 756       | 822       | 514441   
    l2i_tlb:u          | 81       | 98        | 158       | 670132   
    l2i_tlb_refill:u   | 14       | 33        | 39        | 139      
    l1d_cache:u        | 4255335  | 11735420  | 5259920   | 2695772  
    l1d_cache_refill:u | 159      | 4864923   | 5119853   | 2559654  
    l1d_tlb:u          | 4257409  | 20866085  | 10499554  | 5356285  
    l1d_tlb_refill:u   | 61       | 5163418   | 5145831   | 2583967  
    l2d_cache:u        | 1319     | 16055889  | 20253012  | 11795351 
    l2d_cache_refill:u | 931      | 4646308   | 10233857  | 5728077  
    l2d_tlb:u          | 80       | 5163471   | 5146873   | 2584003  
    l2d_tlb_refill:u   | 7        | 12        | 611       | 227      
    ll_cache:u         | 224      | 4645682   | 10232874  | 5140260  
    ll_cache_miss:u    | 25       | 64        | 1556      | 11384    
combined_orders:
    id        | modules                                                                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p1_np1_l2_sl3+fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l4_sp3+hot_b128_bp3_r100_pstr_p512_np4_l4_sp3+itlb_f64_l1_r100_lstr_p512_np2_l4_sl3
    shuffle   | fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l4_sp3+hot_b128_bp3_r100_pstr_p512_np4_l4_sp3+cold_b128_d4_bitrev_lstr_p1_np1_l2_sl3+itlb_f64_l1_r100_lstr_p512_np2_l4_sl3
    sum       | cold_b128_d4_bitrev_lstr_p1_np1_l2_sl3+fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l4_sp3+hot_b128_bp3_r100_pstr_p512_np4_l4_sp3+itlb_f64_l1_r100_lstr_p512_np2_l4_sl3
combined_counts:
    metric             | canonical  | shuffle   | sum      
    -------------------+------------+-----------+----------
    cpu-cycles:u       | 1056596700 | 850953117 | 753384382
    instructions:u     | 106041851  | 106041857 | 106074133
    br_retired:u       | 10571993   | 10571991  | 10575631 
    br_mis_pred:u      | 1531870    | 1553124   | 1532514  
    l1i_cache:u        | 29842298   | 30192795  | 31046634 
    l1i_cache_refill:u | 1114076    | 1021664   | 1108085  
    l1i_tlb:u          | 29842298   | 30192795  | 31046634 
    l1i_tlb_refill:u   | 671158     | 671155    | 670228   
    l2i_cache:u        | 1114077    | 1021663   | 1108080  
    l2i_cache_refill:u | 584022     | 643140    | 516723   
    l2i_tlb:u          | 671533     | 671349    | 670469   
    l2i_tlb_refill:u   | 7361       | 7698      | 225      
    l1d_cache:u        | 23990970   | 23944140  | 23946447 
    l1d_cache_refill:u | 12470707   | 12460982  | 12544589 
    l1d_tlb:u          | 41260950   | 41152567  | 40979333 
    l1d_tlb_refill:u   | 12941969   | 12932072  | 12893277 
    l2d_cache:u        | 47237266   | 47144074  | 48105571 
    l2d_cache_refill:u | 20517916   | 20437395  | 20609173 
    l2d_tlb:u          | 12949544   | 12944792  | 12894427 
    l2d_tlb_refill:u   | 54128      | 58668     | 857      
    ll_cache:u         | 19942114   | 19891768  | 20019040 
    ll_cache_miss:u    | 76505      | 190201    | 13029    

== combo_042_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np2_l2_sl9          
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l4_sp33
    s2 | hot_b128_bp3_r100_pstr_p128_np4_l4_sp3         
    s3 | itlb_f64_l1_r100_lstr_p512_np4_l4_sl5          
single_counts:
    metric             | s0       | s1        | s2        | s3       
    -------------------+----------+-----------+-----------+----------
    cpu-cycles:u       | 11291800 | 143410019 | 191546895 | 172278760
    instructions:u     | 13591055 | 20150997  | 26000994  | 13210994 
    br_retired:u       | 1031408  | 1991404   | 3941401   | 731401   
    br_mis_pred:u      | 130588   | 591693    | 500       | 507      
    l1i_cache:u        | 3572592  | 9482410   | 3332695   | 1800949  
    l1i_cache_refill:u | 655      | 749       | 1115      | 1139475  
    l1i_tlb:u          | 3572592  | 9482410   | 3332695   | 1800949  
    l1i_tlb_refill:u   | 42       | 52        | 52        | 670085   
    l2i_cache:u        | 655      | 749       | 1115      | 1139472  
    l2i_cache_refill:u | 579      | 631       | 723       | 207797   
    l2i_tlb:u          | 78       | 110       | 116       | 670134   
    l2i_tlb_refill:u   | 13       | 48        | 44        | 168      
    l1d_cache:u        | 2175362  | 5964687   | 5257215   | 2695787  
    l1d_cache_refill:u | 147      | 2431194   | 4877657   | 2559482  
    l1d_tlb:u          | 2177586  | 10507493  | 10450322  | 5373744  
    l1d_tlb_refill:u   | 64       | 2600875   | 5140065   | 2586240  
    l2d_cache:u        | 1359     | 7436224   | 13804868  | 11413285 
    l2d_cache_refill:u | 978      | 1959251   | 3531178   | 5246189  
    l2d_tlb:u          | 87       | 2609426   | 5140499   | 2586285  
    l2d_tlb_refill:u   | 30       | 139       | 161       | 712      
    ll_cache:u         | 321      | 1958526   | 3530328   | 5147355  
    ll_cache_miss:u    | 71       | 56        | 571       | 12611    
combined_orders:
    id        | modules                                                                                                                                                           
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np2_l2_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l4_sp33+hot_b128_bp3_r100_pstr_p128_np4_l4_sp3+itlb_f64_l1_r100_lstr_p512_np4_l4_sl5
    shuffle   | itlb_f64_l1_r100_lstr_p512_np4_l4_sl5+cold_b64_d4_bitrev_lstr_p1_np2_l2_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l4_sp33+hot_b128_bp3_r100_pstr_p128_np4_l4_sp3
    sum       | cold_b64_d4_bitrev_lstr_p1_np2_l2_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l4_sp33+hot_b128_bp3_r100_pstr_p128_np4_l4_sp3+itlb_f64_l1_r100_lstr_p512_np4_l4_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 490127149 | 638047276 | 518527474
    instructions:u     | 72921851  | 72921851  | 72954040 
    br_retired:u       | 7691993   | 7691993   | 7695614  
    br_mis_pred:u      | 724615    | 728179    | 723288   
    l1i_cache:u        | 17518682  | 17545399  | 18188646 
    l1i_cache_refill:u | 1055902   | 1005408   | 1141994  
    l1i_tlb:u          | 17518682  | 17545399  | 18188646 
    l1i_tlb_refill:u   | 670763    | 670766    | 670231   
    l2i_cache:u        | 1055901   | 1005411   | 1141991  
    l2i_cache_refill:u | 89110     | 139424    | 209730   
    l2i_tlb:u          | 670835    | 671070    | 670438   
    l2i_tlb_refill:u   | 1249      | 1105      | 273      
    l1d_cache:u        | 16049955  | 16038042  | 16093051 
    l1d_cache_refill:u | 9869957   | 9828964   | 9868480  
    l1d_tlb:u          | 28395646  | 28392724  | 28509145 
    l1d_tlb_refill:u   | 10310273  | 10310002  | 10327244 
    l2d_cache:u        | 36648179  | 35544360  | 32655736 
    l2d_cache_refill:u | 14396417  | 13576939  | 10737596 
    l2d_tlb:u          | 10313792  | 10310832  | 10336297 
    l2d_tlb_refill:u   | 4069      | 3226      | 1042     
    ll_cache:u         | 14217794  | 13422571  | 10636530 
    ll_cache_miss:u    | 24302     | 18503     | 13309    

== combo_043_s4 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p128_np2_l2_sp3     
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p1_np2_l2_sl5
    s2 | hot_b64_bp3_r100_pstr_p512_np1_l4_sp3        
    s3 | itlb_f64_l1_r100_pstr_p512_np1_l1_sp17       
single_counts:
    metric             | s0       | s1       | s2        | s3      
    -------------------+----------+----------+-----------+---------
    cpu-cycles:u       | 86188269 | 47924212 | 125698814 | 51654546
    instructions:u     | 26870994 | 37430997 | 13200988  | 11290988
    br_retired:u       | 1991401  | 3911404  | 2021403   | 731403  
    br_mis_pred:u      | 290723   | 1231056  | 456       | 461     
    l1i_cache:u        | 7256333  | 16953330 | 1737765   | 1496095 
    l1i_cache_refill:u | 949      | 1081     | 813       | 1673444 
    l1i_tlb:u          | 7256333  | 16953330 | 1737765   | 1496095 
    l1i_tlb_refill:u   | 57       | 52       | 52        | 660087  
    l2i_cache:u        | 946      | 1080     | 812       | 1673444 
    l2i_cache_refill:u | 769      | 730      | 576       | 143479  
    l2i_tlb:u          | 108      | 95       | 156       | 660167  
    l2i_tlb_refill:u   | 42       | 12       | 43        | 39      
    l1d_cache:u        | 4256445  | 9115358  | 2697351   | 775497  
    l1d_cache_refill:u | 2415058  | 175      | 2560008   | 640371  
    l1d_tlb:u          | 6944119  | 12788769 | 5365266   | 1579099 
    l1d_tlb_refill:u   | 2580109  | 64       | 2584837   | 680071  
    l2d_cache:u        | 8503036  | 1598     | 10107329  | 3556560 
    l2d_cache_refill:u | 2916804  | 963      | 5123898   | 1393083 
    l2d_tlb:u          | 2580179  | 82       | 2585344   | 680093  
    l2d_tlb_refill:u   | 161      | 4        | 548       | 128     
    ll_cache:u         | 2915884  | 260      | 5123113   | 1284983 
    ll_cache_miss:u    | 4299     | 30       | 142       | 72      
combined_orders:
    id        | modules                                                                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p128_np2_l2_sp3+fetch_b128_d1_bp0_s16_r100_lstr_p1_np2_l2_sl5+hot_b64_bp3_r100_pstr_p512_np1_l4_sp3+itlb_f64_l1_r100_pstr_p512_np1_l1_sp17
    shuffle   | cold_b128_d4_bitrev_pstr_p128_np2_l2_sp3+fetch_b128_d1_bp0_s16_r100_lstr_p1_np2_l2_sl5+itlb_f64_l1_r100_pstr_p512_np1_l1_sp17+hot_b64_bp3_r100_pstr_p512_np1_l4_sp3
    sum       | cold_b128_d4_bitrev_pstr_p128_np2_l2_sp3+fetch_b128_d1_bp0_s16_r100_lstr_p1_np2_l2_sl5+hot_b64_bp3_r100_pstr_p512_np1_l4_sp3+itlb_f64_l1_r100_pstr_p512_np1_l1_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 466902079 | 408099509 | 311465841
    instructions:u     | 88761864  | 88761851  | 88793967 
    br_retired:u       | 8651993   | 8651993   | 8655611  
    br_mis_pred:u      | 1523069   | 1521970   | 1522696  
    l1i_cache:u        | 27436345  | 27326332  | 27443523 
    l1i_cache_refill:u | 1029723   | 907721    | 1676287  
    l1i_tlb:u          | 27436345  | 27326332  | 27443523 
    l1i_tlb_refill:u   | 661089    | 661091    | 660248   
    l2i_cache:u        | 1029721   | 907721    | 1676282  
    l2i_cache_refill:u | 156947    | 227733    | 145554   
    l2i_tlb:u          | 661291    | 661327    | 660526   
    l2i_tlb_refill:u   | 6442      | 5666      | 136      
    l1d_cache:u        | 16843081  | 16844530  | 16844651 
    l1d_cache_refill:u | 5570757   | 5579703   | 5615612  
    l1d_tlb:u          | 26643982  | 26665639  | 26677253 
    l1d_tlb_refill:u   | 5829370   | 5830147   | 5845081  
    l2d_cache:u        | 22022226  | 22421517  | 22168523 
    l2d_cache_refill:u | 8938108   | 9284748   | 9434748  
    l2d_tlb:u          | 5830106   | 5833930   | 5845698  
    l2d_tlb_refill:u   | 55360     | 54253     | 841      
    ll_cache:u         | 8806213   | 9125051   | 9324240  
    ll_cache_miss:u    | 92282     | 23306     | 4543     

== combo_044_s4 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p128_np4_l4_sp17      
    s1 | fetch_b64_d1_bp0_s16_r100_lstr_p128_np2_l4_sl9
    s2 | hot_b128_bp3_r100_lshuf_p512_np2_l4           
    s3 | itlb_f64_l1_r100_rand_p128_np1_l1             
single_counts:
    metric             | s0       | s1       | s2        | s3      
    -------------------+----------+----------+-----------+---------
    cpu-cycles:u       | 68208287 | 81271067 | 252115020 | 51694107
    instructions:u     | 14870988 | 20150997 | 26000998  | 11290988
    br_retired:u       | 1031403  | 1991404  | 3941405   | 731403  
    br_mis_pred:u      | 130706   | 601108   | 535       | 491     
    l1i_cache:u        | 3739274  | 9303684  | 3344653   | 1489126 
    l1i_cache_refill:u | 826      | 658      | 1466      | 1271917 
    l1i_tlb:u          | 3739274  | 9303684  | 3344653   | 1489126 
    l1i_tlb_refill:u   | 47       | 42       | 55        | 660075  
    l2i_cache:u        | 825      | 658      | 1465      | 1271917 
    l2i_cache_refill:u | 638      | 576      | 771       | 129637  
    l2i_tlb:u          | 90       | 79       | 124       | 660151  
    l2i_tlb_refill:u   | 16       | 13       | 46        | 97      
    l1d_cache:u        | 3464085  | 5924820  | 5256732   | 775535  
    l1d_cache_refill:u | 2393002  | 2385740  | 4287590   | 633105  
    l1d_tlb:u          | 6168102  | 10494879 | 8007007   | 1520947 
    l1d_tlb_refill:u   | 2580064  | 2600063  | 2590062   | 664256  
    l2d_cache:u        | 7250130  | 7228548  | 20313331  | 3834796 
    l2d_cache_refill:u | 1749259  | 1762228  | 10194917  | 1201435 
    l2d_tlb:u          | 2580363  | 2610099  | 2590662   | 664286  
    l2d_tlb_refill:u   | 161      | 18       | 76        | 181     
    ll_cache:u         | 1748540  | 1761551  | 10193422  | 1053175 
    ll_cache_miss:u    | 10215    | 588      | 404       | 26      
combined_orders:
    id        | modules                                                                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p128_np4_l4_sp17+fetch_b64_d1_bp0_s16_r100_lstr_p128_np2_l4_sl9+hot_b128_bp3_r100_lshuf_p512_np2_l4+itlb_f64_l1_r100_rand_p128_np1_l1
    shuffle   | fetch_b64_d1_bp0_s16_r100_lstr_p128_np2_l4_sl9+itlb_f64_l1_r100_rand_p128_np1_l1+cold_b64_d4_bitrev_pstr_p128_np4_l4_sp17+hot_b128_bp3_r100_lshuf_p512_np2_l4
    sum       | cold_b64_d4_bitrev_pstr_p128_np4_l4_sp17+fetch_b64_d1_bp0_s16_r100_lstr_p128_np2_l4_sl9+hot_b128_bp3_r100_lshuf_p512_np2_l4+itlb_f64_l1_r100_rand_p128_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 575511065 | 560434145 | 453288481
    instructions:u     | 72281842  | 72281842  | 72313971 
    br_retired:u       | 7691992   | 7691992   | 7695615  
    br_mis_pred:u      | 727865    | 732337    | 732840   
    l1i_cache:u        | 17408070  | 17472889  | 17876737 
    l1i_cache_refill:u | 1207389   | 1015470   | 1274867  
    l1i_tlb:u          | 17408070  | 17472889  | 17876737 
    l1i_tlb_refill:u   | 660835    | 660912    | 660219   
    l2i_cache:u        | 1207393   | 1015475   | 1274865  
    l2i_cache_refill:u | 183578    | 249807    | 131622   
    l2i_tlb:u          | 660901    | 661020    | 660444   
    l2i_tlb_refill:u   | 1001      | 1645      | 172      
    l1d_cache:u        | 15522547  | 15488124  | 15421172 
    l1d_cache_refill:u | 9544273   | 9496403   | 9699437  
    l1d_tlb:u          | 26499130  | 26432346  | 26190935 
    l1d_tlb_refill:u   | 8450604   | 8435304   | 8434445  
    l2d_cache:u        | 39847870  | 38843147  | 38626805 
    l2d_cache_refill:u | 15730670  | 14800448  | 14907839 
    l2d_tlb:u          | 8456362   | 8448572   | 8445410  
    l2d_tlb_refill:u   | 14973     | 12492     | 436      
    ll_cache:u         | 15486033  | 14592306  | 14756688 
    ll_cache_miss:u    | 23278     | 34475     | 11233    

== combo_045_s4 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p512_np2_l2              
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17
    s2 | hot_b64_bp3_r100_lin_p1_np1_l2                  
    s3 | itlb_f64_l1_r100_lin_p128_np2_l4                
single_counts:
    metric             | s0       | s1        | s2       | s3       
    -------------------+----------+-----------+----------+----------
    cpu-cycles:u       | 74485886 | 330932936 | 7798335  | 127735769
    instructions:u     | 13590988 | 39990951  | 11921040 | 13210988 
    br_retired:u       | 1031403  | 3911393   | 2021409  | 731403   
    br_mis_pred:u      | 130829   | 1236373   | 402      | 508      
    l1i_cache:u        | 3595787  | 18690095  | 1566030  | 1756243  
    l1i_cache_refill:u | 910      | 1424      | 599      | 1103078  
    l1i_tlb:u          | 3595787  | 18690095  | 1566030  | 1756243  
    l1i_tlb_refill:u   | 52       | 54        | 42       | 670054   
    l2i_cache:u        | 910      | 1424      | 597      | 1103077  
    l2i_cache_refill:u | 676      | 927       | 553      | 814766   
    l2i_tlb:u          | 100      | 109       | 76       | 670139   
    l2i_tlb_refill:u   | 47       | 48        | 17       | 103      
    l1d_cache:u        | 2176252  | 11738466  | 1415153  | 2695508  
    l1d_cache_refill:u | 1028280  | 5040983   | 147      | 1512518  
    l1d_tlb:u          | 2975340  | 20831728  | 1417117  | 4826333  
    l1d_tlb_refill:u   | 660062   | 5162590   | 60       | 1300069  
    l2d_cache:u        | 5531903  | 22741165  | 1149     | 7877766  
    l2d_cache_refill:u | 2667125  | 10667840  | 806      | 3077720  
    l2d_tlb:u          | 660088   | 5170923   | 79       | 1300088  
    l2d_tlb_refill:u   | 625      | 569       | 5        | 16       
    ll_cache:u         | 2666154  | 10666462  | 243      | 2169743  
    ll_cache_miss:u    | 32917    | 143354    | 28       | 154      
combined_orders:
    id        | modules                                                                                                                                            
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p512_np2_l2+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17+hot_b64_bp3_r100_lin_p1_np1_l2+itlb_f64_l1_r100_lin_p128_np2_l4
    shuffle   | hot_b64_bp3_r100_lin_p1_np1_l2+itlb_f64_l1_r100_lin_p128_np2_l4+cold_b64_d4_bitrev_lin_p512_np2_l2+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17
    sum       | cold_b64_d4_bitrev_lin_p512_np2_l2+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17+hot_b64_bp3_r100_lin_p1_np1_l2+itlb_f64_l1_r100_lin_p128_np2_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 698200412 | 732286594 | 540952926
    instructions:u     | 78681851  | 78681857  | 78713967 
    br_retired:u       | 7691993   | 7691991   | 7695608  
    br_mis_pred:u      | 1363664   | 1390539   | 1368112  
    l1i_cache:u        | 24480535  | 24851131  | 25608155 
    l1i_cache_refill:u | 1000221   | 1343375   | 1106011  
    l1i_tlb:u          | 24480535  | 24851131  | 25608155 
    l1i_tlb_refill:u   | 660984    | 660983    | 670202   
    l2i_cache:u        | 1000222   | 1343373   | 1106008  
    l2i_cache_refill:u | 718590    | 920007    | 816922   
    l2i_tlb:u          | 661047    | 661038    | 670424   
    l2i_tlb_refill:u   | 4224      | 5942      | 215      
    l1d_cache:u        | 18085740  | 18078752  | 18025379 
    l1d_cache_refill:u | 7837898   | 7828995   | 7581928  
    l1d_tlb:u          | 30040330  | 30079196  | 30050518 
    l1d_tlb_refill:u   | 7160143   | 7124469   | 7122781  
    l2d_cache:u        | 36808995  | 36239533  | 36151983 
    l2d_cache_refill:u | 16970417  | 16732230  | 16413491 
    l2d_tlb:u          | 7173665   | 7133858   | 7131178  
    l2d_tlb_refill:u   | 50941     | 65115     | 1215     
    ll_cache:u         | 16314064  | 15962167  | 15502602 
    ll_cache_miss:u    | 263688    | 268697    | 176453   

== combo_046_s4 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p512_np4_l1_sl5         
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l1_sp17
    s2 | hot_b64_bp3_r100_rand_p128_np2_l4               
    s3 | itlb_f64_l1_r100_lshuf_p512_np4_l2              
single_counts:
    metric             | s0       | s1       | s2       | s3      
    -------------------+----------+----------+----------+---------
    cpu-cycles:u       | 41550212 | 98511073 | 89270579 | 78779638
    instructions:u     | 12950988 | 36150997 | 13200988 | 11930988
    br_retired:u       | 1031403  | 3911404  | 2021403  | 731403  
    br_mis_pred:u      | 130692   | 1236200  | 482      | 463     
    l1i_cache:u        | 3541873  | 18120833 | 1739230  | 1646212 
    l1i_cache_refill:u | 699      | 955      | 821      | 1210399 
    l1i_tlb:u          | 3541873  | 18120833 | 1739230  | 1646212 
    l1i_tlb_refill:u   | 51       | 48       | 54       | 660067  
    l2i_cache:u        | 699      | 955      | 820      | 1210399 
    l2i_cache_refill:u | 626      | 732      | 602      | 180911  
    l2i_tlb:u          | 104      | 89       | 196      | 660133  
    l2i_tlb_refill:u   | 44       | 21       | 45       | 324     
    l1d_cache:u        | 1535898  | 7896592  | 2696607  | 1415671 
    l1d_cache_refill:u | 638793   | 1274574  | 2435666  | 784962  
    l1d_tlb:u          | 2302569  | 13098228 | 5029245  | 1935737 
    l1d_tlb_refill:u   | 663946   | 1324099  | 2260088  | 340059  
    l2d_cache:u        | 2774464  | 5605687  | 7795671  | 6901844 
    l2d_cache_refill:u | 1291111  | 2742492  | 2475373  | 2557463 
    l2d_tlb:u          | 663986   | 1337454  | 2260376  | 340281  
    l2d_tlb_refill:u   | 99       | 584      | 136      | 643     
    ll_cache:u         | 1290456  | 2741382  | 2474696  | 2369823 
    ll_cache_miss:u    | 365      | 71334    | 265      | 1058    
combined_orders:
    id        | modules                                                                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p512_np4_l1_sl5+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l1_sp17+hot_b64_bp3_r100_rand_p128_np2_l4+itlb_f64_l1_r100_lshuf_p512_np4_l2
    shuffle   | fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l1_sp17+hot_b64_bp3_r100_rand_p128_np2_l4+cold_b64_d4_bitrev_lstr_p512_np4_l1_sl5+itlb_f64_l1_r100_lshuf_p512_np4_l2
    sum       | cold_b64_d4_bitrev_lstr_p512_np4_l1_sl5+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l1_sp17+hot_b64_bp3_r100_rand_p128_np2_l4+itlb_f64_l1_r100_lshuf_p512_np4_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 426148412 | 485199356 | 308111502
    instructions:u     | 74201842  | 74201842  | 74233961 
    br_retired:u       | 7691992   | 7691992   | 7695613  
    br_mis_pred:u      | 1366751   | 1367739   | 1367837  
    l1i_cache:u        | 23756829  | 23905297  | 25048148 
    l1i_cache_refill:u | 929730    | 1101375   | 1212874  
    l1i_tlb:u          | 23756829  | 23905297  | 25048148 
    l1i_tlb_refill:u   | 660848    | 660845    | 660220   
    l2i_cache:u        | 929729    | 1101374   | 1212873  
    l2i_cache_refill:u | 172066    | 118203    | 182871   
    l2i_tlb:u          | 661025    | 661111    | 660522   
    l2i_tlb_refill:u   | 9061      | 11728     | 434      
    l1d_cache:u        | 13593666  | 13594622  | 13544768 
    l1d_cache_refill:u | 5272166   | 5272979   | 5133995  
    l1d_tlb:u          | 22553336  | 22561990  | 22365779 
    l1d_tlb_refill:u   | 4587888   | 4586530   | 4588192  
    l2d_cache:u        | 23068191  | 22694557  | 23077666 
    l2d_cache_refill:u | 9202749   | 8764034   | 9066439  
    l2d_tlb:u          | 4598508   | 4596813   | 4602097  
    l2d_tlb_refill:u   | 154197    | 156506    | 1462     
    ll_cache:u         | 9028500   | 8644808   | 8876357  
    ll_cache_miss:u    | 34829     | 54309     | 73022    

== combo_047_s4 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np1_l2_sl3         
    s1 | fetch_b64_d1_bp0_s16_r100_lstr_p512_np4_l1_sl5
    s2 | hot_b64_bp3_r100_lstr_p512_np2_l2_sl5         
    s3 | itlb_f64_l1_r100_lshuf_p512_np2_l1            
single_counts:
    metric             | s0       | s1       | s2        | s3      
    -------------------+----------+----------+-----------+---------
    cpu-cycles:u       | 11313920 | 51528825 | 101874085 | 53371077
    instructions:u     | 13591049 | 18230997 | 11920988  | 11290988
    br_retired:u       | 1031410  | 1991404  | 2021403   | 731403  
    br_mis_pred:u      | 130767   | 591158   | 474       | 456     
    l1i_cache:u        | 3562350  | 9160441  | 1576493   | 1515196 
    l1i_cache_refill:u | 711      | 639      | 815       | 1374388 
    l1i_tlb:u          | 3562350  | 9160441  | 1576493   | 1515196 
    l1i_tlb_refill:u   | 54       | 45       | 51        | 660071  
    l2i_cache:u        | 711      | 640      | 813       | 1374386 
    l2i_cache_refill:u | 627      | 552      | 607       | 75051   
    l2i_tlb:u          | 107      | 90       | 179       | 660123  
    l2i_tlb_refill:u   | 33       | 24       | 48        | 53      
    l1d_cache:u        | 2175432  | 4038220  | 1416868   | 775644  
    l1d_cache_refill:u | 144      | 642285   | 1286016   | 629159  
    l1d_tlb:u          | 2177643  | 6621673  | 2802282   | 1167127 
    l1d_tlb_refill:u   | 60       | 670064   | 1304418   | 340063  
    l2d_cache:u        | 1497     | 2949436  | 5084203   | 4037690 
    l2d_cache_refill:u | 1027     | 1404955  | 2565538   | 1391877 
    l2d_tlb:u          | 83       | 672521   | 1304826   | 340120  
    l2d_tlb_refill:u   | 32       | 548      | 78        | 671     
    ll_cache:u         | 361      | 1404168  | 2564901   | 1294343 
    ll_cache_miss:u    | 47       | 24383    | 837       | 7403    
combined_orders:
    id        | modules                                                                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np1_l2_sl3+fetch_b64_d1_bp0_s16_r100_lstr_p512_np4_l1_sl5+hot_b64_bp3_r100_lstr_p512_np2_l2_sl5+itlb_f64_l1_r100_lshuf_p512_np2_l1
    shuffle   | cold_b64_d4_bitrev_lstr_p1_np1_l2_sl3+itlb_f64_l1_r100_lshuf_p512_np2_l1+hot_b64_bp3_r100_lstr_p512_np2_l2_sl5+fetch_b64_d1_bp0_s16_r100_lstr_p512_np4_l1_sl5
    sum       | cold_b64_d4_bitrev_lstr_p1_np1_l2_sl3+fetch_b64_d1_bp0_s16_r100_lstr_p512_np4_l1_sl5+hot_b64_bp3_r100_lstr_p512_np2_l2_sl5+itlb_f64_l1_r100_lshuf_p512_np2_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 263615882 | 283364906 | 218087907
    instructions:u     | 55001998  | 55001998  | 55034022 
    br_retired:u       | 5772013   | 5772013   | 5775620  
    br_mis_pred:u      | 727264    | 727823    | 722855   
    l1i_cache:u        | 15310959  | 15353986  | 15814480 
    l1i_cache_refill:u | 1152368   | 901972    | 1376553  
    l1i_tlb:u          | 15310959  | 15353986  | 15814480 
    l1i_tlb_refill:u   | 660646    | 660655    | 660221   
    l2i_cache:u        | 1152365   | 901972    | 1376550  
    l2i_cache_refill:u | 110063    | 131515    | 76837    
    l2i_tlb:u          | 660888    | 660870    | 660499   
    l2i_tlb_refill:u   | 8887      | 8781      | 158      
    l1d_cache:u        | 8413539   | 8455406   | 8406164  
    l1d_cache_refill:u | 2521179   | 2524245   | 2557604  
    l1d_tlb:u          | 13079171  | 13143814  | 12768725 
    l1d_tlb_refill:u   | 2350223   | 2327647   | 2314605  
    l2d_cache:u        | 12225327  | 12297637  | 12072826 
    l2d_cache_refill:u | 5403623   | 5433140   | 5363397  
    l2d_tlb:u          | 2360818   | 2342355   | 2317550  
    l2d_tlb_refill:u   | 133953    | 134145    | 1329     
    ll_cache:u         | 5286859   | 5295104   | 5263773  
    ll_cache_miss:u    | 38401     | 44337     | 32670    

== combo_048_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p512_np1_l2          
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np2_l2_sp33
    s2 | hot_b64_bp3_r100_lstr_p1_np2_l1_sl5            
    s3 | itlb_f64_l1_r100_lstr_p128_np2_l1_sl9          
single_counts:
    metric             | s0        | s1       | s2       | s3      
    -------------------+-----------+----------+----------+---------
    cpu-cycles:u       | 141861187 | 51499328 | 5247652  | 45125395
    instructions:u     | 26870988  | 18870997 | 11281040 | 11290988
    br_retired:u       | 1991403   | 1991404  | 2021409  | 731403  
    br_mis_pred:u      | 290688    | 595442   | 397      | 472     
    l1i_cache:u        | 7139986   | 9154284  | 1495923  | 1532868 
    l1i_cache_refill:u | 943       | 679      | 603      | 1009568 
    l1i_tlb:u          | 7139986   | 9154284  | 1495923  | 1532868 
    l1i_tlb_refill:u   | 43        | 53       | 51       | 660109  
    l2i_cache:u        | 943       | 678      | 602      | 1009567 
    l2i_cache_refill:u | 684       | 594      | 513      | 99821   
    l2i_tlb:u          | 81        | 102      | 93       | 660155  
    l2i_tlb_refill:u   | 23        | 44       | 20       | 111     
    l1d_cache:u        | 4257132   | 4680970  | 775106   | 775446  
    l1d_cache_refill:u | 2520837   | 1209223  | 140      | 619816  
    l1d_tlb:u          | 6944938   | 7938178  | 777001   | 1515058 
    l1d_tlb_refill:u   | 2584363   | 1322621  | 57       | 663856  
    l2d_cache:u        | 11153338  | 4318387  | 1018     | 3713383 
    l2d_cache_refill:u | 5382302   | 1044466  | 649      | 976691  
    l2d_tlb:u          | 2584395   | 1327762  | 76       | 663887  
    l2d_tlb_refill:u   | 102       | 13       | 6        | 178     
    ll_cache:u         | 5381404   | 1043881  | 163      | 836198  
    ll_cache_miss:u    | 21763     | 137      | 30       | 151     
combined_orders:
    id        | modules                                                                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p512_np1_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np2_l2_sp33+hot_b64_bp3_r100_lstr_p1_np2_l1_sl5+itlb_f64_l1_r100_lstr_p128_np2_l1_sl9
    shuffle   | cold_b128_d4_bitrev_lshuf_p512_np1_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np2_l2_sp33+itlb_f64_l1_r100_lstr_p128_np2_l1_sl9+hot_b64_bp3_r100_lstr_p1_np2_l1_sl5
    sum       | cold_b128_d4_bitrev_lshuf_p512_np1_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np2_l2_sp33+hot_b64_bp3_r100_lstr_p1_np2_l1_sl5+itlb_f64_l1_r100_lstr_p128_np2_l1_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 254737074 | 242292376 | 243733562
    instructions:u     | 68281907  | 68281907  | 68314013 
    br_retired:u       | 6732006   | 6732006   | 6735619  
    br_mis_pred:u      | 890464    | 882336    | 886999   
    l1i_cache:u        | 18801323  | 18660703  | 19323061 
    l1i_cache_refill:u | 1129129   | 999611    | 1011793  
    l1i_tlb:u          | 18801323  | 18660703  | 19323061 
    l1i_tlb_refill:u   | 660862    | 660854    | 660256   
    l2i_cache:u        | 1129127   | 999610    | 1011790  
    l2i_cache_refill:u | 58855     | 34953     | 101612   
    l2i_tlb:u          | 660920    | 660961    | 660431   
    l2i_tlb_refill:u   | 425       | 513       | 198      
    l1d_cache:u        | 10472639  | 10460192  | 10488654 
    l1d_cache_refill:u | 4325183   | 4325460   | 4350016  
    l1d_tlb:u          | 17137203  | 17077855  | 17175175 
    l1d_tlb_refill:u   | 4568797   | 4549864   | 4570897  
    l2d_cache:u        | 18133358  | 18397468  | 19186126 
    l2d_cache_refill:u | 7013553   | 7234587   | 7404108  
    l2d_tlb:u          | 4578863   | 4563684   | 4576120  
    l2d_tlb_refill:u   | 2181      | 3270      | 299      
    ll_cache:u         | 6962641   | 7161311   | 7261646  
    ll_cache_miss:u    | 25561     | 10276     | 22081    

== combo_049_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p512_np2_l2             
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l2_sp17
    s2 | hot_b128_bp3_r100_lin_p512_np4_l4              
    s3 | itlb_f64_l1_r100_lstr_p128_np4_l2_sl5          
single_counts:
    metric             | s0       | s1       | s2        | s3      
    -------------------+----------+----------+-----------+---------
    cpu-cycles:u       | 66810962 | 70318017 | 184354435 | 73553736
    instructions:u     | 13590988 | 18870997 | 26000988  | 11930988
    br_retired:u       | 1031403  | 1991404  | 3941403   | 731403  
    br_mis_pred:u      | 130695   | 591244   | 486       | 496     
    l1i_cache:u        | 3604390  | 9221053  | 3339742   | 1591899 
    l1i_cache_refill:u | 689      | 727      | 1348      | 1626776 
    l1i_tlb:u          | 3604390  | 9221053  | 3339742   | 1591899 
    l1i_tlb_refill:u   | 37       | 56       | 47        | 660085  
    l2i_cache:u        | 687      | 727      | 1347      | 1626774 
    l2i_cache_refill:u | 588      | 652      | 799       | 115111  
    l2i_tlb:u          | 75       | 120      | 77        | 660160  
    l2i_tlb_refill:u   | 19       | 44       | 19        | 40      
    l1d_cache:u        | 2176432  | 4641768  | 5256548   | 1415496 
    l1d_cache_refill:u | 1024503  | 1207214  | 1563393   | 1234293 
    l1d_tlb:u          | 2954413  | 7811398  | 7422799   | 2797365 
    l1d_tlb_refill:u   | 660063   | 1301181  | 1300062   | 1303303 
    l2d_cache:u        | 5652939  | 3885043  | 17871092  | 5600800 
    l2d_cache_refill:u | 2730575  | 955705   | 8508483   | 1627297 
    l2d_tlb:u          | 660094   | 1302542  | 1300235   | 1303351 
    l2d_tlb_refill:u   | 549      | 162      | 545       | 127     
    ll_cache:u         | 2729606  | 954975   | 8506663   | 1461897 
    ll_cache_miss:u    | 104233   | 2205     | 13801     | 4422    
combined_orders:
    id        | modules                                                                                                                                                   
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p512_np2_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l2_sp17+hot_b128_bp3_r100_lin_p512_np4_l4+itlb_f64_l1_r100_lstr_p128_np4_l2_sl5
    shuffle   | hot_b128_bp3_r100_lin_p512_np4_l4+itlb_f64_l1_r100_lstr_p128_np4_l2_sl5+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l2_sp17+cold_b64_d4_bitrev_lin_p512_np2_l2
    sum       | cold_b64_d4_bitrev_lin_p512_np2_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l2_sp17+hot_b128_bp3_r100_lin_p512_np4_l4+itlb_f64_l1_r100_lstr_p128_np4_l2_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 447653869 | 476399910 | 395037150
    instructions:u     | 70361842  | 70361848  | 70393961 
    br_retired:u       | 7691992   | 7691990   | 7695613  
    br_mis_pred:u      | 725512    | 722779    | 722921   
    l1i_cache:u        | 17183662  | 17066837  | 17757084 
    l1i_cache_refill:u | 1086481   | 1007876   | 1629540  
    l1i_tlb:u          | 17183662  | 17066837  | 17757084 
    l1i_tlb_refill:u   | 660743    | 660750    | 660225   
    l2i_cache:u        | 1086480   | 1007876   | 1629535  
    l2i_cache_refill:u | 113515    | 81812     | 117150   
    l2i_tlb:u          | 663501    | 660866    | 660432   
    l2i_tlb_refill:u   | 5813      | 3974      | 122      
    l1d_cache:u        | 13538241  | 13509453  | 13490244 
    l1d_cache_refill:u | 5039948   | 5056560   | 5029403  
    l1d_tlb:u          | 21271880  | 21150377  | 20985975 
    l1d_tlb_refill:u   | 4583987   | 4566064   | 4564609  
    l2d_cache:u        | 33981435  | 34023998  | 33009874 
    l2d_cache_refill:u | 14090175  | 14111236  | 13822060 
    l2d_tlb:u          | 4595019   | 4568081   | 4566222  
    l2d_tlb_refill:u   | 77502     | 78903     | 1383     
    ll_cache:u         | 13971278  | 14052227  | 13653141 
    ll_cache_miss:u    | 216406    | 221075    | 124661   

== combo_050_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p128_np4_l2_sl9       
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p512_np1_l1_sp33
    s2 | hot_b64_bp3_r100_lin_p128_np4_l4               
    s3 | itlb_f64_l1_r100_lstr_p128_np4_l2_sl5          
single_counts:
    metric             | s0        | s1       | s2       | s3      
    -------------------+-----------+----------+----------+---------
    cpu-cycles:u       | 166423868 | 51041972 | 44792044 | 59778613
    instructions:u     | 26870994  | 18230997 | 13200988 | 11930988
    br_retired:u       | 1991401   | 1991404  | 2021403  | 731403  
    br_mis_pred:u      | 290687    | 593179   | 483      | 508     
    l1i_cache:u        | 7217319   | 9235827  | 1728331  | 1563658 
    l1i_cache_refill:u | 1265      | 651      | 680      | 1522885 
    l1i_tlb:u          | 7217319   | 9235827  | 1728331  | 1563658 
    l1i_tlb_refill:u   | 48        | 44       | 52       | 660095  
    l2i_cache:u        | 1265      | 651      | 679      | 1522882 
    l2i_cache_refill:u | 760       | 582      | 573      | 20566   
    l2i_tlb:u          | 80        | 81       | 97       | 660140  
    l2i_tlb_refill:u   | 13        | 23       | 44       | 96      
    l1d_cache:u        | 4257883   | 4010945  | 2695805  | 1415510 
    l1d_cache_refill:u | 2432698   | 633306   | 685704   | 1224268 
    l1d_tlb:u          | 7003774   | 6631632  | 3797420  | 2818819 
    l1d_tlb_refill:u   | 2596182   | 672758   | 660058   | 1305859 
    l2d_cache:u        | 7989798   | 2833729  | 5936600  | 5344863 
    l2d_cache_refill:u | 2466433   | 1381824  | 1361387  | 1337149 
    l2d_tlb:u          | 2596673   | 676879   | 660140   | 1305889 
    l2d_tlb_refill:u   | 152       | 608      | 170      | 152     
    ll_cache:u         | 2465531   | 1381034  | 1360671  | 1289769 
    ll_cache_miss:u    | 3873      | 6453     | 451      | 253     
combined_orders:
    id        | modules                                                                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p128_np4_l2_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p512_np1_l1_sp33+hot_b64_bp3_r100_lin_p128_np4_l4+itlb_f64_l1_r100_lstr_p128_np4_l2_sl5
    shuffle   | fetch_b64_d1_bp0_s16_r100_pstr_p512_np1_l1_sp33+hot_b64_bp3_r100_lin_p128_np4_l4+cold_b128_d4_bitrev_lstr_p128_np4_l2_sl9+itlb_f64_l1_r100_lstr_p128_np4_l2_sl5
    sum       | cold_b128_d4_bitrev_lstr_p128_np4_l2_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p512_np1_l1_sp33+hot_b64_bp3_r100_lin_p128_np4_l4+itlb_f64_l1_r100_lstr_p128_np4_l2_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 252395177 | 273067499 | 322036497
    instructions:u     | 70201898  | 70201989  | 70233967 
    br_retired:u       | 6732005   | 6732012   | 6735611  
    br_mis_pred:u      | 887206    | 882471    | 884857   
    l1i_cache:u        | 19133127  | 18991623  | 19745135 
    l1i_cache_refill:u | 1190277   | 1162383   | 1525481  
    l1i_tlb:u          | 19133127  | 18991623  | 19745135 
    l1i_tlb_refill:u   | 660859    | 660859    | 660239   
    l2i_cache:u        | 1190280   | 1162383   | 1525477  
    l2i_cache_refill:u | 27744     | 45286     | 22481    
    l2i_tlb:u          | 660920    | 661025    | 660398   
    l2i_tlb_refill:u   | 1848      | 3458      | 176      
    l1d_cache:u        | 12403291  | 12404898  | 12380143 
    l1d_cache_refill:u | 4959261   | 5004654   | 4975976  
    l1d_tlb:u          | 20367383  | 20164606  | 20251645 
    l1d_tlb_refill:u   | 5261692   | 5212628   | 5234857  
    l2d_cache:u        | 22660209  | 21505758  | 22104990 
    l2d_cache_refill:u | 6918778   | 5737462   | 6546793  
    l2d_tlb:u          | 5275049   | 5219327   | 5239581  
    l2d_tlb_refill:u   | 13779     | 13128     | 1082     
    ll_cache:u         | 6894419   | 5705618   | 6497005  
    ll_cache_miss:u    | 38454     | 27747     | 11030    

