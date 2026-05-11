== combo_linearity ==
source=/home/tchen/icache_test/output/combo_linearity.csv
mode=csv_render_only
errors=not_computed
layout_snapshots=not_available_from_csv
cases=100
rows=599
metrics=22
metric_set=raw

== combo_000_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | hot_b128_bp3_r100_lstr_p512_np8_l4_sl9
    s1 | itlb_f128_l1_r100_lshuf_p128_np2_l4   
single_counts:
    metric             | s0        | s1       
    -------------------+-----------+----------
    cpu-cycles:u       | 262344824 | 251801035
    instructions:u     | 26001098  | 26011007 
    br_retired:u       | 3941413   | 1371406  
    br_mis_pred:u      | 473       | 498      
    l1i_cache:u        | 3351202   | 3342333  
    l1i_cache_refill:u | 1541      | 2923718  
    l1i_tlb:u          | 3351202   | 3342333  
    l1i_tlb_refill:u   | 53        | 1310056  
    l2i_cache:u        | 1541      | 2923714  
    l2i_cache_refill:u | 909       | 2110302  
    l2i_tlb:u          | 170       | 1310094  
    l2i_tlb_refill:u   | 24        | 46       
    l1d_cache:u        | 5258998   | 5255726  
    l1d_cache_refill:u | 5122267   | 4092656  
    l1d_tlb:u          | 10527768  | 8250664  
    l1d_tlb_refill:u   | 5159239   | 2580079  
    l2d_cache:u        | 20283335  | 16495601 
    l2d_cache_refill:u | 10235816  | 5201945  
    l2d_tlb:u          | 5160243   | 2580367  
    l2d_tlb_refill:u   | 76        | 26       
    ll_cache:u         | 10234851  | 3168636  
    ll_cache_miss:u    | 1858      | 261      
combined_orders:
    id        | modules                                                                   
    ----------+---------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_lstr_p512_np8_l4_sl9+itlb_f128_l1_r100_lshuf_p128_np2_l4
    shuffle   | itlb_f128_l1_r100_lshuf_p128_np2_l4+hot_b128_bp3_r100_lstr_p512_np8_l4_sl9
    sum       | hot_b128_bp3_r100_lstr_p512_np8_l4_sl9+itlb_f128_l1_r100_lshuf_p128_np2_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 508809959 | 663368810 | 514145859
    instructions:u     | 52001242  | 52001242  | 52012105 
    br_retired:u       | 5311592   | 5311592   | 5312819  
    br_mis_pred:u      | 609       | 625       | 971      
    l1i_cache:u        | 6719175   | 6750582   | 6693535  
    l1i_cache_refill:u | 2795862   | 2937984   | 2925259  
    l1i_tlb:u          | 6719175   | 6750582   | 6693535  
    l1i_tlb_refill:u   | 1300346   | 1300395   | 1310109  
    l2i_cache:u        | 2795862   | 2937982   | 2925255  
    l2i_cache_refill:u | 2085304   | 2083117   | 2111211  
    l2i_tlb:u          | 1300407   | 1300477   | 1310264  
    l2i_tlb_refill:u   | 747       | 963       | 70       
    l1d_cache:u        | 10511412  | 10509624  | 10514724 
    l1d_cache_refill:u | 9228894   | 9243179   | 9214923  
    l1d_tlb:u          | 18641129  | 18805746  | 18778432 
    l1d_tlb_refill:u   | 7726255   | 7749197   | 7739318  
    l2d_cache:u        | 38270796  | 38545210  | 36778936 
    l2d_cache_refill:u | 16819356  | 17217395  | 15437761 
    l2d_tlb:u          | 7727171   | 7749938   | 7740610  
    l2d_tlb_refill:u   | 1326      | 3221      | 102      
    ll_cache:u         | 14644510  | 15120088  | 13403487 
    ll_cache_miss:u    | 13949     | 8782      | 2119     

== combo_001_s2 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lin_p1_np4_l4
    s1 | itlb_f128_l1_r100_pstr_p128_np1_l4_sp3  
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 60345628 | 300600580
    instructions:u     | 39990997 | 26011098 
    br_retired:u       | 3911404  | 1371413  
    br_mis_pred:u      | 1231136  | 513      
    l1i_cache:u        | 19664122 | 3327305  
    l1i_cache_refill:u | 912      | 2891186  
    l1i_tlb:u          | 19664122 | 3327305  
    l1i_tlb_refill:u   | 55       | 1310055  
    l2i_cache:u        | 911      | 2891184  
    l2i_cache_refill:u | 735      | 2094702  
    l2i_tlb:u          | 98       | 1310114  
    l2i_tlb_refill:u   | 46       | 180      
    l1d_cache:u        | 11665725 | 5255882  
    l1d_cache_refill:u | 182      | 4875405  
    l1d_tlb:u          | 15299763 | 10460563 
    l1d_tlb_refill:u   | 66       | 5140121  
    l2d_cache:u        | 1951     | 17846427 
    l2d_cache_refill:u | 1334     | 6680555  
    l2d_tlb:u          | 92       | 5140164  
    l2d_tlb_refill:u   | 35       | 22       
    ll_cache:u         | 456      | 4562435  
    ll_cache_miss:u    | 273      | 128      
combined_orders:
    id        | modules                                                                        
    ----------+--------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lin_p1_np4_l4+itlb_f128_l1_r100_pstr_p128_np1_l4_sp3
    shuffle   | itlb_f128_l1_r100_pstr_p128_np1_l4_sp3+fetch_b128_d1_bp0_s16_r100_lin_p1_np4_l4
    sum       | fetch_b128_d1_bp0_s16_r100_lin_p1_np4_l4+itlb_f128_l1_r100_pstr_p128_np1_l4_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 357008162 | 346894460 | 360946208
    instructions:u     | 65991251  | 65991251  | 66002095 
    br_retired:u       | 5281593   | 5281593   | 5282817  
    br_mis_pred:u      | 1234237   | 1231893   | 1231649  
    l1i_cache:u        | 23011045  | 23041967  | 22991427 
    l1i_cache_refill:u | 3003443   | 2981183   | 2892098  
    l1i_tlb:u          | 23011045  | 23041967  | 22991427 
    l1i_tlb_refill:u   | 1300568   | 1300561   | 1310110  
    l2i_cache:u        | 3003441   | 2981177   | 2892095  
    l2i_cache_refill:u | 2149376   | 2132903   | 2095437  
    l2i_tlb:u          | 1300676   | 1300607   | 1310212  
    l2i_tlb_refill:u   | 304       | 104       | 226      
    l1d_cache:u        | 16908372  | 16917266  | 16921607 
    l1d_cache_refill:u | 4841374   | 4863681   | 4875587  
    l1d_tlb:u          | 25755905  | 25750462  | 25760326 
    l1d_tlb_refill:u   | 5140405   | 5140428   | 5140187  
    l2d_cache:u        | 18367442  | 18903093  | 17848378 
    l2d_cache_refill:u | 7200493   | 7543022   | 6681889  
    l2d_tlb:u          | 5140618   | 5140612   | 5140256  
    l2d_tlb_refill:u   | 193       | 35        | 57       
    ll_cache:u         | 5089727   | 5048144   | 4562891  
    ll_cache_miss:u    | 18010     | 17308     | 401      

== combo_002_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | hot_b128_bp3_r100_lin_p128_np1_l1
    s1 | itlb_f64_l1_r100_rand_p16_np4_l1 
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 47864249 | 20575965
    instructions:u     | 22160997 | 11291069
    br_retired:u       | 3941404  | 731412  
    br_mis_pred:u      | 1567     | 398     
    l1i_cache:u        | 2861052  | 1500911 
    l1i_cache_refill:u | 829      | 1202128 
    l1i_tlb:u          | 2861052  | 1500911 
    l1i_tlb_refill:u   | 62       | 660063  
    l2i_cache:u        | 828      | 1202127 
    l2i_cache_refill:u | 600      | 10791   
    l2i_tlb:u          | 126      | 660100  
    l2i_tlb_refill:u   | 25       | 20      
    l1d_cache:u        | 1416206  | 775308  
    l1d_cache_refill:u | 1206511  | 10363   
    l1d_tlb:u          | 2771760  | 777178  
    l1d_tlb_refill:u   | 1300070  | 111     
    l2d_cache:u        | 3688999  | 1519520 
    l2d_cache_refill:u | 1126991  | 21588   
    l2d_tlb:u          | 1300275  | 134     
    l2d_tlb_refill:u   | 37       | 40      
    ll_cache:u         | 1126347  | 10681   
    ll_cache_miss:u    | 973      | 77      
combined_orders:
    id        | modules                                                           
    ----------+-------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_lin_p128_np1_l1+itlb_f64_l1_r100_rand_p16_np4_l1
    shuffle   | itlb_f64_l1_r100_rand_p16_np4_l1+hot_b128_bp3_r100_lin_p128_np1_l1
    sum       | hot_b128_bp3_r100_lin_p128_np1_l1+itlb_f64_l1_r100_rand_p16_np4_l1
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 85014559  | 74500625 | 68440214
    instructions:u     | 33441288  | 33441288 | 33452066
    br_retired:u       | 4671603   | 4671603  | 4672816 
    br_mis_pred:u      | 579       | 613      | 1965    
    l1i_cache:u        | 4345321   | 4375426  | 4361963 
    l1i_cache_refill:u | 1221109   | 1128493  | 1202957 
    l1i_tlb:u          | 4345321   | 4375426  | 4361963 
    l1i_tlb_refill:u   | 670260    | 670288   | 660125  
    l2i_cache:u        | 1221107   | 1128492  | 1202955 
    l2i_cache_refill:u | 12707     | 110392   | 11391   
    l2i_tlb:u          | 670431    | 670456   | 660226  
    l2i_tlb_refill:u   | 114       | 110      | 45      
    l1d_cache:u        | 2186897   | 2186759  | 2191514 
    l1d_cache_refill:u | 1254445   | 1228614  | 1216874 
    l1d_tlb:u          | 3553481   | 3587222  | 3548938 
    l1d_tlb_refill:u   | 1302112   | 1307497  | 1300181 
    l2d_cache:u        | 4869025   | 4934950  | 5208519 
    l2d_cache_refill:u | 1323889   | 1278599  | 1148579 
    l2d_tlb:u          | 1302345   | 1307737  | 1300409 
    l2d_tlb_refill:u   | 186       | 176      | 77      
    ll_cache:u         | 1311862   | 1167249  | 1137028 
    ll_cache_miss:u    | 224       | 74       | 1050    

== combo_003_s2 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | hot_b64_bp3_r100_lin_p16_np4_l1   
    s1 | itlb_f64_l1_r100_lshuf_p128_np1_l2
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 5262165  | 89550494
    instructions:u     | 11281049 | 11930997
    br_retired:u       | 2021410  | 731404  
    br_mis_pred:u      | 448      | 494     
    l1i_cache:u        | 1486143  | 1641929 
    l1i_cache_refill:u | 637      | 1382696 
    l1i_tlb:u          | 1486143  | 1641929 
    l1i_tlb_refill:u   | 51       | 660072  
    l2i_cache:u        | 635      | 1382694 
    l2i_cache_refill:u | 577      | 848496  
    l2i_tlb:u          | 96       | 660143  
    l2i_tlb_refill:u   | 37       | 114     
    l1d_cache:u        | 775223   | 1415388 
    l1d_cache_refill:u | 747      | 1263204 
    l1d_tlb:u          | 777451   | 2815961 
    l1d_tlb_refill:u   | 94       | 1306551 
    l2d_cache:u        | 2637     | 5586513 
    l2d_cache_refill:u | 1099     | 2509086 
    l2d_tlb:u          | 115      | 1306573 
    l2d_tlb_refill:u   | 44       | 23      
    ll_cache:u         | 506      | 1827040 
    ll_cache_miss:u    | 57       | 65      
combined_orders:
    id        | modules                                                           
    ----------+-------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_lin_p16_np4_l1+itlb_f64_l1_r100_lshuf_p128_np1_l2
    shuffle   | itlb_f64_l1_r100_lshuf_p128_np1_l2+hot_b64_bp3_r100_lin_p16_np4_l1
    sum       | hot_b64_bp3_r100_lin_p16_np4_l1+itlb_f64_l1_r100_lshuf_p128_np1_l2
combined_counts:
    metric             | canonical | shuffle   | sum     
    -------------------+-----------+-----------+---------
    cpu-cycles:u       | 114596488 | 134556879 | 94812659
    instructions:u     | 23201294  | 23201288  | 23212046
    br_retired:u       | 2751601   | 2751603   | 2752814 
    br_mis_pred:u      | 610       | 549       | 942     
    l1i_cache:u        | 3110311   | 3110510   | 3128072 
    l1i_cache_refill:u | 992324    | 1061706   | 1383333 
    l1i_tlb:u          | 3110311   | 3110510   | 3128072 
    l1i_tlb_refill:u   | 670166    | 670167    | 660123  
    l2i_cache:u        | 992326    | 1061705   | 1383329 
    l2i_cache_refill:u | 690407    | 750930    | 849073  
    l2i_tlb:u          | 670206    | 670295    | 660239  
    l2i_tlb_refill:u   | 81        | 25        | 151     
    l1d_cache:u        | 2185958   | 2185892   | 2190611 
    l1d_cache_refill:u | 1272454   | 1232968   | 1263951 
    l1d_tlb:u          | 3571385   | 3594547   | 3593412 
    l1d_tlb_refill:u   | 1305720   | 1307781   | 1306645 
    l2d_cache:u        | 5294046   | 5255616   | 5589150 
    l2d_cache_refill:u | 2396122   | 2228368   | 2510185 
    l2d_tlb:u          | 1305757   | 1307829   | 1306688 
    l2d_tlb_refill:u   | 40        | 32        | 67      
    ll_cache:u         | 1733100   | 1632034   | 1827546 
    ll_cache_miss:u    | 2068      | 4316      | 122     

== combo_004_s2 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p16_np4_l1_sp33       
    s1 | fetch_b64_d1_bp0_s16_r100_lstr_p128_np4_l2_sl9
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 9346741  | 63413486
    instructions:u     | 12951049 | 18870988
    br_retired:u       | 1031410  | 1991403 
    br_mis_pred:u      | 130376   | 594722  
    l1i_cache:u        | 3718597  | 8664831 
    l1i_cache_refill:u | 622      | 773     
    l1i_tlb:u          | 3718597  | 8664831 
    l1i_tlb_refill:u   | 46       | 43      
    l2i_cache:u        | 621      | 772     
    l2i_cache_refill:u | 545      | 611     
    l2i_tlb:u          | 74       | 85      
    l2i_tlb_refill:u   | 13       | 14      
    l1d_cache:u        | 1535168  | 4704657 
    l1d_cache_refill:u | 45488    | 1238991 
    l1d_tlb:u          | 1537185  | 7962222 
    l1d_tlb_refill:u   | 90       | 1307560 
    l2d_cache:u        | 102530   | 4066068 
    l2d_cache_refill:u | 1006     | 1257611 
    l2d_tlb:u          | 110      | 1308958 
    l2d_tlb_refill:u   | 4        | 21      
    ll_cache:u         | 447      | 1257009 
    ll_cache_miss:u    | 29       | 1004    
combined_orders:
    id        | modules                                                                               
    ----------+---------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p16_np4_l1_sp33+fetch_b64_d1_bp0_s16_r100_lstr_p128_np4_l2_sl9
    shuffle   | fetch_b64_d1_bp0_s16_r100_lstr_p128_np4_l2_sl9+cold_b64_d4_bitrev_pstr_p16_np4_l1_sp33
    sum       | cold_b64_d4_bitrev_pstr_p16_np4_l1_sp33+fetch_b64_d1_bp0_s16_r100_lstr_p128_np4_l2_sl9
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 65303231  | 64060938 | 72760227
    instructions:u     | 31811288  | 31811294 | 31822037
    br_retired:u       | 3021603   | 3021601  | 3022813 
    br_mis_pred:u      | 723996    | 721958   | 725098  
    l1i_cache:u        | 13258116  | 13230479 | 12383428
    l1i_cache_refill:u | 850       | 943      | 1395    
    l1i_tlb:u          | 13258116  | 13230479 | 12383428
    l1i_tlb_refill:u   | 49        | 52       | 89      
    l2i_cache:u        | 849       | 942      | 1393    
    l2i_cache_refill:u | 673       | 788      | 1156    
    l2i_tlb:u          | 88        | 84       | 159     
    l2i_tlb_refill:u   | 16        | 18       | 27      
    l1d_cache:u        | 6179368   | 6139690  | 6239825 
    l1d_cache_refill:u | 1216994   | 1268922  | 1284479 
    l1d_tlb:u          | 9418465   | 9345332  | 9499407 
    l1d_tlb_refill:u   | 1318005   | 1304312  | 1307650 
    l2d_cache:u        | 4145606   | 4023190  | 4168598 
    l2d_cache_refill:u | 1189388   | 925139   | 1258617 
    l2d_tlb:u          | 1321666   | 1306032  | 1309068 
    l2d_tlb_refill:u   | 38        | 24       | 25      
    ll_cache:u         | 1188555   | 924370   | 1257456 
    ll_cache_miss:u    | 11812     | 528      | 1033    

== combo_005_s2 ==
single_modules:
    id | module                                 
    ---+----------------------------------------
    s0 | hot_b128_bp3_r100_pstr_p512_np4_l4_sp17
    s1 | itlb_f128_l1_r100_pstr_p16_np1_l2_sp33 
single_counts:
    metric             | s0        | s1       
    -------------------+-----------+----------
    cpu-cycles:u       | 266624402 | 103768828
    instructions:u     | 26001098  | 23450997 
    br_retired:u       | 3941413   | 1371404  
    br_mis_pred:u      | 460       | 514      
    l1i_cache:u        | 3350036   | 3286408  
    l1i_cache_refill:u | 1203      | 3161669  
    l1i_tlb:u          | 3350036   | 3286408  
    l1i_tlb_refill:u   | 55        | 1310056  
    l2i_cache:u        | 1202      | 3161668  
    l2i_cache_refill:u | 767       | 971153   
    l2i_tlb:u          | 174       | 1310141  
    l2i_tlb_refill:u   | 22        | 176      
    l1d_cache:u        | 5259402   | 2695425  
    l1d_cache_refill:u | 5119714   | 72578    
    l1d_tlb:u          | 10494415  | 2697576  
    l1d_tlb_refill:u   | 5145238   | 252      
    l2d_cache:u        | 20281619  | 3683820  
    l2d_cache_refill:u | 10248141  | 1140400  
    l2d_tlb:u          | 5146251   | 274      
    l2d_tlb_refill:u   | 76        | 14       
    ll_cache:u         | 10247208  | 94998    
    ll_cache_miss:u    | 1049      | 32       
combined_orders:
    id        | modules                                                                       
    ----------+-------------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_pstr_p512_np4_l4_sp17+itlb_f128_l1_r100_pstr_p16_np1_l2_sp33
    shuffle   | itlb_f128_l1_r100_pstr_p16_np1_l2_sp33+hot_b128_bp3_r100_pstr_p512_np4_l4_sp17
    sum       | hot_b128_bp3_r100_pstr_p512_np4_l4_sp17+itlb_f128_l1_r100_pstr_p16_np1_l2_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 331740256 | 369847151 | 370393230
    instructions:u     | 49441248  | 49441242  | 49452095 
    br_retired:u       | 5311590   | 5311592   | 5312817  
    br_mis_pred:u      | 579       | 593       | 974      
    l1i_cache:u        | 6790558   | 6579647   | 6636444  
    l1i_cache_refill:u | 2966340   | 2992314   | 3162872  
    l1i_tlb:u          | 6790558   | 6579647   | 6636444  
    l1i_tlb_refill:u   | 1300356   | 1300363   | 1310111  
    l2i_cache:u        | 2966340   | 2992314   | 3162870  
    l2i_cache_refill:u | 987308    | 860743    | 971920   
    l2i_tlb:u          | 1300424   | 1300447   | 1310315  
    l2i_tlb_refill:u   | 174       | 385       | 198      
    l1d_cache:u        | 7951343   | 7949940   | 7954827  
    l1d_cache_refill:u | 5209498   | 5179172   | 5192292  
    l1d_tlb:u          | 13197919  | 13182157  | 13191991 
    l1d_tlb_refill:u   | 5148645   | 5146203   | 5145490  
    l2d_cache:u        | 23389478  | 23203254  | 23965439 
    l2d_cache_refill:u | 11326910  | 11092148  | 11388541 
    l2d_tlb:u          | 5149445   | 5146937   | 5146525  
    l2d_tlb_refill:u   | 533       | 615       | 90       
    ll_cache:u         | 10375454  | 10330341  | 10342206 
    ll_cache_miss:u    | 2652      | 9293      | 1081     

== combo_006_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | hot_b64_bp3_r100_pstr_p128_np1_l2_sp33
    s1 | itlb_f64_l1_r100_lstr_p512_np4_l2_sl9 
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 40912599 | 99219122
    instructions:u     | 11920997 | 11930997
    br_retired:u       | 2021404  | 731404  
    br_mis_pred:u      | 401      | 534     
    l1i_cache:u        | 1567871  | 1572825 
    l1i_cache_refill:u | 647      | 1157580 
    l1i_tlb:u          | 1567871  | 1572825 
    l1i_tlb_refill:u   | 44       | 660058  
    l2i_cache:u        | 646      | 1157579 
    l2i_cache_refill:u | 546      | 5245    
    l2i_tlb:u          | 81       | 660123  
    l2i_tlb_refill:u   | 16       | 241     
    l1d_cache:u        | 1416114  | 1415270 
    l1d_cache_refill:u | 1227578  | 1285507 
    l1d_tlb:u          | 2778971  | 2805376 
    l1d_tlb_refill:u   | 1300070  | 1305206 
    l2d_cache:u        | 3598704  | 6509717 
    l2d_cache_refill:u | 1034490  | 2580124 
    l2d_tlb:u          | 1300198  | 1305237 
    l2d_tlb_refill:u   | 23       | 126     
    ll_cache:u         | 1033950  | 2571824 
    ll_cache_miss:u    | 52       | 721     
combined_orders:
    id        | modules                                                                     
    ----------+-----------------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_pstr_p128_np1_l2_sp33+itlb_f64_l1_r100_lstr_p512_np4_l2_sl9
    shuffle   | itlb_f64_l1_r100_lstr_p512_np4_l2_sl9+hot_b64_bp3_r100_pstr_p128_np1_l2_sp33
    sum       | hot_b64_bp3_r100_pstr_p128_np1_l2_sp33+itlb_f64_l1_r100_lstr_p512_np4_l2_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 134680295 | 133582914 | 140131721
    instructions:u     | 23841288  | 23841288  | 23851994 
    br_retired:u       | 2751603   | 2751603   | 2752808  
    br_mis_pred:u      | 627       | 583       | 935      
    l1i_cache:u        | 3182989   | 3171580   | 3140696  
    l1i_cache_refill:u | 1018147   | 896946    | 1158227  
    l1i_tlb:u          | 3182989   | 3171580   | 3140696  
    l1i_tlb_refill:u   | 670155    | 670190    | 660102   
    l2i_cache:u        | 1018145   | 896945    | 1158225  
    l2i_cache_refill:u | 79392     | 14963     | 5791     
    l2i_tlb:u          | 670274    | 670356    | 660204   
    l2i_tlb_refill:u   | 83        | 62        | 257      
    l1d_cache:u        | 2826940   | 2827264   | 2831384  
    l1d_cache_refill:u | 2501451   | 2496308   | 2513085  
    l1d_tlb:u          | 5579616   | 5603653   | 5584347  
    l1d_tlb_refill:u   | 2604543   | 2607211   | 2605276  
    l2d_cache:u        | 9887684   | 10184216  | 10108421 
    l2d_cache_refill:u | 3955482   | 3897296   | 3614614  
    l2d_tlb:u          | 2604757   | 2607523   | 2605435  
    l2d_tlb_refill:u   | 583       | 384       | 149      
    ll_cache:u         | 3872368   | 3880362   | 3605774  
    ll_cache_miss:u    | 3455      | 2264      | 773      

== combo_007_s2 ==
single_modules:
    id | module                                 
    ---+----------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p16_np8_l2_sl9
    s1 | hot_b128_bp3_r100_pstr_p16_np4_l1_sp17 
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 25768634 | 10379134
    instructions:u     | 26871049 | 22161049
    br_retired:u       | 1991410  | 3941410 
    br_mis_pred:u      | 290640   | 382     
    l1i_cache:u        | 7828605  | 2845560 
    l1i_cache_refill:u | 862      | 665     
    l1i_tlb:u          | 7828605  | 2845560 
    l1i_tlb_refill:u   | 53       | 42      
    l2i_cache:u        | 861      | 664     
    l2i_cache_refill:u | 666      | 589     
    l2i_tlb:u          | 94       | 73      
    l2i_tlb_refill:u   | 32       | 12      
    l1d_cache:u        | 4255511  | 1415193 
    l1d_cache_refill:u | 196028   | 271     
    l1d_tlb:u          | 4257786  | 1417163 
    l1d_tlb_refill:u   | 132      | 91      
    l2d_cache:u        | 383016   | 1534    
    l2d_cache_refill:u | 1007     | 937     
    l2d_tlb:u          | 151      | 112     
    l2d_tlb_refill:u   | 8        | 5       
    ll_cache:u         | 286      | 341     
    ll_cache_miss:u    | 194      | 44      
combined_orders:
    id        | modules                                                                       
    ----------+-------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p16_np8_l2_sl9+hot_b128_bp3_r100_pstr_p16_np4_l1_sp17
    shuffle   | hot_b128_bp3_r100_pstr_p16_np4_l1_sp17+cold_b128_d4_bitrev_lstr_p16_np8_l2_sl9
    sum       | cold_b128_d4_bitrev_lstr_p16_np8_l2_sl9+hot_b128_bp3_r100_pstr_p16_np4_l1_sp17
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 35772294  | 35658841 | 36147768
    instructions:u     | 49021297  | 49021297 | 49032098
    br_retired:u       | 5931604   | 5931604  | 5932820 
    br_mis_pred:u      | 290791    | 290977   | 291022  
    l1i_cache:u        | 10097549  | 10100910 | 10674165
    l1i_cache_refill:u | 1118      | 1492     | 1527    
    l1i_tlb:u          | 10097549  | 10100910 | 10674165
    l1i_tlb_refill:u   | 51        | 50       | 95      
    l2i_cache:u        | 1118      | 1491     | 1525    
    l2i_cache_refill:u | 856       | 868      | 1255    
    l2i_tlb:u          | 86        | 89       | 167     
    l2i_tlb_refill:u   | 17        | 15       | 44      
    l1d_cache:u        | 5665647   | 5665511  | 5670704 
    l1d_cache_refill:u | 207361    | 197365   | 196299  
    l1d_tlb:u          | 5672596   | 5671778  | 5674949 
    l1d_tlb_refill:u   | 3656      | 3510     | 223     
    l2d_cache:u        | 427026    | 427078   | 384550  
    l2d_cache_refill:u | 1575      | 1653     | 1944    
    l2d_tlb:u          | 3674      | 3527     | 263     
    l2d_tlb_refill:u   | 5         | 15       | 13      
    ll_cache:u         | 738       | 803      | 627     
    ll_cache_miss:u    | 117       | 115      | 238     

== combo_008_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b128_d4_bitrev_lin_p128_np8_l1   
    s1 | itlb_f128_l1_r100_pstr_p128_np4_l4_sp3
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 31186702 | 297982551
    instructions:u     | 25590997 | 26011098 
    br_retired:u       | 1991404  | 1371413  
    br_mis_pred:u      | 290665   | 476      
    l1i_cache:u        | 7587937  | 3375728  
    l1i_cache_refill:u | 891      | 3208205  
    l1i_tlb:u          | 7587937  | 3375728  
    l1i_tlb_refill:u   | 54       | 1310072  
    l2i_cache:u        | 890      | 3208204  
    l2i_cache_refill:u | 774      | 2308612  
    l2i_tlb:u          | 101      | 1310130  
    l2i_tlb_refill:u   | 34       | 39       
    l1d_cache:u        | 2975512  | 5255506  
    l1d_cache_refill:u | 337426   | 4921718  
    l1d_tlb:u          | 3265761  | 10538789 
    l1d_tlb_refill:u   | 175061   | 5149937  
    l2d_cache:u        | 3568631  | 18743944 
    l2d_cache_refill:u | 567433   | 7639724  
    l2d_tlb:u          | 175136   | 5149999  
    l2d_tlb_refill:u   | 11       | 160      
    ll_cache:u         | 566706   | 5653031  
    ll_cache_miss:u    | 624      | 523      
combined_orders:
    id        | modules                                                                   
    ----------+---------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lin_p128_np8_l1+itlb_f128_l1_r100_pstr_p128_np4_l4_sp3
    shuffle   | itlb_f128_l1_r100_pstr_p128_np4_l4_sp3+cold_b128_d4_bitrev_lin_p128_np8_l1
    sum       | cold_b128_d4_bitrev_lin_p128_np8_l1+itlb_f128_l1_r100_pstr_p128_np4_l4_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 318250528 | 346586045 | 329169253
    instructions:u     | 51591389  | 51591242  | 51602095 
    br_retired:u       | 3361612   | 3361592   | 3362817  
    br_mis_pred:u      | 290802    | 290827    | 291141   
    l1i_cache:u        | 10417068  | 10460679  | 10963665 
    l1i_cache_refill:u | 2847623   | 2993994   | 3209096  
    l1i_tlb:u          | 10417068  | 10460679  | 10963665 
    l1i_tlb_refill:u   | 1310452   | 1310457   | 1310126  
    l2i_cache:u        | 2847623   | 2993994   | 3209094  
    l2i_cache_refill:u | 2026713   | 2159034   | 2309386  
    l2i_tlb:u          | 1310592   | 1310513   | 1310231  
    l2i_tlb_refill:u   | 41        | 84        | 73       
    l1d_cache:u        | 8245881   | 8226994   | 8231018  
    l1d_cache_refill:u | 5195013   | 5219605   | 5259144  
    l1d_tlb:u          | 13778800  | 13800951  | 13804550 
    l1d_tlb_refill:u   | 5310638   | 5328334   | 5324998  
    l2d_cache:u        | 24002358  | 22995976  | 22312575 
    l2d_cache_refill:u | 8141192   | 8064980   | 8207157  
    l2d_tlb:u          | 5311231   | 5328578   | 5325135  
    l2d_tlb_refill:u   | 406       | 299       | 171      
    ll_cache:u         | 5982044   | 5869157   | 6219737  
    ll_cache_miss:u    | 35905     | 88585     | 1147     

== combo_009_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p16_np2_l4     
    s1 | hot_b128_bp3_r100_pstr_p128_np1_l4_sp3
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 16574869 | 222747336
    instructions:u     | 14871049 | 26001007 
    br_retired:u       | 1031410  | 3941406  
    br_mis_pred:u      | 130636   | 738      
    l1i_cache:u        | 3942337  | 3338954  
    l1i_cache_refill:u | 737      | 1194     
    l1i_tlb:u          | 3942337  | 3338954  
    l1i_tlb_refill:u   | 54       | 53       
    l2i_cache:u        | 737      | 1193     
    l2i_cache_refill:u | 630      | 734      
    l2i_tlb:u          | 111      | 191      
    l2i_tlb_refill:u   | 37       | 42       
    l1d_cache:u        | 3455206  | 5258522  
    l1d_cache_refill:u | 215      | 4923965  
    l1d_tlb:u          | 3457263  | 10473024 
    l1d_tlb_refill:u   | 112      | 5142021  
    l2d_cache:u        | 1437     | 15773594 
    l2d_cache_refill:u | 890      | 5527721  
    l2d_tlb:u          | 131      | 5142533  
    l2d_tlb_refill:u   | 10       | 161      
    ll_cache:u         | 295      | 5526965  
    ll_cache_miss:u    | 72       | 413      
combined_orders:
    id        | modules                                                                 
    ----------+-------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p16_np2_l4+hot_b128_bp3_r100_pstr_p128_np1_l4_sp3
    shuffle   | hot_b128_bp3_r100_pstr_p128_np1_l4_sp3+cold_b64_d4_bitrev_lin_p16_np2_l4
    sum       | cold_b64_d4_bitrev_lin_p16_np2_l4+hot_b128_bp3_r100_pstr_p128_np1_l4_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 246125729 | 205711348 | 239322205
    instructions:u     | 40861307  | 40861297  | 40872056 
    br_retired:u       | 4971606   | 4971604   | 4972816  
    br_mis_pred:u      | 130823    | 130794    | 131374   
    l1i_cache:u        | 7094991   | 7056571   | 7281291  
    l1i_cache_refill:u | 2082      | 1768      | 1931     
    l1i_tlb:u          | 7094991   | 7056571   | 7281291  
    l1i_tlb_refill:u   | 56        | 59        | 107      
    l2i_cache:u        | 2081      | 1768      | 1930     
    l2i_cache_refill:u | 911       | 773       | 1364     
    l2i_tlb:u          | 202       | 105       | 302      
    l2i_tlb_refill:u   | 34        | 49        | 79       
    l1d_cache:u        | 8708326   | 8708466   | 8713728  
    l1d_cache_refill:u | 4968967   | 4897630   | 4924180  
    l1d_tlb:u          | 13952170  | 13926723  | 13930287 
    l1d_tlb_refill:u   | 5148162   | 5143228   | 5142133  
    l2d_cache:u        | 16588987  | 15382046  | 15775031 
    l2d_cache_refill:u | 5664073   | 5101150   | 5528611  
    l2d_tlb:u          | 5148712   | 5143811   | 5142664  
    l2d_tlb_refill:u   | 86        | 178       | 171      
    ll_cache:u         | 5663043   | 5100102   | 5527260  
    ll_cache_miss:u    | 20016     | 8249      | 485      

== combo_010_s2 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl9         
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np8_l1_sp3
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 16436234 | 43382766
    instructions:u     | 14871040 | 18230988
    br_retired:u       | 1031409  | 1991403 
    br_mis_pred:u      | 130644   | 590477  
    l1i_cache:u        | 3728297  | 8480860 
    l1i_cache_refill:u | 747      | 730     
    l1i_tlb:u          | 3728297  | 8480860 
    l1i_tlb_refill:u   | 52       | 57      
    l2i_cache:u        | 746      | 729     
    l2i_cache_refill:u | 628      | 631     
    l2i_tlb:u          | 99       | 95      
    l2i_tlb_refill:u   | 40       | 21      
    l1d_cache:u        | 3455286  | 4059537 
    l1d_cache_refill:u | 153      | 609750  
    l1d_tlb:u          | 3457362  | 6670316 
    l1d_tlb_refill:u   | 61       | 670061  
    l2d_cache:u        | 1252     | 2337302 
    l2d_cache_refill:u | 861      | 839123  
    l2d_tlb:u          | 83       | 671622  
    l2d_tlb_refill:u   | 4        | 136     
    ll_cache:u         | 253      | 838360  
    ll_cache_miss:u    | 165      | 2567    
combined_orders:
    id        | modules                                                                             
    ----------+-------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p128_np8_l1_sp3
    shuffle   | fetch_b64_d1_bp0_s16_r100_pstr_p128_np8_l1_sp3+cold_b64_d4_bitrev_lstr_p1_np2_l4_sl9
    sum       | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p128_np8_l1_sp3
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 56211197  | 56315895 | 59819000
    instructions:u     | 33091297  | 33091297 | 33102028
    br_retired:u       | 3021604   | 3021604  | 3022812 
    br_mis_pred:u      | 721872    | 721601   | 721121  
    l1i_cache:u        | 13379513  | 13292117 | 12209157
    l1i_cache_refill:u | 816       | 820      | 1477    
    l1i_tlb:u          | 13379513  | 13292117 | 12209157
    l1i_tlb_refill:u   | 49        | 51       | 109     
    l2i_cache:u        | 817       | 820      | 1475    
    l2i_cache_refill:u | 703       | 694      | 1259    
    l2i_tlb:u          | 90        | 90       | 194     
    l2i_tlb_refill:u   | 15        | 14       | 61      
    l1d_cache:u        | 7449117   | 7460642  | 7514823 
    l1d_cache_refill:u | 601732    | 600423   | 609903  
    l1d_tlb:u          | 9975654   | 10023032 | 10127678
    l1d_tlb_refill:u   | 661966    | 664568   | 670122  
    l2d_cache:u        | 2135093   | 2171390  | 2338554 
    l2d_cache_refill:u | 665133    | 676044   | 839984  
    l2d_tlb:u          | 663432    | 668652   | 671705  
    l2d_tlb_refill:u   | 139       | 7        | 140     
    ll_cache:u         | 664263    | 675307   | 838613  
    ll_cache_miss:u    | 854       | 557      | 2732    

== combo_011_s2 ==
single_modules:
    id | module                                      
    ---+---------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lshuf_p512_np8_l4
    s1 | itlb_f128_l1_r100_lstr_p512_np4_l1_sl3      
single_counts:
    metric             | s0        | s1       
    -------------------+-----------+----------
    cpu-cycles:u       | 294939957 | 114679936
    instructions:u     | 39991089  | 22170997 
    br_retired:u       | 3911412   | 1371404  
    br_mis_pred:u      | 1237749   | 462      
    l1i_cache:u        | 17719959  | 3111542  
    l1i_cache_refill:u | 1578      | 2773190  
    l1i_tlb:u          | 17719959  | 3111542  
    l1i_tlb_refill:u   | 57        | 1300066  
    l2i_cache:u        | 1576      | 2773188  
    l2i_cache_refill:u | 1062      | 762748   
    l2i_tlb:u          | 120       | 1300122  
    l2i_tlb_refill:u   | 46        | 183      
    l1d_cache:u        | 11819970  | 1415474  
    l1d_cache_refill:u | 4142795   | 1108695  
    l1d_tlb:u          | 16388335  | 2445626  
    l1d_tlb_refill:u   | 670069    | 980078   
    l2d_cache:u        | 22573343  | 7932222  
    l2d_cache_refill:u | 9865597   | 3589030  
    l2d_tlb:u          | 678876    | 980147   
    l2d_tlb_refill:u   | 77        | 137      
    ll_cache:u         | 9863848   | 2555212  
    ll_cache_miss:u    | 15340     | 701      
combined_orders:
    id        | modules                                                                            
    ----------+------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lshuf_p512_np8_l4+itlb_f128_l1_r100_lstr_p512_np4_l1_sl3
    shuffle   | itlb_f128_l1_r100_lstr_p512_np4_l1_sl3+fetch_b128_d1_bp0_s16_r100_lshuf_p512_np8_l4
    sum       | fetch_b128_d1_bp0_s16_r100_lshuf_p512_np8_l4+itlb_f128_l1_r100_lstr_p512_np4_l1_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 410059704 | 460601715 | 409619893
    instructions:u     | 62151251  | 62151251  | 62162086 
    br_retired:u       | 5281593   | 5281593   | 5282816  
    br_mis_pred:u      | 1233603   | 1232498   | 1238211  
    l1i_cache:u        | 22921366  | 22967683  | 20831501 
    l1i_cache_refill:u | 2908416   | 2817225   | 2774768  
    l1i_tlb:u          | 22921366  | 22967683  | 20831501 
    l1i_tlb_refill:u   | 1300557   | 1300543   | 1300123  
    l2i_cache:u        | 2908414   | 2817225   | 2774764  
    l2i_cache_refill:u | 965752    | 947934    | 763810   
    l2i_tlb:u          | 1300748   | 1300641   | 1300242  
    l2i_tlb_refill:u   | 9644      | 9610      | 229      
    l1d_cache:u        | 13135226  | 13139223  | 13235444 
    l1d_cache_refill:u | 5428121   | 5346120   | 5251490  
    l1d_tlb:u          | 18694711  | 18910883  | 18833961 
    l1d_tlb_refill:u   | 1650096   | 1670115   | 1650147  
    l2d_cache:u        | 30809601  | 30773816  | 30505565 
    l2d_cache_refill:u | 13803011  | 13658960  | 13454627 
    l2d_tlb:u          | 1659474   | 1680789   | 1659023  
    l2d_tlb_refill:u   | 40674     | 40369     | 214      
    ll_cache:u         | 12726320  | 12658191  | 12419060 
    ll_cache_miss:u    | 58397     | 211467    | 16041    

== combo_012_s2 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p16_np2_l2_sp17
    s1 | hot_b64_bp3_r100_lshuf_p1_np2_l4        
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 24391607 | 12973839
    instructions:u     | 26871049 | 13201049
    br_retired:u       | 1991410  | 2021410 
    br_mis_pred:u      | 290608   | 436     
    l1i_cache:u        | 7772855  | 1736347 
    l1i_cache_refill:u | 821      | 616     
    l1i_tlb:u          | 7772855  | 1736347 
    l1i_tlb_refill:u   | 48       | 46      
    l2i_cache:u        | 821      | 615     
    l2i_cache_refill:u | 693      | 565     
    l2i_tlb:u          | 78       | 70      
    l2i_tlb_refill:u   | 17       | 14      
    l1d_cache:u        | 4255465  | 2695312 
    l1d_cache_refill:u | 45277    | 140     
    l1d_tlb:u          | 4261574  | 2697419 
    l1d_tlb_refill:u   | 131      | 63      
    l2d_cache:u        | 101620   | 1234    
    l2d_cache_refill:u | 1014     | 905     
    l2d_tlb:u          | 152      | 91      
    l2d_tlb_refill:u   | 4        | 20      
    ll_cache:u         | 310      | 300     
    ll_cache_miss:u    | 105      | 103     
combined_orders:
    id        | modules                                                                  
    ----------+--------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p16_np2_l2_sp17+hot_b64_bp3_r100_lshuf_p1_np2_l4
    shuffle   | hot_b64_bp3_r100_lshuf_p1_np2_l4+cold_b128_d4_bitrev_pstr_p16_np2_l2_sp17
    sum       | cold_b128_d4_bitrev_pstr_p16_np2_l2_sp17+hot_b64_bp3_r100_lshuf_p1_np2_l4
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 36646505  | 37450776 | 37365446
    instructions:u     | 40061288  | 40061288 | 40072098
    br_retired:u       | 4011603   | 4011603  | 4012820 
    br_mis_pred:u      | 290863    | 290870   | 291044  
    l1i_cache:u        | 8860530   | 9060010  | 9509202 
    l1i_cache_refill:u | 966       | 1132     | 1437    
    l1i_tlb:u          | 8860530   | 9060010  | 9509202 
    l1i_tlb_refill:u   | 48        | 58       | 94      
    l2i_cache:u        | 966       | 1131     | 1436    
    l2i_cache_refill:u | 786       | 839      | 1258    
    l2i_tlb:u          | 84        | 105      | 148     
    l2i_tlb_refill:u   | 16        | 41       | 31      
    l1d_cache:u        | 6945550   | 6945639  | 6950777 
    l1d_cache_refill:u | 51214     | 50832    | 45417   
    l1d_tlb:u          | 6947946   | 6948071  | 6958993 
    l1d_tlb_refill:u   | 138       | 150      | 194     
    l2d_cache:u        | 94040     | 93371    | 102854  
    l2d_cache_refill:u | 1090      | 1136     | 1919    
    l2d_tlb:u          | 169       | 172      | 243     
    l2d_tlb_refill:u   | 11        | 11       | 24      
    ll_cache:u         | 326       | 326      | 610     
    ll_cache_miss:u    | 87        | 87       | 208     

== combo_013_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | hot_b64_bp3_r100_pstr_p16_np1_l1_sp33 
    s1 | itlb_f128_l1_r100_lstr_p128_np8_l2_sl3
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 5264242  | 150327640
    instructions:u     | 11281049 | 23450997 
    br_retired:u       | 2021410  | 1371404  
    br_mis_pred:u      | 406      | 483      
    l1i_cache:u        | 1485666  | 3245539  
    l1i_cache_refill:u | 600      | 2830709  
    l1i_tlb:u          | 1485666  | 3245539  
    l1i_tlb_refill:u   | 50       | 1310046  
    l2i_cache:u        | 600      | 2830705  
    l2i_cache_refill:u | 547      | 911812   
    l2i_tlb:u          | 96       | 1310095  
    l2i_tlb_refill:u   | 19       | 185      
    l1d_cache:u        | 775181   | 2695670  
    l1d_cache_refill:u | 190      | 1329090  
    l1d_tlb:u          | 777247   | 4123912  
    l1d_tlb_refill:u   | 94       | 980070   
    l2d_cache:u        | 1221     | 9128008  
    l2d_cache_refill:u | 756      | 2746666  
    l2d_tlb:u          | 113      | 980093   
    l2d_tlb_refill:u   | 6        | 32       
    ll_cache:u         | 245      | 1800306  
    ll_cache_miss:u    | 84       | 1966     
combined_orders:
    id        | modules                                                                     
    ----------+-----------------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_pstr_p16_np1_l1_sp33+itlb_f128_l1_r100_lstr_p128_np8_l2_sl3
    shuffle   | itlb_f128_l1_r100_lstr_p128_np8_l2_sl3+hot_b64_bp3_r100_pstr_p16_np1_l1_sp33
    sum       | hot_b64_bp3_r100_pstr_p16_np1_l1_sp33+itlb_f128_l1_r100_lstr_p128_np8_l2_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 144426780 | 139121571 | 155591882
    instructions:u     | 34721288  | 34721288  | 34732046 
    br_retired:u       | 3391603   | 3391603   | 3392814  
    br_mis_pred:u      | 587       | 585       | 889      
    l1i_cache:u        | 4684128   | 4647571   | 4731205  
    l1i_cache_refill:u | 2756653   | 2911565   | 2831309  
    l1i_tlb:u          | 4684128   | 4647571   | 4731205  
    l1i_tlb_refill:u   | 1310148   | 1310180   | 1310096  
    l2i_cache:u        | 2756652   | 2911564   | 2831305  
    l2i_cache_refill:u | 715226    | 840967    | 912359   
    l2i_tlb:u          | 1310184   | 1310211   | 1310191  
    l2i_tlb_refill:u   | 41        | 30        | 204      
    l1d_cache:u        | 3465878   | 3465881   | 3470851  
    l1d_cache_refill:u | 1165023   | 1197379   | 1329280  
    l1d_tlb:u          | 4935305   | 4845460   | 4901159  
    l1d_tlb_refill:u   | 981674    | 981678    | 980164   
    l2d_cache:u        | 9184452   | 9398235   | 9129229  
    l2d_cache_refill:u | 2912190   | 2899852   | 2747422  
    l2d_tlb:u          | 981710    | 981719    | 980206   
    l2d_tlb_refill:u   | 42        | 38        | 38       
    ll_cache:u         | 2095351   | 2045447   | 1800551  
    ll_cache_miss:u    | 1340      | 6403      | 2050     

== combo_014_s2 ==
single_modules:
    id | module                                 
    ---+----------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p16_np8_l4   
    s1 | hot_b128_bp3_r100_pstr_p128_np2_l2_sp17
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 35907659 | 125882596
    instructions:u     | 29430997 | 23440997 
    br_retired:u       | 1991404  | 3941404  
    br_mis_pred:u      | 290422   | 480      
    l1i_cache:u        | 8146737  | 3011722  
    l1i_cache_refill:u | 883      | 927      
    l1i_tlb:u          | 8146737  | 3011722  
    l1i_tlb_refill:u   | 47       | 56       
    l2i_cache:u        | 882      | 926      
    l2i_cache_refill:u | 712      | 683      
    l2i_tlb:u          | 73       | 93       
    l2i_tlb_refill:u   | 13       | 40       
    l1d_cache:u        | 6815477  | 2696963  
    l1d_cache_refill:u | 130922   | 2435784  
    l1d_tlb:u          | 6821480  | 5393106  
    l1d_tlb_refill:u   | 146      | 2588985  
    l2d_cache:u        | 302674   | 8042184  
    l2d_cache_refill:u | 1228     | 2853326  
    l2d_tlb:u          | 166      | 2589520  
    l2d_tlb_refill:u   | 5        | 135      
    ll_cache:u         | 470      | 2852532  
    ll_cache_miss:u    | 349      | 902      
combined_orders:
    id        | modules                                                                     
    ----------+-----------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p16_np8_l4+hot_b128_bp3_r100_pstr_p128_np2_l2_sp17
    shuffle   | hot_b128_bp3_r100_pstr_p128_np2_l2_sp17+cold_b128_d4_bitrev_lshuf_p16_np8_l4
    sum       | cold_b128_d4_bitrev_lshuf_p16_np8_l4+hot_b128_bp3_r100_pstr_p128_np2_l2_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 120558032 | 114275572 | 161790255
    instructions:u     | 52861297  | 52861303  | 52871994 
    br_retired:u       | 5931604   | 5931602   | 5932808  
    br_mis_pred:u      | 291072    | 291179    | 290902   
    l1i_cache:u        | 10517022  | 10561678  | 11158459 
    l1i_cache_refill:u | 2264      | 1811      | 1810     
    l1i_tlb:u          | 10517022  | 10561678  | 11158459 
    l1i_tlb_refill:u   | 53        | 50        | 103      
    l2i_cache:u        | 2264      | 1811      | 1808     
    l2i_cache_refill:u | 1049      | 1006      | 1395     
    l2i_tlb:u          | 88        | 91        | 166      
    l2i_tlb_refill:u   | 18        | 18        | 53       
    l1d_cache:u        | 9507120   | 9507354   | 9512440  
    l1d_cache_refill:u | 2537195   | 2529696   | 2566706  
    l1d_tlb:u          | 12207876  | 12198980  | 12214586 
    l1d_tlb_refill:u   | 2590947   | 2586405   | 2589131  
    l2d_cache:u        | 8776793   | 9004908   | 8344858  
    l2d_cache_refill:u | 2138536   | 2279134   | 2854554  
    l2d_tlb:u          | 2591281   | 2586641   | 2589686  
    l2d_tlb_refill:u   | 151       | 24        | 140      
    ll_cache:u         | 2137386   | 2278145   | 2853002  
    ll_cache_miss:u    | 6657      | 4086      | 1251     

== combo_015_s2 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p16_np2_l4_sp17
    s1 | hot_b64_bp3_r100_lstr_p128_np8_l4_sl9   
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 34554835 | 78363094
    instructions:u     | 29430997 | 13200997
    br_retired:u       | 1991404  | 2021404 
    br_mis_pred:u      | 290627   | 475     
    l1i_cache:u        | 8068268  | 1730013 
    l1i_cache_refill:u | 925      | 722     
    l1i_tlb:u          | 8068268  | 1730013 
    l1i_tlb_refill:u   | 48       | 47      
    l2i_cache:u        | 924      | 722     
    l2i_cache_refill:u | 701      | 579     
    l2i_tlb:u          | 85       | 86      
    l2i_tlb_refill:u   | 14       | 13      
    l1d_cache:u        | 6815462  | 2696714 
    l1d_cache_refill:u | 50235    | 2450254 
    l1d_tlb:u          | 6817626  | 5348499 
    l1d_tlb_refill:u   | 126      | 2582597 
    l2d_cache:u        | 91619    | 7680404 
    l2d_cache_refill:u | 996      | 2552764 
    l2d_tlb:u          | 142      | 2582941 
    l2d_tlb_refill:u   | 8        | 130     
    ll_cache:u         | 306      | 2552109 
    ll_cache_miss:u    | 58       | 780     
combined_orders:
    id        | modules                                                                       
    ----------+-------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p16_np2_l4_sp17+hot_b64_bp3_r100_lstr_p128_np8_l4_sl9
    shuffle   | hot_b64_bp3_r100_lstr_p128_np8_l4_sl9+cold_b128_d4_bitrev_pstr_p16_np2_l4_sp17
    sum       | cold_b128_d4_bitrev_pstr_p16_np2_l4_sp17+hot_b64_bp3_r100_lstr_p128_np8_l4_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 161636065 | 120641601 | 112917929
    instructions:u     | 42621297  | 42621297  | 42631994 
    br_retired:u       | 4011604   | 4011604   | 4012808  
    br_mis_pred:u      | 291029    | 292860    | 291102   
    l1i_cache:u        | 9242621   | 9252175   | 9798281  
    l1i_cache_refill:u | 1905      | 1311      | 1647     
    l1i_tlb:u          | 9242621   | 9252175   | 9798281  
    l1i_tlb_refill:u   | 61        | 50        | 95       
    l2i_cache:u        | 1904      | 1310      | 1646     
    l2i_cache_refill:u | 1064      | 936       | 1280     
    l2i_tlb:u          | 95        | 86        | 171      
    l2i_tlb_refill:u   | 18        | 19        | 27       
    l1d_cache:u        | 9507522   | 9507103   | 9512176  
    l1d_cache_refill:u | 2441979   | 2494881   | 2500489  
    l1d_tlb:u          | 12181511  | 12175616  | 12166125 
    l1d_tlb_refill:u   | 2584254   | 2584314   | 2582723  
    l2d_cache:u        | 7645823   | 8022386   | 7772023  
    l2d_cache_refill:u | 2360776   | 2601497   | 2553760  
    l2d_tlb:u          | 2584663   | 2584561   | 2583083  
    l2d_tlb_refill:u   | 128       | 55        | 138      
    ll_cache:u         | 2359610   | 2600352   | 2552415  
    ll_cache_miss:u    | 2546      | 9362      | 838      

== combo_016_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | hot_b128_bp3_r100_lshuf_p128_np8_l2   
    s1 | itlb_f128_l1_r100_lstr_p512_np8_l1_sl9
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 47835794 | 151905265
    instructions:u     | 23440997 | 22170997 
    br_retired:u       | 3941404  | 1371404  
    br_mis_pred:u      | 461      | 512      
    l1i_cache:u        | 3009957  | 3007931  
    l1i_cache_refill:u | 724      | 2729150  
    l1i_tlb:u          | 3009957  | 3007931  
    l1i_tlb_refill:u   | 40       | 1300065  
    l2i_cache:u        | 724      | 2729150  
    l2i_cache_refill:u | 605      | 463298   
    l2i_tlb:u          | 93       | 1300131  
    l2i_tlb_refill:u   | 17       | 202      
    l1d_cache:u        | 2695865  | 1415988  
    l1d_cache_refill:u | 1402952  | 1290265  
    l1d_tlb:u          | 3272908  | 2849463  
    l1d_tlb_refill:u   | 340059   | 1320067  
    l2d_cache:u        | 6979855  | 8093912  
    l2d_cache_refill:u | 882849   | 3234530  
    l2d_tlb:u          | 340090   | 1320099  
    l2d_tlb_refill:u   | 62       | 187      
    ll_cache:u         | 882094   | 2569844  
    ll_cache_miss:u    | 2356     | 5429     
combined_orders:
    id        | modules                                                                   
    ----------+---------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_lshuf_p128_np8_l2+itlb_f128_l1_r100_lstr_p512_np8_l1_sl9
    shuffle   | itlb_f128_l1_r100_lstr_p512_np8_l1_sl9+hot_b128_bp3_r100_lshuf_p128_np8_l2
    sum       | hot_b128_bp3_r100_lshuf_p128_np8_l2+itlb_f128_l1_r100_lstr_p512_np8_l1_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 203064081 | 186763874 | 199741059
    instructions:u     | 45601294  | 45601288  | 45611994 
    br_retired:u       | 5311601   | 5311603   | 5312808  
    br_mis_pred:u      | 600       | 577       | 973      
    l1i_cache:u        | 6109347   | 6088156   | 6017888  
    l1i_cache_refill:u | 2755197   | 2851731   | 2729874  
    l1i_tlb:u          | 6109347   | 6088156   | 6017888  
    l1i_tlb_refill:u   | 1300350   | 1300354   | 1300105  
    l2i_cache:u        | 2755197   | 2851729   | 2729874  
    l2i_cache_refill:u | 729444    | 932363    | 463903   
    l2i_tlb:u          | 1300405   | 1300426   | 1300224  
    l2i_tlb_refill:u   | 245       | 513       | 219      
    l1d_cache:u        | 4107237   | 4106714   | 4111853  
    l1d_cache_refill:u | 2757605   | 2754422   | 2693217  
    l1d_tlb:u          | 6028808   | 6054779   | 6122371  
    l1d_tlb_refill:u   | 1644559   | 1645016   | 1660126  
    l2d_cache:u        | 16227003  | 16480527  | 15073767 
    l2d_cache_refill:u | 5256064   | 5664292   | 4117379  
    l2d_tlb:u          | 1644622   | 1645058   | 1660189  
    l2d_tlb_refill:u   | 1385      | 1550      | 249      
    ll_cache:u         | 4569836   | 4619375   | 3451938  
    ll_cache_miss:u    | 18092     | 287173    | 7785     

== combo_017_s2 ==
single_modules:
    id | module                                 
    ---+----------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p16_np8_l1_sl5
    s1 | itlb_f128_l1_r100_lstr_p1_np4_l2_sl9   
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 19750130 | 92690990
    instructions:u     | 25591049 | 23450988
    br_retired:u       | 1991410  | 1371403 
    br_mis_pred:u      | 290621   | 468     
    l1i_cache:u        | 7667765  | 3304511 
    l1i_cache_refill:u | 817      | 2862751 
    l1i_tlb:u          | 7667765  | 3304511 
    l1i_tlb_refill:u   | 49       | 1310062 
    l2i_cache:u        | 815      | 2862748 
    l2i_cache_refill:u | 707      | 599026  
    l2i_tlb:u          | 97       | 1310099 
    l2i_tlb_refill:u   | 15       | 24      
    l1d_cache:u        | 2975348  | 2695240 
    l1d_cache_refill:u | 193610   | 6824    
    l1d_tlb:u          | 2977539  | 2697055 
    l1d_tlb_refill:u   | 115      | 64      
    l2d_cache:u        | 459211   | 3494314 
    l2d_cache_refill:u | 1236     | 851775  
    l2d_tlb:u          | 135      | 86      
    l2d_tlb_refill:u   | 7        | 8       
    ll_cache:u         | 544      | 6949    
    ll_cache_miss:u    | 84       | 25      
combined_orders:
    id        | modules                                                                     
    ----------+-----------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p16_np8_l1_sl5+itlb_f128_l1_r100_lstr_p1_np4_l2_sl9
    shuffle   | itlb_f128_l1_r100_lstr_p1_np4_l2_sl9+cold_b128_d4_bitrev_lstr_p16_np8_l1_sl5
    sum       | cold_b128_d4_bitrev_lstr_p16_np8_l1_sl5+itlb_f128_l1_r100_lstr_p1_np4_l2_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 101194237 | 103693624 | 112441120
    instructions:u     | 49031288  | 49031294  | 49042037 
    br_retired:u       | 3361603   | 3361601   | 3362813  
    br_mis_pred:u      | 290794    | 290773    | 291089   
    l1i_cache:u        | 10359491  | 10291562  | 10972276 
    l1i_cache_refill:u | 3463150   | 3301089   | 2863568  
    l1i_tlb:u          | 10359491  | 10291562  | 10972276 
    l1i_tlb_refill:u   | 1310518   | 1310451   | 1310111  
    l2i_cache:u        | 3463151   | 3301087   | 2863563  
    l2i_cache_refill:u | 756550    | 835472    | 599733   
    l2i_tlb:u          | 1310695   | 1310485   | 1310196  
    l2i_tlb_refill:u   | 174       | 29        | 39       
    l1d_cache:u        | 5665673   | 5665826   | 5670588  
    l1d_cache_refill:u | 163839    | 168268    | 200434   
    l1d_tlb:u          | 5668032   | 5668976   | 5674594  
    l1d_tlb_refill:u   | 267       | 278       | 179      
    l2d_cache:u        | 4600091   | 4339461   | 3953525  
    l2d_cache_refill:u | 713071    | 657201    | 853011   
    l2d_tlb:u          | 291       | 303       | 221      
    l2d_tlb_refill:u   | 48        | 48        | 15       
    ll_cache:u         | 13149     | 4493      | 7493     
    ll_cache_miss:u    | 119       | 203       | 109      

== combo_018_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | hot_b128_bp3_r100_lstr_p512_np1_l2_sl3
    s1 | itlb_f128_l1_r100_lstr_p512_np4_l1_sl3
single_counts:
    metric             | s0        | s1       
    -------------------+-----------+----------
    cpu-cycles:u       | 126108998 | 144799276
    instructions:u     | 23440997  | 22170997 
    br_retired:u       | 3941404   | 1371404  
    br_mis_pred:u      | 480       | 512      
    l1i_cache:u        | 3018684   | 3124190  
    l1i_cache_refill:u | 924       | 2752876  
    l1i_tlb:u          | 3018684   | 3124190  
    l1i_tlb_refill:u   | 51        | 1300054  
    l2i_cache:u        | 924       | 2752877  
    l2i_cache_refill:u | 714       | 766811   
    l2i_tlb:u          | 179       | 1300110  
    l2i_tlb_refill:u   | 43        | 156      
    l1d_cache:u        | 2697168   | 1415663  
    l1d_cache_refill:u | 2560040   | 1109137  
    l1d_tlb:u          | 5365105   | 2465291  
    l1d_tlb_refill:u   | 2584726   | 980078   
    l2d_cache:u        | 10181117  | 7778407  
    l2d_cache_refill:u | 5123875   | 3391037  
    l2d_tlb:u          | 2585225   | 980112   
    l2d_tlb_refill:u   | 547       | 154      
    ll_cache:u         | 5123146   | 2540756  
    ll_cache_miss:u    | 85        | 830      
combined_orders:
    id        | modules                                                                      
    ----------+------------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_lstr_p512_np1_l2_sl3+itlb_f128_l1_r100_lstr_p512_np4_l1_sl3
    shuffle   | itlb_f128_l1_r100_lstr_p512_np4_l1_sl3+hot_b128_bp3_r100_lstr_p512_np1_l2_sl3
    sum       | hot_b128_bp3_r100_lstr_p512_np1_l2_sl3+itlb_f128_l1_r100_lstr_p512_np4_l1_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 305047443 | 395902284 | 270908274
    instructions:u     | 45601389  | 45601248  | 45611994 
    br_retired:u       | 5311612   | 5311590   | 5312808  
    br_mis_pred:u      | 594       | 610       | 992      
    l1i_cache:u        | 6208077   | 6159628   | 6142874  
    l1i_cache_refill:u | 2827367   | 2842961   | 2753800  
    l1i_tlb:u          | 6208077   | 6159628   | 6142874  
    l1i_tlb_refill:u   | 1300346   | 1300356   | 1300105  
    l2i_cache:u        | 2827366   | 2842959   | 2753801  
    l2i_cache_refill:u | 971925    | 895691    | 767525   
    l2i_tlb:u          | 1300391   | 1300441   | 1300289  
    l2i_tlb_refill:u   | 9361      | 8867      | 199      
    l1d_cache:u        | 4109509   | 4110090   | 4112831  
    l1d_cache_refill:u | 3742321   | 3746751   | 3669177  
    l1d_tlb:u          | 7865409   | 7926910   | 7830396  
    l1d_tlb_refill:u   | 3565179   | 3565459   | 3564804  
    l2d_cache:u        | 17997057  | 18033250  | 17959524 
    l2d_cache_refill:u | 8656056   | 8504198   | 8514912  
    l2d_tlb:u          | 3565698   | 3566092   | 3565337  
    l2d_tlb_refill:u   | 40047     | 39543     | 701      
    ll_cache:u         | 7682869   | 7681712   | 7663902  
    ll_cache_miss:u    | 12305     | 21933     | 915      

== combo_019_s2 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p128_np4_l1_sl9        
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l4_sp17
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 29197046 | 194151740
    instructions:u     | 12950997 | 20150988 
    br_retired:u       | 1031404  | 1991403  
    br_mis_pred:u      | 130639   | 597633   
    l1i_cache:u        | 3735340  | 8911040  
    l1i_cache_refill:u | 673      | 711      
    l1i_tlb:u          | 3735340  | 8911040  
    l1i_tlb_refill:u   | 41       | 46       
    l2i_cache:u        | 673      | 710      
    l2i_cache_refill:u | 589      | 643      
    l2i_tlb:u          | 73       | 91       
    l2i_tlb_refill:u   | 14       | 22       
    l1d_cache:u        | 1536006  | 5990147  
    l1d_cache_refill:u | 611241   | 2530712  
    l1d_tlb:u          | 2288708  | 10545703 
    l1d_tlb_refill:u   | 660581   | 2590053  
    l2d_cache:u        | 1951585  | 11124213 
    l2d_cache_refill:u | 581814   | 5511619  
    l2d_tlb:u          | 661255   | 2591531  
    l2d_tlb_refill:u   | 145      | 547      
    ll_cache:u         | 581113   | 5510644  
    ll_cache_miss:u    | 9708     | 237241   
combined_orders:
    id        | modules                                                                                
    ----------+----------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p128_np4_l1_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l4_sp17
    shuffle   | fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l4_sp17+cold_b64_d4_bitrev_lstr_p128_np4_l1_sl9
    sum       | cold_b64_d4_bitrev_lstr_p128_np4_l1_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l4_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 239566106 | 238151217 | 223348786
    instructions:u     | 33091298  | 33091298  | 33101985 
    br_retired:u       | 3021605   | 3021605   | 3022807  
    br_mis_pred:u      | 721839    | 722771    | 728272   
    l1i_cache:u        | 13359596  | 13457476  | 12646380 
    l1i_cache_refill:u | 1010      | 1202      | 1384     
    l1i_tlb:u          | 13359596  | 13457476  | 12646380 
    l1i_tlb_refill:u   | 47        | 50        | 87       
    l2i_cache:u        | 1009      | 1201      | 1383     
    l2i_cache_refill:u | 752       | 891       | 1232     
    l2i_tlb:u          | 92        | 84        | 164      
    l2i_tlb_refill:u   | 26        | 27        | 36       
    l1d_cache:u        | 7489699   | 7508809   | 7526153  
    l1d_cache_refill:u | 3120601   | 3135595   | 3141953  
    l1d_tlb:u          | 12818011  | 12862383  | 12834411 
    l1d_tlb_refill:u   | 3262272   | 3263623   | 3250634  
    l2d_cache:u        | 13699180  | 13512893  | 13075798 
    l2d_cache_refill:u | 6340377   | 6252518   | 6093433  
    l2d_tlb:u          | 3274324   | 3274655   | 3252786  
    l2d_tlb_refill:u   | 210       | 182       | 692      
    ll_cache:u         | 6339155   | 6252401   | 6091757  
    ll_cache_miss:u    | 115058    | 111248    | 246949   

== combo_020_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b128_d4_bitrev_rand_p16_np4_l1   
    s1 | itlb_f128_l1_r100_lstr_p128_np4_l2_sl3
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 19534980 | 142652693
    instructions:u     | 25591049 | 23450997 
    br_retired:u       | 1991410  | 1371404  
    br_mis_pred:u      | 290602   | 502      
    l1i_cache:u        | 7632800  | 3319288  
    l1i_cache_refill:u | 796      | 3028482  
    l1i_tlb:u          | 7632800  | 3319288  
    l1i_tlb_refill:u   | 50       | 1310062  
    l2i_cache:u        | 794      | 3028479  
    l2i_cache_refill:u | 694      | 1519428  
    l2i_tlb:u          | 84       | 1310128  
    l2i_tlb_refill:u   | 13       | 141      
    l1d_cache:u        | 2975443  | 2695402  
    l1d_cache_refill:u | 89076    | 1986427  
    l1d_tlb:u          | 2977779  | 5088667  
    l1d_tlb_refill:u   | 111      | 1940071  
    l2d_cache:u        | 217996   | 10366598 
    l2d_cache_refill:u | 1376     | 4101351  
    l2d_tlb:u          | 136      | 1940175  
    l2d_tlb_refill:u   | 55       | 26       
    ll_cache:u         | 561      | 2583338  
    ll_cache_miss:u    | 57       | 261      
combined_orders:
    id        | modules                                                                   
    ----------+---------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_rand_p16_np4_l1+itlb_f128_l1_r100_lstr_p128_np4_l2_sl3
    shuffle   | itlb_f128_l1_r100_lstr_p128_np4_l2_sl3+cold_b128_d4_bitrev_rand_p16_np4_l1
    sum       | cold_b128_d4_bitrev_rand_p16_np4_l1+itlb_f128_l1_r100_lstr_p128_np4_l2_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 161520617 | 216390192 | 162187673
    instructions:u     | 49031288  | 49031313  | 49042046 
    br_retired:u       | 3361603   | 3361604   | 3362814  
    br_mis_pred:u      | 290824    | 290854    | 291104   
    l1i_cache:u        | 10405936  | 10420921  | 10952088 
    l1i_cache_refill:u | 3002367   | 3028175   | 3029278  
    l1i_tlb:u          | 10405936  | 10420921  | 10952088 
    l1i_tlb_refill:u   | 1310490   | 1310452   | 1310112  
    l2i_cache:u        | 3002366   | 3028173   | 3029273  
    l2i_cache_refill:u | 1506073   | 1515897   | 1520122  
    l2i_tlb:u          | 1310637   | 1310583   | 1310212  
    l2i_tlb_refill:u   | 180       | 45        | 154      
    l1d_cache:u        | 5665968   | 5666264   | 5670845  
    l1d_cache_refill:u | 2238931   | 2245302   | 2075503  
    l1d_tlb:u          | 7939358   | 7890397   | 8066446  
    l1d_tlb_refill:u   | 1942013   | 1941920   | 1940182  
    l2d_cache:u        | 11884633  | 11731564  | 10584594 
    l2d_cache_refill:u | 4414615   | 4198056   | 4102727  
    l2d_tlb:u          | 1942224   | 1942179   | 1940311  
    l2d_tlb_refill:u   | 222       | 176       | 81       
    ll_cache:u         | 2806158   | 2697886   | 2583899  
    ll_cache_miss:u    | 1880      | 15290     | 318      

== combo_021_s2 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p128_np8_l1_sl9
    s1 | hot_b64_bp3_r100_lstr_p16_np8_l1_sl9    
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 57877021 | 5341233 
    instructions:u     | 25590997 | 11281049
    br_retired:u       | 1991404  | 2021410 
    br_mis_pred:u      | 290651   | 400     
    l1i_cache:u        | 7619672  | 1485649 
    l1i_cache_refill:u | 1029     | 602     
    l1i_tlb:u          | 7619672  | 1485649 
    l1i_tlb_refill:u   | 48       | 53      
    l2i_cache:u        | 1028     | 602     
    l2i_cache_refill:u | 769      | 562     
    l2i_tlb:u          | 75       | 97      
    l2i_tlb_refill:u   | 18       | 16      
    l1d_cache:u        | 2978938  | 775231  
    l1d_cache_refill:u | 1239593  | 1089    
    l1d_tlb:u          | 4453232  | 777255  
    l1d_tlb_refill:u   | 1320064  | 92      
    l2d_cache:u        | 4200041  | 3325    
    l2d_cache_refill:u | 1422132  | 1082    
    l2d_tlb:u          | 1322553  | 165     
    l2d_tlb_refill:u   | 20       | 3       
    ll_cache:u         | 1421342  | 550     
    ll_cache_miss:u    | 7278     | 78      
combined_orders:
    id        | modules                                                                      
    ----------+------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p128_np8_l1_sl9+hot_b64_bp3_r100_lstr_p16_np8_l1_sl9
    shuffle   | hot_b64_bp3_r100_lstr_p16_np8_l1_sl9+cold_b128_d4_bitrev_lstr_p128_np8_l1_sl9
    sum       | cold_b128_d4_bitrev_lstr_p128_np8_l1_sl9+hot_b64_bp3_r100_lstr_p16_np8_l1_sl9
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 58397658  | 57625131 | 63218254
    instructions:u     | 36861297  | 36861297 | 36872046
    br_retired:u       | 4011604   | 4011604  | 4012814 
    br_mis_pred:u      | 290580    | 291086   | 291051  
    l1i_cache:u        | 8589509   | 8506272  | 9105321 
    l1i_cache_refill:u | 1009      | 1021     | 1631    
    l1i_tlb:u          | 8589509   | 8506272  | 9105321 
    l1i_tlb_refill:u   | 53        | 53       | 101     
    l2i_cache:u        | 1009      | 1020     | 1630    
    l2i_cache_refill:u | 802       | 803      | 1331    
    l2i_tlb:u          | 191       | 90       | 172     
    l2i_tlb_refill:u   | 17        | 14       | 34      
    l1d_cache:u        | 3756978   | 3748210  | 3754169 
    l1d_cache_refill:u | 1250298   | 1266087  | 1240682 
    l1d_tlb:u          | 5272013   | 5157061  | 5230487 
    l1d_tlb_refill:u   | 1321034   | 1303198  | 1320156 
    l2d_cache:u        | 4306226   | 4164519  | 4203366 
    l2d_cache_refill:u | 1447461   | 1292406  | 1423214 
    l2d_tlb:u          | 1324010   | 1306502  | 1322718 
    l2d_tlb_refill:u   | 147       | 10       | 23      
    ll_cache:u         | 1446455   | 1291607  | 1421892 
    ll_cache_miss:u    | 2225      | 319      | 7356    

== combo_022_s2 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_pstr_p16_np1_l4_sp33
    s1 | itlb_f128_l1_r100_lshuf_p16_np1_l4             
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 58875412 | 116657019
    instructions:u     | 39990988 | 26010997 
    br_retired:u       | 3911403  | 1371404  
    br_mis_pred:u      | 1231391  | 486      
    l1i_cache:u        | 17245132 | 3569160  
    l1i_cache_refill:u | 919      | 3237861  
    l1i_tlb:u          | 17245132 | 3569160  
    l1i_tlb_refill:u   | 49       | 1310082  
    l2i_cache:u        | 919      | 3237855  
    l2i_cache_refill:u | 717      | 1226658  
    l2i_tlb:u          | 82       | 1310151  
    l2i_tlb_refill:u   | 12       | 29       
    l1d_cache:u        | 11700471 | 5255335  
    l1d_cache_refill:u | 50698    | 67633    
    l1d_tlb:u          | 15352477 | 5257405  
    l1d_tlb_refill:u   | 200      | 291      
    l2d_cache:u        | 102820   | 3675693  
    l2d_cache_refill:u | 929      | 1560400  
    l2d_tlb:u          | 228      | 322      
    l2d_tlb_refill:u   | 7        | 52       
    ll_cache:u         | 244      | 112585   
    ll_cache_miss:u    | 5        | 26       
combined_orders:
    id        | modules                                                                           
    ----------+-----------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_pstr_p16_np1_l4_sp33+itlb_f128_l1_r100_lshuf_p16_np1_l4
    shuffle   | itlb_f128_l1_r100_lshuf_p16_np1_l4+fetch_b128_d1_bp0_s16_r100_pstr_p16_np1_l4_sp33
    sum       | fetch_b128_d1_bp0_s16_r100_pstr_p16_np1_l4_sp33+itlb_f128_l1_r100_lshuf_p16_np1_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 170860149 | 168825460 | 175532431
    instructions:u     | 65991297  | 65991297  | 66001985 
    br_retired:u       | 5281604   | 5281604   | 5282807  
    br_mis_pred:u      | 1231882   | 1231451   | 1231877  
    l1i_cache:u        | 23184685  | 23106452  | 20814292 
    l1i_cache_refill:u | 3239441   | 3263928   | 3238780  
    l1i_tlb:u          | 23184685  | 23106452  | 20814292 
    l1i_tlb_refill:u   | 1300602   | 1300552   | 1310131  
    l2i_cache:u        | 3239437   | 3263926   | 3238774  
    l2i_cache_refill:u | 1074469   | 1008563   | 1227375  
    l2i_tlb:u          | 1300716   | 1300587   | 1310233  
    l2i_tlb_refill:u   | 192       | 27        | 41       
    l1d_cache:u        | 16916576  | 16916920  | 16955806 
    l1d_cache_refill:u | 107574    | 114974    | 118331   
    l1d_tlb:u          | 20556696  | 20556506  | 20609882 
    l1d_tlb_refill:u   | 3867      | 3850      | 491      
    l2d_cache:u        | 3530117   | 3475190   | 3778513  
    l2d_cache_refill:u | 1167216   | 1165666   | 1561329  
    l2d_tlb:u          | 3995      | 3920      | 550      
    l2d_tlb_refill:u   | 13        | 9         | 59       
    ll_cache:u         | 95272     | 100015    | 112829   
    ll_cache_miss:u    | 46        | 450       | 31       

== combo_023_s2 ==
single_modules:
    id | module                                      
    ---+---------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p128_np8_l1_sp17    
    s1 | fetch_b128_d1_bp0_s16_r100_lshuf_p512_np1_l4
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 25460707 | 259333759
    instructions:u     | 12951049 | 39990998 
    br_retired:u       | 1031410  | 3911405  
    br_mis_pred:u      | 130639   | 1231712  
    l1i_cache:u        | 3683287  | 17609918 
    l1i_cache_refill:u | 677      | 999      
    l1i_tlb:u          | 3683287  | 17609918 
    l1i_tlb_refill:u   | 52       | 43       
    l2i_cache:u        | 675      | 997      
    l2i_cache_refill:u | 606      | 774      
    l2i_tlb:u          | 86       | 82       
    l2i_tlb_refill:u   | 39       | 22       
    l1d_cache:u        | 1535875  | 11786078 
    l1d_cache_refill:u | 606738   | 5072697  
    l1d_tlb:u          | 2309801  | 20972140 
    l1d_tlb_refill:u   | 666310   | 5163944  
    l2d_cache:u        | 2079670  | 21572541 
    l2d_cache_refill:u | 660177   | 10643589 
    l2d_tlb:u          | 666380   | 5165351  
    l2d_tlb_refill:u   | 135      | 100      
    ll_cache:u         | 659467   | 10642621 
    ll_cache_miss:u    | 446      | 80897    
combined_orders:
    id        | modules                                                                              
    ----------+--------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p128_np8_l1_sp17+fetch_b128_d1_bp0_s16_r100_lshuf_p512_np1_l4
    shuffle   | fetch_b128_d1_bp0_s16_r100_lshuf_p512_np1_l4+cold_b64_d4_bitrev_pstr_p128_np8_l1_sp17
    sum       | cold_b64_d4_bitrev_pstr_p128_np8_l1_sp17+fetch_b128_d1_bp0_s16_r100_lshuf_p512_np1_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 330752363 | 292618510 | 284794466
    instructions:u     | 52931242  | 52931389  | 52942047 
    br_retired:u       | 4941592   | 4941612   | 4942815  
    br_mis_pred:u      | 1377432   | 1385010   | 1362351  
    l1i_cache:u        | 23439601  | 23513563  | 21293205 
    l1i_cache_refill:u | 2011      | 1821      | 1676     
    l1i_tlb:u          | 23439601  | 23513563  | 21293205 
    l1i_tlb_refill:u   | 56        | 46        | 95       
    l2i_cache:u        | 2011      | 1820      | 1672     
    l2i_cache_refill:u | 1182      | 1044      | 1380     
    l2i_tlb:u          | 103       | 87        | 168      
    l2i_tlb_refill:u   | 51        | 28        | 61       
    l1d_cache:u        | 13285155  | 13299063  | 13321953 
    l1d_cache_refill:u | 5660394   | 5658825   | 5679435  
    l1d_tlb:u          | 23232668  | 23154417  | 23281941 
    l1d_tlb_refill:u   | 5822015   | 5820183   | 5830254  
    l2d_cache:u        | 24323588  | 24274254  | 23652211 
    l2d_cache_refill:u | 11437932  | 11060067  | 11303766 
    l2d_tlb:u          | 5824815   | 5820575   | 5831731  
    l2d_tlb_refill:u   | 850       | 198       | 235      
    ll_cache:u         | 11445799  | 11058805  | 11302088 
    ll_cache_miss:u    | 31936     | 4254      | 81343    

== combo_024_s2 ==
single_modules:
    id | module                                     
    ---+--------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p128_np1_l2_sp3   
    s1 | fetch_b128_d1_bp0_s16_r100_rand_p512_np2_l2
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 95876804 | 168595214
    instructions:u     | 26870997 | 37430988 
    br_retired:u       | 1991404  | 3911403  
    br_mis_pred:u      | 290703   | 1238684  
    l1i_cache:u        | 7868724  | 17125662 
    l1i_cache_refill:u | 914      | 1070     
    l1i_tlb:u          | 7868724  | 17125662 
    l1i_tlb_refill:u   | 45       | 46       
    l2i_cache:u        | 912      | 1068     
    l2i_cache_refill:u | 714      | 738      
    l2i_tlb:u          | 84       | 82       
    l2i_tlb_refill:u   | 18       | 24       
    l1d_cache:u        | 4257135  | 9223859  
    l1d_cache_refill:u | 2390047  | 2540816  
    l1d_tlb:u          | 7032045  | 15706474 
    l1d_tlb_refill:u   | 2600067  | 2534000  
    l2d_cache:u        | 8666480  | 11132502 
    l2d_cache_refill:u | 3062549  | 5298042  
    l2d_tlb:u          | 2600294  | 2551106  
    l2d_tlb_refill:u   | 155      | 78       
    ll_cache:u         | 3061634  | 5297153  
    ll_cache_miss:u    | 50       | 29186    
combined_orders:
    id        | modules                                                                             
    ----------+-------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p128_np1_l2_sp3+fetch_b128_d1_bp0_s16_r100_rand_p512_np2_l2
    shuffle   | fetch_b128_d1_bp0_s16_r100_rand_p512_np2_l2+cold_b128_d4_bitrev_pstr_p128_np1_l2_sp3
    sum       | cold_b128_d4_bitrev_pstr_p128_np1_l2_sp3+fetch_b128_d1_bp0_s16_r100_rand_p512_np2_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 263458710 | 263568608 | 264472018
    instructions:u     | 64291395  | 64291395  | 64301985 
    br_retired:u       | 5901610   | 5901610   | 5902807  
    br_mis_pred:u      | 1521878   | 1521779   | 1529387  
    l1i_cache:u        | 26587007  | 26540971  | 24994386 
    l1i_cache_refill:u | 2557      | 1887      | 1984     
    l1i_tlb:u          | 26587007  | 26540971  | 24994386 
    l1i_tlb_refill:u   | 54        | 49        | 91       
    l2i_cache:u        | 2556      | 1887      | 1980     
    l2i_cache_refill:u | 1238      | 1084      | 1452     
    l2i_tlb:u          | 87        | 89        | 166      
    l2i_tlb_refill:u   | 30        | 30        | 42       
    l1d_cache:u        | 13414552  | 13405334  | 13480994 
    l1d_cache_refill:u | 4920739   | 4949465   | 4930863  
    l1d_tlb:u          | 22547731  | 22630610  | 22738519 
    l1d_tlb_refill:u   | 5120179   | 5144314   | 5134067  
    l2d_cache:u        | 19910455  | 19373659  | 19798982 
    l2d_cache_refill:u | 8265963   | 7811015   | 8360591  
    l2d_tlb:u          | 5130379   | 5156118   | 5151400  
    l2d_tlb_refill:u   | 169       | 263       | 233      
    ll_cache:u         | 8264581   | 7809667   | 8358787  
    ll_cache_miss:u    | 60104     | 30611     | 29236    

== combo_025_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | hot_b128_bp3_r100_pstr_p512_np2_l1_sp3
    s1 | itlb_f128_l1_r100_pstr_p128_np2_l4_sp3
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 66784062 | 309799279
    instructions:u     | 22160997 | 26011098 
    br_retired:u       | 3941404  | 1371413  
    br_mis_pred:u      | 431      | 458      
    l1i_cache:u        | 2852329  | 3339326  
    l1i_cache_refill:u | 881      | 3302792  
    l1i_tlb:u          | 2852329  | 3339326  
    l1i_tlb_refill:u   | 45       | 1310056  
    l2i_cache:u        | 880      | 3302790  
    l2i_cache_refill:u | 644      | 2320571  
    l2i_tlb:u          | 139      | 1310085  
    l2i_tlb_refill:u   | 19       | 39       
    l1d_cache:u        | 1416502  | 5255928  
    l1d_cache_refill:u | 1275753  | 4951785  
    l1d_tlb:u          | 2804637  | 10532574 
    l1d_tlb_refill:u   | 1305014  | 5150216  
    l2d_cache:u        | 5216080  | 18436967 
    l2d_cache_refill:u | 2614368  | 7391037  
    l2d_tlb:u          | 1305349  | 5150268  
    l2d_tlb_refill:u   | 75       | 29       
    ll_cache:u         | 2613733  | 5296581  
    ll_cache_miss:u    | 4032     | 392      
combined_orders:
    id        | modules                                                                      
    ----------+------------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_pstr_p512_np2_l1_sp3+itlb_f128_l1_r100_pstr_p128_np2_l4_sp3
    shuffle   | itlb_f128_l1_r100_pstr_p128_np2_l4_sp3+hot_b128_bp3_r100_pstr_p512_np2_l1_sp3
    sum       | hot_b128_bp3_r100_pstr_p512_np2_l1_sp3+itlb_f128_l1_r100_pstr_p128_np2_l4_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 358185717 | 357707833 | 376583341
    instructions:u     | 48161242  | 48161242  | 48172095 
    br_retired:u       | 5311592   | 5311592   | 5312817  
    br_mis_pred:u      | 601       | 586       | 889      
    l1i_cache:u        | 6226576   | 6184447   | 6191655  
    l1i_cache_refill:u | 2900171   | 2988989   | 3303673  
    l1i_tlb:u          | 6226576   | 6184447   | 6191655  
    l1i_tlb_refill:u   | 1310254   | 1310268   | 1310101  
    l2i_cache:u        | 2900167   | 2988989   | 3303670  
    l2i_cache_refill:u | 2052147   | 2152489   | 2321215  
    l2i_tlb:u          | 1310403   | 1310443   | 1310224  
    l2i_tlb_refill:u   | 295       | 425       | 58       
    l1d_cache:u        | 6667059   | 6667338   | 6672430  
    l1d_cache_refill:u | 6170829   | 6176139   | 6227538  
    l1d_tlb:u          | 13296133  | 13310761  | 13337211 
    l1d_tlb_refill:u   | 6450911   | 6451951   | 6455230  
    l2d_cache:u        | 23289770  | 23457727  | 23653047 
    l2d_cache_refill:u | 9673406   | 9770948   | 10005405 
    l2d_tlb:u          | 6451201   | 6452451   | 6455617  
    l2d_tlb_refill:u   | 2878      | 2113      | 104      
    ll_cache:u         | 7496184   | 7656765   | 7910314  
    ll_cache_miss:u    | 724       | 10989     | 4424     

== combo_026_s2 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | hot_b64_bp3_r100_pstr_p1_np1_l4_sp3  
    s1 | itlb_f64_l1_r100_lstr_p512_np2_l2_sl9
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 12939982 | 88974180
    instructions:u     | 13201055 | 11930997
    br_retired:u       | 2021408  | 731404  
    br_mis_pred:u      | 437      | 462     
    l1i_cache:u        | 1726488  | 1622920 
    l1i_cache_refill:u | 624      | 1309183 
    l1i_tlb:u          | 1726488  | 1622920 
    l1i_tlb_refill:u   | 44       | 660062  
    l2i_cache:u        | 623      | 1309184 
    l2i_cache_refill:u | 533      | 164886  
    l2i_tlb:u          | 71       | 660118  
    l2i_tlb_refill:u   | 12       | 119     
    l1d_cache:u        | 2695361  | 1415469 
    l1d_cache_refill:u | 145      | 1279979 
    l1d_tlb:u          | 2697398  | 2799498 
    l1d_tlb_refill:u   | 60       | 1304284 
    l2d_cache:u        | 1368     | 6409693 
    l2d_cache_refill:u | 953      | 2743423 
    l2d_tlb:u          | 81       | 1304309 
    l2d_tlb_refill:u   | 32       | 150     
    ll_cache:u         | 338      | 2563054 
    ll_cache_miss:u    | 32       | 316     
combined_orders:
    id        | modules                                                                  
    ----------+--------------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_pstr_p1_np1_l4_sp3+itlb_f64_l1_r100_lstr_p512_np2_l2_sl9
    shuffle   | itlb_f64_l1_r100_lstr_p512_np2_l2_sl9+hot_b64_bp3_r100_pstr_p1_np1_l4_sp3
    sum       | hot_b64_bp3_r100_pstr_p1_np1_l4_sp3+itlb_f64_l1_r100_lstr_p512_np2_l2_sl9
combined_counts:
    metric             | canonical | shuffle  | sum      
    -------------------+-----------+----------+----------
    cpu-cycles:u       | 108292155 | 92633347 | 101914162
    instructions:u     | 25121297  | 25121297 | 25132052 
    br_retired:u       | 2751604   | 2751604  | 2752812  
    br_mis_pred:u      | 585       | 629      | 899      
    l1i_cache:u        | 3364354   | 3359307  | 3349408  
    l1i_cache_refill:u | 856142    | 813380   | 1309807  
    l1i_tlb:u          | 3364354   | 3359307  | 3349408  
    l1i_tlb_refill:u   | 660253    | 660260   | 660106   
    l2i_cache:u        | 856142    | 813380   | 1309807  
    l2i_cache_refill:u | 238448    | 138347   | 165419   
    l2i_tlb:u          | 660319    | 660345   | 660189   
    l2i_tlb_refill:u   | 51        | 87       | 131      
    l1d_cache:u        | 4105964   | 4105886  | 4110830  
    l1d_cache_refill:u | 1279608   | 1279148  | 1280124  
    l1d_tlb:u          | 5493080   | 5493173  | 5496896  
    l1d_tlb_refill:u   | 1304850   | 1305012  | 1304344  
    l2d_cache:u        | 6048442   | 6004898  | 6411061  
    l2d_cache_refill:u | 2755963   | 2741745  | 2744376  
    l2d_tlb:u          | 1304911   | 1305060  | 1304390  
    l2d_tlb_refill:u   | 669       | 661      | 182      
    ll_cache:u         | 2578485   | 2573104  | 2563392  
    ll_cache_miss:u    | 2372      | 3101     | 348      

== combo_027_s2 ==
single_modules:
    id | module                                   
    ---+------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lin_p16_np2_l4
    s1 | itlb_f128_l1_r100_pstr_p16_np2_l1_sp33   
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 58719106 | 98093018
    instructions:u     | 39990988 | 22170997
    br_retired:u       | 3911403  | 1371404 
    br_mis_pred:u      | 1231082  | 461     
    l1i_cache:u        | 17202602 | 3064850 
    l1i_cache_refill:u | 862      | 3393131 
    l1i_tlb:u          | 17202602 | 3064850 
    l1i_tlb_refill:u   | 48       | 1300088 
    l2i_cache:u        | 861      | 3393124 
    l2i_cache_refill:u | 690      | 1162736 
    l2i_tlb:u          | 90       | 1300173 
    l2i_tlb_refill:u   | 13       | 35      
    l1d_cache:u        | 11695591 | 1415280 
    l1d_cache_refill:u | 82959    | 97593   
    l1d_tlb:u          | 15349590 | 1417200 
    l1d_tlb_refill:u   | 188      | 262     
    l2d_cache:u        | 434183   | 3385045 
    l2d_cache_refill:u | 1082     | 1098711 
    l2d_tlb:u          | 215      | 286     
    l2d_tlb_refill:u   | 3        | 10      
    ll_cache:u         | 310      | 130585  
    ll_cache_miss:u    | 189      | 59      
combined_orders:
    id        | modules                                                                         
    ----------+---------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lin_p16_np2_l4+itlb_f128_l1_r100_pstr_p16_np2_l1_sp33
    shuffle   | itlb_f128_l1_r100_pstr_p16_np2_l1_sp33+fetch_b128_d1_bp0_s16_r100_lin_p16_np2_l4
    sum       | fetch_b128_d1_bp0_s16_r100_lin_p16_np2_l4+itlb_f128_l1_r100_pstr_p16_np2_l1_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 162909227 | 158428622 | 156812124
    instructions:u     | 62151297  | 62151297  | 62161985 
    br_retired:u       | 5281604   | 5281604   | 5282807  
    br_mis_pred:u      | 1231199   | 1231524   | 1231543  
    l1i_cache:u        | 22701048  | 22684731  | 20267452 
    l1i_cache_refill:u | 3374758   | 3220465   | 3393993  
    l1i_tlb:u          | 22701048  | 22684731  | 20267452 
    l1i_tlb_refill:u   | 1300557   | 1300552   | 1300136  
    l2i_cache:u        | 3374755   | 3220461   | 3393985  
    l2i_cache_refill:u | 1241776   | 958268    | 1163426  
    l2i_tlb:u          | 1300670   | 1300602   | 1300263  
    l2i_tlb_refill:u   | 181       | 29        | 48       
    l1d_cache:u        | 13066824  | 13088170  | 13110871 
    l1d_cache_refill:u | 174749    | 275952    | 180552   
    l1d_tlb:u          | 16715034  | 16719268  | 16766790 
    l1d_tlb_refill:u   | 3833      | 3835      | 450      
    l2d_cache:u        | 3747057   | 4072013   | 3819228  
    l2d_cache_refill:u | 1018541   | 1102387   | 1099793  
    l2d_tlb:u          | 3961      | 3960      | 501      
    l2d_tlb_refill:u   | 16        | 68        | 13       
    ll_cache:u         | 106787    | 134611    | 130895   
    ll_cache_miss:u    | 54        | 877       | 248      

== combo_028_s2 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | hot_b64_bp3_r100_pstr_p16_np8_l1_sp17
    s1 | itlb_f64_l1_r100_lstr_p128_np2_l2_sl5
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 5268958  | 69002613
    instructions:u     | 11281049 | 11930997
    br_retired:u       | 2021410  | 731404  
    br_mis_pred:u      | 426      | 495     
    l1i_cache:u        | 1485944  | 1707590 
    l1i_cache_refill:u | 572      | 1457059 
    l1i_tlb:u          | 1485944  | 1707590 
    l1i_tlb_refill:u   | 52       | 660052  
    l2i_cache:u        | 570      | 1457056 
    l2i_cache_refill:u | 533      | 247788  
    l2i_tlb:u          | 86       | 660094  
    l2i_tlb_refill:u   | 13       | 21      
    l1d_cache:u        | 775230   | 1415490 
    l1d_cache_refill:u | 483      | 1223578 
    l1d_tlb:u          | 777315   | 2786082 
    l1d_tlb_refill:u   | 94       | 1302372 
    l2d_cache:u        | 2170     | 5353195 
    l2d_cache_refill:u | 1186     | 1726478 
    l2d_tlb:u          | 115      | 1302400 
    l2d_tlb_refill:u   | 26       | 160     
    ll_cache:u         | 583      | 1487960 
    ll_cache_miss:u    | 78       | 449     
combined_orders:
    id        | modules                                                                    
    ----------+----------------------------------------------------------------------------
    canonical | hot_b64_bp3_r100_pstr_p16_np8_l1_sp17+itlb_f64_l1_r100_lstr_p128_np2_l2_sl5
    shuffle   | itlb_f64_l1_r100_lstr_p128_np2_l2_sl5+hot_b64_bp3_r100_pstr_p16_np8_l1_sp17
    sum       | hot_b64_bp3_r100_pstr_p16_np8_l1_sp17+itlb_f64_l1_r100_lstr_p128_np2_l2_sl5
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 81252052  | 86105167 | 74271571
    instructions:u     | 23201288  | 23201288 | 23212046
    br_retired:u       | 2751603   | 2751603  | 2752814 
    br_mis_pred:u      | 578       | 582      | 921     
    l1i_cache:u        | 3148686   | 3120573  | 3193534 
    l1i_cache_refill:u | 1134619   | 998530   | 1457631 
    l1i_tlb:u          | 3148686   | 3120573  | 3193534 
    l1i_tlb_refill:u   | 670161    | 670211   | 660104  
    l2i_cache:u        | 1134619   | 998529   | 1457626 
    l2i_cache_refill:u | 297832    | 376455   | 248321  
    l2i_tlb:u          | 670211    | 670259   | 660180  
    l2i_tlb_refill:u   | 109       | 19       | 34      
    l1d_cache:u        | 2185688   | 2185655  | 2190720 
    l1d_cache_refill:u | 1228761   | 1250639  | 1224061 
    l1d_tlb:u          | 3584804   | 3603900  | 3563397 
    l1d_tlb_refill:u   | 1308021   | 1319031  | 1302466 
    l2d_cache:u        | 5233913   | 4967801  | 5355365 
    l2d_cache_refill:u | 1774491   | 1663404  | 1727664 
    l2d_tlb:u          | 1308044   | 1319058  | 1302515 
    l2d_tlb_refill:u   | 21        | 28       | 186     
    ll_cache:u         | 1455468   | 1348209  | 1488543 
    ll_cache_miss:u    | 204       | 122      | 527     

== combo_029_s2 ==
single_modules:
    id | module                                 
    ---+----------------------------------------
    s0 | hot_b128_bp3_r100_pstr_p512_np8_l1_sp17
    s1 | itlb_f128_l1_r100_pstr_p16_np8_l4_sp17 
single_counts:
    metric             | s0       | s1       
    -------------------+----------+----------
    cpu-cycles:u       | 71312806 | 102693959
    instructions:u     | 22160997 | 26010997 
    br_retired:u       | 3941404  | 1371404  
    br_mis_pred:u      | 438      | 461      
    l1i_cache:u        | 2852398  | 3427628  
    l1i_cache_refill:u | 728      | 3224178  
    l1i_tlb:u          | 2852398  | 3427628  
    l1i_tlb_refill:u   | 42       | 1310095  
    l2i_cache:u        | 727      | 3224174  
    l2i_cache_refill:u | 624      | 990299   
    l2i_tlb:u          | 143      | 1310179  
    l2i_tlb_refill:u   | 25       | 172      
    l1d_cache:u        | 1416301  | 5255468  
    l1d_cache_refill:u | 1280690  | 61006    
    l1d_tlb:u          | 2808277  | 5257747  
    l1d_tlb_refill:u   | 1305777  | 256      
    l2d_cache:u        | 5106738  | 3134833  
    l2d_cache_refill:u | 2569172  | 924833   
    l2d_tlb:u          | 1306132  | 282      
    l2d_tlb_refill:u   | 76       | 49       
    ll_cache:u         | 2568438  | 86761    
    ll_cache_miss:u    | 14148    | 135      
combined_orders:
    id        | modules                                                                       
    ----------+-------------------------------------------------------------------------------
    canonical | hot_b128_bp3_r100_pstr_p512_np8_l1_sp17+itlb_f128_l1_r100_pstr_p16_np8_l4_sp17
    shuffle   | itlb_f128_l1_r100_pstr_p16_np8_l4_sp17+hot_b128_bp3_r100_pstr_p512_np8_l1_sp17
    sum       | hot_b128_bp3_r100_pstr_p512_np8_l1_sp17+itlb_f128_l1_r100_pstr_p16_np8_l4_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 207758767 | 202400004 | 174006765
    instructions:u     | 48161298  | 48161294  | 48171994 
    br_retired:u       | 5311605   | 5311601   | 5312808  
    br_mis_pred:u      | 599       | 580       | 899      
    l1i_cache:u        | 6279986   | 6328883   | 6280026  
    l1i_cache_refill:u | 2944127   | 3061798   | 3224906  
    l1i_tlb:u          | 6279986   | 6328883   | 6280026  
    l1i_tlb_refill:u   | 1310253   | 1310302   | 1310137  
    l2i_cache:u        | 2944127   | 3061798   | 3224901  
    l2i_cache_refill:u | 988754    | 824194    | 990923   
    l2i_tlb:u          | 1310417   | 1310376   | 1310322  
    l2i_tlb_refill:u   | 126       | 189       | 197      
    l1d_cache:u        | 6666932   | 6667282   | 6671769  
    l1d_cache_refill:u | 1381441   | 1366868   | 1341696  
    l1d_tlb:u          | 8062411   | 8060032   | 8066024  
    l1d_tlb_refill:u   | 1307062   | 1306625   | 1306033  
    l2d_cache:u        | 8624053   | 8080916   | 8241571  
    l2d_cache_refill:u | 3980021   | 3385208   | 3494005  
    l2d_tlb:u          | 1307306   | 1306974   | 1306414  
    l2d_tlb_refill:u   | 418       | 184       | 125      
    ll_cache:u         | 2727400   | 2694123   | 2655199  
    ll_cache_miss:u    | 3920      | 3672      | 14283    

== combo_030_s2 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p128_np4_l1    
    s1 | hot_b128_bp3_r100_lstr_p128_np4_l1_sl3
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 22087743 | 52381500
    instructions:u     | 12951049 | 22160997
    br_retired:u       | 1031410  | 3941404 
    br_mis_pred:u      | 130655   | 402     
    l1i_cache:u        | 3717008  | 2850761 
    l1i_cache_refill:u | 694      | 854     
    l1i_tlb:u          | 3717008  | 2850761 
    l1i_tlb_refill:u   | 54       | 55      
    l2i_cache:u        | 692      | 853     
    l2i_cache_refill:u | 631      | 672     
    l2i_tlb:u          | 94       | 92      
    l2i_tlb_refill:u   | 45       | 45      
    l1d_cache:u        | 1536240  | 1415987 
    l1d_cache_refill:u | 290276   | 1220841 
    l1d_tlb:u          | 1860304  | 2470379 
    l1d_tlb_refill:u   | 170058   | 980061  
    l2d_cache:u        | 1953061  | 3526552 
    l2d_cache_refill:u | 337310   | 957090  
    l2d_tlb:u          | 171607   | 980200  
    l2d_tlb_refill:u   | 16       | 129     
    ll_cache:u         | 336694   | 956358  
    ll_cache_miss:u    | 877      | 923     
combined_orders:
    id        | modules                                                                  
    ----------+--------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p128_np4_l1+hot_b128_bp3_r100_lstr_p128_np4_l1_sl3
    shuffle   | hot_b128_bp3_r100_lstr_p128_np4_l1_sl3+cold_b64_d4_bitrev_lin_p128_np4_l1
    sum       | cold_b64_d4_bitrev_lin_p128_np4_l1+hot_b128_bp3_r100_lstr_p128_np4_l1_sl3
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 71417361  | 64769944 | 74469243
    instructions:u     | 35101297  | 35101297 | 35112046
    br_retired:u       | 4971604   | 4971604  | 4972814 
    br_mis_pred:u      | 131140    | 130642   | 131057  
    l1i_cache:u        | 6341978   | 6329612  | 6567769 
    l1i_cache_refill:u | 981       | 964      | 1548    
    l1i_tlb:u          | 6341978   | 6329612  | 6567769 
    l1i_tlb_refill:u   | 45        | 46       | 109     
    l2i_cache:u        | 978       | 963      | 1545    
    l2i_cache_refill:u | 736       | 753      | 1303    
    l2i_tlb:u          | 185       | 86       | 186     
    l2i_tlb_refill:u   | 19        | 15       | 90      
    l1d_cache:u        | 2947340   | 2947286  | 2952227 
    l1d_cache_refill:u | 1506993   | 1503927  | 1511117 
    l1d_tlb:u          | 4292456   | 4291510  | 4330683 
    l1d_tlb_refill:u   | 1150063   | 1150060  | 1150119 
    l2d_cache:u        | 6002551   | 5944013  | 5479613 
    l2d_cache_refill:u | 1627261   | 1602639  | 1294400 
    l2d_tlb:u          | 1150912   | 1151223  | 1151807 
    l2d_tlb_refill:u   | 289       | 257      | 145     
    ll_cache:u         | 1626315   | 1601658  | 1293052 
    ll_cache_miss:u    | 10168     | 11577    | 1800    

== combo_031_s2 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p16_np4_l4_sp33
    s1 | itlb_f64_l1_r100_pstr_p128_np4_l1_sp3   
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 35006085 | 40473050
    instructions:u     | 29430997 | 11290997
    br_retired:u       | 1991404  | 731404  
    br_mis_pred:u      | 290628   | 433     
    l1i_cache:u        | 8088203  | 1478550 
    l1i_cache_refill:u | 864      | 1499671 
    l1i_tlb:u          | 8088203  | 1478550 
    l1i_tlb_refill:u   | 48       | 660050  
    l2i_cache:u        | 864      | 1499669 
    l2i_cache_refill:u | 721      | 15261   
    l2i_tlb:u          | 90       | 660083  
    l2i_tlb_refill:u   | 14       | 23      
    l1d_cache:u        | 6815551  | 775572  
    l1d_cache_refill:u | 100306   | 620522  
    l1d_tlb:u          | 6817969  | 1505700 
    l1d_tlb_refill:u   | 152      | 660727  
    l2d_cache:u        | 182786   | 3398062 
    l2d_cache_refill:u | 1494     | 701358  
    l2d_tlb:u          | 183      | 660773  
    l2d_tlb_refill:u   | 42       | 168     
    ll_cache:u         | 685      | 686053  
    ll_cache_miss:u    | 61       | 692     
combined_orders:
    id        | modules                                                                       
    ----------+-------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p16_np4_l4_sp33+itlb_f64_l1_r100_pstr_p128_np4_l1_sp3
    shuffle   | itlb_f64_l1_r100_pstr_p128_np4_l1_sp3+cold_b128_d4_bitrev_pstr_p16_np4_l4_sp33
    sum       | cold_b128_d4_bitrev_pstr_p16_np4_l4_sp33+itlb_f64_l1_r100_pstr_p128_np4_l1_sp3
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 86398702  | 73700574 | 75479135
    instructions:u     | 40711288  | 40711288 | 40721994
    br_retired:u       | 2721603   | 2721603  | 2722808 
    br_mis_pred:u      | 290948    | 290984   | 291061  
    l1i_cache:u        | 9024193   | 8995220  | 9566753 
    l1i_cache_refill:u | 1440446   | 1101209  | 1500535 
    l1i_tlb:u          | 9024193   | 8995220  | 9566753 
    l1i_tlb_refill:u   | 660638    | 660554   | 660098  
    l2i_cache:u        | 1440446   | 1101210  | 1500533 
    l2i_cache_refill:u | 140042    | 5825     | 15982   
    l2i_tlb:u          | 660764    | 660589   | 660173  
    l2i_tlb_refill:u   | 111       | 30       | 37      
    l1d_cache:u        | 7588466   | 7586166  | 7591123 
    l1d_cache_refill:u | 695636    | 703629   | 720828  
    l1d_tlb:u          | 8326280   | 8329502  | 8323669 
    l1d_tlb_refill:u   | 663437    | 664710   | 660879  
    l2d_cache:u        | 3913132   | 4358156  | 3580848 
    l2d_cache_refill:u | 657802    | 863814   | 702852  
    l2d_tlb:u          | 663559    | 664835   | 660956  
    l2d_tlb_refill:u   | 32        | 172      | 210     
    ll_cache:u         | 596035    | 859882   | 686738  
    ll_cache_miss:u    | 7992      | 4207     | 753     

== combo_032_s2 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lshuf_p1_np2_l4
    s1 | itlb_f64_l1_r100_rand_p512_np2_l1         
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 60322514 | 52910318
    instructions:u     | 39990988 | 11290997
    br_retired:u       | 3911403  | 731404  
    br_mis_pred:u      | 1231152  | 497     
    l1i_cache:u        | 19663780 | 1486508 
    l1i_cache_refill:u | 932      | 1497136 
    l1i_tlb:u          | 19663780 | 1486508 
    l1i_tlb_refill:u   | 55       | 660058  
    l2i_cache:u        | 931      | 1497134 
    l2i_cache_refill:u | 779      | 15680   
    l2i_tlb:u          | 94       | 660101  
    l2i_tlb_refill:u   | 30       | 148     
    l1d_cache:u        | 11665635 | 775543  
    l1d_cache_refill:u | 186      | 639726  
    l1d_tlb:u          | 15299513 | 1475128 
    l1d_tlb_refill:u   | 90       | 637380  
    l2d_cache:u        | 1535     | 4030121 
    l2d_cache_refill:u | 955      | 1306573 
    l2d_tlb:u          | 118      | 637410  
    l2d_tlb_refill:u   | 6        | 643     
    ll_cache:u         | 244      | 1284140 
    ll_cache_miss:u    | 76       | 388     
combined_orders:
    id        | modules                                                                     
    ----------+-----------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lshuf_p1_np2_l4+itlb_f64_l1_r100_rand_p512_np2_l1
    shuffle   | itlb_f64_l1_r100_rand_p512_np2_l1+fetch_b128_d1_bp0_s16_r100_lshuf_p1_np2_l4
    sum       | fetch_b128_d1_bp0_s16_r100_lshuf_p1_np2_l4+itlb_f64_l1_r100_rand_p512_np2_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 140402266 | 131778958 | 113232832
    instructions:u     | 51271288  | 51271288  | 51281985 
    br_retired:u       | 4641603   | 4641603   | 4642807  
    br_mis_pred:u      | 1234325   | 1231482   | 1231649  
    l1i_cache:u        | 21142167  | 21114075  | 21150288 
    l1i_cache_refill:u | 1092346   | 1354474   | 1498068  
    l1i_tlb:u          | 21142167  | 21114075  | 21150288 
    l1i_tlb_refill:u   | 660557    | 660556    | 660113   
    l2i_cache:u        | 1092348   | 1354473   | 1498065  
    l2i_cache_refill:u | 23796     | 34375     | 16459    
    l2i_tlb:u          | 660691    | 660611    | 660195   
    l2i_tlb_refill:u   | 173       | 54        | 178      
    l1d_cache:u        | 12427457  | 12437887  | 12441178 
    l1d_cache_refill:u | 639828    | 641524    | 639912   
    l1d_tlb:u          | 16779281  | 16783043  | 16774641 
    l1d_tlb_refill:u   | 639775    | 639792    | 637470   
    l2d_cache:u        | 3741331   | 3851292   | 4031656  
    l2d_cache_refill:u | 1336439   | 1316793   | 1307528  
    l2d_tlb:u          | 639909    | 639923    | 637528   
    l2d_tlb_refill:u   | 119       | 112       | 649      
    ll_cache:u         | 1308939   | 1290477   | 1284384  
    ll_cache_miss:u    | 6588      | 523       | 464      

== combo_033_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | hot_b64_bp3_r100_lin_p1_np1_l4   
    s1 | itlb_f64_l1_r100_lshuf_p16_np1_l4
single_counts:
    metric             | s0       | s1      
    -------------------+----------+---------
    cpu-cycles:u       | 12937740 | 31517971
    instructions:u     | 13201049 | 13210997
    br_retired:u       | 2021410  | 731404  
    br_mis_pred:u      | 490      | 417     
    l1i_cache:u        | 1726675  | 1715829 
    l1i_cache_refill:u | 681      | 1877073 
    l1i_tlb:u          | 1726675  | 1715829 
    l1i_tlb_refill:u   | 51       | 670070  
    l2i_cache:u        | 680      | 1877071 
    l2i_cache_refill:u | 570      | 10757   
    l2i_tlb:u          | 109      | 670136  
    l2i_tlb_refill:u   | 44       | 25      
    l1d_cache:u        | 2695278  | 2695402 
    l1d_cache_refill:u | 150      | 10198   
    l1d_tlb:u          | 2697271  | 2697419 
    l1d_tlb_refill:u   | 62       | 115     
    l2d_cache:u        | 1235     | 929127  
    l2d_cache_refill:u | 811      | 21292   
    l2d_tlb:u          | 134      | 138     
    l2d_tlb_refill:u   | 4        | 59      
    ll_cache:u         | 258      | 10408   
    ll_cache_miss:u    | 27       | 51      
combined_orders:
    id        | modules                                                         
    ----------+-----------------------------------------------------------------
    canonical | hot_b64_bp3_r100_lin_p1_np1_l4+itlb_f64_l1_r100_lshuf_p16_np1_l4
    shuffle   | itlb_f64_l1_r100_lshuf_p16_np1_l4+hot_b64_bp3_r100_lin_p1_np1_l4
    sum       | hot_b64_bp3_r100_lin_p1_np1_l4+itlb_f64_l1_r100_lshuf_p16_np1_l4
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 45226454  | 45703169 | 44455711
    instructions:u     | 26401297  | 26401303 | 26412046
    br_retired:u       | 2751604   | 2751602  | 2752814 
    br_mis_pred:u      | 555       | 532      | 907     
    l1i_cache:u        | 3482449   | 3502192  | 3442504 
    l1i_cache_refill:u | 994851    | 1325421  | 1877754 
    l1i_tlb:u          | 3482449   | 3502192  | 3442504 
    l1i_tlb_refill:u   | 660260    | 660268   | 670121  
    l2i_cache:u        | 994850    | 1325420  | 1877751 
    l2i_cache_refill:u | 31265     | 60923    | 11327   
    l2i_tlb:u          | 660321    | 660312   | 670245  
    l2i_tlb_refill:u   | 110       | 22       | 69      
    l1d_cache:u        | 5385548   | 5385532  | 5390680 
    l1d_cache_refill:u | 17319     | 74989    | 10348   
    l1d_tlb:u          | 5387684   | 5387541  | 5394690 
    l1d_tlb_refill:u   | 153       | 174      | 177     
    l2d_cache:u        | 1138432   | 1335092  | 930362  
    l2d_cache_refill:u | 41473     | 85912    | 22103   
    l2d_tlb:u          | 177       | 195      | 272     
    l2d_tlb_refill:u   | 44        | 7        | 63      
    ll_cache:u         | 20385     | 302      | 10666   
    ll_cache_miss:u    | 24        | 15       | 78      

== combo_034_s3 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p512_np2_l1_sp17 
    s1 | fetch_b128_d1_bp0_s16_r100_lin_p512_np2_l4
    s2 | itlb_f64_l1_r100_lshuf_p1_np1_l1          
single_counts:
    metric             | s0       | s1        | s2      
    -------------------+----------+-----------+---------
    cpu-cycles:u       | 85360583 | 253883727 | 28464449
    instructions:u     | 25590997 | 39991004  | 11290997
    br_retired:u       | 1991404  | 3911403   | 731404  
    br_mis_pred:u      | 290735   | 1240588   | 428     
    l1i_cache:u        | 7607938  | 17517068  | 1565381 
    l1i_cache_refill:u | 961      | 1224      | 1744539 
    l1i_tlb:u          | 7607938  | 17517068  | 1565381 
    l1i_tlb_refill:u   | 65       | 53        | 660108  
    l2i_cache:u        | 957      | 1223      | 1744535 
    l2i_cache_refill:u | 792      | 837       | 90313   
    l2i_tlb:u          | 120      | 110       | 660190  
    l2i_tlb_refill:u   | 52       | 43        | 107     
    l1d_cache:u        | 2977039  | 11840290  | 775387  
    l1d_cache_refill:u | 1263214  | 3188775   | 156     
    l1d_tlb:u          | 4390420  | 18351917  | 777226  
    l1d_tlb_refill:u   | 1305259  | 2590072   | 72      
    l2d_cache:u        | 5622636  | 23012120  | 1464950 
    l2d_cache_refill:u | 2727099  | 10560951  | 91254   
    l2d_tlb:u          | 1305421  | 2592846   | 101     
    l2d_tlb_refill:u   | 83       | 626       | 35      
    ll_cache:u         | 2726223  | 10559025  | 360     
    ll_cache_miss:u    | 39252    | 13574     | 29      
combined_orders:
    id        | modules                                                                                                              
    ----------+----------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p512_np2_l1_sp17+fetch_b128_d1_bp0_s16_r100_lin_p512_np2_l4+itlb_f64_l1_r100_lshuf_p1_np1_l1
    shuffle   | itlb_f64_l1_r100_lshuf_p1_np1_l1+fetch_b128_d1_bp0_s16_r100_lin_p512_np2_l4+cold_b128_d4_bitrev_pstr_p512_np2_l1_sp17
    sum       | cold_b128_d4_bitrev_pstr_p512_np2_l1_sp17+fetch_b128_d1_bp0_s16_r100_lin_p512_np2_l4+itlb_f64_l1_r100_lshuf_p1_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 438350029 | 418345159 | 367708759
    instructions:u     | 76851542  | 76851548  | 76872998 
    br_retired:u       | 6631792   | 6631790   | 6634211  
    br_mis_pred:u      | 1521809   | 1522086   | 1531751  
    l1i_cache:u        | 28445229  | 28446421  | 26690387 
    l1i_cache_refill:u | 1265912   | 1088932   | 1746724  
    l1i_tlb:u          | 28445229  | 28446421  | 26690387 
    l1i_tlb_refill:u   | 660952    | 660971    | 660226   
    l2i_cache:u        | 1265911   | 1088930   | 1746715  
    l2i_cache_refill:u | 16030     | 16291     | 91942    
    l2i_tlb:u          | 661248    | 661251    | 660420   
    l2i_tlb_refill:u   | 4077      | 4141      | 202      
    l1d_cache:u        | 15536339  | 15541523  | 15592716 
    l1d_cache_refill:u | 4249144   | 4253189   | 4452145  
    l1d_tlb:u          | 23794700  | 23805164  | 23519563 
    l1d_tlb_refill:u   | 3900164   | 3900184   | 3895403  
    l2d_cache:u        | 29521015  | 29825680  | 30099706 
    l2d_cache_refill:u | 13472906  | 13165086  | 13379304 
    l2d_tlb:u          | 3907604   | 3918178   | 3898368  
    l2d_tlb_refill:u   | 21408     | 20561     | 744      
    ll_cache:u         | 13454486  | 13145685  | 13285608 
    ll_cache_miss:u    | 238349    | 41885     | 52855    

== combo_035_s3 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | cold_b64_d4_bitrev_rand_p128_np2_l1       
    s1 | fetch_b64_d1_bp0_s16_r100_rand_p128_np2_l1
    s2 | itlb_f64_l1_r100_rand_p16_np8_l1          
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 26769079 | 36218999 | 30395754
    instructions:u     | 12950997 | 18230988 | 11290997
    br_retired:u       | 1031404  | 1991403  | 731404  
    br_mis_pred:u      | 130705   | 591146   | 447     
    l1i_cache:u        | 3707959  | 8460586  | 1504879 
    l1i_cache_refill:u | 793      | 703      | 1523115 
    l1i_tlb:u          | 3707959  | 8460586  | 1504879 
    l1i_tlb_refill:u   | 56       | 51       | 660057  
    l2i_cache:u        | 794      | 703      | 1523112 
    l2i_cache_refill:u | 649      | 624      | 271857  
    l2i_tlb:u          | 101      | 111      | 660107  
    l2i_tlb_refill:u   | 45       | 40       | 101     
    l1d_cache:u        | 1535802  | 4028040  | 775269  
    l1d_cache_refill:u | 606789   | 619112   | 21627   
    l1d_tlb:u          | 2163685  | 6458546  | 777067  
    l1d_tlb_refill:u   | 537576   | 562692   | 128     
    l2d_cache:u        | 2118467  | 1928728  | 1069837 
    l2d_cache_refill:u | 698019   | 529066   | 155791  
    l2d_tlb:u          | 538491   | 562743   | 152     
    l2d_tlb_refill:u   | 126      | 16       | 38      
    ll_cache:u         | 697331   | 528525   | 12258   
    ll_cache_miss:u    | 71       | 122      | 76      
combined_orders:
    id        | modules                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_rand_p128_np2_l1+fetch_b64_d1_bp0_s16_r100_rand_p128_np2_l1+itlb_f64_l1_r100_rand_p16_np8_l1
    shuffle   | cold_b64_d4_bitrev_rand_p128_np2_l1+itlb_f64_l1_r100_rand_p16_np8_l1+fetch_b64_d1_bp0_s16_r100_rand_p128_np2_l1
    sum       | cold_b64_d4_bitrev_rand_p128_np2_l1+fetch_b64_d1_bp0_s16_r100_rand_p128_np2_l1+itlb_f64_l1_r100_rand_p16_np8_l1
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 90909682  | 91645248 | 93383832
    instructions:u     | 42451603  | 42451597 | 42472982
    br_retired:u       | 3751802   | 3751804  | 3754211 
    br_mis_pred:u      | 721951    | 722265   | 722298  
    l1i_cache:u        | 14518662  | 14603641 | 13673424
    l1i_cache_refill:u | 820287    | 931190   | 1524611 
    l1i_tlb:u          | 14518662  | 14603641 | 13673424
    l1i_tlb_refill:u   | 670459    | 670446   | 660164  
    l2i_cache:u        | 820287    | 931189   | 1524609 
    l2i_cache_refill:u | 67314     | 40245    | 273130  
    l2i_tlb:u          | 670708    | 670593   | 660319  
    l2i_tlb_refill:u   | 116       | 39       | 186     
    l1d_cache:u        | 6291114   | 6289231  | 6339111 
    l1d_cache_refill:u | 1239300   | 1236405  | 1247528 
    l1d_tlb:u          | 9310294   | 9318839  | 9399298 
    l1d_tlb_refill:u   | 1102497   | 1102534  | 1100396 
    l2d_cache:u        | 5185452   | 5293759  | 5117032 
    l2d_cache_refill:u | 1490475   | 1562909  | 1382876 
    l2d_tlb:u          | 1106057   | 1107131  | 1101386 
    l2d_tlb_refill:u   | 65        | 47       | 180     
    ll_cache:u         | 1426904   | 1523810  | 1238114 
    ll_cache_miss:u    | 9570      | 13837    | 269     

== combo_036_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lstr_p512_np8_l1_sl5
    s1 | hot_b128_bp3_r100_lin_p1_np2_l1                
    s2 | itlb_f64_l1_r100_lin_p128_np2_l2               
single_counts:
    metric             | s0        | s1       | s2      
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 101725608 | 10372749 | 72440670
    instructions:u     | 36150988  | 22161064 | 11930997
    br_retired:u       | 3911403   | 3941409  | 731404  
    br_mis_pred:u      | 1231787   | 429      | 454     
    l1i_cache:u        | 16913904  | 2856059  | 1592286 
    l1i_cache_refill:u | 905       | 703      | 1459820 
    l1i_tlb:u          | 16913904  | 2856059  | 1592286 
    l1i_tlb_refill:u   | 47        | 50       | 660089  
    l2i_cache:u        | 903       | 702      | 1459820 
    l2i_cache_refill:u | 774       | 627      | 364472  
    l2i_tlb:u          | 86        | 100      | 660174  
    l2i_tlb_refill:u   | 19        | 37       | 16      
    l1d_cache:u        | 7971841   | 1415190  | 1415246 
    l1d_cache_refill:u | 1225795   | 144      | 798732  
    l1d_tlb:u          | 12633754  | 1417189  | 2467359 
    l1d_tlb_refill:u   | 840073    | 63       | 660072  
    l2d_cache:u        | 6201537   | 1224     | 4203871 
    l2d_cache_refill:u | 2625301   | 839      | 1379194 
    l2d_tlb:u          | 853562    | 83       | 660099  
    l2d_tlb_refill:u   | 555       | 7        | 160     
    ll_cache:u         | 2624247   | 233      | 1107518 
    ll_cache_miss:u    | 2861      | 29       | 273     
combined_orders:
    id        | modules                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lstr_p512_np8_l1_sl5+hot_b128_bp3_r100_lin_p1_np2_l1+itlb_f64_l1_r100_lin_p128_np2_l2
    shuffle   | itlb_f64_l1_r100_lin_p128_np2_l2+hot_b128_bp3_r100_lin_p1_np2_l1+fetch_b128_d1_bp0_s16_r100_lstr_p512_np8_l1_sl5
    sum       | fetch_b128_d1_bp0_s16_r100_lstr_p512_np8_l1_sl5+hot_b128_bp3_r100_lin_p1_np2_l1+itlb_f64_l1_r100_lin_p128_np2_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 203790549 | 285902364 | 184539027
    instructions:u     | 70221597  | 70221698  | 70243049 
    br_retired:u       | 8581804   | 8581813   | 8584216  
    br_mis_pred:u      | 1231736   | 1231462   | 1232670  
    l1i_cache:u        | 23754213  | 23789612  | 21362249 
    l1i_cache_refill:u | 903368    | 1072578   | 1461428  
    l1i_tlb:u          | 23754213  | 23789612  | 21362249 
    l1i_tlb_refill:u   | 660760    | 660756    | 660186   
    l2i_cache:u        | 903367    | 1072577   | 1461425  
    l2i_cache_refill:u | 295341    | 343611    | 365873   
    l2i_tlb:u          | 660837    | 660822    | 660360   
    l2i_tlb_refill:u   | 348       | 404       | 72       
    l1d_cache:u        | 10713936  | 10691330  | 10802277 
    l1d_cache_refill:u | 2162033   | 2174138   | 2024671  
    l1d_tlb:u          | 16187410  | 16231220  | 16518302 
    l1d_tlb_refill:u   | 1490183   | 1490185   | 1500208  
    l2d_cache:u        | 11262923  | 11126877  | 10406632 
    l2d_cache_refill:u | 4465495   | 4351751   | 4005334  
    l2d_tlb:u          | 1499863   | 1500861   | 1513744  
    l2d_tlb_refill:u   | 2282      | 2256      | 722      
    ll_cache:u         | 4047477   | 4074686   | 3731998  
    ll_cache_miss:u    | 10431     | 7573      | 3163     

== combo_037_s3 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b64_d4_bitrev_rand_p16_np1_l1    
    s1 | hot_b128_bp3_r100_lstr_p128_np4_l1_sl3
    s2 | itlb_f128_l1_r100_lstr_p128_np8_l4_sl3
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 8869000  | 39311975 | 225058626
    instructions:u     | 12951049 | 22160997 | 26011007 
    br_retired:u       | 1031410  | 3941404  | 1371406  
    br_mis_pred:u      | 130613   | 364      | 472      
    l1i_cache:u        | 3701928  | 2849516  | 3698077  
    l1i_cache_refill:u | 684      | 847      | 3242438  
    l1i_tlb:u          | 3701928  | 2849516  | 3698077  
    l1i_tlb_refill:u   | 48       | 44       | 1310059  
    l2i_cache:u        | 683      | 845      | 3242435  
    l2i_cache_refill:u | 616      | 633      | 1765594  
    l2i_tlb:u          | 86       | 79       | 1310097  
    l2i_tlb_refill:u   | 15       | 13       | 34       
    l1d_cache:u        | 1535192  | 1416254  | 5255602  
    l1d_cache_refill:u | 176      | 1211867  | 2230323  
    l1d_tlb:u          | 1537284  | 2457929  | 8042765  
    l1d_tlb_refill:u   | 97       | 980063   | 1940080  
    l2d_cache:u        | 1341     | 3700797  | 15061704 
    l2d_cache_refill:u | 869      | 1145674  | 4569573  
    l2d_tlb:u          | 123      | 980286   | 1940132  
    l2d_tlb_refill:u   | 13       | 150      | 167      
    ll_cache:u         | 294      | 1144947  | 3206355  
    ll_cache_miss:u    | 25       | 240      | 573      
combined_orders:
    id        | modules                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_rand_p16_np1_l1+hot_b128_bp3_r100_lstr_p128_np4_l1_sl3+itlb_f128_l1_r100_lstr_p128_np8_l4_sl3
    shuffle   | hot_b128_bp3_r100_lstr_p128_np4_l1_sl3+cold_b64_d4_bitrev_rand_p16_np1_l1+itlb_f128_l1_r100_lstr_p128_np8_l4_sl3
    sum       | cold_b64_d4_bitrev_rand_p16_np1_l1+hot_b128_bp3_r100_lstr_p128_np4_l1_sl3+itlb_f128_l1_r100_lstr_p128_np8_l4_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 263882695 | 272331802 | 273239601
    instructions:u     | 61101689  | 61101689  | 61123053 
    br_retired:u       | 6341812   | 6341812   | 6344220  
    br_mis_pred:u      | 135298    | 131109    | 131449   
    l1i_cache:u        | 9937864   | 9916579   | 10249521 
    l1i_cache_refill:u | 2895255   | 2837540   | 3243969  
    l1i_tlb:u          | 9937864   | 9916579   | 10249521 
    l1i_tlb_refill:u   | 1300554   | 1300549   | 1310151  
    l2i_cache:u        | 2895253   | 2837537   | 3243963  
    l2i_cache_refill:u | 1359871   | 1458593   | 1766843  
    l2i_tlb:u          | 1300598   | 1300589   | 1310262  
    l2i_tlb_refill:u   | 35        | 50        | 62       
    l1d_cache:u        | 8199153   | 8196919   | 8207048  
    l1d_cache_refill:u | 3545987   | 3528604   | 3442366  
    l1d_tlb:u          | 12026962  | 11984429  | 12037978 
    l1d_tlb_refill:u   | 2921765   | 2921893   | 2920240  
    l2d_cache:u        | 19924709  | 20913206  | 18763842 
    l2d_cache_refill:u | 6382273   | 7149027   | 5716116  
    l2d_tlb:u          | 2922236   | 2922221   | 2920541  
    l2d_tlb_refill:u   | 358       | 314       | 330      
    ll_cache:u         | 5005080   | 5596189   | 4351596  
    ll_cache_miss:u    | 4048      | 4318      | 838      

== combo_038_s3 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp17      
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p16_np8_l1_sl5
    s2 | hot_b128_bp3_r100_lstr_p512_np2_l4_sl3        
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 27929195 | 45886923 | 247781512
    instructions:u     | 12950997 | 36150988 | 26001007 
    br_retired:u       | 1031404  | 3911403  | 3941406  
    br_mis_pred:u      | 130622   | 1231065  | 463      
    l1i_cache:u        | 3673252  | 17043834 | 3349144  
    l1i_cache_refill:u | 658      | 884      | 1212     
    l1i_tlb:u          | 3673252  | 17043834 | 3349144  
    l1i_tlb_refill:u   | 46       | 54       | 44       
    l2i_cache:u        | 658      | 883      | 1211     
    l2i_cache_refill:u | 569      | 748      | 665      
    l2i_tlb:u          | 80       | 115      | 171      
    l2i_tlb_refill:u   | 15       | 40       | 22       
    l1d_cache:u        | 1535711  | 7985024  | 5259006  
    l1d_cache_refill:u | 591030   | 382287   | 5119835  
    l1d_tlb:u          | 2307078  | 11585682 | 10483180 
    l1d_tlb_refill:u   | 664172   | 170      | 5143749  
    l2d_cache:u        | 1937605  | 1359542  | 20226720 
    l2d_cache_refill:u | 565704   | 1220     | 10251500 
    l2d_tlb:u          | 666884   | 200      | 5144619  
    l2d_tlb_refill:u   | 13       | 3        | 546      
    ll_cache:u         | 565118   | 488      | 10250648 
    ll_cache_miss:u    | 1630     | 68       | 1442     
combined_orders:
    id        | modules                                                                                                                       
    ----------+-------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp17+fetch_b128_d1_bp0_s16_r100_lstr_p16_np8_l1_sl5+hot_b128_bp3_r100_lstr_p512_np2_l4_sl3
    shuffle   | hot_b128_bp3_r100_lstr_p512_np2_l4_sl3+cold_b64_d4_bitrev_pstr_p128_np4_l1_sp17+fetch_b128_d1_bp0_s16_r100_lstr_p16_np8_l1_sl5
    sum       | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp17+fetch_b128_d1_bp0_s16_r100_lstr_p16_np8_l1_sl5+hot_b128_bp3_r100_lstr_p512_np2_l4_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 359104235 | 456451112 | 321597630
    instructions:u     | 75081548  | 75081542  | 75102992 
    br_retired:u       | 8881790   | 8881792   | 8884213  
    br_mis_pred:u      | 1362270   | 1361866   | 1362150  
    l1i_cache:u        | 26078366  | 26027744  | 24066230 
    l1i_cache_refill:u | 3824      | 4088      | 2754     
    l1i_tlb:u          | 26078366  | 26027744  | 24066230 
    l1i_tlb_refill:u   | 64        | 53        | 144      
    l2i_cache:u        | 3823      | 4089      | 2752     
    l2i_cache_refill:u | 1597      | 1505      | 1982     
    l2i_tlb:u          | 188       | 88        | 366      
    l2i_tlb_refill:u   | 39        | 30        | 77       
    l1d_cache:u        | 14632014  | 14634866  | 14779741 
    l1d_cache_refill:u | 6158385   | 6127857   | 6093152  
    l1d_tlb:u          | 24335233  | 24234305  | 24375940 
    l1d_tlb_refill:u   | 5820073   | 5806308   | 5808091  
    l2d_cache:u        | 25193462  | 25142471  | 23523867 
    l2d_cache_refill:u | 10991567  | 11101593  | 10818424 
    l2d_tlb:u          | 5823811   | 5808479   | 5811703  
    l2d_tlb_refill:u   | 238       | 939       | 562      
    ll_cache:u         | 10989784  | 11099306  | 10816254 
    ll_cache_miss:u    | 5982      | 31871     | 3140     

== combo_039_s3 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b128_d4_bitrev_lin_p512_np2_l2   
    s1 | hot_b64_bp3_r100_pstr_p512_np1_l1_sp33
    s2 | itlb_f128_l1_r100_lstr_p1_np4_l4_sl5  
single_counts:
    metric             | s0        | s1       | s2      
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 128998995 | 36435269 | 79046101
    instructions:u     | 26870997  | 11280997 | 26010988
    br_retired:u       | 1991404   | 2021404  | 1371403 
    br_mis_pred:u      | 290712    | 469      | 529     
    l1i_cache:u        | 7746906   | 1489880  | 3640942 
    l1i_cache_refill:u | 1184      | 672      | 2868238 
    l1i_tlb:u          | 7746906   | 1489880  | 3640942 
    l1i_tlb_refill:u   | 52        | 52       | 1310076 
    l2i_cache:u        | 1184      | 671      | 2868236 
    l2i_cache_refill:u | 834       | 564      | 900040  
    l2i_tlb:u          | 88        | 173      | 1310145 
    l2i_tlb_refill:u   | 23        | 44       | 174     
    l1d_cache:u        | 4261071   | 775864   | 5255385 
    l1d_cache_refill:u | 1827163   | 640105   | 365     
    l1d_tlb:u          | 5739811   | 1515065  | 5257286 
    l1d_tlb_refill:u   | 1310065   | 663353   | 70      
    l2d_cache:u        | 11234317  | 2529106  | 2729994 
    l2d_cache_refill:u | 5445427   | 1281899  | 803136  
    l2d_tlb:u          | 1310275   | 663618   | 91      
    l2d_tlb_refill:u   | 638       | 84       | 15      
    ll_cache:u         | 5443988   | 1281310  | 539     
    ll_cache_miss:u    | 65421     | 56       | 27      
combined_orders:
    id        | modules                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lin_p512_np2_l2+hot_b64_bp3_r100_pstr_p512_np1_l1_sp33+itlb_f128_l1_r100_lstr_p1_np4_l4_sl5
    shuffle   | hot_b64_bp3_r100_pstr_p512_np1_l1_sp33+cold_b128_d4_bitrev_lin_p512_np2_l2+itlb_f128_l1_r100_lstr_p1_np4_l4_sl5
    sum       | cold_b128_d4_bitrev_lin_p512_np2_l2+hot_b64_bp3_r100_pstr_p512_np1_l1_sp33+itlb_f128_l1_r100_lstr_p1_np4_l4_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 318169931 | 273928461 | 244480365
    instructions:u     | 64141695  | 64141689  | 64162982 
    br_retired:u       | 5381810   | 5381812   | 5384211  
    br_mis_pred:u      | 290924    | 291014    | 291710   
    l1i_cache:u        | 12313934  | 12308162  | 12877728 
    l1i_cache_refill:u | 3098283   | 2941355   | 2870094  
    l1i_tlb:u          | 12313934  | 12308162  | 12877728 
    l1i_tlb_refill:u   | 1310552   | 1310545   | 1310180  
    l2i_cache:u        | 3098281   | 2941354   | 2870091  
    l2i_cache_refill:u | 1079872   | 911197    | 901438   
    l2i_tlb:u          | 1310841   | 1310765   | 1310406  
    l2i_tlb_refill:u   | 7050      | 7161      | 241      
    l1d_cache:u        | 10279885  | 10279054  | 10292320 
    l1d_cache_refill:u | 2532369   | 2536445   | 2467633  
    l1d_tlb:u          | 12584815  | 12667046  | 12512162 
    l1d_tlb_refill:u   | 1974744   | 1989731   | 1973488  
    l2d_cache:u        | 17541693  | 17499136  | 16493417 
    l2d_cache_refill:u | 8073149   | 8016294   | 7530462  
    l2d_tlb:u          | 1975409   | 1990235   | 1973984  
    l2d_tlb_refill:u   | 32126     | 34979     | 737      
    ll_cache:u         | 6930865   | 7134428   | 6725837  
    ll_cache_miss:u    | 66416     | 120166    | 65504    

== combo_040_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p16_np1_l2              
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p16_np1_l4_sp17
    s2 | hot_b64_bp3_r100_rand_p1_np8_l1                
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 12164236 | 58582598 | 5242609 
    instructions:u     | 13591049 | 39990988 | 11281040
    br_retired:u       | 1031410  | 3911403  | 2021409 
    br_mis_pred:u      | 130437   | 1231140  | 377     
    l1i_cache:u        | 3782443  | 17202718 | 1495552 
    l1i_cache_refill:u | 708      | 953      | 564     
    l1i_tlb:u          | 3782443  | 17202718 | 1495552 
    l1i_tlb_refill:u   | 53       | 55       | 49      
    l2i_cache:u        | 707      | 953      | 564     
    l2i_cache_refill:u | 632      | 787      | 521     
    l2i_tlb:u          | 101      | 126      | 96      
    l2i_tlb_refill:u   | 44       | 43       | 42      
    l1d_cache:u        | 2175246  | 11700619 | 775171  
    l1d_cache_refill:u | 50184    | 42718    | 158     
    l1d_tlb:u          | 2177295  | 15355550 | 777161  
    l1d_tlb_refill:u   | 97       | 188      | 59      
    l2d_cache:u        | 91234    | 101752   | 1224    
    l2d_cache_refill:u | 831      | 988      | 790     
    l2d_tlb:u          | 119      | 211      | 91      
    l2d_tlb_refill:u   | 5        | 10       | 3       
    ll_cache:u         | 224      | 283      | 245     
    ll_cache_miss:u    | 21       | 11       | 13      
combined_orders:
    id        | modules                                                                                                          
    ----------+------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p16_np1_l2+fetch_b128_d1_bp0_s16_r100_pstr_p16_np1_l4_sp17+hot_b64_bp3_r100_rand_p1_np8_l1
    shuffle   | hot_b64_bp3_r100_rand_p1_np8_l1+fetch_b128_d1_bp0_s16_r100_pstr_p16_np1_l4_sp17+cold_b64_d4_bitrev_lin_p16_np1_l2
    sum       | cold_b64_d4_bitrev_lin_p16_np1_l2+fetch_b128_d1_bp0_s16_r100_pstr_p16_np1_l4_sp17+hot_b64_bp3_r100_rand_p1_np8_l1
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 77226788  | 77231385 | 75989443
    instructions:u     | 64841588  | 64841588 | 64863077
    br_retired:u       | 6961803   | 6961803  | 6964222 
    br_mis_pred:u      | 1361496   | 1363086  | 1361954 
    l1i_cache:u        | 24641269  | 24662689 | 22480713
    l1i_cache_refill:u | 1470      | 1807     | 2225    
    l1i_tlb:u          | 24641269  | 24662689 | 22480713
    l1i_tlb_refill:u   | 53        | 56       | 157     
    l2i_cache:u        | 1469      | 1806     | 2224    
    l2i_cache_refill:u | 891       | 936      | 1940    
    l2i_tlb:u          | 177       | 98       | 323     
    l2i_tlb_refill:u   | 12        | 17       | 129     
    l1d_cache:u        | 14606702  | 14606433 | 14651036
    l1d_cache_refill:u | 52641     | 52993    | 93060   
    l1d_tlb:u          | 18246747  | 18246697 | 18310006
    l1d_tlb_refill:u   | 3789      | 3790     | 344     
    l2d_cache:u        | 90658     | 90456    | 194210  
    l2d_cache_refill:u | 1599      | 1328     | 2609    
    l2d_tlb:u          | 3917      | 3918     | 421     
    l2d_tlb_refill:u   | 58        | 16       | 18      
    ll_cache:u         | 555       | 419      | 752     
    ll_cache_miss:u    | 31        | 22       | 45      

== combo_041_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_rand_p16_np1_l4            
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l4_sp33
    s2 | itlb_f128_l1_r100_lin_p512_np8_l4              
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 34120280 | 60180987 | 190514230
    instructions:u     | 29431006 | 39990988 | 26010997 
    br_retired:u       | 1991405  | 3911403  | 1371404  
    br_mis_pred:u      | 290662   | 1231092  | 518      
    l1i_cache:u        | 8068455  | 17424222 | 3665872  
    l1i_cache_refill:u | 922      | 1130     | 2914579  
    l1i_tlb:u          | 8068455  | 17424222 | 3665872  
    l1i_tlb_refill:u   | 57       | 50       | 1310057  
    l2i_cache:u        | 921      | 1130     | 2914576  
    l2i_cache_refill:u | 798      | 761      | 1319773  
    l2i_tlb:u          | 106      | 82       | 1310117  
    l2i_tlb_refill:u   | 47       | 13       | 282      
    l1d_cache:u        | 6815572  | 11695631 | 5255861  
    l1d_cache_refill:u | 199      | 230570   | 1303987  
    l1d_tlb:u          | 6818041  | 15350904 | 6165443  
    l1d_tlb_refill:u   | 130      | 190      | 660076   
    l2d_cache:u        | 1877     | 1418353  | 20434119 
    l2d_cache_refill:u | 1219     | 1419     | 9088902  
    l2d_tlb:u          | 156      | 217      | 660114   
    l2d_tlb_refill:u   | 43       | 44       | 850      
    ll_cache:u         | 402      | 593      | 7806409  
    ll_cache_miss:u    | 40       | 166      | 20738    
combined_orders:
    id        | modules                                                                                                              
    ----------+----------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_rand_p16_np1_l4+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l4_sp33+itlb_f128_l1_r100_lin_p512_np8_l4
    shuffle   | fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l4_sp33+cold_b128_d4_bitrev_rand_p16_np1_l4+itlb_f128_l1_r100_lin_p512_np8_l4
    sum       | cold_b128_d4_bitrev_rand_p16_np1_l4+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l4_sp33+itlb_f128_l1_r100_lin_p512_np8_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 259527733 | 279715163 | 284815497
    instructions:u     | 95411613  | 95411698  | 95432991 
    br_retired:u       | 7271804   | 7271813   | 7274212  
    br_mis_pred:u      | 1521504   | 1521538   | 1522272  
    l1i_cache:u        | 30754544  | 30812819  | 29158549 
    l1i_cache_refill:u | 2960480   | 2949508   | 2916631  
    l1i_tlb:u          | 30754544  | 30812819  | 29158549 
    l1i_tlb_refill:u   | 1301071   | 1301084   | 1310164  
    l2i_cache:u        | 2960476   | 2949509   | 2916627  
    l2i_cache_refill:u | 1134354   | 1270502   | 1321332  
    l2i_tlb:u          | 1301135   | 1301191   | 1310305  
    l2i_tlb_refill:u   | 89        | 545       | 342      
    l1d_cache:u        | 23729024  | 23719420  | 23767064 
    l1d_cache_refill:u | 1596380   | 1573118   | 1534756  
    l1d_tlb:u          | 28263210  | 28252704  | 28334388 
    l1d_tlb_refill:u   | 663763    | 663783    | 660396   
    l2d_cache:u        | 22538587  | 22376920  | 21854349 
    l2d_cache_refill:u | 9271790   | 9173114   | 9091540  
    l2d_tlb:u          | 663793    | 663918    | 660487   
    l2d_tlb_refill:u   | 230       | 210       | 937      
    ll_cache:u         | 7992976   | 7879379   | 7807404  
    ll_cache_miss:u    | 33848     | 85104     | 20944    

== combo_042_s3 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p16_np1_l1            
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p1_np8_l2_sl9
    s2 | itlb_f128_l1_r100_pstr_p512_np1_l1_sp33      
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 8894203  | 50061692 | 196995308
    instructions:u     | 12951049 | 37430997 | 22170997 
    br_retired:u       | 1031410  | 3911404  | 1371404  
    br_mis_pred:u      | 130633   | 1230495  | 458      
    l1i_cache:u        | 3699832  | 19337876 | 2978993  
    l1i_cache_refill:u | 708      | 893      | 3002898  
    l1i_tlb:u          | 3699832  | 19337876 | 2978993  
    l1i_tlb_refill:u   | 52       | 49       | 1300056  
    l2i_cache:u        | 707      | 892      | 3002895  
    l2i_cache_refill:u | 635      | 713      | 1871453  
    l2i_tlb:u          | 104      | 85       | 1300115  
    l2i_tlb_refill:u   | 32       | 17       | 91       
    l1d_cache:u        | 1535326  | 9095670  | 1415852  
    l1d_cache_refill:u | 617      | 142      | 1279872  
    l1d_tlb:u          | 1537615  | 12739103 | 2804477  
    l1d_tlb_refill:u   | 95       | 64       | 1304943  
    l2d_cache:u        | 2719     | 1845     | 7691037  
    l2d_cache_refill:u | 1000     | 1048     | 4295375  
    l2d_tlb:u          | 124      | 88       | 1304967  
    l2d_tlb_refill:u   | 50       | 33       | 143      
    ll_cache:u         | 345      | 326      | 2564970  
    ll_cache_miss:u    | 76       | 28       | 122      
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p16_np1_l1+fetch_b128_d1_bp0_s16_r100_lstr_p1_np8_l2_sl9+itlb_f128_l1_r100_pstr_p512_np1_l1_sp33
    shuffle   | cold_b64_d4_bitrev_lin_p16_np1_l1+itlb_f128_l1_r100_pstr_p512_np1_l1_sp33+fetch_b128_d1_bp0_s16_r100_lstr_p1_np8_l2_sl9
    sum       | cold_b64_d4_bitrev_lin_p16_np1_l1+fetch_b128_d1_bp0_s16_r100_lstr_p1_np8_l2_sl9+itlb_f128_l1_r100_pstr_p512_np1_l1_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 190381404 | 293353473 | 255951203
    instructions:u     | 72531603  | 72531698  | 72553043 
    br_retired:u       | 6311802   | 6311813   | 6314218  
    br_mis_pred:u      | 1361874   | 1361883   | 1361586  
    l1i_cache:u        | 25766080  | 25770665  | 26016701 
    l1i_cache_refill:u | 2743872   | 3099033   | 3004499  
    l1i_tlb:u          | 25766080  | 25770665  | 26016701 
    l1i_tlb_refill:u   | 1300770   | 1300756   | 1300157  
    l2i_cache:u        | 2743865   | 3099032   | 3004494  
    l2i_cache_refill:u | 1779648   | 1963905   | 1872801  
    l2i_tlb:u          | 1300809   | 1300809   | 1300304  
    l2i_tlb_refill:u   | 74        | 275       | 140      
    l1d_cache:u        | 12047359  | 12037792  | 12046848 
    l1d_cache_refill:u | 1275098   | 1276451   | 1280631  
    l1d_tlb:u          | 17065520  | 17087378  | 17081195 
    l1d_tlb_refill:u   | 1306177   | 1308917   | 1305102  
    l2d_cache:u        | 8119809   | 8061267   | 7695601  
    l2d_cache_refill:u | 4609416   | 4534050   | 4297423  
    l2d_tlb:u          | 1306304   | 1309033   | 1305179  
    l2d_tlb_refill:u   | 624       | 196       | 226      
    ll_cache:u         | 2665757   | 2638575   | 2565641  
    ll_cache_miss:u    | 4108      | 31440     | 226      

== combo_043_s3 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_rand_p1_np2_l1            
    s1 | fetch_b64_d1_bp0_s16_r100_lstr_p512_np2_l2_sl5
    s2 | hot_b64_bp3_r100_rand_p512_np4_l1             
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 18161947 | 90364769 | 44923085
    instructions:u     | 25591040 | 18870994 | 11280997
    br_retired:u       | 1991409  | 1991401  | 2021404 
    br_mis_pred:u      | 290626   | 592955   | 458     
    l1i_cache:u        | 6987962  | 8590879  | 1500512 
    l1i_cache_refill:u | 826      | 748      | 673     
    l1i_tlb:u          | 6987962  | 8590879  | 1500512 
    l1i_tlb_refill:u   | 47       | 52       | 50      
    l2i_cache:u        | 826      | 747      | 673     
    l2i_cache_refill:u | 712      | 632      | 571     
    l2i_tlb:u          | 79       | 105      | 170     
    l2i_tlb_refill:u   | 14       | 44       | 46      
    l1d_cache:u        | 2975541  | 4731977  | 776152  
    l1d_cache_refill:u | 160      | 1285073  | 637837  
    l1d_tlb:u          | 2977850  | 8096617  | 1475153 
    l1d_tlb_refill:u   | 64       | 1322689  | 635085  
    l2d_cache:u        | 1632     | 5085307  | 2576812 
    l2d_cache_refill:u | 1153     | 2566232  | 1298482 
    l2d_tlb:u          | 87       | 1335578  | 635269  
    l2d_tlb_refill:u   | 34       | 441      | 614     
    ll_cache:u         | 349      | 2565443  | 1297765 
    ll_cache_miss:u    | 50       | 836      | 1633    
combined_orders:
    id        | modules                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_rand_p1_np2_l1+fetch_b64_d1_bp0_s16_r100_lstr_p512_np2_l2_sl5+hot_b64_bp3_r100_rand_p512_np4_l1
    shuffle   | fetch_b64_d1_bp0_s16_r100_lstr_p512_np2_l2_sl5+hot_b64_bp3_r100_rand_p512_np4_l1+cold_b128_d4_bitrev_rand_p1_np2_l1
    sum       | cold_b128_d4_bitrev_rand_p1_np2_l1+fetch_b64_d1_bp0_s16_r100_lstr_p512_np2_l2_sl5+hot_b64_bp3_r100_rand_p512_np4_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 146039356 | 167354129 | 153449801
    instructions:u     | 55721597  | 55721597  | 55743031 
    br_retired:u       | 6001804   | 6001804   | 6004214  
    br_mis_pred:u      | 882103    | 881683    | 884039   
    l1i_cache:u        | 18135414  | 18105893  | 17079353 
    l1i_cache_refill:u | 1688      | 1880      | 2247     
    l1i_tlb:u          | 18135414  | 18105893  | 17079353 
    l1i_tlb_refill:u   | 48        | 58        | 149      
    l2i_cache:u        | 1689      | 1880      | 2246     
    l2i_cache_refill:u | 1133      | 1247      | 1915     
    l2i_tlb:u          | 185       | 116       | 354      
    l2i_tlb_refill:u   | 40        | 48        | 104      
    l1d_cache:u        | 8409261   | 8419816   | 8483670  
    l1d_cache_refill:u | 1910840   | 1911561   | 1923070  
    l1d_tlb:u          | 12326169  | 12393062  | 12549620 
    l1d_tlb_refill:u   | 1943116   | 1955416   | 1957838  
    l2d_cache:u        | 8271667   | 8318777   | 7663751  
    l2d_cache_refill:u | 3984305   | 4031552   | 3865867  
    l2d_tlb:u          | 1943441   | 1964813   | 1970934  
    l2d_tlb_refill:u   | 3996      | 5094      | 1089     
    ll_cache:u         | 3982548   | 4029866   | 3863557  
    ll_cache_miss:u    | 26650     | 43892     | 2519     

== combo_044_s3 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p16_np1_l4_sp17  
    s1 | fetch_b64_d1_bp0_s16_r100_rand_p128_np8_l2
    s2 | itlb_f64_l1_r100_pstr_p16_np1_l1_sp3      
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 34639315 | 52094635 | 23852644
    instructions:u     | 29430997 | 18870988 | 11291049
    br_retired:u       | 1991404  | 1991403  | 731410  
    br_mis_pred:u      | 290661   | 591128   | 432     
    l1i_cache:u        | 8093622  | 8624781  | 1487971 
    l1i_cache_refill:u | 917      | 694      | 1423503 
    l1i_tlb:u          | 8093622  | 8624781  | 1487971 
    l1i_tlb_refill:u   | 58       | 52       | 660100  
    l2i_cache:u        | 916      | 691      | 1423503 
    l2i_cache_refill:u | 759      | 609      | 38013   
    l2i_tlb:u          | 104      | 97       | 660181  
    l2i_tlb_refill:u   | 47       | 17       | 23      
    l1d_cache:u        | 6815445  | 4703009  | 775306  
    l1d_cache_refill:u | 189      | 1232502  | 10263   
    l1d_tlb:u          | 6817687  | 7668545  | 777181  
    l1d_tlb_refill:u   | 135      | 1032585  | 110     
    l2d_cache:u        | 1715     | 3971547  | 1242138 
    l2d_cache_refill:u | 1112     | 1107754  | 111741  
    l2d_tlb:u          | 155      | 1045185  | 135     
    l2d_tlb_refill:u   | 12       | 19       | 44      
    ll_cache:u         | 394      | 1107095  | 10548   
    ll_cache_miss:u    | 30       | 481      | 42      
combined_orders:
    id        | modules                                                                                                                 
    ----------+-------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p16_np1_l4_sp17+fetch_b64_d1_bp0_s16_r100_rand_p128_np8_l2+itlb_f64_l1_r100_pstr_p16_np1_l1_sp3
    shuffle   | cold_b128_d4_bitrev_pstr_p16_np1_l4_sp17+itlb_f64_l1_r100_pstr_p16_np1_l1_sp3+fetch_b64_d1_bp0_s16_r100_rand_p128_np8_l2
    sum       | cold_b128_d4_bitrev_pstr_p16_np1_l4_sp17+fetch_b64_d1_bp0_s16_r100_rand_p128_np8_l2+itlb_f64_l1_r100_pstr_p16_np1_l1_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 108816900 | 114424680 | 110586594
    instructions:u     | 59571597  | 59571597  | 59593034 
    br_retired:u       | 4711804   | 4711804   | 4714217  
    br_mis_pred:u      | 881642    | 881762    | 882221   
    l1i_cache:u        | 18632470  | 18709334  | 18206374 
    l1i_cache_refill:u | 1053228   | 1304217   | 1425114  
    l1i_tlb:u          | 18632470  | 18709334  | 18206374 
    l1i_tlb_refill:u   | 660808    | 660757    | 660210   
    l2i_cache:u        | 1053229   | 1304216   | 1425110  
    l2i_cache_refill:u | 39082     | 121773    | 39381    
    l2i_tlb:u          | 660929    | 660865    | 660382   
    l2i_tlb_refill:u   | 112       | 122       | 87       
    l1d_cache:u        | 12215422  | 12224990  | 12293760 
    l1d_cache_refill:u | 1247069   | 1250433   | 1242954  
    l1d_tlb:u          | 15078715  | 15085474  | 15263413 
    l1d_tlb_refill:u   | 1027898   | 1027861   | 1032830  
    l2d_cache:u        | 5297685   | 5059929   | 5215400  
    l2d_cache_refill:u | 1109801   | 1191573   | 1220607  
    l2d_tlb:u          | 1030473   | 1029096   | 1045475  
    l2d_tlb_refill:u   | 32        | 191       | 75       
    ll_cache:u         | 1073568   | 1133392   | 1118037  
    ll_cache_miss:u    | 413       | 3227      | 553      

== combo_045_s3 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_rand_p1_np2_l1            
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p16_np8_l2_sl5
    s2 | itlb_f128_l1_r100_lstr_p128_np4_l2_sl9        
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 18161094 | 50831841 | 198488599
    instructions:u     | 25591046 | 37430988 | 23451003 
    br_retired:u       | 1991407  | 3911403  | 1371402  
    br_mis_pred:u      | 290602   | 1231072  | 468      
    l1i_cache:u        | 6987733  | 16962782 | 3401486  
    l1i_cache_refill:u | 828      | 832      | 2965657  
    l1i_tlb:u          | 6987733  | 16962782 | 3401486  
    l1i_tlb_refill:u   | 47       | 50       | 1310073  
    l2i_cache:u        | 827      | 831      | 2965654  
    l2i_cache_refill:u | 655      | 685      | 1396362  
    l2i_tlb:u          | 77       | 82       | 1310133  
    l2i_tlb_refill:u   | 11       | 14       | 29       
    l1d_cache:u        | 2975475  | 9125585  | 2695724  
    l1d_cache_refill:u | 169      | 462018   | 2480731  
    l1d_tlb:u          | 2977740  | 12777897 | 5372670  
    l1d_tlb_refill:u   | 65       | 177      | 2584718  
    l2d_cache:u        | 1632     | 1487947  | 11031765 
    l2d_cache_refill:u | 1123     | 1196     | 4297965  
    l2d_tlb:u          | 84       | 203      | 2584790  
    l2d_tlb_refill:u   | 29       | 6        | 31       
    ll_cache:u         | 334      | 527      | 2879086  
    ll_cache_miss:u    | 47       | 72       | 241      
combined_orders:
    id        | modules                                                                                                                 
    ----------+-------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_rand_p1_np2_l1+fetch_b128_d1_bp0_s16_r100_lstr_p16_np8_l2_sl5+itlb_f128_l1_r100_lstr_p128_np4_l2_sl9
    shuffle   | itlb_f128_l1_r100_lstr_p128_np4_l2_sl9+fetch_b128_d1_bp0_s16_r100_lstr_p16_np8_l2_sl5+cold_b128_d4_bitrev_rand_p1_np2_l1
    sum       | cold_b128_d4_bitrev_rand_p1_np2_l1+fetch_b128_d1_bp0_s16_r100_lstr_p16_np8_l2_sl5+itlb_f128_l1_r100_lstr_p128_np4_l2_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 270428852 | 258789198 | 267481534
    instructions:u     | 86451689  | 86451598  | 86473037 
    br_retired:u       | 7271812   | 7271805   | 7274212  
    br_mis_pred:u      | 1521538   | 1521886   | 1522142  
    l1i_cache:u        | 29750360  | 29728876  | 27352001 
    l1i_cache_refill:u | 3014643   | 2988963   | 2967317  
    l1i_tlb:u          | 29750360  | 29728876  | 27352001 
    l1i_tlb_refill:u   | 1300978   | 1300947   | 1310170  
    l2i_cache:u        | 3014639   | 2988963   | 2967312  
    l2i_cache_refill:u | 1477682   | 1376909   | 1397702  
    l2i_tlb:u          | 1301047   | 1300990   | 1310292  
    l2i_tlb_refill:u   | 178       | 41        | 54       
    l1d_cache:u        | 14758739  | 14768520  | 14796784 
    l1d_cache_refill:u | 2873808   | 2832061   | 2942918  
    l1d_tlb:u          | 21081758  | 21087816  | 21128307 
    l1d_tlb_refill:u   | 2588351   | 2588480   | 2584960  
    l2d_cache:u        | 15358655  | 15135223  | 12521344 
    l2d_cache_refill:u | 4574862   | 4553744   | 4300284  
    l2d_tlb:u          | 2588479   | 2588621   | 2585077  
    l2d_tlb_refill:u   | 41        | 160       | 66       
    ll_cache:u         | 3086599   | 3107736   | 2879947  
    ll_cache_miss:u    | 1253      | 1949      | 360      

== combo_046_s3 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp33
    s1 | fetch_b64_d1_bp0_s16_r100_rand_p1_np2_l2
    s2 | hot_b128_bp3_r100_lshuf_p1_np4_l1       
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 25439452 | 24282199 | 10361489
    instructions:u     | 12951049 | 18871040 | 22161040
    br_retired:u       | 1031410  | 1991409  | 3941409 
    br_mis_pred:u      | 130635   | 591101   | 466     
    l1i_cache:u        | 3687100  | 9623270  | 2856511 
    l1i_cache_refill:u | 686      | 713      | 689     
    l1i_tlb:u          | 3687100  | 9623270  | 2856511 
    l1i_tlb_refill:u   | 43       | 53       | 55      
    l2i_cache:u        | 686      | 711      | 689     
    l2i_cache_refill:u | 589      | 622      | 609     
    l2i_tlb:u          | 73       | 95       | 94      
    l2i_tlb_refill:u   | 14       | 33       | 23      
    l1d_cache:u        | 1535954  | 4625350  | 1415224 
    l1d_cache_refill:u | 608942   | 150      | 157     
    l1d_tlb:u          | 2377892  | 6348773  | 1417230 
    l1d_tlb_refill:u   | 680074   | 57       | 58      
    l2d_cache:u        | 2090957  | 1269     | 1186    
    l2d_cache_refill:u | 680662   | 806      | 803     
    l2d_tlb:u          | 680219   | 77       | 119     
    l2d_tlb_refill:u   | 27       | 6        | 4       
    ll_cache:u         | 680045   | 237      | 229     
    ll_cache_miss:u    | 202      | 12       | 25      
combined_orders:
    id        | modules                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp33+fetch_b64_d1_bp0_s16_r100_rand_p1_np2_l2+hot_b128_bp3_r100_lshuf_p1_np4_l1
    shuffle   | fetch_b64_d1_bp0_s16_r100_rand_p1_np2_l2+hot_b128_bp3_r100_lshuf_p1_np4_l1+cold_b64_d4_bitrev_pstr_p128_np4_l1_sp33
    sum       | cold_b64_d4_bitrev_pstr_p128_np4_l1_sp33+fetch_b64_d1_bp0_s16_r100_rand_p1_np2_l2+hot_b128_bp3_r100_lshuf_p1_np4_l1
combined_counts:
    metric             | canonical | shuffle  | sum     
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 62124247  | 61203890 | 60083140
    instructions:u     | 53961603  | 53961597 | 53983129
    br_retired:u       | 6961802   | 6961804  | 6964228 
    br_mis_pred:u      | 724179    | 722180   | 722202  
    l1i_cache:u        | 15904462  | 15910683 | 16166881
    l1i_cache_refill:u | 1546      | 1386     | 2088    
    l1i_tlb:u          | 15904462  | 15910683 | 16166881
    l1i_tlb_refill:u   | 52        | 57       | 151     
    l2i_cache:u        | 1546      | 1385     | 2086    
    l2i_cache_refill:u | 989       | 940      | 1820    
    l2i_tlb:u          | 181       | 120      | 262     
    l2i_tlb_refill:u   | 20        | 47       | 70      
    l1d_cache:u        | 7572333   | 7568032  | 7576528 
    l1d_cache_refill:u | 605505    | 591960   | 609249  
    l1d_tlb:u          | 10081272  | 10075189 | 10143895
    l1d_tlb_refill:u   | 663019    | 663638   | 680189  
    l2d_cache:u        | 1946828   | 2071762  | 2093412 
    l2d_cache_refill:u | 534314    | 634951   | 682271  
    l2d_tlb:u          | 666109    | 664220   | 680415  
    l2d_tlb_refill:u   | 16        | 21       | 37      
    ll_cache:u         | 533339    | 634060   | 680511  
    ll_cache_miss:u    | 635       | 720      | 239     

== combo_047_s3 ==
single_modules:
    id | module                                   
    ---+------------------------------------------
    s0 | fetch_b64_d1_bp0_s16_r100_lin_p128_np1_l2
    s1 | hot_b64_bp3_r100_lshuf_p128_np8_l1       
    s2 | itlb_f128_l1_r100_lstr_p512_np8_l2_sl9   
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 58667694 | 13700418 | 201316554
    instructions:u     | 18870988 | 11281049 | 23450997 
    br_retired:u       | 1991403  | 2021410  | 1371404  
    br_mis_pred:u      | 593661   | 536      | 478      
    l1i_cache:u        | 8730937  | 1487904  | 3238567  
    l1i_cache_refill:u | 818      | 640      | 2869702  
    l1i_tlb:u          | 8730937  | 1487904  | 3238567  
    l1i_tlb_refill:u   | 43       | 52       | 1310061  
    l2i_cache:u        | 817      | 640      | 2869699  
    l2i_cache_refill:u | 609      | 578      | 730030   
    l2i_tlb:u          | 85       | 167      | 1310120  
    l2i_tlb_refill:u   | 15       | 33       | 94       
    l1d_cache:u        | 4683060  | 775339   | 2695952  
    l1d_cache_refill:u | 1254657  | 379817   | 2560555  
    l1d_tlb:u          | 7973396  | 955459   | 5419179  
    l1d_tlb_refill:u   | 1320190  | 85084    | 2600051  
    l2d_cache:u        | 3888041  | 1923493  | 12896420 
    l2d_cache_refill:u | 1305964  | 298581   | 5980438  
    l2d_tlb:u          | 1325168  | 85109    | 2600141  
    l2d_tlb_refill:u   | 24       | 64       | 815      
    ll_cache:u         | 1305341  | 297990   | 5130519  
    ll_cache_miss:u    | 42       | 470      | 1051     
combined_orders:
    id        | modules                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp0_s16_r100_lin_p128_np1_l2+hot_b64_bp3_r100_lshuf_p128_np8_l1+itlb_f128_l1_r100_lstr_p512_np8_l2_sl9
    shuffle   | hot_b64_bp3_r100_lshuf_p128_np8_l1+fetch_b64_d1_bp0_s16_r100_lin_p128_np1_l2+itlb_f128_l1_r100_lstr_p512_np8_l2_sl9
    sum       | fetch_b64_d1_bp0_s16_r100_lin_p128_np1_l2+hot_b64_bp3_r100_lshuf_p128_np8_l1+itlb_f128_l1_r100_lstr_p512_np8_l2_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 335078945 | 386997162 | 273684666
    instructions:u     | 53581542  | 53581548  | 53603034 
    br_retired:u       | 5381792   | 5381790   | 5384217  
    br_mis_pred:u      | 591353    | 591838    | 594675   
    l1i_cache:u        | 14307095  | 14310585  | 13457408 
    l1i_cache_refill:u | 3002508   | 3179293   | 2871160  
    l1i_tlb:u          | 14307095  | 14310585  | 13457408 
    l1i_tlb_refill:u   | 1300447   | 1300458   | 1310156  
    l2i_cache:u        | 3002508   | 3179293   | 2871156  
    l2i_cache_refill:u | 1157735   | 1254841   | 731217   
    l2i_tlb:u          | 1300500   | 1300521   | 1310372  
    l2i_tlb_refill:u   | 881       | 2435      | 142      
    l1d_cache:u        | 8133274   | 8136570   | 8154351  
    l1d_cache_refill:u | 4296132   | 4269512   | 4195029  
    l1d_tlb:u          | 14303298  | 14261073  | 14348034 
    l1d_tlb_refill:u   | 3989569   | 3983063   | 4005325  
    l2d_cache:u        | 19878958  | 19692641  | 18707954 
    l2d_cache_refill:u | 8450802   | 8506803   | 7584983  
    l2d_tlb:u          | 4015205   | 3995668   | 4010418  
    l2d_tlb_refill:u   | 2712      | 2993      | 903      
    ll_cache:u         | 7259201   | 7286541   | 6733850  
    ll_cache_miss:u    | 15168     | 88352     | 1563     

== combo_048_s3 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl9 
    s1 | hot_b128_bp3_r100_lstr_p128_np2_l4_sl9
    s2 | itlb_f64_l1_r100_lin_p128_np2_l1      
single_counts:
    metric             | s0       | s1        | s2      
    -------------------+----------+-----------+---------
    cpu-cycles:u       | 8753109  | 135155094 | 38183897
    instructions:u     | 12951040 | 26000997  | 11290997
    br_retired:u       | 1031409  | 3941404   | 731404  
    br_mis_pred:u      | 130419   | 484       | 454     
    l1i_cache:u        | 3484151  | 3336180   | 1496525 
    l1i_cache_refill:u | 676      | 947       | 1091997 
    l1i_tlb:u          | 3484151  | 3336180   | 1496525 
    l1i_tlb_refill:u   | 52       | 54        | 660066  
    l2i_cache:u        | 676      | 947       | 1091996 
    l2i_cache_refill:u | 603      | 671       | 8972    
    l2i_tlb:u          | 91       | 87        | 660139  
    l2i_tlb_refill:u   | 15       | 17        | 100     
    l1d_cache:u        | 1535399  | 5257243   | 775154  
    l1d_cache_refill:u | 162      | 4916219   | 606696  
    l1d_tlb:u          | 1537580  | 10502946  | 1208790 
    l1d_tlb_refill:u   | 61       | 5159002   | 340062  
    l2d_cache:u        | 1375     | 14351745  | 3201931 
    l2d_cache_refill:u | 977      | 4083469   | 740911  
    l2d_tlb:u          | 86       | 5159426   | 340222  
    l2d_tlb_refill:u   | 32       | 9         | 25      
    ll_cache:u         | 311      | 4082775   | 708507  
    ll_cache_miss:u    | 86       | 323       | 69      
combined_orders:
    id        | modules                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl9+hot_b128_bp3_r100_lstr_p128_np2_l4_sl9+itlb_f64_l1_r100_lin_p128_np2_l1
    shuffle   | itlb_f64_l1_r100_lin_p128_np2_l1+hot_b128_bp3_r100_lstr_p128_np2_l4_sl9+cold_b64_d4_bitrev_lstr_p1_np2_l1_sl9
    sum       | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl9+hot_b128_bp3_r100_lstr_p128_np2_l4_sl9+itlb_f64_l1_r100_lin_p128_np2_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 184916381 | 232146927 | 182092100
    instructions:u     | 50221603  | 50221613  | 50243034 
    br_retired:u       | 5701802   | 5701804   | 5704217  
    br_mis_pred:u      | 131508    | 130894    | 131357   
    l1i_cache:u        | 8321314   | 8340383   | 8316856  
    l1i_cache_refill:u | 975881    | 968976    | 1093620  
    l1i_tlb:u          | 8321314   | 8340383   | 8316856  
    l1i_tlb_refill:u   | 660557    | 660553    | 660172   
    l2i_cache:u        | 975881    | 968975    | 1093619  
    l2i_cache_refill:u | 64820     | 40517     | 10246    
    l2i_tlb:u          | 660623    | 660592    | 660317   
    l2i_tlb_refill:u   | 37        | 29        | 132      
    l1d_cache:u        | 7558031   | 7558534   | 7567796  
    l1d_cache_refill:u | 5472351   | 5419179   | 5523077  
    l1d_tlb:u          | 13175816  | 13180120  | 13249316 
    l1d_tlb_refill:u   | 5480230   | 5480212   | 5499125  
    l2d_cache:u        | 17822103  | 15335861  | 17555051 
    l2d_cache_refill:u | 4992926   | 2595643   | 4825357  
    l2d_tlb:u          | 5480869   | 5480727   | 5499734  
    l2d_tlb_refill:u   | 290       | 292       | 66       
    ll_cache:u         | 4909961   | 2547062   | 4791593  
    ll_cache_miss:u    | 910       | 7294      | 478      

== combo_049_s3 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p512_np2_l1        
    s1 | fetch_b128_d1_bp0_s16_r100_lin_p128_np1_l1
    s2 | hot_b64_bp3_r100_lin_p1_np1_l1            
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 60951527 | 76927511 | 5231922 
    instructions:u     | 12950997 | 36150988 | 11281049
    br_retired:u       | 1031404  | 3911403  | 2021410 
    br_mis_pred:u      | 130737   | 1239578  | 368     
    l1i_cache:u        | 3692235  | 16992648 | 1485780 
    l1i_cache_refill:u | 706      | 890      | 573     
    l1i_tlb:u          | 3692235  | 16992648 | 1485780 
    l1i_tlb_refill:u   | 55       | 51       | 43      
    l2i_cache:u        | 704      | 889      | 573     
    l2i_cache_refill:u | 610      | 671      | 528     
    l2i_tlb:u          | 107      | 89       | 73      
    l2i_tlb_refill:u   | 32       | 14       | 13      
    l1d_cache:u        | 1536138  | 7959631  | 775248  
    l1d_cache_refill:u | 602952   | 1199747  | 147     
    l1d_tlb:u          | 2061613  | 13209414 | 777344  
    l1d_tlb_refill:u   | 350065   | 1320075  | 60      
    l2d_cache:u        | 2765929  | 3658869  | 1377    
    l2d_cache_refill:u | 1396637  | 944659   | 943     
    l2d_tlb:u          | 350190   | 1325751  | 81      
    l2d_tlb_refill:u   | 545      | 13       | 30      
    ll_cache:u         | 1395903  | 943844   | 341     
    ll_cache_miss:u    | 35520    | 77       | 22      
combined_orders:
    id        | modules                                                                                                     
    ----------+-------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p512_np2_l1+fetch_b128_d1_bp0_s16_r100_lin_p128_np1_l1+hot_b64_bp3_r100_lin_p1_np1_l1
    shuffle   | fetch_b128_d1_bp0_s16_r100_lin_p128_np1_l1+hot_b64_bp3_r100_lin_p1_np1_l1+cold_b64_d4_bitrev_lin_p512_np2_l1
    sum       | cold_b64_d4_bitrev_lin_p512_np2_l1+fetch_b128_d1_bp0_s16_r100_lin_p128_np1_l1+hot_b64_bp3_r100_lin_p1_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 127063807 | 133379838 | 143110960
    instructions:u     | 60361597  | 60361597  | 60383034 
    br_retired:u       | 6961804   | 6961804   | 6964217  
    br_mis_pred:u      | 1364487   | 1361749   | 1370683  
    l1i_cache:u        | 24288908  | 24188101  | 22170663 
    l1i_cache_refill:u | 2225      | 1705      | 2169     
    l1i_tlb:u          | 24288908  | 24188101  | 22170663 
    l1i_tlb_refill:u   | 50        | 47        | 149      
    l2i_cache:u        | 2225      | 1704      | 2166     
    l2i_cache_refill:u | 1050      | 988       | 1809     
    l2i_tlb:u          | 184       | 102       | 269      
    l2i_tlb_refill:u   | 25        | 30        | 59       
    l1d_cache:u        | 10198556  | 10200932  | 10271017 
    l1d_cache_refill:u | 1750233   | 1765067   | 1802846  
    l1d_tlb:u          | 15966713  | 15854327  | 16048371 
    l1d_tlb_refill:u   | 1660258   | 1660260   | 1670200  
    l2d_cache:u        | 6873121   | 7080511   | 6426175  
    l2d_cache_refill:u | 2561410   | 2712163   | 2342239  
    l2d_tlb:u          | 1660855   | 1670189   | 1676022  
    l2d_tlb_refill:u   | 903       | 198       | 588      
    ll_cache:u         | 2560095   | 2711006   | 2340088  
    ll_cache_miss:u    | 8501      | 6984      | 35619    

== combo_050_s3 ==
single_modules:
    id | module                                     
    ---+--------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p16_np4_l1       
    s1 | fetch_b128_d1_bp0_s16_r100_rand_p128_np8_l4
    s2 | hot_b64_bp3_r100_rand_p512_np1_l1          
single_counts:
    metric             | s0       | s1        | s2      
    -------------------+----------+-----------+---------
    cpu-cycles:u       | 20214514 | 202197235 | 46377881
    instructions:u     | 25591049 | 39990988  | 11280997
    br_retired:u       | 1991410  | 3911403   | 2021404 
    br_mis_pred:u      | 290642   | 1239062   | 450     
    l1i_cache:u        | 7638093  | 17624733  | 1501802 
    l1i_cache_refill:u | 855      | 1310      | 814     
    l1i_tlb:u          | 7638093  | 17624733  | 1501802 
    l1i_tlb_refill:u   | 50       | 54        | 59      
    l2i_cache:u        | 854      | 1309      | 813     
    l2i_cache_refill:u | 747      | 851       | 599     
    l2i_tlb:u          | 87       | 94        | 111     
    l2i_tlb_refill:u   | 12       | 18        | 48      
    l1d_cache:u        | 2975338  | 11888408  | 776219  
    l1d_cache_refill:u | 100263   | 4925663   | 640149  
    l1d_tlb:u          | 2977514  | 19705098  | 1521147 
    l1d_tlb_refill:u   | 110      | 4005164   | 664455  
    l2d_cache:u        | 201736   | 15605997  | 2530184 
    l2d_cache_refill:u | 992      | 4141302   | 1282694 
    l2d_tlb:u          | 135      | 4020991   | 664721  
    l2d_tlb_refill:u   | 47       | 20        | 83      
    ll_cache:u         | 313      | 4140410   | 1282053 
    ll_cache_miss:u    | 71       | 15135     | 1855    
combined_orders:
    id        | modules                                                                                                           
    ----------+-------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p16_np4_l1+fetch_b128_d1_bp0_s16_r100_rand_p128_np8_l4+hot_b64_bp3_r100_rand_p512_np1_l1
    shuffle   | fetch_b128_d1_bp0_s16_r100_rand_p128_np8_l4+cold_b128_d4_bitrev_lshuf_p16_np4_l1+hot_b64_bp3_r100_rand_p512_np1_l1
    sum       | cold_b128_d4_bitrev_lshuf_p16_np4_l1+fetch_b128_d1_bp0_s16_r100_rand_p128_np8_l4+hot_b64_bp3_r100_rand_p512_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 244701284 | 288331561 | 268789630
    instructions:u     | 76841598  | 76841689  | 76863034 
    br_retired:u       | 7921805   | 7921812   | 7924217  
    br_mis_pred:u      | 1522995   | 1522011   | 1530154  
    l1i_cache:u        | 28329345  | 28381904  | 26764628 
    l1i_cache_refill:u | 2846      | 3313      | 2979     
    l1i_tlb:u          | 28329345  | 28381904  | 26764628 
    l1i_tlb_refill:u   | 52        | 59        | 163      
    l2i_cache:u        | 2847      | 3312      | 2976     
    l2i_cache_refill:u | 1378      | 1733      | 2197     
    l2i_tlb:u          | 201       | 123       | 292      
    l2i_tlb_refill:u   | 38        | 50        | 78       
    l1d_cache:u        | 15449773  | 15458834  | 15639965 
    l1d_cache_refill:u | 5607754   | 5629433   | 5666075  
    l1d_tlb:u          | 24119103  | 24032867  | 24203759 
    l1d_tlb_refill:u   | 4707343   | 4673517   | 4669729  
    l2d_cache:u        | 19406867  | 18652410  | 18337917 
    l2d_cache_refill:u | 5319401   | 5421841   | 5424988  
    l2d_tlb:u          | 4718128   | 4685157   | 4685847  
    l2d_tlb_refill:u   | 709       | 189       | 150      
    ll_cache:u         | 5317282   | 5419895   | 5422776  
    ll_cache_miss:u    | 28053     | 35638     | 17061    

== combo_051_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_lstr_p512_np2_l2_sl3
    s1 | hot_b128_bp3_r100_lstr_p16_np4_l2_sl3          
    s2 | itlb_f64_l1_r100_pstr_p1_np1_l4_sp3            
single_counts:
    metric             | s0        | s1       | s2      
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 217224699 | 15514396 | 28567334
    instructions:u     | 37430998  | 23441049 | 13210997
    br_retired:u       | 3911405   | 3941410  | 731404  
    br_mis_pred:u      | 1234244   | 456      | 438     
    l1i_cache:u        | 17139206  | 3006286  | 1728927 
    l1i_cache_refill:u | 1086      | 735      | 1539143 
    l1i_tlb:u          | 17139206  | 3006286  | 1728927 
    l1i_tlb_refill:u   | 48        | 45       | 670081  
    l2i_cache:u        | 1086      | 735      | 1539142 
    l2i_cache_refill:u | 730       | 633      | 715     
    l2i_tlb:u          | 95        | 80       | 670158  
    l2i_tlb_refill:u   | 27        | 13       | 18      
    l1d_cache:u        | 9224266   | 2695318  | 2695389 
    l1d_cache_refill:u | 2566686   | 375      | 134     
    l1d_tlb:u          | 15744157  | 2697453  | 2697376 
    l1d_tlb_refill:u   | 2600549   | 111      | 64      
    l2d_cache:u        | 11132149  | 2303     | 1809598 
    l2d_cache_refill:u | 5148176   | 1217     | 1145    
    l2d_tlb:u          | 2611017   | 132      | 91      
    l2d_tlb_refill:u   | 109       | 19       | 31      
    ll_cache:u         | 5147261   | 560      | 335     
    ll_cache_miss:u    | 13415     | 87       | 61      
combined_orders:
    id        | modules                                                                                                                  
    ----------+--------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_lstr_p512_np2_l2_sl3+hot_b128_bp3_r100_lstr_p16_np4_l2_sl3+itlb_f64_l1_r100_pstr_p1_np1_l4_sp3
    shuffle   | hot_b128_bp3_r100_lstr_p16_np4_l2_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p512_np2_l2_sl3+itlb_f64_l1_r100_pstr_p1_np1_l4_sp3
    sum       | fetch_b128_d1_bp0_s16_r100_lstr_p512_np2_l2_sl3+hot_b128_bp3_r100_lstr_p16_np4_l2_sl3+itlb_f64_l1_r100_pstr_p1_np1_l4_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 259039008 | 206306736 | 261306429
    instructions:u     | 74061607  | 74061597  | 74083044 
    br_retired:u       | 8581806   | 8581804   | 8584219  
    br_mis_pred:u      | 1231660   | 1231655   | 1235138  
    l1i_cache:u        | 24229087  | 24218087  | 21874419 
    l1i_cache_refill:u | 1066992   | 1037888   | 1540964  
    l1i_tlb:u          | 24229087  | 24218087  | 21874419 
    l1i_tlb_refill:u   | 660760    | 660796    | 670174   
    l2i_cache:u        | 1066989   | 1037885   | 1540963  
    l2i_cache_refill:u | 15147     | 14570     | 2078     
    l2i_tlb:u          | 660830    | 660868    | 670333   
    l2i_tlb_refill:u   | 185       | 67        | 58       
    l1d_cache:u        | 14570968  | 14565335  | 14614973 
    l1d_cache_refill:u | 2543861   | 2549599   | 2567195  
    l1d_tlb:u          | 21024517  | 21090838  | 21138986 
    l1d_tlb_refill:u   | 2601888   | 2601885   | 2600724  
    l2d_cache:u        | 12673251  | 12771991  | 12944050 
    l2d_cache_refill:u | 5506446   | 5459619   | 5150538  
    l2d_tlb:u          | 2609905   | 2612089   | 2611240  
    l2d_tlb_refill:u   | 789       | 202       | 159      
    ll_cache:u         | 5490941   | 5444705   | 5148156  
    ll_cache_miss:u    | 253582    | 18149     | 13563    

== combo_052_s3 ==
single_modules:
    id | module                                     
    ---+--------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p512_np4_l2      
    s1 | fetch_b64_d1_bp0_s16_r100_lshuf_p512_np4_l4
    s2 | hot_b64_bp3_r100_lin_p128_np8_l1           
single_counts:
    metric             | s0        | s1        | s2      
    -------------------+-----------+-----------+---------
    cpu-cycles:u       | 173766612 | 123745892 | 11305889
    instructions:u     | 26870997  | 20150988  | 11281049
    br_retired:u       | 1991404   | 1991403   | 2021410 
    br_mis_pred:u      | 290726    | 592417    | 454     
    l1i_cache:u        | 7784353   | 8770490   | 1487495 
    l1i_cache_refill:u | 1127      | 812       | 577     
    l1i_tlb:u          | 7784353   | 8770490   | 1487495 
    l1i_tlb_refill:u   | 54        | 56        | 39      
    l2i_cache:u        | 1127      | 812       | 577     
    l2i_cache_refill:u | 828       | 662       | 531     
    l2i_tlb:u          | 99        | 104       | 89      
    l2i_tlb_refill:u   | 39        | 43        | 16      
    l1d_cache:u        | 4258534   | 5985231   | 775651  
    l1d_cache_refill:u | 1929462   | 1507228   | 172552  
    l1d_tlb:u          | 5138629   | 8735689   | 944397  
    l1d_tlb_refill:u   | 660059    | 660064    | 85117   
    l2d_cache:u        | 10980464  | 11317086  | 1419503 
    l2d_cache_refill:u | 4968510   | 4809925   | 236882  
    l2d_tlb:u          | 660122    | 660726    | 85146   
    l2d_tlb_refill:u   | 576       | 62        | 165     
    ll_cache:u         | 4967240   | 4808849   | 236239  
    ll_cache_miss:u    | 9675      | 24933     | 718     
combined_orders:
    id        | modules                                                                                                           
    ----------+-------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p512_np4_l2+fetch_b64_d1_bp0_s16_r100_lshuf_p512_np4_l4+hot_b64_bp3_r100_lin_p128_np8_l1
    shuffle   | hot_b64_bp3_r100_lin_p128_np8_l1+cold_b128_d4_bitrev_lshuf_p512_np4_l2+fetch_b64_d1_bp0_s16_r100_lshuf_p512_np4_l4
    sum       | cold_b128_d4_bitrev_lshuf_p512_np4_l2+fetch_b64_d1_bp0_s16_r100_lshuf_p512_np4_l4+hot_b64_bp3_r100_lin_p128_np8_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 300728435 | 344071644 | 308818393
    instructions:u     | 58281695  | 58281548  | 58303034 
    br_retired:u       | 6001810   | 6001790   | 6004217  
    br_mis_pred:u      | 882855    | 882051    | 883597   
    l1i_cache:u        | 18543944  | 18602195  | 18042338 
    l1i_cache_refill:u | 2927      | 2753      | 2516     
    l1i_tlb:u          | 18543944  | 18602195  | 18042338 
    l1i_tlb_refill:u   | 48        | 49        | 149      
    l2i_cache:u        | 2926      | 2752      | 2516     
    l2i_cache_refill:u | 1621      | 1595      | 2021     
    l2i_tlb:u          | 99        | 94        | 292      
    l2i_tlb_refill:u   | 42        | 43        | 98       
    l1d_cache:u        | 10954691  | 10960244  | 11019416 
    l1d_cache_refill:u | 3397091   | 3419320   | 3609242  
    l1d_tlb:u          | 14741713  | 14769589  | 14818715 
    l1d_tlb_refill:u   | 1405173   | 1405169   | 1405240  
    l2d_cache:u        | 24743452  | 24725526  | 23717053 
    l2d_cache_refill:u | 10435056  | 10383711  | 10015317 
    l2d_tlb:u          | 1405772   | 1405679   | 1405994  
    l2d_tlb_refill:u   | 35043     | 36283     | 803      
    ll_cache:u         | 10430219  | 10378418  | 10012328 
    ll_cache_miss:u    | 41264     | 75149     | 35326    

== combo_053_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p16_np1_l4_sp17        
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l4_sp17
    s2 | hot_b128_bp3_r100_lin_p128_np8_l2              
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 16558932 | 60231095 | 39323664
    instructions:u     | 14871049 | 39990988 | 23440997
    br_retired:u       | 1031410  | 3911403  | 3941404 
    br_mis_pred:u      | 130590   | 1231695  | 497     
    l1i_cache:u        | 3942538  | 17427213 | 3009210 
    l1i_cache_refill:u | 678      | 863      | 762     
    l1i_tlb:u          | 3942538  | 17427213 | 3009210 
    l1i_tlb_refill:u   | 43       | 51       | 52      
    l2i_cache:u        | 676      | 862      | 759     
    l2i_cache_refill:u | 525      | 709      | 643     
    l2i_tlb:u          | 69       | 91       | 155     
    l2i_tlb_refill:u   | 14       | 11       | 38      
    l1d_cache:u        | 3455294  | 11755012 | 2695828 
    l1d_cache_refill:u | 188      | 190154   | 631166  
    l1d_tlb:u          | 3457386  | 15385487 | 3158955 
    l1d_tlb_refill:u   | 107      | 193      | 340074  
    l2d_cache:u        | 1270     | 1176532  | 5845897 
    l2d_cache_refill:u | 779      | 1179     | 780476  
    l2d_tlb:u          | 128      | 227      | 340099  
    l2d_tlb_refill:u   | 5        | 51       | 141     
    ll_cache:u         | 230      | 404      | 779672  
    ll_cache_miss:u    | 18       | 34       | 5986    
combined_orders:
    id        | modules                                                                                                                  
    ----------+--------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p16_np1_l4_sp17+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l4_sp17+hot_b128_bp3_r100_lin_p128_np8_l2
    shuffle   | cold_b64_d4_bitrev_pstr_p16_np1_l4_sp17+hot_b128_bp3_r100_lin_p128_np8_l2+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l4_sp17
    sum       | cold_b64_d4_bitrev_pstr_p16_np1_l4_sp17+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l4_sp17+hot_b128_bp3_r100_lin_p128_np8_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 123365489 | 116921548 | 116113691
    instructions:u     | 78281594  | 78281588  | 78303034 
    br_retired:u       | 8881801   | 8881803   | 8884217  
    br_mis_pred:u      | 1363725   | 1361525   | 1362782  
    l1i_cache:u        | 26398609  | 26431539  | 24378961 
    l1i_cache_refill:u | 2575      | 1892      | 2303     
    l1i_tlb:u          | 26398609  | 26431539  | 24378961 
    l1i_tlb_refill:u   | 64        | 54        | 146      
    l2i_cache:u        | 2573      | 1891      | 2297     
    l2i_cache_refill:u | 1515      | 1180      | 1877     
    l2i_tlb:u          | 203       | 81        | 315      
    l2i_tlb_refill:u   | 33        | 16        | 63       
    l1d_cache:u        | 17883089  | 17819695  | 17906134 
    l1d_cache_refill:u | 966008    | 899037    | 821508   
    l1d_tlb:u          | 22144449  | 22015052  | 22001828 
    l1d_tlb_refill:u   | 343717    | 343684    | 340374   
    l2d_cache:u        | 8450892   | 7870981   | 7023699  
    l2d_cache_refill:u | 1168860   | 951650    | 782434   
    l2d_tlb:u          | 343853    | 343807    | 340454   
    l2d_tlb_refill:u   | 15        | 25        | 197      
    ll_cache:u         | 1167532   | 950297    | 780306   
    ll_cache_miss:u    | 9077      | 12519     | 6038     

== combo_054_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p128_np8_l1_sp17      
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l2_sp33
    s2 | hot_b128_bp3_r100_lin_p1_np8_l4                
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 45519053 | 68007646 | 25724934
    instructions:u     | 25590997 | 18870988 | 26001046
    br_retired:u       | 1991404  | 1991403  | 3941407 
    br_mis_pred:u      | 290510   | 590778   | 420     
    l1i_cache:u        | 7579831  | 8674550  | 3336718 
    l1i_cache_refill:u | 890      | 678      | 793     
    l1i_tlb:u          | 7579831  | 8674550  | 3336718 
    l1i_tlb_refill:u   | 56       | 43       | 41      
    l2i_cache:u        | 888      | 678      | 791     
    l2i_cache_refill:u | 774      | 587      | 632     
    l2i_tlb:u          | 99       | 86       | 77      
    l2i_tlb_refill:u   | 45       | 17       | 14      
    l1d_cache:u        | 2981669  | 4752212  | 5255495 
    l1d_cache_refill:u | 1165140  | 1244648  | 153     
    l1d_tlb:u          | 4368366  | 8084271  | 5257642 
    l1d_tlb_refill:u   | 1300118  | 1320059  | 65      
    l2d_cache:u        | 4332086  | 3646203  | 1523    
    l2d_cache_refill:u | 1036032  | 1045690  | 1060    
    l2d_tlb:u          | 1302608  | 1326264  | 89      
    l2d_tlb_refill:u   | 156      | 23       | 27      
    ll_cache:u         | 1035114  | 1045097  | 371     
    ll_cache_miss:u    | 6335     | 34       | 28      
combined_orders:
    id        | modules                                                                                                                  
    ----------+--------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p128_np8_l1_sp17+fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l2_sp33+hot_b128_bp3_r100_lin_p1_np8_l4
    shuffle   | fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l2_sp33+hot_b128_bp3_r100_lin_p1_np8_l4+cold_b128_d4_bitrev_pstr_p128_np8_l1_sp17
    sum       | cold_b128_d4_bitrev_pstr_p128_np8_l1_sp17+fetch_b64_d1_bp0_s16_r100_pstr_p128_np1_l2_sp33+hot_b128_bp3_r100_lin_p1_np8_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 130092248 | 129478006 | 139251633
    instructions:u     | 70441601  | 70441588  | 70463031 
    br_retired:u       | 7921803   | 7921803   | 7924214  
    br_mis_pred:u      | 882248    | 881802    | 881708   
    l1i_cache:u        | 20059715  | 20020061  | 19591099 
    l1i_cache_refill:u | 1965      | 2964      | 2361     
    l1i_tlb:u          | 20059715  | 20020061  | 19591099 
    l1i_tlb_refill:u   | 64        | 54        | 140      
    l2i_cache:u        | 1966      | 2963      | 2357     
    l2i_cache_refill:u | 1259      | 1500      | 1993     
    l2i_tlb:u          | 198       | 97        | 262      
    l2i_tlb_refill:u   | 22        | 18        | 76       
    l1d_cache:u        | 12882138  | 12875969  | 12989376 
    l1d_cache_refill:u | 2354884   | 2352303   | 2409941  
    l1d_tlb:u          | 17518342  | 17574255  | 17710279 
    l1d_tlb_refill:u   | 2607386   | 2631154   | 2620242  
    l2d_cache:u        | 8149361   | 8268991   | 7979812  
    l2d_cache_refill:u | 2108976   | 2216110   | 2082782  
    l2d_tlb:u          | 2612784   | 2640574   | 2628961  
    l2d_tlb_refill:u   | 32        | 286       | 206      
    ll_cache:u         | 2107534   | 2214580   | 2080582  
    ll_cache_miss:u    | 27125     | 11396     | 6397     

== combo_055_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lshuf_p512_np8_l2           
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l1_sp17
    s2 | itlb_f64_l1_r100_pstr_p1_np2_l4_sp3            
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 91173470 | 44586854 | 34720027
    instructions:u     | 13590997 | 36150988 | 13210997
    br_retired:u       | 1031404  | 3911403  | 731404  
    br_mis_pred:u      | 130737   | 1231060  | 438     
    l1i_cache:u        | 3820589  | 16762107 | 1780539 
    l1i_cache_refill:u | 747      | 896      | 1228231 
    l1i_tlb:u          | 3820589  | 16762107 | 1780539 
    l1i_tlb_refill:u   | 52       | 54       | 670073  
    l2i_cache:u        | 747      | 896      | 1228229 
    l2i_cache_refill:u | 653      | 752      | 116580  
    l2i_tlb:u          | 110      | 113      | 670152  
    l2i_tlb_refill:u   | 48       | 42       | 22      
    l1d_cache:u        | 2179662  | 7904955  | 2695238 
    l1d_cache_refill:u | 1027409  | 270965   | 143     
    l1d_tlb:u          | 2471428  | 11543757 | 2696898 
    l1d_tlb_refill:u   | 175061   | 151      | 65      
    l2d_cache:u        | 5601449  | 1008553  | 1154419 
    l2d_cache_refill:u | 2502828  | 1402     | 101219  
    l2d_tlb:u          | 175127   | 180      | 89      
    l2d_tlb_refill:u   | 82       | 51       | 6       
    ll_cache:u         | 2502014  | 599      | 283     
    ll_cache_miss:u    | 9625     | 73       | 22      
combined_orders:
    id        | modules                                                                                                                 
    ----------+-------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lshuf_p512_np8_l2+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l1_sp17+itlb_f64_l1_r100_pstr_p1_np2_l4_sp3
    shuffle   | fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l1_sp17+itlb_f64_l1_r100_pstr_p1_np2_l4_sp3+cold_b64_d4_bitrev_lshuf_p512_np8_l2
    sum       | cold_b64_d4_bitrev_lshuf_p512_np8_l2+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l1_sp17+itlb_f64_l1_r100_pstr_p1_np2_l4_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 150922993 | 138818237 | 170480351
    instructions:u     | 62931588  | 62931588  | 62952982 
    br_retired:u       | 5671803   | 5671803   | 5674211  
    br_mis_pred:u      | 1361780   | 1361850   | 1362235  
    l1i_cache:u        | 24502671  | 24589964  | 22363235 
    l1i_cache_refill:u | 1079629   | 1219775   | 1229874  
    l1i_tlb:u          | 24502671  | 24589964  | 22363235 
    l1i_tlb_refill:u   | 660815    | 660746    | 670179   
    l2i_cache:u        | 1079628   | 1219774   | 1229872  
    l2i_cache_refill:u | 15931     | 14975     | 117985   
    l2i_tlb:u          | 660893    | 660781    | 670375   
    l2i_tlb_refill:u   | 223       | 74        | 112      
    l1d_cache:u        | 12689823  | 12728458  | 12779855 
    l1d_cache_refill:u | 1308501   | 1330911   | 1298517  
    l1d_tlb:u          | 16576651  | 16627929  | 16712083 
    l1d_tlb_refill:u   | 172022    | 172062    | 175277   
    l2d_cache:u        | 7969363   | 7479439   | 7764421  
    l2d_cache_refill:u | 2538427   | 2551804   | 2605449  
    l2d_tlb:u          | 172148    | 172185    | 175396   
    l2d_tlb_refill:u   | 192       | 654       | 139      
    ll_cache:u         | 2522764   | 2536390   | 2502896  
    ll_cache_miss:u    | 2471      | 1914      | 9720     

== combo_056_s3 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np2_l4_sp3
    s1 | hot_b128_bp3_r100_lstr_p128_np4_l2_sl3        
    s2 | itlb_f64_l1_r100_rand_p512_np2_l1             
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 90329435 | 67413656 | 55801534
    instructions:u     | 20150988 | 23440997 | 11291003
    br_retired:u       | 1991403  | 3941404  | 731402  
    br_mis_pred:u      | 591218   | 428      | 497     
    l1i_cache:u        | 8714082  | 3008855  | 1485017 
    l1i_cache_refill:u | 677      | 779      | 1601789 
    l1i_tlb:u          | 8714082  | 3008855  | 1485017 
    l1i_tlb_refill:u   | 45       | 46       | 660055  
    l2i_cache:u        | 677      | 779      | 1601788 
    l2i_cache_refill:u | 571      | 641      | 46430   
    l2i_tlb:u          | 82       | 166      | 660105  
    l2i_tlb_refill:u   | 15       | 15       | 166     
    l1d_cache:u        | 6014270  | 2696330  | 775455  
    l1d_cache_refill:u | 2346785  | 2305281  | 639866  
    l1d_tlb:u          | 10585543 | 4720465  | 1474937 
    l1d_tlb_refill:u   | 2600060  | 1940062  | 637800  
    l2d_cache:u        | 7498592  | 6548596  | 3671689 
    l2d_cache_refill:u | 1993010  | 1382073  | 1335786 
    l2d_tlb:u          | 2607054  | 1940340  | 637821  
    l2d_tlb_refill:u   | 10       | 20       | 146     
    ll_cache:u         | 1992354  | 1381406  | 1282294 
    ll_cache_miss:u    | 170      | 262      | 284     
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp0_s16_r100_pstr_p128_np2_l4_sp3+hot_b128_bp3_r100_lstr_p128_np4_l2_sl3+itlb_f64_l1_r100_rand_p512_np2_l1
    shuffle   | hot_b128_bp3_r100_lstr_p128_np4_l2_sl3+itlb_f64_l1_r100_rand_p512_np2_l1+fetch_b64_d1_bp0_s16_r100_pstr_p128_np2_l4_sp3
    sum       | fetch_b64_d1_bp0_s16_r100_pstr_p128_np2_l4_sp3+hot_b128_bp3_r100_lstr_p128_np4_l2_sl3+itlb_f64_l1_r100_rand_p512_np2_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 255030273 | 246515056 | 213544625
    instructions:u     | 54861598  | 54861598  | 54882988 
    br_retired:u       | 6661805   | 6661805   | 6664209  
    br_mis_pred:u      | 595151    | 591444    | 592143   
    l1i_cache:u        | 14408062  | 14297310  | 13207954 
    l1i_cache_refill:u | 1762106   | 1050803   | 1603245  
    l1i_tlb:u          | 14408062  | 14297310  | 13207954 
    l1i_tlb_refill:u   | 660547    | 660548    | 660146   
    l2i_cache:u        | 1762104   | 1050801   | 1603244  
    l2i_cache_refill:u | 36576     | 42946     | 47642    
    l2i_tlb:u          | 660661    | 660622    | 660353   
    l2i_tlb_refill:u   | 546       | 622       | 196      
    l1d_cache:u        | 9377213   | 9409554   | 9486055  
    l1d_cache_refill:u | 5271904   | 5221992   | 5291932  
    l1d_tlb:u          | 16729076  | 16760131  | 16780945 
    l1d_tlb_refill:u   | 5194228   | 5179563   | 5177922  
    l2d_cache:u        | 19344896  | 19573590  | 17718877 
    l2d_cache_refill:u | 5938686   | 6346821   | 4710869  
    l2d_tlb:u          | 5194398   | 5184053   | 5185215  
    l2d_tlb_refill:u   | 1834      | 5673      | 176      
    ll_cache:u         | 5909751   | 6302870   | 4656054  
    ll_cache_miss:u    | 3147      | 7885      | 716      

== combo_057_s3 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | fetch_b64_d1_bp0_s16_r100_lstr_p16_np8_l2_sl9
    s1 | hot_b128_bp3_r100_lshuf_p128_np2_l2          
    s2 | itlb_f64_l1_r100_lstr_p1_np4_l1_sl5          
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 25766549 | 68820289 | 19964629
    instructions:u     | 18871046 | 23440997 | 11291040
    br_retired:u       | 1991407  | 3941404  | 731409  
    br_mis_pred:u      | 591498   | 501      | 455     
    l1i_cache:u        | 8639149  | 3009643  | 1521857 
    l1i_cache_refill:u | 656      | 1013     | 1196770 
    l1i_tlb:u          | 8639149  | 3009643  | 1521857 
    l1i_tlb_refill:u   | 46       | 53       | 660105  
    l2i_cache:u        | 655      | 1013     | 1196767 
    l2i_cache_refill:u | 584      | 707      | 724     
    l2i_tlb:u          | 79       | 145      | 660217  
    l2i_tlb_refill:u   | 14       | 41       | 107     
    l1d_cache:u        | 4672226  | 2695910  | 775077  
    l1d_cache_refill:u | 208278   | 2174681  | 189     
    l1d_tlb:u          | 6405920  | 4130876  | 776686  
    l1d_tlb_refill:u   | 118      | 1300062  | 61      
    l2d_cache:u        | 659371   | 7679479  | 1072121 
    l2d_cache_refill:u | 1301     | 2070448  | 1062    
    l2d_tlb:u          | 137      | 1300111  | 79      
    l2d_tlb_refill:u   | 49       | 15       | 3       
    ll_cache:u         | 614      | 2069781  | 265     
    ll_cache_miss:u    | 84       | 97       | 12      
combined_orders:
    id        | modules                                                                                                              
    ----------+----------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp0_s16_r100_lstr_p16_np8_l2_sl9+hot_b128_bp3_r100_lshuf_p128_np2_l2+itlb_f64_l1_r100_lstr_p1_np4_l1_sl5
    shuffle   | hot_b128_bp3_r100_lshuf_p128_np2_l2+fetch_b64_d1_bp0_s16_r100_lstr_p16_np8_l2_sl9+itlb_f64_l1_r100_lstr_p1_np4_l1_sl5
    sum       | fetch_b64_d1_bp0_s16_r100_lstr_p16_np8_l2_sl9+hot_b128_bp3_r100_lshuf_p128_np2_l2+itlb_f64_l1_r100_lstr_p1_np4_l1_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 140282358 | 123137111 | 114551467
    instructions:u     | 53581588  | 53581588  | 53603083 
    br_retired:u       | 6661803   | 6661803   | 6664220  
    br_mis_pred:u      | 592018    | 593569    | 592454   
    l1i_cache:u        | 14209032  | 14135713  | 13170649 
    l1i_cache_refill:u | 1296582   | 1116390   | 1198439  
    l1i_tlb:u          | 14209032  | 14135713  | 13170649 
    l1i_tlb_refill:u   | 660557    | 660624    | 660204   
    l2i_cache:u        | 1296581   | 1116387   | 1198435  
    l2i_cache_refill:u | 188076    | 13193     | 2015     
    l2i_tlb:u          | 660623    | 660755    | 660441   
    l2i_tlb_refill:u   | 105       | 112       | 162      
    l1d_cache:u        | 8088220   | 8088646   | 8143213  
    l1d_cache_refill:u | 2435555   | 2339484   | 2383148  
    l1d_tlb:u          | 11286530  | 11287945  | 11313482 
    l1d_tlb_refill:u   | 1302106   | 1302029   | 1300241  
    l2d_cache:u        | 10120447  | 9569370   | 9410971  
    l2d_cache_refill:u | 2075398   | 1683679   | 2072811  
    l2d_tlb:u          | 1302778   | 1302067   | 1300327  
    l2d_tlb_refill:u   | 191       | 177       | 67       
    ll_cache:u         | 1941679   | 1669702   | 2070660  
    ll_cache_miss:u    | 820       | 445       | 193      

== combo_058_s3 ==
single_modules:
    id | module                                   
    ---+------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p16_np8_l4_sl9   
    s1 | fetch_b64_d1_bp0_s16_r100_lin_p512_np4_l4
    s2 | hot_b128_bp3_r100_pstr_p128_np8_l2_sp3   
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 17474516 | 92415063 | 91423537
    instructions:u     | 14871049 | 20150988 | 23440997
    br_retired:u       | 1031410  | 1991403  | 3941404 
    br_mis_pred:u      | 130605   | 596781   | 491     
    l1i_cache:u        | 3962754  | 8901010  | 3010562 
    l1i_cache_refill:u | 684      | 698      | 849     
    l1i_tlb:u          | 3962754  | 8901010  | 3010562 
    l1i_tlb_refill:u   | 55       | 45       | 53      
    l2i_cache:u        | 683      | 697      | 849     
    l2i_cache_refill:u | 603      | 614      | 700     
    l2i_tlb:u          | 82       | 79       | 188     
    l2i_tlb_refill:u   | 17       | 21       | 48      
    l1d_cache:u        | 3455310  | 6012066  | 2697396 
    l1d_cache_refill:u | 92627    | 844959   | 2414468 
    l1d_tlb:u          | 3457346  | 9013377  | 5411221 
    l1d_tlb_refill:u   | 108      | 670063   | 2589901 
    l2d_cache:u        | 229370   | 10040993 | 7686600 
    l2d_cache_refill:u | 1128     | 4576273  | 2168584 
    l2d_tlb:u          | 126      | 680705   | 2590221 
    l2d_tlb_refill:u   | 6        | 1232     | 126     
    ll_cache:u         | 566      | 4575237  | 2167726 
    ll_cache_miss:u    | 34       | 8844     | 382     
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p16_np8_l4_sl9+fetch_b64_d1_bp0_s16_r100_lin_p512_np4_l4+hot_b128_bp3_r100_pstr_p128_np8_l2_sp3
    shuffle   | fetch_b64_d1_bp0_s16_r100_lin_p512_np4_l4+cold_b64_d4_bitrev_lstr_p16_np8_l4_sl9+hot_b128_bp3_r100_pstr_p128_np8_l2_sp3
    sum       | cold_b64_d4_bitrev_lstr_p16_np8_l4_sl9+fetch_b64_d1_bp0_s16_r100_lin_p512_np4_l4+hot_b128_bp3_r100_pstr_p128_np8_l2_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 199431439 | 223401733 | 201313116
    instructions:u     | 58441588  | 58441604  | 58463034 
    br_retired:u       | 6961803   | 6961803   | 6964217  
    br_mis_pred:u      | 724815    | 721796    | 727877   
    l1i_cache:u        | 16710126  | 16569244  | 15874326 
    l1i_cache_refill:u | 2351      | 2329      | 2231     
    l1i_tlb:u          | 16710126  | 16569244  | 15874326 
    l1i_tlb_refill:u   | 56        | 56        | 153      
    l2i_cache:u        | 2351      | 2329      | 2229     
    l2i_cache_refill:u | 1298      | 1362      | 1917     
    l2i_tlb:u          | 102       | 132       | 349      
    l2i_tlb_refill:u   | 32        | 48        | 86       
    l1d_cache:u        | 12072733  | 12067075  | 12164772 
    l1d_cache_refill:u | 3444024   | 3449423   | 3352054  
    l1d_tlb:u          | 17615034  | 17711120  | 17881944 
    l1d_tlb_refill:u   | 3245596   | 3264217   | 3260072  
    l2d_cache:u        | 19567948  | 19381661  | 17956963 
    l2d_cache_refill:u | 7005627   | 7123939   | 6745985  
    l2d_tlb:u          | 3247819   | 3265899   | 3271052  
    l2d_tlb_refill:u   | 861       | 700       | 1364     
    ll_cache:u         | 7003743   | 7122019   | 6743529  
    ll_cache_miss:u    | 45852     | 35232     | 9260     

== combo_059_s3 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b64_d4_bitrev_lshuf_p128_np1_l1  
    s1 | hot_b64_bp3_r100_lstr_p16_np1_l1_sl3  
    s2 | itlb_f64_l1_r100_pstr_p512_np2_l4_sp33
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 26474831 | 5241934  | 156940066
    instructions:u     | 12950997 | 11281049 | 13210997 
    br_retired:u       | 1031404  | 2021410  | 731404   
    br_mis_pred:u      | 130630   | 371      | 485      
    l1i_cache:u        | 3690677  | 1485336  | 1738509  
    l1i_cache_refill:u | 679      | 554      | 1587946  
    l1i_tlb:u          | 3690677  | 1485336  | 1738509  
    l1i_tlb_refill:u   | 42       | 41       | 670047   
    l2i_cache:u        | 679      | 553      | 1587944  
    l2i_cache_refill:u | 592      | 493      | 379378   
    l2i_tlb:u          | 81       | 72       | 670101   
    l2i_tlb_refill:u   | 12       | 17       | 1358     
    l1d_cache:u        | 1535834  | 775179   | 2695584  
    l1d_cache_refill:u | 606109   | 155      | 2559539  
    l1d_tlb:u          | 2321220  | 777079   | 5354630  
    l1d_tlb_refill:u   | 667245   | 73       | 2583716  
    l2d_cache:u        | 1927123  | 1314     | 11133298 
    l2d_cache_refill:u | 536750   | 832      | 5402121  
    l2d_tlb:u          | 668732   | 98       | 2583755  
    l2d_tlb_refill:u   | 17       | 47       | 125      
    ll_cache:u         | 536115   | 304      | 5134497  
    ll_cache_miss:u    | 31       | 19       | 7752     
combined_orders:
    id        | modules                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lshuf_p128_np1_l1+hot_b64_bp3_r100_lstr_p16_np1_l1_sl3+itlb_f64_l1_r100_pstr_p512_np2_l4_sp33
    shuffle   | hot_b64_bp3_r100_lstr_p16_np1_l1_sl3+cold_b64_d4_bitrev_lshuf_p128_np1_l1+itlb_f64_l1_r100_pstr_p512_np2_l4_sp33
    sum       | cold_b64_d4_bitrev_lshuf_p128_np1_l1+hot_b64_bp3_r100_lstr_p16_np1_l1_sl3+itlb_f64_l1_r100_pstr_p512_np2_l4_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 216725640 | 181795231 | 188656831
    instructions:u     | 37421604  | 37421588  | 37443043 
    br_retired:u       | 3781803   | 3781803   | 3784218  
    br_mis_pred:u      | 130917    | 131163    | 131486   
    l1i_cache:u        | 6730473   | 6843934   | 6914522  
    l1i_cache_refill:u | 1058699   | 1056041   | 1589179  
    l1i_tlb:u          | 6730473   | 6843934   | 6914522  
    l1i_tlb_refill:u   | 670357    | 670379    | 670130   
    l2i_cache:u        | 1058697   | 1056040   | 1589176  
    l2i_cache_refill:u | 354006    | 287438    | 380463   
    l2i_tlb:u          | 670430    | 670458    | 670254   
    l2i_tlb_refill:u   | 992       | 91        | 1387     
    l1d_cache:u        | 4997097   | 4997474   | 5006597  
    l1d_cache_refill:u | 3154793   | 3152470   | 3165803  
    l1d_tlb:u          | 8450390   | 8423977   | 8452929  
    l1d_tlb_refill:u   | 3250794   | 3247062   | 3251034  
    l2d_cache:u        | 13627772  | 13984196  | 13061735 
    l2d_cache_refill:u | 6189731   | 6372377   | 5939703  
    l2d_tlb:u          | 3251533   | 3247465   | 3252585  
    l2d_tlb_refill:u   | 2041      | 2376      | 189      
    ll_cache:u         | 5854167   | 6035008   | 5670916  
    ll_cache_miss:u    | 6543      | 7448      | 7802     

== combo_060_s3 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p128_np2_l2         
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p16_np4_l4_sl5
    s2 | hot_b128_bp3_r100_rand_p1_np1_l1              
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 76288552 | 60295876 | 10353080
    instructions:u     | 26870997 | 39990988 | 22161049
    br_retired:u       | 1991404  | 3911403  | 3941410 
    br_mis_pred:u      | 290690   | 1231082  | 429     
    l1i_cache:u        | 7749801  | 17362833 | 2846332 
    l1i_cache_refill:u | 903      | 1118     | 666     
    l1i_tlb:u          | 7749801  | 17362833 | 2846332 
    l1i_tlb_refill:u   | 49       | 55       | 46      
    l2i_cache:u        | 903      | 1117     | 666     
    l2i_cache_refill:u | 710      | 721      | 596     
    l2i_tlb:u          | 96       | 104      | 74      
    l2i_tlb_refill:u   | 17       | 47       | 13      
    l1d_cache:u        | 4255566  | 11703228 | 1415267 
    l1d_cache_refill:u | 2111081  | 200743   | 155     
    l1d_tlb:u          | 5885107  | 15347722 | 1417291 
    l1d_tlb_refill:u   | 1300063  | 170      | 63      
    l2d_cache:u        | 7316831  | 382606   | 1362    
    l2d_cache_refill:u | 1827835  | 1439     | 970     
    l2d_tlb:u          | 1300155  | 201      | 88      
    l2d_tlb_refill:u   | 114      | 44       | 32      
    ll_cache:u         | 1826964  | 600      | 292     
    ll_cache_miss:u    | 96       | 73       | 21      
combined_orders:
    id        | modules                                                                                                              
    ----------+----------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p128_np2_l2+fetch_b128_d1_bp0_s16_r100_lstr_p16_np4_l4_sl5+hot_b128_bp3_r100_rand_p1_np1_l1
    shuffle   | fetch_b128_d1_bp0_s16_r100_lstr_p16_np4_l4_sl5+cold_b128_d4_bitrev_lshuf_p128_np2_l2+hot_b128_bp3_r100_rand_p1_np1_l1
    sum       | cold_b128_d4_bitrev_lshuf_p128_np2_l2+fetch_b128_d1_bp0_s16_r100_lstr_p16_np4_l4_sl5+hot_b128_bp3_r100_rand_p1_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 146760218 | 148903489 | 146937508
    instructions:u     | 89001597  | 89001597  | 89023034 
    br_retired:u       | 9841804   | 9841804   | 9844217  
    br_mis_pred:u      | 1521832   | 1521710   | 1522201  
    l1i_cache:u        | 29656892  | 29655873  | 27958966 
    l1i_cache_refill:u | 2437      | 3088      | 2687     
    l1i_tlb:u          | 29656892  | 29655873  | 27958966 
    l1i_tlb_refill:u   | 55        | 55        | 150      
    l2i_cache:u        | 2437      | 3087      | 2686     
    l2i_cache_refill:u | 1232      | 1202      | 2027     
    l2i_tlb:u          | 195       | 195       | 274      
    l2i_tlb_refill:u   | 15        | 18        | 77       
    l1d_cache:u        | 17357886  | 17337758  | 17374061 
    l1d_cache_refill:u | 2538321   | 2559785   | 2311979  
    l1d_tlb:u          | 22403477  | 22415109  | 22650120 
    l1d_tlb_refill:u   | 1302235   | 1302145   | 1300296  
    l2d_cache:u        | 8324127   | 8395746   | 7700799  
    l2d_cache_refill:u | 1720617   | 1874220   | 1830244  
    l2d_tlb:u          | 1302362   | 1308905   | 1300444  
    l2d_tlb_refill:u   | 159       | 21        | 190      
    ll_cache:u         | 1719185   | 1872988   | 1827856  
    ll_cache_miss:u    | 6386      | 109       | 190      

== combo_061_s3 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | fetch_b64_d1_bp0_s16_r100_rand_p512_np4_l4
    s1 | hot_b64_bp3_r100_lstr_p512_np4_l1_sl9     
    s2 | itlb_f64_l1_r100_lstr_p512_np2_l1_sl3     
single_counts:
    metric             | s0        | s1       | s2      
    -------------------+-----------+----------+---------
    cpu-cycles:u       | 186316672 | 34719915 | 49976104
    instructions:u     | 20150988  | 11280997 | 11290997
    br_retired:u       | 1991403   | 2021404  | 731404  
    br_mis_pred:u      | 592266    | 488      | 483     
    l1i_cache:u        | 8779364   | 1489856  | 1496618 
    l1i_cache_refill:u | 743       | 671      | 1428020 
    l1i_tlb:u          | 8779364   | 1489856  | 1496618 
    l1i_tlb_refill:u   | 52        | 50       | 660057  
    l2i_cache:u        | 742       | 670      | 1428019 
    l2i_cache_refill:u | 632       | 567      | 19390   
    l2i_tlb:u          | 108       | 204      | 660091  
    l2i_tlb_refill:u   | 46        | 29       | 113     
    l1d_cache:u        | 5996223   | 776022   | 775422  
    l1d_cache_refill:u | 2545407   | 640096   | 641288  
    l1d_tlb:u          | 10462983  | 1523639  | 1510810 
    l1d_tlb_refill:u   | 2489670   | 664948   | 663312  
    l2d_cache:u        | 11196605  | 2529229  | 3686227 
    l2d_cache_refill:u | 5443424   | 1282447  | 1304962 
    l2d_tlb:u          | 2501045   | 665206   | 663338  
    l2d_tlb_refill:u   | 683       | 252      | 104     
    ll_cache:u         | 5442390   | 1281822  | 1283617 
    ll_cache_miss:u    | 96582     | 187      | 376     
combined_orders:
    id        | modules                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp0_s16_r100_rand_p512_np4_l4+hot_b64_bp3_r100_lstr_p512_np4_l1_sl9+itlb_f64_l1_r100_lstr_p512_np2_l1_sl3
    shuffle   | hot_b64_bp3_r100_lstr_p512_np4_l1_sl9+fetch_b64_d1_bp0_s16_r100_rand_p512_np4_l4+itlb_f64_l1_r100_lstr_p512_np2_l1_sl3
    sum       | fetch_b64_d1_bp0_s16_r100_rand_p512_np4_l4+hot_b64_bp3_r100_lstr_p512_np4_l1_sl9+itlb_f64_l1_r100_lstr_p512_np2_l1_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 295944087 | 452046896 | 271012691
    instructions:u     | 42701689  | 42701548  | 42722982 
    br_retired:u       | 4741812   | 4741790   | 4744211  
    br_mis_pred:u      | 591651    | 593447    | 593237   
    l1i_cache:u        | 12832457  | 12897975  | 11765838 
    l1i_cache_refill:u | 1140432   | 1184498   | 1429434  
    l1i_tlb:u          | 12832457  | 12897975  | 11765838 
    l1i_tlb_refill:u   | 660447    | 660459    | 660159   
    l2i_cache:u        | 1140431   | 1184498   | 1429431  
    l2i_cache_refill:u | 38435     | 133738    | 20589    
    l2i_tlb:u          | 660707    | 660673    | 660403   
    l2i_tlb_refill:u   | 8573      | 8776      | 188      
    l1d_cache:u        | 7496907   | 7470845   | 7547667  
    l1d_cache_refill:u | 3800439   | 3809588   | 3826791  
    l1d_tlb:u          | 13627207  | 13479555  | 13497432 
    l1d_tlb_refill:u   | 3821721   | 3811678   | 3817930  
    l2d_cache:u        | 18069341  | 17568538  | 17412061 
    l2d_cache_refill:u | 8180511   | 8102042   | 8030833  
    l2d_tlb:u          | 3832270   | 3812038   | 3829589  
    l2d_tlb_refill:u   | 134028    | 134218    | 1039     
    ll_cache:u         | 8147556   | 7964071   | 8007829  
    ll_cache_miss:u    | 91000     | 71978     | 97145    

== combo_062_s3 ==
single_modules:
    id | module                                   
    ---+------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p512_np8_l2_sp33
    s1 | hot_b128_bp3_r100_lstr_p128_np2_l1_sl3   
    s2 | itlb_f128_l1_r100_pstr_p128_np8_l4_sp3   
single_counts:
    metric             | s0        | s1       | s2       
    -------------------+-----------+----------+----------
    cpu-cycles:u       | 145604680 | 46119789 | 246128683
    instructions:u     | 26870997  | 22160997 | 26011013 
    br_retired:u       | 1991404   | 3941404  | 1371404  
    br_mis_pred:u      | 290678    | 430      | 484      
    l1i_cache:u        | 7758547   | 2850564  | 3585161  
    l1i_cache_refill:u | 1235      | 696      | 2917498  
    l1i_tlb:u          | 7758547   | 2850564  | 3585161  
    l1i_tlb_refill:u   | 54        | 47       | 1310059  
    l2i_cache:u        | 1234      | 695      | 2917497  
    l2i_cache_refill:u | 913       | 582      | 1130537  
    l2i_tlb:u          | 99        | 136      | 1310098  
    l2i_tlb_refill:u   | 46        | 13       | 45       
    l1d_cache:u        | 4260315   | 1416304  | 5255989  
    l1d_cache_refill:u | 2522709   | 1223903  | 4936081  
    l1d_tlb:u          | 6964696   | 2836308  | 10513623 
    l1d_tlb_refill:u   | 2585305   | 1319476  | 5148018  
    l2d_cache:u        | 11202941  | 3909696  | 18399065 
    l2d_cache_refill:u | 5377401   | 1338003  | 6307451  
    l2d_tlb:u          | 2585343   | 1319808  | 5148071  
    l2d_tlb_refill:u   | 77        | 143      | 173      
    ll_cache:u         | 5376430   | 1337301  | 5196372  
    ll_cache_miss:u    | 33543     | 145      | 859      
combined_orders:
    id        | modules                                                                                                                
    ----------+------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p512_np8_l2_sp33+hot_b128_bp3_r100_lstr_p128_np2_l1_sl3+itlb_f128_l1_r100_pstr_p128_np8_l4_sp3
    shuffle   | itlb_f128_l1_r100_pstr_p128_np8_l4_sp3+hot_b128_bp3_r100_lstr_p128_np2_l1_sl3+cold_b128_d4_bitrev_pstr_p512_np8_l2_sp33
    sum       | cold_b128_d4_bitrev_pstr_p512_np8_l2_sp33+hot_b128_bp3_r100_lstr_p128_np2_l1_sl3+itlb_f128_l1_r100_pstr_p128_np8_l4_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 537569250 | 590818318 | 437853152
    instructions:u     | 75021542  | 75021542  | 75043007 
    br_retired:u       | 7301792   | 7301792   | 7304212  
    br_mis_pred:u      | 291308    | 290971    | 291592   
    l1i_cache:u        | 13632883  | 13618892  | 14194272 
    l1i_cache_refill:u | 3096136   | 2905688   | 2919429  
    l1i_tlb:u          | 13632883  | 13618892  | 14194272 
    l1i_tlb_refill:u   | 1300745   | 1300746   | 1310160  
    l2i_cache:u        | 3096133   | 2905686   | 2919426  
    l2i_cache_refill:u | 1400490   | 1199974   | 1132032  
    l2i_tlb:u          | 1300815   | 1300818   | 1310333  
    l2i_tlb_refill:u   | 1325      | 1230      | 104      
    l1d_cache:u        | 10923035  | 10926267  | 10932608 
    l1d_cache_refill:u | 8660017   | 8681561   | 8682693  
    l1d_tlb:u          | 20219967  | 20220666  | 20314627 
    l1d_tlb_refill:u   | 9027667   | 9029611   | 9052799  
    l2d_cache:u        | 33568638  | 33119758  | 33511702 
    l2d_cache_refill:u | 13348058  | 12910662  | 13022855 
    l2d_tlb:u          | 9028067   | 9029972   | 9053222  
    l2d_tlb_refill:u   | 3651      | 3430      | 393      
    ll_cache:u         | 12176567  | 11644016  | 11910103 
    ll_cache_miss:u    | 12547     | 13920     | 34547    

== combo_063_s3 ==
single_modules:
    id | module                                
    ---+---------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl5 
    s1 | hot_b64_bp3_r100_pstr_p512_np1_l1_sp17
    s2 | itlb_f128_l1_r100_lstr_p128_np8_l4_sl9
single_counts:
    metric             | s0       | s1       | s2       
    -------------------+----------+----------+----------
    cpu-cycles:u       | 8730083  | 34089225 | 246943514
    instructions:u     | 12951040 | 11280997 | 26011007 
    br_retired:u       | 1031409  | 2021404  | 1371406  
    br_mis_pred:u      | 130591   | 441      | 475      
    l1i_cache:u        | 3487816  | 1490887  | 3554011  
    l1i_cache_refill:u | 645      | 656      | 3005061  
    l1i_tlb:u          | 3487816  | 1490887  | 3554011  
    l1i_tlb_refill:u   | 42       | 52       | 1310065  
    l2i_cache:u        | 646      | 658      | 3005061  
    l2i_cache_refill:u | 568      | 584      | 1493310  
    l2i_tlb:u          | 75       | 131      | 1310107  
    l2i_tlb_refill:u   | 14       | 40       | 38       
    l1d_cache:u        | 1535167  | 775948   | 5255790  
    l1d_cache_refill:u | 157      | 640171   | 4928381  
    l1d_tlb:u          | 1537125  | 1531423  | 10481424 
    l1d_tlb_refill:u   | 57       | 666413   | 5142714  
    l2d_cache:u        | 1219     | 2528203  | 17504157 
    l2d_cache_refill:u | 787      | 1282217  | 5663686  
    l2d_tlb:u          | 77       | 666762   | 5142765  
    l2d_tlb_refill:u   | 31       | 557      | 28       
    ll_cache:u         | 209      | 1281538  | 3948263  
    ll_cache_miss:u    | 16       | 44       | 982      
combined_orders:
    id        | modules                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl5+hot_b64_bp3_r100_pstr_p512_np1_l1_sp17+itlb_f128_l1_r100_lstr_p128_np8_l4_sl9
    shuffle   | itlb_f128_l1_r100_lstr_p128_np8_l4_sl9+hot_b64_bp3_r100_pstr_p512_np1_l1_sp17+cold_b64_d4_bitrev_lstr_p1_np2_l1_sl5
    sum       | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl5+hot_b64_bp3_r100_pstr_p512_np1_l1_sp17+itlb_f128_l1_r100_lstr_p128_np8_l4_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 299535283 | 305646234 | 289762822
    instructions:u     | 50221698  | 50221698  | 50243044 
    br_retired:u       | 4421813   | 4421813   | 4424219  
    br_mis_pred:u      | 131464    | 130947    | 131507   
    l1i_cache:u        | 8521718   | 8637787   | 8532714  
    l1i_cache_refill:u | 3031798   | 2996941   | 3006362  
    l1i_tlb:u          | 8521718   | 8637787   | 8532714  
    l1i_tlb_refill:u   | 1310346   | 1310343   | 1310159  
    l2i_cache:u        | 3031796   | 2996935   | 3006365  
    l2i_cache_refill:u | 1708192   | 1686231   | 1494462  
    l2i_tlb:u          | 1310397   | 1310386   | 1310313  
    l2i_tlb_refill:u   | 634       | 129       | 92       
    l1d_cache:u        | 7558098   | 7557218   | 7566905  
    l1d_cache_refill:u | 5554340   | 5536292   | 5568709  
    l1d_tlb:u          | 13615416  | 13538185  | 13549972 
    l1d_tlb_refill:u   | 5831626   | 5808832   | 5809184  
    l2d_cache:u        | 20993828  | 20465943  | 20033579 
    l2d_cache_refill:u | 8189858   | 7406747   | 6946690  
    l2d_tlb:u          | 5832126   | 5809063   | 5809604  
    l2d_tlb_refill:u   | 1905      | 1621      | 616      
    ll_cache:u         | 6227182   | 5826693   | 5230010  
    ll_cache_miss:u    | 5861      | 6367      | 1042     

== combo_064_s3 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np8_l1_sp33
    s1 | hot_b64_bp3_r100_lin_p512_np4_l4               
    s2 | itlb_f64_l1_r100_pstr_p16_np8_l4_sp17          
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 40133004 | 86611987 | 28056153
    instructions:u     | 18230988 | 13200997 | 13210997
    br_retired:u       | 1991403  | 2021404  | 731404  
    br_mis_pred:u      | 596717   | 504      | 458     
    l1i_cache:u        | 8608794  | 1732754  | 1727678 
    l1i_cache_refill:u | 693      | 752      | 1388320 
    l1i_tlb:u          | 8608794  | 1732754  | 1727678 
    l1i_tlb_refill:u   | 52       | 49       | 670068  
    l2i_cache:u        | 694      | 752      | 1388319 
    l2i_cache_refill:u | 628      | 606      | 815     
    l2i_tlb:u          | 110      | 162      | 670118  
    l2i_tlb_refill:u   | 45       | 44       | 82      
    l1d_cache:u        | 4056580  | 2696247  | 2695238 
    l1d_cache_refill:u | 601257   | 889975   | 46071   
    l1d_tlb:u          | 6684403  | 3896003  | 2696951 
    l1d_tlb_refill:u   | 670058   | 660163   | 111     
    l2d_cache:u        | 1907697  | 9220397  | 1212813 
    l2d_cache_refill:u | 491122   | 4399079  | 1333    
    l2d_tlb:u          | 671473   | 660739   | 127     
    l2d_tlb_refill:u   | 108      | 84       | 8       
    ll_cache:u         | 490424   | 4398185  | 569     
    ll_cache_miss:u    | 325      | 3378     | 42      
combined_orders:
    id        | modules                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp0_s16_r100_pstr_p128_np8_l1_sp33+hot_b64_bp3_r100_lin_p512_np4_l4+itlb_f64_l1_r100_pstr_p16_np8_l4_sp17
    shuffle   | fetch_b64_d1_bp0_s16_r100_pstr_p128_np8_l1_sp33+itlb_f64_l1_r100_pstr_p16_np8_l4_sp17+hot_b64_bp3_r100_lin_p512_np4_l4
    sum       | fetch_b64_d1_bp0_s16_r100_pstr_p128_np8_l1_sp33+hot_b64_bp3_r100_lin_p512_np4_l4+itlb_f64_l1_r100_pstr_p16_np8_l4_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 152814402 | 156219993 | 154801144
    instructions:u     | 44621588  | 44621588  | 44642982 
    br_retired:u       | 4741803   | 4741803   | 4744211  
    br_mis_pred:u      | 593292    | 591328    | 597679   
    l1i_cache:u        | 13029705  | 13021705  | 12069226 
    l1i_cache_refill:u | 1276086   | 1010949   | 1389765  
    l1i_tlb:u          | 13029705  | 13021705  | 12069226 
    l1i_tlb_refill:u   | 660453    | 660482    | 670169   
    l2i_cache:u        | 1276085   | 1010950   | 1389765  
    l2i_cache_refill:u | 23468     | 125263    | 2049     
    l2i_tlb:u          | 660522    | 660578    | 670390   
    l2i_tlb_refill:u   | 154       | 216       | 171      
    l1d_cache:u        | 9394349   | 9419705   | 9448065  
    l1d_cache_refill:u | 1566066   | 1500019   | 1537303  
    l1d_tlb:u          | 13024885  | 13223877  | 13277357 
    l1d_tlb_refill:u   | 1325167   | 1340146   | 1330332  
    l2d_cache:u        | 12780420  | 12833448  | 12340907 
    l2d_cache_refill:u | 5383683   | 5234481   | 4891534  
    l2d_tlb:u          | 1326582   | 1361295   | 1332339  
    l2d_tlb_refill:u   | 1133      | 1918      | 200      
    ll_cache:u         | 5346646   | 5098812   | 4889178  
    ll_cache_miss:u    | 10411     | 10751     | 3745     

== combo_065_s3 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l1_sp17
    s1 | hot_b64_bp3_r100_rand_p512_np4_l2               
    s2 | itlb_f128_l1_r100_pstr_p128_np2_l1_sp3          
single_counts:
    metric             | s0        | s1       | s2       
    -------------------+-----------+----------+----------
    cpu-cycles:u       | 104298619 | 90619663 | 133985668
    instructions:u     | 36150988  | 11920997 | 22170997 
    br_retired:u       | 3911403   | 2021404  | 1371404  
    br_mis_pred:u      | 1235748   | 457      | 467      
    l1i_cache:u        | 16944683  | 1584052  | 3224206  
    l1i_cache_refill:u | 983       | 695      | 2801344  
    l1i_tlb:u          | 16944683  | 1584052  | 3224206  
    l1i_tlb_refill:u   | 58        | 49       | 1300050  
    l2i_cache:u        | 981       | 693      | 2801338  
    l2i_cache_refill:u | 777       | 554      | 1120703  
    l2i_tlb:u          | 98        | 86       | 1300095  
    l2i_tlb_refill:u   | 33        | 19       | 47       
    l1d_cache:u        | 7928539   | 1417024  | 1415745  
    l1d_cache_refill:u | 1264385   | 1286210  | 1222679  
    l1d_tlb:u          | 13193792  | 2766871  | 2784504  
    l1d_tlb_refill:u   | 1322166   | 1262574  | 1302849  
    l2d_cache:u        | 5612844   | 5127619  | 7324686  
    l2d_cache_refill:u | 2652126   | 2580207  | 2937262  
    l2d_tlb:u          | 1335450   | 1262856  | 1302887  
    l2d_tlb_refill:u   | 221       | 67       | 161      
    ll_cache:u         | 2651233   | 2579594  | 1719057  
    ll_cache_miss:u    | 13375     | 6005     | 4067     
combined_orders:
    id        | modules                                                                                                                  
    ----------+--------------------------------------------------------------------------------------------------------------------------
    canonical | fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l1_sp17+hot_b64_bp3_r100_rand_p512_np4_l2+itlb_f128_l1_r100_pstr_p128_np2_l1_sp3
    shuffle   | itlb_f128_l1_r100_pstr_p128_np2_l1_sp3+fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l1_sp17+hot_b64_bp3_r100_rand_p512_np4_l2
    sum       | fetch_b128_d1_bp0_s16_r100_pstr_p512_np4_l1_sp17+hot_b64_bp3_r100_rand_p512_np4_l2+itlb_f128_l1_r100_pstr_p128_np2_l1_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 427208209 | 452978408 | 328903950
    instructions:u     | 70221542  | 70221542  | 70242982 
    br_retired:u       | 7301792   | 7301792   | 7304211  
    br_mis_pred:u      | 1231649   | 1231833   | 1236672  
    l1i_cache:u        | 24046352  | 24105336  | 21752941 
    l1i_cache_refill:u | 3189075   | 3062245   | 2803022  
    l1i_tlb:u          | 24046352  | 24105336  | 21752941 
    l1i_tlb_refill:u   | 1300646   | 1300643   | 1300157  
    l2i_cache:u        | 3189073   | 3062242   | 2803012  
    l2i_cache_refill:u | 1498671   | 1413047   | 1122034  
    l2i_tlb:u          | 1300826   | 1300856   | 1300279  
    l2i_tlb_refill:u   | 8223      | 9838      | 99       
    l1d_cache:u        | 10705570  | 10723054  | 10761308 
    l1d_cache_refill:u | 3777997   | 3770103   | 3773274  
    l1d_tlb:u          | 18769351  | 18709294  | 18745167 
    l1d_tlb_refill:u   | 3914319   | 3873531   | 3887589  
    l2d_cache:u        | 19063811  | 19168480  | 18065149 
    l2d_cache_refill:u | 8741935   | 8828041   | 8169595  
    l2d_tlb:u          | 3926188   | 3882844   | 3901193  
    l2d_tlb_refill:u   | 61767     | 57316     | 449      
    ll_cache:u         | 7366694   | 7524819   | 6949884  
    ll_cache_miss:u    | 159345    | 150445    | 23447    

== combo_066_s3 ==
single_modules:
    id | module                                   
    ---+------------------------------------------
    s0 | fetch_b64_d1_bp0_s16_r100_lin_p128_np8_l4
    s1 | hot_b64_bp3_r100_pstr_p512_np8_l1_sp17   
    s2 | itlb_f64_l1_r100_rand_p1_np2_l1          
single_counts:
    metric             | s0       | s1       | s2      
    -------------------+----------+----------+---------
    cpu-cycles:u       | 47379666 | 43698991 | 22009059
    instructions:u     | 20150988 | 11280997 | 11291049
    br_retired:u       | 1991403  | 2021404  | 731410  
    br_mis_pred:u      | 590572   | 419      | 475     
    l1i_cache:u        | 8703060  | 1490674  | 1485677 
    l1i_cache_refill:u | 788      | 637      | 1837930 
    l1i_tlb:u          | 8703060  | 1490674  | 1485677 
    l1i_tlb_refill:u   | 53       | 43       | 660105  
    l2i_cache:u        | 787      | 635      | 1837929 
    l2i_cache_refill:u | 661      | 555      | 794     
    l2i_tlb:u          | 94       | 130      | 660214  
    l2i_tlb_refill:u   | 17       | 20       | 78      
    l1d_cache:u        | 5969495  | 776139   | 775383  
    l1d_cache_refill:u | 650541   | 640217   | 148     
    l1d_tlb:u          | 8216849  | 1526040  | 777276  
    l1d_tlb_refill:u   | 340061   | 665438   | 62      
    l2d_cache:u        | 6477483  | 2531528  | 1417475 
    l2d_cache_refill:u | 832172   | 1283809  | 1184    
    l2d_tlb:u          | 340083   | 665710   | 94      
    l2d_tlb_refill:u   | 20       | 126      | 32      
    ll_cache:u         | 831527   | 1283152  | 303     
    ll_cache_miss:u    | 4868     | 2114     | 62      
combined_orders:
    id        | modules                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------
    canonical | fetch_b64_d1_bp0_s16_r100_lin_p128_np8_l4+hot_b64_bp3_r100_pstr_p512_np8_l1_sp17+itlb_f64_l1_r100_rand_p1_np2_l1
    shuffle   | itlb_f64_l1_r100_rand_p1_np2_l1+hot_b64_bp3_r100_pstr_p512_np8_l1_sp17+fetch_b64_d1_bp0_s16_r100_lin_p128_np8_l4
    sum       | fetch_b64_d1_bp0_s16_r100_lin_p128_np8_l4+hot_b64_bp3_r100_pstr_p512_np8_l1_sp17+itlb_f64_l1_r100_rand_p1_np2_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 119601762 | 122885173 | 113087716
    instructions:u     | 42701597  | 42701597  | 42723034 
    br_retired:u       | 4741804   | 4741804   | 4744217  
    br_mis_pred:u      | 591489    | 591749    | 591466   
    l1i_cache:u        | 12804763  | 12810402  | 11679411 
    l1i_cache_refill:u | 1636576   | 1119457   | 1839355  
    l1i_tlb:u          | 12804763  | 12810402  | 11679411 
    l1i_tlb_refill:u   | 660454    | 660453    | 660201   
    l2i_cache:u        | 1636575   | 1119457   | 1839351  
    l2i_cache_refill:u | 14511     | 18507     | 2010     
    l2i_tlb:u          | 660514    | 660513    | 660438   
    l2i_tlb_refill:u   | 73        | 86        | 115      
    l1d_cache:u        | 7457765   | 7459375   | 7521017  
    l1d_cache_refill:u | 1322814   | 1334851   | 1290906  
    l1d_tlb:u          | 10417313  | 10495066  | 10520165 
    l1d_tlb_refill:u   | 1005607   | 1029766   | 1005561  
    l2d_cache:u        | 12602131  | 12728267  | 10426486 
    l2d_cache_refill:u | 3365800   | 3312169   | 2117165  
    l2d_tlb:u          | 1005914   | 1030213   | 1005887  
    l2d_tlb_refill:u   | 268       | 1509      | 178      
    ll_cache:u         | 3352547   | 3296149   | 2114982  
    ll_cache_miss:u    | 41955     | 54613     | 7044     

== combo_067_s4 ==
single_modules:
    id | module                                     
    ---+--------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p16_np1_l1_sp33    
    s1 | fetch_b128_d1_bp0_s16_r100_rand_p128_np1_l2
    s2 | hot_b128_bp3_r100_pstr_p128_np1_l1_sp3     
    s3 | itlb_f64_l1_r100_rand_p128_np1_l2          
single_counts:
    metric             | s0       | s1        | s2       | s3       
    -------------------+----------+-----------+----------+----------
    cpu-cycles:u       | 9340623  | 123180558 | 52431285 | 136140614
    instructions:u     | 12951049 | 37430988  | 22160997 | 11930997 
    br_retired:u       | 1031410  | 3911403   | 3941404  | 731404   
    br_mis_pred:u      | 130415   | 1232897   | 470      | 463      
    l1i_cache:u        | 3705228  | 17074941  | 2850334  | 1597598  
    l1i_cache_refill:u | 687      | 1057      | 751      | 1205393  
    l1i_tlb:u          | 3705228  | 17074941  | 2850334  | 1597598  
    l1i_tlb_refill:u   | 57       | 51        | 45       | 660085   
    l2i_cache:u        | 687      | 1056      | 751      | 1205392  
    l2i_cache_refill:u | 588      | 761       | 610      | 793770   
    l2i_tlb:u          | 94       | 98        | 82       | 660167   
    l2i_tlb_refill:u   | 21       | 19        | 14       | 105      
    l1d_cache:u        | 1535303  | 9164658   | 1416228  | 1415533  
    l1d_cache_refill:u | 44993    | 2423828   | 1206451  | 1229513  
    l1d_tlb:u          | 1537461  | 15610649  | 2787450  | 2822655  
    l1d_tlb_refill:u   | 87       | 2600095   | 1300233  | 1307754  
    l2d_cache:u        | 101300   | 8164360   | 3630809  | 5437463  
    l2d_cache_refill:u | 911      | 2606551   | 1068177  | 2449397  
    l2d_tlb:u          | 119      | 2615716   | 1300442  | 1307778  
    l2d_tlb_refill:u   | 9        | 17        | 160      | 14       
    ll_cache:u         | 280      | 2605745   | 1067456  | 1739157  
    ll_cache_miss:u    | 25       | 86        | 40       | 279      
combined_orders:
    id        | modules                                                                                                                                                     
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p16_np1_l1_sp33+fetch_b128_d1_bp0_s16_r100_rand_p128_np1_l2+hot_b128_bp3_r100_pstr_p128_np1_l1_sp3+itlb_f64_l1_r100_rand_p128_np1_l2
    shuffle   | itlb_f64_l1_r100_rand_p128_np1_l2+fetch_b128_d1_bp0_s16_r100_rand_p128_np1_l2+cold_b64_d4_bitrev_pstr_p16_np1_l1_sp33+hot_b128_bp3_r100_pstr_p128_np1_l1_sp3
    sum       | cold_b64_d4_bitrev_pstr_p16_np1_l1_sp33+fetch_b128_d1_bp0_s16_r100_rand_p128_np1_l2+hot_b128_bp3_r100_pstr_p128_np1_l1_sp3+itlb_f64_l1_r100_rand_p128_np1_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 332040364 | 339017442 | 321093080
    instructions:u     | 84441851  | 84441857  | 84474031 
    br_retired:u       | 9611993   | 9611991   | 9615621  
    br_mis_pred:u      | 1362037   | 1382209   | 1364245  
    l1i_cache:u        | 27354111  | 27579687  | 25228101 
    l1i_cache_refill:u | 1201868   | 1100306   | 1207888  
    l1i_tlb:u          | 27354111  | 27579687  | 25228101 
    l1i_tlb_refill:u   | 660968    | 661066    | 660238   
    l2i_cache:u        | 1201867   | 1100305   | 1207886  
    l2i_cache_refill:u | 842589    | 796139    | 795729   
    l2i_tlb:u          | 661080    | 661232    | 660441   
    l2i_tlb_refill:u   | 179       | 69        | 159      
    l1d_cache:u        | 13505286  | 13490923  | 13531722 
    l1d_cache_refill:u | 4935264   | 4982057   | 4904785  
    l1d_tlb:u          | 22812020  | 22637415  | 22758215 
    l1d_tlb_refill:u   | 5206223   | 5205996   | 5208169  
    l2d_cache:u        | 18301670  | 17820000  | 17333932 
    l2d_cache_refill:u | 7043336   | 6682705   | 6125036  
    l2d_tlb:u          | 5220753   | 5209885   | 5224055  
    l2d_tlb_refill:u   | 204       | 458       | 200      
    ll_cache:u         | 6310269   | 5970321   | 5412638  
    ll_cache_miss:u    | 30971     | 692       | 430      

== combo_068_s4 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p128_np2_l1_sp3      
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p1_np4_l4_sp3
    s2 | hot_b128_bp3_r100_pstr_p1_np1_l4_sp3         
    s3 | itlb_f64_l1_r100_lshuf_p16_np1_l1            
single_counts:
    metric             | s0       | s1       | s2       | s3      
    -------------------+----------+----------+----------+---------
    cpu-cycles:u       | 22262413 | 60288338 | 25721545 | 26737724
    instructions:u     | 12951049 | 39990997 | 26001058 | 11290997
    br_retired:u       | 1031410  | 3911404  | 3941411  | 731404  
    br_mis_pred:u      | 130434   | 1230518  | 463      | 442     
    l1i_cache:u        | 3687007  | 19658128 | 3327790  | 1480047 
    l1i_cache_refill:u | 677      | 906      | 756      | 1747537 
    l1i_tlb:u          | 3687007  | 19658128 | 3327790  | 1480047 
    l1i_tlb_refill:u   | 53       | 46       | 50       | 660057  
    l2i_cache:u        | 678      | 905      | 755      | 1747534 
    l2i_cache_refill:u | 608      | 717      | 601      | 76169   
    l2i_tlb:u          | 93       | 86       | 106      | 660095  
    l2i_tlb_refill:u   | 20       | 15       | 43       | 19      
    l1d_cache:u        | 1535859  | 11665663 | 5255420  | 775213  
    l1d_cache_refill:u | 598875   | 180      | 143      | 15224   
    l1d_tlb:u          | 2291727  | 15299444 | 5257557  | 776949  
    l1d_tlb_refill:u   | 661562   | 60       | 69       | 112     
    l2d_cache:u        | 2001868  | 1879     | 1301     | 1415332 
    l2d_cache_refill:u | 627683   | 1214     | 861      | 41203   
    l2d_tlb:u          | 665447   | 89       | 102      | 129     
    l2d_tlb_refill:u   | 146      | 32       | 6        | 8       
    ll_cache:u         | 626963   | 405      | 250      | 20401   
    ll_cache_miss:u    | 187      | 40       | 19       | 21      
combined_orders:
    id        | modules                                                                                                                                                     
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p128_np2_l1_sp3+fetch_b128_d1_bp0_s16_r100_pstr_p1_np4_l4_sp3+hot_b128_bp3_r100_pstr_p1_np1_l4_sp3+itlb_f64_l1_r100_lshuf_p16_np1_l1
    shuffle   | itlb_f64_l1_r100_lshuf_p16_np1_l1+fetch_b128_d1_bp0_s16_r100_pstr_p1_np4_l4_sp3+cold_b64_d4_bitrev_pstr_p128_np2_l1_sp3+hot_b128_bp3_r100_pstr_p1_np1_l4_sp3
    sum       | cold_b64_d4_bitrev_pstr_p128_np2_l1_sp3+fetch_b128_d1_bp0_s16_r100_pstr_p1_np4_l4_sp3+hot_b128_bp3_r100_pstr_p1_np1_l4_sp3+itlb_f64_l1_r100_lshuf_p16_np1_l1
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 130380532 | 131654598 | 135010020
    instructions:u     | 90201888  | 90201888  | 90234101 
    br_retired:u       | 9612003   | 9612003   | 9615629  
    br_mis_pred:u      | 1361707   | 1362038   | 1361857  
    l1i_cache:u        | 27900186  | 27932206  | 28152972 
    l1i_cache_refill:u | 1124420   | 1011010   | 1749876  
    l1i_tlb:u          | 27900186  | 27932206  | 28152972 
    l1i_tlb_refill:u   | 670961    | 671042    | 660206   
    l2i_cache:u        | 1124419   | 1011009   | 1749872  
    l2i_cache_refill:u | 13998     | 13566     | 78095    
    l2i_tlb:u          | 671107    | 671276    | 660380   
    l2i_tlb_refill:u   | 29        | 37        | 97       
    l1d_cache:u        | 19233278  | 19218528  | 19232155 
    l1d_cache_refill:u | 605693    | 609142    | 614422   
    l1d_tlb:u          | 23728055  | 23620239  | 23625677 
    l1d_tlb_refill:u   | 679195    | 669130    | 661803   
    l2d_cache:u        | 3180714   | 2984755   | 3420380  
    l2d_cache_refill:u | 555446    | 542376    | 670961   
    l2d_tlb:u          | 679336    | 671237    | 665767   
    l2d_tlb_refill:u   | 179       | 178       | 192      
    ll_cache:u         | 540555    | 517411    | 648019   
    ll_cache_miss:u    | 668       | 2778      | 267      

== combo_069_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p1_np1_l2               
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p128_np2_l4_sl5
    s2 | hot_b128_bp3_r100_pstr_p128_np1_l4_sp17        
    s3 | itlb_f64_l1_r100_pstr_p128_np1_l2_sp17         
single_counts:
    metric             | s0       | s1        | s2        | s3       
    -------------------+----------+-----------+-----------+----------
    cpu-cycles:u       | 11300723 | 199921240 | 161754251 | 106313701
    instructions:u     | 13591040 | 39990988  | 26000997  | 11930997 
    br_retired:u       | 1031409  | 3911403   | 3941404   | 731404   
    br_mis_pred:u      | 130411   | 1260209   | 464       | 478      
    l1i_cache:u        | 3556314  | 17966190  | 3331057   | 1597610  
    l1i_cache_refill:u | 665      | 1579      | 1148      | 1153942  
    l1i_tlb:u          | 3556314  | 17966190  | 3331057   | 1597610  
    l1i_tlb_refill:u   | 40       | 46        | 53        | 660094   
    l2i_cache:u        | 664      | 1580      | 1148      | 1153940  
    l2i_cache_refill:u | 590      | 842       | 694       | 751104   
    l2i_tlb:u          | 72       | 93        | 191       | 660166   
    l2i_tlb_refill:u   | 12       | 19        | 45        | 27       
    l1d_cache:u        | 2175337  | 11719116  | 5256981   | 1415442  
    l1d_cache_refill:u | 151      | 4793382   | 4821824   | 1248855  
    l1d_tlb:u          | 2177526  | 20718102  | 10451435  | 2767045  
    l1d_tlb_refill:u   | 62       | 5160065   | 5140160   | 1300072  
    l2d_cache:u        | 1523     | 15183449  | 15358760  | 6269904  
    l2d_cache_refill:u | 1047     | 4127937   | 5114586   | 2997699  
    l2d_tlb:u          | 88       | 5180169   | 5140472   | 1300093  
    l2d_tlb_refill:u   | 32       | 128       | 140       | 18       
    ll_cache:u         | 362      | 4126989   | 5113748   | 2019473  
    ll_cache_miss:u    | 36       | 199       | 30        | 28       
combined_orders:
    id        | modules                                                                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p1_np1_l2+fetch_b128_d1_bp0_s16_r100_lstr_p128_np2_l4_sl5+hot_b128_bp3_r100_pstr_p128_np1_l4_sp17+itlb_f64_l1_r100_pstr_p128_np1_l2_sp17
    shuffle   | itlb_f64_l1_r100_pstr_p128_np1_l2_sp17+fetch_b128_d1_bp0_s16_r100_lstr_p128_np2_l4_sl5+hot_b128_bp3_r100_pstr_p128_np1_l4_sp17+cold_b64_d4_bitrev_lin_p1_np1_l2
    sum       | cold_b64_d4_bitrev_lin_p1_np1_l2+fetch_b128_d1_bp0_s16_r100_lstr_p128_np2_l4_sl5+hot_b128_bp3_r100_pstr_p128_np1_l4_sp17+itlb_f64_l1_r100_pstr_p128_np1_l2_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 513576721 | 807653278 | 479289915
    instructions:u     | 91481848  | 91481842  | 91514022 
    br_retired:u       | 9611990   | 9611992   | 9615620  
    br_mis_pred:u      | 1367692   | 1362856   | 1391562  
    l1i_cache:u        | 28447675  | 28356313  | 26451171 
    l1i_cache_refill:u | 1129868   | 1129639   | 1157334  
    l1i_tlb:u          | 28447675  | 28356313  | 26451171 
    l1i_tlb_refill:u   | 670974    | 670945    | 660233   
    l2i_cache:u        | 1129865   | 1129640   | 1157332  
    l2i_cache_refill:u | 778152    | 769358    | 753230   
    l2i_tlb:u          | 671147    | 671101    | 660522   
    l2i_tlb_refill:u   | 216       | 49        | 103      
    l1d_cache:u        | 20590240  | 20585213  | 20566876 
    l1d_cache_refill:u | 11056012  | 11015250  | 10864212 
    l1d_tlb:u          | 36309219  | 36181783  | 36114108 
    l1d_tlb_refill:u   | 11614909  | 11610232  | 11600359 
    l2d_cache:u        | 38021265  | 37134430  | 36813636 
    l2d_cache_refill:u | 13198505  | 12736924  | 12241269 
    l2d_tlb:u          | 11623815  | 11620884  | 11620822 
    l2d_tlb_refill:u   | 465       | 511       | 318      
    ll_cache:u         | 12388238  | 11975357  | 11260572 
    ll_cache_miss:u    | 16612     | 1042      | 293      

== combo_070_s4 ==
single_modules:
    id | module                                      
    ---+---------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p512_np2_l4_sl9    
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p1_np8_l4_sp3
    s2 | hot_b128_bp3_r100_lstr_p16_np8_l1_sl9       
    s3 | itlb_f128_l1_r100_lstr_p1_np2_l4_sl5        
single_counts:
    metric             | s0        | s1       | s2       | s3       
    -------------------+-----------+----------+----------+----------
    cpu-cycles:u       | 270433181 | 29394821 | 10691917 | 115812762
    instructions:u     | 29431098  | 20150997 | 22161055 | 26010997 
    br_retired:u       | 1991413   | 1991404  | 3941408  | 1371404  
    br_mis_pred:u      | 290714    | 591069   | 396      | 508      
    l1i_cache:u        | 8163242   | 9783377  | 2846068  | 3633044  
    l1i_cache_refill:u | 1316      | 705      | 667      | 2977791  
    l1i_tlb:u          | 8163242   | 9783377  | 2846068  | 3633044  
    l1i_tlb_refill:u   | 47        | 50       | 54       | 1310058  
    l2i_cache:u        | 1315      | 702      | 667      | 2977790  
    l2i_cache_refill:u | 806       | 612      | 598      | 1057764  
    l2i_tlb:u          | 84        | 90       | 96       | 1310113  
    l2i_tlb_refill:u   | 19        | 12       | 13       | 156      
    l1d_cache:u        | 6818669   | 5905559  | 1415276  | 5255807  
    l1d_cache_refill:u | 5043253   | 154      | 30862    | 6559     
    l1d_tlb:u          | 12060891  | 7629075  | 1417357  | 5257948  
    l1d_tlb_refill:u   | 5142283   | 62       | 91       | 73       
    l2d_cache:u        | 22091154  | 1472     | 52952    | 3434363  
    l2d_cache_refill:u | 10816327  | 1007     | 1166     | 1440591  
    l2d_tlb:u          | 5142344   | 87       | 113      | 104      
    l2d_tlb_refill:u   | 71        | 23       | 5        | 31       
    ll_cache:u         | 10815167  | 345      | 544      | 3800     
    ll_cache_miss:u    | 66593     | 36       | 63       | 23       
combined_orders:
    id        | modules                                                                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p512_np2_l4_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p1_np8_l4_sp3+hot_b128_bp3_r100_lstr_p16_np8_l1_sl9+itlb_f128_l1_r100_lstr_p1_np2_l4_sl5
    shuffle   | hot_b128_bp3_r100_lstr_p16_np8_l1_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p1_np8_l4_sp3+cold_b128_d4_bitrev_lstr_p512_np2_l4_sl9+itlb_f128_l1_r100_lstr_p1_np2_l4_sl5
    sum       | cold_b128_d4_bitrev_lstr_p512_np2_l4_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p1_np8_l4_sp3+hot_b128_bp3_r100_lstr_p16_np8_l1_sl9+itlb_f128_l1_r100_lstr_p1_np2_l4_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 433557003 | 413922500 | 426332681
    instructions:u     | 97721842  | 97721842  | 97754147 
    br_retired:u       | 9291992   | 9291992   | 9295629  
    br_mis_pred:u      | 882021    | 882036    | 882687   
    l1i_cache:u        | 23759212  | 23586201  | 24425731 
    l1i_cache_refill:u | 3166604   | 2954273   | 2980479  
    l1i_tlb:u          | 23759212  | 23586201  | 24425731 
    l1i_tlb_refill:u   | 1301054   | 1301048   | 1310209  
    l2i_cache:u        | 3166603   | 2954272   | 2980474  
    l2i_cache_refill:u | 727164    | 999766    | 1059780  
    l2i_tlb:u          | 1301120   | 1301204   | 1310383  
    l2i_tlb_refill:u   | 253       | 346       | 200      
    l1d_cache:u        | 19380894  | 19381026  | 19395311 
    l1d_cache_refill:u | 5058661   | 5094443   | 5080828  
    l1d_tlb:u          | 26377705  | 26367319  | 26365271 
    l1d_tlb_refill:u   | 5147608   | 5144934   | 5142509  
    l2d_cache:u        | 25481950  | 25626176  | 25579941 
    l2d_cache_refill:u | 11496626  | 11982732  | 12259091 
    l2d_tlb:u          | 5147658   | 5144985   | 5142648  
    l2d_tlb_refill:u   | 1030      | 345       | 130      
    ll_cache:u         | 10867623  | 10908913  | 10819856 
    ll_cache_miss:u    | 42518     | 97815     | 66715    

== combo_071_s4 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p16_np1_l2            
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p16_np2_l1_sp3
    s2 | hot_b128_bp3_r100_lstr_p16_np2_l2_sl5        
    s3 | itlb_f128_l1_r100_pstr_p16_np4_l4_sp3        
single_counts:
    metric             | s0       | s1       | s2       | s3       
    -------------------+----------+----------+----------+----------
    cpu-cycles:u       | 12235753 | 21189435 | 15492388 | 116131460
    instructions:u     | 13591055 | 18231040 | 23441055 | 26010997 
    br_retired:u       | 1031408  | 1991409  | 3941408  | 1371404  
    br_mis_pred:u      | 130401   | 591019   | 453      | 478      
    l1i_cache:u        | 3782445  | 8413178  | 3006251  | 3617793  
    l1i_cache_refill:u | 686      | 663      | 682      | 3072833  
    l1i_tlb:u          | 3782445  | 8413178  | 3006251  | 3617793  
    l1i_tlb_refill:u   | 57       | 46       | 46       | 1310071  
    l2i_cache:u        | 685      | 663      | 681      | 3072831  
    l2i_cache_refill:u | 591      | 572      | 585      | 1042519  
    l2i_tlb:u          | 92       | 87       | 89       | 1310108  
    l2i_tlb_refill:u   | 16       | 14       | 12       | 30       
    l1d_cache:u        | 2175316  | 4005200  | 2695344  | 5255365  
    l1d_cache_refill:u | 167      | 48991    | 214      | 80530    
    l1d_tlb:u          | 2177482  | 5758893  | 2740468  | 5257464  
    l1d_tlb_refill:u   | 92       | 112      | 92       | 277      
    l2d_cache:u        | 1546     | 93996    | 1679     | 3154527  
    l2d_cache_refill:u | 1062     | 864      | 1117     | 1038886  
    l2d_tlb:u          | 119      | 136      | 116      | 298      
    l2d_tlb_refill:u   | 39       | 11       | 46       | 12       
    ll_cache:u         | 384      | 281      | 425      | 110830   
    ll_cache_miss:u    | 22       | 29       | 23       | 59       
combined_orders:
    id        | modules                                                                                                                                                    
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p16_np1_l2+fetch_b64_d1_bp0_s16_r100_pstr_p16_np2_l1_sp3+hot_b128_bp3_r100_lstr_p16_np2_l2_sl5+itlb_f128_l1_r100_pstr_p16_np4_l4_sp3
    shuffle   | cold_b64_d4_bitrev_lin_p16_np1_l2+itlb_f128_l1_r100_pstr_p16_np4_l4_sp3+fetch_b64_d1_bp0_s16_r100_pstr_p16_np2_l1_sp3+hot_b128_bp3_r100_lstr_p16_np2_l2_sl5
    sum       | cold_b64_d4_bitrev_lin_p16_np1_l2+fetch_b64_d1_bp0_s16_r100_pstr_p16_np2_l1_sp3+hot_b128_bp3_r100_lstr_p16_np2_l2_sl5+itlb_f128_l1_r100_pstr_p16_np4_l4_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 158963237 | 160905671 | 165049036
    instructions:u     | 81241897  | 81241903  | 81274147 
    br_retired:u       | 8332004   | 8332002   | 8335629  
    br_mis_pred:u      | 722198    | 722296    | 722351   
    l1i_cache:u        | 19686188  | 19718780  | 18819667 
    l1i_cache_refill:u | 2947017   | 2981551   | 3074864  
    l1i_tlb:u          | 19686188  | 19718780  | 18819667 
    l1i_tlb_refill:u   | 1300749   | 1300851   | 1310220  
    l2i_cache:u        | 2947013   | 2981546   | 3074860  
    l2i_cache_refill:u | 887755    | 884833    | 1044267  
    l2i_tlb:u          | 1300869   | 1300909   | 1310376  
    l2i_tlb_refill:u   | 30        | 184       | 72       
    l1d_cache:u        | 14087097  | 14096429  | 14131225 
    l1d_cache_refill:u | 190765    | 176357    | 129902   
    l1d_tlb:u          | 15848926  | 15847909  | 15934307 
    l1d_tlb_refill:u   | 7231      | 7325      | 573      
    l2d_cache:u        | 4014309   | 3958165   | 3251748  
    l2d_cache_refill:u | 1229381   | 972978    | 1041929  
    l2d_tlb:u          | 7253      | 7352      | 669      
    l2d_tlb_refill:u   | 25        | 12        | 108      
    ll_cache:u         | 128756    | 132437    | 111920   
    ll_cache_miss:u    | 351       | 50        | 133      

== combo_072_s4 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_rand_p16_np2_l2           
    s1 | fetch_b64_d1_bp0_s16_r100_lstr_p512_np1_l4_sl3
    s2 | hot_b128_bp3_r100_lstr_p16_np8_l4_sl3         
    s3 | itlb_f128_l1_r100_pstr_p512_np2_l1_sp17       
single_counts:
    metric             | s0       | s1        | s2       | s3       
    -------------------+----------+-----------+----------+----------
    cpu-cycles:u       | 24421925 | 165992013 | 25743661 | 164996024
    instructions:u     | 26871049 | 20150988  | 26001049 | 22171003 
    br_retired:u       | 1991410  | 1991403   | 3941410  | 1371402  
    br_mis_pred:u      | 290421   | 593835    | 445      | 508      
    l1i_cache:u        | 7746343  | 8866919   | 3326771  | 3056518  
    l1i_cache_refill:u | 820      | 706       | 734      | 3163069  
    l1i_tlb:u          | 7746343  | 8866919   | 3326771  | 3056518  
    l1i_tlb_refill:u   | 49       | 45        | 46       | 1300067  
    l2i_cache:u        | 818      | 704       | 732      | 3163067  
    l2i_cache_refill:u | 683      | 614       | 624      | 1321385  
    l2i_tlb:u          | 84       | 80        | 78       | 1300138  
    l2i_tlb_refill:u   | 12       | 24        | 12       | 188      
    l1d_cache:u        | 4255414  | 5969324   | 5255758  | 1415688  
    l1d_cache_refill:u | 222      | 2525367   | 93761    | 1279904  
    l1d_tlb:u          | 4257678  | 10504000  | 5263628  | 2802474  
    l1d_tlb_refill:u   | 111      | 2590056   | 131      | 1304713  
    l2d_cache:u        | 1744     | 11007441  | 213924   | 8513808  
    l2d_cache_refill:u | 1143     | 5476026   | 1300     | 4098621  
    l2d_tlb:u          | 135      | 2594643   | 152      | 1304739  
    l2d_tlb_refill:u   | 7        | 112       | 9        | 214      
    ll_cache:u         | 379      | 5475225   | 642      | 2564012  
    ll_cache_miss:u    | 44       | 4418      | 101      | 365      
combined_orders:
    id        | modules                                                                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_rand_p16_np2_l2+fetch_b64_d1_bp0_s16_r100_lstr_p512_np1_l4_sl3+hot_b128_bp3_r100_lstr_p16_np8_l4_sl3+itlb_f128_l1_r100_pstr_p512_np2_l1_sp17
    shuffle   | itlb_f128_l1_r100_pstr_p512_np2_l1_sp17+cold_b128_d4_bitrev_rand_p16_np2_l2+fetch_b64_d1_bp0_s16_r100_lstr_p512_np1_l4_sl3+hot_b128_bp3_r100_lstr_p16_np8_l4_sl3
    sum       | cold_b128_d4_bitrev_rand_p16_np2_l2+fetch_b64_d1_bp0_s16_r100_lstr_p512_np1_l4_sl3+hot_b128_bp3_r100_lstr_p16_np8_l4_sl3+itlb_f128_l1_r100_pstr_p512_np2_l1_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 411626359 | 402420295 | 381153623
    instructions:u     | 95161851  | 95161857  | 95194089 
    br_retired:u       | 9291993   | 9291991   | 9295625  
    br_mis_pred:u      | 885057    | 884468    | 885209   
    l1i_cache:u        | 23485307  | 23508973  | 22996551 
    l1i_cache_refill:u | 2996663   | 2929624   | 3165329  
    l1i_tlb:u          | 23485307  | 23508973  | 22996551 
    l1i_tlb_refill:u   | 1301047   | 1301043   | 1300207  
    l2i_cache:u        | 2996659   | 2929624   | 3165321  
    l2i_cache_refill:u | 1339248   | 1326316   | 1323306  
    l2i_tlb:u          | 1301271   | 1301349   | 1300380  
    l2i_tlb_refill:u   | 9966      | 9837      | 236      
    l1d_cache:u        | 16864625  | 16864678  | 16896184 
    l1d_cache_refill:u | 3864340   | 3805436   | 3899254  
    l1d_tlb:u          | 22849922  | 22920126  | 22827780 
    l1d_tlb_refill:u   | 3910121   | 3908929   | 3895011  
    l2d_cache:u        | 19441194  | 19453780  | 19736917 
    l2d_cache_refill:u | 9247268   | 9374644   | 9577090  
    l2d_tlb:u          | 3917964   | 3910506   | 3899669  
    l2d_tlb_refill:u   | 50522     | 50970     | 342      
    ll_cache:u         | 7893994   | 7956388   | 8040258  
    ll_cache_miss:u    | 26025     | 42303     | 4928     

== combo_073_s4 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | cold_b128_d4_bitrev_lin_p128_np2_l4          
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p1_np8_l4_sp3
    s2 | hot_b128_bp3_r100_lstr_p128_np8_l4_sl5       
    s3 | itlb_f128_l1_r100_lstr_p512_np8_l4_sl3       
single_counts:
    metric             | s0        | s1       | s2        | s3       
    -------------------+-----------+----------+-----------+----------
    cpu-cycles:u       | 139846135 | 60297957 | 126061716 | 325902296
    instructions:u     | 29430997  | 39991003 | 26000997  | 26010951 
    br_retired:u       | 1991404   | 3911402  | 3941404   | 1371393  
    br_mis_pred:u      | 290692    | 1231084  | 481       | 481      
    l1i_cache:u        | 8113407   | 19663323 | 3336430   | 3761195  
    l1i_cache_refill:u | 1058      | 1124     | 1244      | 2832724  
    l1i_tlb:u          | 8113407   | 19663323 | 3336430   | 3761195  
    l1i_tlb_refill:u   | 54        | 50       | 52        | 1310056  
    l2i_cache:u        | 1058      | 1123     | 1243      | 2832722  
    l2i_cache_refill:u | 738       | 738      | 775       | 1249142  
    l2i_tlb:u          | 97        | 82       | 158       | 1310105  
    l2i_tlb_refill:u   | 14        | 11       | 19        | 71       
    l1d_cache:u        | 6826522   | 11655848 | 5256942   | 5255996  
    l1d_cache_refill:u | 3404636   | 185      | 4083490   | 2297633  
    l1d_tlb:u          | 10259460  | 15299707 | 8940349   | 7981266  
    l1d_tlb_refill:u   | 2590061   | 74       | 3220059   | 1950071  
    l2d_cache:u        | 13515810  | 1743     | 13385586  | 21820205 
    l2d_cache_refill:u | 3460843   | 1095     | 3334640   | 10663621 
    l2d_tlb:u          | 2590100   | 97       | 3220439   | 1950139  
    l2d_tlb_refill:u   | 117       | 13       | 21        | 210      
    ll_cache:u         | 3459765   | 316      | 3333849   | 9283049  
    ll_cache_miss:u    | 6775      | 38       | 470       | 9061     
combined_orders:
    id        | modules                                                                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lin_p128_np2_l4+fetch_b128_d1_bp0_s16_r100_pstr_p1_np8_l4_sp3+hot_b128_bp3_r100_lstr_p128_np8_l4_sl5+itlb_f128_l1_r100_lstr_p512_np8_l4_sl3
    shuffle   | cold_b128_d4_bitrev_lin_p128_np2_l4+hot_b128_bp3_r100_lstr_p128_np8_l4_sl5+itlb_f128_l1_r100_lstr_p512_np8_l4_sl3+fetch_b128_d1_bp0_s16_r100_pstr_p1_np8_l4_sp3
    sum       | cold_b128_d4_bitrev_lin_p128_np2_l4+fetch_b128_d1_bp0_s16_r100_pstr_p1_np8_l4_sp3+hot_b128_bp3_r100_lstr_p128_np8_l4_sl5+itlb_f128_l1_r100_lstr_p512_np8_l4_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 698755000 | 668409291 | 652108104
    instructions:u     | 121401851 | 121401851 | 121433948
    br_retired:u       | 11211993  | 11211993  | 11215603 
    br_mis_pred:u      | 1526077   | 1521630   | 1522738  
    l1i_cache:u        | 34137133  | 34085656  | 34874355 
    l1i_cache_refill:u | 3018432   | 2974816   | 2836150  
    l1i_tlb:u          | 34137133  | 34085656  | 34874355 
    l1i_tlb_refill:u   | 1311253   | 1311250   | 1310212  
    l2i_cache:u        | 3018431   | 2974816   | 2836146  
    l2i_cache_refill:u | 1391641   | 1438766   | 1251393  
    l2i_tlb:u          | 1311462   | 1311448   | 1310442  
    l2i_tlb_refill:u   | 1671      | 1617      | 115      
    l1d_cache:u        | 28977383  | 28985550  | 28995308 
    l1d_cache_refill:u | 10004977  | 10104459  | 9785944  
    l1d_tlb:u          | 42137432  | 41866555  | 42480782 
    l1d_tlb_refill:u   | 7770549   | 7740339   | 7760265  
    l2d_cache:u        | 50977468  | 51347809  | 48723344 
    l2d_cache_refill:u | 18322226  | 18170339  | 17460199 
    l2d_tlb:u          | 7771697   | 7744230   | 7760775  
    l2d_tlb_refill:u   | 6719      | 3855      | 361      
    ll_cache:u         | 16983420  | 16841655  | 16076979 
    ll_cache_miss:u    | 39420     | 31319     | 16344    

== combo_074_s4 ==
single_modules:
    id | module                                      
    ---+---------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p1_np2_l2_sl9      
    s1 | fetch_b128_d1_bp0_s16_r100_lshuf_p128_np4_l1
    s2 | hot_b64_bp3_r100_pstr_p128_np4_l1_sp3       
    s3 | itlb_f64_l1_r100_pstr_p512_np1_l2_sp17      
single_counts:
    metric             | s0       | s1       | s2       | s3       
    -------------------+----------+----------+----------+----------
    cpu-cycles:u       | 23276927 | 61795935 | 22556315 | 103594111
    instructions:u     | 26871046 | 36150988 | 11281049 | 11930997 
    br_retired:u       | 1991407  | 3911403  | 2021410  | 731404   
    br_mis_pred:u      | 290601   | 1237783  | 446      | 488      
    l1i_cache:u        | 7148095  | 16939788 | 1488793  | 1686442  
    l1i_cache_refill:u | 856      | 902      | 629      | 1030615  
    l1i_tlb:u          | 7148095  | 16939788 | 1488793  | 1686442  
    l1i_tlb_refill:u   | 49       | 47       | 41       | 660068   
    l2i_cache:u        | 855      | 901      | 629      | 1030615  
    l2i_cache_refill:u | 725      | 711      | 546      | 498432   
    l2i_tlb:u          | 77       | 88       | 75       | 660120   
    l2i_tlb_refill:u   | 14       | 12       | 14       | 122      
    l1d_cache:u        | 4255353  | 7910256  | 775672   | 1415663  
    l1d_cache_refill:u | 145      | 870537   | 612973   | 1277521  
    l1d_tlb:u          | 4257436  | 12156201 | 1554681  | 2800890  
    l1d_tlb_refill:u   | 60       | 350060   | 674071   | 1304582  
    l2d_cache:u        | 1402     | 4566085  | 1974239  | 6708408  
    l2d_cache_refill:u | 952      | 681583   | 692591   | 3215168  
    l2d_tlb:u          | 78       | 360091   | 674298   | 1304615  
    l2d_tlb_refill:u   | 6        | 11       | 12       | 666      
    ll_cache:u         | 235      | 680911   | 692047   | 2562143  
    ll_cache_miss:u    | 32       | 1358     | 124      | 57       
combined_orders:
    id        | modules                                                                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p1_np2_l2_sl9+fetch_b128_d1_bp0_s16_r100_lshuf_p128_np4_l1+hot_b64_bp3_r100_pstr_p128_np4_l1_sp3+itlb_f64_l1_r100_pstr_p512_np1_l2_sp17
    shuffle   | fetch_b128_d1_bp0_s16_r100_lshuf_p128_np4_l1+cold_b128_d4_bitrev_lstr_p1_np2_l2_sl9+hot_b64_bp3_r100_pstr_p128_np4_l1_sp3+itlb_f64_l1_r100_pstr_p512_np1_l2_sp17
    sum       | cold_b128_d4_bitrev_lstr_p1_np2_l2_sl9+fetch_b128_d1_bp0_s16_r100_lshuf_p128_np4_l1+hot_b64_bp3_r100_pstr_p128_np4_l1_sp3+itlb_f64_l1_r100_pstr_p512_np1_l2_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 224981829 | 217759265 | 211223288
    instructions:u     | 86201898  | 86201898  | 86234080 
    br_retired:u       | 8652005   | 8652005   | 8655624  
    br_mis_pred:u      | 1521647   | 1522622   | 1529318  
    l1i_cache:u        | 29596835  | 29561446  | 27263118 
    l1i_cache_refill:u | 1136831   | 1192930   | 1033002  
    l1i_tlb:u          | 29596835  | 29561446  | 27263118 
    l1i_tlb_refill:u   | 661054    | 661061    | 660205   
    l2i_cache:u        | 1136832   | 1192929   | 1033000  
    l2i_cache_refill:u | 644502    | 555018    | 500414   
    l2i_tlb:u          | 661131    | 661142    | 660360   
    l2i_tlb_refill:u   | 437       | 508       | 162      
    l1d_cache:u        | 14305158  | 14304931  | 14356944 
    l1d_cache_refill:u | 2796118   | 2843967   | 2761176  
    l1d_tlb:u          | 20591681  | 20788753  | 20769208 
    l1d_tlb_refill:u   | 2318744   | 2356621   | 2328773  
    l2d_cache:u        | 13535994  | 13363739  | 13250134 
    l2d_cache_refill:u | 5064891   | 5020590   | 4590294  
    l2d_tlb:u          | 2329644   | 2367124   | 2339082  
    l2d_tlb_refill:u   | 2354      | 1969      | 695      
    ll_cache:u         | 4410888   | 4410700   | 3935336  
    ll_cache_miss:u    | 22313     | 57858     | 1571     

== combo_075_s4 ==
single_modules:
    id | module                                     
    ---+--------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p128_np4_l2_sl3   
    s1 | fetch_b128_d1_bp0_s16_r100_rand_p512_np4_l4
    s2 | hot_b128_bp3_r100_pstr_p1_np2_l2_sp3       
    s3 | itlb_f128_l1_r100_lstr_p128_np8_l2_sl5     
single_counts:
    metric             | s0       | s1        | s2       | s3       
    -------------------+----------+-----------+----------+----------
    cpu-cycles:u       | 91665670 | 290175541 | 15488330 | 148410264
    instructions:u     | 26870997 | 39991089  | 23441049 | 23450997 
    br_retired:u       | 1991404  | 3911412   | 3941410  | 1371404  
    br_mis_pred:u      | 290695   | 1248592   | 432      | 468      
    l1i_cache:u        | 7770935  | 17587549  | 3016138  | 3277765  
    l1i_cache_refill:u | 1127     | 1642      | 755      | 2859705  
    l1i_tlb:u          | 7770935  | 17587549  | 3016138  | 3277765  
    l1i_tlb_refill:u   | 49       | 46        | 56       | 1310058  
    l2i_cache:u        | 1127     | 1640      | 755      | 2859705  
    l2i_cache_refill:u | 783      | 943       | 632      | 755530   
    l2i_tlb:u          | 86       | 85        | 94       | 1310094  
    l2i_tlb_refill:u   | 17       | 27        | 16       | 50       
    l1d_cache:u        | 4258802  | 11825412  | 2695486  | 2696027  
    l1d_cache_refill:u | 2229776  | 5080810   | 155      | 2111343  
    l1d_tlb:u          | 6413850  | 20756735  | 2697688  | 4716468  
    l1d_tlb_refill:u   | 1940063  | 4935607   | 60       | 1630070  
    l2d_cache:u        | 8055479  | 23325311  | 1434     | 10090381 
    l2d_cache_refill:u | 2524827  | 10704517  | 971      | 3183741  
    l2d_tlb:u          | 1940157  | 4938328   | 143      | 1630098  
    l2d_tlb_refill:u   | 24       | 110       | 32       | 18       
    ll_cache:u         | 2524043  | 10703367  | 300      | 2433371  
    ll_cache_miss:u    | 306      | 50286     | 22       | 6175     
combined_orders:
    id        | modules                                                                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p128_np4_l2_sl3+fetch_b128_d1_bp0_s16_r100_rand_p512_np4_l4+hot_b128_bp3_r100_pstr_p1_np2_l2_sp3+itlb_f128_l1_r100_lstr_p128_np8_l2_sl5
    shuffle   | cold_b128_d4_bitrev_lstr_p128_np4_l2_sl3+hot_b128_bp3_r100_pstr_p1_np2_l2_sp3+fetch_b128_d1_bp0_s16_r100_rand_p512_np4_l4+itlb_f128_l1_r100_lstr_p128_np8_l2_sl5
    sum       | cold_b128_d4_bitrev_lstr_p128_np4_l2_sl3+fetch_b128_d1_bp0_s16_r100_rand_p512_np4_l4+hot_b128_bp3_r100_pstr_p1_np2_l2_sp3+itlb_f128_l1_r100_lstr_p128_np8_l2_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 606127308 | 612538858 | 545739805
    instructions:u     | 113721842 | 113721842 | 113754132
    br_retired:u       | 11211992  | 11211992  | 11215630 
    br_mis_pred:u      | 1523618   | 1522781   | 1540187  
    l1i_cache:u        | 33387279  | 33377794  | 31652387 
    l1i_cache_refill:u | 2935327   | 2979350   | 2863229  
    l1i_tlb:u          | 33387279  | 33377794  | 31652387 
    l1i_tlb_refill:u   | 1311145   | 1311169   | 1310209  
    l2i_cache:u        | 2935326   | 2979349   | 2863227  
    l2i_cache_refill:u | 876299    | 1155842   | 757888   
    l2i_tlb:u          | 1311246   | 1311270   | 1310359  
    l2i_tlb_refill:u   | 1187      | 1319      | 110      
    l1d_cache:u        | 21348205  | 21358517  | 21475727 
    l1d_cache_refill:u | 9485630   | 9463886   | 9422084  
    l1d_tlb:u          | 34047031  | 34217409  | 34584741 
    l1d_tlb_refill:u   | 8495271   | 8531906   | 8505800  
    l2d_cache:u        | 41451330  | 41797222  | 41472605 
    l2d_cache_refill:u | 16469184  | 17045155  | 16414056 
    l2d_tlb:u          | 8506322   | 8544938   | 8508726  
    l2d_tlb_refill:u   | 3907      | 3644      | 184      
    ll_cache:u         | 15549644  | 15885074  | 15661081 
    ll_cache_miss:u    | 148167    | 119093    | 56789    

== combo_076_s4 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b64_d4_bitrev_lshuf_p16_np1_l1             
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17
    s2 | hot_b64_bp3_r100_lstr_p1_np4_l1_sl5             
    s3 | itlb_f128_l1_r100_pstr_p16_np4_l2_sp3           
single_counts:
    metric             | s0       | s1        | s2       | s3      
    -------------------+----------+-----------+----------+---------
    cpu-cycles:u       | 9270531  | 291418455 | 5247955  | 91565408
    instructions:u     | 12951049 | 39991095  | 11281040 | 23450997
    br_retired:u       | 1031410  | 3911410   | 2021409  | 1371404 
    br_mis_pred:u      | 130591   | 1233720   | 418      | 469     
    l1i_cache:u        | 3698210  | 17443593  | 1495931  | 3107107 
    l1i_cache_refill:u | 666      | 1270      | 602      | 3657139 
    l1i_tlb:u          | 3698210  | 17443593  | 1495931  | 3107107 
    l1i_tlb_refill:u   | 52       | 47        | 52       | 1310095 
    l2i_cache:u        | 665      | 1269      | 601      | 3657136 
    l2i_cache_refill:u | 582      | 809       | 560      | 1203908 
    l2i_tlb:u          | 94       | 91        | 98       | 1310175 
    l2i_tlb_refill:u   | 24       | 20        | 26       | 23      
    l1d_cache:u        | 1535260  | 11808889  | 775206   | 2695427 
    l1d_cache_refill:u | 163      | 5058309   | 139      | 118886  
    l1d_tlb:u          | 1537494  | 21128066  | 777249   | 2697680 
    l1d_tlb_refill:u   | 94       | 5180058   | 58       | 238     
    l2d_cache:u        | 1456     | 22251830  | 1255     | 3634285 
    l2d_cache_refill:u | 1010     | 10900966  | 925      | 1241662 
    l2d_tlb:u          | 118      | 5193000   | 87       | 266     
    l2d_tlb_refill:u   | 37       | 91        | 19       | 51      
    ll_cache:u         | 358      | 10904744  | 332      | 177774  
    ll_cache_miss:u    | 27       | 130897    | 19       | 64      
combined_orders:
    id        | modules                                                                                                                                                       
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lshuf_p16_np1_l1+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17+hot_b64_bp3_r100_lstr_p1_np4_l1_sl5+itlb_f128_l1_r100_pstr_p16_np4_l2_sp3
    shuffle   | cold_b64_d4_bitrev_lshuf_p16_np1_l1+hot_b64_bp3_r100_lstr_p1_np4_l1_sl5+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17+itlb_f128_l1_r100_pstr_p16_np4_l2_sp3
    sum       | cold_b64_d4_bitrev_lshuf_p16_np1_l1+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17+hot_b64_bp3_r100_lstr_p1_np4_l1_sl5+itlb_f128_l1_r100_pstr_p16_np4_l2_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 401167060 | 395797718 | 397502349
    instructions:u     | 87641851  | 87641864  | 87674181 
    br_retired:u       | 8331993   | 8331993   | 8335633  
    br_mis_pred:u      | 1377650   | 1384188   | 1365198  
    l1i_cache:u        | 28296595  | 28443582  | 25744841 
    l1i_cache_refill:u | 3055491   | 2950452   | 3659677  
    l1i_tlb:u          | 28296595  | 28443582  | 25744841 
    l1i_tlb_refill:u   | 1300852   | 1300880   | 1310246  
    l2i_cache:u        | 3055486   | 2950450   | 3659671  
    l2i_cache_refill:u | 992847    | 960148    | 1205859  
    l2i_tlb:u          | 1300906   | 1300947   | 1310458  
    l2i_tlb_refill:u   | 351       | 610       | 93       
    l1d_cache:u        | 16761226  | 16754964  | 16814782 
    l1d_cache_refill:u | 5123835   | 5107088   | 5177497  
    l1d_tlb:u          | 25838173  | 25829390  | 26140489 
    l1d_tlb_refill:u   | 5163840   | 5163714   | 5180448  
    l2d_cache:u        | 25982884  | 25895633  | 25888826 
    l2d_cache_refill:u | 12148177  | 12015923  | 12144563 
    l2d_tlb:u          | 5175622   | 5171960   | 5193471  
    l2d_tlb_refill:u   | 653       | 876       | 198      
    ll_cache:u         | 11081648  | 11076728  | 11083208 
    ll_cache_miss:u    | 75418     | 120834    | 131007   

== combo_077_s4 ==
single_modules:
    id | module                                     
    ---+--------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p16_np1_l2_sp17    
    s1 | fetch_b64_d1_bp0_s16_r100_lshuf_p512_np2_l4
    s2 | hot_b64_bp3_r100_pstr_p128_np1_l2_sp33     
    s3 | itlb_f64_l1_r100_lstr_p128_np4_l4_sl5      
single_counts:
    metric             | s0       | s1        | s2       | s3       
    -------------------+----------+-----------+----------+----------
    cpu-cycles:u       | 11413507 | 133043640 | 40304691 | 101023939
    instructions:u     | 13591049 | 20150988  | 11920997 | 13211003 
    br_retired:u       | 1031410  | 1991403   | 2021404  | 731402   
    br_mis_pred:u      | 130407   | 592675    | 438      | 469      
    l1i_cache:u        | 3776153  | 8769349   | 1568654  | 1776086  
    l1i_cache_refill:u | 709      | 682       | 724      | 1135570  
    l1i_tlb:u          | 3776153  | 8769349   | 1568654  | 1776086  
    l1i_tlb_refill:u   | 45       | 47        | 45       | 670086   
    l2i_cache:u        | 708      | 681       | 725      | 1135567  
    l2i_cache_refill:u | 592      | 597       | 517      | 198414   
    l2i_tlb:u          | 84       | 91        | 131      | 670139   
    l2i_tlb_refill:u   | 13       | 42        | 15       | 26       
    l1d_cache:u        | 2175249  | 5983823   | 1415933  | 2695245  
    l1d_cache_refill:u | 172      | 2200756   | 1220133  | 2466809  
    l1d_tlb:u          | 2177328  | 9258307   | 2768334  | 5415342  
    l1d_tlb_refill:u   | 90       | 1310064   | 1300080  | 2593177  
    l2d_cache:u        | 1227     | 11138613  | 3352237  | 8728936  
    l2d_cache_refill:u | 793      | 5257295   | 790655   | 2524080  
    l2d_tlb:u          | 119      | 1317351   | 1300199  | 2593202  
    l2d_tlb_refill:u   | 5        | 635       | 129      | 36       
    ll_cache:u         | 259      | 5256160   | 790025   | 2453050  
    ll_cache_miss:u    | 12       | 26640     | 43       | 164      
combined_orders:
    id        | modules                                                                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p16_np1_l2_sp17+fetch_b64_d1_bp0_s16_r100_lshuf_p512_np2_l4+hot_b64_bp3_r100_pstr_p128_np1_l2_sp33+itlb_f64_l1_r100_lstr_p128_np4_l4_sl5
    shuffle   | itlb_f64_l1_r100_lstr_p128_np4_l4_sl5+hot_b64_bp3_r100_pstr_p128_np1_l2_sp33+fetch_b64_d1_bp0_s16_r100_lshuf_p512_np2_l4+cold_b64_d4_bitrev_pstr_p16_np1_l2_sp17
    sum       | cold_b64_d4_bitrev_pstr_p16_np1_l2_sp17+fetch_b64_d1_bp0_s16_r100_lshuf_p512_np2_l4+hot_b64_bp3_r100_pstr_p128_np1_l2_sp33+itlb_f64_l1_r100_lstr_p128_np4_l4_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 338789010 | 343254860 | 285785777
    instructions:u     | 58841857  | 58841857  | 58874037 
    br_retired:u       | 5771991   | 5771991   | 5775619  
    br_mis_pred:u      | 726960    | 722309    | 723989   
    l1i_cache:u        | 16855135  | 16858698  | 15890242 
    l1i_cache_refill:u | 1312745   | 1111781   | 1137685  
    l1i_tlb:u          | 16855135  | 16858698  | 15890242 
    l1i_tlb_refill:u   | 660648    | 660652    | 670223   
    l2i_cache:u        | 1312745   | 1111778   | 1137681  
    l2i_cache_refill:u | 358283    | 328267    | 200120   
    l2i_tlb:u          | 660704    | 660691    | 670445   
    l2i_tlb_refill:u   | 713       | 1304      | 96       
    l1d_cache:u        | 12197282  | 12191064  | 12270250 
    l1d_cache_refill:u | 5891143   | 5882545   | 5887870  
    l1d_tlb:u          | 19485664  | 19559110  | 19619311 
    l1d_tlb_refill:u   | 5190650   | 5231656   | 5203411  
    l2d_cache:u        | 24105917  | 24619069  | 23221013 
    l2d_cache_refill:u | 9190345   | 9982022   | 8572823  
    l2d_tlb:u          | 5190982   | 5232304   | 5210871  
    l2d_tlb_refill:u   | 2668      | 2912      | 805      
    ll_cache:u         | 8965667   | 9569816   | 8499494  
    ll_cache_miss:u    | 76307     | 109894    | 26859    

== combo_078_s4 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p1_np8_l2_sl9        
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l2_sp3
    s2 | hot_b64_bp3_r100_rand_p16_np8_l2              
    s3 | itlb_f128_l1_r100_pstr_p16_np8_l4_sp17        
single_counts:
    metric             | s0       | s1       | s2       | s3      
    -------------------+----------+----------+----------+---------
    cpu-cycles:u       | 23315096 | 81156215 | 8789165  | 83824911
    instructions:u     | 26871049 | 18870988 | 11921049 | 26010997
    br_retired:u       | 1991410  | 1991403  | 2021410  | 1371404 
    br_mis_pred:u      | 290417   | 592049   | 496      | 458     
    l1i_cache:u        | 7146704  | 8591876  | 1566405  | 3576719 
    l1i_cache_refill:u | 825      | 663      | 640      | 3237012 
    l1i_tlb:u          | 7146704  | 8591876  | 1566405  | 3576719 
    l1i_tlb_refill:u   | 47       | 51       | 51       | 1310071 
    l2i_cache:u        | 824      | 663      | 638      | 3237012 
    l2i_cache_refill:u | 705      | 585      | 591      | 1267263 
    l2i_tlb:u          | 82       | 99       | 99       | 1310113 
    l2i_tlb_refill:u   | 14       | 43       | 29       | 30      
    l1d_cache:u        | 4255391  | 4702417  | 1415208  | 5255402 
    l1d_cache_refill:u | 166      | 1276710  | 504      | 90332   
    l1d_tlb:u          | 4257564  | 7963674  | 1417288  | 5257654 
    l1d_tlb_refill:u   | 66       | 1310061  | 95       | 238     
    l2d_cache:u        | 1728     | 5378986  | 2267     | 3466295 
    l2d_cache_refill:u | 1131     | 2599074  | 1157     | 1430460 
    l2d_tlb:u          | 90       | 1311554  | 142      | 258     
    l2d_tlb_refill:u   | 13       | 670      | 10       | 51      
    ll_cache:u         | 349      | 2598276  | 621      | 135469  
    ll_cache_miss:u    | 50       | 7931     | 89       | 213     
combined_orders:
    id        | modules                                                                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p1_np8_l2_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l2_sp3+hot_b64_bp3_r100_rand_p16_np8_l2+itlb_f128_l1_r100_pstr_p16_np8_l4_sp17
    shuffle   | itlb_f128_l1_r100_pstr_p16_np8_l4_sp17+hot_b64_bp3_r100_rand_p16_np8_l2+fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l2_sp3+cold_b128_d4_bitrev_lstr_p1_np8_l2_sl9
    sum       | cold_b128_d4_bitrev_lstr_p1_np8_l2_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p512_np4_l2_sp3+hot_b64_bp3_r100_rand_p16_np8_l2+itlb_f128_l1_r100_pstr_p16_np8_l4_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 226407239 | 244551274 | 197085387
    instructions:u     | 83641907  | 83641907  | 83674083 
    br_retired:u       | 7372006   | 7372006   | 7375627  
    br_mis_pred:u      | 881656    | 882238    | 883420   
    l1i_cache:u        | 21871141  | 21963625  | 20881704 
    l1i_cache_refill:u | 2987067   | 3069782   | 3239140  
    l1i_tlb:u          | 21871141  | 21963625  | 20881704 
    l1i_tlb_refill:u   | 1300949   | 1300949   | 1310220  
    l2i_cache:u        | 2987066   | 3069781   | 3239137  
    l2i_cache_refill:u | 739368    | 1114354   | 1269144  
    l2i_tlb:u          | 1301083   | 1301008   | 1310393  
    l2i_tlb_refill:u   | 167       | 436       | 116      
    l1d_cache:u        | 15560227  | 15560405  | 15628418 
    l1d_cache_refill:u | 1378951   | 1387615   | 1367712  
    l1d_tlb:u          | 18740531  | 18735186  | 18896180 
    l1d_tlb_refill:u   | 1307410   | 1306837   | 1310460  
    l2d_cache:u        | 9227030   | 8912652   | 8849276  
    l2d_cache_refill:u | 3869273   | 3946711   | 4031822  
    l2d_tlb:u          | 1307507   | 1306963   | 1312044  
    l2d_tlb_refill:u   | 963       | 1113      | 744      
    ll_cache:u         | 2963365   | 2846653   | 2734715  
    ll_cache_miss:u    | 60948     | 32085     | 8283     

== combo_079_s4 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b128_d4_bitrev_pstr_p512_np4_l2_sp17       
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np8_l4_sp17
    s2 | hot_b64_bp3_r100_pstr_p16_np1_l2_sp33           
    s3 | itlb_f64_l1_r100_lstr_p512_np2_l4_sl9           
single_counts:
    metric             | s0        | s1        | s2       | s3       
    -------------------+-----------+-----------+----------+----------
    cpu-cycles:u       | 147984302 | 298962116 | 7827479  | 181878294
    instructions:u     | 26870997  | 39991089  | 11921055 | 13210997 
    br_retired:u       | 1991404   | 3911412   | 2021408  | 731404   
    br_mis_pred:u      | 290501    | 1232734   | 436      | 468      
    l1i_cache:u        | 7827023   | 17497938  | 1565935  | 1877715  
    l1i_cache_refill:u | 1036      | 1534      | 642      | 1161539  
    l1i_tlb:u          | 7827023   | 17497938  | 1565935  | 1877715  
    l1i_tlb_refill:u   | 48        | 48        | 54       | 670073   
    l2i_cache:u        | 1034      | 1534      | 641      | 1161538  
    l2i_cache_refill:u | 763       | 1040      | 569      | 545025   
    l2i_tlb:u          | 90        | 101       | 98       | 670128   
    l2i_tlb_refill:u   | 26        | 28        | 28       | 50       
    l1d_cache:u        | 4262852   | 11782614  | 1415266  | 2695622  
    l1d_cache_refill:u | 2524507   | 5048249   | 164      | 2559833  
    l1d_tlb:u          | 7016544   | 20921602  | 1417375  | 5422113  
    l1d_tlb_refill:u   | 2600087   | 5162091   | 73       | 2600065  
    l2d_cache:u        | 11208557  | 22428660  | 1304     | 11184842 
    l2d_cache_refill:u | 5398775   | 10636041  | 847      | 5668384  
    l2d_tlb:u          | 2600886   | 5174543   | 104      | 2600110  
    l2d_tlb_refill:u   | 108       | 102       | 48       | 128      
    ll_cache:u         | 5397773   | 10634747  | 273      | 5125387  
    ll_cache_miss:u    | 47354     | 40872     | 65       | 950      
combined_orders:
    id        | modules                                                                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_pstr_p512_np4_l2_sp17+fetch_b128_d1_bp0_s16_r100_pstr_p512_np8_l4_sp17+hot_b64_bp3_r100_pstr_p16_np1_l2_sp33+itlb_f64_l1_r100_lstr_p512_np2_l4_sl9
    shuffle   | fetch_b128_d1_bp0_s16_r100_pstr_p512_np8_l4_sp17+itlb_f64_l1_r100_lstr_p512_np2_l4_sl9+cold_b128_d4_bitrev_pstr_p512_np4_l2_sp17+hot_b64_bp3_r100_pstr_p16_np1_l2_sp33
    sum       | cold_b128_d4_bitrev_pstr_p512_np4_l2_sp17+fetch_b128_d1_bp0_s16_r100_pstr_p512_np8_l4_sp17+hot_b64_bp3_r100_pstr_p16_np1_l2_sp33+itlb_f64_l1_r100_lstr_p512_np2_l4_sl9
combined_counts:
    metric             | canonical | shuffle    | sum      
    -------------------+-----------+------------+----------
    cpu-cycles:u       | 870305956 | 1112679280 | 636652191
    instructions:u     | 91961857  | 91961851   | 91994138 
    br_retired:u       | 8651991   | 8651993    | 8655628  
    br_mis_pred:u      | 1537671   | 1542889    | 1524139  
    l1i_cache:u        | 30612851  | 30777604   | 28768611 
    l1i_cache_refill:u | 998341    | 1016564    | 1164751  
    l1i_tlb:u          | 30612851  | 30777604   | 28768611 
    l1i_tlb_refill:u   | 661208    | 661235     | 670223   
    l2i_cache:u        | 998339    | 1016564    | 1164747  
    l2i_cache_refill:u | 450630    | 581437     | 547397   
    l2i_tlb:u          | 661835    | 661618     | 670417   
    l2i_tlb_refill:u   | 9116      | 8959       | 132      
    l1d_cache:u        | 20153731  | 20163960   | 20156354 
    l1d_cache_refill:u | 10142228  | 10145104   | 10132753 
    l1d_tlb:u          | 34840764  | 34850149   | 34777634 
    l1d_tlb_refill:u   | 10332899  | 10330937   | 10362316 
    l2d_cache:u        | 45229215  | 45508660   | 44823363 
    l2d_cache_refill:u | 21971202  | 21990044   | 21704047 
    l2d_tlb:u          | 10342143  | 10340056   | 10375643 
    l2d_tlb_refill:u   | 139779    | 140530     | 386      
    ll_cache:u         | 21459117  | 21411353   | 21158180 
    ll_cache_miss:u    | 153921    | 343997     | 89241    

== combo_080_s4 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b64_d4_bitrev_lin_p128_np8_l4      
    s1 | fetch_b64_d1_bp0_s16_r100_lin_p16_np2_l4
    s2 | hot_b64_bp3_r100_lstr_p16_np4_l2_sl5    
    s3 | itlb_f128_l1_r100_pstr_p512_np2_l1_sp17 
single_counts:
    metric             | s0       | s1       | s2       | s3       
    -------------------+----------+----------+----------+----------
    cpu-cycles:u       | 45434675 | 28912392 | 7836024  | 186263940
    instructions:u     | 14870997 | 20150988 | 11921049 | 22170997 
    br_retired:u       | 1031404  | 1991403  | 2021410  | 1371404  
    br_mis_pred:u      | 130712   | 591627   | 437      | 472      
    l1i_cache:u        | 3977939  | 8683243  | 1566024  | 3072418  
    l1i_cache_refill:u | 928      | 682      | 639      | 2799932  
    l1i_tlb:u          | 3977939  | 8683243  | 1566024  | 3072418  
    l1i_tlb_refill:u   | 62       | 47       | 46       | 1300045  
    l2i_cache:u        | 929      | 683      | 639      | 2799928  
    l2i_cache_refill:u | 718      | 591      | 568      | 1137403  
    l2i_tlb:u          | 115      | 79       | 81       | 1300091  
    l2i_tlb_refill:u   | 43       | 16       | 15       | 78       
    l1d_cache:u        | 3455773  | 5922424  | 1415150  | 1415681  
    l1d_cache_refill:u | 614147   | 48007    | 642      | 1279912  
    l1d_tlb:u          | 3929566  | 7672226  | 1417093  | 2799914  
    l1d_tlb_refill:u   | 340058   | 128      | 91       | 1304481  
    l2d_cache:u        | 6512038  | 109574   | 2112     | 7701704  
    l2d_cache_refill:u | 796868   | 1087     | 716      | 3609069  
    l2d_tlb:u          | 340114   | 162      | 109      | 1304517  
    l2d_tlb_refill:u   | 119      | 45       | 5        | 129      
    ll_cache:u         | 796050   | 409      | 246      | 2565105  
    ll_cache_miss:u    | 43540    | 96       | 86       | 2483     
combined_orders:
    id        | modules                                                                                                                                                 
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lin_p128_np8_l4+fetch_b64_d1_bp0_s16_r100_lin_p16_np2_l4+hot_b64_bp3_r100_lstr_p16_np4_l2_sl5+itlb_f128_l1_r100_pstr_p512_np2_l1_sp17
    shuffle   | hot_b64_bp3_r100_lstr_p16_np4_l2_sl5+cold_b64_d4_bitrev_lin_p128_np8_l4+fetch_b64_d1_bp0_s16_r100_lin_p16_np2_l4+itlb_f128_l1_r100_pstr_p512_np2_l1_sp17
    sum       | cold_b64_d4_bitrev_lin_p128_np8_l4+fetch_b64_d1_bp0_s16_r100_lin_p16_np2_l4+hot_b64_bp3_r100_lstr_p16_np4_l2_sl5+itlb_f128_l1_r100_pstr_p512_np2_l1_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 297142790 | 240684708 | 268447031
    instructions:u     | 69082004  | 69081913  | 69114031 
    br_retired:u       | 6412011   | 6412004   | 6415621  
    br_mis_pred:u      | 722185    | 721724    | 723248   
    l1i_cache:u        | 18126084  | 18155671  | 17299624 
    l1i_cache_refill:u | 3176849   | 3015618   | 2802181  
    l1i_tlb:u          | 18126084  | 18155671  | 17299624 
    l1i_tlb_refill:u   | 1300648   | 1300656   | 1300200  
    l2i_cache:u        | 3176844   | 3015613   | 2802179  
    l2i_cache_refill:u | 1599394   | 1495799   | 1139280  
    l2i_tlb:u          | 1300733   | 1300766   | 1300366  
    l2i_tlb_refill:u   | 905       | 846       | 152      
    l1d_cache:u        | 12179632  | 12179059  | 12209028 
    l1d_cache_refill:u | 2030760   | 2045616   | 1942708  
    l1d_tlb:u          | 15800461  | 15787691  | 15818799 
    l1d_tlb_refill:u   | 1648673   | 1647789   | 1644758  
    l2d_cache:u        | 16309255  | 16201411  | 14325428 
    l2d_cache_refill:u | 5677245   | 5438981   | 4407740  
    l2d_tlb:u          | 1648784   | 1647826   | 1644902  
    l2d_tlb_refill:u   | 903       | 1764      | 298      
    ll_cache:u         | 4139356   | 4032540   | 3361810  
    ll_cache_miss:u    | 78982     | 21668     | 46205    

== combo_081_s4 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p512_np2_l4_sl3     
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p1_np4_l4_sl9
    s2 | hot_b128_bp3_r100_lstr_p16_np8_l1_sl5        
    s3 | itlb_f128_l1_r100_pstr_p16_np4_l2_sp33       
single_counts:
    metric             | s0        | s1       | s2       | s3      
    -------------------+-----------+----------+----------+---------
    cpu-cycles:u       | 361914193 | 60307453 | 10408977 | 93703585
    instructions:u     | 29430957  | 39990997 | 22161055 | 23450997
    br_retired:u       | 1991391   | 3911404  | 3941408  | 1371404 
    br_mis_pred:u      | 290756    | 1230507  | 351      | 516     
    l1i_cache:u        | 8205942   | 19638253 | 2845112  | 3208757 
    l1i_cache_refill:u | 1427      | 921      | 671      | 3706626 
    l1i_tlb:u          | 8205942   | 19638253 | 2845112  | 3208757 
    l1i_tlb_refill:u   | 50        | 48       | 43       | 1310060 
    l2i_cache:u        | 1428      | 921      | 671      | 3706622 
    l2i_cache_refill:u | 841       | 660      | 579      | 1095913 
    l2i_tlb:u          | 86        | 91       | 82       | 1310104 
    l2i_tlb_refill:u   | 23        | 12       | 14       | 127     
    l1d_cache:u        | 6819204   | 11665540 | 1415243  | 2695317 
    l1d_cache_refill:u | 5049758   | 169      | 827      | 92259   
    l1d_tlb:u          | 12067759  | 15299290 | 1417289  | 2697447 
    l1d_tlb_refill:u   | 5143318   | 66       | 93       | 244     
    l2d_cache:u        | 22284889  | 1579     | 3034     | 3189558 
    l2d_cache_refill:u | 10867814  | 908      | 1203     | 931244  
    l2d_tlb:u          | 5143386   | 91       | 115      | 266     
    l2d_tlb_refill:u   | 105       | 7        | 8        | 17      
    ll_cache:u         | 10866522  | 228      | 582      | 126211  
    ll_cache_miss:u    | 449561    | 43       | 178      | 137     
combined_orders:
    id        | modules                                                                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p512_np2_l4_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p1_np4_l4_sl9+hot_b128_bp3_r100_lstr_p16_np8_l1_sl5+itlb_f128_l1_r100_pstr_p16_np4_l2_sp33
    shuffle   | fetch_b128_d1_bp0_s16_r100_lstr_p1_np4_l4_sl9+hot_b128_bp3_r100_lstr_p16_np8_l1_sl5+itlb_f128_l1_r100_pstr_p16_np4_l2_sp33+cold_b128_d4_bitrev_lstr_p512_np2_l4_sl3
    sum       | cold_b128_d4_bitrev_lstr_p512_np2_l4_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p1_np4_l4_sl9+hot_b128_bp3_r100_lstr_p16_np8_l1_sl5+itlb_f128_l1_r100_pstr_p16_np4_l2_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 531436908 | 522995859 | 526334208
    instructions:u     | 115001851 | 115001851 | 115034006
    br_retired:u       | 11211993  | 11211993  | 11215607 
    br_mis_pred:u      | 1522383   | 1525621   | 1522130  
    l1i_cache:u        | 33425869  | 33258544  | 33898064 
    l1i_cache_refill:u | 3070838   | 2918449   | 3709645  
    l1i_tlb:u          | 33425869  | 33258544  | 33898064 
    l1i_tlb_refill:u   | 1301250   | 1301259   | 1310201  
    l2i_cache:u        | 3070837   | 2918449   | 3709642  
    l2i_cache_refill:u | 1001712   | 815549    | 1097993  
    l2i_tlb:u          | 1301291   | 1301339   | 1310363  
    l2i_tlb_refill:u   | 172       | 280       | 176      
    l1d_cache:u        | 22575313  | 22585479  | 22595304 
    l1d_cache_refill:u | 5121001   | 5145061   | 5143013  
    l1d_tlb:u          | 31478805  | 31568433  | 31481785 
    l1d_tlb_refill:u   | 5145868   | 5163824   | 5143721  
    l2d_cache:u        | 25652524  | 25577168  | 25479060 
    l2d_cache_refill:u | 11688602  | 11725029  | 11801169 
    l2d_tlb:u          | 5146031   | 5173475   | 5143858  
    l2d_tlb_refill:u   | 951       | 979       | 137      
    ll_cache:u         | 10886869  | 10882252  | 10993543 
    ll_cache_miss:u    | 418571    | 359695    | 449919   

== combo_082_s4 ==
single_modules:
    id | module                                       
    ---+----------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p16_np1_l4_sl3      
    s1 | fetch_b64_d1_bp0_s16_r100_lstr_p16_np2_l1_sl9
    s2 | hot_b64_bp3_r100_lshuf_p1_np8_l2             
    s3 | itlb_f128_l1_r100_lstr_p128_np2_l2_sl9       
single_counts:
    metric             | s0       | s1       | s2       | s3       
    -------------------+----------+----------+----------+----------
    cpu-cycles:u       | 34173020 | 21242243 | 7793002  | 217555361
    instructions:u     | 29430997 | 18231040 | 11921040 | 23451007 
    br_retired:u       | 1991404  | 1991409  | 2021409  | 1371406  
    br_mis_pred:u      | 290631   | 590994   | 425      | 473      
    l1i_cache:u        | 8068213  | 8446377  | 1575952  | 3052092  
    l1i_cache_refill:u | 849      | 617      | 607      | 2783383  
    l1i_tlb:u          | 8068213  | 8446377  | 1575952  | 3052092  
    l1i_tlb_refill:u   | 51       | 45       | 43       | 1310059  
    l2i_cache:u        | 848      | 616      | 607      | 2783381  
    l2i_cache_refill:u | 743      | 569      | 503      | 1977548  
    l2i_tlb:u          | 86       | 74       | 79       | 1310100  
    l2i_tlb_refill:u   | 16       | 12       | 11       | 35       
    l1d_cache:u        | 6815549  | 4005418  | 1415282  | 2695762  
    l1d_cache_refill:u | 49512    | 42014    | 150      | 2469696  
    l1d_tlb:u          | 6817983  | 5758955  | 1417313  | 5346498  
    l1d_tlb_refill:u   | 133      | 110      | 62       | 2581247  
    l2d_cache:u        | 95784    | 231238   | 1264     | 11395591 
    l2d_cache_refill:u | 1177     | 935      | 894      | 5308259  
    l2d_tlb:u          | 163      | 139      | 83       | 2581275  
    l2d_tlb_refill:u   | 41       | 46       | 26       | 30       
    ll_cache:u         | 358      | 323      | 300      | 3292200  
    ll_cache_miss:u    | 27       | 10       | 22       | 746      
combined_orders:
    id        | modules                                                                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p16_np1_l4_sl3+fetch_b64_d1_bp0_s16_r100_lstr_p16_np2_l1_sl9+hot_b64_bp3_r100_lshuf_p1_np8_l2+itlb_f128_l1_r100_lstr_p128_np2_l2_sl9
    shuffle   | cold_b128_d4_bitrev_lstr_p16_np1_l4_sl3+hot_b64_bp3_r100_lshuf_p1_np8_l2+itlb_f128_l1_r100_lstr_p128_np2_l2_sl9+fetch_b64_d1_bp0_s16_r100_lstr_p16_np2_l1_sl9
    sum       | cold_b128_d4_bitrev_lstr_p16_np1_l4_sl3+fetch_b64_d1_bp0_s16_r100_lstr_p16_np2_l1_sl9+hot_b64_bp3_r100_lshuf_p1_np8_l2+itlb_f128_l1_r100_lstr_p128_np2_l2_sl9
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 275584597 | 279837769 | 280763626
    instructions:u     | 83001998  | 83001998  | 83034084 
    br_retired:u       | 7372013   | 7372013   | 7375628  
    br_mis_pred:u      | 881573    | 882497    | 882523   
    l1i_cache:u        | 21622007  | 21643365  | 21142634 
    l1i_cache_refill:u | 3197245   | 2912280   | 2785456  
    l1i_tlb:u          | 21622007  | 21643365  | 21142634 
    l1i_tlb_refill:u   | 1300857   | 1300848   | 1310198  
    l2i_cache:u        | 3197242   | 2912278   | 2785452  
    l2i_cache_refill:u | 2213758   | 2084220   | 1979363  
    l2i_tlb:u          | 1300905   | 1300930   | 1310339  
    l2i_tlb_refill:u   | 48        | 196       | 74       
    l1d_cache:u        | 14897422  | 14898036  | 14932011 
    l1d_cache_refill:u | 2523663   | 2554673   | 2561372  
    l1d_tlb:u          | 19313331  | 19319846  | 19340749 
    l1d_tlb_refill:u   | 2588687   | 2588735   | 2581552  
    l2d_cache:u        | 11992466  | 12006792  | 11723877 
    l2d_cache_refill:u | 5125146   | 5395387   | 5311265  
    l2d_tlb:u          | 2588714   | 2588880   | 2581660  
    l2d_tlb_refill:u   | 203       | 220       | 143      
    ll_cache:u         | 3086172   | 3264280   | 3293181  
    ll_cache_miss:u    | 188       | 290       | 805      

== combo_083_s4 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl9     
    s1 | fetch_b128_d1_bp0_s16_r100_rand_p16_np8_l1
    s2 | hot_b64_bp3_r100_pstr_p128_np8_l2_sp3     
    s3 | itlb_f64_l1_r100_lstr_p1_np8_l1_sl3       
single_counts:
    metric             | s0       | s1       | s2       | s3      
    -------------------+----------+----------+----------+---------
    cpu-cycles:u       | 16408890 | 46080240 | 38590041 | 21457737
    instructions:u     | 14871040 | 36150988 | 11920997 | 11291040
    br_retired:u       | 1031409  | 3911403  | 2021404  | 731409  
    br_mis_pred:u      | 130595   | 1231043  | 435      | 460     
    l1i_cache:u        | 3727734  | 16812035 | 1568771  | 1486802 
    l1i_cache_refill:u | 688      | 808      | 656      | 1685359 
    l1i_tlb:u          | 3727734  | 16812035 | 1568771  | 1486802 
    l1i_tlb_refill:u   | 48       | 46       | 53       | 660131  
    l2i_cache:u        | 688      | 805      | 656      | 1685357 
    l2i_cache_refill:u | 615      | 682      | 552      | 850     
    l2i_tlb:u          | 81       | 83       | 163      | 660226  
    l2i_tlb_refill:u   | 15       | 16       | 24       | 26      
    l1d_cache:u        | 3455371  | 7950386  | 1416114  | 775163  
    l1d_cache_refill:u | 151      | 373795   | 1176817  | 10139   
    l1d_tlb:u          | 3457514  | 11572587 | 2780270  | 776818  
    l1d_tlb_refill:u   | 61       | 170      | 1300092  | 60      
    l2d_cache:u        | 1403     | 1704213  | 4143242  | 1807573 
    l2d_cache_refill:u | 976      | 1352     | 904377   | 21165   
    l2d_tlb:u          | 82       | 196      | 1300844  | 79      
    l2d_tlb_refill:u   | 25       | 8        | 15       | 8       
    ll_cache:u         | 306      | 661      | 903758   | 10325   
    ll_cache_miss:u    | 19       | 24       | 2586     | 27      
combined_orders:
    id        | modules                                                                                                                                                   
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl9+fetch_b128_d1_bp0_s16_r100_rand_p16_np8_l1+hot_b64_bp3_r100_pstr_p128_np8_l2_sp3+itlb_f64_l1_r100_lstr_p1_np8_l1_sl3
    shuffle   | hot_b64_bp3_r100_pstr_p128_np8_l2_sp3+cold_b64_d4_bitrev_lstr_p1_np2_l4_sl9+fetch_b128_d1_bp0_s16_r100_rand_p16_np8_l1+itlb_f64_l1_r100_lstr_p1_np8_l1_sl3
    sum       | cold_b64_d4_bitrev_lstr_p1_np2_l4_sl9+fetch_b128_d1_bp0_s16_r100_rand_p16_np8_l1+hot_b64_bp3_r100_pstr_p128_np8_l2_sp3+itlb_f64_l1_r100_lstr_p1_np8_l1_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 133130305 | 126172410 | 122536908
    instructions:u     | 74201888  | 74201888  | 74234065 
    br_retired:u       | 7692003   | 7692003   | 7695625  
    br_mis_pred:u      | 1362200   | 1361499   | 1362533  
    l1i_cache:u        | 26094285  | 25997804  | 23595342 
    l1i_cache_refill:u | 1135847   | 1187953   | 1687511  
    l1i_tlb:u          | 26094285  | 25997804  | 23595342 
    l1i_tlb_refill:u   | 660852    | 660915    | 660278   
    l2i_cache:u        | 1135847   | 1187950   | 1687506  
    l2i_cache_refill:u | 103653    | 13313     | 2699     
    l2i_tlb:u          | 660896    | 661023    | 660553   
    l2i_tlb_refill:u   | 29        | 33        | 81       
    l1d_cache:u        | 13470125  | 13466499  | 13597034 
    l1d_cache_refill:u | 1561544   | 1624869   | 1560902  
    l1d_tlb:u          | 18501676  | 18488423  | 18587189 
    l1d_tlb_refill:u   | 1307934   | 1305801   | 1300383  
    l2d_cache:u        | 8145164   | 7351224   | 7656431  
    l2d_cache_refill:u | 1336183   | 1284714   | 927870   
    l2d_tlb:u          | 1308307   | 1306240   | 1301201  
    l2d_tlb_refill:u   | 174       | 23        | 56       
    ll_cache:u         | 1236307   | 1269986   | 915050   
    ll_cache_miss:u    | 1981      | 427       | 2656     

== combo_084_s4 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p128_np8_l2         
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l2_sp3
    s2 | hot_b64_bp3_r100_rand_p512_np1_l4             
    s3 | itlb_f128_l1_r100_pstr_p512_np1_l2_sp3        
single_counts:
    metric             | s0       | s1       | s2        | s3       
    -------------------+----------+----------+-----------+----------
    cpu-cycles:u       | 57431613 | 53450387 | 140802518 | 265679280
    instructions:u     | 26870997 | 18870988 | 13200997  | 23451098 
    br_retired:u       | 1991404  | 1991403  | 2021404   | 1371413  
    br_mis_pred:u      | 290751   | 591623   | 452       | 484      
    l1i_cache:u        | 7779332  | 8669955  | 1749847   | 3007774  
    l1i_cache_refill:u | 904      | 638      | 920       | 2953277  
    l1i_tlb:u          | 7779332  | 8669955  | 1749847   | 3007774  
    l1i_tlb_refill:u   | 55       | 43       | 54        | 1310053  
    l2i_cache:u        | 903      | 637      | 919       | 2953274  
    l2i_cache_refill:u | 812      | 558      | 642       | 2165006  
    l2i_tlb:u          | 109      | 81       | 156       | 1310105  
    l2i_tlb_refill:u   | 37       | 16       | 47        | 103      
    l1d_cache:u        | 4256491  | 4695782  | 2697397   | 2696649  
    l1d_cache_refill:u | 1507049  | 1203376  | 2560068   | 2574813  
    l1d_tlb:u          | 4838431  | 7890839  | 5375256   | 5417556  
    l1d_tlb_refill:u   | 350064   | 1303049  | 2586796   | 2600157  
    l2d_cache:u        | 7998955  | 3997678  | 10112576  | 12924562 
    l2d_cache_refill:u | 1259489  | 906583   | 5123497   | 7247388  
    l2d_tlb:u          | 350218   | 1303529  | 2587212   | 2600185  
    l2d_tlb_refill:u   | 168      | 133      | 607       | 149      
    ll_cache:u         | 1258450  | 905876   | 5122642   | 5138992  
    ll_cache_miss:u    | 13599    | 551      | 70        | 171      
combined_orders:
    id        | modules                                                                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p128_np8_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l2_sp3+hot_b64_bp3_r100_rand_p512_np1_l4+itlb_f128_l1_r100_pstr_p512_np1_l2_sp3
    shuffle   | itlb_f128_l1_r100_pstr_p512_np1_l2_sp3+cold_b128_d4_bitrev_lshuf_p128_np8_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l2_sp3+hot_b64_bp3_r100_rand_p512_np1_l4
    sum       | cold_b128_d4_bitrev_lshuf_p128_np8_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l2_sp3+hot_b64_bp3_r100_rand_p512_np1_l4+itlb_f128_l1_r100_pstr_p512_np1_l2_sp3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 607969245 | 640707153 | 517363798
    instructions:u     | 82361851  | 82361851  | 82394080 
    br_retired:u       | 7371993   | 7371993   | 7375624  
    br_mis_pred:u      | 882875    | 881836    | 883310   
    l1i_cache:u        | 21605863  | 21680326  | 21206908 
    l1i_cache_refill:u | 3015364   | 3051358   | 2955739  
    l1i_tlb:u          | 21605863  | 21680326  | 21206908 
    l1i_tlb_refill:u   | 1300843   | 1300848   | 1310205  
    l2i_cache:u        | 3015362   | 3051355   | 2955733  
    l2i_cache_refill:u | 2194795   | 2228497   | 2167018  
    l2i_tlb:u          | 1301087   | 1301192   | 1310451  
    l2i_tlb_refill:u   | 13437     | 13290     | 203      
    l1d_cache:u        | 14280191  | 14280935  | 14346319 
    l1d_cache_refill:u | 8005053   | 8046410   | 7845306  
    l1d_tlb:u          | 23394945  | 23479026  | 23522082 
    l1d_tlb_refill:u   | 6815622   | 6865711   | 6840066  
    l2d_cache:u        | 37280369  | 36901647  | 35033771 
    l2d_cache_refill:u | 15602334  | 15543680  | 14536957 
    l2d_tlb:u          | 6820435   | 6879656   | 6841144  
    l2d_tlb_refill:u   | 118754    | 94245     | 1057     
    ll_cache:u         | 13348098  | 13371098  | 12425960 
    ll_cache_miss:u    | 163403    | 114339    | 14391    

== combo_085_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl3          
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p128_np1_l4_sl3
    s2 | hot_b64_bp3_r100_lstr_p16_np4_l4_sl5           
    s3 | itlb_f64_l1_r100_lshuf_p128_np8_l4             
single_counts:
    metric             | s0       | s1        | s2       | s3      
    -------------------+----------+-----------+----------+---------
    cpu-cycles:u       | 8725238  | 203049616 | 12928619 | 74934493
    instructions:u     | 12951040 | 39990988  | 13201049 | 13210997
    br_retired:u       | 1031409  | 3911403   | 2021410  | 731404  
    br_mis_pred:u      | 130590   | 1250693   | 406      | 491     
    l1i_cache:u        | 3487399  | 17673789  | 1726078  | 1764532 
    l1i_cache_refill:u | 660      | 1280      | 625      | 1146114 
    l1i_tlb:u          | 3487399  | 17673789  | 1726078  | 1764532 
    l1i_tlb_refill:u   | 46       | 47        | 44       | 670055  
    l2i_cache:u        | 659      | 1278      | 625      | 1146113 
    l2i_cache_refill:u | 563      | 768       | 546      | 142910  
    l2i_tlb:u          | 85       | 90        | 73       | 670098  
    l2i_tlb_refill:u   | 11       | 13        | 14       | 25      
    l1d_cache:u        | 1535353  | 11752047  | 2695394  | 2695448 
    l1d_cache_refill:u | 166      | 4816334   | 321      | 1472807 
    l1d_tlb:u          | 1537510  | 20976980  | 2697525  | 3194107 
    l1d_tlb_refill:u   | 67       | 5160058   | 113      | 340062  
    l2d_cache:u        | 1421     | 15157608  | 1925     | 8656343 
    l2d_cache_refill:u | 979      | 4145666   | 1126     | 1466287 
    l2d_tlb:u          | 93       | 5160130   | 136      | 340116  
    l2d_tlb_refill:u   | 35       | 164       | 41       | 151     
    ll_cache:u         | 294      | 4144664   | 496      | 1304851 
    ll_cache_miss:u    | 34       | 2461      | 61       | 307     
combined_orders:
    id        | modules                                                                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p128_np1_l4_sl3+hot_b64_bp3_r100_lstr_p16_np4_l4_sl5+itlb_f64_l1_r100_lshuf_p128_np8_l4
    shuffle   | itlb_f64_l1_r100_lshuf_p128_np8_l4+cold_b64_d4_bitrev_lstr_p1_np2_l1_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p128_np1_l4_sl3+hot_b64_bp3_r100_lstr_p16_np4_l4_sl5
    sum       | cold_b64_d4_bitrev_lstr_p1_np2_l1_sl3+fetch_b128_d1_bp0_s16_r100_lstr_p128_np1_l4_sl3+hot_b64_bp3_r100_lstr_p16_np4_l4_sl5+itlb_f64_l1_r100_lshuf_p128_np8_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 288828222 | 290437113 | 299637966
    instructions:u     | 79321989  | 79321989  | 79354074 
    br_retired:u       | 7692012   | 7692012   | 7695626  
    br_mis_pred:u      | 1363410   | 1361971   | 1382180  
    l1i_cache:u        | 26781107  | 26709546  | 24651798 
    l1i_cache_refill:u | 916673    | 996795    | 1148679  
    l1i_tlb:u          | 26781107  | 26709546  | 24651798 
    l1i_tlb_refill:u   | 670874    | 670938    | 670192   
    l2i_cache:u        | 916670    | 996794    | 1148675  
    l2i_cache_refill:u | 61077     | 57019     | 144787   
    l2i_tlb:u          | 670961    | 671058    | 670346   
    l2i_tlb_refill:u   | 123       | 54        | 63       
    l1d_cache:u        | 18629602  | 18621181  | 18678242 
    l1d_cache_refill:u | 6505363   | 6543060   | 6289628  
    l1d_tlb:u          | 28104325  | 28238128  | 28406122 
    l1d_tlb_refill:u   | 5501924   | 5530508   | 5500300  
    l2d_cache:u        | 25192944  | 25003567  | 23817297 
    l2d_cache_refill:u | 6457973   | 6445079   | 5614058  
    l2d_tlb:u          | 5512643   | 5539181   | 5500475  
    l2d_tlb_refill:u   | 336       | 317       | 391      
    ll_cache:u         | 6398639   | 6381743   | 5450305  
    ll_cache_miss:u    | 18334     | 30951     | 2863     

== combo_086_s4 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p16_np8_l1_sl5   
    s1 | fetch_b128_d1_bp0_s16_r100_lin_p128_np8_l2
    s2 | hot_b64_bp3_r100_pstr_p16_np8_l4_sp3      
    s3 | itlb_f128_l1_r100_rand_p1_np4_l2          
single_counts:
    metric             | s0       | s1       | s2       | s3      
    -------------------+----------+----------+----------+---------
    cpu-cycles:u       | 20125742 | 67400599 | 12959040 | 61029587
    instructions:u     | 25591049 | 37430988 | 13201049 | 23450988
    br_retired:u       | 1991410  | 3911403  | 2021410  | 1371403 
    br_mis_pred:u      | 290405   | 1233450  | 418      | 490     
    l1i_cache:u        | 7626263  | 17084004 | 1726133  | 3231810 
    l1i_cache_refill:u | 796      | 940      | 633      | 2789013 
    l1i_tlb:u          | 7626263  | 17084004 | 1726133  | 3231810 
    l1i_tlb_refill:u   | 48       | 55       | 55       | 1310077 
    l2i_cache:u        | 796      | 939      | 632      | 2789007 
    l2i_cache_refill:u | 666      | 809      | 554      | 508274  
    l2i_tlb:u          | 80       | 108      | 104      | 1310150 
    l2i_tlb_refill:u   | 13       | 46       | 14       | 28      
    l1d_cache:u        | 2975447  | 9186696  | 2695159  | 2695262 
    l1d_cache_refill:u | 196779   | 656390   | 884      | 10144   
    l1d_tlb:u          | 2977857  | 13334798 | 2697111  | 2697068 
    l1d_tlb_refill:u   | 118      | 350066   | 92       | 58      
    l2d_cache:u        | 440220   | 6228098  | 2661     | 3290637 
    l2d_cache_refill:u | 1493     | 731522   | 799      | 840475  
    l2d_tlb:u          | 145      | 358212   | 118      | 81      
    l2d_tlb_refill:u   | 52       | 125      | 46       | 8       
    ll_cache:u         | 699      | 730606   | 322      | 10323   
    ll_cache_miss:u    | 104      | 1232     | 105      | 40      
combined_orders:
    id        | modules                                                                                                                                                 
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p16_np8_l1_sl5+fetch_b128_d1_bp0_s16_r100_lin_p128_np8_l2+hot_b64_bp3_r100_pstr_p16_np8_l4_sp3+itlb_f128_l1_r100_rand_p1_np4_l2
    shuffle   | fetch_b128_d1_bp0_s16_r100_lin_p128_np8_l2+hot_b64_bp3_r100_pstr_p16_np8_l4_sp3+itlb_f128_l1_r100_rand_p1_np4_l2+cold_b128_d4_bitrev_lstr_p16_np8_l1_sl5
    sum       | cold_b128_d4_bitrev_lstr_p16_np8_l1_sl5+fetch_b128_d1_bp0_s16_r100_lin_p128_np8_l2+hot_b64_bp3_r100_pstr_p16_np8_l4_sp3+itlb_f128_l1_r100_rand_p1_np4_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 183260237 | 211438781 | 161514968
    instructions:u     | 99641897  | 99641913  | 99674074 
    br_retired:u       | 9292004   | 9292004   | 9295626  
    br_mis_pred:u      | 1522508   | 1522284   | 1524763  
    l1i_cache:u        | 31473997  | 31405685  | 29668210 
    l1i_cache_refill:u | 3016247   | 3042754   | 2791382  
    l1i_tlb:u          | 31473997  | 31405685  | 29668210 
    l1i_tlb_refill:u   | 1301060   | 1301056   | 1310235  
    l2i_cache:u        | 3016248   | 3042755   | 2791374  
    l2i_cache_refill:u | 1331019   | 802799    | 510303   
    l2i_tlb:u          | 1301127   | 1301141   | 1310442  
    l2i_tlb_refill:u   | 194       | 192       | 101      
    l1d_cache:u        | 17498160  | 17504892  | 17552564 
    l1d_cache_refill:u | 835539    | 907586    | 864197   
    l1d_tlb:u          | 21692905  | 21730294  | 21706834 
    l1d_tlb_refill:u   | 363730    | 353616    | 350334   
    l2d_cache:u        | 12562384  | 13392742  | 9961616  
    l2d_cache_refill:u | 2512028   | 1982575   | 1574289  
    l2d_tlb:u          | 372581    | 363642    | 358556   
    l2d_tlb_refill:u   | 207       | 168       | 231      
    ll_cache:u         | 1172629   | 1224043   | 741950   
    ll_cache_miss:u    | 15005     | 33617     | 1481     

== combo_087_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p16_np1_l1_sl3        
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17
    s2 | hot_b128_bp3_r100_pstr_p512_np4_l4_sp3         
    s3 | itlb_f64_l1_r100_pstr_p128_np1_l1_sp33         
single_counts:
    metric             | s0       | s1        | s2        | s3      
    -------------------+----------+-----------+-----------+---------
    cpu-cycles:u       | 18754194 | 140642880 | 305374863 | 71273448
    instructions:u     | 25591049 | 20150988  | 26001098  | 11290997
    br_retired:u       | 1991410  | 1991403   | 3941413   | 731404  
    br_mis_pred:u      | 290618   | 594007    | 501       | 456     
    l1i_cache:u        | 7587676  | 8828922   | 3354124   | 1604424 
    l1i_cache_refill:u | 823      | 832       | 1892      | 967887  
    l1i_tlb:u          | 7587676  | 8828922   | 3354124   | 1604424 
    l1i_tlb_refill:u   | 50       | 53        | 68        | 660071  
    l2i_cache:u        | 821      | 829       | 1891      | 967886  
    l2i_cache_refill:u | 680      | 689       | 946       | 422979  
    l2i_tlb:u          | 91       | 119       | 133       | 660118  
    l2i_tlb_refill:u   | 14       | 46        | 51        | 23      
    l1d_cache:u        | 2975437  | 5966547   | 5259111   | 775567  
    l1d_cache_refill:u | 185      | 2532079   | 5119927   | 623730  
    l1d_tlb:u          | 2977783  | 10581857  | 10485043  | 1520778 
    l1d_tlb_refill:u   | 112      | 2600978   | 5144020   | 664561  
    l2d_cache:u        | 1697     | 11141571  | 20259212  | 3416086 
    l2d_cache_refill:u | 1187     | 5343111   | 10241998  | 1277618 
    l2d_tlb:u          | 137      | 2616543   | 5144961   | 664596  
    l2d_tlb_refill:u   | 49       | 557       | 82        | 154     
    ll_cache:u         | 390      | 5342271   | 10241148  | 928130  
    ll_cache_miss:u    | 29       | 51354     | 588       | 23      
combined_orders:
    id        | modules                                                                                                                                                              
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p16_np1_l1_sl3+fetch_b64_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17+hot_b128_bp3_r100_pstr_p512_np4_l4_sp3+itlb_f64_l1_r100_pstr_p128_np1_l1_sp33
    shuffle   | hot_b128_bp3_r100_pstr_p512_np4_l4_sp3+itlb_f64_l1_r100_pstr_p128_np1_l1_sp33+fetch_b64_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17+cold_b128_d4_bitrev_lstr_p16_np1_l1_sl3
    sum       | cold_b128_d4_bitrev_lstr_p16_np1_l1_sl3+fetch_b64_d1_bp0_s16_r100_pstr_p512_np2_l4_sp17+hot_b128_bp3_r100_pstr_p512_np4_l4_sp3+itlb_f64_l1_r100_pstr_p128_np1_l1_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 570628850 | 586656462 | 536045385
    instructions:u     | 83001851  | 83001857  | 83034132 
    br_retired:u       | 8651993   | 8651991   | 8655630  
    br_mis_pred:u      | 883588    | 888698    | 885582   
    l1i_cache:u        | 21811956  | 21817911  | 21375146 
    l1i_cache_refill:u | 1050240   | 1064952   | 971434   
    l1i_tlb:u          | 21811956  | 21817911  | 21375146 
    l1i_tlb_refill:u   | 660988    | 660989    | 660242   
    l2i_cache:u        | 1050240   | 1064954   | 971427   
    l2i_cache_refill:u | 356721    | 154048    | 425294   
    l2i_tlb:u          | 661218    | 661218    | 660461   
    l2i_tlb_refill:u   | 4767      | 5835      | 134      
    l1d_cache:u        | 14939788  | 14952644  | 14976662 
    l1d_cache_refill:u | 8282029   | 8319043   | 8275921  
    l1d_tlb:u          | 25468498  | 25604329  | 25565461 
    l1d_tlb_refill:u   | 8400110   | 8412658   | 8409671  
    l2d_cache:u        | 35300421  | 35295531  | 34818566 
    l2d_cache_refill:u | 16963267  | 17114772  | 16863914 
    l2d_tlb:u          | 8401150   | 8430609   | 8426237  
    l2d_tlb_refill:u   | 56546     | 57518     | 842      
    ll_cache:u         | 16737631  | 16921453  | 16511939 
    ll_cache_miss:u    | 84846     | 80910     | 51994    

== combo_088_s4 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p512_np4_l4_sp17      
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p16_np2_l4_sl5
    s2 | hot_b128_bp3_r100_lstr_p16_np8_l4_sl5         
    s3 | itlb_f64_l1_r100_lshuf_p1_np2_l2              
single_counts:
    metric             | s0        | s1       | s2       | s3      
    -------------------+-----------+----------+----------+---------
    cpu-cycles:u       | 138469718 | 59562307 | 25742739 | 22628968
    instructions:u     | 14870997  | 39990988 | 26001049 | 11931055
    br_retired:u       | 1031404   | 3911403  | 3941410  | 731408  
    br_mis_pred:u      | 130818    | 1231087  | 587      | 422     
    l1i_cache:u        | 3944836   | 17232563 | 3328006  | 1569507 
    l1i_cache_refill:u | 739       | 871      | 807      | 1274001 
    l1i_tlb:u          | 3944836   | 17232563 | 3328006  | 1569507 
    l1i_tlb_refill:u   | 45        | 48       | 46       | 660136  
    l2i_cache:u        | 738       | 871      | 806      | 1274000 
    l2i_cache_refill:u | 646       | 698      | 630      | 748     
    l2i_tlb:u          | 82        | 86       | 101      | 660234  
    l2i_tlb_refill:u   | 27        | 13       | 17       | 105     
    l1d_cache:u        | 3462099   | 11685476 | 5255628  | 1415259 
    l1d_cache_refill:u | 2522948   | 70893    | 522      | 163     
    l1d_tlb:u          | 6155643   | 15340681 | 5258160  | 1417087 
    l1d_tlb_refill:u   | 2584960   | 190      | 131      | 64      
    l2d_cache:u        | 11125975  | 113974   | 2860     | 1103438 
    l2d_cache_refill:u | 5445895   | 1204     | 1457     | 1186    
    l2d_tlb:u          | 2585046   | 218      | 152      | 83      
    l2d_tlb_refill:u   | 547       | 49       | 44       | 25      
    ll_cache:u         | 5444988   | 420      | 742      | 274     
    ll_cache_miss:u    | 71537     | 51       | 73       | 16      
combined_orders:
    id        | modules                                                                                                                                                       
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p512_np4_l4_sp17+fetch_b128_d1_bp0_s16_r100_lstr_p16_np2_l4_sl5+hot_b128_bp3_r100_lstr_p16_np8_l4_sl5+itlb_f64_l1_r100_lshuf_p1_np2_l2
    shuffle   | cold_b64_d4_bitrev_pstr_p512_np4_l4_sp17+fetch_b128_d1_bp0_s16_r100_lstr_p16_np2_l4_sl5+itlb_f64_l1_r100_lshuf_p1_np2_l2+hot_b128_bp3_r100_lstr_p16_np8_l4_sl5
    sum       | cold_b64_d4_bitrev_pstr_p512_np4_l4_sp17+fetch_b128_d1_bp0_s16_r100_lstr_p16_np2_l4_sl5+hot_b128_bp3_r100_lstr_p16_np8_l4_sl5+itlb_f64_l1_r100_lshuf_p1_np2_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 242605438 | 304004171 | 246403732
    instructions:u     | 92761898  | 92761989  | 92794089 
    br_retired:u       | 9612005   | 9612012   | 9615625  
    br_mis_pred:u      | 1362190   | 1363091   | 1362914  
    l1i_cache:u        | 28255080  | 28297120  | 26074912 
    l1i_cache_refill:u | 1130043   | 1036976   | 1276418  
    l1i_tlb:u          | 28255080  | 28297120  | 26074912 
    l1i_tlb_refill:u   | 670976    | 670983    | 660275   
    l2i_cache:u        | 1130043   | 1036975   | 1276415  
    l2i_cache_refill:u | 16362     | 16082     | 2722     
    l2i_tlb:u          | 671128    | 671175    | 660503   
    l2i_tlb_refill:u   | 136       | 224       | 162      
    l1d_cache:u        | 21772730  | 21781809  | 21818462 
    l1d_cache_refill:u | 2676752   | 2672900   | 2594526  
    l1d_tlb:u          | 28113161  | 28115017  | 28171571 
    l1d_tlb_refill:u   | 2587765   | 2588929   | 2585345  
    l2d_cache:u        | 12653851  | 12499168  | 12346247 
    l2d_cache_refill:u | 5416514   | 5402899   | 5449742  
    l2d_tlb:u          | 2587942   | 2589114   | 2585499  
    l2d_tlb_refill:u   | 644       | 1398      | 665      
    ll_cache:u         | 5400778   | 5387535   | 5446424  
    ll_cache_miss:u    | 22182     | 17168     | 71677    

== combo_089_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p512_np4_l2          
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l4_sp17
    s2 | hot_b128_bp3_r100_rand_p16_np2_l4              
    s3 | itlb_f128_l1_r100_pstr_p512_np1_l2_sp33        
single_counts:
    metric             | s0        | s1       | s2       | s3       
    -------------------+-----------+----------+----------+----------
    cpu-cycles:u       | 156652242 | 99346332 | 25753439 | 295731877
    instructions:u     | 26871024  | 20150988 | 26001049 | 23451098 
    br_retired:u       | 1991408   | 1991403  | 3941410  | 1371413  
    br_mis_pred:u      | 290693    | 596524   | 454      | 492      
    l1i_cache:u        | 7793775   | 8852624  | 3327007  | 3001804  
    l1i_cache_refill:u | 1054      | 785      | 808      | 3334169  
    l1i_tlb:u          | 7793775   | 8852624  | 3327007  | 3001804  
    l1i_tlb_refill:u   | 48        | 44       | 49       | 1310048  
    l2i_cache:u        | 1053      | 784      | 807      | 3334167  
    l2i_cache_refill:u | 770       | 614      | 665      | 2366280  
    l2i_tlb:u          | 82        | 76       | 81       | 1310088  
    l2i_tlb_refill:u   | 22        | 15       | 14       | 86       
    l1d_cache:u        | 4256827   | 5996331  | 5255432  | 2696088  
    l1d_cache_refill:u | 1806117   | 2410891  | 221      | 2554207  
    l1d_tlb:u          | 5158740   | 10553136 | 5257614  | 5367006  
    l1d_tlb_refill:u   | 660066    | 2585093  | 110      | 2585315  
    l2d_cache:u        | 11036747  | 8144098  | 1650     | 13123809 
    l2d_cache_refill:u | 4926474   | 2343785  | 1005     | 7281537  
    l2d_tlb:u          | 660207    | 2585142  | 130      | 2585362  
    l2d_tlb_refill:u   | 78        | 138      | 9        | 655      
    ll_cache:u         | 4925221   | 2342957  | 364      | 5127641  
    ll_cache_miss:u    | 76068     | 2124     | 65       | 2241     
combined_orders:
    id        | modules                                                                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p512_np4_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l4_sp17+hot_b128_bp3_r100_rand_p16_np2_l4+itlb_f128_l1_r100_pstr_p512_np1_l2_sp33
    shuffle   | cold_b128_d4_bitrev_lshuf_p512_np4_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l4_sp17+itlb_f128_l1_r100_pstr_p512_np1_l2_sp33+hot_b128_bp3_r100_rand_p16_np2_l4
    sum       | cold_b128_d4_bitrev_lshuf_p512_np4_l2+fetch_b64_d1_bp0_s16_r100_pstr_p128_np4_l4_sp17+hot_b128_bp3_r100_rand_p16_np2_l4+itlb_f128_l1_r100_pstr_p512_np1_l2_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 566514670 | 601233031 | 577483890
    instructions:u     | 96441851  | 96441851  | 96474159 
    br_retired:u       | 9291993   | 9291993   | 9295634  
    br_mis_pred:u      | 883118    | 881880    | 888163   
    l1i_cache:u        | 23425049  | 23402551  | 22975210 
    l1i_cache_refill:u | 2814703   | 2943616   | 3336816  
    l1i_tlb:u          | 23425049  | 23402551  | 22975210 
    l1i_tlb_refill:u   | 1310955   | 1310946   | 1310189  
    l2i_cache:u        | 2814702   | 2943609   | 3336811  
    l2i_cache_refill:u | 2135688   | 2146704   | 2368329  
    l2i_tlb:u          | 1311251   | 1311181   | 1310327  
    l2i_tlb_refill:u   | 9340      | 11676     | 137      
    l1d_cache:u        | 18124461  | 18160462  | 18204678 
    l1d_cache_refill:u | 6729520   | 6751960   | 6771436  
    l1d_tlb:u          | 26237648  | 26289263  | 26336496 
    l1d_tlb_refill:u   | 5851346   | 5842501   | 5830584  
    l2d_cache:u        | 32225589  | 32702448  | 32306304 
    l2d_cache_refill:u | 14088788  | 14236144  | 14552801 
    l2d_tlb:u          | 5854906   | 5849059   | 5830841  
    l2d_tlb_refill:u   | 69777     | 74181     | 880      
    ll_cache:u         | 11967075  | 12101963  | 12396183 
    ll_cache_miss:u    | 28568     | 149138    | 80498    

== combo_090_s4 ==
single_modules:
    id | module                                          
    ---+-------------------------------------------------
    s0 | cold_b64_d4_bitrev_rand_p1_np4_l1               
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l2_sp33
    s2 | hot_b128_bp3_r100_lstr_p512_np8_l2_sl9          
    s3 | itlb_f128_l1_r100_pstr_p16_np2_l2_sp17          
single_counts:
    metric             | s0       | s1        | s2        | s3      
    -------------------+----------+-----------+-----------+---------
    cpu-cycles:u       | 8740882  | 119040521 | 134134041 | 88001682
    instructions:u     | 12951049 | 37430988  | 23440997  | 23451003
    br_retired:u       | 1031410  | 3911403   | 3941404   | 1371402 
    br_mis_pred:u      | 130634   | 1243001   | 469       | 452     
    l1i_cache:u        | 3482818  | 17229392  | 3015531   | 3290153 
    l1i_cache_refill:u | 704      | 1047      | 854       | 2930372 
    l1i_tlb:u          | 3482818  | 17229392  | 3015531   | 3290153 
    l1i_tlb_refill:u   | 56       | 57        | 42        | 1310062 
    l2i_cache:u        | 702      | 1047      | 853       | 2930372 
    l2i_cache_refill:u | 631      | 807       | 673       | 870079  
    l2i_tlb:u          | 108      | 95        | 162       | 1310103 
    l2i_tlb_refill:u   | 36       | 25        | 21        | 42      
    l1d_cache:u        | 1535176  | 9199419   | 2697394   | 2695404 
    l1d_cache_refill:u | 168      | 2448386   | 2560987   | 68405   
    l1d_tlb:u          | 1537180  | 15677491  | 5362876   | 2697532 
    l1d_tlb_refill:u   | 61       | 2600370   | 2584309   | 257     
    l2d_cache:u        | 1189     | 8284152   | 10138079  | 3079730 
    l2d_cache_refill:u | 819      | 2679280   | 5133633   | 936138  
    l2d_tlb:u          | 85       | 2600659   | 2584868   | 286     
    l2d_tlb_refill:u   | 3        | 16        | 234       | 34      
    ll_cache:u         | 215      | 2678492   | 5132683   | 91720   
    ll_cache_miss:u    | 48       | 101       | 2814      | 47      
combined_orders:
    id        | modules                                                                                                                                                         
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_rand_p1_np4_l1+fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l2_sp33+hot_b128_bp3_r100_lstr_p512_np8_l2_sl9+itlb_f128_l1_r100_pstr_p16_np2_l2_sp17
    shuffle   | itlb_f128_l1_r100_pstr_p16_np2_l2_sp17+cold_b64_d4_bitrev_rand_p1_np4_l1+hot_b128_bp3_r100_lstr_p512_np8_l2_sl9+fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l2_sp33
    sum       | cold_b64_d4_bitrev_rand_p1_np4_l1+fetch_b128_d1_bp0_s16_r100_pstr_p128_np1_l2_sp33+hot_b128_bp3_r100_lstr_p512_np8_l2_sl9+itlb_f128_l1_r100_pstr_p16_np2_l2_sp17
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 353387637 | 375302351 | 349917126
    instructions:u     | 97241851  | 97241857  | 97274037 
    br_retired:u       | 10251993  | 10251991  | 10255619 
    br_mis_pred:u      | 1362509   | 1361900   | 1374556  
    l1i_cache:u        | 29124162  | 29106054  | 27017894 
    l1i_cache_refill:u | 2996980   | 2990488   | 2932977  
    l1i_tlb:u          | 29124162  | 29106054  | 27017894 
    l1i_tlb_refill:u   | 1300952   | 1300943   | 1310217  
    l2i_cache:u        | 2996977   | 2990486   | 2932974  
    l2i_cache_refill:u | 814858    | 990046    | 872190   
    l2i_tlb:u          | 1301014   | 1300997   | 1310468  
    l2i_tlb_refill:u   | 352       | 845       | 124      
    l1d_cache:u        | 16090288  | 16052506  | 16127393 
    l1d_cache_refill:u | 5064396   | 5029333   | 5077946  
    l1d_tlb:u          | 25229612  | 25149490  | 25275079 
    l1d_tlb_refill:u   | 5182432   | 5188141   | 5184997  
    l2d_cache:u        | 21665043  | 21367338  | 21503150 
    l2d_cache_refill:u | 8684527   | 8637539   | 8749870  
    l2d_tlb:u          | 5192967   | 5193922   | 5185898  
    l2d_tlb_refill:u   | 3040      | 3514      | 287      
    ll_cache:u         | 7890837   | 7666689   | 7903110  
    ll_cache_miss:u    | 14884     | 20197     | 3010     

== combo_091_s4 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl9      
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l2_sp3
    s2 | hot_b64_bp3_r100_lstr_p16_np4_l2_sl9          
    s3 | itlb_f64_l1_r100_pstr_p512_np2_l4_sp33        
single_counts:
    metric             | s0        | s1       | s2       | s3       
    -------------------+-----------+----------+----------+----------
    cpu-cycles:u       | 175718628 | 50404928 | 7828954  | 146213392
    instructions:u     | 29431003  | 37431001 | 11921049 | 13210997 
    br_retired:u       | 1991402   | 3911403  | 2021410  | 731404   
    br_mis_pred:u      | 290726    | 1231106  | 383      | 481      
    l1i_cache:u        | 8192120   | 17106044 | 1565545  | 1748572  
    l1i_cache_refill:u | 1404      | 917      | 608      | 1020420  
    l1i_tlb:u          | 8192120   | 17106044 | 1565545  | 1748572  
    l1i_tlb_refill:u   | 55        | 57       | 43       | 670044   
    l2i_cache:u        | 1403      | 916      | 607      | 1020419  
    l2i_cache_refill:u | 940       | 768      | 541      | 306637   
    l2i_tlb:u          | 103       | 109      | 83       | 670093   
    l2i_tlb_refill:u   | 42        | 40       | 15       | 282      
    l1d_cache:u        | 6837202   | 9211986  | 1415285  | 2696260  
    l1d_cache_refill:u | 4794323   | 335511   | 202      | 2558966  
    l1d_tlb:u          | 12111360  | 12912057 | 1417400  | 5364477  
    l1d_tlb_refill:u   | 5145761   | 176      | 76       | 2584737  
    l2d_cache:u        | 17585355  | 667935   | 1565     | 11223546 
    l2d_cache_refill:u | 6407467   | 1449     | 1093     | 5450538  
    l2d_tlb:u          | 5145796   | 209      | 100      | 2584799  
    l2d_tlb_refill:u   | 11        | 45       | 38       | 620      
    ll_cache:u         | 6406576   | 646      | 489      | 5129194  
    ll_cache_miss:u    | 44830     | 143      | 78       | 567      
combined_orders:
    id        | modules                                                                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl9+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l2_sp3+hot_b64_bp3_r100_lstr_p16_np4_l2_sl9+itlb_f64_l1_r100_pstr_p512_np2_l4_sp33
    shuffle   | fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l2_sp3+itlb_f64_l1_r100_pstr_p512_np2_l4_sp33+cold_b128_d4_bitrev_lstr_p128_np4_l4_sl9+hot_b64_bp3_r100_lstr_p16_np4_l2_sl9
    sum       | cold_b128_d4_bitrev_lstr_p128_np4_l4_sl9+fetch_b128_d1_bp0_s16_r100_pstr_p16_np4_l2_sp3+hot_b64_bp3_r100_lstr_p16_np4_l2_sl9+itlb_f64_l1_r100_pstr_p512_np2_l4_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 655586903 | 458166285 | 380165902
    instructions:u     | 91961851  | 91961851  | 91994050 
    br_retired:u       | 8651993   | 8651993   | 8655619  
    br_mis_pred:u      | 1527789   | 1529635   | 1522696  
    l1i_cache:u        | 30336643  | 30358215  | 28612281 
    l1i_cache_refill:u | 1050574   | 996052    | 1023349  
    l1i_tlb:u          | 30336643  | 30358215  | 28612281 
    l1i_tlb_refill:u   | 661196    | 661200    | 670199   
    l2i_cache:u        | 1050572   | 996053    | 1023345  
    l2i_cache_refill:u | 366926    | 295664    | 308886   
    l2i_tlb:u          | 661268    | 661370    | 670388   
    l2i_tlb_refill:u   | 378       | 897       | 379      
    l1d_cache:u        | 20020966  | 20021361  | 20160733 
    l1d_cache_refill:u | 7582530   | 7619928   | 7689002  
    l1d_tlb:u          | 31579858  | 31689266  | 31805294 
    l1d_tlb_refill:u   | 7733204   | 7763783   | 7730750  
    l2d_cache:u        | 28778262  | 27877591  | 29478401 
    l2d_cache_refill:u | 10851235  | 10118895  | 11860547 
    l2d_tlb:u          | 7739114   | 7765528   | 7730904  
    l2d_tlb_refill:u   | 343       | 1958      | 714      
    ll_cache:u         | 10511794  | 9815661   | 11536905 
    ll_cache_miss:u    | 20578     | 23338     | 45618    

== combo_092_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b128_d4_bitrev_lshuf_p512_np4_l2          
    s1 | fetch_b128_d1_bp0_s16_r100_lstr_p512_np1_l4_sl3
    s2 | hot_b128_bp3_r100_lshuf_p16_np2_l2             
    s3 | itlb_f64_l1_r100_lstr_p512_np2_l1_sl3          
single_counts:
    metric             | s0        | s1        | s2       | s3      
    -------------------+-----------+-----------+----------+---------
    cpu-cycles:u       | 210031165 | 265377151 | 15501753 | 59903176
    instructions:u     | 26871007  | 39991089  | 23441049 | 11290997
    br_retired:u       | 1991406   | 3911412   | 3941410  | 731404  
    br_mis_pred:u      | 290682    | 1233471   | 482      | 516     
    l1i_cache:u        | 7776327   | 17454171  | 3006448  | 1502084 
    l1i_cache_refill:u | 1097      | 1668      | 748      | 1180200 
    l1i_tlb:u          | 7776327   | 17454171  | 3006448  | 1502084 
    l1i_tlb_refill:u   | 47        | 56        | 54       | 660057  
    l2i_cache:u        | 1096      | 1668      | 747      | 1180195 
    l2i_cache_refill:u | 800       | 856       | 652      | 23790   
    l2i_tlb:u          | 88        | 110       | 119      | 660110  
    l2i_tlb_refill:u   | 23        | 46        | 47       | 122     
    l1d_cache:u        | 4267009   | 11763835  | 2695291  | 775620  
    l1d_cache_refill:u | 1684575   | 5058356   | 327      | 640031  
    l1d_tlb:u          | 5257986   | 20968823  | 2697515  | 1524322 
    l1d_tlb_refill:u   | 670068    | 5180063   | 93       | 665247  
    l2d_cache:u        | 11209562  | 22140607  | 1731     | 4021225 
    l2d_cache_refill:u | 4920697   | 10488659  | 984      | 1304180 
    l2d_tlb:u          | 670118    | 5188986   | 114      | 665318  
    l2d_tlb_refill:u   | 575       | 547       | 47       | 552     
    ll_cache:u         | 4919320   | 10487624  | 331      | 1281898 
    ll_cache_miss:u    | 23595     | 56        | 36       | 302     
combined_orders:
    id        | modules                                                                                                                                                       
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lshuf_p512_np4_l2+fetch_b128_d1_bp0_s16_r100_lstr_p512_np1_l4_sl3+hot_b128_bp3_r100_lshuf_p16_np2_l2+itlb_f64_l1_r100_lstr_p512_np2_l1_sl3
    shuffle   | fetch_b128_d1_bp0_s16_r100_lstr_p512_np1_l4_sl3+itlb_f64_l1_r100_lstr_p512_np2_l1_sl3+hot_b128_bp3_r100_lshuf_p16_np2_l2+cold_b128_d4_bitrev_lshuf_p512_np4_l2
    sum       | cold_b128_d4_bitrev_lshuf_p512_np4_l2+fetch_b128_d1_bp0_s16_r100_lstr_p512_np1_l4_sl3+hot_b128_bp3_r100_lshuf_p16_np2_l2+itlb_f64_l1_r100_lstr_p512_np2_l1_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 777700347 | 774417900 | 550813245
    instructions:u     | 101561851 | 101561857 | 101594142
    br_retired:u       | 10571993  | 10571991  | 10575632 
    br_mis_pred:u      | 1522277   | 1523756   | 1525151  
    l1i_cache:u        | 31548569  | 31468619  | 29739030 
    l1i_cache_refill:u | 1040017   | 1014443   | 1183713  
    l1i_tlb:u          | 31548569  | 31468619  | 29739030 
    l1i_tlb_refill:u   | 661308    | 661325    | 660214   
    l2i_cache:u        | 1040019   | 1014441   | 1183706  
    l2i_cache_refill:u | 120496    | 49425     | 26098    
    l2i_tlb:u          | 661603    | 661647    | 660427   
    l2i_tlb_refill:u   | 9459      | 9581      | 238      
    l1d_cache:u        | 19502391  | 19422721  | 19501755 
    l1d_cache_refill:u | 7483327   | 7513935   | 7383289  
    l1d_tlb:u          | 30350418  | 30204974  | 30448646 
    l1d_tlb_refill:u   | 6486132   | 6487252   | 6515471  
    l2d_cache:u        | 37398121  | 37164171  | 37373125 
    l2d_cache_refill:u | 16894644  | 16918159  | 16714520 
    l2d_tlb:u          | 6487187   | 6497261   | 6524536  
    l2d_tlb_refill:u   | 138926    | 138216    | 1721     
    ll_cache:u         | 16748337  | 16864263  | 16689173 
    ll_cache_miss:u    | 80907     | 131889    | 23989    

== combo_093_s4 ==
single_modules:
    id | module                                        
    ---+-----------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p128_np2_l2_sl5      
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p16_np2_l2_sp3
    s2 | hot_b64_bp3_r100_lin_p16_np2_l1               
    s3 | itlb_f64_l1_r100_lshuf_p512_np4_l4            
single_counts:
    metric             | s0        | s1       | s2       | s3       
    -------------------+-----------+----------+----------+----------
    cpu-cycles:u       | 106444822 | 48787984 | 5251402  | 152230541
    instructions:u     | 26870997  | 37430988 | 11281049 | 13210997 
    br_retired:u       | 1991404   | 3911403  | 2021410  | 731404   
    br_mis_pred:u      | 290725    | 1231034  | 389      | 460      
    l1i_cache:u        | 7713522   | 16882334 | 1485599  | 1883892  
    l1i_cache_refill:u | 999       | 863      | 568      | 1315653  
    l1i_tlb:u          | 7713522   | 16882334 | 1485599  | 1883892  
    l1i_tlb_refill:u   | 54        | 52       | 44       | 670059   
    l2i_cache:u        | 997       | 862      | 569      | 1315651  
    l2i_cache_refill:u | 799       | 715      | 526      | 382889   
    l2i_tlb:u          | 105       | 87       | 88       | 670100   
    l2i_tlb_refill:u   | 39        | 17       | 13       | 49       
    l1d_cache:u        | 4256514   | 9128098  | 775365   | 2695725  
    l1d_cache_refill:u | 2352536   | 89526    | 171      | 1486851  
    l1d_tlb:u          | 6955158   | 12787277 | 777569   | 3665413  
    l1d_tlb_refill:u   | 2583435   | 171      | 75       | 660073   
    l2d_cache:u        | 8460987   | 406062   | 1589     | 11574633 
    l2d_cache_refill:u | 2777430   | 15803    | 1099     | 5016506  
    l2d_tlb:u          | 2584161   | 200      | 100      | 660097   
    l2d_tlb_refill:u   | 299       | 48       | 49       | 159      
    ll_cache:u         | 2776490   | 14970    | 453      | 4660034  
    ll_cache_miss:u    | 17512     | 481      | 347      | 1146     
combined_orders:
    id        | modules                                                                                                                                                   
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p128_np2_l2_sl5+fetch_b128_d1_bp0_s16_r100_pstr_p16_np2_l2_sp3+hot_b64_bp3_r100_lin_p16_np2_l1+itlb_f64_l1_r100_lshuf_p512_np4_l4
    shuffle   | hot_b64_bp3_r100_lin_p16_np2_l1+cold_b128_d4_bitrev_lstr_p128_np2_l2_sl5+fetch_b128_d1_bp0_s16_r100_pstr_p16_np2_l2_sp3+itlb_f64_l1_r100_lshuf_p512_np4_l4
    sum       | cold_b128_d4_bitrev_lstr_p128_np2_l2_sl5+fetch_b128_d1_bp0_s16_r100_pstr_p16_np2_l2_sp3+hot_b64_bp3_r100_lin_p16_np2_l1+itlb_f64_l1_r100_lshuf_p512_np4_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 298626307 | 360770940 | 312714749
    instructions:u     | 88761998  | 88761851  | 88794031 
    br_retired:u       | 8652013   | 8651993   | 8655621  
    br_mis_pred:u      | 1522321   | 1521998   | 1522608  
    l1i_cache:u        | 29826288  | 29943081  | 27965347 
    l1i_cache_refill:u | 1016546   | 1108565   | 1318083  
    l1i_tlb:u          | 29826288  | 29943081  | 27965347 
    l1i_tlb_refill:u   | 661066    | 661124    | 670209   
    l2i_cache:u        | 1016545   | 1108564   | 1318079  
    l2i_cache_refill:u | 228726    | 325488    | 384929   
    l2i_tlb:u          | 661132    | 661233    | 670380   
    l2i_tlb_refill:u   | 673       | 509       | 118      
    l1d_cache:u        | 16821109  | 16811607  | 16855702 
    l1d_cache_refill:u | 4180276   | 4178971   | 3929084  
    l1d_tlb:u          | 24092260  | 24047813  | 24185417 
    l1d_tlb_refill:u   | 3259327   | 3256134   | 3243754  
    l2d_cache:u        | 20966209  | 20678475  | 20443271 
    l2d_cache_refill:u | 7401461   | 7794780   | 7810838  
    l2d_tlb:u          | 3270400   | 3256413   | 3244558  
    l2d_tlb_refill:u   | 1983      | 2026      | 555      
    ll_cache:u         | 7167742   | 7481955   | 7451947  
    ll_cache_miss:u    | 9428      | 22663     | 19486    

== combo_094_s4 ==
single_modules:
    id | module                                    
    ---+-------------------------------------------
    s0 | cold_b128_d4_bitrev_lstr_p512_np8_l4_sl9  
    s1 | fetch_b128_d1_bp0_s16_r100_lin_p128_np8_l4
    s2 | hot_b64_bp3_r100_pstr_p16_np1_l4_sp33     
    s3 | itlb_f64_l1_r100_lstr_p16_np2_l2_sl3      
single_counts:
    metric             | s0        | s1       | s2       | s3      
    -------------------+-----------+----------+----------+---------
    cpu-cycles:u       | 378764880 | 99453483 | 12933145 | 22255410
    instructions:u     | 29430957  | 39990994 | 13201049 | 11931049
    br_retired:u       | 1991391   | 3911401  | 2021410  | 731410  
    br_mis_pred:u      | 290866    | 1232289  | 410      | 451     
    l1i_cache:u        | 8233683   | 17385040 | 1725987  | 1578221 
    l1i_cache_refill:u | 1913      | 925      | 656      | 1127382 
    l1i_tlb:u          | 8233683   | 17385040 | 1725987  | 1578221 
    l1i_tlb_refill:u   | 53        | 49       | 45       | 660078  
    l2i_cache:u        | 1912      | 922      | 656      | 1127379 
    l2i_cache_refill:u | 1245      | 761      | 554      | 832     
    l2i_tlb:u          | 107       | 91       | 81       | 660147  
    l2i_tlb_refill:u   | 46        | 17       | 12       | 97      
    l1d_cache:u        | 6824164   | 11752558 | 2695335  | 1415286 
    l1d_cache_refill:u | 5087909   | 1275626  | 261      | 10280   
    l1d_tlb:u          | 12083742  | 16247738 | 2697622  | 1417166 
    l1d_tlb_refill:u   | 5144182   | 670060   | 115      | 133     
    l2d_cache:u        | 22098486  | 13057339 | 1612     | 1792414 
    l2d_cache_refill:u | 10827570  | 1584346  | 951      | 21367   
    l2d_tlb:u          | 5144252   | 678896   | 146      | 159     
    l2d_tlb_refill:u   | 671       | 14       | 42       | 46      
    ll_cache:u         | 10826097  | 1583571  | 346      | 10522   
    ll_cache_miss:u    | 135824    | 23560    | 39       | 27      
combined_orders:
    id        | modules                                                                                                                                                       
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b128_d4_bitrev_lstr_p512_np8_l4_sl9+fetch_b128_d1_bp0_s16_r100_lin_p128_np8_l4+hot_b64_bp3_r100_pstr_p16_np1_l4_sp33+itlb_f64_l1_r100_lstr_p16_np2_l2_sl3
    shuffle   | cold_b128_d4_bitrev_lstr_p512_np8_l4_sl9+fetch_b128_d1_bp0_s16_r100_lin_p128_np8_l4+itlb_f64_l1_r100_lstr_p16_np2_l2_sl3+hot_b64_bp3_r100_pstr_p16_np1_l4_sp33
    sum       | cold_b128_d4_bitrev_lstr_p512_np8_l4_sl9+fetch_b128_d1_bp0_s16_r100_lin_p128_np8_l4+hot_b64_bp3_r100_pstr_p16_np1_l4_sp33+itlb_f64_l1_r100_lstr_p16_np2_l2_sl3
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 475003184 | 444609920 | 513406918
    instructions:u     | 94521857  | 94521851  | 94554049 
    br_retired:u       | 8651991   | 8651993   | 8655612  
    br_mis_pred:u      | 1525172   | 1521768   | 1524016  
    l1i_cache:u        | 30741030  | 30604078  | 28922931 
    l1i_cache_refill:u | 1070022   | 1028932   | 1130876  
    l1i_tlb:u          | 30741030  | 30604078  | 28922931 
    l1i_tlb_refill:u   | 661159    | 661166    | 660225   
    l2i_cache:u        | 1070022   | 1028930   | 1130869  
    l2i_cache_refill:u | 59327     | 63884     | 3392     
    l2i_tlb:u          | 661238    | 661287    | 660426   
    l2i_tlb_refill:u   | 277       | 604       | 172      
    l1d_cache:u        | 22643791  | 22613736  | 22687343 
    l1d_cache_refill:u | 6336270   | 6459016   | 6374076  
    l1d_tlb:u          | 32466082  | 32473518  | 32446268 
    l1d_tlb_refill:u   | 5819106   | 5816726   | 5814490  
    l2d_cache:u        | 39715696  | 39184783  | 36949851 
    l2d_cache_refill:u | 13980308  | 13878960  | 12434234 
    l2d_tlb:u          | 5828528   | 5826829   | 5823453  
    l2d_tlb_refill:u   | 1189      | 2455      | 773      
    ll_cache:u         | 13902761  | 13815309  | 12420536 
    ll_cache_miss:u    | 181162    | 250091    | 159450   

== combo_095_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p16_np8_l1_sl3         
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp3
    s2 | hot_b64_bp3_r100_pstr_p512_np1_l1_sp33         
    s3 | itlb_f128_l1_r100_pstr_p512_np2_l4_sp3         
single_counts:
    metric             | s0       | s1        | s2       | s3       
    -------------------+----------+-----------+----------+----------
    cpu-cycles:u       | 9158490  | 414313732 | 38208027 | 560879249
    instructions:u     | 12951049 | 39990948  | 11280997 | 26010951 
    br_retired:u       | 1031410  | 3911390   | 2021404  | 1371393  
    br_mis_pred:u      | 130412   | 1254426   | 475      | 498      
    l1i_cache:u        | 3704805  | 17740781  | 1490216  | 3554079  
    l1i_cache_refill:u | 664      | 1795      | 749      | 2936218  
    l1i_tlb:u          | 3704805  | 17740781  | 1490216  | 3554079  
    l1i_tlb_refill:u   | 56       | 58        | 54       | 1310066  
    l2i_cache:u        | 663      | 1794      | 748      | 2936213  
    l2i_cache_refill:u | 596      | 873       | 566      | 1705618  
    l2i_tlb:u          | 92       | 106       | 167      | 1310129  
    l2i_tlb_refill:u   | 19       | 46        | 44       | 252      
    l1d_cache:u        | 1535221  | 11780962  | 776470   | 5256041  
    l1d_cache_refill:u | 30816    | 5053540   | 640085   | 5114570  
    l1d_tlb:u          | 1537261  | 20934956  | 1519077  | 10497262 
    l1d_tlb_refill:u   | 98       | 5180053   | 663887   | 5146754  
    l2d_cache:u        | 62965    | 22392931  | 2530364  | 23165804 
    l2d_cache_refill:u | 1114     | 10586678  | 1282762  | 11935475 
    l2d_tlb:u          | 118      | 5192941   | 664206   | 5146798  
    l2d_tlb_refill:u   | 49       | 74        | 593      | 208      
    ll_cache:u         | 533      | 10585495  | 1282048  | 10315025 
    ll_cache_miss:u    | 213      | 220039    | 1540     | 2272     
combined_orders:
    id        | modules                                                                                                                                                             
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p16_np8_l1_sl3+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp3+hot_b64_bp3_r100_pstr_p512_np1_l1_sp33+itlb_f128_l1_r100_pstr_p512_np2_l4_sp3
    shuffle   | itlb_f128_l1_r100_pstr_p512_np2_l4_sp3+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp3+cold_b64_d4_bitrev_lstr_p16_np8_l1_sl3+hot_b64_bp3_r100_pstr_p512_np1_l1_sp33
    sum       | cold_b64_d4_bitrev_lstr_p16_np8_l1_sl3+fetch_b128_d1_bp0_s16_r100_pstr_p512_np2_l4_sp3+hot_b64_bp3_r100_pstr_p512_np1_l1_sp33+itlb_f128_l1_r100_pstr_p512_np2_l4_sp3
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 1144053731 | 1050232737 | 1022559498
    instructions:u     | 90201851   | 90201857   | 90233945  
    br_retired:u       | 8331993    | 8331991    | 8335597   
    br_mis_pred:u      | 1364590    | 1373815    | 1385811   
    l1i_cache:u        | 28361349   | 28526227   | 26489881  
    l1i_cache_refill:u | 2954184    | 2975958    | 2939426   
    l1i_tlb:u          | 28361349   | 28526227   | 26489881  
    l1i_tlb_refill:u   | 1310857    | 1310857    | 1310234   
    l2i_cache:u        | 2954182    | 2975957    | 2939418   
    l2i_cache_refill:u | 1567653    | 1672663    | 1707653   
    l2i_tlb:u          | 1311054    | 1311149    | 1310494   
    l2i_tlb_refill:u   | 15032      | 14906      | 361       
    l1d_cache:u        | 19302887   | 19331017   | 19348694  
    l1d_cache_refill:u | 10863118   | 10840638   | 10839011  
    l1d_tlb:u          | 34543309   | 34533188   | 34488556  
    l1d_tlb_refill:u   | 10977838   | 10973068   | 10990792  
    l2d_cache:u        | 48998194   | 49357456   | 48152064  
    l2d_cache_refill:u | 24164092   | 24356723   | 23806029  
    l2d_tlb:u          | 10988617   | 10983878   | 11004063  
    l2d_tlb_refill:u   | 151923     | 151232     | 924       
    ll_cache:u         | 22506081   | 22607394   | 22183101  
    ll_cache_miss:u    | 284436     | 158244     | 224064    

== combo_096_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p16_np8_l4_sp33        
    s1 | fetch_b128_d1_bp0_s16_r100_pstr_p16_np8_l4_sp33
    s2 | hot_b64_bp3_r100_pstr_p512_np1_l4_sp3          
    s3 | itlb_f128_l1_r100_pstr_p512_np1_l4_sp33        
single_counts:
    metric             | s0       | s1       | s2        | s3       
    -------------------+----------+----------+-----------+----------
    cpu-cycles:u       | 17504724 | 61957841 | 169620845 | 478489034
    instructions:u     | 14871049 | 39990988 | 13200997  | 26010951 
    br_retired:u       | 1031410  | 3911403  | 2021404   | 1371393  
    br_mis_pred:u      | 130603   | 1231390  | 443       | 485      
    l1i_cache:u        | 3967027  | 17275863 | 1741790   | 3322162  
    l1i_cache_refill:u | 727      | 887      | 827       | 2866091  
    l1i_tlb:u          | 3967027  | 17275863 | 1741790   | 3322162  
    l1i_tlb_refill:u   | 49       | 53       | 44        | 1310055  
    l2i_cache:u        | 725      | 886      | 826       | 2866091  
    l2i_cache_refill:u | 584      | 770      | 614       | 2136615  
    l2i_tlb:u          | 85       | 103      | 154       | 1310088  
    l2i_tlb_refill:u   | 14       | 37       | 23        | 1890     
    l1d_cache:u        | 3455475  | 11785493 | 2698003   | 5255660  
    l1d_cache_refill:u | 92555    | 467434   | 2560037   | 5119249  
    l1d_tlb:u          | 3463417  | 15349419 | 5366284   | 10516761 
    l1d_tlb_refill:u   | 112      | 191      | 2585001   | 5149910  
    l2d_cache:u        | 202551   | 1537338  | 10111710  | 23180654 
    l2d_cache_refill:u | 1504     | 1270     | 5123802   | 12403532 
    l2d_tlb:u          | 135      | 215      | 2585616   | 5149972  
    l2d_tlb_refill:u   | 46       | 7        | 79        | 1281     
    ll_cache:u         | 792      | 546      | 5123125   | 10249409 
    ll_cache_miss:u    | 95       | 68       | 1264      | 3443     
combined_orders:
    id        | modules                                                                                                                                                              
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p16_np8_l4_sp33+fetch_b128_d1_bp0_s16_r100_pstr_p16_np8_l4_sp33+hot_b64_bp3_r100_pstr_p512_np1_l4_sp3+itlb_f128_l1_r100_pstr_p512_np1_l4_sp33
    shuffle   | itlb_f128_l1_r100_pstr_p512_np1_l4_sp33+hot_b64_bp3_r100_pstr_p512_np1_l4_sp3+cold_b64_d4_bitrev_pstr_p16_np8_l4_sp33+fetch_b128_d1_bp0_s16_r100_pstr_p16_np8_l4_sp33
    sum       | cold_b64_d4_bitrev_pstr_p16_np8_l4_sp33+fetch_b128_d1_bp0_s16_r100_pstr_p16_np8_l4_sp33+hot_b64_bp3_r100_pstr_p512_np1_l4_sp3+itlb_f128_l1_r100_pstr_p512_np1_l4_sp33
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 704922223 | 979556301 | 727572444
    instructions:u     | 94041851  | 94041851  | 94073985 
    br_retired:u       | 8331993   | 8331993   | 8335610  
    br_mis_pred:u      | 1361736   | 1361675   | 1362921  
    l1i_cache:u        | 28498547  | 28501357  | 26306842 
    l1i_cache_refill:u | 2866698   | 3091832   | 2868532  
    l1i_tlb:u          | 28498547  | 28501357  | 26306842 
    l1i_tlb_refill:u   | 1310854   | 1310847   | 1310201  
    l2i_cache:u        | 2866695   | 3091830   | 2868528  
    l2i_cache_refill:u | 2166253   | 2230248   | 2138583  
    l2i_tlb:u          | 1310981   | 1310936   | 1310430  
    l2i_tlb_refill:u   | 10701     | 10248     | 1964     
    l1d_cache:u        | 23063761  | 23044943  | 23194631 
    l1d_cache_refill:u | 8227837   | 8097327   | 8239275  
    l1d_tlb:u          | 34700763  | 34630333  | 34695881 
    l1d_tlb_refill:u   | 7739443   | 7730331   | 7735214  
    l2d_cache:u        | 36645670  | 37918394  | 35032253 
    l2d_cache_refill:u | 17556129  | 17611270  | 17530108 
    l2d_tlb:u          | 7739941   | 7731162   | 7735938  
    l2d_tlb_refill:u   | 53627     | 50977     | 1413     
    ll_cache:u         | 15422615  | 15433784  | 15373872 
    ll_cache_miss:u    | 10177     | 8611      | 4870     

== combo_097_s4 ==
single_modules:
    id | module                                         
    ---+------------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p1_np8_l1_sl9          
    s1 | fetch_b64_d1_bp0_s16_r100_pstr_p512_np8_l4_sp33
    s2 | hot_b128_bp3_r100_lshuf_p16_np1_l2             
    s3 | itlb_f64_l1_r100_rand_p1_np2_l4                
single_counts:
    metric             | s0       | s1        | s2       | s3      
    -------------------+----------+-----------+----------+---------
    cpu-cycles:u       | 8736491  | 154130274 | 15498291 | 27014596
    instructions:u     | 12951049 | 20150988  | 23441055 | 13210997
    br_retired:u       | 1031410  | 1991403   | 3941408  | 731404  
    br_mis_pred:u      | 130629   | 598460    | 408      | 455     
    l1i_cache:u        | 3488004  | 8883115   | 3005996  | 1727859 
    l1i_cache_refill:u | 681      | 767       | 708      | 1088272 
    l1i_tlb:u          | 3488004  | 8883115   | 3005996  | 1727859 
    l1i_tlb_refill:u   | 52       | 54        | 54       | 670083  
    l2i_cache:u        | 680      | 767       | 706      | 1088270 
    l2i_cache_refill:u | 608      | 685       | 633      | 871     
    l2i_tlb:u          | 104      | 99        | 101      | 670146  
    l2i_tlb_refill:u   | 45       | 42        | 22       | 66      
    l1d_cache:u        | 1535310  | 6015272   | 2695255  | 2695186 
    l1d_cache_refill:u | 171      | 2528364   | 173      | 153     
    l1d_tlb:u          | 1537395  | 10662660  | 2746965  | 2696867 
    l1d_tlb_refill:u   | 60       | 2602562   | 111      | 60      
    l2d_cache:u        | 1398     | 11112935  | 1527     | 1834920 
    l2d_cache_refill:u | 963      | 5304023   | 1019     | 1170    
    l2d_tlb:u          | 88       | 2614556   | 136      | 93      
    l2d_tlb_refill:u   | 26       | 95        | 46       | 18      
    ll_cache:u         | 298      | 5303212   | 326      | 295     
    ll_cache_miss:u    | 26       | 167964    | 33       | 41      
combined_orders:
    id        | modules                                                                                                                                                 
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p1_np8_l1_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p512_np8_l4_sp33+hot_b128_bp3_r100_lshuf_p16_np1_l2+itlb_f64_l1_r100_rand_p1_np2_l4
    shuffle   | hot_b128_bp3_r100_lshuf_p16_np1_l2+cold_b64_d4_bitrev_lstr_p1_np8_l1_sl9+itlb_f64_l1_r100_rand_p1_np2_l4+fetch_b64_d1_bp0_s16_r100_pstr_p512_np8_l4_sp33
    sum       | cold_b64_d4_bitrev_lstr_p1_np8_l1_sl9+fetch_b64_d1_bp0_s16_r100_pstr_p512_np8_l4_sp33+hot_b128_bp3_r100_lshuf_p16_np1_l2+itlb_f64_l1_r100_rand_p1_np2_l4
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 203791083 | 226204616 | 205379652
    instructions:u     | 69721908  | 69721898  | 69754089 
    br_retired:u       | 7692005   | 7692005   | 7695625  
    br_mis_pred:u      | 723141    | 723497    | 729952   
    l1i_cache:u        | 18124110  | 18167592  | 17104974 
    l1i_cache_refill:u | 1251060   | 964223    | 1090428  
    l1i_tlb:u          | 18124110  | 18167592  | 17104974 
    l1i_tlb_refill:u   | 660750    | 660747    | 670243   
    l2i_cache:u        | 1251059   | 964224    | 1090423  
    l2i_cache_refill:u | 14084     | 14275     | 2797     
    l2i_tlb:u          | 660794    | 660790    | 670450   
    l2i_tlb_refill:u   | 70        | 59        | 175      
    l1d_cache:u        | 12851856  | 12853590  | 12941023 
    l1d_cache_refill:u | 2533502   | 2528554   | 2528861  
    l1d_tlb:u          | 17335614  | 17348690  | 17643887 
    l1d_tlb_refill:u   | 2586354   | 2587077   | 2602793  
    l2d_cache:u        | 12437959  | 12496082  | 12950780 
    l2d_cache_refill:u | 5519727   | 5504912   | 5307175  
    l2d_tlb:u          | 2586481   | 2587989   | 2614873  
    l2d_tlb_refill:u   | 236       | 337       | 185      
    ll_cache:u         | 5504631   | 5490017   | 5304131  
    ll_cache_miss:u    | 42586     | 29252     | 168064   

== combo_098_s4 ==
single_modules:
    id | module                                     
    ---+--------------------------------------------
    s0 | cold_b64_d4_bitrev_lstr_p512_np2_l4_sl5    
    s1 | fetch_b128_d1_bp0_s16_r100_lshuf_p16_np1_l1
    s2 | hot_b128_bp3_r100_lstr_p128_np8_l4_sl9     
    s3 | itlb_f64_l1_r100_lshuf_p512_np8_l2         
single_counts:
    metric             | s0        | s1       | s2        | s3       
    -------------------+-----------+----------+-----------+----------
    cpu-cycles:u       | 240590249 | 43052277 | 143221043 | 111419674
    instructions:u     | 14871007  | 36150994 | 26000997  | 11930997 
    br_retired:u       | 1031406   | 3911401  | 3941404   | 731404   
    br_mis_pred:u      | 130700    | 1231068  | 461       | 480      
    l1i_cache:u        | 3965157   | 16722282 | 3335563   | 1576650  
    l1i_cache_refill:u | 790       | 900      | 1010      | 1039528  
    l1i_tlb:u          | 3965157   | 16722282 | 3335563   | 1576650  
    l1i_tlb_refill:u   | 55        | 55       | 49        | 660048   
    l2i_cache:u        | 790       | 898      | 1009      | 1039526  
    l2i_cache_refill:u | 630       | 757      | 676       | 6429     
    l2i_tlb:u          | 89        | 107      | 175       | 660088   
    l2i_tlb_refill:u   | 26        | 33       | 16        | 51       
    l1d_cache:u        | 3457026   | 7845490  | 5257280   | 1415621  
    l1d_cache_refill:u | 2516143   | 50609    | 4933287   | 1009399  
    l1d_tlb:u          | 6140391   | 11499401 | 10500524  | 1651532  
    l1d_tlb_refill:u   | 2584162   | 160      | 5154824   | 170061   
    l2d_cache:u        | 11091233  | 92710    | 14659205  | 6616081  
    l2d_cache_refill:u | 5434452   | 1077     | 4265265   | 2473317  
    l2d_tlb:u          | 2584211   | 184      | 5155278   | 170089   
    l2d_tlb_refill:u   | 75        | 49       | 163       | 680      
    ll_cache:u         | 5433626   | 336      | 4264466   | 2462082  
    ll_cache_miss:u    | 43364     | 66       | 961       | 1922     
combined_orders:
    id        | modules                                                                                                                                                      
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_lstr_p512_np2_l4_sl5+fetch_b128_d1_bp0_s16_r100_lshuf_p16_np1_l1+hot_b128_bp3_r100_lstr_p128_np8_l4_sl9+itlb_f64_l1_r100_lshuf_p512_np8_l2
    shuffle   | hot_b128_bp3_r100_lstr_p128_np8_l4_sl9+itlb_f64_l1_r100_lshuf_p512_np8_l2+fetch_b128_d1_bp0_s16_r100_lshuf_p16_np1_l1+cold_b64_d4_bitrev_lstr_p512_np2_l4_sl5
    sum       | cold_b64_d4_bitrev_lstr_p512_np2_l4_sl5+fetch_b128_d1_bp0_s16_r100_lshuf_p16_np1_l1+hot_b128_bp3_r100_lstr_p128_np8_l4_sl9+itlb_f64_l1_r100_lshuf_p512_np8_l2
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 540711601 | 703125880 | 538283243
    instructions:u     | 88921851  | 88921851  | 88953995 
    br_retired:u       | 9611993   | 9611993   | 9615615  
    br_mis_pred:u      | 1362504   | 1362155   | 1362709  
    l1i_cache:u        | 27803075  | 27805109  | 25599652 
    l1i_cache_refill:u | 961884    | 1077639   | 1042228  
    l1i_tlb:u          | 27803075  | 27805109  | 25599652 
    l1i_tlb_refill:u   | 661089    | 661109    | 660207   
    l2i_cache:u        | 961881    | 1077638   | 1042223  
    l2i_cache_refill:u | 30446     | 58484     | 8492     
    l2i_tlb:u          | 661265    | 661234    | 660459   
    l2i_tlb_refill:u   | 6401      | 6474      | 126      
    l1d_cache:u        | 18014756  | 17957723  | 17975417 
    l1d_cache_refill:u | 8602456   | 8465165   | 8509438  
    l1d_tlb:u          | 29915172  | 29823787  | 29791848 
    l1d_tlb_refill:u   | 7912251   | 7900833   | 7909207  
    l2d_cache:u        | 34351602  | 33909185  | 32459229 
    l2d_cache_refill:u | 14021474  | 13736682  | 12174111 
    l2d_tlb:u          | 7915045   | 7901801   | 7909762  
    l2d_tlb_refill:u   | 58695     | 56992     | 967      
    ll_cache:u         | 13984053  | 13672861  | 12160510 
    ll_cache_miss:u    | 81984     | 133544    | 46313    

== combo_099_s4 ==
single_modules:
    id | module                                  
    ---+-----------------------------------------
    s0 | cold_b64_d4_bitrev_pstr_p16_np4_l4_sp17 
    s1 | fetch_b64_d1_bp0_s16_r100_lin_p16_np8_l1
    s2 | hot_b128_bp3_r100_lstr_p512_np4_l1_sl9  
    s3 | itlb_f128_l1_r100_lstr_p128_np2_l1_sl5  
single_counts:
    metric             | s0       | s1       | s2       | s3       
    -------------------+----------+----------+----------+----------
    cpu-cycles:u       | 17031487 | 21136677 | 67246687 | 157676960
    instructions:u     | 14871049 | 18231046 | 22160997 | 22170997 
    br_retired:u       | 1031410  | 1991407  | 3941404  | 1371404  
    br_mis_pred:u      | 130607   | 591011   | 450      | 500      
    l1i_cache:u        | 3958386  | 8391403  | 2852178  | 3215212  
    l1i_cache_refill:u | 669      | 640      | 749      | 2941833  
    l1i_tlb:u          | 3958386  | 8391403  | 2852178  | 3215212  
    l1i_tlb_refill:u   | 45       | 39       | 39       | 1300059  
    l2i_cache:u        | 668      | 638      | 748      | 2941831  
    l2i_cache_refill:u | 587      | 587      | 620      | 1429422  
    l2i_tlb:u          | 84       | 75       | 162      | 1300103  
    l2i_tlb_refill:u   | 12       | 14       | 23       | 40       
    l1d_cache:u        | 3458054  | 4005468  | 1416608  | 1415372  
    l1d_cache_refill:u | 93641    | 48275    | 1279971  | 1246465  
    l1d_tlb:u          | 3465247  | 5758986  | 2802578  | 2793816  
    l1d_tlb_refill:u   | 111      | 116      | 1304576  | 1303111  
    l2d_cache:u        | 243681   | 92394    | 5073022  | 7032619  
    l2d_cache_refill:u | 1276     | 1395     | 2569971  | 3129767  
    l2d_tlb:u          | 138      | 138      | 1304926  | 1303135  
    l2d_tlb_refill:u   | 47       | 38       | 96       | 21       
    ll_cache:u         | 597      | 717      | 2569249  | 1782139  
    ll_cache_miss:u    | 270      | 91       | 705      | 323      
combined_orders:
    id        | modules                                                                                                                                                       
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | cold_b64_d4_bitrev_pstr_p16_np4_l4_sp17+fetch_b64_d1_bp0_s16_r100_lin_p16_np8_l1+hot_b128_bp3_r100_lstr_p512_np4_l1_sl9+itlb_f128_l1_r100_lstr_p128_np2_l1_sl5
    shuffle   | hot_b128_bp3_r100_lstr_p512_np4_l1_sl9+itlb_f128_l1_r100_lstr_p128_np2_l1_sl5+cold_b64_d4_bitrev_pstr_p16_np4_l4_sp17+fetch_b64_d1_bp0_s16_r100_lin_p16_np8_l1
    sum       | cold_b64_d4_bitrev_pstr_p16_np4_l4_sp17+fetch_b64_d1_bp0_s16_r100_lin_p16_np8_l1+hot_b128_bp3_r100_lstr_p512_np4_l1_sl9+itlb_f128_l1_r100_lstr_p128_np2_l1_sl5
combined_counts:
    metric             | canonical | shuffle   | sum      
    -------------------+-----------+-----------+----------
    cpu-cycles:u       | 283971083 | 279354739 | 263091811
    instructions:u     | 77401998  | 77401998  | 77434089 
    br_retired:u       | 8332013   | 8332013   | 8335625  
    br_mis_pred:u      | 722958    | 722173    | 722568   
    l1i_cache:u        | 19191278  | 19192314  | 18417179 
    l1i_cache_refill:u | 2988215   | 2985613   | 2943891  
    l1i_tlb:u          | 19191278  | 19192314  | 18417179 
    l1i_tlb_refill:u   | 1300749   | 1300749   | 1300182  
    l2i_cache:u        | 2988210   | 2985611   | 2943885  
    l2i_cache_refill:u | 1664174   | 1476465   | 1431216  
    l2i_tlb:u          | 1300799   | 1300793   | 1300424  
    l2i_tlb_refill:u   | 533       | 588       | 89       
    l1d_cache:u        | 10260597  | 10259235  | 10295502 
    l1d_cache_refill:u | 2561842   | 2564430   | 2668352  
    l1d_tlb:u          | 14787304  | 14772033  | 14820627 
    l1d_tlb_refill:u   | 2612963   | 2611356   | 2607914  
    l2d_cache:u        | 13259226  | 13090338  | 12441716 
    l2d_cache_refill:u | 6004129   | 5977260   | 5702409  
    l2d_tlb:u          | 2623130   | 2611632   | 2608337  
    l2d_tlb_refill:u   | 2705      | 648       | 202      
    ll_cache:u         | 4452675   | 4581178   | 4352702  
    ll_cache_miss:u    | 27692     | 17186     | 1389     

