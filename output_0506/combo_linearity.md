== combo_linearity ==
source=output/combo_linearity.csv
mode=csv_render_only
errors=not_computed
layout_snapshots=not_available_from_csv
cases=100
rows=746
metrics=22
metric_set=raw

== combo_000_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld1_indir_p128_lp4_r1000
    s1 | mix_b128_ld14_lin_p512_lp1_r1000 
single_counts:
    metric             | s0         | s1         
    -------------------+------------+------------
    cpu-cycles:u       | 2755929652 | 76400168030
    instructions:u     | 2085063801 | 2085065116 
    br_retired:u       | 8004920    | 8005198    
    br_mis_pred:u      | 1970       | 3336       
    l1i_cache:u        | 266224777  | 268419941  
    l1i_cache_refill:u | 3744       | 58632      
    l1i_tlb:u          | 266224777  | 268419941  
    l1i_tlb_refill:u   | 39         | 48         
    l2i_cache:u        | 3760       | 58891      
    l2i_cache_refill:u | 657        | 2692       
    l2i_tlb:u          | 190        | 92         
    l2i_tlb_refill:u   | 16         | 31         
    l1d_cache:u        | 141083738  | 1808802560 
    l1d_cache_refill:u | 119542373  | 1795769212 
    l1d_tlb:u          | 254157391  | 3618874168 
    l1d_tlb_refill:u   | 106258825  | 1798254700 
    l2d_cache:u        | 354303185  | 7098561775 
    l2d_cache_refill:u | 78054426   | 3580061110 
    l2d_tlb:u          | 106410353  | 1798506598 
    l2d_tlb_refill:u   | 21         | 614        
    ll_cache:u         | 78052351   | 3580016529 
    ll_cache_miss:u    | 1016       | 161176     
combined_orders:
    id        | modules                                                           
    ----------+-------------------------------------------------------------------
    canonical | mix_b128_ld1_indir_p128_lp4_r1000+mix_b128_ld14_lin_p512_lp1_r1000
    shuffle   | mix_b128_ld14_lin_p512_lp1_r1000+mix_b128_ld1_indir_p128_lp4_r1000
    sum       | mix_b128_ld1_indir_p128_lp4_r1000+mix_b128_ld14_lin_p512_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 88744548603 | 80194013064 | 79156097682
    instructions:u     | 4170068086  | 4170068029  | 4170128917 
    br_retired:u       | 16007195    | 16007186    | 16010118   
    br_mis_pred:u      | 5846        | 4691        | 5306       
    l1i_cache:u        | 536703509   | 536526625   | 534644718  
    l1i_cache_refill:u | 133260      | 117315      | 62376      
    l1i_tlb:u          | 536703509   | 536526625   | 534644718  
    l1i_tlb_refill:u   | 51          | 50          | 87         
    l2i_cache:u        | 133386      | 117431      | 62651      
    l2i_cache_refill:u | 15137       | 15367       | 3349       
    l2i_tlb:u          | 160         | 95          | 282        
    l2i_tlb_refill:u   | 31          | 37          | 47         
    l1d_cache:u        | 1949852567  | 1950175285  | 1949886298 
    l1d_cache_refill:u | 1913578883  | 1913378063  | 1915311585 
    l1d_tlb:u          | 3869321303  | 3869559709  | 3873031559 
    l1d_tlb_refill:u   | 1903286658  | 1903558391  | 1904513525 
    l2d_cache:u        | 7441546022  | 7466408321  | 7452864960 
    l2d_cache_refill:u | 3672480012  | 3692958826  | 3658115536 
    l2d_tlb:u          | 1903566343  | 1903812687  | 1904916951 
    l2d_tlb_refill:u   | 25287       | 3761        | 635        
    ll_cache:u         | 3672433816  | 3692909337  | 3658068880 
    ll_cache_miss:u    | 1754073     | 1393356     | 162192     

== combo_001_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b64_ld4_xpage_p512_lp1_r1000 
    s1 | mix_b128_ld1_pshuf_p128_lp1_r1000
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 11154938205 | 3565082490
    instructions:u     | 1061063801  | 2085063795
    br_retired:u       | 8004920     | 8004922   
    br_mis_pred:u      | 2212        | 2503      
    l1i_cache:u        | 139117291   | 266067046 
    l1i_cache_refill:u | 4601        | 3551      
    l1i_tlb:u          | 139117291   | 266067046 
    l1i_tlb_refill:u   | 45          | 39        
    l2i_cache:u        | 4612        | 3563      
    l2i_cache_refill:u | 743         | 636       
    l2i_tlb:u          | 564         | 74        
    l2i_tlb_refill:u   | 24          | 16        
    l1d_cache:u        | 269625366   | 141116461 
    l1d_cache_refill:u | 256337614   | 122801640 
    l1d_tlb:u          | 536037812   | 277948226 
    l1d_tlb_refill:u   | 258421892   | 130000069 
    l2d_cache:u        | 1012759858  | 371040787 
    l2d_cache_refill:u | 513082928   | 114933613 
    l2d_tlb:u          | 258499902   | 130001498 
    l2d_tlb_refill:u   | 645         | 102       
    ll_cache:u         | 513078131   | 114932176 
    ll_cache_miss:u    | 47070       | 557       
combined_orders:
    id        | modules                                                           
    ----------+-------------------------------------------------------------------
    canonical | mix_b64_ld4_xpage_p512_lp1_r1000+mix_b128_ld1_pshuf_p128_lp1_r1000
    shuffle   | mix_b128_ld1_pshuf_p128_lp1_r1000+mix_b64_ld4_xpage_p512_lp1_r1000
    sum       | mix_b64_ld4_xpage_p512_lp1_r1000+mix_b128_ld1_pshuf_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 15833987915 | 16482401016 | 14720020695
    instructions:u     | 3146066786  | 3146066792  | 3146127596 
    br_retired:u       | 16006921    | 16006919    | 16009842   
    br_mis_pred:u      | 4632        | 4538        | 4715       
    l1i_cache:u        | 404414875   | 404362996   | 405184337  
    l1i_cache_refill:u | 16941       | 18823       | 8152       
    l1i_tlb:u          | 404414875   | 404362996   | 405184337  
    l1i_tlb_refill:u   | 41          | 50          | 84         
    l2i_cache:u        | 17014       | 18877       | 8175       
    l2i_cache_refill:u | 1113        | 1167        | 1379       
    l2i_tlb:u          | 90          | 101         | 638        
    l2i_tlb_refill:u   | 29          | 38          | 40         
    l1d_cache:u        | 410666718   | 410705161   | 410741827  
    l1d_cache_refill:u | 377502968   | 374034688   | 379139254  
    l1d_tlb:u          | 813851704   | 813742956   | 813986038  
    l1d_tlb_refill:u   | 388440468   | 388443926   | 388421961  
    l2d_cache:u        | 1386959740  | 1417621735  | 1383800645 
    l2d_cache_refill:u | 623295332   | 632814747   | 628016541  
    l2d_tlb:u          | 388524205   | 388524837   | 388501400  
    l2d_tlb_refill:u   | 1228        | 1118        | 747        
    ll_cache:u         | 623289239   | 632806868   | 628010307  
    ll_cache_miss:u    | 56115       | 142400      | 47627      

== combo_002_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld1_indir_p1_lp1_r1000  
    s1 | mix_b64_ld14_indir_p512_lp4_r1000
single_counts:
    metric             | s0         | s1         
    -------------------+------------+------------
    cpu-cycles:u       | 530112979  | 38900538635
    instructions:u     | 2085064014 | 1061065045 
    br_retired:u       | 8004982    | 8005188    
    br_mis_pred:u      | 2251       | 3196       
    l1i_cache:u        | 265040751  | 140113243  
    l1i_cache_refill:u | 974        | 12835      
    l1i_tlb:u          | 265040751  | 140113243  
    l1i_tlb_refill:u   | 38         | 42         
    l2i_cache:u        | 978        | 12866      
    l2i_cache_refill:u | 591        | 1746       
    l2i_tlb:u          | 838        | 191        
    l2i_tlb_refill:u   | 12         | 28         
    l1d_cache:u        | 141033728  | 911080557  
    l1d_cache_refill:u | 151        | 891505786  
    l1d_tlb:u          | 141047587  | 1781314315 
    l1d_tlb_refill:u   | 66         | 857294769  
    l2d_cache:u        | 1691       | 3425198718 
    l2d_cache_refill:u | 899        | 1645472472 
    l2d_tlb:u          | 91         | 857403584  
    l2d_tlb_refill:u   | 4          | 279        
    ll_cache:u         | 271        | 1645399985 
    ll_cache_miss:u    | 39         | 27987144   
combined_orders:
    id        | modules                                                          
    ----------+------------------------------------------------------------------
    canonical | mix_b128_ld1_indir_p1_lp1_r1000+mix_b64_ld14_indir_p512_lp4_r1000
    shuffle   | mix_b64_ld14_indir_p512_lp4_r1000+mix_b128_ld1_indir_p1_lp1_r1000
    sum       | mix_b128_ld1_indir_p1_lp1_r1000+mix_b64_ld14_indir_p512_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 40174390669 | 41262942702 | 39430651614
    instructions:u     | 3146068026  | 3146068032  | 3146129059 
    br_retired:u       | 16007186    | 16007188    | 16010170   
    br_mis_pred:u      | 5431        | 3218        | 5447       
    l1i_cache:u        | 404140415   | 404161770   | 405153994  
    l1i_cache_refill:u | 34781       | 33033       | 13809      
    l1i_tlb:u          | 404140415   | 404161770   | 405153994  
    l1i_tlb_refill:u   | 44          | 50          | 80         
    l2i_cache:u        | 34845       | 33116       | 13844      
    l2i_cache_refill:u | 3890        | 3968        | 2337       
    l2i_tlb:u          | 102         | 102         | 1029       
    l2i_tlb_refill:u   | 27          | 24          | 40         
    l1d_cache:u        | 1052214337  | 1052199692  | 1052114285 
    l1d_cache_refill:u | 891365475   | 890870142   | 891505937  
    l1d_tlb:u          | 1919696409  | 1919640008  | 1922361902 
    l1d_tlb_refill:u   | 856340766   | 856332356   | 857294835  
    l2d_cache:u        | 3429505775  | 3421375594  | 3425200409 
    l2d_cache_refill:u | 1652389545  | 1644480624  | 1645473371 
    l2d_tlb:u          | 856456117   | 856437166   | 857403675  
    l2d_tlb_refill:u   | 281         | 276         | 283        
    ll_cache:u         | 1652323516  | 1644403795  | 1645400256 
    ll_cache_miss:u    | 15600462    | 23447594    | 27987183   

== combo_003_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b64_ld7_pshuf_p1_lp1_r1000   
    s1 | mix_b128_ld1_indir_p128_lp1_r1000
single_counts:
    metric             | s0         | s1        
    -------------------+------------+-----------
    cpu-cycles:u       | 1810090131 | 3961127861
    instructions:u     | 1061064014 | 2085063795
    br_retired:u       | 8004982    | 8004922   
    br_mis_pred:u      | 2512       | 2063      
    l1i_cache:u        | 137055272  | 266232246 
    l1i_cache_refill:u | 1277       | 3803      
    l1i_tlb:u          | 137055272  | 266232246 
    l1i_tlb_refill:u   | 47         | 44        
    l2i_cache:u        | 1282       | 3822      
    l2i_cache_refill:u | 555        | 647       
    l2i_tlb:u          | 98         | 580       
    l2i_tlb_refill:u   | 13         | 14        
    l1d_cache:u        | 461037606  | 141107025 
    l1d_cache_refill:u | 173        | 125492416 
    l1d_tlb:u          | 461083393  | 278130016 
    l1d_tlb_refill:u   | 77         | 130000087 
    l2d_cache:u        | 1755       | 368344014 
    l2d_cache_refill:u | 788        | 109888506 
    l2d_tlb:u          | 103        | 130004637 
    l2d_tlb_refill:u   | 4          | 21        
    ll_cache:u         | 250        | 109887568 
    ll_cache_miss:u    | 58         | 689       
combined_orders:
    id        | modules                                                         
    ----------+-----------------------------------------------------------------
    canonical | mix_b64_ld7_pshuf_p1_lp1_r1000+mix_b128_ld1_indir_p128_lp1_r1000
    shuffle   | mix_b128_ld1_indir_p128_lp1_r1000+mix_b64_ld7_pshuf_p1_lp1_r1000
    sum       | mix_b64_ld7_pshuf_p1_lp1_r1000+mix_b128_ld1_indir_p128_lp1_r1000
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 5889771003 | 5946715435 | 5771217992
    instructions:u     | 3146066795 | 3146066795 | 3146127809
    br_retired:u       | 16006922   | 16006922   | 16009904  
    br_mis_pred:u      | 4496       | 3573       | 4575      
    l1i_cache:u        | 402106647  | 402268987  | 403287518 
    l1i_cache_refill:u | 7025       | 7334       | 5080      
    l1i_tlb:u          | 402106647  | 402268987  | 403287518 
    l1i_tlb_refill:u   | 45         | 42         | 91        
    l2i_cache:u        | 7054       | 7362       | 5104      
    l2i_cache_refill:u | 750        | 1320       | 1202      
    l2i_tlb:u          | 83         | 325        | 678       
    l2i_tlb_refill:u   | 17         | 18         | 27        
    l1d_cache:u        | 602048262  | 602135138  | 602144631 
    l1d_cache_refill:u | 123291101  | 123654332  | 125492589 
    l1d_tlb:u          | 739352907  | 739180130  | 739213409 
    l1d_tlb_refill:u   | 130001408  | 130001479  | 130000164 
    l2d_cache:u        | 383268684  | 373863254  | 368345769 
    l2d_cache_refill:u | 120194048  | 117189359  | 109889294 
    l2d_tlb:u          | 130002073  | 130007260  | 130004740 
    l2d_tlb_refill:u   | 125        | 26         | 25        
    ll_cache:u         | 120192414  | 117186547  | 109887818 
    ll_cache_miss:u    | 471        | 562        | 747       

== combo_004_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld2_pshuf_p512_lp1_r1000
    s1 | mix_b64_ld2_lin_p1_lp4_r1000     
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 10809278508 | 530933323 
    instructions:u     | 2085063801  | 1061064023
    br_retired:u       | 8004920     | 8004983   
    br_mis_pred:u      | 3095        | 2351      
    l1i_cache:u        | 266124564   | 137083033 
    l1i_cache_refill:u | 9332        | 775       
    l1i_tlb:u          | 266124564   | 137083033 
    l1i_tlb_refill:u   | 42          | 39        
    l2i_cache:u        | 9358        | 772       
    l2i_cache_refill:u | 806         | 524       
    l2i_tlb:u          | 136         | 77        
    l2i_tlb_refill:u   | 23          | 11        
    l1d_cache:u        | 269079665   | 141052876 
    l1d_cache_refill:u | 252197861   | 157       
    l1d_tlb:u          | 532905411   | 141102927 
    l1d_tlb_refill:u   | 258025255   | 70        
    l2d_cache:u        | 1097453836  | 1284      
    l2d_cache_refill:u | 534605493   | 763       
    l2d_tlb:u          | 258034416   | 92        
    l2d_tlb_refill:u   | 230         | 6         
    ll_cache:u         | 534591667   | 226       
    ll_cache_miss:u    | 12701915    | 24        
combined_orders:
    id        | modules                                                       
    ----------+---------------------------------------------------------------
    canonical | mix_b128_ld2_pshuf_p512_lp1_r1000+mix_b64_ld2_lin_p1_lp4_r1000
    shuffle   | mix_b64_ld2_lin_p1_lp4_r1000+mix_b128_ld2_pshuf_p512_lp1_r1000
    sum       | mix_b128_ld2_pshuf_p512_lp1_r1000+mix_b64_ld2_lin_p1_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 11367409363 | 11523183943 | 11340211831
    instructions:u     | 3146066792  | 3146066792  | 3146127824 
    br_retired:u       | 16006919    | 16006919    | 16009903   
    br_mis_pred:u      | 3013        | 5024        | 5446       
    l1i_cache:u        | 405210084   | 404225967   | 403207597  
    l1i_cache_refill:u | 13781       | 16573       | 10107      
    l1i_tlb:u          | 405210084   | 404225967   | 403207597  
    l1i_tlb_refill:u   | 47          | 46          | 81         
    l2i_cache:u        | 13841       | 16626       | 10130      
    l2i_cache_refill:u | 2017        | 2019        | 1330       
    l2i_tlb:u          | 93          | 205         | 213        
    l2i_tlb_refill:u   | 26          | 26          | 34         
    l1d_cache:u        | 410111587   | 410108934   | 410132541  
    l1d_cache_refill:u | 254652568   | 254222720   | 252198018  
    l1d_tlb:u          | 673974578   | 673983296   | 674008338  
    l1d_tlb_refill:u   | 258022842   | 258022646   | 258025325  
    l2d_cache:u        | 1039495464  | 1048016923  | 1097455120 
    l2d_cache_refill:u | 518420882   | 519080732   | 534606256  
    l2d_tlb:u          | 258029481   | 258030476   | 258034508  
    l2d_tlb_refill:u   | 242         | 225         | 236        
    ll_cache:u         | 518412244   | 519073438   | 534591893  
    ll_cache_miss:u    | 4029312     | 5120744     | 12701939   

== combo_005_s2 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld1_xpage_p128_lp1_r1000   
    s1 | mix_b128_ld2_pshuf_p524288_lp1_r1000
single_counts:
    metric             | s0         | s1         
    -------------------+------------+------------
    cpu-cycles:u       | 3786845545 | 11087906361
    instructions:u     | 2085063801 | 2085063801 
    br_retired:u       | 8004920    | 8004920    
    br_mis_pred:u      | 2440       | 2707       
    l1i_cache:u        | 266143250  | 266908400  
    l1i_cache_refill:u | 3870       | 14802      
    l1i_tlb:u          | 266143250  | 266908400  
    l1i_tlb_refill:u   | 48         | 135        
    l2i_cache:u        | 3891       | 14835      
    l2i_cache_refill:u | 679        | 1017       
    l2i_tlb:u          | 89         | 819        
    l2i_tlb_refill:u   | 18         | 130        
    l1d_cache:u        | 141049911  | 269322581  
    l1d_cache_refill:u | 119984360  | 48911009   
    l1d_tlb:u          | 277941379  | 271526132  
    l1d_tlb_refill:u   | 130000067  | 788167     
    l2d_cache:u        | 361048182  | 1149253594 
    l2d_cache_refill:u | 91356297   | 476885138  
    l2d_tlb:u          | 130000750  | 792839     
    l2d_tlb_refill:u   | 116        | 480567     
    ll_cache:u         | 91355061   | 476617112  
    ll_cache_miss:u    | 340        | 435229784  
combined_orders:
    id        | modules                                                               
    ----------+-----------------------------------------------------------------------
    canonical | mix_b128_ld1_xpage_p128_lp1_r1000+mix_b128_ld2_pshuf_p524288_lp1_r1000
    shuffle   | mix_b128_ld2_pshuf_p524288_lp1_r1000+mix_b128_ld1_xpage_p128_lp1_r1000
    sum       | mix_b128_ld1_xpage_p128_lp1_r1000+mix_b128_ld2_pshuf_p524288_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 14996143004 | 14819248291 | 14874751906
    instructions:u     | 4170066792  | 4170066792  | 4170127602 
    br_retired:u       | 16006919    | 16006919    | 16009840   
    br_mis_pred:u      | 4681        | 4158        | 5147       
    l1i_cache:u        | 532031367   | 532177119   | 533051650  
    l1i_cache_refill:u | 34216       | 33651       | 18672      
    l1i_tlb:u          | 532031367   | 532177119   | 533051650  
    l1i_tlb_refill:u   | 205         | 199         | 183        
    l2i_cache:u        | 34279       | 33729       | 18726      
    l2i_cache_refill:u | 2870        | 3206        | 1696       
    l2i_tlb:u          | 727         | 684         | 908        
    l2i_tlb_refill:u   | 202         | 194         | 148        
    l1d_cache:u        | 410433305   | 410332787   | 410372492  
    l1d_cache_refill:u | 169857284   | 170477704   | 168895369  
    l1d_tlb:u          | 551029112   | 548740180   | 549467511  
    l1d_tlb_refill:u   | 131810082   | 130789574   | 130788234  
    l2d_cache:u        | 1516210828  | 1502388061  | 1510301776 
    l2d_cache_refill:u | 587709819   | 579269557   | 568241435  
    l2d_tlb:u          | 131817806   | 130796349   | 130793589  
    l2d_tlb_refill:u   | 604240      | 603722      | 480683     
    ll_cache:u         | 587427415   | 579028387   | 567972173  
    ll_cache_miss:u    | 430058455   | 426711676   | 435230124  

== combo_006_s2 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld14_indir_p524288_lp4_r1000
    s1 | mix_b64_ld1_pshuf_p1_lp4_r1000      
single_counts:
    metric             | s0           | s1        
    -------------------+--------------+-----------
    cpu-cycles:u       | 228476571089 | 274099534 
    instructions:u     | 1061065163   | 1061064170
    br_retired:u       | 8005213      | 8005003   
    br_mis_pred:u      | 3334         | 2125      
    l1i_cache:u        | 137861526    | 138042728 
    l1i_cache_refill:u | 65949        | 655       
    l1i_tlb:u          | 137861526    | 138042728 
    l1i_tlb_refill:u   | 389          | 39        
    l2i_cache:u        | 66065        | 656       
    l2i_cache_refill:u | 7700         | 538       
    l2i_tlb:u          | 443          | 86        
    l2i_tlb_refill:u   | 383          | 12        
    l1d_cache:u        | 909336551    | 77033890  
    l1d_cache_refill:u | 896801897    | 130       
    l1d_tlb:u          | 1794865026   | 77048471  
    l1d_tlb_refill:u   | 870226773    | 68        
    l2d_cache:u        | 3602076273   | 1449      
    l2d_cache_refill:u | 1812076864   | 881       
    l2d_tlb:u          | 870279553    | 332       
    l2d_tlb_refill:u   | 8494059      | 6         
    ll_cache:u         | 1811081073   | 333       
    ll_cache_miss:u    | 1784158741   | 26        
combined_orders:
    id        | modules                                                            
    ----------+--------------------------------------------------------------------
    canonical | mix_b64_ld14_indir_p524288_lp4_r1000+mix_b64_ld1_pshuf_p1_lp4_r1000
    shuffle   | mix_b64_ld1_pshuf_p1_lp4_r1000+mix_b64_ld14_indir_p524288_lp4_r1000
    sum       | mix_b64_ld14_indir_p524288_lp4_r1000+mix_b64_ld1_pshuf_p1_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 228665867257 | 228855122692 | 228750670623
    instructions:u     | 2122068127   | 2122068076   | 2122129333  
    br_retired:u       | 16007208     | 16007201     | 16010216    
    br_mis_pred:u      | 3665         | 5026         | 5459        
    l1i_cache:u        | 274999597    | 275017602    | 275904254   
    l1i_cache_refill:u | 105652       | 103772       | 66604       
    l1i_tlb:u          | 274999597    | 275017602    | 275904254   
    l1i_tlb_refill:u   | 458          | 508          | 428         
    l2i_cache:u        | 105844       | 103922       | 66721       
    l2i_cache_refill:u | 11422        | 11226        | 8238        
    l2i_tlb:u          | 1254         | 566          | 529         
    l2i_tlb_refill:u   | 453          | 503          | 395         
    l1d_cache:u        | 986051286    | 986434216    | 986370441   
    l1d_cache_refill:u | 897848937    | 896972280    | 896802027   
    l1d_tlb:u          | 1871400656   | 1874105489   | 1871913497  
    l1d_tlb_refill:u   | 870174588    | 870437359    | 870226841   
    l2d_cache:u        | 3606802820   | 3606107839   | 3602077722  
    l2d_cache_refill:u | 1815016691   | 1814128692   | 1812077745  
    l2d_tlb:u          | 870223021    | 870491838    | 870279885   
    l2d_tlb_refill:u   | 8411716      | 10193322     | 8494065     
    ll_cache:u         | 1813396036   | 1813130154   | 1811081406  
    ll_cache_miss:u    | 1785895970   | 1785954365   | 1784158767  

== combo_007_s2 ==
single_modules:
    id | module                          
    ---+---------------------------------
    s0 | mix_b128_ld14_xpage_p1_lp1_r1000
    s1 | mix_b64_ld2_indir_p512_lp1_r1000
single_counts:
    metric             | s0         | s1        
    -------------------+------------+-----------
    cpu-cycles:u       | 7186384382 | 5872273344
    instructions:u     | 2085063786 | 1061063795
    br_retired:u       | 8004921    | 8004922   
    br_mis_pred:u      | 3127       | 2701      
    l1i_cache:u        | 265066751  | 137113099 
    l1i_cache_refill:u | 5979       | 2512      
    l1i_tlb:u          | 265066751  | 137113099 
    l1i_tlb_refill:u   | 58         | 49        
    l2i_cache:u        | 5992       | 2522      
    l2i_cache_refill:u | 698        | 616       
    l2i_tlb:u          | 106        | 110       
    l2i_tlb_refill:u   | 32         | 27        
    l1d_cache:u        | 1805038962 | 141067650 
    l1d_cache_refill:u | 235        | 127960494 
    l1d_tlb:u          | 1805087195 | 277132356 
    l1d_tlb_refill:u   | 135        | 130018458 
    l2d_cache:u        | 6310       | 512471492 
    l2d_cache_refill:u | 1030       | 256127526 
    l2d_tlb:u          | 174        | 130030703 
    l2d_tlb_refill:u   | 18         | 195       
    ll_cache:u         | 318        | 256124233 
    ll_cache_miss:u    | 57         | 14295     
combined_orders:
    id        | modules                                                          
    ----------+------------------------------------------------------------------
    canonical | mix_b128_ld14_xpage_p1_lp1_r1000+mix_b64_ld2_indir_p512_lp1_r1000
    shuffle   | mix_b64_ld2_indir_p512_lp1_r1000+mix_b128_ld14_xpage_p1_lp1_r1000
    sum       | mix_b128_ld14_xpage_p1_lp1_r1000+mix_b64_ld2_indir_p512_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 13854275128 | 12827939976 | 13058657726
    instructions:u     | 3146066801  | 3146066795  | 3146127581 
    br_retired:u       | 16006920    | 16006922    | 16009843   
    br_mis_pred:u      | 4937        | 4945        | 5828       
    l1i_cache:u        | 403153047   | 403153101   | 402179850  
    l1i_cache_refill:u | 16204       | 15662       | 8491       
    l1i_tlb:u          | 403153047   | 403153101   | 402179850  
    l1i_tlb_refill:u   | 50          | 51          | 107        
    l2i_cache:u        | 16267       | 15714       | 8514       
    l2i_cache_refill:u | 1845        | 1882        | 1314       
    l2i_tlb:u          | 102         | 157         | 216        
    l2i_tlb_refill:u   | 26          | 25          | 59         
    l1d_cache:u        | 1946303962  | 1946081128  | 1946106612 
    l1d_cache_refill:u | 126914615   | 127556065   | 127960729  
    l1d_tlb:u          | 2086919877  | 2081927032  | 2082219551 
    l1d_tlb_refill:u   | 131131265   | 130018686   | 130018593  
    l2d_cache:u        | 536771140   | 514714531   | 512477802  
    l2d_cache_refill:u | 256319249   | 258023705   | 256128556  
    l2d_tlb:u          | 131205511   | 130026910   | 130030877  
    l2d_tlb_refill:u   | 407         | 253         | 213        
    ll_cache:u         | 256314138   | 258017930   | 256124551  
    ll_cache_miss:u    | 10630       | 1581418     | 14352      

== combo_008_s2 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld4_xpage_p524288_lp4_r1000
    s1 | mix_b128_ld1_lin_p1_lp1_r1000      
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 64595422009 | 530119170 
    instructions:u     | 1061065143  | 2085064014
    br_retired:u       | 8005202     | 8004982   
    br_mis_pred:u      | 2498        | 2300      
    l1i_cache:u        | 141645319   | 265042348 
    l1i_cache_refill:u | 22402       | 1038      
    l1i_tlb:u          | 141645319   | 265042348 
    l1i_tlb_refill:u   | 301         | 38        
    l2i_cache:u        | 22452       | 1038      
    l2i_cache_refill:u | 3473        | 602       
    l2i_tlb:u          | 361         | 276       
    l2i_tlb_refill:u   | 298         | 11        
    l1d_cache:u        | 270573207   | 141033766 
    l1d_cache_refill:u | 257461077   | 144       
    l1d_tlb:u          | 535870921   | 141047679 
    l1d_tlb_refill:u   | 251042198   | 75        
    l2d_cache:u        | 1023320538  | 1885      
    l2d_cache_refill:u | 519171636   | 959       
    l2d_tlb:u          | 251318051   | 96        
    l2d_tlb_refill:u   | 2990684     | 4         
    ll_cache:u         | 519052424   | 341       
    ll_cache_miss:u    | 515891200   | 39        
combined_orders:
    id        | modules                                                          
    ----------+------------------------------------------------------------------
    canonical | mix_b64_ld4_xpage_p524288_lp4_r1000+mix_b128_ld1_lin_p1_lp1_r1000
    shuffle   | mix_b128_ld1_lin_p1_lp1_r1000+mix_b64_ld4_xpage_p524288_lp4_r1000
    sum       | mix_b64_ld4_xpage_p524288_lp4_r1000+mix_b128_ld1_lin_p1_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 65115428904 | 65134333325 | 65125541179
    instructions:u     | 3146068073  | 3146068116  | 3146129157 
    br_retired:u       | 16007193    | 16007198    | 16010184   
    br_mis_pred:u      | 3411        | 4657        | 4798       
    l1i_cache:u        | 407727813   | 407763730   | 406687667  
    l1i_cache_refill:u | 50852       | 53948       | 23440      
    l1i_tlb:u          | 407727813   | 407763730   | 406687667  
    l1i_tlb_refill:u   | 382         | 432         | 339        
    l2i_cache:u        | 50929       | 54024       | 23490      
    l2i_cache_refill:u | 5674        | 5622        | 4075       
    l2i_tlb:u          | 600         | 582         | 637        
    l2i_tlb_refill:u   | 376         | 428         | 309        
    l1d_cache:u        | 411559285   | 411558002   | 411606973  
    l1d_cache_refill:u | 257455568   | 257455135   | 257461221  
    l1d_tlb:u          | 676386583   | 676109733   | 676918600  
    l1d_tlb_refill:u   | 251071272   | 251029624   | 251042273  
    l2d_cache:u        | 1022672548  | 1022261722  | 1023322423 
    l2d_cache_refill:u | 519046904   | 519075631   | 519172595  
    l2d_tlb:u          | 251345276   | 251299260   | 251318147  
    l2d_tlb_refill:u   | 2532660     | 2263574     | 2990688    
    ll_cache:u         | 518925046   | 518950406   | 519052765  
    ll_cache_miss:u    | 515894100   | 515931877   | 515891239  

== combo_009_s2 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b128_ld14_xpage_p512_lp4_r1000
    s1 | mix_b128_ld4_pshuf_p128_lp1_r1000 
single_counts:
    metric             | s0          | s1         
    -------------------+-------------+------------
    cpu-cycles:u       | 77398587889 | 12931455463
    instructions:u     | 2085065123  | 2085063795 
    br_retired:u       | 8005200     | 8004922    
    br_mis_pred:u      | 3114        | 2252       
    l1i_cache:u        | 270133622   | 266071380  
    l1i_cache_refill:u | 55968       | 10621      
    l1i_tlb:u          | 270133622   | 266071380  
    l1i_tlb_refill:u   | 44          | 46         
    l2i_cache:u        | 56368       | 10664      
    l2i_cache_refill:u | 3387        | 798        
    l2i_tlb:u          | 178         | 135        
    l2i_tlb_refill:u   | 32          | 18         
    l1d_cache:u        | 1808947226  | 525527349  
    l1d_cache_refill:u | 1795363384  | 490116984  
    l1d_tlb:u          | 3616530103  | 1048104059 
    l1d_tlb_refill:u   | 1797097427  | 514205275  
    l2d_cache:u        | 7115091373  | 1343652179 
    l2d_cache_refill:u | 3597388971  | 318577742  
    l2d_tlb:u          | 1797279562  | 514652319  
    l2d_tlb_refill:u   | 891         | 28         
    ll_cache:u         | 3597358133  | 318574795  
    ll_cache_miss:u    | 19738831    | 6359       
combined_orders:
    id        | modules                                                             
    ----------+---------------------------------------------------------------------
    canonical | mix_b128_ld14_xpage_p512_lp4_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000
    shuffle   | mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b128_ld14_xpage_p512_lp4_r1000
    sum       | mix_b128_ld14_xpage_p512_lp4_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle      | sum        
    -------------------+-------------+--------------+------------
    cpu-cycles:u       | 99579424612 | 100066486199 | 90330043352
    instructions:u     | 4170068110  | 4170068013   | 4170128918 
    br_retired:u       | 16007198    | 16007185     | 16010122   
    br_mis_pred:u      | 5765        | 6415         | 5366       
    l1i_cache:u        | 537725026   | 537580742    | 536205002  
    l1i_cache_refill:u | 128036      | 128371       | 66589      
    l1i_tlb:u          | 537725026   | 537580742    | 536205002  
    l1i_tlb_refill:u   | 49          | 47           | 90         
    l2i_cache:u        | 128476      | 128791       | 67032      
    l2i_cache_refill:u | 9877        | 11092        | 4185       
    l2i_tlb:u          | 253         | 202          | 313        
    l2i_tlb_refill:u   | 34          | 38           | 50         
    l1d_cache:u        | 2334422783  | 2334530386   | 2334474575 
    l1d_cache_refill:u | 2287726281  | 2290127991   | 2285480368 
    l1d_tlb:u          | 4663803173  | 4665033412   | 4664634162 
    l1d_tlb_refill:u   | 2311311049  | 2311313244   | 2311302702 
    l2d_cache:u        | 8438401464  | 8460926146   | 8458743552 
    l2d_cache_refill:u | 3906213292  | 3931150068   | 3915966713 
    l2d_tlb:u          | 2311604602  | 2311898439   | 2311931881 
    l2d_tlb_refill:u   | 2604        | 2538         | 919        
    ll_cache:u         | 3906165612  | 3931104168   | 3915932928 
    ll_cache_miss:u    | 18675215    | 20571794     | 19745190   

== combo_010_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b64_ld7_lin_p524288_lp1_r1000
    s1 | mix_b128_ld7_indir_p1_lp1_r1000  
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 18585497896 | 3602137812
    instructions:u     | 1061063801  | 2085063786
    br_retired:u       | 8004920     | 8004921   
    br_mis_pred:u      | 2715        | 2654      
    l1i_cache:u        | 138213220   | 266057971 
    l1i_cache_refill:u | 7242        | 3398      
    l1i_tlb:u          | 138213220   | 266057971 
    l1i_tlb_refill:u   | 161         | 42        
    l2i_cache:u        | 7252        | 3420      
    l2i_cache_refill:u | 1075        | 663       
    l2i_tlb:u          | 632         | 294       
    l2i_tlb_refill:u   | 158         | 12        
    l1d_cache:u        | 461606829   | 909038205 
    l1d_cache_refill:u | 86355798    | 183       
    l1d_tlb:u          | 466017850   | 909086112 
    l1d_tlb_refill:u   | 1377512     | 108       
    l2d_cache:u        | 1894568223  | 3939      
    l2d_cache_refill:u | 781713781   | 919       
    l2d_tlb:u          | 1385353     | 141       
    l2d_tlb_refill:u   | 839304      | 11        
    ll_cache:u         | 781283846   | 278       
    ll_cache_miss:u    | 714228906   | 33        
combined_orders:
    id        | modules                                                          
    ----------+------------------------------------------------------------------
    canonical | mix_b64_ld7_lin_p524288_lp1_r1000+mix_b128_ld7_indir_p1_lp1_r1000
    shuffle   | mix_b128_ld7_indir_p1_lp1_r1000+mix_b64_ld7_lin_p524288_lp1_r1000
    sum       | mix_b64_ld7_lin_p524288_lp1_r1000+mix_b128_ld7_indir_p1_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 22213355812 | 22192516100 | 22187635708
    instructions:u     | 3146067018  | 3146067012  | 3146127587 
    br_retired:u       | 16006976    | 16006978    | 16009841   
    br_mis_pred:u      | 2934        | 4098        | 5369       
    l1i_cache:u        | 403472951   | 403546630   | 404271191  
    l1i_cache_refill:u | 23556       | 25165       | 10640      
    l1i_tlb:u          | 403472951   | 403546630   | 404271191  
    l1i_tlb_refill:u   | 222         | 256         | 203        
    l2i_cache:u        | 23646       | 25238       | 10672      
    l2i_cache_refill:u | 2868        | 2652        | 1738       
    l2i_tlb:u          | 610         | 601         | 926        
    l2i_tlb_refill:u   | 218         | 250         | 170        
    l1d_cache:u        | 1370805247  | 1370528106  | 1370645034 
    l1d_cache_refill:u | 86426669    | 86706846    | 86355981   
    l1d_tlb:u          | 1375239601  | 1374947757  | 1375103962 
    l1d_tlb_refill:u   | 1380162     | 1379347     | 1377620    
    l2d_cache:u        | 1897459609  | 1895529420  | 1894572162 
    l2d_cache_refill:u | 784107865   | 779629027   | 781714700  
    l2d_tlb:u          | 1389275     | 1388442     | 1385494    
    l2d_tlb_refill:u   | 843657      | 843817      | 839315     
    ll_cache:u         | 783619306   | 779162034   | 781284124  
    ll_cache_miss:u    | 716402457   | 710845506   | 714228939  

== combo_011_s2 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b128_ld7_pshuf_p512_lp4_r1000 
    s1 | mix_b128_ld14_indir_p512_lp1_r1000
single_counts:
    metric             | s0          | s1         
    -------------------+-------------+------------
    cpu-cycles:u       | 31217190123 | 75888662529
    instructions:u     | 2085065072  | 2085065096 
    br_retired:u       | 8005192     | 8005196    
    br_mis_pred:u      | 2695        | 3253       
    l1i_cache:u        | 268547496   | 269761075  
    l1i_cache_refill:u | 24307       | 56074      
    l1i_tlb:u          | 268547496   | 269761075  
    l1i_tlb_refill:u   | 43          | 52         
    l2i_cache:u        | 24506       | 56343      
    l2i_cache_refill:u | 5056        | 2623       
    l2i_tlb:u          | 154         | 156        
    l2i_tlb_refill:u   | 23          | 26         
    l1d_cache:u        | 910680473   | 1808874889 
    l1d_cache_refill:u | 298270695   | 1794495790 
    l1d_tlb:u          | 1246336619  | 3615747118 
    l1d_tlb_refill:u   | 226306365   | 1797087169 
    l2d_cache:u        | 3587526902  | 7096099187 
    l2d_cache_refill:u | 1565951457  | 3594836376 
    l2d_tlb:u          | 226373155   | 1797313446 
    l2d_tlb_refill:u   | 287         | 513        
    ll_cache:u         | 1565757130  | 3594797203 
    ll_cache_miss:u    | 40400277    | 1576796    
combined_orders:
    id        | modules                                                             
    ----------+---------------------------------------------------------------------
    canonical | mix_b128_ld7_pshuf_p512_lp4_r1000+mix_b128_ld14_indir_p512_lp1_r1000
    shuffle   | mix_b128_ld14_indir_p512_lp1_r1000+mix_b128_ld7_pshuf_p512_lp4_r1000
    sum       | mix_b128_ld7_pshuf_p512_lp4_r1000+mix_b128_ld14_indir_p512_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 126293277667 | 123433534238 | 107105852652
    instructions:u     | 4170068064   | 4170068064   | 4170130168  
    br_retired:u       | 16007192     | 16007192     | 16010388    
    br_mis_pred:u      | 6023         | 6637         | 5948        
    l1i_cache:u        | 537816113    | 535757625    | 538308571   
    l1i_cache_refill:u | 176674       | 174050       | 80381       
    l1i_tlb:u          | 537816113    | 535757625    | 538308571   
    l1i_tlb_refill:u   | 48           | 46           | 95          
    l2i_cache:u        | 177148       | 174316       | 80849       
    l2i_cache_refill:u | 30776        | 31367        | 7679        
    l2i_tlb:u          | 242          | 174          | 310         
    l2i_tlb_refill:u   | 44           | 40           | 49          
    l1d_cache:u        | 2719940016   | 2714251098   | 2719555362  
    l1d_cache_refill:u | 2131367598   | 2128982052   | 2092766485  
    l1d_tlb:u          | 4855270691   | 4841197066   | 4862083737  
    l1d_tlb_refill:u   | 2023523477   | 2020015390   | 2023393534  
    l2d_cache:u        | 10587138114  | 10593076997  | 10683626089 
    l2d_cache_refill:u | 5131101737   | 5129849796   | 5160787833  
    l2d_tlb:u          | 2023782514   | 2020091972   | 2023686601  
    l2d_tlb_refill:u   | 96244        | 108678       | 800         
    ll_cache:u         | 5130847953   | 5129601933   | 5160554333  
    ll_cache_miss:u    | 63794832     | 70981023     | 41977073    

== combo_012_s2 ==
single_modules:
    id | module                         
    ---+--------------------------------
    s0 | mix_b64_ld2_lin_p512_lp1_r1000 
    s1 | mix_b128_ld2_xpage_p1_lp1_r1000
single_counts:
    metric             | s0         | s1        
    -------------------+------------+-----------
    cpu-cycles:u       | 5430859312 | 1042132014
    instructions:u     | 1061063795 | 2085064014
    br_retired:u       | 8004922    | 8004982   
    br_mis_pred:u      | 2631       | 2966      
    l1i_cache:u        | 138124115  | 266052363 
    l1i_cache_refill:u | 2523       | 1378      
    l1i_tlb:u          | 138124115  | 266052363 
    l1i_tlb_refill:u   | 47         | 35        
    l2i_cache:u        | 2528       | 1383      
    l2i_cache_refill:u | 617        | 619       
    l2i_tlb:u          | 132        | 740       
    l2i_tlb_refill:u   | 22         | 11        
    l1d_cache:u        | 141062413  | 269037211 
    l1d_cache_refill:u | 127558920  | 165       
    l1d_tlb:u          | 276841834  | 269077979 
    l1d_tlb_refill:u   | 130015850  | 74        
    l2d_cache:u        | 514464427  | 1912      
    l2d_cache_refill:u | 256130618  | 878       
    l2d_tlb:u          | 130021348  | 102       
    l2d_tlb_refill:u   | 172        | 5         
    ll_cache:u         | 256128236  | 232       
    ll_cache_miss:u    | 3504       | 24        
combined_orders:
    id        | modules                                                       
    ----------+---------------------------------------------------------------
    canonical | mix_b64_ld2_lin_p512_lp1_r1000+mix_b128_ld2_xpage_p1_lp1_r1000
    shuffle   | mix_b128_ld2_xpage_p1_lp1_r1000+mix_b64_ld2_lin_p512_lp1_r1000
    sum       | mix_b64_ld2_lin_p512_lp1_r1000+mix_b128_ld2_xpage_p1_lp1_r1000
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 6513863629 | 6555435006 | 6472991326
    instructions:u     | 3146066795 | 3146066795 | 3146127809
    br_retired:u       | 16006922   | 16006922   | 16009904  
    br_mis_pred:u      | 4971       | 4063       | 5597      
    l1i_cache:u        | 403174990  | 403650574  | 404176478 
    l1i_cache_refill:u | 8209       | 9218       | 3901      
    l1i_tlb:u          | 403174990  | 403650574  | 404176478 
    l1i_tlb_refill:u   | 48         | 57         | 82        
    l2i_cache:u        | 8225       | 9242       | 3911      
    l2i_cache_refill:u | 1427       | 1503       | 1236      
    l2i_tlb:u          | 107        | 106        | 872       
    l2i_tlb_refill:u   | 26         | 31         | 33        
    l1d_cache:u        | 410084102  | 410090888  | 410099624 
    l1d_cache_refill:u | 127341271  | 128007815  | 127559085 
    l1d_tlb:u          | 545889749  | 545951810  | 545919813 
    l1d_tlb_refill:u   | 130017645  | 130020306  | 130015924 
    l2d_cache:u        | 514917161  | 519459533  | 514466339 
    l2d_cache_refill:u | 255703668  | 257360191  | 256131496 
    l2d_tlb:u          | 130026740  | 130031348  | 130021450 
    l2d_tlb_refill:u   | 172        | 185        | 177       
    ll_cache:u         | 255700281  | 257354353  | 256128468 
    ll_cache_miss:u    | 2622       | 886296     | 3528      

== combo_013_s2 ==
single_modules:
    id | module                          
    ---+---------------------------------
    s0 | mix_b64_ld1_indir_p128_lp4_r1000
    s1 | mix_b64_ld1_pshuf_p1_lp1_r1000  
single_counts:
    metric             | s0         | s1        
    -------------------+------------+-----------
    cpu-cycles:u       | 1428141051 | 274087785 
    instructions:u     | 1061064029 | 1061064161
    br_retired:u       | 8004981    | 8005002   
    br_mis_pred:u      | 2059       | 1964      
    l1i_cache:u        | 138175046  | 138044586 
    l1i_cache_refill:u | 1028       | 744       
    l1i_tlb:u          | 138175046  | 138044586 
    l1i_tlb_refill:u   | 36         | 41        
    l2i_cache:u        | 1028       | 743       
    l2i_cache_refill:u | 558        | 527       
    l2i_tlb:u          | 858        | 87        
    l2i_tlb_refill:u   | 11         | 10        
    l1d_cache:u        | 77067180   | 77033769  
    l1d_cache_refill:u | 60681327   | 140       
    l1d_tlb:u          | 136951213  | 77047764  
    l1d_tlb_refill:u   | 54131916   | 59        
    l2d_cache:u        | 158131015  | 1160      
    l2d_cache_refill:u | 30672585   | 794       
    l2d_tlb:u          | 54140257   | 249       
    l2d_tlb_refill:u   | 23         | 5         
    ll_cache:u         | 30671663   | 243       
    ll_cache_miss:u    | 1482       | 32        
combined_orders:
    id        | modules                                                        
    ----------+----------------------------------------------------------------
    canonical | mix_b64_ld1_indir_p128_lp4_r1000+mix_b64_ld1_pshuf_p1_lp1_r1000
    shuffle   | mix_b64_ld1_pshuf_p1_lp1_r1000+mix_b64_ld1_indir_p128_lp4_r1000
    sum       | mix_b64_ld1_indir_p128_lp4_r1000+mix_b64_ld1_pshuf_p1_lp1_r1000
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 1788015595 | 1489838676 | 1702228836
    instructions:u     | 2122067029 | 2122067029 | 2122128190
    br_retired:u       | 16006981   | 16006981   | 16009983  
    br_mis_pred:u      | 3053       | 3393       | 4023      
    l1i_cache:u        | 275209116  | 275193745  | 276219632 
    l1i_cache_refill:u | 2033       | 1782       | 1772      
    l1i_tlb:u          | 275209116  | 275193745  | 276219632 
    l1i_tlb_refill:u   | 44         | 42         | 77        
    l2i_cache:u        | 2036       | 1787       | 1771      
    l2i_cache_refill:u | 693        | 666        | 1085      
    l2i_tlb:u          | 117        | 84         | 945       
    l2i_tlb_refill:u   | 11         | 15         | 21        
    l1d_cache:u        | 154050396  | 154073168  | 154100949 
    l1d_cache_refill:u | 60390480   | 60456915   | 60681467  
    l1d_tlb:u          | 214272271  | 220108032  | 213998977 
    l1d_tlb_refill:u   | 54131083   | 55383554   | 54131975  
    l2d_cache:u        | 151185906  | 159634041  | 158132175 
    l2d_cache_refill:u | 24035666   | 32592230   | 30673379  
    l2d_tlb:u          | 54131365   | 55390733   | 54140506  
    l2d_tlb_refill:u   | 8          | 12         | 28        
    ll_cache:u         | 24034671   | 32591053   | 30671906  
    ll_cache_miss:u    | 987        | 13305      | 1514      

== combo_014_s2 ==
single_modules:
    id | module                          
    ---+---------------------------------
    s0 | mix_b64_ld7_lin_p512_lp1_r1000  
    s1 | mix_b64_ld2_xpage_p512_lp4_r1000
single_counts:
    metric             | s0          | s1        
    -------------------+-------------+-----------
    cpu-cycles:u       | 18811643671 | 5568946559
    instructions:u     | 1061063795  | 1061063795
    br_retired:u       | 8004922     | 8004922   
    br_mis_pred:u      | 3402        | 2387      
    l1i_cache:u        | 138245453   | 138327823 
    l1i_cache_refill:u | 6366        | 2385      
    l1i_tlb:u          | 138245453   | 138327823 
    l1i_tlb_refill:u   | 47          | 45        
    l2i_cache:u        | 6380        | 2391      
    l2i_cache_refill:u | 873         | 643       
    l2i_tlb:u          | 435         | 134       
    l2i_tlb_refill:u   | 22          | 23        
    l1d_cache:u        | 461194103   | 141160581 
    l1d_cache_refill:u | 446662201   | 127952888 
    l1d_tlb:u          | 915704303   | 277328550 
    l1d_tlb_refill:u   | 450128463   | 130062486 
    l2d_cache:u        | 1793965638  | 514716574 
    l2d_cache_refill:u | 904180368   | 258101626 
    l2d_tlb:u          | 450137499   | 130084712 
    l2d_tlb_refill:u   | 232         | 115       
    ll_cache:u         | 904170165   | 258099085 
    ll_cache_miss:u    | 5467006     | 547923    
combined_orders:
    id        | modules                                                        
    ----------+----------------------------------------------------------------
    canonical | mix_b64_ld7_lin_p512_lp1_r1000+mix_b64_ld2_xpage_p512_lp4_r1000
    shuffle   | mix_b64_ld2_xpage_p512_lp4_r1000+mix_b64_ld7_lin_p512_lp1_r1000
    sum       | mix_b64_ld7_lin_p512_lp1_r1000+mix_b64_ld2_xpage_p512_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 28908518066 | 30276081160 | 24380590230
    instructions:u     | 2122068066  | 2122068020  | 2122127590 
    br_retired:u       | 16007192    | 16007186    | 16009844   
    br_mis_pred:u      | 5146        | 5556        | 5789       
    l1i_cache:u        | 275548785   | 275471144   | 276573276  
    l1i_cache_refill:u | 20179       | 22592       | 8751       
    l1i_tlb:u          | 275548785   | 275471144   | 276573276  
    l1i_tlb_refill:u   | 43          | 50          | 92         
    l2i_cache:u        | 20219       | 22681       | 8771       
    l2i_cache_refill:u | 2101        | 2029        | 1516       
    l2i_tlb:u          | 104         | 122         | 569        
    l2i_tlb_refill:u   | 40          | 47          | 45         
    l1d_cache:u        | 602265427   | 602547332   | 602354684  
    l1d_cache_refill:u | 570622305   | 573234911   | 574615089  
    l1d_tlb:u          | 1192859838  | 1199166613  | 1193032853 
    l1d_tlb_refill:u   | 580164598   | 582294772   | 580190949  
    l2d_cache:u        | 2400578269  | 2387208799  | 2308682212 
    l2d_cache_refill:u | 1201065783  | 1190036076  | 1162281994 
    l2d_tlb:u          | 580186134   | 582414238   | 580222211  
    l2d_tlb_refill:u   | 71085       | 111085      | 347        
    ll_cache:u         | 1201038851  | 1190004803  | 1162269250 
    ll_cache_miss:u    | 24656188    | 25660490    | 6014929    

== combo_015_s2 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b128_ld4_lin_p524288_lp4_r1000
    s1 | mix_b128_ld14_lin_p128_lp4_r1000  
single_counts:
    metric             | s0          | s1         
    -------------------+-------------+------------
    cpu-cycles:u       | 53226209165 | 29007700577
    instructions:u     | 2085064944  | 2085065106 
    br_retired:u       | 8005175     | 8005198    
    br_mis_pred:u      | 3022        | 3145       
    l1i_cache:u        | 266908772   | 266339041  
    l1i_cache_refill:u | 53772       | 20625      
    l1i_tlb:u          | 266908772   | 266339041  
    l1i_tlb_refill:u   | 342         | 50         
    l2i_cache:u        | 53894       | 20694      
    l2i_cache_refill:u | 11985       | 1468       
    l2i_tlb:u          | 531         | 97         
    l2i_tlb_refill:u   | 337         | 13         
    l1d_cache:u        | 525371560   | 1806401608 
    l1d_cache_refill:u | 130141432   | 395157119  
    l1d_tlb:u          | 526571643   | 2431509462 
    l1d_tlb_refill:u   | 419186      | 450274576  
    l2d_cache:u        | 1753719015  | 5833955925 
    l2d_cache_refill:u | 960583744   | 1040460442 
    l2d_tlb:u          | 434146      | 450437160  
    l2d_tlb_refill:u   | 271190      | 31         
    ll_cache:u         | 960336438   | 1040391688 
    ll_cache_miss:u    | 911243126   | 1738814    
combined_orders:
    id        | modules                                                            
    ----------+--------------------------------------------------------------------
    canonical | mix_b128_ld4_lin_p524288_lp4_r1000+mix_b128_ld14_lin_p128_lp4_r1000
    shuffle   | mix_b128_ld14_lin_p128_lp4_r1000+mix_b128_ld4_lin_p524288_lp4_r1000
    sum       | mix_b128_ld4_lin_p524288_lp4_r1000+mix_b128_ld14_lin_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 85012050455 | 84970586559 | 82233909742
    instructions:u     | 4170068083  | 4170068134  | 4170130050 
    br_retired:u       | 16007194    | 16007201    | 16010373   
    br_mis_pred:u      | 3879        | 6142        | 6167       
    l1i_cache:u        | 534142298   | 534153792   | 533247813  
    l1i_cache_refill:u | 135874      | 133971      | 74397      
    l1i_tlb:u          | 534142298   | 534153792   | 533247813  
    l1i_tlb_refill:u   | 484         | 543         | 392        
    l2i_cache:u        | 136096      | 134111      | 74588      
    l2i_cache_refill:u | 26908       | 28164       | 13453      
    l2i_tlb:u          | 1132        | 808         | 628        
    l2i_tlb_refill:u   | 477         | 540         | 350        
    l1d_cache:u        | 2332261157  | 2332258535  | 2331773168 
    l1d_cache_refill:u | 588630019   | 585004270   | 525298551  
    l1d_tlb:u          | 2923571267  | 2938319335  | 2958081105 
    l1d_tlb_refill:u   | 451766720   | 450742984   | 450693762  
    l2d_cache:u        | 7329122627  | 7304377261  | 7587674940 
    l2d_cache_refill:u | 2404333334  | 2339981325  | 2001044186 
    l2d_tlb:u          | 451807137   | 450766896   | 450871306  
    l2d_tlb_refill:u   | 343860      | 342033      | 271221     
    ll_cache:u         | 2403899299  | 2339553271  | 2000728126 
    ll_cache_miss:u    | 1295225523  | 1252992939  | 912981940  

== combo_016_s2 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld14_indir_p1_lp1_r1000 
    s1 | mix_b128_ld1_pshuf_p128_lp1_r1000
single_counts:
    metric             | s0         | s1        
    -------------------+------------+-----------
    cpu-cycles:u       | 7186403257 | 4452207299
    instructions:u     | 2085063786 | 2085063795
    br_retired:u       | 8004921    | 8004922   
    br_mis_pred:u      | 3074       | 2631      
    l1i_cache:u        | 266065752  | 265093934 
    l1i_cache_refill:u | 6022       | 4707      
    l1i_tlb:u          | 266065752  | 265093934 
    l1i_tlb_refill:u   | 46         | 45        
    l2i_cache:u        | 6071       | 4728      
    l2i_cache_refill:u | 644        | 694       
    l2i_tlb:u          | 134        | 146       
    l2i_tlb_refill:u   | 14         | 19        
    l1d_cache:u        | 1805038900 | 141084780 
    l1d_cache_refill:u | 212        | 123911893 
    l1d_tlb:u          | 1805087813 | 277264078 
    l1d_tlb_refill:u   | 133        | 130000077 
    l2d_cache:u        | 6672       | 364520107 
    l2d_cache_refill:u | 924        | 108399238 
    l2d_tlb:u          | 154        | 130002127 
    l2d_tlb_refill:u   | 3          | 25        
    ll_cache:u         | 278        | 108397254 
    ll_cache_miss:u    | 72         | 831       
combined_orders:
    id        | modules                                                           
    ----------+-------------------------------------------------------------------
    canonical | mix_b128_ld14_indir_p1_lp1_r1000+mix_b128_ld1_pshuf_p128_lp1_r1000
    shuffle   | mix_b128_ld1_pshuf_p128_lp1_r1000+mix_b128_ld14_indir_p1_lp1_r1000
    sum       | mix_b128_ld14_indir_p1_lp1_r1000+mix_b128_ld1_pshuf_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 10928427429 | 11539065644 | 11638610556
    instructions:u     | 4170066795  | 4170066801  | 4170127581 
    br_retired:u       | 16006922    | 16006920    | 16009843   
    br_mis_pred:u      | 4496        | 4777        | 5705       
    l1i_cache:u        | 532167298   | 532288314   | 531159686  
    l1i_cache_refill:u | 24681       | 25658       | 10729      
    l1i_tlb:u          | 532167298   | 532288314   | 531159686  
    l1i_tlb_refill:u   | 47          | 45          | 91         
    l2i_cache:u        | 24731       | 25690       | 10799      
    l2i_cache_refill:u | 2084        | 1084        | 1338       
    l2i_tlb:u          | 88          | 84          | 280        
    l2i_tlb_refill:u   | 23          | 19          | 33         
    l1d_cache:u        | 1946121670  | 1946111305  | 1946123680 
    l1d_cache_refill:u | 121583111   | 123402729   | 123912105  
    l1d_tlb:u          | 2081646914  | 2082602271  | 2082351891 
    l1d_tlb_refill:u   | 130001513   | 130001909   | 130000210  
    l2d_cache:u        | 375167401   | 378196729   | 364526779  
    l2d_cache_refill:u | 110196553   | 122016263   | 108400162  
    l2d_tlb:u          | 130590816   | 130002940   | 130002281  
    l2d_tlb_refill:u   | 24          | 24          | 28         
    ll_cache:u         | 110193161   | 122013592   | 108397532  
    ll_cache_miss:u    | 1816        | 2631        | 903        

== combo_017_s3 ==
single_modules:
    id | module                         
    ---+--------------------------------
    s0 | mix_b128_ld1_xpage_p1_lp4_r1000
    s1 | mix_b128_ld2_lin_p128_lp1_r1000
    s2 | mix_b64_ld2_lin_p128_lp4_r1000 
single_counts:
    metric             | s0         | s1         | s2        
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 530099541  | 6955830636 | 2240337700
    instructions:u     | 2085064023 | 2085063795 | 1061064023
    br_retired:u       | 8004983    | 8004922    | 8004983   
    br_mis_pred:u      | 2296       | 2944       | 2216      
    l1i_cache:u        | 266041568  | 265081589  | 138116373 
    l1i_cache_refill:u | 1047       | 6146       | 1548      
    l1i_tlb:u          | 266041568  | 265081589  | 138116373 
    l1i_tlb_refill:u   | 41         | 47         | 43        
    l2i_cache:u        | 1051       | 6159       | 1550      
    l2i_cache_refill:u | 607        | 696        | 621       
    l2i_tlb:u          | 626        | 104        | 344       
    l2i_tlb_refill:u   | 12         | 17         | 11        
    l1d_cache:u        | 141034659  | 269067109  | 141050612 
    l1d_cache_refill:u | 175        | 243740839  | 26918701  
    l1d_tlb:u          | 141050159  | 532887854  | 196232888 
    l1d_tlb_refill:u   | 76         | 258000134  | 34001252  
    l2d_cache:u        | 1956       | 765701182  | 336858533 
    l2d_cache_refill:u | 879        | 232458918  | 83320377  
    l2d_tlb:u          | 107        | 258505686  | 34001459  
    l2d_tlb_refill:u   | 5          | 18         | 25        
    ll_cache:u         | 250        | 232457051  | 83315714  
    ll_cache_miss:u    | 72         | 2772       | 610923    
combined_orders:
    id        | modules                                                                                       
    ----------+-----------------------------------------------------------------------------------------------
    canonical | mix_b128_ld1_xpage_p1_lp4_r1000+mix_b128_ld2_lin_p128_lp1_r1000+mix_b64_ld2_lin_p128_lp4_r1000
    shuffle   | mix_b128_ld1_xpage_p1_lp4_r1000+mix_b64_ld2_lin_p128_lp4_r1000+mix_b128_ld2_lin_p128_lp1_r1000
    sum       | mix_b128_ld1_xpage_p1_lp4_r1000+mix_b128_ld2_lin_p128_lp1_r1000+mix_b64_ld2_lin_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum       
    -------------------+-------------+-------------+-----------
    cpu-cycles:u       | 11416268967 | 11249499291 | 9726267877
    instructions:u     | 5231069792  | 5231069792  | 5231191841
    br_retired:u       | 24008919    | 24008919    | 24014888  
    br_mis_pred:u      | 8014        | 8095        | 7456      
    l1i_cache:u        | 671296336   | 671318494   | 669239530 
    l1i_cache_refill:u | 47741       | 47738       | 8741      
    l1i_tlb:u          | 671296336   | 671318494   | 669239530 
    l1i_tlb_refill:u   | 56          | 49          | 131       
    l2i_cache:u        | 47767       | 47788       | 8760      
    l2i_cache_refill:u | 5074        | 6613        | 1924      
    l2i_tlb:u          | 113         | 96          | 1074      
    l2i_tlb_refill:u   | 36          | 20          | 40        
    l1d_cache:u        | 551095093   | 551122239   | 551152380 
    l1d_cache_refill:u | 274196554   | 273064650   | 270659715 
    l1d_tlb:u          | 870167966   | 869762118   | 870170901 
    l1d_tlb_refill:u   | 292004808   | 292008977   | 292001462 
    l2d_cache:u        | 1141330491  | 1164175944  | 1102561671
    l2d_cache_refill:u | 324774444   | 322330397   | 315780174 
    l2d_tlb:u          | 292009683   | 292491183   | 292507252 
    l2d_tlb_refill:u   | 45          | 28          | 48        
    ll_cache:u         | 324755965   | 322316833   | 315773015 
    ll_cache_miss:u    | 114657      | 2726381     | 613767    

== combo_018_s3 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b64_ld14_lin_p524288_lp1_r1000
    s1 | mix_b64_ld7_pshuf_p512_lp4_r1000  
    s2 | mix_b64_ld7_lin_p128_lp1_r1000    
single_counts:
    metric             | s0          | s1          | s2        
    -------------------+-------------+-------------+-----------
    cpu-cycles:u       | 37151968307 | 16699067612 | 9979523847
    instructions:u     | 1061065099  | 1061063801  | 1061063815
    br_retired:u       | 8005196     | 8004920     | 8004924   
    br_mis_pred:u      | 2903        | 2481        | 3015      
    l1i_cache:u        | 140391649   | 138499324   | 138224482 
    l1i_cache_refill:u | 13073       | 6151        | 3658      
    l1i_tlb:u          | 140391649   | 138499324   | 138224482 
    l1i_tlb_refill:u   | 238         | 51          | 57        
    l2i_cache:u        | 13100       | 6168        | 3666      
    l2i_cache_refill:u | 1633        | 2778        | 650       
    l2i_tlb:u          | 585         | 109         | 265       
    l2i_tlb_refill:u   | 231         | 27          | 20        
    l1d_cache:u        | 910405654   | 462195312   | 461594742 
    l1d_cache_refill:u | 168910464   | 195772398   | 434386762 
    l1d_tlb:u          | 917380341   | 630044349   | 917565730 
    l1d_tlb_refill:u   | 2748844     | 114219112   | 450435268 
    l2d_cache:u        | 3798626226  | 1620971151  | 1163183403
    l2d_cache_refill:u | 1559917603  | 700947238   | 260076949 
    l2d_tlb:u          | 2762133     | 114291302   | 450540303 
    l2d_tlb_refill:u   | 1671005     | 697         | 25        
    ll_cache:u         | 1558988459  | 700872815   | 260073150 
    ll_cache_miss:u    | 1421291887  | 20174586    | 10775     
combined_orders:
    id        | modules                                                                                           
    ----------+---------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_lin_p524288_lp1_r1000+mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b64_ld7_lin_p128_lp1_r1000
    shuffle   | mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b64_ld14_lin_p524288_lp1_r1000+mix_b64_ld7_lin_p128_lp1_r1000
    sum       | mix_b64_ld14_lin_p524288_lp1_r1000+mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b64_ld7_lin_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 68759934848 | 72940347050 | 63830559766
    instructions:u     | 3183071053  | 3183071060  | 3183192715 
    br_retired:u       | 24009189    | 24009191    | 24015040   
    br_mis_pred:u      | 7257        | 7562        | 8399       
    l1i_cache:u        | 419606141   | 418437405   | 417115455  
    l1i_cache_refill:u | 61067       | 60832       | 22882      
    l1i_tlb:u          | 419606141   | 418437405   | 417115455  
    l1i_tlb_refill:u   | 400         | 400         | 346        
    l2i_cache:u        | 61222       | 60992       | 22934      
    l2i_cache_refill:u | 9522        | 9954        | 5061       
    l2i_tlb:u          | 962         | 1050        | 959        
    l2i_tlb_refill:u   | 396         | 394         | 278        
    l1d_cache:u        | 1834391811  | 1834685259  | 1834195708 
    l1d_cache_refill:u | 826076033   | 829483701   | 799069624  
    l1d_tlb:u          | 2464830459  | 2465494585  | 2464990420 
    l1d_tlb_refill:u   | 567469942   | 567669625   | 567403224  
    l2d_cache:u        | 6452934224  | 6517033399  | 6582780780 
    l2d_cache_refill:u | 2478229623  | 2555789930  | 2520941790 
    l2d_tlb:u          | 567586568   | 567777312   | 567593738  
    l2d_tlb_refill:u   | 2834726     | 2836642     | 1671727    
    ll_cache:u         | 2477157804  | 2554720861  | 2519934424 
    ll_cache_miss:u    | 1428058640  | 1438315378  | 1441477248 

== combo_019_s3 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld14_indir_p1_lp4_r1000 
    s1 | mix_b128_ld2_indir_p128_lp4_r1000
    s2 | mix_b128_ld7_indir_p128_lp4_r1000
single_counts:
    metric             | s0         | s1         | s2         
    -------------------+------------+------------+------------
    cpu-cycles:u       | 7186365692 | 6383937527 | 16765054591
    instructions:u     | 2085063795 | 2085063801 | 2085063795 
    br_retired:u       | 8004922    | 8004920    | 8004922    
    br_mis_pred:u      | 3119       | 2811       | 2434       
    l1i_cache:u        | 266069461  | 265207869  | 267319021  
    l1i_cache_refill:u | 6064       | 5617       | 13234      
    l1i_tlb:u          | 266069461  | 265207869  | 267319021  
    l1i_tlb_refill:u   | 43         | 53         | 48         
    l2i_cache:u        | 6109       | 5643       | 13278      
    l2i_cache_refill:u | 654        | 779        | 1330       
    l2i_tlb:u          | 194        | 170        | 101        
    l2i_tlb_refill:u   | 15         | 44         | 15         
    l1d_cache:u        | 1805038569 | 269156312  | 909653944  
    l1d_cache_refill:u | 242        | 235875112  | 842200907  
    l1d_tlb:u          | 1805086347 | 484568150  | 1654202264 
    l1d_tlb_refill:u   | 128        | 208539685  | 733984106  
    l2d_cache:u        | 6681       | 624502259  | 2083919487 
    l2d_cache_refill:u | 946        | 105555374  | 317796553  
    l2d_tlb:u          | 159        | 208600786  | 734117550  
    l2d_tlb_refill:u   | 6          | 18         | 14         
    ll_cache:u         | 299        | 105552268  | 317793252  
    ll_cache_miss:u    | 66         | 4630       | 24074      
combined_orders:
    id        | modules                                                                                             
    ----------+-----------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_indir_p1_lp4_r1000+mix_b128_ld2_indir_p128_lp4_r1000+mix_b128_ld7_indir_p128_lp4_r1000
    shuffle   | mix_b128_ld2_indir_p128_lp4_r1000+mix_b128_ld7_indir_p128_lp4_r1000+mix_b128_ld14_indir_p1_lp4_r1000
    sum       | mix_b128_ld14_indir_p1_lp4_r1000+mix_b128_ld2_indir_p128_lp4_r1000+mix_b128_ld7_indir_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 31772321044 | 32457204837 | 30335357810
    instructions:u     | 6255071090  | 6255071066  | 6255191391 
    br_retired:u       | 24009195    | 24009192    | 24014764   
    br_mis_pred:u      | 7309        | 8458        | 8364       
    l1i_cache:u        | 801176401   | 800541436   | 798596351  
    l1i_cache_refill:u | 127364      | 123409      | 24915      
    l1i_tlb:u          | 801176401   | 800541436   | 798596351  
    l1i_tlb_refill:u   | 58          | 52          | 144        
    l2i_cache:u        | 127620      | 123648      | 25030      
    l2i_cache_refill:u | 9113        | 9791        | 2763       
    l2i_tlb:u          | 187         | 119         | 465        
    l2i_tlb_refill:u   | 22          | 25          | 74         
    l1d_cache:u        | 2983887458  | 2984102271  | 2983848825 
    l1d_cache_refill:u | 1086311287  | 1078578104  | 1078076261 
    l1d_tlb:u          | 3949245399  | 3940724758  | 3943856761 
    l1d_tlb_refill:u   | 944066944   | 941212862   | 942523919  
    l2d_cache:u        | 2750447707  | 2755501122  | 2708428427 
    l2d_cache_refill:u | 465154686   | 466808894   | 423352873  
    l2d_tlb:u          | 944204904   | 941312714   | 942718495  
    l2d_tlb_refill:u   | 49          | 50          | 38         
    ll_cache:u         | 465142935   | 466791185   | 423345819  
    ll_cache_miss:u    | 90477       | 2712966     | 28770      

== combo_020_s3 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b128_ld1_pshuf_p128_lp1_r1000    
    s1 | mix_b128_ld2_pshuf_p1_lp4_r1000      
    s2 | mix_b128_ld14_indir_p524288_lp4_r1000
single_counts:
    metric             | s0         | s1         | s2          
    -------------------+------------+------------+-------------
    cpu-cycles:u       | 3673851045 | 1042094514 | 456689308031
    instructions:u     | 2085063801 | 2085064023 | 2085065381  
    br_retired:u       | 8004920    | 8004983    | 8005245     
    br_mis_pred:u      | 2174       | 2815       | 5307        
    l1i_cache:u        | 266173295  | 265055978  | 267140867   
    l1i_cache_refill:u | 3586       | 1463       | 288087      
    l1i_tlb:u          | 266173295  | 265055978  | 267140867   
    l1i_tlb_refill:u   | 41         | 44         | 590         
    l2i_cache:u        | 3598       | 1469       | 291456      
    l2i_cache_refill:u | 650        | 626        | 14966       
    l2i_tlb:u          | 220        | 452        | 1160        
    l2i_tlb_refill:u   | 14         | 12         | 584         
    l1d_cache:u        | 141053670  | 269037925  | 1805306049  
    l1d_cache_refill:u | 123373748  | 161        | 1792350870  
    l1d_tlb:u          | 276376108  | 269066434  | 3566918026  
    l1d_tlb_refill:u   | 130000074  | 72         | 1738359437  
    l2d_cache:u        | 378435546  | 2308       | 7195205053  
    l2d_cache_refill:u | 122282287  | 978        | 3619764021  
    l2d_tlb:u          | 130000493  | 90         | 1738440545  
    l2d_tlb_refill:u   | 18         | 6          | 16505062    
    ll_cache:u         | 122281412  | 344        | 3617823962  
    ll_cache_miss:u    | 1093       | 41         | 3565953251  
combined_orders:
    id        | modules                                                                                                
    ----------+--------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld1_pshuf_p128_lp1_r1000+mix_b128_ld2_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p524288_lp4_r1000
    shuffle   | mix_b128_ld2_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p524288_lp4_r1000+mix_b128_ld1_pshuf_p128_lp1_r1000
    sum       | mix_b128_ld1_pshuf_p128_lp1_r1000+mix_b128_ld2_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p524288_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 460986436273 | 462130490481 | 461405253590
    instructions:u     | 6255071423   | 6255071372   | 6255193205  
    br_retired:u       | 24009251     | 24009244     | 24015148    
    br_mis_pred:u      | 6849         | 6278         | 10296       
    l1i_cache:u        | 800238009    | 799927334    | 798370140   
    l1i_cache_refill:u | 542454       | 552173       | 293136      
    l1i_tlb:u          | 800238009    | 799927334    | 798370140   
    l1i_tlb_refill:u   | 1048         | 1021         | 675         
    l2i_cache:u        | 545683       | 555128       | 296523      
    l2i_cache_refill:u | 46497        | 46579        | 16242       
    l2i_tlb:u          | 1104         | 1967         | 1832        
    l2i_tlb_refill:u   | 1044         | 1017         | 610         
    l1d_cache:u        | 2215346169   | 2215095175   | 2215397644  
    l1d_cache_refill:u | 1915120539   | 1916399202   | 1915724779  
    l1d_tlb:u          | 4114353052   | 4117004323   | 4112360568  
    l1d_tlb_refill:u   | 1868757031   | 1868291209   | 1868359583  
    l2d_cache:u        | 7580772038   | 7596022154   | 7573642907  
    l2d_cache_refill:u | 3740407925   | 3758812276   | 3742047286  
    l2d_tlb:u          | 1868840636   | 1868367988   | 1868441128  
    l2d_tlb_refill:u   | 17135369     | 20522421     | 16505086    
    ll_cache:u         | 3739226257   | 3755578423   | 3740105718  
    ll_cache_miss:u    | 3567983172   | 3566602233   | 3565954385  

== combo_021_s3 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b64_ld4_xpage_p1_lp4_r1000       
    s1 | mix_b128_ld4_xpage_p1_lp1_r1000      
    s2 | mix_b128_ld14_indir_p524288_lp1_r1000
single_counts:
    metric             | s0         | s1         | s2          
    -------------------+------------+------------+-------------
    cpu-cycles:u       | 1042974554 | 2067412292 | 452819806534
    instructions:u     | 1061064023 | 2085064020 | 2085065405  
    br_retired:u       | 8004983    | 8004980    | 8005248     
    br_mis_pred:u      | 2310       | 2430       | 4151        
    l1i_cache:u        | 138065997  | 265112106  | 267231777   
    l1i_cache_refill:u | 868        | 2159       | 284635      
    l1i_tlb:u          | 138065997  | 265112106  | 267231777   
    l1i_tlb_refill:u   | 39         | 45         | 585         
    l2i_cache:u        | 866        | 2175       | 288167      
    l2i_cache_refill:u | 539        | 642        | 13663       
    l2i_tlb:u          | 211        | 115        | 761         
    l2i_tlb_refill:u   | 14         | 14         | 582         
    l1d_cache:u        | 269039313  | 525082658  | 1805309348  
    l1d_cache_refill:u | 239        | 177        | 1791495142  
    l1d_tlb:u          | 269086158  | 525136352  | 3568597400  
    l1d_tlb_refill:u   | 74         | 89         | 1738804278  
    l2d_cache:u        | 1878       | 2994       | 7115216924  
    l2d_cache_refill:u | 893        | 936        | 3613967334  
    l2d_tlb:u          | 129        | 112        | 1738881424  
    l2d_tlb_refill:u   | 3          | 3          | 17827168    
    ll_cache:u         | 317        | 316        | 3613371552  
    ll_cache_miss:u    | 49         | 42         | 3600415917  
combined_orders:
    id        | modules                                                                                             
    ----------+-----------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld4_xpage_p1_lp4_r1000+mix_b128_ld4_xpage_p1_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000
    shuffle   | mix_b128_ld4_xpage_p1_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000+mix_b64_ld4_xpage_p1_lp4_r1000
    sum       | mix_b64_ld4_xpage_p1_lp4_r1000+mix_b128_ld4_xpage_p1_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 455476603104 | 455522844197 | 455930193380
    instructions:u     | 5231071338   | 5231071338   | 5231193448  
    br_retired:u       | 24009240     | 24009240     | 24015211    
    br_mis_pred:u      | 7754         | 7362         | 8891        
    l1i_cache:u        | 672227307    | 672235523    | 670409880   
    l1i_cache_refill:u | 605476       | 606103       | 287662      
    l1i_tlb:u          | 672227307    | 672235523    | 670409880   
    l1i_tlb_refill:u   | 947          | 898          | 669         
    l2i_cache:u        | 605785       | 606439       | 291208      
    l2i_cache_refill:u | 71281        | 69551        | 14844       
    l2i_tlb:u          | 1027         | 1724         | 1087        
    l2i_tlb_refill:u   | 942          | 891          | 610         
    l1d_cache:u        | 2599403490   | 2599412682   | 2599431319  
    l1d_cache_refill:u | 1793417003   | 1791556045   | 1791495558  
    l1d_tlb:u          | 4366898044   | 4364866157   | 4362819910  
    l1d_tlb_refill:u   | 1739647401   | 1738736657   | 1738804441  
    l2d_cache:u        | 7124073520   | 7118839551   | 7115221796  
    l2d_cache_refill:u | 3618951101   | 3614199370   | 3613969163  
    l2d_tlb:u          | 1739721616   | 1738814512   | 1738881665  
    l2d_tlb_refill:u   | 18303935     | 20030015     | 17827174    
    ll_cache:u         | 3618299704   | 3613543311   | 3613372185  
    ll_cache_miss:u    | 3603361550   | 3600582532   | 3600416008  

== combo_022_s3 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld1_xpage_p512_lp1_r1000   
    s1 | mix_b64_ld1_pshuf_p524288_lp4_r1000
    s2 | mix_b128_ld7_xpage_p512_lp1_r1000  
single_counts:
    metric             | s0         | s1         | s2         
    -------------------+------------+------------+------------
    cpu-cycles:u       | 2977470466 | 3765484727 | 37929336346
    instructions:u     | 1061063795 | 1061063801 | 2085065099 
    br_retired:u       | 8004922    | 8004920    | 8005196    
    br_mis_pred:u      | 2363       | 2259       | 3515       
    l1i_cache:u        | 137121158  | 138309820  | 265454558  
    l1i_cache_refill:u | 1512       | 2031       | 28372      
    l1i_tlb:u          | 137121158  | 138309820  | 265454558  
    l1i_tlb_refill:u   | 50         | 39         | 44         
    l2i_cache:u        | 1510       | 2034       | 28556      
    l2i_cache_refill:u | 623        | 1011       | 1624       
    l2i_tlb:u          | 91         | 79         | 96         
    l2i_tlb_refill:u   | 25         | 37         | 29         
    l1d_cache:u        | 77051719   | 77128989   | 909368613  
    l1d_cache_refill:u | 63999559   | 23008197   | 895963522  
    l1d_tlb:u          | 148646265  | 77351019   | 1812479977 
    l1d_tlb_refill:u   | 66005975   | 49847      | 898270186  
    l2d_cache:u        | 252756465  | 271212119  | 3539673705 
    l2d_cache_refill:u | 128055830  | 128720506  | 1788393084 
    l2d_tlb:u          | 66006306   | 49915      | 898293389  
    l2d_tlb_refill:u   | 170        | 30090      | 332        
    ll_cache:u         | 128053680  | 128702987  | 1788375614 
    ll_cache_miss:u    | 1781       | 105835163  | 134283     
combined_orders:
    id        | modules                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld1_xpage_p512_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp4_r1000+mix_b128_ld7_xpage_p512_lp1_r1000
    shuffle   | mix_b64_ld1_xpage_p512_lp1_r1000+mix_b128_ld7_xpage_p512_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp4_r1000
    sum       | mix_b64_ld1_xpage_p512_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp4_r1000+mix_b128_ld7_xpage_p512_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 53280462081 | 55552886426 | 44672291539
    instructions:u     | 4207071032  | 4207071043  | 4207192695 
    br_retired:u       | 24009187    | 24009190    | 24015038   
    br_mis_pred:u      | 8649        | 7619        | 8137       
    l1i_cache:u        | 541118628   | 541041095   | 540885536  
    l1i_cache_refill:u | 106330      | 102998      | 31915      
    l1i_tlb:u          | 541118628   | 541041095   | 540885536  
    l1i_tlb_refill:u   | 434         | 391         | 133        
    l2i_cache:u        | 106425      | 103097      | 32100      
    l2i_cache_refill:u | 17016       | 16456       | 3258       
    l2i_tlb:u          | 803         | 968         | 266        
    l2i_tlb_refill:u   | 430         | 387         | 91         
    l1d_cache:u        | 1063626527  | 1063413794  | 1063549321 
    l1d_cache_refill:u | 983054836   | 986088190   | 982971278  
    l1d_tlb:u          | 2038868051  | 2043136541  | 2038477261 
    l1d_tlb_refill:u   | 964444120   | 966298077   | 964326008  
    l2d_cache:u        | 4079427687  | 4082035792  | 4063642289 
    l2d_cache_refill:u | 2059314460  | 2061287697  | 2045169420 
    l2d_tlb:u          | 964483677   | 966336644   | 964349610  
    l2d_tlb_refill:u   | 388646      | 331898      | 30592      
    ll_cache:u         | 2059225834  | 2061186171  | 2045132281 
    ll_cache_miss:u    | 113824562   | 113154084   | 105971227  

== combo_023_s3 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld14_indir_p512_lp4_r1000   
    s1 | mix_b128_ld7_xpage_p524288_lp4_r1000
    s2 | mix_b128_ld1_lin_p1_lp4_r1000       
single_counts:
    metric             | s0          | s1           | s2        
    -------------------+-------------+--------------+-----------
    cpu-cycles:u       | 38575134460 | 225886403199 | 530115251 
    instructions:u     | 1061065123  | 2085065120   | 2085064023
    br_retired:u       | 8005199     | 8005208      | 8004983   
    br_mis_pred:u      | 3027        | 4297         | 2268      
    l1i_cache:u        | 140017938   | 268217264    | 266042823 
    l1i_cache_refill:u | 13458       | 167707       | 1220      
    l1i_tlb:u          | 140017938   | 268217264    | 266042823 
    l1i_tlb_refill:u   | 46          | 530          | 36        
    l2i_cache:u        | 13472       | 169243       | 1221      
    l2i_cache_refill:u | 1694        | 7564         | 595       
    l2i_tlb:u          | 104         | 711          | 75        
    l2i_tlb_refill:u   | 25          | 525          | 11        
    l1d_cache:u        | 911108020   | 911049983    | 141033835 
    l1d_cache_refill:u | 891050334   | 897664762    | 157       
    l1d_tlb:u          | 1771475739  | 1800105636   | 141047852 
    l1d_tlb_refill:u   | 851483132   | 871419426    | 72        
    l2d_cache:u        | 3423810319  | 3570282050   | 1677      
    l2d_cache_refill:u | 1643023115  | 1814065552   | 953       
    l2d_tlb:u          | 851588705   | 871504247    | 100       
    l2d_tlb_refill:u   | 288         | 10310170     | 6         
    ll_cache:u         | 1642965927  | 1813434642   | 306       
    ll_cache_miss:u    | 8536506     | 1806325276   | 73        
combined_orders:
    id        | modules                                                                                             
    ----------+-----------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_indir_p512_lp4_r1000+mix_b128_ld7_xpage_p524288_lp4_r1000+mix_b128_ld1_lin_p1_lp4_r1000
    shuffle   | mix_b128_ld1_lin_p1_lp4_r1000+mix_b64_ld14_indir_p512_lp4_r1000+mix_b128_ld7_xpage_p524288_lp4_r1000
    sum       | mix_b64_ld14_indir_p512_lp4_r1000+mix_b128_ld7_xpage_p524288_lp4_r1000+mix_b128_ld1_lin_p1_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 274990870411 | 275073771269 | 264991652910
    instructions:u     | 5231071306   | 5231071325   | 5231194266  
    br_retired:u       | 24009235     | 24009237     | 24015390    
    br_mis_pred:u      | 8287         | 10268        | 9592        
    l1i_cache:u        | 679884654    | 680030777    | 674278025   
    l1i_cache_refill:u | 354535       | 352362       | 182385      
    l1i_tlb:u          | 679884654    | 680030777    | 674278025   
    l1i_tlb_refill:u   | 794          | 859          | 612         
    l2i_cache:u        | 355701       | 353155       | 183936      
    l2i_cache_refill:u | 25119        | 26642        | 9853        
    l2i_tlb:u          | 1562         | 1112         | 890         
    l2i_tlb_refill:u   | 788          | 856          | 561         
    l1d_cache:u        | 1965745539   | 1965974204   | 1963191838  
    l1d_cache_refill:u | 1790395798   | 1790347776   | 1788715253  
    l1d_tlb:u          | 3718084977   | 3718763952   | 3712629227  
    l1d_tlb_refill:u   | 1724977612   | 1725229711   | 1722902630  
    l2d_cache:u        | 7010444132   | 7001792871   | 6994094046  
    l2d_cache_refill:u | 3467589100   | 3463751222   | 3457089620  
    l2d_tlb:u          | 1725225591   | 1725488482   | 1723093052  
    l2d_tlb_refill:u   | 9778372      | 9776516      | 10310464    
    ll_cache:u         | 3467127560   | 3463299753   | 3456400875  
    ll_cache_miss:u    | 1887875835   | 1888317781   | 1814861855  

== combo_024_s3 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b64_ld7_xpage_p128_lp4_r1000 
    s1 | mix_b64_ld14_indir_p512_lp1_r1000
    s2 | mix_b128_ld4_lin_p1_lp4_r1000    
single_counts:
    metric             | s0          | s1          | s2        
    -------------------+-------------+-------------+-----------
    cpu-cycles:u       | 10183049321 | 39903638048 | 2067400697
    instructions:u     | 1061063795  | 1061065053  | 2085064023
    br_retired:u       | 8004922     | 8005190     | 8004983   
    br_mis_pred:u      | 2513        | 3260        | 2435      
    l1i_cache:u        | 137716026   | 138979927   | 265111632 
    l1i_cache_refill:u | 3914        | 13037       | 2180      
    l1i_tlb:u          | 137716026   | 138979927   | 265111632 
    l1i_tlb_refill:u   | 52          | 54          | 49        
    l2i_cache:u        | 3922        | 13069       | 2196      
    l2i_cache_refill:u | 767         | 1456        | 661       
    l2i_tlb:u          | 108         | 122         | 109       
    l2i_tlb_refill:u   | 35          | 48          | 15        
    l1d_cache:u        | 461572536   | 911053332   | 525083288 
    l1d_cache_refill:u | 436740344   | 897380783   | 185       
    l1d_tlb:u          | 917420477   | 1818211275  | 525136990 
    l1d_tlb_refill:u   | 450402520   | 899636670   | 85        
    l2d_cache:u        | 1223208786  | 3544442543  | 3202      
    l2d_cache_refill:u | 278704012   | 1795941308  | 1031      
    l2d_tlb:u          | 450491706   | 899798964   | 171       
    l2d_tlb_refill:u   | 32          | 469         | 22        
    ll_cache:u         | 278700219   | 1795921986  | 343       
    ll_cache_miss:u    | 856396      | 106517      | 55        
combined_orders:
    id        | modules                                                                                         
    ----------+-------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_xpage_p128_lp4_r1000+mix_b64_ld14_indir_p512_lp1_r1000+mix_b128_ld4_lin_p1_lp4_r1000
    shuffle   | mix_b128_ld4_lin_p1_lp4_r1000+mix_b64_ld7_xpage_p128_lp4_r1000+mix_b64_ld14_indir_p512_lp1_r1000
    sum       | mix_b64_ld7_xpage_p128_lp4_r1000+mix_b64_ld14_indir_p512_lp1_r1000+mix_b128_ld4_lin_p1_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 54282688916 | 56094610610 | 52154088066
    instructions:u     | 4207071107  | 4207071013  | 4207192871 
    br_retired:u       | 24009197    | 24009185    | 24015095   
    br_mis_pred:u      | 8049        | 8193        | 8208       
    l1i_cache:u        | 544616522   | 543533984   | 541807585  
    l1i_cache_refill:u | 76823       | 84047       | 19131      
    l1i_tlb:u          | 544616522   | 543533984   | 541807585  
    l1i_tlb_refill:u   | 50          | 47          | 155        
    l2i_cache:u        | 76951       | 84201       | 19187      
    l2i_cache_refill:u | 6826        | 7261        | 2884       
    l2i_tlb:u          | 154         | 182         | 339        
    l2i_tlb_refill:u   | 34          | 30          | 98         
    l1d_cache:u        | 1898119739  | 1897654194  | 1897709156 
    l1d_cache_refill:u | 1334307850  | 1332435731  | 1334121312 
    l1d_tlb:u          | 3261937960  | 3260771895  | 3260768742 
    l1d_tlb_refill:u   | 1350405417  | 1350055637  | 1350039275 
    l2d_cache:u        | 4831412427  | 4781953369  | 4767654531 
    l2d_cache_refill:u | 2124698040  | 2089479053  | 2074646351 
    l2d_tlb:u          | 1350671397  | 1350326736  | 1350290841 
    l2d_tlb_refill:u   | 2230        | 5387        | 523        
    ll_cache:u         | 2124670037  | 2089447901  | 2074622548 
    ll_cache_miss:u    | 5659918     | 7072188     | 962968     

== combo_025_s3 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b64_ld4_pshuf_p1_lp4_r1000       
    s1 | mix_b128_ld14_indir_p524288_lp4_r1000
    s2 | mix_b64_ld14_pshuf_p512_lp4_r1000    
single_counts:
    metric             | s0         | s1           | s2         
    -------------------+------------+--------------+------------
    cpu-cycles:u       | 1043129953 | 456702258797 | 31777405616
    instructions:u     | 1061064029 | 2085065362   | 1061065024 
    br_retired:u       | 8004981    | 8005243      | 8005186    
    br_mis_pred:u      | 1909       | 4186         | 3445       
    l1i_cache:u        | 137079720  | 267095535    | 139476475  
    l1i_cache_refill:u | 917        | 277462       | 10584      
    l1i_tlb:u          | 137079720  | 267095535    | 139476475  
    l1i_tlb_refill:u   | 37         | 589          | 43         
    l2i_cache:u        | 918        | 279935       | 10606      
    l2i_cache_refill:u | 537        | 13426        | 4678       
    l2i_tlb:u          | 198        | 759          | 92         
    l2i_tlb_refill:u   | 10         | 584          | 23         
    l1d_cache:u        | 269044942  | 1805279319   | 910723656  
    l1d_cache_refill:u | 153        | 1792354251   | 330006420  
    l1d_tlb:u          | 269083335  | 3566770256   | 1243553200 
    l1d_tlb_refill:u   | 71         | 1738280692   | 226345229  
    l2d_cache:u        | 1602       | 7192300573   | 3420498211 
    l2d_cache_refill:u | 808        | 3618087449   | 1520886095 
    l2d_tlb:u          | 140        | 1738359485   | 226387215  
    l2d_tlb_refill:u   | 5          | 16532350     | 299        
    ll_cache:u         | 269        | 3615483167   | 1520723309 
    ll_cache_miss:u    | 30         | 3563766308   | 11004234   
combined_orders:
    id        | modules                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld4_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p524288_lp4_r1000+mix_b64_ld14_pshuf_p512_lp4_r1000
    shuffle   | mix_b128_ld14_indir_p524288_lp4_r1000+mix_b64_ld14_pshuf_p512_lp4_r1000+mix_b64_ld4_pshuf_p1_lp4_r1000
    sum       | mix_b64_ld4_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p524288_lp4_r1000+mix_b64_ld14_pshuf_p512_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 489016889882 | 489324275861 | 489522794366
    instructions:u     | 4207071352   | 4207071423   | 4207194415  
    br_retired:u       | 24009242     | 24009251     | 24015410    
    br_mis_pred:u      | 15557        | 14372        | 9540        
    l1i_cache:u        | 543632157    | 543664365    | 543651730   
    l1i_cache_refill:u | 391175       | 399302       | 288963      
    l1i_tlb:u          | 543632157    | 543664365    | 543651730   
    l1i_tlb_refill:u   | 789          | 779          | 669         
    l2i_cache:u        | 392741       | 401379       | 291459      
    l2i_cache_refill:u | 47904        | 52366        | 18641       
    l2i_tlb:u          | 1784         | 1169         | 1049        
    l2i_tlb_refill:u   | 785          | 773          | 617         
    l1d_cache:u        | 2983116210   | 2985006805   | 2985047917  
    l1d_cache_refill:u | 2134755299   | 2133948627   | 2122360824  
    l1d_tlb:u          | 5080787630   | 5079140480   | 5079406791  
    l1d_tlb_refill:u   | 1964046129   | 1964853632   | 1964625992  
    l2d_cache:u        | 10512602682  | 10507557358  | 10612800386 
    l2d_cache_refill:u | 5107870139   | 5110357077   | 5138974352  
    l2d_tlb:u          | 1964244272   | 1965057598   | 1964746840  
    l2d_tlb_refill:u   | 22016597     | 16817758     | 16532654    
    ll_cache:u         | 5105546737   | 5108018292   | 5136206745  
    ll_cache_miss:u    | 3735853780   | 3742975060   | 3574770572  

== combo_026_s3 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld2_lin_p512_lp4_r1000  
    s1 | mix_b64_ld2_pshuf_p128_lp4_r1000 
    s2 | mix_b128_ld4_pshuf_p128_lp4_r1000
single_counts:
    metric             | s0         | s1         | s2        
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 7886464874 | 2420760809 | 9515793637
    instructions:u     | 2085063801 | 1061064023 | 2085063801
    br_retired:u       | 8004920    | 8004983    | 8004920   
    br_mis_pred:u      | 2779       | 2007       | 2682      
    l1i_cache:u        | 266474343  | 138308510  | 265688432 
    l1i_cache_refill:u | 6323       | 1376       | 8272      
    l1i_tlb:u          | 266474343  | 138308510  | 265688432 
    l1i_tlb_refill:u   | 50         | 41         | 45        
    l2i_cache:u        | 6333       | 1379       | 8307      
    l2i_cache_refill:u | 1535       | 597        | 777       
    l2i_tlb:u          | 95         | 343        | 1041      
    l2i_tlb_refill:u   | 30         | 14         | 17        
    l1d_cache:u        | 269302358  | 141152790  | 525342146 
    l1d_cache_refill:u | 70039793   | 48706357   | 169123585 
    l1d_tlb:u          | 355137397  | 201172188  | 720034908 
    l1d_tlb_refill:u   | 66039247   | 35020148   | 130000093 
    l2d_cache:u        | 880803839  | 423270476  | 1759290716
    l2d_cache_refill:u | 451132562  | 75800048   | 321097140 
    l2d_tlb:u          | 66040701   | 35062386   | 130027472 
    l2d_tlb_refill:u   | 739        | 17         | 80        
    ll_cache:u         | 451077177  | 75795257   | 321073700 
    ll_cache_miss:u    | 41389828   | 57687      | 4402319   
combined_orders:
    id        | modules                                                                                           
    ----------+---------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld2_lin_p512_lp4_r1000+mix_b64_ld2_pshuf_p128_lp4_r1000+mix_b128_ld4_pshuf_p128_lp4_r1000
    shuffle   | mix_b64_ld2_pshuf_p128_lp4_r1000+mix_b128_ld2_lin_p512_lp4_r1000+mix_b128_ld4_pshuf_p128_lp4_r1000
    sum       | mix_b128_ld2_lin_p512_lp4_r1000+mix_b64_ld2_pshuf_p128_lp4_r1000+mix_b128_ld4_pshuf_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 24613092606 | 19913920474 | 19823019320
    instructions:u     | 5231070009  | 5231069786  | 5231191625 
    br_retired:u       | 24008975    | 24008921    | 24014823   
    br_mis_pred:u      | 8209        | 8292        | 7468       
    l1i_cache:u        | 670648507   | 671044559   | 670471285  
    l1i_cache_refill:u | 90613       | 78014       | 15971      
    l1i_tlb:u          | 670648507   | 671044559   | 670471285  
    l1i_tlb_refill:u   | 60          | 47          | 136        
    l2i_cache:u        | 90701       | 78105       | 16019      
    l2i_cache_refill:u | 16623       | 14619       | 2909       
    l2i_tlb:u          | 106         | 299         | 1479       
    l2i_tlb_refill:u   | 49          | 34          | 61         
    l1d_cache:u        | 935900032   | 935758153   | 935797294  
    l1d_cache_refill:u | 286541414   | 285812500   | 287869735  
    l1d_tlb:u          | 1284603758  | 1278153199  | 1276344493 
    l1d_tlb_refill:u   | 230057586   | 230059058   | 231059488  
    l2d_cache:u        | 2966519431  | 2904953101  | 3063365031 
    l2d_cache_refill:u | 819067844   | 802509910   | 848029750  
    l2d_tlb:u          | 230213067   | 230133154   | 231130559  
    l2d_tlb_refill:u   | 2191        | 2160        | 836        
    ll_cache:u         | 818988018   | 802430111   | 847946134  
    ll_cache_miss:u    | 24821273    | 27584039    | 45849834   

== combo_027_s3 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b64_ld2_pshuf_p128_lp4_r1000 
    s1 | mix_b64_ld14_pshuf_p512_lp1_r1000
    s2 | mix_b128_ld4_indir_p128_lp4_r1000
single_counts:
    metric             | s0         | s1          | s2         
    -------------------+------------+-------------+------------
    cpu-cycles:u       | 2103617423 | 37650255538 | 10497848631
    instructions:u     | 1061064023 | 1061065096  | 2085063795 
    br_retired:u       | 8004983    | 8005195     | 8004922    
    br_mis_pred:u      | 2065       | 3139        | 2184       
    l1i_cache:u        | 138251612  | 138905806   | 266897433  
    l1i_cache_refill:u | 1333       | 14720       | 8308       
    l1i_tlb:u          | 138251612  | 138905806   | 266897433  
    l1i_tlb_refill:u   | 48         | 45          | 45         
    l2i_cache:u        | 1336       | 14755       | 8325       
    l2i_cache_refill:u | 630        | 1249        | 902        
    l2i_tlb:u          | 135        | 119         | 149        
    l2i_tlb_refill:u   | 13         | 33          | 13         
    l1d_cache:u        | 141109725  | 911013713   | 525457903  
    l1d_cache_refill:u | 47468629   | 895415652   | 478214468  
    l1d_tlb:u          | 193573946  | 1818044916  | 955566576  
    l1d_tlb_refill:u   | 34010106   | 899602026   | 421153253  
    l2d_cache:u        | 426896065  | 3551860772  | 1265273923 
    l2d_cache_refill:u | 62973323   | 1785669936  | 245582414  
    l2d_tlb:u          | 34023270   | 899766724   | 421250760  
    l2d_tlb_refill:u   | 65         | 339         | 16         
    ll_cache:u         | 62970381   | 1785651577  | 245577712  
    ll_cache_miss:u    | 119208     | 107234      | 11803      
combined_orders:
    id        | modules                                                                                             
    ----------+-----------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld2_pshuf_p128_lp4_r1000+mix_b64_ld14_pshuf_p512_lp1_r1000+mix_b128_ld4_indir_p128_lp4_r1000
    shuffle   | mix_b128_ld4_indir_p128_lp4_r1000+mix_b64_ld2_pshuf_p128_lp4_r1000+mix_b64_ld14_pshuf_p512_lp1_r1000
    sum       | mix_b64_ld2_pshuf_p128_lp4_r1000+mix_b64_ld14_pshuf_p512_lp1_r1000+mix_b128_ld4_indir_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 54214681356 | 56933802256 | 50251721592
    instructions:u     | 4207071037  | 4207071013  | 4207192914 
    br_retired:u       | 24009188    | 24009185    | 24015100   
    br_mis_pred:u      | 8771        | 8174        | 7388       
    l1i_cache:u        | 546451660   | 546349468   | 544054851  
    l1i_cache_refill:u | 79575       | 90954       | 24361      
    l1i_tlb:u          | 546451660   | 546349468   | 544054851  
    l1i_tlb_refill:u   | 50          | 47          | 138        
    l2i_cache:u        | 79749       | 91093       | 24416      
    l2i_cache_refill:u | 10294       | 8727        | 2781       
    l2i_tlb:u          | 134         | 280         | 403        
    l2i_tlb_refill:u   | 43          | 33          | 59         
    l1d_cache:u        | 1577585772  | 1577739291  | 1577581341 
    l1d_cache_refill:u | 1413472043  | 1415018575  | 1421098749 
    l1d_tlb:u          | 2965624952  | 2965390654  | 2967185438 
    l1d_tlb_refill:u   | 1352718305  | 1352858577  | 1354765385 
    l2d_cache:u        | 5328167220  | 5162082704  | 5244030760 
    l2d_cache_refill:u | 2159374554  | 2016839019  | 2094225673 
    l2d_tlb:u          | 1353060794  | 1353389314  | 1355040754 
    l2d_tlb_refill:u   | 6337        | 4091        | 420        
    ll_cache:u         | 2159335813  | 2016811737  | 2094199670 
    ll_cache_miss:u    | 6922302     | 8603885     | 238245     

== combo_028_s3 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b64_ld4_lin_p524288_lp4_r1000
    s1 | mix_b64_ld1_xpage_p128_lp4_r1000 
    s2 | mix_b128_ld7_lin_p128_lp1_r1000  
single_counts:
    metric             | s0          | s1         | s2         
    -------------------+-------------+------------+------------
    cpu-cycles:u       | 26160226362 | 1363855283 | 23564307417
    instructions:u     | 1061065006  | 1061064029 | 2085064012 
    br_retired:u       | 8005184     | 8004981    | 8004978    
    br_mis_pred:u      | 3286        | 1957       | 3261       
    l1i_cache:u        | 137390512   | 138155476  | 265895293  
    l1i_cache_refill:u | 9678        | 1126       | 18514      
    l1i_tlb:u          | 137390512   | 138155476  | 265895293  
    l1i_tlb_refill:u   | 204         | 42         | 46         
    l2i_cache:u        | 9716        | 1130       | 18655      
    l2i_cache_refill:u | 3228        | 579        | 1171       
    l2i_tlb:u          | 524         | 457        | 212        
    l2i_tlb_refill:u   | 200         | 14         | 17         
    l1d_cache:u        | 269201195   | 77073697   | 909501614  
    l1d_cache_refill:u | 68806881    | 60380194   | 859676493  
    l1d_tlb:u          | 269806479   | 149891479  | 1813109931 
    l1d_tlb_refill:u   | 206056      | 66012869   | 898323212  
    l2d_cache:u        | 862449177   | 158870431  | 2312053380 
    l2d_cache_refill:u | 462609520   | 25756718   | 518576941  
    l2d_tlb:u          | 216120      | 66073952   | 898413200  
    l2d_tlb_refill:u   | 140888      | 99         | 28         
    ll_cache:u         | 462492704   | 25756012   | 518574561  
    ll_cache_miss:u    | 436117854   | 17163      | 22698      
combined_orders:
    id        | modules                                                                                           
    ----------+---------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld4_lin_p524288_lp4_r1000+mix_b64_ld1_xpage_p128_lp4_r1000+mix_b128_ld7_lin_p128_lp1_r1000
    shuffle   | mix_b64_ld1_xpage_p128_lp4_r1000+mix_b128_ld7_lin_p128_lp1_r1000+mix_b64_ld4_lin_p524288_lp4_r1000
    sum       | mix_b64_ld4_lin_p524288_lp4_r1000+mix_b64_ld1_xpage_p128_lp4_r1000+mix_b128_ld7_lin_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 53495817219 | 53844498901 | 51088389062
    instructions:u     | 4207071010  | 4207070983  | 4207193047 
    br_retired:u       | 24009184    | 24009180    | 24015143   
    br_mis_pred:u      | 7641        | 8167        | 8504       
    l1i_cache:u        | 540994441   | 541402224   | 541441281  
    l1i_cache_refill:u | 96008       | 94537       | 29318      
    l1i_tlb:u          | 540994441   | 541402224   | 541441281  
    l1i_tlb_refill:u   | 434         | 466         | 292        
    l2i_cache:u        | 96063       | 94648       | 29501      
    l2i_cache_refill:u | 24516       | 21988       | 4978       
    l2i_tlb:u          | 1052        | 694         | 1193       
    l2i_tlb_refill:u   | 430         | 461         | 231        
    l1d_cache:u        | 1255896402  | 1255655523  | 1255776506 
    l1d_cache_refill:u | 988951693   | 992105782   | 988863568  
    l1d_tlb:u          | 2233164845  | 2232213779  | 2232807889 
    l1d_tlb_refill:u   | 964696590   | 964526417   | 964542137  
    l2d_cache:u        | 3498456195  | 3376924077  | 3333372988 
    l2d_cache_refill:u | 1167690376  | 1046590265  | 1006943179 
    l2d_tlb:u          | 964735059   | 964603199   | 964703272  
    l2d_tlb_refill:u   | 214821      | 214684      | 141015     
    ll_cache:u         | 1167536254  | 1046445064  | 1006823277 
    ll_cache_miss:u    | 444725638   | 443231277   | 436157715  

== combo_029_s3 ==
single_modules:
    id | module                          
    ---+---------------------------------
    s0 | mix_b128_ld4_lin_p128_lp4_r1000 
    s1 | mix_b64_ld2_indir_p128_lp1_r1000
    s2 | mix_b64_ld7_indir_p512_lp1_r1000
single_counts:
    metric             | s0         | s1         | s2         
    -------------------+------------+------------+------------
    cpu-cycles:u       | 8501302720 | 3585997455 | 18966518985
    instructions:u     | 2085063795 | 1061063801 | 1061063801 
    br_retired:u       | 8004922    | 8004920    | 8004920    
    br_mis_pred:u      | 2687       | 2546       | 3421       
    l1i_cache:u        | 266569256  | 137086927  | 138240930  
    l1i_cache_refill:u | 7152       | 1788       | 6660       
    l1i_tlb:u          | 266569256  | 137086927  | 138240930  
    l1i_tlb_refill:u   | 44         | 44         | 46         
    l2i_cache:u        | 7202       | 1793       | 6670       
    l2i_cache_refill:u | 929        | 570        | 943        
    l2i_tlb:u          | 803        | 107        | 206        
    l2i_tlb_refill:u   | 13         | 17         | 27         
    l1d_cache:u        | 525370980  | 141205769  | 461189622  
    l1d_cache_refill:u | 130974963  | 123311089  | 446534855  
    l1d_tlb:u          | 693201726  | 281272131  | 915938722  
    l1d_tlb_refill:u   | 130000096  | 131000150  | 450125652  
    l2d_cache:u        | 1482770217 | 359416040  | 1796075921 
    l2d_cache_refill:u | 360255451  | 103247787  | 901453940  
    l2d_tlb:u          | 130114707  | 131438172  | 450137503  
    l2d_tlb_refill:u   | 27         | 11         | 587        
    ll_cache:u         | 360234586  | 103246562  | 901443668  
    ll_cache_miss:u    | 543283     | 777        | 6427031    
combined_orders:
    id        | modules                                                                                          
    ----------+--------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld4_lin_p128_lp4_r1000+mix_b64_ld2_indir_p128_lp1_r1000+mix_b64_ld7_indir_p512_lp1_r1000
    shuffle   | mix_b64_ld2_indir_p128_lp1_r1000+mix_b64_ld7_indir_p512_lp1_r1000+mix_b128_ld4_lin_p128_lp4_r1000
    sum       | mix_b128_ld4_lin_p128_lp4_r1000+mix_b64_ld2_indir_p128_lp1_r1000+mix_b64_ld7_indir_p512_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 40165356136 | 39127122246 | 31053819160
    instructions:u     | 4207071044  | 4207071060  | 4207191397 
    br_retired:u       | 24009189    | 24009190    | 24014762   
    br_mis_pred:u      | 9517        | 7995        | 8654       
    l1i_cache:u        | 544010384   | 544041314   | 541897113  
    l1i_cache_refill:u | 82698       | 75019       | 15600      
    l1i_tlb:u          | 544010384   | 544041314   | 541897113  
    l1i_tlb_refill:u   | 56          | 49          | 134        
    l2i_cache:u        | 82791       | 75105       | 15665      
    l2i_cache_refill:u | 9931        | 10442       | 2442       
    l2i_tlb:u          | 138         | 260         | 1116       
    l2i_tlb_refill:u   | 38          | 39          | 57         
    l1d_cache:u        | 1127694357  | 1127680015  | 1127766371 
    l1d_cache_refill:u | 694150619   | 691979557   | 700820907  
    l1d_tlb:u          | 1900655981  | 1892374415  | 1890412579 
    l1d_tlb_refill:u   | 710137601   | 710121932   | 711125898  
    l2d_cache:u        | 3732102748  | 3739795658  | 3638262178 
    l2d_cache_refill:u | 1416342264  | 1366187608  | 1364957178 
    l2d_tlb:u          | 710253703   | 710514647   | 711690382  
    l2d_tlb_refill:u   | 3060        | 3267        | 625        
    ll_cache:u         | 1416286873  | 1366143195  | 1364924816 
    ll_cache_miss:u    | 53875931    | 60835553    | 6971091    

== combo_030_s3 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld7_pshuf_p512_lp1_r1000    
    s1 | mix_b128_ld1_xpage_p524288_lp1_r1000
    s2 | mix_b128_ld7_xpage_p1_lp4_r1000     
single_counts:
    metric             | s0          | s1          | s2        
    -------------------+-------------+-------------+-----------
    cpu-cycles:u       | 19055839196 | 32359327856 | 3602119837
    instructions:u     | 1061063795  | 2085065099  | 2085063801
    br_retired:u       | 8004922     | 8005196     | 8004920   
    br_mis_pred:u      | 3298        | 3612        | 2703      
    l1i_cache:u        | 138216490   | 265513521   | 265060060 
    l1i_cache_refill:u | 6845        | 30991       | 3436      
    l1i_tlb:u          | 138216490   | 265513521   | 265060060 
    l1i_tlb_refill:u   | 44          | 259         | 44        
    l2i_cache:u        | 6857        | 31061       | 3438      
    l2i_cache_refill:u | 868         | 1615        | 638       
    l2i_tlb:u          | 94          | 726         | 86        
    l2i_tlb_refill:u   | 17          | 255         | 14        
    l1d_cache:u        | 461158549   | 141182744   | 909038393 
    l1d_cache_refill:u | 446378778   | 127061336   | 180       
    l1d_tlb:u          | 915710953   | 275573403   | 909085297 
    l1d_tlb_refill:u   | 450100165   | 126142329   | 90        
    l2d_cache:u        | 1794958322  | 548545231   | 3727      
    l2d_cache_refill:u | 905845560   | 293768761   | 911       
    l2d_tlb:u          | 450110602   | 126179594   | 116       
    l2d_tlb_refill:u   | 254         | 1150245     | 4         
    ll_cache:u         | 905835200   | 293677151   | 274       
    ll_cache_miss:u    | 8459118     | 285888932   | 18        
combined_orders:
    id        | modules                                                                                              
    ----------+------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_pshuf_p512_lp1_r1000+mix_b128_ld1_xpage_p524288_lp1_r1000+mix_b128_ld7_xpage_p1_lp4_r1000
    shuffle   | mix_b128_ld7_xpage_p1_lp4_r1000+mix_b128_ld1_xpage_p524288_lp1_r1000+mix_b64_ld7_pshuf_p512_lp1_r1000
    sum       | mix_b64_ld7_pshuf_p512_lp1_r1000+mix_b128_ld1_xpage_p524288_lp1_r1000+mix_b128_ld7_xpage_p1_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 54756338429 | 54888904494 | 55017286889
    instructions:u     | 5231071016  | 5231071016  | 5231192695 
    br_retired:u       | 24009186    | 24009186    | 24015038   
    br_mis_pred:u      | 7785        | 8700        | 9613       
    l1i_cache:u        | 670987131   | 670997557   | 668790071  
    l1i_cache_refill:u | 119060      | 113611      | 41272      
    l1i_tlb:u          | 670987131   | 670997557   | 668790071  
    l1i_tlb_refill:u   | 452         | 477         | 347        
    l2i_cache:u        | 119209      | 113784      | 41356      
    l2i_cache_refill:u | 13974       | 12755       | 3121       
    l2i_tlb:u          | 756         | 870         | 906        
    l2i_tlb_refill:u   | 446         | 472         | 286        
    l1d_cache:u        | 1511336979  | 1511330819  | 1511379686 
    l1d_cache_refill:u | 574949075   | 574109643   | 573440294  
    l1d_tlb:u          | 2102113558  | 2102387281  | 2100369653 
    l1d_tlb_refill:u   | 576265567   | 576216338   | 576242584  
    l2d_cache:u        | 2319291016  | 2336489944  | 2343507280 
    l2d_cache_refill:u | 1186704819  | 1195061469  | 1199615232 
    l2d_tlb:u          | 576312655   | 576263204   | 576290312  
    l2d_tlb_refill:u   | 3255646     | 3607208     | 1150503    
    ll_cache:u         | 1186564591  | 1194921079  | 1199512625 
    ll_cache_miss:u    | 284858666   | 292631317   | 294348068  

== combo_031_s3 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld2_xpage_p512_lp1_r1000   
    s1 | mix_b64_ld4_pshuf_p524288_lp1_r1000
    s2 | mix_b128_ld7_lin_p128_lp1_r1000    
single_counts:
    metric             | s0         | s1          | s2         
    -------------------+------------+-------------+------------
    cpu-cycles:u       | 5831153080 | 11093493165 | 22018821045
    instructions:u     | 1061063801 | 1061063795  | 2085064018 
    br_retired:u       | 8004920    | 8004922     | 8004976    
    br_mis_pred:u      | 2694       | 2787        | 3245       
    l1i_cache:u        | 137099676  | 138813313   | 265889090  
    l1i_cache_refill:u | 2532       | 5012        | 16965      
    l1i_tlb:u          | 137099676  | 138813313   | 265889090  
    l1i_tlb_refill:u   | 47         | 119         | 53         
    l2i_cache:u        | 2539       | 5024        | 17045      
    l2i_cache_refill:u | 619        | 1028        | 1252       
    l2i_tlb:u          | 101        | 229         | 131        
    l2i_tlb_refill:u   | 28         | 116         | 17         
    l1d_cache:u        | 141062671  | 269406249   | 909579102  
    l1d_cache_refill:u | 127545899  | 48322967    | 864831379  
    l1d_tlb:u          | 277273754  | 271458841   | 1813380122 
    l1d_tlb_refill:u   | 130015643  | 788051      | 898382653  
    l2d_cache:u        | 514141886  | 1148698921  | 2350144229 
    l2d_cache_refill:u | 255842576  | 478504262   | 556769602  
    l2d_tlb:u          | 130022980  | 792726      | 898636139  
    l2d_tlb_refill:u   | 194        | 480819      | 24         
    ll_cache:u         | 255839348  | 478216290   | 556764477  
    ll_cache_miss:u    | 1684       | 436725361   | 20888      
combined_orders:
    id        | modules                                                                                             
    ----------+-----------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld2_xpage_p512_lp1_r1000+mix_b64_ld4_pshuf_p524288_lp1_r1000+mix_b128_ld7_lin_p128_lp1_r1000
    shuffle   | mix_b64_ld4_pshuf_p524288_lp1_r1000+mix_b64_ld2_xpage_p512_lp1_r1000+mix_b128_ld7_lin_p128_lp1_r1000
    sum       | mix_b64_ld2_xpage_p512_lp1_r1000+mix_b64_ld4_pshuf_p524288_lp1_r1000+mix_b128_ld7_lin_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 42749335043 | 41055784875 | 38943467290
    instructions:u     | 4207071067  | 4207071023  | 4207191614 
    br_retired:u       | 24009193    | 24009187    | 24014818   
    br_mis_pred:u      | 8294        | 8463        | 8726       
    l1i_cache:u        | 541752409   | 541449485   | 541802079  
    l1i_cache_refill:u | 89710       | 90105       | 24509      
    l1i_tlb:u          | 541752409   | 541449485   | 541802079  
    l1i_tlb_refill:u   | 378         | 378         | 219        
    l2i_cache:u        | 89819       | 90216       | 24608      
    l2i_cache_refill:u | 6644        | 5926        | 2899       
    l2i_tlb:u          | 849         | 952         | 461        
    l2i_tlb_refill:u   | 376         | 374         | 161        
    l1d_cache:u        | 1319825505  | 1320638308  | 1320048022 
    l1d_cache_refill:u | 1045514425  | 1041020560  | 1040700245 
    l1d_tlb:u          | 2363124153  | 2364584479  | 2362112717 
    l1d_tlb_refill:u   | 1029021883  | 1029643695  | 1029186347 
    l2d_cache:u        | 4218310278  | 4140191386  | 4012985036 
    l2d_cache_refill:u | 1508296058  | 1414459974  | 1291116440 
    l2d_tlb:u          | 1029054265  | 1029768860  | 1029451845 
    l2d_tlb_refill:u   | 1173102     | 1178371     | 481037     
    ll_cache:u         | 1508022934  | 1414157809  | 1290820115 
    ll_cache_miss:u    | 430805524   | 433727243   | 436747933  

== combo_032_s3 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld7_indir_p524288_lp1_r1000
    s1 | mix_b128_ld4_indir_p524288_lp1_r1000
    s2 | mix_b64_ld14_xpage_p524288_lp4_r1000
single_counts:
    metric             | s0           | s1           | s2          
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 226349917250 | 129397037771 | 225888436043
    instructions:u     | 2085065163   | 2085065100   | 1061065144  
    br_retired:u       | 8005213      | 8005197      | 8005211     
    br_mis_pred:u      | 3894         | 2819         | 3543        
    l1i_cache:u        | 270110975    | 270661994    | 137841406   
    l1i_cache_refill:u | 170935       | 100043       | 66917       
    l1i_tlb:u          | 270110975    | 270661994    | 137841406   
    l1i_tlb_refill:u   | 596          | 463          | 417         
    l2i_cache:u        | 172536       | 100772       | 67053       
    l2i_cache_refill:u | 6369         | 4098         | 6412        
    l2i_tlb:u          | 691          | 518          | 491         
    l2i_tlb_refill:u   | 593          | 459          | 412         
    l1d_cache:u        | 910894946    | 526872572    | 909321190   
    l1d_cache_refill:u | 896926601    | 512806698    | 896047713   
    l1d_tlb:u          | 1799877560   | 1042951020   | 1796753784  
    l1d_tlb_refill:u   | 871534112    | 499344326    | 870423201   
    l2d_cache:u        | 3565714596   | 2037715489   | 3563803602  
    l2d_cache_refill:u | 1811101573   | 1035458649   | 1810871934  
    l2d_tlb:u          | 871618386    | 499655038    | 870475677   
    l2d_tlb_refill:u   | 10246152     | 4976106      | 10208412    
    ll_cache:u         | 1810800518   | 1035285331   | 1810451492  
    ll_cache_miss:u    | 1801792895   | 1029165729   | 1806387610  
combined_orders:
    id        | modules                                                                                                       
    ----------+---------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld7_indir_p524288_lp1_r1000+mix_b128_ld4_indir_p524288_lp1_r1000+mix_b64_ld14_xpage_p524288_lp4_r1000
    shuffle   | mix_b64_ld14_xpage_p524288_lp4_r1000+mix_b128_ld4_indir_p524288_lp1_r1000+mix_b128_ld7_indir_p524288_lp1_r1000
    sum       | mix_b128_ld7_indir_p524288_lp1_r1000+mix_b128_ld4_indir_p524288_lp1_r1000+mix_b64_ld14_xpage_p524288_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 581670048327 | 582001249606 | 581635391064
    instructions:u     | 5231071349   | 5231071342   | 5231195407  
    br_retired:u       | 24009241     | 24009239     | 24015621    
    br_mis_pred:u      | 9176         | 9479         | 10256       
    l1i_cache:u        | 673677144    | 680574320    | 678614375   
    l1i_cache_refill:u | 675185       | 671643       | 337895      
    l1i_tlb:u          | 673677144    | 680574320    | 678614375   
    l1i_tlb_refill:u   | 2275         | 2298         | 1476        
    l2i_cache:u        | 676816       | 673110       | 340361      
    l2i_cache_refill:u | 65582        | 60930        | 16879       
    l2i_tlb:u          | 2686         | 2710         | 1700        
    l2i_tlb_refill:u   | 2269         | 2293         | 1464        
    l1d_cache:u        | 2350239577   | 2350172323   | 2347088708  
    l1d_cache_refill:u | 2307926034   | 2307927908   | 2305781012  
    l1d_tlb:u          | 4650801646   | 4653908615   | 4639582364  
    l1d_tlb_refill:u   | 2243441551   | 2243480179   | 2241301639  
    l2d_cache:u        | 9182203950   | 9186161799   | 9167233687  
    l2d_cache_refill:u | 4663322029   | 4663656487   | 4657432156  
    l2d_tlb:u          | 2243963236   | 2243975304   | 2241749101  
    l2d_tlb_refill:u   | 29414305     | 32661166     | 25430670    
    ll_cache:u         | 4662171570   | 4662648876   | 4656537341  
    ll_cache_miss:u    | 4639722813   | 4639407855   | 4637346234  

== combo_033_s3 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld4_pshuf_p524288_lp1_r1000
    s1 | mix_b64_ld2_pshuf_p1_lp4_r1000      
    s2 | mix_b128_ld14_indir_p128_lp4_r1000  
single_counts:
    metric             | s0          | s1         | s2         
    -------------------+-------------+------------+------------
    cpu-cycles:u       | 22021481135 | 530953840  | 34510478807
    instructions:u     | 2085064018  | 1061064023 | 2085065130 
    br_retired:u       | 8004976     | 8004983    | 8005201    
    br_mis_pred:u      | 3030        | 2353       | 3053       
    l1i_cache:u        | 267421536   | 138086005  | 266855757  
    l1i_cache_refill:u | 26905       | 722        | 25246      
    l1i_tlb:u          | 267421536   | 138086005  | 266855757  
    l1i_tlb_refill:u   | 211         | 37         | 60         
    l2i_cache:u        | 26958       | 725        | 25343      
    l2i_cache_refill:u | 1388        | 522        | 1821       
    l2i_tlb:u          | 640         | 164        | 135        
    l2i_tlb_refill:u   | 208         | 10         | 23         
    l1d_cache:u        | 525319170   | 141052820  | 1805104445 
    l1d_cache_refill:u | 96513124    | 168        | 1668384787 
    l1d_tlb:u          | 529293719   | 141102165  | 3282814425 
    l1d_tlb_refill:u   | 1573831     | 68         | 1462095456 
    l2d_cache:u        | 2249823213  | 1345       | 4310620368 
    l2d_cache_refill:u | 928644887   | 774        | 782359559  
    l2d_tlb:u          | 1582599     | 90         | 1462110819 
    l2d_tlb_refill:u   | 958533      | 3          | 24         
    ll_cache:u         | 928097133   | 236        | 782347554  
    ll_cache_miss:u    | 845744225   | 26         | 65295      
combined_orders:
    id        | modules                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld4_pshuf_p524288_lp1_r1000+mix_b64_ld2_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p128_lp4_r1000
    shuffle   | mix_b128_ld14_indir_p128_lp4_r1000+mix_b64_ld2_pshuf_p1_lp4_r1000+mix_b128_ld4_pshuf_p524288_lp1_r1000
    sum       | mix_b128_ld4_pshuf_p524288_lp1_r1000+mix_b64_ld2_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 63450636730 | 60599755548 | 57062913782
    instructions:u     | 5231071080  | 5231071134  | 5231193171 
    br_retired:u       | 24009193    | 24009201    | 24015160   
    br_mis_pred:u      | 8053        | 7856        | 8436       
    l1i_cache:u        | 671874132   | 673725640   | 672363298  
    l1i_cache_refill:u | 165207      | 161695      | 52873      
    l1i_tlb:u          | 671874132   | 673725640   | 672363298  
    l1i_tlb_refill:u   | 525         | 524         | 308        
    l2i_cache:u        | 165369      | 161853      | 53026      
    l2i_cache_refill:u | 11145       | 14174       | 3731       
    l2i_tlb:u          | 1180        | 891         | 939        
    l2i_tlb_refill:u   | 520         | 519         | 241        
    l1d_cache:u        | 2471293289  | 2473725894  | 2471476435 
    l1d_cache_refill:u | 1767044534  | 1764294298  | 1764898079 
    l1d_tlb:u          | 3957509318  | 3965297931  | 3953210309 
    l1d_tlb_refill:u   | 1464034318  | 1464934030  | 1463669355 
    l2d_cache:u        | 6644626188  | 6781043579  | 6560444926 
    l2d_cache_refill:u | 1796663310  | 1943479240  | 1711005220 
    l2d_tlb:u          | 1464060852  | 1465013343  | 1463693508 
    l2d_tlb_refill:u   | 1169495     | 1171250     | 958560     
    ll_cache:u         | 1796033966  | 1943881322  | 1710444923 
    ll_cache_miss:u    | 857625272   | 853383149   | 845809546  

== combo_034_s4 ==
single_modules:
    id | module                        
    ---+-------------------------------
    s0 | mix_b64_ld7_lin_p128_lp4_r1000
    s1 | mix_b64_ld2_lin_p512_lp4_r1000
    s2 | mix_b64_ld2_lin_p512_lp4_r1000
    s3 | mix_b64_ld2_lin_p128_lp1_r1000
single_counts:
    metric             | s0         | s1         | s2         | s3        
    -------------------+------------+------------+------------+-----------
    cpu-cycles:u       | 7245519356 | 5909012607 | 4434158663 | 3252432144
    instructions:u     | 1061063795 | 1061063801 | 1061063801 | 1061063801
    br_retired:u       | 8004922    | 8004920    | 8004920    | 8004920   
    br_mis_pred:u      | 2112       | 2157       | 2261       | 2539      
    l1i_cache:u        | 137848715  | 137534817  | 138381086  | 138086113 
    l1i_cache_refill:u | 2830       | 2356       | 1943       | 1509      
    l1i_tlb:u          | 137848715  | 137534817  | 138381086  | 138086113 
    l1i_tlb_refill:u   | 45         | 42         | 44         | 41        
    l2i_cache:u        | 2833       | 2358       | 1944       | 1510      
    l2i_cache_refill:u | 1256       | 1254       | 1084       | 559       
    l2i_tlb:u          | 1061       | 308        | 89         | 528       
    l2i_tlb_refill:u   | 15         | 22         | 19         | 14        
    l1d_cache:u        | 461333341  | 141194220  | 141224624  | 141057626 
    l1d_cache_refill:u | 110179215  | 36800710   | 36346869   | 121202072 
    l1d_tlb:u          | 619260919  | 183787005  | 187341782  | 276704551 
    l1d_tlb_refill:u   | 114000147  | 34022187   | 35026218   | 130000167 
    l2d_cache:u        | 1406369892 | 387725859  | 383104516  | 355187422 
    l2d_cache_refill:u | 258650242  | 200219320  | 200536865  | 90102470  
    l2d_tlb:u          | 114058162  | 34024509   | 35027865   | 130006394 
    l2d_tlb_refill:u   | 16         | 144        | 577        | 34        
    ll_cache:u         | 258633701  | 200196614  | 200513880  | 90101384  
    ll_cache_miss:u    | 1956371    | 1120382    | 936438     | 404       
combined_orders:
    id        | modules                                                                                                                    
    ----------+----------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_lin_p128_lp4_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld2_lin_p128_lp1_r1000
    shuffle   | mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld7_lin_p128_lp4_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld2_lin_p128_lp1_r1000
    sum       | mix_b64_ld7_lin_p128_lp4_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld2_lin_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 25205131168 | 25491308282 | 20841122770
    instructions:u     | 4244073018  | 4244073018  | 4244255198 
    br_retired:u       | 32010976    | 32010976    | 32019682   
    br_mis_pred:u      | 10502       | 10409       | 9069       
    l1i_cache:u        | 551955577   | 551880961   | 551850731  
    l1i_cache_refill:u | 48440       | 50312       | 8638       
    l1i_tlb:u          | 551955577   | 551880961   | 551850731  
    l1i_tlb_refill:u   | 48          | 60          | 172        
    l2i_cache:u        | 48485       | 50391       | 8645       
    l2i_cache_refill:u | 6502        | 7732        | 4153       
    l2i_tlb:u          | 163         | 163         | 1986       
    l2i_tlb_refill:u   | 45          | 46          | 70         
    l1d_cache:u        | 884957719   | 885100330   | 884809811  
    l1d_cache_refill:u | 305117165   | 305119065   | 304528866  
    l1d_tlb:u          | 1263559042  | 1279313960  | 1267094257 
    l1d_tlb_refill:u   | 312045555   | 316063551   | 313048719  
    l2d_cache:u        | 2519269502  | 2539669808  | 2532387689 
    l2d_cache_refill:u | 856857588   | 975033522   | 749508897  
    l2d_tlb:u          | 312586086   | 316184764   | 313116930  
    l2d_tlb_refill:u   | 693565      | 695430      | 771        
    ll_cache:u         | 856744982   | 974890790   | 749445579  
    ll_cache_miss:u    | 90309574    | 205888763   | 4013595    

== combo_035_s4 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld14_pshuf_p128_lp4_r1000  
    s1 | mix_b128_ld14_pshuf_p1_lp4_r1000   
    s2 | mix_b128_ld2_lin_p1_lp4_r1000      
    s3 | mix_b64_ld1_pshuf_p524288_lp1_r1000
single_counts:
    metric             | s0          | s1         | s2         | s3        
    -------------------+-------------+------------+------------+-----------
    cpu-cycles:u       | 15180780315 | 7186305567 | 1042115792 | 2667073346
    instructions:u     | 1061063801  | 2085063801 | 2085064023 | 1061063801
    br_retired:u       | 8004920     | 8004920    | 8004983    | 8004920   
    br_mis_pred:u      | 3032        | 2986       | 2903       | 2074      
    l1i_cache:u        | 138848719   | 265065938  | 266056171  | 137303630 
    l1i_cache_refill:u | 5572        | 6081       | 1301       | 1551      
    l1i_tlb:u          | 138848719   | 265065938  | 266056171  | 137303630 
    l1i_tlb_refill:u   | 44          | 46         | 43         | 45        
    l2i_cache:u        | 5578        | 6099       | 1304       | 1553      
    l2i_cache_refill:u | 2449        | 633        | 602        | 630       
    l2i_tlb:u          | 125         | 106        | 624        | 284       
    l2i_tlb_refill:u   | 11          | 14         | 13         | 40        
    l1d_cache:u        | 909216363   | 1805039221 | 269037478  | 77106916  
    l1d_cache_refill:u | 314956073   | 272        | 182        | 12448404  
    l1d_tlb:u          | 1242060886  | 1805086957 | 269070842  | 77744393  
    l1d_tlb_refill:u   | 226032324   | 123        | 74         | 197833    
    l2d_cache:u        | 2749628055  | 6569       | 2172       | 274115683 
    l2d_cache_refill:u | 330502240   | 990        | 959        | 113567293 
    l2d_tlb:u          | 226098792   | 145        | 110        | 197906    
    l2d_tlb_refill:u   | 15          | 6          | 26         | 117981    
    ll_cache:u         | 330483522   | 312        | 276        | 113502398 
    ll_cache_miss:u    | 2027742     | 85         | 33         | 104215203 
combined_orders:
    id        | modules                                                                                                                             
    ----------+-------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_pshuf_p128_lp4_r1000+mix_b128_ld14_pshuf_p1_lp4_r1000+mix_b128_ld2_lin_p1_lp4_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000
    shuffle   | mix_b64_ld14_pshuf_p128_lp4_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000+mix_b128_ld14_pshuf_p1_lp4_r1000+mix_b128_ld2_lin_p1_lp4_r1000
    sum       | mix_b64_ld14_pshuf_p128_lp4_r1000+mix_b128_ld14_pshuf_p1_lp4_r1000+mix_b128_ld2_lin_p1_lp4_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 26999972485 | 26662487303 | 26076275020
    instructions:u     | 6292073982  | 6292074052  | 6292255426 
    br_retired:u       | 32011181    | 32011190    | 32019743   
    br_mis_pred:u      | 9108        | 6350        | 10995      
    l1i_cache:u        | 809403131   | 809247877   | 807274458  
    l1i_cache_refill:u | 122763      | 122933      | 14505      
    l1i_tlb:u          | 809403131   | 809247877   | 807274458  
    l1i_tlb_refill:u   | 379         | 373         | 178        
    l2i_cache:u        | 123203      | 123271      | 14534      
    l2i_cache_refill:u | 14908       | 13971       | 4314       
    l2i_tlb:u          | 956         | 815         | 1139       
    l2i_tlb_refill:u   | 373         | 366         | 78         
    l1d_cache:u        | 3061056072  | 3061059376  | 3060399978 
    l1d_cache_refill:u | 320118293   | 332117929   | 327404931  
    l1d_tlb:u          | 3399580062  | 3390600485  | 3393963078 
    l1d_tlb_refill:u   | 226398719   | 226383910   | 226230354  
    l2d_cache:u        | 3032725874  | 3105064248  | 3023752479 
    l2d_cache_refill:u | 445317225   | 552135476   | 444071482  
    l2d_tlb:u          | 226428175   | 226457300   | 226296953  
    l2d_tlb_refill:u   | 173856      | 175438      | 118028     
    ll_cache:u         | 445189788   | 551987775   | 443986508  
    ll_cache_miss:u    | 195616278   | 219637008   | 106243063  

== combo_036_s4 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld7_xpage_p512_lp1_r1000
    s1 | mix_b128_ld7_indir_p1_lp4_r1000  
    s2 | mix_b64_ld2_indir_p128_lp1_r1000 
    s3 | mix_b128_ld2_pshuf_p128_lp4_r1000
single_counts:
    metric             | s0          | s1         | s2         | s3        
    -------------------+-------------+------------+------------+-----------
    cpu-cycles:u       | 37674703100 | 3602109661 | 3580073868 | 4668702724
    instructions:u     | 2085065130  | 2085063801 | 1061063795 | 2085063808
    br_retired:u       | 8005201     | 8004920    | 8004922    | 8004922   
    br_mis_pred:u      | 3439        | 2540       | 2534       | 2581      
    l1i_cache:u        | 266472807   | 266061438  | 138094246  | 265146207 
    l1i_cache_refill:u | 29243       | 3311       | 1804       | 4261      
    l1i_tlb:u          | 266472807   | 266061438  | 138094246  | 265146207 
    l1i_tlb_refill:u   | 46          | 42         | 55         | 44        
    l2i_cache:u        | 29429       | 3333       | 1804       | 4283      
    l2i_cache_refill:u | 1654        | 600        | 620        | 726       
    l2i_tlb:u          | 95          | 82         | 111        | 91        
    l2i_tlb_refill:u   | 27          | 12         | 16         | 18        
    l1d_cache:u        | 909372140   | 909038140  | 141057820  | 269120768 
    l1d_cache_refill:u | 896104779   | 170        | 121084710  | 87858002  
    l1d_tlb:u          | 1812602636  | 909086333  | 277062865  | 378534099 
    l1d_tlb_refill:u   | 898272165   | 92         | 130000123  | 67013797  
    l2d_cache:u        | 3538197474  | 4145       | 367472062  | 843366244 
    l2d_cache_refill:u | 1794007562  | 932        | 102353961  | 146509161 
    l2d_tlb:u          | 898296918   | 167        | 130456784  | 67083418  
    l2d_tlb_refill:u   | 296         | 5          | 33         | 127       
    ll_cache:u         | 1793993882  | 303        | 102352591  | 146503107 
    ll_cache_miss:u    | 81256       | 71         | 565        | 2123521   
combined_orders:
    id        | modules                                                                                                                             
    ----------+-------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld7_xpage_p512_lp1_r1000+mix_b128_ld7_indir_p1_lp4_r1000+mix_b64_ld2_indir_p128_lp1_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000
    shuffle   | mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b128_ld7_xpage_p512_lp1_r1000+mix_b64_ld2_indir_p128_lp1_r1000+mix_b128_ld7_indir_p1_lp4_r1000
    sum       | mix_b128_ld7_xpage_p512_lp1_r1000+mix_b128_ld7_indir_p1_lp4_r1000+mix_b64_ld2_indir_p128_lp1_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 54751053088 | 52714131649 | 49525589353
    instructions:u     | 7316074065  | 7316074089  | 7316256534 
    br_retired:u       | 32011191    | 32011194    | 32019965   
    br_mis_pred:u      | 9620        | 8523        | 11094      
    l1i_cache:u        | 936023761   | 935990500   | 935774698  
    l1i_cache_refill:u | 194790      | 178063      | 38619      
    l1i_tlb:u          | 936023761   | 935990500   | 935774698  
    l1i_tlb_refill:u   | 51          | 53          | 187        
    l2i_cache:u        | 195233      | 178859      | 38849      
    l2i_cache_refill:u | 15737       | 15648       | 3600       
    l2i_tlb:u          | 123         | 107         | 379        
    l2i_tlb_refill:u   | 41          | 42          | 73         
    l1d_cache:u        | 2228583873  | 2228622750  | 2228588868 
    l1d_cache_refill:u | 1109025093  | 1109901927  | 1105047661 
    l1d_tlb:u          | 3365161063  | 3364955328  | 3377285933 
    l1d_tlb_refill:u   | 1094307880  | 1094365393  | 1095286177 
    l2d_cache:u        | 4766915306  | 4816647529  | 4749039925 
    l2d_cache_refill:u | 2058336990  | 2084284929  | 2042871616 
    l2d_tlb:u          | 1094363304  | 1094785677  | 1095837287 
    l2d_tlb_refill:u   | 5347        | 13184       | 461        
    ll_cache:u         | 2058292129  | 2084239569  | 2042849883 
    ll_cache_miss:u    | 33700345    | 5047360     | 2205413    

== combo_037_s4 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld4_pshuf_p524288_lp4_r1000
    s1 | mix_b64_ld1_lin_p128_lp4_r1000     
    s2 | mix_b128_ld2_xpage_p512_lp1_r1000  
    s3 | mix_b64_ld14_indir_p1_lp4_r1000    
single_counts:
    metric             | s0          | s1         | s2          | s3        
    -------------------+-------------+------------+-------------+-----------
    cpu-cycles:u       | 20759656308 | 1217870344 | 11374344668 | 3602153898
    instructions:u     | 1061063808  | 1061064023 | 2085063795  | 1061063795
    br_retired:u       | 8004922     | 8004983    | 8004922     | 8004922   
    br_mis_pred:u      | 2785        | 2011       | 3185        | 2561      
    l1i_cache:u        | 137798300   | 138165911  | 266133637   | 137057227 
    l1i_cache_refill:u | 7855        | 1050       | 9568        | 1823      
    l1i_tlb:u          | 137798300   | 138165911  | 266133637   | 137057227 
    l1i_tlb_refill:u   | 180         | 45         | 47          | 47        
    l2i_cache:u        | 7864        | 1051       | 9614        | 1825      
    l2i_cache_refill:u | 3243        | 579        | 850         | 542       
    l2i_tlb:u          | 303         | 793        | 99          | 96        
    l2i_tlb_refill:u   | 176         | 11         | 31          | 17        
    l1d_cache:u        | 269458589   | 77060341   | 269071162   | 909037873 
    l1d_cache_refill:u | 116202901   | 14717266   | 253926113   | 183       
    l1d_tlb:u          | 270160533   | 104426249  | 532884636   | 909084560 
    l1d_tlb_refill:u   | 204068      | 17000159   | 258020869   | 92        
    l2d_cache:u        | 964663243   | 174122536  | 1056026183  | 2647      
    l2d_cache_refill:u | 473457100   | 39410102   | 521644385   | 905       
    l2d_tlb:u          | 212585      | 17000258   | 258028147   | 129       
    l2d_tlb_refill:u   | 136900      | 21         | 260         | 6         
    ll_cache:u         | 473369555   | 39407418   | 521635583   | 344       
    ll_cache_miss:u    | 402077842   | 31961      | 7927195     | 58        
combined_orders:
    id        | modules                                                                                                                             
    ----------+-------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld4_pshuf_p524288_lp4_r1000+mix_b64_ld1_lin_p128_lp4_r1000+mix_b128_ld2_xpage_p512_lp1_r1000+mix_b64_ld14_indir_p1_lp4_r1000
    shuffle   | mix_b64_ld14_indir_p1_lp4_r1000+mix_b128_ld2_xpage_p512_lp1_r1000+mix_b64_ld4_pshuf_p524288_lp4_r1000+mix_b64_ld1_lin_p128_lp4_r1000
    sum       | mix_b64_ld4_pshuf_p524288_lp4_r1000+mix_b64_ld1_lin_p128_lp4_r1000+mix_b128_ld2_xpage_p512_lp1_r1000+mix_b64_ld14_indir_p1_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 37202724287 | 36986233839 | 36954025218
    instructions:u     | 5268074080  | 5268074056  | 5268255421 
    br_retired:u       | 32011194    | 32011191    | 32019749   
    br_mis_pred:u      | 9517        | 8243        | 10542      
    l1i_cache:u        | 679279940   | 680319047   | 679155075  
    l1i_cache_refill:u | 100070      | 93586       | 20296      
    l1i_tlb:u          | 679279940   | 680319047   | 679155075  
    l1i_tlb_refill:u   | 379         | 409         | 319        
    l2i_cache:u        | 100151      | 93665       | 20354      
    l2i_cache_refill:u | 21372       | 19231       | 5214       
    l2i_tlb:u          | 857         | 774         | 1291       
    l2i_tlb_refill:u   | 374         | 403         | 235        
    l1d_cache:u        | 1524555471  | 1524566238  | 1524627965 
    l1d_cache_refill:u | 389745059   | 391888626   | 384846463  
    l1d_tlb:u          | 1813020666  | 1812912265  | 1816555978 
    l1d_tlb_refill:u   | 275235240   | 275223258   | 275225188  
    l2d_cache:u        | 2149403251  | 2118479293  | 2194814609 
    l2d_cache_refill:u | 1018856553  | 1027192336  | 1034512492 
    l2d_tlb:u          | 275257099   | 275240135   | 275241119  
    l2d_tlb_refill:u   | 378089      | 375117      | 137187     
    ll_cache:u         | 1018711552  | 1027064797  | 1034412900 
    ll_cache_miss:u    | 413714940   | 413897269   | 410037056  

== combo_038_s4 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b64_ld1_lin_p524288_lp1_r1000 
    s1 | mix_b128_ld14_xpage_p512_lp1_r1000
    s2 | mix_b64_ld1_indir_p512_lp1_r1000  
    s3 | mix_b64_ld2_pshuf_p512_lp4_r1000  
single_counts:
    metric             | s0         | s1          | s2         | s3        
    -------------------+------------+-------------+------------+-----------
    cpu-cycles:u       | 2714147125 | 74113196722 | 2864175315 | 5084537751
    instructions:u     | 1061063801 | 2085065046  | 1061063795 | 1061063795
    br_retired:u       | 8004920    | 8005189     | 8004922    | 8004922   
    br_mis_pred:u      | 2064       | 3218        | 2471       | 2623      
    l1i_cache:u        | 138308076  | 268427667   | 137086747  | 138187401 
    l1i_cache_refill:u | 1435       | 53392       | 1813       | 2151      
    l1i_tlb:u          | 138308076  | 268427667   | 137086747  | 138187401 
    l1i_tlb_refill:u   | 45         | 45          | 40         | 38        
    l2i_cache:u        | 1437       | 53713       | 1822       | 2159      
    l2i_cache_refill:u | 585        | 2388        | 592        | 1136      
    l2i_tlb:u          | 581        | 106         | 88         | 386       
    l2i_tlb_refill:u   | 41         | 22          | 22         | 22        
    l1d_cache:u        | 77105626   | 1808564611  | 77051789   | 141206607 
    l1d_cache_refill:u | 12156211   | 1794441596  | 64000741   | 65993733  
    l1d_tlb:u          | 77773157   | 3614516931  | 148606973  | 192608475 
    l1d_tlb_refill:u   | 203488     | 1796849659  | 66005945   | 34021464  
    l2d_cache:u        | 273114020  | 7086464163  | 252703532  | 410778775 
    l2d_cache_refill:u | 111747984  | 3592389321  | 128049332  | 180476133 
    l2d_tlb:u          | 203542     | 1797114057  | 66006265   | 34023179  
    l2d_tlb_refill:u   | 118199     | 490         | 209        | 183       
    ll_cache:u         | 111682687  | 3592348806  | 128047207  | 180464739 
    ll_cache_miss:u    | 102012174  | 145114      | 1057       | 105667    
combined_orders:
    id        | modules                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld1_lin_p524288_lp1_r1000+mix_b128_ld14_xpage_p512_lp1_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b64_ld2_pshuf_p512_lp4_r1000
    shuffle   | mix_b64_ld2_pshuf_p512_lp4_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b64_ld1_lin_p524288_lp1_r1000+mix_b128_ld14_xpage_p512_lp1_r1000
    sum       | mix_b64_ld1_lin_p524288_lp1_r1000+mix_b128_ld14_xpage_p512_lp1_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b64_ld2_pshuf_p512_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 86243022923 | 86059113451 | 84776056913
    instructions:u     | 5268074116  | 5268074071  | 5268256437 
    br_retired:u       | 32011198    | 32011193    | 32019953   
    br_mis_pred:u      | 12347       | 11522       | 10376      
    l1i_cache:u        | 683059945   | 683065639   | 682009891  
    l1i_cache_refill:u | 152246      | 155121      | 58791      
    l1i_tlb:u          | 683059945   | 683065639   | 682009891  
    l1i_tlb_refill:u   | 612         | 617         | 168        
    l2i_cache:u        | 152598      | 155502      | 59131      
    l2i_cache_refill:u | 22492       | 24641       | 4701       
    l2i_tlb:u          | 1218        | 1275        | 1161       
    l2i_tlb_refill:u   | 603         | 614         | 107        
    l1d_cache:u        | 2104445556  | 2104209003  | 2103928633 
    l1d_cache_refill:u | 1939545651  | 1937987831  | 1936592281 
    l1d_tlb:u          | 4036321377  | 4035570194  | 4033505536 
    l1d_tlb_refill:u   | 1897512770  | 1897345416  | 1897080556 
    l2d_cache:u        | 8036147483  | 8031461931  | 8023060490 
    l2d_cache_refill:u | 4028860699  | 4024065304  | 4012662770 
    l2d_tlb:u          | 1897786354  | 1897616220  | 1897347043 
    l2d_tlb_refill:u   | 1645562     | 1644202     | 119081     
    ll_cache:u         | 4028622617  | 4023842920  | 4012543439 
    ll_cache_miss:u    | 117290646   | 114686418   | 102264012  

== combo_039_s4 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b128_ld14_indir_p524288_lp4_r1000
    s1 | mix_b128_ld2_xpage_p524288_lp4_r1000 
    s2 | mix_b128_ld2_pshuf_p128_lp4_r1000    
    s3 | mix_b128_ld4_xpage_p128_lp1_r1000    
single_counts:
    metric             | s0           | s1          | s2         | s3         
    -------------------+--------------+-------------+------------+------------
    cpu-cycles:u       | 456893329039 | 64709510762 | 4531682112 | 15568930834
    instructions:u     | 2085065405   | 2085065052  | 2085063795 | 2085063795 
    br_retired:u       | 8005248      | 8005191     | 8004922    | 8004922    
    br_mis_pred:u      | 4713         | 3699        | 2759       | 2420       
    l1i_cache:u        | 267102017    | 266970343   | 265112815  | 266085186  
    l1i_cache_refill:u | 292762       | 53454       | 4674       | 12816      
    l1i_tlb:u          | 267102017    | 266970343   | 265112815  | 266085186  
    l1i_tlb_refill:u   | 590          | 367         | 45         | 46         
    l2i_cache:u        | 296144       | 53675       | 4699       | 12872      
    l2i_cache_refill:u | 15957        | 8071        | 784        | 874        
    l2i_tlb:u          | 795          | 465         | 287        | 114        
    l2i_tlb_refill:u   | 586          | 364         | 16         | 20         
    l1d_cache:u        | 1805295469   | 269622663   | 269063598  | 525611908  
    l1d_cache_refill:u | 1792644512   | 255193157   | 79424191   | 492397529  
    l1d_tlb:u          | 3564952594   | 532346052   | 373838850  | 1048590832 
    l1d_tlb_refill:u   | 1738211344   | 250436933   | 66004644   | 514241131  
    l2d_cache:u        | 7193713440   | 1108328735  | 802612287  | 1367556058 
    l2d_cache_refill:u | 3620977021   | 596668225   | 136391449  | 342708992  
    l2d_tlb:u          | 1738291486   | 250565352   | 66004898   | 514749543  
    l2d_tlb_refill:u   | 14765249     | 2714124     | 86         | 26         
    ll_cache:u         | 3619041135   | 596450629   | 136387370  | 342706775  
    ll_cache_miss:u    | 3566167875   | 584636630   | 679372     | 9688       
combined_orders:
    id        | modules                                                                                                                                       
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_indir_p524288_lp4_r1000+mix_b128_ld2_xpage_p524288_lp4_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b128_ld4_xpage_p128_lp1_r1000
    shuffle   | mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b128_ld2_xpage_p524288_lp4_r1000+mix_b128_ld4_xpage_p128_lp1_r1000+mix_b128_ld14_indir_p524288_lp4_r1000
    sum       | mix_b128_ld14_indir_p524288_lp4_r1000+mix_b128_ld2_xpage_p524288_lp4_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b128_ld4_xpage_p128_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 539443963594 | 540782072739 | 541703452747
    instructions:u     | 8340074362   | 8340074362   | 8340258047  
    br_retired:u       | 32011243     | 32011243     | 32020283    
    br_mis_pred:u      | 11137        | 10747        | 13591       
    l1i_cache:u        | 1067715062   | 1067882235   | 1065270361  
    l1i_cache_refill:u | 897280       | 860245       | 363706      
    l1i_tlb:u          | 1067715062   | 1067882235   | 1065270361  
    l1i_tlb_refill:u   | 2252         | 2293         | 1048        
    l2i_cache:u        | 900626       | 863768       | 367390      
    l2i_cache_refill:u | 129951       | 127551       | 25686       
    l2i_tlb:u          | 3096         | 2435         | 1661        
    l2i_tlb_refill:u   | 2250         | 2289         | 986         
    l1d_cache:u        | 2869493135   | 2869901958   | 2869593638  
    l1d_cache_refill:u | 2622612899   | 2628256069   | 2619659389  
    l1d_tlb:u          | 5527923186   | 5523207208   | 5519728328  
    l1d_tlb_refill:u   | 2568742804   | 2569088439   | 2568894052  
    l2d_cache:u        | 10471760486  | 10476531989  | 10472210520 
    l2d_cache_refill:u | 4656762873   | 4710147369   | 4696745687  
    l2d_tlb:u          | 2569450334   | 2569498716   | 2569611279  
    l2d_tlb_refill:u   | 27543680     | 23200385     | 17479485    
    ll_cache:u         | 4651028689   | 4707761295   | 4694585909  
    ll_cache_miss:u    | 4221746591   | 4179289821   | 4151493565  

== combo_040_s4 ==
single_modules:
    id | module                         
    ---+--------------------------------
    s0 | mix_b64_ld7_lin_p1_lp4_r1000   
    s1 | mix_b64_ld2_lin_p512_lp4_r1000 
    s2 | mix_b128_ld2_indir_p1_lp4_r1000
    s3 | mix_b64_ld7_lin_p1_lp1_r1000   
single_counts:
    metric             | s0         | s1         | s2         | s3        
    -------------------+------------+------------+------------+-----------
    cpu-cycles:u       | 1810097396 | 4381093908 | 1042107787 | 1810086750
    instructions:u     | 1061064029 | 1061063795 | 2085064023 | 1061064020
    br_retired:u       | 8004981    | 8004922    | 8004983    | 8004980   
    br_mis_pred:u      | 2439       | 2101       | 2618       | 2536      
    l1i_cache:u        | 138054474  | 138457898  | 265057366  | 137055596 
    l1i_cache_refill:u | 1299       | 2068       | 1397       | 1276      
    l1i_tlb:u          | 138054474  | 138457898  | 265057366  | 137055596 
    l1i_tlb_refill:u   | 43         | 42         | 41         | 42        
    l2i_cache:u        | 1303       | 2072       | 1401       | 1277      
    l2i_cache_refill:u | 562        | 1158       | 612        | 535       
    l2i_tlb:u          | 106        | 700        | 98         | 86        
    l2i_tlb_refill:u   | 13         | 24         | 12         | 12        
    l1d_cache:u        | 461037773  | 141203926  | 269038344  | 461037517 
    l1d_cache_refill:u | 213        | 37439668   | 187        | 171       
    l1d_tlb:u          | 461083564  | 184029315  | 269073437  | 461083326 
    l1d_tlb_refill:u   | 78         | 34023484   | 86         | 85        
    l2d_cache:u        | 1890       | 378004987  | 2437       | 2058      
    l2d_cache_refill:u | 835        | 193146890  | 1064       | 872       
    l2d_tlb:u          | 131        | 34025280   | 126        | 121       
    l2d_tlb_refill:u   | 5          | 128        | 35         | 4         
    ll_cache:u         | 267        | 193128026  | 359        | 313       
    ll_cache_miss:u    | 26         | 2109334    | 149        | 46        
combined_orders:
    id        | modules                                                                                                                 
    ----------+-------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_lin_p1_lp4_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b128_ld2_indir_p1_lp4_r1000+mix_b64_ld7_lin_p1_lp1_r1000
    shuffle   | mix_b128_ld2_indir_p1_lp4_r1000+mix_b64_ld7_lin_p1_lp1_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld7_lin_p1_lp4_r1000
    sum       | mix_b64_ld7_lin_p1_lp4_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b128_ld2_indir_p1_lp4_r1000+mix_b64_ld7_lin_p1_lp1_r1000
combined_counts:
    metric             | canonical  | shuffle    | sum       
    -------------------+------------+------------+-----------
    cpu-cycles:u       | 9205243493 | 9248680869 | 9043385841
    instructions:u     | 5268072786 | 5268072786 | 5268255867
    br_retired:u       | 32010921   | 32010921   | 32019866  
    br_mis_pred:u      | 9178       | 9389       | 9694      
    l1i_cache:u        | 678458679  | 678594143  | 678625334 
    l1i_cache_refill:u | 39840      | 40451      | 6040      
    l1i_tlb:u          | 678458679  | 678594143  | 678625334 
    l1i_tlb_refill:u   | 47         | 45         | 168       
    l2i_cache:u        | 39860      | 40479      | 6053      
    l2i_cache_refill:u | 7322       | 6284       | 2867      
    l2i_tlb:u          | 162        | 442        | 990       
    l2i_tlb_refill:u   | 33         | 33         | 61        
    l1d_cache:u        | 1332243994 | 1332187137 | 1332317560
    l1d_cache_refill:u | 36056530   | 36671323   | 37440239  
    l1d_tlb:u          | 1380299320 | 1380263677 | 1375269642
    l1d_tlb_refill:u   | 35027703   | 35022356   | 34023733  
    l2d_cache:u        | 420241671  | 425045241  | 378011372 
    l2d_cache_refill:u | 219983137  | 220657193  | 193149661 
    l2d_tlb:u          | 35032238   | 35026930   | 34025658  
    l2d_tlb_refill:u   | 320        | 242        | 172       
    ll_cache:u         | 219948648  | 220623421  | 193128965 
    ll_cache_miss:u    | 1237906    | 900509     | 2109555   

== combo_041_s4 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b128_ld2_xpage_p512_lp4_r1000 
    s1 | mix_b64_ld7_xpage_p1_lp4_r1000    
    s2 | mix_b128_ld14_xpage_p512_lp1_r1000
    s3 | mix_b64_ld2_pshuf_p1_lp4_r1000    
single_counts:
    metric             | s0          | s1         | s2          | s3        
    -------------------+-------------+------------+-------------+-----------
    cpu-cycles:u       | 14729527786 | 1810098882 | 74721453200 | 530945572 
    instructions:u     | 2085063801  | 1061064029 | 2085065143  | 1061064023
    br_retired:u       | 8004920     | 8004981    | 8005202     | 8004983   
    br_mis_pred:u      | 3210        | 2422       | 3110        | 2359      
    l1i_cache:u        | 266265477   | 138056835  | 269888246   | 138086296 
    l1i_cache_refill:u | 11502       | 1192       | 51947       | 760       
    l1i_tlb:u          | 266265477   | 138056835  | 269888246   | 138086296 
    l1i_tlb_refill:u   | 44          | 46         | 51          | 38        
    l2i_cache:u        | 11530       | 1193       | 52181       | 758       
    l2i_cache_refill:u | 1066        | 597        | 2431        | 525       
    l2i_tlb:u          | 89          | 184        | 110         | 146       
    l2i_tlb_refill:u   | 20          | 12         | 27          | 12        
    l1d_cache:u        | 269192842   | 461037851  | 1808890812  | 141052827 
    l1d_cache_refill:u | 255510167   | 180        | 1795351850  | 151       
    l1d_tlb:u          | 533334487   | 461084611  | 3619162784  | 141102558 
    l1d_tlb_refill:u   | 258079100   | 89         | 1798337870  | 70        
    l2d_cache:u        | 1090985689  | 1888       | 7101045414  | 1532      
    l2d_cache_refill:u | 533982860   | 849        | 3587700707  | 845       
    l2d_tlb:u          | 258096275   | 111        | 1798588753  | 95        
    l2d_tlb_refill:u   | 163         | 5          | 405         | 4         
    ll_cache:u         | 533967551   | 268        | 3587674275  | 291       
    ll_cache_miss:u    | 5724942     | 73         | 155121      | 34        
combined_orders:
    id        | modules                                                                                                                           
    ----------+-----------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld2_xpage_p512_lp4_r1000+mix_b64_ld7_xpage_p1_lp4_r1000+mix_b128_ld14_xpage_p512_lp1_r1000+mix_b64_ld2_pshuf_p1_lp4_r1000
    shuffle   | mix_b64_ld2_pshuf_p1_lp4_r1000+mix_b64_ld7_xpage_p1_lp4_r1000+mix_b128_ld14_xpage_p512_lp1_r1000+mix_b128_ld2_xpage_p512_lp4_r1000
    sum       | mix_b128_ld2_xpage_p512_lp4_r1000+mix_b64_ld7_xpage_p1_lp4_r1000+mix_b128_ld14_xpage_p512_lp1_r1000+mix_b64_ld2_pshuf_p1_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum        
    -------------------+--------------+--------------+------------
    cpu-cycles:u       | 101946599455 | 101123827304 | 91792025440
    instructions:u     | 6292074073   | 6292074100   | 6292256996 
    br_retired:u       | 32011193     | 32011197     | 32020086   
    br_mis_pred:u      | 7736         | 12063        | 11101      
    l1i_cache:u        | 810244668    | 810161377    | 812296854  
    l1i_cache_refill:u | 244856       | 232650       | 65401      
    l1i_tlb:u          | 810244668    | 810161377    | 812296854  
    l1i_tlb_refill:u   | 54           | 52           | 179        
    l2i_cache:u        | 245005       | 232983       | 65662      
    l2i_cache_refill:u | 21529        | 19913        | 4619       
    l2i_tlb:u          | 532          | 109          | 529        
    l2i_tlb_refill:u   | 43           | 48           | 71         
    l1d_cache:u        | 2680211312   | 2679991127   | 2680174332 
    l1d_cache_refill:u | 2051027627   | 2050267158   | 2050862348 
    l1d_tlb:u          | 4751527420   | 4751178234   | 4754684440 
    l1d_tlb_refill:u   | 2055329538   | 2055129011   | 2056417129 
    l2d_cache:u        | 8114281544   | 8131746895   | 8192034523 
    l2d_cache_refill:u | 4110822065   | 4110421646   | 4121685261 
    l2d_tlb:u          | 2055560645   | 2055347980   | 2056685234 
    l2d_tlb_refill:u   | 98286        | 103951       | 577        
    ll_cache:u         | 4110750495   | 4110367961   | 4121642385 
    ll_cache_miss:u    | 9734461      | 7806780      | 5880170    

== combo_042_s4 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld1_pshuf_p128_lp1_r1000    
    s1 | mix_b128_ld2_indir_p1_lp4_r1000     
    s2 | mix_b128_ld7_pshuf_p128_lp4_r1000   
    s3 | mix_b128_ld7_xpage_p524288_lp4_r1000
single_counts:
    metric             | s0         | s1         | s2          | s3          
    -------------------+------------+------------+-------------+-------------
    cpu-cycles:u       | 1945696621 | 1042108866 | 15644224411 | 226006019524
    instructions:u     | 1061064029 | 2085064029 | 2085063795  | 2085065109  
    br_retired:u       | 8004981    | 8004981    | 8004922     | 8005205     
    br_mis_pred:u      | 1995       | 2524       | 2354        | 4063        
    l1i_cache:u        | 138238950  | 265057202  | 267831825   | 266876150   
    l1i_cache_refill:u | 1181       | 1539       | 12063       | 169613      
    l1i_tlb:u          | 138238950  | 265057202  | 267831825   | 266876150   
    l1i_tlb_refill:u   | 40         | 43         | 41          | 526         
    l2i_cache:u        | 1182       | 1541       | 12099       | 171148      
    l2i_cache_refill:u | 560        | 612        | 2821        | 8959        
    l2i_tlb:u          | 618        | 293        | 254         | 750         
    l2i_tlb_refill:u   | 12         | 12         | 14          | 520         
    l1d_cache:u        | 77108173   | 269037388  | 910307606   | 910883596   
    l1d_cache_refill:u | 61567124   | 190        | 303602474   | 897072668   
    l1d_tlb:u          | 152014380  | 269071867  | 1254597457  | 1798771609  
    l1d_tlb_refill:u   | 67023621   | 84         | 226244911   | 871304395   
    l2d_cache:u        | 187420540  | 2126       | 2916062207  | 3566548513  
    l2d_cache_refill:u | 59335263   | 915        | 483985665   | 1812434414  
    l2d_tlb:u          | 67023879   | 109        | 226302290   | 871388257   
    l2d_tlb_refill:u   | 166        | 5          | 18          | 9280368     
    ll_cache:u         | 59334265   | 292        | 483953468   | 1812035967  
    ll_cache_miss:u    | 822        | 43         | 664811      | 1805839016  
combined_orders:
    id        | modules                                                                                                                                
    ----------+----------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld1_pshuf_p128_lp1_r1000+mix_b128_ld2_indir_p1_lp4_r1000+mix_b128_ld7_pshuf_p128_lp4_r1000+mix_b128_ld7_xpage_p524288_lp4_r1000
    shuffle   | mix_b128_ld2_indir_p1_lp4_r1000+mix_b128_ld7_pshuf_p128_lp4_r1000+mix_b128_ld7_xpage_p524288_lp4_r1000+mix_b64_ld1_pshuf_p128_lp1_r1000
    sum       | mix_b64_ld1_pshuf_p128_lp1_r1000+mix_b128_ld2_indir_p1_lp4_r1000+mix_b128_ld7_pshuf_p128_lp4_r1000+mix_b128_ld7_xpage_p524288_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 246012060487 | 245376126183 | 244638049422
    instructions:u     | 7316074163   | 7316074139   | 7316256962  
    br_retired:u       | 32011213     | 32011210     | 32020089    
    br_mis_pred:u      | 10892        | 10493        | 10936       
    l1i_cache:u        | 944035049    | 943887100    | 938004127   
    l1i_cache_refill:u | 436626       | 437302       | 184396      
    l1i_tlb:u          | 944035049    | 943887100    | 938004127   
    l1i_tlb_refill:u   | 1072         | 971          | 650         
    l2i_cache:u        | 438166       | 438740       | 185970      
    l2i_cache_refill:u | 58753        | 53430        | 12952       
    l2i_tlb:u          | 1235         | 1924         | 1915        
    l2i_tlb_refill:u   | 1063         | 965          | 558         
    l1d_cache:u        | 2169054380   | 2169217164   | 2167336763  
    l1d_cache_refill:u | 1256506071   | 1262190740   | 1262242456  
    l1d_tlb:u          | 3471454357   | 3469750142   | 3474455313  
    l1d_tlb_refill:u   | 1165259682   | 1165407623   | 1164573011  
    l2d_cache:u        | 6866592961   | 6859044936   | 6670033386  
    l2d_cache_refill:u | 2375905281   | 2438314102   | 2355756257  
    l2d_tlb:u          | 1165422436   | 1165652398   | 1164714535  
    l2d_tlb_refill:u   | 11490869     | 11345559     | 9280557     
    ll_cache:u         | 2375381183   | 2437736537   | 2355323992  
    ll_cache_miss:u    | 1924731266   | 1903888345   | 1806504692  

== combo_043_s4 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b64_ld14_xpage_p1_lp1_r1000  
    s1 | mix_b64_ld1_indir_p128_lp1_r1000 
    s2 | mix_b128_ld4_indir_p128_lp4_r1000
    s3 | mix_b128_ld1_indir_p128_lp4_r1000
single_counts:
    metric             | s0         | s1         | s2          | s3        
    -------------------+------------+------------+-------------+-----------
    cpu-cycles:u       | 3602198119 | 1746847772 | 10947479961 | 2907426345
    instructions:u     | 1061063786 | 1061064029 | 2085063801  | 2085063801
    br_retired:u       | 8004921    | 8004981    | 8004920     | 8004920   
    br_mis_pred:u      | 2532       | 1986       | 2267        | 2120      
    l1i_cache:u        | 138056170  | 137182251  | 266887591   | 265283606 
    l1i_cache_refill:u | 1836       | 1212       | 9291        | 2670      
    l1i_tlb:u          | 138056170  | 137182251  | 266887591   | 265283606 
    l1i_tlb_refill:u   | 38         | 51         | 43          | 37        
    l2i_cache:u        | 1840       | 1217       | 9316        | 2670      
    l2i_cache_refill:u | 524        | 603        | 981         | 643       
    l2i_tlb:u          | 252        | 676        | 135         | 812       
    l2i_tlb_refill:u   | 13         | 21         | 19          | 13        
    l1d_cache:u        | 909037928  | 77092579   | 525472486   | 141137362 
    l1d_cache_refill:u | 180        | 61031896   | 473665583   | 115921932 
    l1d_tlb:u          | 909084091  | 149262030  | 953945856   | 252840776 
    l1d_tlb_refill:u   | 101        | 66019466   | 419104977   | 105270942 
    l2d_cache:u        | 2462       | 183317037  | 1229564809  | 331575216 
    l2d_cache_refill:u | 813        | 51925585   | 207394236   | 69201519  
    l2d_tlb:u          | 129        | 66019804   | 419246111   | 105290368 
    l2d_tlb_refill:u   | 3          | 13         | 26          | 21        
    ll_cache:u         | 247        | 51924001   | 207389811   | 69199893  
    ll_cache_miss:u    | 32         | 363        | 2960        | 1763      
combined_orders:
    id        | modules                                                                                                                             
    ----------+-------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_xpage_p1_lp1_r1000+mix_b64_ld1_indir_p128_lp1_r1000+mix_b128_ld4_indir_p128_lp4_r1000+mix_b128_ld1_indir_p128_lp4_r1000
    shuffle   | mix_b64_ld1_indir_p128_lp1_r1000+mix_b64_ld14_xpage_p1_lp1_r1000+mix_b128_ld1_indir_p128_lp4_r1000+mix_b128_ld4_indir_p128_lp4_r1000
    sum       | mix_b64_ld14_xpage_p1_lp1_r1000+mix_b64_ld1_indir_p128_lp1_r1000+mix_b128_ld4_indir_p128_lp4_r1000+mix_b128_ld1_indir_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 20361083346 | 20776370042 | 19203952197
    instructions:u     | 6292072792  | 6292072786  | 6292255417 
    br_retired:u       | 32010919    | 32010921    | 32019742   
    br_mis_pred:u      | 9177        | 9836        | 8905       
    l1i_cache:u        | 809613422   | 809654834   | 807409618  
    l1i_cache_refill:u | 95251       | 101370      | 15009      
    l1i_tlb:u          | 809613422   | 809654834   | 807409618  
    l1i_tlb_refill:u   | 51          | 57          | 169        
    l2i_cache:u        | 95518       | 101838      | 15043      
    l2i_cache_refill:u | 6319        | 5919        | 2751       
    l2i_tlb:u          | 109         | 136         | 1875       
    l2i_tlb_refill:u   | 26          | 39          | 66         
    l1d_cache:u        | 1652760909  | 1652712827  | 1652740355 
    l1d_cache_refill:u | 649044733   | 649213316   | 650619591  
    l1d_tlb:u          | 2265259222  | 2263827150  | 2265132753 
    l1d_tlb_refill:u   | 590427976   | 590413639   | 590395486  
    l2d_cache:u        | 1879918309  | 1863854362  | 1744459524 
    l2d_cache_refill:u | 418536136   | 411411863   | 328522153  
    l2d_tlb:u          | 590704391   | 590695330   | 590556412  
    l2d_tlb_refill:u   | 186         | 162         | 63         
    ll_cache:u         | 418521326   | 411397819   | 328513952  
    ll_cache_miss:u    | 452219      | 257499      | 5118       

== combo_044_s4 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b128_ld14_pshuf_p128_lp4_r1000   
    s1 | mix_b128_ld14_pshuf_p524288_lp1_r1000
    s2 | mix_b128_ld1_pshuf_p1_lp4_r1000      
    s3 | mix_b64_ld7_pshuf_p524288_lp1_r1000  
single_counts:
    metric             | s0          | s1          | s2         | s3         
    -------------------+-------------+-------------+------------+------------
    cpu-cycles:u       | 30805895432 | 74215755722 | 530122202  | 18565142048
    instructions:u     | 2085065080  | 2085065123  | 2085064023 | 1061063795 
    br_retired:u       | 8005194     | 8005200     | 8004983    | 8004922    
    br_mis_pred:u      | 3152        | 3374        | 2279       | 2673       
    l1i_cache:u        | 267313347   | 267798054   | 266044413  | 138320459  
    l1i_cache_refill:u | 24483       | 57571       | 1038       | 7651       
    l1i_tlb:u          | 267313347   | 267798054   | 266044413  | 138320459  
    l1i_tlb_refill:u   | 48          | 365         | 39         | 160        
    l2i_cache:u        | 24665       | 57914       | 1042       | 7680       
    l2i_cache_refill:u | 2270        | 2613        | 601        | 1167       
    l2i_tlb:u          | 97          | 645         | 224        | 640        
    l2i_tlb_refill:u   | 18          | 361         | 13         | 155        
    l1d_cache:u        | 1806449252  | 1807006147  | 141033986  | 461644883  
    l1d_cache_refill:u | 523999467   | 339018082   | 153        | 86286049   
    l1d_tlb:u          | 2537081167  | 1819561713  | 141048389  | 466030043  
    l1d_tlb_refill:u   | 450275574   | 5490523     | 78         | 1377531    
    l2d_cache:u        | 7519405155  | 7570438414  | 1693       | 1895916290 
    l2d_cache_refill:u | 1329959215  | 3105777233  | 871        | 781362924  
    l2d_tlb:u          | 450302456   | 5508084     | 100        | 1385410    
    l2d_tlb_refill:u   | 18          | 3328871     | 4          | 839455     
    ll_cache:u         | 1329883629  | 3103968373  | 263        | 780895483  
    ll_cache_miss:u    | 105484449   | 2830894012  | 24         | 713634822  
combined_orders:
    id        | modules                                                                                                                                     
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld14_pshuf_p524288_lp1_r1000+mix_b128_ld1_pshuf_p1_lp4_r1000+mix_b64_ld7_pshuf_p524288_lp1_r1000
    shuffle   | mix_b128_ld14_pshuf_p524288_lp1_r1000+mix_b64_ld7_pshuf_p524288_lp1_r1000+mix_b128_ld1_pshuf_p1_lp4_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000
    sum       | mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld14_pshuf_p524288_lp1_r1000+mix_b128_ld1_pshuf_p1_lp4_r1000+mix_b64_ld7_pshuf_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 133933227777 | 132540742373 | 124116915404
    instructions:u     | 7316074119   | 7316074049   | 7316258021  
    br_retired:u       | 32011199     | 32011190     | 32020299    
    br_mis_pred:u      | 10048        | 11135        | 11478       
    l1i_cache:u        | 943245312    | 943202718    | 939476273   
    l1i_cache_refill:u | 337457       | 315760       | 90743       
    l1i_tlb:u          | 943245312    | 943202718    | 939476273   
    l1i_tlb_refill:u   | 1353         | 1375         | 612         
    l2i_cache:u        | 337731       | 316109       | 91301       
    l2i_cache_refill:u | 54260        | 53174        | 6651        
    l2i_tlb:u          | 2081         | 1906         | 1606        
    l2i_tlb_refill:u   | 1342         | 1374         | 547         
    l1d_cache:u        | 4217133691   | 4216984029   | 4216134268  
    l1d_cache_refill:u | 984719836    | 943973973    | 949303751   
    l1d_tlb:u          | 4901642761   | 4952553107   | 4963721312  
    l1d_tlb_refill:u   | 457265936    | 458391591    | 457143706   
    l2d_cache:u        | 15712689616  | 17174878555  | 16985761552 
    l2d_cache_refill:u | 4894194989   | 5198292256   | 5217100243  
    l2d_tlb:u          | 457318393    | 458518835    | 457196050   
    l2d_tlb_refill:u   | 5412818      | 5424454      | 4168348     
    ll_cache:u         | 4891574356   | 5195734763   | 5214747748  
    ll_cache_miss:u    | 3807799407   | 4157425697   | 3650013307  

== combo_045_s4 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld2_pshuf_p512_lp4_r1000   
    s1 | mix_b128_ld7_pshuf_p524288_lp1_r1000
    s2 | mix_b128_ld2_pshuf_p128_lp4_r1000   
    s3 | mix_b64_ld1_xpage_p128_lp4_r1000    
single_counts:
    metric             | s0         | s1          | s2         | s3        
    -------------------+------------+-------------+------------+-----------
    cpu-cycles:u       | 9349031708 | 37100354423 | 4307192368 | 1426840533
    instructions:u     | 2085063808 | 2085065072  | 2085063795 | 1061064023
    br_retired:u       | 8004922    | 8005192     | 8004922    | 8004983   
    br_mis_pred:u      | 2170       | 3106        | 2552       | 2099      
    l1i_cache:u        | 266784431  | 267846813   | 266199161  | 137165898 
    l1i_cache_refill:u | 7804       | 34696       | 4257       | 1108      
    l1i_tlb:u          | 266784431  | 267846813   | 266199161  | 137165898 
    l1i_tlb_refill:u   | 44         | 272         | 52         | 55        
    l2i_cache:u        | 7827       | 34815       | 4268       | 1109      
    l2i_cache_refill:u | 1947       | 1890        | 752        | 618       
    l2i_tlb:u          | 91         | 588         | 466        | 144       
    l2i_tlb_refill:u   | 19         | 269         | 26         | 22        
    l1d_cache:u        | 269322874  | 909993574   | 269081654  | 77070402  
    l1d_cache_refill:u | 110009855  | 171507436   | 81293793   | 61207861  
    l1d_tlb:u          | 369297737  | 917302895   | 377166584  | 153202639 
    l1d_tlb_refill:u   | 66038442   | 2748499     | 66006813   | 67011636  
    l2d_cache:u        | 933914820  | 3784289183  | 835400595  | 155097304 
    l2d_cache_refill:u | 403999874  | 1552617561  | 117032051  | 27032624  
    l2d_tlb:u          | 66038935   | 2761227     | 66009623   | 67012319  
    l2d_tlb_refill:u   | 229        | 1674550     | 16         | 10        
    ll_cache:u         | 403963614  | 1551718364  | 117028362  | 27031745  
    ll_cache_miss:u    | 840761     | 1415532449  | 71937      | 12371     
combined_orders:
    id        | modules                                                                                                                                  
    ----------+------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld2_pshuf_p512_lp4_r1000+mix_b128_ld7_pshuf_p524288_lp1_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b64_ld1_xpage_p128_lp4_r1000
    shuffle   | mix_b64_ld1_xpage_p128_lp4_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b128_ld7_pshuf_p524288_lp1_r1000+mix_b128_ld2_pshuf_p512_lp4_r1000
    sum       | mix_b128_ld2_pshuf_p512_lp4_r1000+mix_b128_ld7_pshuf_p524288_lp1_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b64_ld1_xpage_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 58226663606 | 58084765880 | 52183419032
    instructions:u     | 7316074116  | 7316074092  | 7316256698 
    br_retired:u       | 32011198    | 32011195    | 32020019   
    br_mis_pred:u      | 9131        | 11167       | 9927       
    l1i_cache:u        | 939075788   | 937401797   | 937996303  
    l1i_cache_refill:u | 203751      | 199966      | 47865      
    l1i_tlb:u          | 939075788   | 937401797   | 937996303  
    l1i_tlb_refill:u   | 585         | 603         | 423        
    l2i_cache:u        | 203932      | 200221      | 48019      
    l2i_cache_refill:u | 35618       | 36235       | 5207       
    l2i_tlb:u          | 1015        | 1180        | 1289       
    l2i_tlb_refill:u   | 579         | 612         | 336        
    l1d_cache:u        | 1525889632  | 1524567325  | 1525468504 
    l1d_cache_refill:u | 449511295   | 447261738   | 424018945  
    l1d_tlb:u          | 1808084381  | 1808020007  | 1816969855 
    l1d_tlb_refill:u   | 200863415   | 200803958   | 201805390  
    l2d_cache:u        | 5578910495  | 5608329822  | 5708701902 
    l2d_cache_refill:u | 2132345486  | 2135567956  | 2100682110 
    l2d_tlb:u          | 200896553   | 200840301   | 201822104  
    l2d_tlb_refill:u   | 3063302     | 2996622     | 1674805    
    ll_cache:u         | 2131237376  | 2134926854  | 2099742085 
    ll_cache_miss:u    | 1460093899  | 1461437944  | 1416457518 

== combo_046_s4 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld14_indir_p128_lp1_r1000  
    s1 | mix_b128_ld2_indir_p524288_lp1_r1000
    s2 | mix_b128_ld4_pshuf_p1_lp4_r1000     
    s3 | mix_b64_ld2_pshuf_p128_lp1_r1000    
single_counts:
    metric             | s0          | s1          | s2         | s3        
    -------------------+-------------+-------------+------------+-----------
    cpu-cycles:u       | 57217496208 | 64600702716 | 2067036019 | 3869288498
    instructions:u     | 2085065092  | 2085065100  | 2085064029 | 1061063795
    br_retired:u       | 8005195     | 8005197     | 8004981    | 8004922   
    br_mis_pred:u      | 3298        | 3794        | 2444       | 2590      
    l1i_cache:u        | 267108363   | 265504043   | 266088281  | 137079850 
    l1i_cache_refill:u | 43460       | 52953       | 2357       | 1746      
    l1i_tlb:u          | 267108363   | 265504043   | 266088281  | 137079850 
    l1i_tlb_refill:u   | 49          | 367         | 54         | 34        
    l2i_cache:u        | 43982       | 53174       | 2368       | 1750      
    l2i_cache_refill:u | 1673        | 4141        | 652        | 573       
    l2i_tlb:u          | 222         | 424         | 110        | 110       
    l2i_tlb_refill:u   | 15          | 362         | 30         | 16        
    l1d_cache:u        | 1805110028  | 269638587   | 525065495  | 141054213 
    l1d_cache_refill:u | 1723237487  | 256139172   | 193        | 122021208 
    l1d_tlb:u          | 3607506926  | 537527894   | 525115789  | 276827828 
    l1d_tlb_refill:u   | 1795055545  | 251312292   | 98         | 130000133 
    l2d_cache:u        | 4974470467  | 1018597460  | 3043       | 364446406 
    l2d_cache_refill:u | 1389087695  | 517160472   | 1022       | 99289396  
    l2d_tlb:u          | 1795063352  | 251416852   | 126        | 130500869 
    l2d_tlb_refill:u   | 20          | 3063907     | 14         | 37        
    ll_cache:u         | 1389076311  | 517069445   | 324        | 99288352  
    ll_cache_miss:u    | 34456       | 514383189   | 28         | 515       
combined_orders:
    id        | modules                                                                                                                                 
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_indir_p128_lp1_r1000+mix_b128_ld2_indir_p524288_lp1_r1000+mix_b128_ld4_pshuf_p1_lp4_r1000+mix_b64_ld2_pshuf_p128_lp1_r1000
    shuffle   | mix_b128_ld14_indir_p128_lp1_r1000+mix_b64_ld2_pshuf_p128_lp1_r1000+mix_b128_ld2_indir_p524288_lp1_r1000+mix_b128_ld4_pshuf_p1_lp4_r1000
    sum       | mix_b128_ld14_indir_p128_lp1_r1000+mix_b128_ld2_indir_p524288_lp1_r1000+mix_b128_ld4_pshuf_p1_lp4_r1000+mix_b64_ld2_pshuf_p128_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 121611747966 | 125906467754 | 127754523441
    instructions:u     | 7316074049   | 7316074100   | 7316258016  
    br_retired:u       | 32011190     | 32011197     | 32020295    
    br_mis_pred:u      | 10611        | 10020        | 12126       
    l1i_cache:u        | 937499128    | 937576306    | 935780537   
    l1i_cache_refill:u | 300402       | 302096       | 100516      
    l1i_tlb:u          | 937499128    | 937576306    | 935780537   
    l1i_tlb_refill:u   | 814          | 815          | 504         
    l2i_cache:u        | 301122       | 303097       | 101274      
    l2i_cache_refill:u | 23664        | 35631        | 7039        
    l2i_tlb:u          | 1397         | 1207         | 866         
    l2i_tlb_refill:u   | 802          | 812          | 423         
    l1d_cache:u        | 2741786039   | 2740690198   | 2740868323  
    l1d_cache_refill:u | 2102002546   | 2115827624   | 2101398060  
    l1d_tlb:u          | 4944525962   | 4940587428   | 4946978437  
    l1d_tlb_refill:u   | 2175328169   | 2174384685   | 2176368068  
    l2d_cache:u        | 6065871605   | 7308871268   | 6357517376  
    l2d_cache_refill:u | 1710165631   | 2951269254   | 2005538585  
    l2d_tlb:u          | 2175895947   | 2174509406   | 2176981199  
    l2d_tlb_refill:u   | 4257992      | 3502460      | 3063978     
    ll_cache:u         | 1710015254   | 2951082093   | 2005434432  
    ll_cache_miss:u    | 515729333    | 538507779    | 514418188   

== combo_047_s4 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld7_indir_p524288_lp4_r1000
    s1 | mix_b128_ld7_lin_p512_lp4_r1000     
    s2 | mix_b64_ld7_pshuf_p512_lp4_r1000    
    s3 | mix_b64_ld2_pshuf_p512_lp4_r1000    
single_counts:
    metric             | s0           | s1          | s2          | s3        
    -------------------+--------------+-------------+-------------+-----------
    cpu-cycles:u       | 228539781031 | 26124188291 | 16791502756 | 5075033758
    instructions:u     | 2085065117   | 2085065049  | 1061063795  | 1061063801
    br_retired:u       | 8005207      | 8005189     | 8004922     | 8004920   
    br_mis_pred:u      | 4398         | 2565        | 2669        | 2125      
    l1i_cache:u        | 268054183    | 267206380   | 139512509   | 138472021 
    l1i_cache_refill:u | 167464       | 19501       | 6681        | 2424      
    l1i_tlb:u          | 268054183    | 267206380   | 139512509   | 138472021 
    l1i_tlb_refill:u   | 515          | 48          | 46          | 44        
    l2i_cache:u        | 168990       | 19638       | 6695        | 2428      
    l2i_cache_refill:u | 9056         | 1692        | 3093        | 1220      
    l2i_tlb:u          | 713          | 126         | 109         | 332       
    l2i_tlb_refill:u   | 512          | 34          | 19          | 24        
    l1d_cache:u        | 910874645    | 910475206   | 462156152   | 141144788 
    l1d_cache_refill:u | 897557898    | 297025655   | 192861756   | 67137718  
    l1d_tlb:u          | 1799631655   | 1168639746  | 631662448   | 196511562 
    l1d_tlb_refill:u   | 871395973    | 226271659   | 114215380   | 35017030  
    l2d_cache:u        | 3609526899   | 3009907026  | 1612400968  | 412351610 
    l2d_cache_refill:u | 1816368516   | 1588704750  | 697529591   | 180486161 
    l2d_tlb:u          | 871480388    | 226344704   | 114278650   | 35039035  
    l2d_tlb_refill:u   | 10156098     | 274         | 247         | 185       
    ll_cache:u         | 1814548578   | 1588511163  | 697460671   | 180473663 
    ll_cache_miss:u    | 1785701699   | 22689151    | 11025883    | 374469    
combined_orders:
    id        | modules                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld7_indir_p524288_lp4_r1000+mix_b128_ld7_lin_p512_lp4_r1000+mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b64_ld2_pshuf_p512_lp4_r1000
    shuffle   | mix_b64_ld2_pshuf_p512_lp4_r1000+mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b128_ld7_lin_p512_lp4_r1000+mix_b128_ld7_indir_p524288_lp4_r1000
    sum       | mix_b128_ld7_indir_p524288_lp4_r1000+mix_b128_ld7_lin_p512_lp4_r1000+mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b64_ld2_pshuf_p512_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 274608682669 | 275566413650 | 276530505836
    instructions:u     | 6292074342   | 6292074280   | 6292257762  
    br_retired:u       | 32011240     | 32011230     | 32020238    
    br_mis_pred:u      | 12260        | 12672        | 11757       
    l1i_cache:u        | 816362688    | 816478597    | 813245093   
    l1i_cache_refill:u | 425633       | 428690       | 196070      
    l1i_tlb:u          | 816362688    | 816478597    | 813245093   
    l1i_tlb_refill:u   | 992          | 1338         | 653         
    l2i_cache:u        | 426492       | 429998       | 197751      
    l2i_cache_refill:u | 58016        | 61470        | 15061       
    l2i_tlb:u          | 1833         | 1557         | 1280        
    l2i_tlb_refill:u   | 988          | 1333         | 589         
    l1d_cache:u        | 2427184524   | 2427190368   | 2424650791  
    l1d_cache_refill:u | 1401027542   | 1395657930   | 1454583027  
    l1d_tlb:u          | 3795733060   | 3798477064   | 3796445411  
    l1d_tlb_refill:u   | 1247977853   | 1247883369   | 1246900042  
    l2d_cache:u        | 8545171126   | 8524883354   | 8644186503  
    l2d_cache_refill:u | 4393301143   | 4366383940   | 4283089018  
    l2d_tlb:u          | 1248285691   | 1248186928   | 1247142777  
    l2d_tlb_refill:u   | 12227622     | 12073628     | 10156804    
    ll_cache:u         | 4391642330   | 4364566769   | 4280994075  
    ll_cache_miss:u    | 2483599149   | 2473676355   | 1819791202  

== combo_048_s4 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld1_xpage_p1_lp1_r1000     
    s1 | mix_b64_ld4_pshuf_p128_lp1_r1000   
    s2 | mix_b64_ld4_pshuf_p128_lp1_r1000   
    s3 | mix_b64_ld2_xpage_p524288_lp4_r1000
single_counts:
    metric             | s0         | s1         | s2         | s3         
    -------------------+------------+------------+------------+------------
    cpu-cycles:u       | 274100967  | 6903797815 | 6865205020 | 32289797982
    instructions:u     | 1061064161 | 1061063795 | 1061063795 | 1061065123 
    br_retired:u       | 8005002    | 8004922    | 8004922    | 8005199    
    br_mis_pred:u      | 2103       | 2157       | 2162       | 3369       
    l1i_cache:u        | 137041074  | 137651251  | 138618233  | 139297396  
    l1i_cache_refill:u | 733        | 2694       | 2707       | 12466      
    l1i_tlb:u          | 137041074  | 137651251  | 138618233  | 139297396  
    l1i_tlb_refill:u   | 45         | 41         | 45         | 243        
    l2i_cache:u        | 733        | 2697       | 2714       | 12499      
    l2i_cache_refill:u | 556        | 565        | 613        | 1749       
    l2i_tlb:u          | 86         | 689        | 437        | 308        
    l2i_tlb_refill:u   | 12         | 11         | 13         | 230        
    l1d_cache:u        | 77033560   | 269358129  | 269172663  | 141730387  
    l1d_cache_refill:u | 149        | 246917237  | 250133954  | 128420886  
    l1d_tlb:u          | 77047743   | 535805062  | 535266136  | 279222635  
    l1d_tlb_refill:u   | 62         | 258133290  | 258049736  | 126399471  
    l2d_cache:u        | 1250       | 632415424  | 693667349  | 509533481  
    l2d_cache_refill:u | 770        | 119629085  | 177276429  | 258188649  
    l2d_tlb:u          | 416        | 258505099  | 258288370  | 126499649  
    l2d_tlb_refill:u   | 3          | 19         | 17         | 1400036    
    ll_cache:u         | 237        | 119628232  | 177274903  | 258187189  
    ll_cache_miss:u    | 20         | 809        | 3433       | 257085310  
combined_orders:
    id        | modules                                                                                                                             
    ----------+-------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld1_xpage_p1_lp1_r1000+mix_b64_ld4_pshuf_p128_lp1_r1000+mix_b64_ld4_pshuf_p128_lp1_r1000+mix_b64_ld2_xpage_p524288_lp4_r1000
    shuffle   | mix_b64_ld2_xpage_p524288_lp4_r1000+mix_b64_ld1_xpage_p1_lp1_r1000+mix_b64_ld4_pshuf_p128_lp1_r1000+mix_b64_ld4_pshuf_p128_lp1_r1000
    sum       | mix_b64_ld1_xpage_p1_lp1_r1000+mix_b64_ld4_pshuf_p128_lp1_r1000+mix_b64_ld4_pshuf_p128_lp1_r1000+mix_b64_ld2_xpage_p524288_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 47291527187 | 48104005970 | 46332901784
    instructions:u     | 4244074040  | 4244074091  | 4244256874 
    br_retired:u       | 32011189    | 32011196    | 32020045   
    br_mis_pred:u      | 12944       | 11517       | 9791       
    l1i_cache:u        | 553095677   | 552958923   | 552607954  
    l1i_cache_refill:u | 82835       | 86169       | 18600      
    l1i_tlb:u          | 553095677   | 552958923   | 552607954  
    l1i_tlb_refill:u   | 422         | 423         | 374        
    l2i_cache:u        | 82900       | 86264       | 18643      
    l2i_cache_refill:u | 17098       | 19337       | 3483       
    l2i_tlb:u          | 565         | 596         | 1520       
    l2i_tlb_refill:u   | 417         | 419         | 266        
    l1d_cache:u        | 757715075   | 756857374   | 757294739  
    l1d_cache_refill:u | 617102900   | 623600212   | 625472226  
    l1d_tlb:u          | 1429579148  | 1427318520  | 1427341576 
    l1d_tlb_refill:u   | 642884913   | 642411216   | 642582559  
    l2d_cache:u        | 2011387768  | 2163911932  | 1835617504 
    l2d_cache_refill:u | 725288284   | 829966657   | 555094933  
    l2d_tlb:u          | 643602722   | 643328856   | 643293534  
    l2d_tlb_refill:u   | 2430489     | 2790029     | 1400075    
    ll_cache:u         | 725182337   | 829753101   | 555090561  
    ll_cache_miss:u    | 298500368   | 298905026   | 257089572  

== combo_049_s4 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b64_ld4_lin_p512_lp4_r1000    
    s1 | mix_b64_ld7_lin_p524288_lp4_r1000 
    s2 | mix_b64_ld14_lin_p524288_lp4_r1000
    s3 | mix_b128_ld2_lin_p512_lp4_r1000   
single_counts:
    metric             | s0         | s1          | s2          | s3        
    -------------------+------------+-------------+-------------+-----------
    cpu-cycles:u       | 7524042017 | 45535925322 | 90486669258 | 7811597901
    instructions:u     | 1061063795 | 1061065133  | 1061065089  | 2085063795
    br_retired:u       | 8004922    | 8005203     | 8005194     | 8004922   
    br_mis_pred:u      | 2578       | 3247        | 3427        | 2842      
    l1i_cache:u        | 138591483  | 137907449   | 139134667   | 265431555 
    l1i_cache_refill:u | 3053       | 15769       | 29278       | 7416      
    l1i_tlb:u          | 138591483  | 137907449   | 139134667   | 265431555 
    l1i_tlb_refill:u   | 42         | 261         | 339         | 47        
    l2i_cache:u        | 3054       | 15828       | 29520       | 7429      
    l2i_cache_refill:u | 1051       | 7457        | 9813        | 958       
    l2i_tlb:u          | 90         | 414         | 445         | 86        
    l2i_tlb_refill:u   | 23         | 257         | 334         | 25        
    l1d_cache:u        | 269421445  | 461654625   | 913157160   | 269247111 
    l1d_cache_refill:u | 78974611   | 116886743   | 209560719   | 74412263  
    l1d_tlb:u          | 347502114  | 463382010   | 918589838   | 352850258 
    l1d_tlb_refill:u   | 66071744   | 356522      | 705747      | 66030801  
    l2d_cache:u        | 869081429  | 1508241168  | 3496157800  | 881291608 
    l2d_cache_refill:u | 460607713  | 817927863   | 2032986153  | 454447602 
    l2d_tlb:u          | 66142665   | 370470      | 724721      | 66032440  
    l2d_tlb_refill:u   | 218        | 238310      | 457502      | 554       
    ll_cache:u         | 460549118  | 817725065   | 2032644216  | 454392156 
    ll_cache_miss:u    | 4650482    | 778668313   | 1941068659  | 7203709   
combined_orders:
    id        | modules                                                                                                                            
    ----------+------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld4_lin_p512_lp4_r1000+mix_b64_ld7_lin_p524288_lp4_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b128_ld2_lin_p512_lp4_r1000
    shuffle   | mix_b64_ld4_lin_p512_lp4_r1000+mix_b64_ld7_lin_p524288_lp4_r1000+mix_b128_ld2_lin_p512_lp4_r1000+mix_b64_ld14_lin_p524288_lp4_r1000
    sum       | mix_b64_ld4_lin_p512_lp4_r1000+mix_b64_ld7_lin_p524288_lp4_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b128_ld2_lin_p512_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 151717112951 | 151279073163 | 151358234498
    instructions:u     | 5268074143   | 5268074073   | 5268257812  
    br_retired:u       | 32011202     | 32011193     | 32020241    
    br_mis_pred:u      | 11271        | 10948        | 12094       
    l1i_cache:u        | 685273134    | 683397270    | 681065154   
    l1i_cache_refill:u | 216675       | 228268       | 55516       
    l1i_tlb:u          | 685273134    | 683397270    | 681065154   
    l1i_tlb_refill:u   | 1075         | 1169         | 689         
    l2i_cache:u        | 216920       | 228577       | 55831       
    l2i_cache_refill:u | 37274        | 42604        | 19279       
    l2i_tlb:u          | 2037         | 1463         | 1035        
    l2i_tlb_refill:u   | 1072         | 1166         | 639         
    l1d_cache:u        | 1913052474   | 1910775741   | 1913480341  
    l1d_cache_refill:u | 474672475    | 473850076    | 479834336   
    l1d_tlb:u          | 2075593154   | 2070778555   | 2082324220  
    l1d_tlb_refill:u   | 133165926    | 133165393    | 133164814   
    l2d_cache:u        | 6595769580   | 6621816139   | 6754772005  
    l2d_cache_refill:u | 3785216250   | 3810951023   | 3765969331  
    l2d_tlb:u          | 133294955    | 133280580    | 133270296   
    l2d_tlb_refill:u   | 2012448      | 2017271      | 696584      
    ll_cache:u         | 3784193877   | 3809896837   | 3765310555  
    ll_cache_miss:u    | 3023268600   | 3013144621   | 2731591163  

== combo_050_s4 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b128_ld14_indir_p512_lp1_r1000 
    s1 | mix_b64_ld7_pshuf_p524288_lp1_r1000
    s2 | mix_b64_ld4_xpage_p128_lp4_r1000   
    s3 | mix_b128_ld14_xpage_p128_lp4_r1000 
single_counts:
    metric             | s0          | s1          | s2         | s3         
    -------------------+-------------+-------------+------------+------------
    cpu-cycles:u       | 74613471740 | 18587423756 | 6037625981 | 43859032611
    instructions:u     | 2085065143  | 1061063801  | 1061063795 | 2085065116 
    br_retired:u       | 8005202     | 8004920     | 8004922    | 8005198    
    br_mis_pred:u      | 3220        | 2779        | 2138       | 3363       
    l1i_cache:u        | 269424352   | 138145661   | 137609142  | 266703369  
    l1i_cache_refill:u | 53142       | 6798        | 2649       | 32100      
    l1i_tlb:u          | 269424352   | 138145661   | 137609142  | 266703369  
    l1i_tlb_refill:u   | 46          | 180         | 45         | 45         
    l2i_cache:u        | 53442       | 6810        | 2656       | 32352      
    l2i_cache_refill:u | 2350        | 1037        | 688        | 2514       
    l2i_tlb:u          | 141         | 384         | 197        | 204        
    l2i_tlb_refill:u   | 32          | 176         | 17         | 20         
    l1d_cache:u        | 1805038624  | 461159649   | 269400677  | 1805055335 
    l1d_cache_refill:u | 1792305544  | 88051676    | 243746990  | 1712220122 
    l1d_tlb:u          | 3604708681  | 465605014   | 535669615  | 3606441096 
    l1d_tlb_refill:u   | 1794001178  | 1376914     | 258153206  | 1794009848 
    l2d_cache:u        | 7080079991  | 1898927420  | 723817653  | 4524006826 
    l2d_cache_refill:u | 3587967683  | 780998287   | 147778256  | 937647064  
    l2d_tlb:u          | 1794022134  | 1384789     | 258687766  | 1794015905 
    l2d_tlb_refill:u   | 510         | 838991      | 19         | 30         
    ll_cache:u         | 3587945407  | 780666416   | 147776059  | 937632478  
    ll_cache_miss:u    | 147089      | 713065942   | 6273       | 7239755    
combined_orders:
    id        | modules                                                                                                                                   
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_indir_p512_lp1_r1000+mix_b64_ld7_pshuf_p524288_lp1_r1000+mix_b64_ld4_xpage_p128_lp4_r1000+mix_b128_ld14_xpage_p128_lp4_r1000
    shuffle   | mix_b64_ld4_xpage_p128_lp4_r1000+mix_b128_ld14_xpage_p128_lp4_r1000+mix_b64_ld7_pshuf_p524288_lp1_r1000+mix_b128_ld14_indir_p512_lp1_r1000
    sum       | mix_b128_ld14_indir_p512_lp1_r1000+mix_b64_ld7_pshuf_p524288_lp1_r1000+mix_b64_ld4_xpage_p128_lp4_r1000+mix_b128_ld14_xpage_p128_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 145342192107 | 143129930832 | 143097554088
    instructions:u     | 6292074143   | 6292074041   | 6292257855  
    br_retired:u       | 32011202     | 32011188     | 32020242    
    br_mis_pred:u      | 13926        | 13136        | 11500       
    l1i_cache:u        | 812880903    | 814254665    | 811882524   
    l1i_cache_refill:u | 289356       | 291936       | 94689       
    l1i_tlb:u          | 812880903    | 814254665    | 811882524   
    l1i_tlb_refill:u   | 774          | 775          | 316         
    l2i_cache:u        | 289679       | 292296       | 95260       
    l2i_cache_refill:u | 27740        | 35552        | 6589        
    l2i_tlb:u          | 1348         | 1339         | 926         
    l2i_tlb_refill:u   | 769          | 770          | 245         
    l1d_cache:u        | 4345451185   | 4345144170   | 4340654285  
    l1d_cache_refill:u | 3821512943   | 3828690695   | 3836324332  
    l1d_tlb:u          | 8224739292   | 8224340508   | 8212424406  
    l1d_tlb_refill:u   | 3850771608   | 3850804096   | 3847541146  
    l2d_cache:u        | 14389490612  | 13997276990  | 14226831890 
    l2d_cache_refill:u | 5601011413   | 5200687438   | 5454391290  
    l2d_tlb:u          | 3851146297   | 3851188581   | 3848110594  
    l2d_tlb_refill:u   | 1960276      | 1962790      | 839550      
    ll_cache:u         | 5600672985   | 5200645214   | 5454020360  
    ll_cache_miss:u    | 735845026    | 730938543    | 720459059   

== combo_051_s5 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld14_lin_p128_lp1_r1000    
    s1 | mix_b128_ld1_pshuf_p524288_lp4_r1000
    s2 | mix_b64_ld4_xpage_p524288_lp1_r1000 
    s3 | mix_b128_ld14_xpage_p128_lp4_r1000  
    s4 | mix_b128_ld2_lin_p1_lp1_r1000       
single_counts:
    metric             | s0          | s1          | s2          | s3          | s4        
    -------------------+-------------+-------------+-------------+-------------+-----------
    cpu-cycles:u       | 50488731190 | 10223911574 | 64696016439 | 40814317684 | 1042105410
    instructions:u     | 2085065092  | 2085063801  | 1061065092  | 2085065096  | 2085064014
    br_retired:u       | 8005195     | 8004920     | 8005195     | 8005195     | 8004982   
    br_mis_pred:u      | 3671        | 2838        | 2454        | 3206        | 2870      
    l1i_cache:u        | 266305938   | 265637846   | 139239964   | 266701392   | 266058827 
    l1i_cache_refill:u | 37332       | 13349       | 22157       | 30331       | 1452      
    l1i_tlb:u          | 266305938   | 265637846   | 139239964   | 266701392   | 266058827 
    l1i_tlb_refill:u   | 47          | 120         | 302         | 55          | 43        
    l2i_cache:u        | 37458       | 13372       | 22204       | 30532       | 1461      
    l2i_cache_refill:u | 1747        | 2512        | 2862        | 2642        | 612       
    l2i_tlb:u          | 170         | 535         | 373         | 159         | 83        
    l2i_tlb_refill:u   | 18          | 108         | 297         | 36          | 15        
    l1d_cache:u        | 1807651053  | 141245809   | 270618523   | 1805246710  | 269037485 
    l1d_cache_refill:u | 1713574031  | 60609032    | 256806366   | 1710864717  | 186       
    l1d_tlb:u          | 3612503600  | 141687530   | 535522428   | 3606337105  | 269079274 
    l1d_tlb_refill:u   | 1795962158  | 103479      | 251028777   | 1794139777  | 90        
    l2d_cache:u        | 4723850959  | 457272480   | 1020394542  | 4596953569  | 2284      
    l2d_cache_refill:u | 1134013719  | 216799009   | 518369390   | 1012810909  | 989       
    l2d_tlb:u          | 1795998459  | 107606      | 251265445   | 1794152487  | 127       
    l2d_tlb_refill:u   | 29          | 68990       | 2522880     | 15          | 18        
    ll_cache:u         | 1134007162  | 216756147   | 518279527   | 1012795083  | 319       
    ll_cache_miss:u    | 51354       | 182109489   | 514292585   | 2474802     | 66        
combined_orders:
    id        | modules                                                                                                                                                                   
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_lin_p128_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000+mix_b64_ld4_xpage_p524288_lp1_r1000+mix_b128_ld14_xpage_p128_lp4_r1000+mix_b128_ld2_lin_p1_lp1_r1000
    shuffle   | mix_b64_ld4_xpage_p524288_lp1_r1000+mix_b128_ld14_lin_p128_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000+mix_b128_ld14_xpage_p128_lp4_r1000+mix_b128_ld2_lin_p1_lp1_r1000
    sum       | mix_b128_ld14_lin_p128_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000+mix_b64_ld4_xpage_p524288_lp1_r1000+mix_b128_ld14_xpage_p128_lp4_r1000+mix_b128_ld2_lin_p1_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 172497347100 | 166257168106 | 167265082297
    instructions:u     | 9401077178   | 9401077124   | 9401323095  
    br_retired:u       | 40013215     | 40013207     | 40025487    
    br_mis_pred:u      | 9499         | 8622         | 15039       
    l1i_cache:u        | 1207216292   | 1208154205   | 1203943967  
    l1i_cache_refill:u | 498426       | 490874       | 104621      
    l1i_tlb:u          | 1207216292   | 1208154205   | 1203943967  
    l1i_tlb_refill:u   | 1759         | 1703         | 567         
    l2i_cache:u        | 499142       | 491401       | 105027      
    l2i_cache_refill:u | 73878        | 77480        | 10375       
    l2i_tlb:u          | 2313         | 2239         | 1320        
    l2i_tlb_refill:u   | 1755         | 1698         | 474         
    l1d_cache:u        | 4294003022   | 4293585259   | 4293799580  
    l1d_cache_refill:u | 3757749186   | 3738694448   | 3741854332  
    l1d_tlb:u          | 8168821873   | 8164970631   | 8165129937  
    l1d_tlb_refill:u   | 3841487007   | 3841113175   | 3841234281  
    l2d_cache:u        | 10845632490  | 10834078772  | 10798473834 
    l2d_cache_refill:u | 2909997366   | 2890064070   | 2881994016  
    l2d_tlb:u          | 3841849989   | 3841487082   | 3841524124  
    l2d_tlb_refill:u   | 4792268      | 4028748      | 2591932     
    ll_cache:u         | 2909697829   | 2889723012   | 2881838238  
    ll_cache_miss:u    | 750128563    | 739394175    | 698928296   

== combo_052_s5 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld14_pshuf_p128_lp4_r1000  
    s1 | mix_b64_ld7_lin_p1_lp4_r1000        
    s2 | mix_b128_ld7_xpage_p128_lp1_r1000   
    s3 | mix_b128_ld2_lin_p512_lp1_r1000     
    s4 | mix_b64_ld14_indir_p524288_lp1_r1000
single_counts:
    metric             | s0          | s1         | s2          | s3          | s4          
    -------------------+-------------+------------+-------------+-------------+-------------
    cpu-cycles:u       | 34436331288 | 1810100092 | 23820256352 | 10987933919 | 226329054555
    instructions:u     | 2085065103  | 1061064029 | 2085064012  | 2085063795  | 1061065096  
    br_retired:u       | 8005197     | 8004981    | 8004978     | 8004922     | 8005205     
    br_mis_pred:u      | 3377        | 2433       | 2919        | 3200        | 3624        
    l1i_cache:u        | 267389587   | 137054548  | 267330239   | 266129208   | 137864301   
    l1i_cache_refill:u | 26707       | 1211       | 18629       | 8902        | 67322       
    l1i_tlb:u          | 267389587   | 137054548  | 267330239   | 266129208   | 137864301   
    l1i_tlb_refill:u   | 44          | 47         | 48          | 46          | 414         
    l2i_cache:u        | 27047       | 1211       | 18756       | 8943        | 67456       
    l2i_cache_refill:u | 5246        | 559        | 867         | 758         | 4776        
    l2i_tlb:u          | 124         | 89         | 151         | 269         | 493         
    l2i_tlb_refill:u   | 16          | 13         | 18          | 31          | 409         
    l1d_cache:u        | 1806349391  | 461037546  | 909437559   | 269078720   | 909362787   
    l1d_cache_refill:u | 594897361   | 163        | 874138128   | 255886138   | 895869640   
    l1d_tlb:u          | 2492395393  | 461083318  | 1812682357  | 532938070   | 1795622302  
    l1d_tlb_refill:u   | 451252959   | 95         | 898296126   | 258024569   | 870089803   
    l2d_cache:u        | 6081333792  | 1818       | 2460676146  | 1045914447  | 3560842181  
    l2d_cache_refill:u | 1066222843  | 790        | 667027651   | 517311700   | 1810065050  
    l2d_tlb:u          | 451279536   | 128        | 898304577   | 258033799   | 870141036   
    l2d_tlb_refill:u   | 133         | 7          | 26          | 249         | 9351386     
    ll_cache:u         | 1066139747  | 248        | 667023069   | 517302748   | 1809114792  
    ll_cache_miss:u    | 10612204    | 55         | 21637       | 4603971     | 1802068858  
combined_orders:
    id        | modules                                                                                                                                                               
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b64_ld7_lin_p1_lp4_r1000+mix_b128_ld7_xpage_p128_lp1_r1000+mix_b128_ld2_lin_p512_lp1_r1000+mix_b64_ld14_indir_p524288_lp1_r1000
    shuffle   | mix_b64_ld14_indir_p524288_lp1_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld2_lin_p512_lp1_r1000+mix_b128_ld7_xpage_p128_lp1_r1000+mix_b64_ld7_lin_p1_lp4_r1000
    sum       | mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b64_ld7_lin_p1_lp4_r1000+mix_b128_ld7_xpage_p128_lp1_r1000+mix_b128_ld2_lin_p512_lp1_r1000+mix_b64_ld14_indir_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 300973864017 | 298712773924 | 297383676206
    instructions:u     | 8377077412   | 8377077240   | 8377322035  
    br_retired:u       | 40013249     | 40013226     | 40025283    
    br_mis_pred:u      | 11445        | 9905         | 15553       
    l1i_cache:u        | 1076887225   | 1076506238   | 1075767883  
    l1i_cache_refill:u | 611009       | 596043       | 122771      
    l1i_tlb:u          | 1076887225   | 1076506238   | 1075767883  
    l1i_tlb_refill:u   | 1205         | 1124         | 599         
    l2i_cache:u        | 611266       | 596460       | 123413      
    l2i_cache_refill:u | 99119        | 106611       | 12206       
    l2i_tlb:u          | 1347         | 1581         | 1126        
    l2i_tlb_refill:u   | 1200         | 1118         | 487         
    l1d_cache:u        | 4355895601   | 4355509635   | 4355266003  
    l1d_cache_refill:u | 2539866303   | 2523226594   | 2620791430  
    l1d_tlb:u          | 7121971055   | 7133474810   | 7094721440  
    l1d_tlb_refill:u   | 2476835693   | 2476717703   | 2477663552  
    l2d_cache:u        | 14372135207  | 14374887362  | 13148768384 
    l2d_cache_refill:u | 4307110168   | 4201125142   | 4060628034  
    l2d_tlb:u          | 2477158165   | 2476923520   | 2477759076  
    l2d_tlb_refill:u   | 12780795     | 11829328     | 9351801     
    ll_cache:u         | 4306480602   | 4200498521   | 4059580604  
    ll_cache_miss:u    | 2233380977   | 2298694873   | 1817306725  

== combo_053_s5 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b128_ld4_lin_p524288_lp4_r1000   
    s1 | mix_b128_ld14_pshuf_p524288_lp4_r1000
    s2 | mix_b64_ld4_lin_p1_lp4_r1000         
    s3 | mix_b128_ld2_pshuf_p1_lp1_r1000      
    s4 | mix_b128_ld2_lin_p1_lp4_r1000        
single_counts:
    metric             | s0          | s1           | s2         | s3         | s4        
    -------------------+-------------+--------------+------------+------------+-----------
    cpu-cycles:u       | 53282452506 | 151145159252 | 1043135906 | 1042098430 | 1042095121
    instructions:u     | 2085064995  | 2085065116   | 1061064023 | 2085064027 | 2085064029
    br_retired:u       | 8005182     | 8005198      | 8004983    | 8004982    | 8004981   
    br_mis_pred:u      | 3068        | 3537         | 1908       | 2469       | 2433      
    l1i_cache:u        | 266700459   | 269981505    | 137080015  | 266058034  | 266061432 
    l1i_cache_refill:u | 52455       | 126477       | 923        | 1521       | 1592      
    l1i_tlb:u          | 266700459   | 269981505    | 137080015  | 266058034  | 266061432 
    l1i_tlb_refill:u   | 340         | 455          | 36         | 42         | 40        
    l2i_cache:u        | 52548       | 126864       | 924        | 1530       | 1595      
    l2i_cache_refill:u | 10688       | 25802        | 517        | 599        | 604       
    l2i_tlb:u          | 472         | 615          | 216        | 107        | 200       
    l2i_tlb_refill:u   | 336         | 451          | 10         | 14         | 15        
    l1d_cache:u        | 525293271   | 1805963225   | 269044890  | 269037276  | 269037361 
    l1d_cache_refill:u | 128879191   | 565584582    | 143        | 169        | 178       
    l1d_tlb:u          | 526430308   | 1810315138   | 269083529  | 269063486  | 269078662 
    l1d_tlb_refill:u   | 406781      | 1434856      | 93         | 72         | 71        
    l2d_cache:u        | 1756110129  | 8312989860   | 1894       | 2172       | 2205      
    l2d_cache_refill:u | 963492322   | 4296437245   | 921        | 889        | 971       
    l2d_tlb:u          | 421946      | 1457683      | 127        | 97         | 95        
    l2d_tlb_refill:u   | 270768      | 883297       | 6          | 3          | 17        
    ll_cache:u         | 963236031   | 4295538349   | 350        | 296        | 272       
    ll_cache_miss:u    | 915963920   | 3883003026   | 48         | 43         | 19        
combined_orders:
    id        | modules                                                                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld4_lin_p524288_lp4_r1000+mix_b128_ld14_pshuf_p524288_lp4_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld2_pshuf_p1_lp1_r1000+mix_b128_ld2_lin_p1_lp4_r1000
    shuffle   | mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld4_lin_p524288_lp4_r1000+mix_b128_ld14_pshuf_p524288_lp4_r1000+mix_b128_ld2_pshuf_p1_lp1_r1000+mix_b128_ld2_lin_p1_lp4_r1000
    sum       | mix_b128_ld4_lin_p524288_lp4_r1000+mix_b128_ld14_pshuf_p524288_lp4_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld2_pshuf_p1_lp1_r1000+mix_b128_ld2_lin_p1_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 208297154005 | 207525540355 | 207554941215
    instructions:u     | 9401077108   | 9401077111   | 9401322190  
    br_retired:u       | 40013206     | 40013207     | 40025326    
    br_mis_pred:u      | 7979         | 7814         | 13415       
    l1i_cache:u        | 1207422350   | 1202139889   | 1205881445  
    l1i_cache_refill:u | 565265       | 561682       | 182968      
    l1i_tlb:u          | 1207422350   | 1202139889   | 1205881445  
    l1i_tlb_refill:u   | 1888         | 1906         | 913         
    l2i_cache:u        | 565608       | 562009       | 183461      
    l2i_cache_refill:u | 126288       | 130584       | 38210       
    l2i_tlb:u          | 2621         | 2468         | 1610        
    l2i_tlb_refill:u   | 1875         | 1901         | 826         
    l1d_cache:u        | 3139829551   | 3138883798   | 3138376023  
    l1d_cache_refill:u | 715426641    | 734692815    | 694464263   
    l1d_tlb:u          | 3146750072   | 3145168460   | 3143971123  
    l1d_tlb_refill:u   | 1857403      | 1860782      | 1841873     
    l2d_cache:u        | 9944793094   | 9987657844   | 10069106260 
    l2d_cache_refill:u | 5191920154   | 5215377311   | 5259932348  
    l2d_tlb:u          | 1900228      | 1903549      | 1879948     
    l2d_tlb_refill:u   | 1502312      | 1498782      | 1154091     
    ll_cache:u         | 5190677469   | 5214158433   | 5258775298  
    ll_cache_miss:u    | 4722456709   | 4746559416   | 4798967056  

== combo_054_s5 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld1_pshuf_p1_lp4_r1000  
    s1 | mix_b64_ld4_lin_p128_lp1_r1000   
    s2 | mix_b64_ld14_lin_p1_lp1_r1000    
    s3 | mix_b128_ld14_lin_p128_lp1_r1000 
    s4 | mix_b64_ld14_pshuf_p128_lp1_r1000
single_counts:
    metric             | s0         | s1         | s2         | s3          | s4         
    -------------------+------------+------------+------------+-------------+------------
    cpu-cycles:u       | 530104971  | 7196695625 | 3602131870 | 43910012388 | 23595053863
    instructions:u     | 2085064023 | 1061063795 | 1061063792 | 2085065089  | 1061064012 
    br_retired:u       | 8004983    | 8004922    | 8004919    | 8005194     | 8004978    
    br_mis_pred:u      | 2255       | 2062       | 2740       | 3497        | 3327       
    l1i_cache:u        | 266042636  | 138679342  | 137058594  | 267380546   | 138106532  
    l1i_cache_refill:u | 1188       | 3343       | 1835       | 33145       | 8424       
    l1i_tlb:u          | 266042636  | 138679342  | 137058594  | 267380546   | 138106532  
    l1i_tlb_refill:u   | 40         | 53         | 53         | 67          | 62         
    l2i_cache:u        | 1191       | 3351       | 1839       | 33301       | 8438       
    l2i_cache_refill:u | 619        | 733        | 580        | 1678        | 847        
    l2i_tlb:u          | 542        | 166        | 115        | 125         | 203        
    l2i_tlb_refill:u   | 13         | 19         | 26         | 52          | 41         
    l1d_cache:u        | 141033878  | 269409601  | 909038028  | 1807339831  | 909066483  
    l1d_cache_refill:u | 172        | 245202753  | 194        | 1713462862  | 865347728  
    l1d_tlb:u          | 141048178  | 535443997  | 909084757  | 3610954881  | 1813523450 
    l1d_tlb_refill:u   | 80         | 258161216  | 100        | 1795670927  | 898021160  
    l2d_cache:u        | 1801       | 709366888  | 2533       | 4843115497  | 2584458260 
    l2d_cache_refill:u | 913        | 196486319  | 843        | 1254421255  | 791196544  
    l2d_tlb:u          | 102        | 258321622  | 283        | 1795717541  | 898024922  
    l2d_tlb_refill:u   | 5          | 432        | 10         | 37          | 178        
    ll_cache:u         | 280        | 196481257  | 306        | 1254406791  | 791186512  
    ll_cache_miss:u    | 37         | 19740      | 99         | 108412      | 147174     
combined_orders:
    id        | modules                                                                                                                                                        
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld1_pshuf_p1_lp4_r1000+mix_b64_ld4_lin_p128_lp1_r1000+mix_b64_ld14_lin_p1_lp1_r1000+mix_b128_ld14_lin_p128_lp1_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000
    shuffle   | mix_b64_ld14_lin_p1_lp1_r1000+mix_b128_ld14_lin_p128_lp1_r1000+mix_b128_ld1_pshuf_p1_lp4_r1000+mix_b64_ld4_lin_p128_lp1_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000
    sum       | mix_b128_ld1_pshuf_p1_lp4_r1000+mix_b64_ld4_lin_p128_lp1_r1000+mix_b64_ld14_lin_p1_lp1_r1000+mix_b128_ld14_lin_p128_lp1_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 95259379592 | 97111669073 | 78833998717
    instructions:u     | 7353077080  | 7353077091  | 7353320711 
    br_retired:u       | 40013193    | 40013196    | 40024996   
    br_mis_pred:u      | 13573       | 13583       | 13881      
    l1i_cache:u        | 945866295   | 946641758   | 947267650  
    l1i_cache_refill:u | 270754      | 243885      | 47935      
    l1i_tlb:u          | 945866295   | 946641758   | 947267650  
    l1i_tlb_refill:u   | 64          | 96          | 275        
    l2i_cache:u        | 271195      | 244430      | 48120      
    l2i_cache_refill:u | 15892       | 10707       | 4457       
    l2i_tlb:u          | 218         | 290         | 1151       
    l2i_tlb_refill:u   | 34          | 85          | 151        
    l1d_cache:u        | 4034762942  | 4033572225  | 4035887821 
    l1d_cache_refill:u | 2820065250  | 2832239454  | 2824013709 
    l1d_tlb:u          | 7007183623  | 7006174163  | 7010055263 
    l1d_tlb_refill:u   | 2951053267  | 2950226691  | 2951853483 
    l2d_cache:u        | 8170560253  | 8044401419  | 8136944979 
    l2d_cache_refill:u | 2275486641  | 2152544753  | 2242105874 
    l2d_tlb:u          | 2951533652  | 2950684408  | 2952064470 
    l2d_tlb_refill:u   | 206         | 367         | 662        
    ll_cache:u         | 2275437124  | 2152518199  | 2242075146 
    ll_cache_miss:u    | 1042517     | 240563      | 275462     

== combo_055_s5 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b128_ld14_indir_p524288_lp1_r1000
    s1 | mix_b64_ld4_indir_p524288_lp4_r1000  
    s2 | mix_b64_ld4_lin_p128_lp1_r1000       
    s3 | mix_b128_ld1_xpage_p128_lp1_r1000    
    s4 | mix_b128_ld2_xpage_p128_lp4_r1000    
single_counts:
    metric             | s0           | s1          | s2         | s3         | s4        
    -------------------+--------------+-------------+------------+------------+-----------
    cpu-cycles:u       | 452672414522 | 65338922448 | 7168911619 | 3815635029 | 5884011081
    instructions:u     | 2085065389   | 1061065092  | 1061063795 | 2085063801 | 2085063801
    br_retired:u       | 8005247      | 8005195     | 8004922    | 8004920    | 8004920   
    br_mis_pred:u      | 4619         | 2521        | 2280       | 2704       | 2725      
    l1i_cache:u        | 267219907    | 140655921   | 137602172  | 266062021  | 266107681 
    l1i_cache_refill:u | 286537       | 21598       | 2954       | 3687       | 4818      
    l1i_tlb:u          | 267219907    | 140655921   | 137602172  | 266062021  | 266107681 
    l1i_tlb_refill:u   | 586          | 304         | 47         | 47         | 46        
    l2i_cache:u        | 288997       | 21622       | 2960       | 3695       | 4828      
    l2i_cache_refill:u | 11349        | 2877        | 649        | 698        | 749       
    l2i_tlb:u          | 776          | 388         | 93         | 212        | 84        
    l2i_tlb_refill:u   | 581          | 299         | 14         | 14         | 15        
    l1d_cache:u        | 1805344635   | 270651497   | 269440399  | 141061184  | 269064206 
    l1d_cache_refill:u | 1791582669   | 257884225   | 246240611  | 122494424  | 239502886 
    l1d_tlb:u          | 3567244798   | 536102069   | 536056999  | 277649478  | 533536679 
    l1d_tlb_refill:u   | 1738786538   | 251124563   | 258168642  | 130000071  | 258000118 
    l2d_cache:u        | 7112613406   | 1033835257  | 698457325  | 362908770  | 733383583 
    l2d_cache_refill:u | 3612583993   | 518768140   | 185500380  | 106383844  | 144780548 
    l2d_tlb:u          | 1738864473   | 251394787   | 258522264  | 130000452  | 258289102 
    l2d_tlb_refill:u   | 16493238     | 3021347     | 13         | 21         | 16        
    ll_cache:u         | 3611987796   | 518041893   | 185499204  | 106382064  | 144777437 
    ll_cache_miss:u    | 3599522819   | 510031229   | 1009       | 368        | 160276    
combined_orders:
    id        | modules                                                                                                                                                                     
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_indir_p524288_lp1_r1000+mix_b64_ld4_indir_p524288_lp4_r1000+mix_b64_ld4_lin_p128_lp1_r1000+mix_b128_ld1_xpage_p128_lp1_r1000+mix_b128_ld2_xpage_p128_lp4_r1000
    shuffle   | mix_b128_ld14_indir_p524288_lp1_r1000+mix_b128_ld1_xpage_p128_lp1_r1000+mix_b128_ld2_xpage_p128_lp4_r1000+mix_b64_ld4_indir_p524288_lp4_r1000+mix_b64_ld4_lin_p128_lp1_r1000
    sum       | mix_b128_ld14_indir_p524288_lp1_r1000+mix_b64_ld4_indir_p524288_lp4_r1000+mix_b64_ld4_lin_p128_lp1_r1000+mix_b128_ld1_xpage_p128_lp1_r1000+mix_b128_ld2_xpage_p128_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 536578584181 | 534169571838 | 534879894699
    instructions:u     | 8377077311   | 8377077351   | 8377321878  
    br_retired:u       | 40013236     | 40013240     | 40025204    
    br_mis_pred:u      | 16359        | 15835        | 14849       
    l1i_cache:u        | 1079170640   | 1078586167   | 1077647702  
    l1i_cache_refill:u | 735990       | 726645       | 319594      
    l1i_tlb:u          | 1079170640   | 1078586167   | 1077647702  
    l1i_tlb_refill:u   | 2269         | 2234         | 1030        
    l2i_cache:u        | 736966       | 727411       | 322102      
    l2i_cache_refill:u | 180714       | 81772        | 16322       
    l2i_tlb:u          | 2905         | 2984         | 1553        
    l2i_tlb_refill:u   | 2267         | 2221         | 923         
    l1d_cache:u        | 2755342811   | 2753463271   | 2755561921  
    l1d_cache_refill:u | 2656535672   | 2409674004   | 2657704815  
    l1d_tlb:u          | 5455796106   | 5042281990   | 5450590023  
    l1d_tlb_refill:u   | 2635731462   | 2233306627   | 2636079932  
    l2d_cache:u        | 10104758743  | 10454098752  | 9941198341  
    l2d_cache_refill:u | 4733779192   | 4563491355   | 4568016905  
    l2d_tlb:u          | 2636496696   | 2233633453   | 2637071078  
    l2d_tlb_refill:u   | 26122849     | 26761777     | 19514635    
    ll_cache:u         | 4732589275   | 4562337656   | 4566688394  
    ll_cache_miss:u    | 4176726973   | 4261410702   | 4109715701  

== combo_056_s5 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld2_lin_p524288_lp1_r1000  
    s1 | mix_b128_ld1_xpage_p1_lp4_r1000     
    s2 | mix_b128_ld2_indir_p524288_lp1_r1000
    s3 | mix_b128_ld7_indir_p128_lp1_r1000   
    s4 | mix_b64_ld1_pshuf_p1_lp1_r1000      
single_counts:
    metric             | s0          | s1         | s2          | s3          | s4        
    -------------------+-------------+------------+-------------+-------------+-----------
    cpu-cycles:u       | 11010357487 | 530116879  | 64679377210 | 24887895398 | 274100706 
    instructions:u     | 2085063808  | 2085064023 | 2085064998  | 2085064018  | 1061064161
    br_retired:u       | 8004922     | 8004983    | 8005183     | 8004976     | 8005002   
    br_mis_pred:u      | 2669        | 2284       | 3682        | 3144        | 1889      
    l1i_cache:u        | 266894242   | 266043442  | 265680612   | 266791752   | 137044246 
    l1i_cache_refill:u | 12976       | 1039       | 50522       | 18998       | 876       
    l1i_tlb:u          | 266894242   | 266043442  | 265680612   | 266791752   | 137044246 
    l1i_tlb_refill:u   | 130         | 41         | 367         | 56          | 51        
    l2i_cache:u        | 12998       | 1040       | 50606       | 19054       | 878       
    l2i_cache_refill:u | 1170        | 602        | 3658        | 1164        | 557       
    l2i_tlb:u          | 758         | 669        | 461         | 107         | 101       
    l2i_tlb_refill:u   | 122         | 14         | 362         | 33          | 19        
    l1d_cache:u        | 269343944   | 141034098  | 269556037   | 909269133   | 77033732  
    l1d_cache_refill:u | 48223471    | 166        | 254379499   | 862629396   | 132       
    l1d_tlb:u          | 271579270   | 141048713  | 531861985   | 1812679929  | 77047932  
    l1d_tlb_refill:u   | 787837      | 66         | 250411373   | 898154293   | 65        
    l2d_cache:u        | 1144380435  | 1706       | 1105544189  | 2409919649  | 1342      
    l2d_cache_refill:u | 470627709   | 872        | 596653424   | 617125776   | 915       
    l2d_tlb:u          | 792266      | 91         | 250519040   | 898248434   | 432       
    l2d_tlb_refill:u   | 480368      | 4          | 2265872     | 31          | 7         
    ll_cache:u         | 470364281   | 236        | 596509601   | 617120707   | 343       
    ll_cache_miss:u    | 428327350   | 26         | 580335784   | 39811       | 37        
combined_orders:
    id        | modules                                                                                                                                                                 
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld2_lin_p524288_lp1_r1000+mix_b128_ld1_xpage_p1_lp4_r1000+mix_b128_ld2_indir_p524288_lp1_r1000+mix_b128_ld7_indir_p128_lp1_r1000+mix_b64_ld1_pshuf_p1_lp1_r1000
    shuffle   | mix_b128_ld7_indir_p128_lp1_r1000+mix_b64_ld1_pshuf_p1_lp1_r1000+mix_b128_ld2_lin_p524288_lp1_r1000+mix_b128_ld2_indir_p524288_lp1_r1000+mix_b128_ld1_xpage_p1_lp4_r1000
    sum       | mix_b128_ld2_lin_p524288_lp1_r1000+mix_b128_ld1_xpage_p1_lp4_r1000+mix_b128_ld2_indir_p524288_lp1_r1000+mix_b128_ld7_indir_p128_lp1_r1000+mix_b64_ld1_pshuf_p1_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle     | sum         
    -------------------+--------------+-------------+-------------
    cpu-cycles:u       | 101405888736 | 98411190814 | 101381847680
    instructions:u     | 9401076986   | 9401077083  | 9401321008  
    br_retired:u       | 40013181     | 40013194    | 40025066    
    br_mis_pred:u      | 7514         | 7651        | 13668       
    l1i_cache:u        | 1202432517   | 1201604613  | 1202454294  
    l1i_cache_refill:u | 411488       | 378283      | 84411       
    l1i_tlb:u          | 1202432517   | 1201604613  | 1202454294  
    l1i_tlb_refill:u   | 1429         | 1412        | 645         
    l2i_cache:u        | 411709       | 378662      | 84576       
    l2i_cache_refill:u | 43354        | 40006       | 7151        
    l2i_tlb:u          | 1766         | 1785        | 2096        
    l2i_tlb_refill:u   | 1423         | 1406        | 550         
    l1d_cache:u        | 1666056079   | 1666191618  | 1666236944  
    l1d_cache_refill:u | 1184788728   | 1180515532  | 1165232664  
    l1d_tlb:u          | 2836096642   | 2835981954  | 2834217829  
    l1d_tlb_refill:u   | 1149274567   | 1149376038  | 1149353634  
    l2d_cache:u        | 4718398167   | 4761586441  | 4659847321  
    l2d_cache_refill:u | 1735182486   | 1768840709  | 1684408696  
    l2d_tlb:u          | 1149425628   | 1149737709  | 1149560263  
    l2d_tlb_refill:u   | 5988683      | 5251175     | 2746282     
    ll_cache:u         | 1734695260   | 1768315560  | 1683995168  
    ll_cache_miss:u    | 978051472    | 1026128877  | 1008703008  

== combo_057_s5 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b128_ld2_lin_p524288_lp1_r1000   
    s1 | mix_b128_ld14_indir_p524288_lp4_r1000
    s2 | mix_b128_ld7_lin_p524288_lp1_r1000   
    s3 | mix_b128_ld4_pshuf_p128_lp1_r1000    
    s4 | mix_b64_ld1_pshuf_p524288_lp4_r1000  
single_counts:
    metric             | s0          | s1           | s2          | s3          | s4        
    -------------------+-------------+--------------+-------------+-------------+-----------
    cpu-cycles:u       | 11117363427 | 456741333259 | 37136014724 | 14931473733 | 3853153052
    instructions:u     | 2085063795  | 2085065389   | 2085065005  | 2085063795  | 1061063795
    br_retired:u       | 8004922     | 8005247      | 8005184     | 8004922     | 8004922   
    br_mis_pred:u      | 2642        | 5501         | 2998        | 2354        | 2278      
    l1i_cache:u        | 266851834   | 266103064    | 267022079   | 267147135   | 137307338 
    l1i_cache_refill:u | 14143       | 281303       | 36642       | 11706       | 1946      
    l1i_tlb:u          | 266851834   | 266103064    | 267022079   | 267147135   | 137307338 
    l1i_tlb_refill:u   | 126         | 589          | 299         | 65          | 40        
    l2i_cache:u        | 14167       | 281998       | 36718       | 11732       | 1950      
    l2i_cache_refill:u | 887         | 16794        | 1817        | 958         | 1011      
    l2i_tlb:u          | 568         | 968          | 690         | 121         | 475       
    l2i_tlb_refill:u   | 121         | 584          | 293         | 57          | 38        
    l1d_cache:u        | 269333768   | 1805289411   | 910189246   | 525709350   | 77126485  
    l1d_cache_refill:u | 47739541    | 1792621570   | 171346349   | 487589091   | 22655995  
    l1d_tlb:u          | 271555401   | 3568341399   | 917533574   | 1048583666  | 77348860  
    l1d_tlb_refill:u   | 788637      | 1738161824   | 2748931     | 514274768   | 49966     
    l2d_cache:u        | 1161820504  | 7198335711   | 3784227167  | 1430815649  | 272255231 
    l2d_cache_refill:u | 479266387   | 3621749031   | 1553486333  | 387526487   | 129102284 
    l2d_tlb:u          | 793324      | 1738241404   | 2761790     | 514722714   | 49999     
    l2d_tlb_refill:u   | 481041      | 18213801     | 1671885     | 163         | 30163     
    ll_cache:u         | 478975866   | 3618805852   | 1552238612  | 387521197   | 129108549 
    ll_cache_miss:u    | 435792522   | 3566248281   | 1415940772  | 24096       | 106179511 
combined_orders:
    id        | modules                                                                                                                                                                          
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld2_lin_p524288_lp1_r1000+mix_b128_ld14_indir_p524288_lp4_r1000+mix_b128_ld7_lin_p524288_lp1_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp4_r1000
    shuffle   | mix_b128_ld14_indir_p524288_lp4_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp4_r1000+mix_b128_ld2_lin_p524288_lp1_r1000+mix_b128_ld7_lin_p524288_lp1_r1000
    sum       | mix_b128_ld2_lin_p524288_lp1_r1000+mix_b128_ld14_indir_p524288_lp4_r1000+mix_b128_ld7_lin_p524288_lp1_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 524635140217 | 525816875586 | 523779338195
    instructions:u     | 9401077378   | 9401077354   | 9401321779  
    br_retired:u       | 40013244     | 40013241     | 40025197    
    br_mis_pred:u      | 13919        | 13500        | 15773       
    l1i_cache:u        | 1205587709   | 1206089241   | 1204431450  
    l1i_cache_refill:u | 993118       | 968041       | 345740      
    l1i_tlb:u          | 1205587709   | 1206089241   | 1204431450  
    l1i_tlb_refill:u   | 4098         | 3882         | 1119        
    l2i_cache:u        | 993554       | 968671       | 346565      
    l2i_cache_refill:u | 174790       | 163043       | 21467       
    l2i_tlb:u          | 4888         | 4856         | 2822        
    l2i_tlb_refill:u   | 4092         | 3875         | 1093        
    l1d_cache:u        | 3587491992   | 3587644935   | 3587648260  
    l1d_cache_refill:u | 2527409343   | 2529669705   | 2521952546  
    l1d_tlb:u          | 5883026632   | 5890129386   | 5883362900  
    l1d_tlb_refill:u   | 2256375181   | 2256017504   | 2256024126  
    l2d_cache:u        | 13909151170  | 13870498804  | 13847454262 
    l2d_cache_refill:u | 6227239440   | 6208413267   | 6171130522  
    l2d_tlb:u          | 2256662172   | 2256627613   | 2256569231  
    l2d_tlb_refill:u   | 20344444     | 27198944     | 20397053    
    ll_cache:u         | 6223729855   | 6204084083   | 6166650076  
    ll_cache_miss:u    | 5542514453   | 5550600447   | 5524185182  

== combo_058_s5 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b64_ld7_xpage_p524288_lp1_r1000  
    s1 | mix_b64_ld2_lin_p128_lp1_r1000       
    s2 | mix_b64_ld1_pshuf_p512_lp4_r1000     
    s3 | mix_b64_ld1_indir_p512_lp1_r1000     
    s4 | mix_b128_ld14_indir_p524288_lp1_r1000
single_counts:
    metric             | s0           | s1         | s2         | s3         | s4          
    -------------------+--------------+------------+------------+------------+-------------
    cpu-cycles:u       | 113299074585 | 4020462951 | 2739989776 | 2910328289 | 452248124354
    instructions:u     | 1061065143   | 1061063801 | 1061063795 | 1061063815 | 2085065357  
    br_retired:u       | 8005202      | 8004920    | 8004922    | 8004924    | 8005242     
    br_mis_pred:u      | 3355         | 2584       | 2071       | 2497       | 5130        
    l1i_cache:u        | 141585167    | 138097009  | 138350745  | 138089880  | 270997579   
    l1i_cache_refill:u | 37023        | 2041       | 1562       | 1432       | 271996      
    l1i_tlb:u          | 141585167    | 138097009  | 138350745  | 138089880  | 270997579   
    l1i_tlb_refill:u   | 357          | 48         | 51         | 35         | 586         
    l2i_cache:u        | 37095        | 2044       | 1565       | 1431       | 272853      
    l2i_cache_refill:u | 4007         | 605        | 934        | 552        | 10698       
    l2i_tlb:u          | 414          | 285        | 149        | 114        | 1139        
    l2i_tlb_refill:u   | 353          | 13         | 38         | 23         | 581         
    l1d_cache:u        | 462612343    | 141057529  | 77122853   | 77038996   | 1805309848  
    l1d_cache_refill:u | 446841399    | 122482162  | 33718236   | 64501302   | 1791551416  
    l1d_tlb:u          | 911342260    | 277156035  | 103136201  | 148602097  | 3564397784  
    l1d_tlb_refill:u   | 437244745    | 130000135  | 17000241   | 66000950   | 1737702277  
    l2d_cache:u        | 1868206053   | 386860234  | 204616194  | 262139101  | 7110952387  
    l2d_cache_refill:u | 981848409    | 123734545  | 88928853   | 128045990  | 3613450076  
    l2d_tlb:u          | 437308051    | 130432302  | 17000306   | 66001274   | 1737779322  
    l2d_tlb_refill:u   | 4347682      | 18         | 182        | 518        | 14786461    
    ll_cache:u         | 981649802    | 123732857  | 88923047   | 128044163  | 3612170249  
    ll_cache_miss:u    | 975834358    | 278        | 102453     | 767        | 3599979189  
combined_orders:
    id        | modules                                                                                                                                                                   
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_xpage_p524288_lp1_r1000+mix_b64_ld2_lin_p128_lp1_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000
    shuffle   | mix_b64_ld2_lin_p128_lp1_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000
    sum       | mix_b64_ld7_xpage_p524288_lp1_r1000+mix_b64_ld2_lin_p128_lp1_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 576663044257 | 576077971444 | 575217979955
    instructions:u     | 6329077378   | 6329077335   | 6329321911  
    br_retired:u       | 40013244     | 40013239     | 40025210    
    br_mis_pred:u      | 21468        | 21191        | 15637       
    l1i_cache:u        | 824197902    | 820456319    | 827120380   
    l1i_cache_refill:u | 655296       | 654462       | 314054      
    l1i_tlb:u          | 824197902    | 820456319    | 827120380   
    l1i_tlb_refill:u   | 1982         | 1989         | 1077        
    l2i_cache:u        | 656129       | 655461       | 314988      
    l2i_cache_refill:u | 117982       | 109526       | 16796       
    l2i_tlb:u          | 4993         | 4958         | 2101        
    l2i_tlb_refill:u   | 1978         | 1974         | 1008        
    l1d_cache:u        | 2566048023   | 2563096254   | 2563141569  
    l1d_cache_refill:u | 2459949684   | 2455777640   | 2459094515  
    l1d_tlb:u          | 5021155552   | 5017559465   | 5004634377  
    l1d_tlb_refill:u   | 2390994752   | 2388325891   | 2387948348  
    l2d_cache:u        | 9857119467   | 9862299341   | 9832773969  
    l2d_cache_refill:u | 4967490783   | 4955480215   | 4936007873  
    l2d_tlb:u          | 2391203527   | 2388474986   | 2388521255  
    l2d_tlb_refill:u   | 27879605     | 31522980     | 19134861    
    ll_cache:u         | 4966437827   | 4954379750   | 4934520118  
    ll_cache_miss:u    | 4599402762   | 4594308742   | 4575917045  

== combo_059_s5 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld1_lin_p128_lp1_r1000     
    s1 | mix_b64_ld4_pshuf_p524288_lp1_r1000 
    s2 | mix_b128_ld14_indir_p128_lp4_r1000  
    s3 | mix_b128_ld1_pshuf_p524288_lp4_r1000
    s4 | mix_b64_ld7_indir_p524288_lp1_r1000 
single_counts:
    metric             | s0         | s1          | s2          | s3          | s4          
    -------------------+------------+-------------+-------------+-------------+-------------
    cpu-cycles:u       | 3793036195 | 11088605818 | 40233197031 | 10000669728 | 113258148574
    instructions:u     | 2085063801 | 1061063795  | 2085065103  | 2085063801  | 1061065025  
    br_retired:u       | 8004920    | 8004922     | 8005197     | 8004920     | 8005187     
    br_mis_pred:u      | 2503       | 2838        | 3398        | 2918        | 3331        
    l1i_cache:u        | 266093265  | 137804026   | 266696510   | 266640563   | 139508592   
    l1i_cache_refill:u | 3746       | 4589        | 30422       | 11456       | 36497       
    l1i_tlb:u          | 266093265  | 137804026   | 266696510   | 266640563   | 139508592   
    l1i_tlb_refill:u   | 46         | 123         | 46          | 110         | 370         
    l2i_cache:u        | 3753       | 4601        | 30512       | 11480       | 36588       
    l2i_cache_refill:u | 660        | 774         | 2243        | 2296        | 3808        
    l2i_tlb:u          | 103        | 377         | 230         | 679         | 444         
    l2i_tlb_refill:u   | 15         | 115         | 17          | 104         | 365         
    l1d_cache:u        | 141076442  | 269432349   | 1806731720  | 141209846   | 462609854   
    l1d_cache_refill:u | 122634810  | 48251066    | 1673463755  | 56014928    | 446755899   
    l1d_tlb:u          | 279365496  | 271581076   | 3280939227  | 141644175   | 911682394   
    l1d_tlb_refill:u   | 131000104  | 807310      | 1459226386  | 107198      | 437164657   
    l2d_cache:u        | 346238071  | 1147802197  | 4653469048  | 484305071   | 1870563786  
    l2d_cache_refill:u | 90182069   | 476258855   | 1106941347  | 228736271   | 983568367   
    l2d_tlb:u          | 131000460  | 811762      | 1459260961  | 110816      | 437227796   
    l2d_tlb_refill:u   | 51         | 480947      | 29          | 67483       | 4773177     
    ll_cache:u         | 90181196   | 475988279   | 1106915430  | 228754294   | 983363742   
    ll_cache_miss:u    | 2339       | 434026496   | 174808      | 189617644   | 977535860   
combined_orders:
    id        | modules                                                                                                                                                                        
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld1_lin_p128_lp1_r1000+mix_b64_ld4_pshuf_p524288_lp1_r1000+mix_b128_ld14_indir_p128_lp4_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000+mix_b64_ld7_indir_p524288_lp1_r1000
    shuffle   | mix_b128_ld1_lin_p128_lp1_r1000+mix_b64_ld7_indir_p524288_lp1_r1000+mix_b128_ld14_indir_p128_lp4_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000+mix_b64_ld4_pshuf_p524288_lp1_r1000
    sum       | mix_b128_ld1_lin_p128_lp1_r1000+mix_b64_ld4_pshuf_p524288_lp1_r1000+mix_b128_ld14_indir_p128_lp4_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000+mix_b64_ld7_indir_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 178697338870 | 175644201582 | 178373657346
    instructions:u     | 8377077187   | 8377077160   | 8377321525  
    br_retired:u       | 40013216     | 40013212     | 40025146    
    br_mis_pred:u      | 12757        | 13813        | 14988       
    l1i_cache:u        | 1082989719   | 1082147203   | 1076742956  
    l1i_cache_refill:u | 493489       | 473754       | 86710       
    l1i_tlb:u          | 1082989719   | 1082147203   | 1076742956  
    l1i_tlb_refill:u   | 2260         | 2116         | 695         
    l2i_cache:u        | 493770       | 473977       | 86934       
    l2i_cache_refill:u | 105259       | 105686       | 9781        
    l2i_tlb:u          | 2643         | 2887         | 1833        
    l2i_tlb_refill:u   | 2252         | 2106         | 616         
    l1d_cache:u        | 2824356383   | 2821927108   | 2821060211  
    l1d_cache_refill:u | 2352325519   | 2355901955   | 2347120458  
    l1d_tlb:u          | 4891068415   | 4899355798   | 4885212368  
    l1d_tlb_refill:u   | 2029736118   | 2031441252   | 2028305655  
    l2d_cache:u        | 8624979569   | 8320133375   | 8502378173  
    l2d_cache_refill:u | 2981587662   | 2694178045   | 2885686909  
    l2d_tlb:u          | 2029885580   | 2031628049   | 2028411795  
    l2d_tlb_refill:u   | 7705115      | 8601033      | 5321687     
    ll_cache:u         | 2981807590   | 2693503131   | 2885202941  
    ll_cache_miss:u    | 1671452279   | 1567614519   | 1601357147  

== combo_060_s5 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld14_indir_p1_lp1_r1000 
    s1 | mix_b128_ld2_pshuf_p128_lp1_r1000
    s2 | mix_b128_ld1_pshuf_p512_lp4_r1000
    s3 | mix_b64_ld4_indir_p128_lp4_r1000 
    s4 | mix_b64_ld1_xpage_p1_lp1_r1000   
single_counts:
    metric             | s0         | s1         | s2         | s3         | s4        
    -------------------+------------+------------+------------+------------+-----------
    cpu-cycles:u       | 7186298311 | 6910689132 | 5316604119 | 5293261649 | 274096512 
    instructions:u     | 2085063792 | 2085063801 | 2085063795 | 1061063801 | 1061064161
    br_retired:u       | 8004919    | 8004920    | 8004922    | 8004920    | 8005002   
    br_mis_pred:u      | 3030       | 2944       | 2848       | 2096       | 2128      
    l1i_cache:u        | 266068364  | 265104577  | 266344886  | 138547363  | 137041520 
    l1i_cache_refill:u | 5851       | 5946       | 4949       | 2945       | 635       
    l1i_tlb:u          | 266068364  | 265104577  | 266344886  | 138547363  | 137041520 
    l1i_tlb_refill:u   | 46         | 45         | 46         | 43         | 41        
    l2i_cache:u        | 5861       | 5955       | 4958       | 2948       | 637       
    l2i_cache_refill:u | 656        | 676        | 1380       | 581        | 541       
    l2i_tlb:u          | 260        | 116        | 99         | 89         | 86        
    l2i_tlb_refill:u   | 17         | 22         | 26         | 14         | 13        
    l1d_cache:u        | 1805038639 | 269058103  | 141166372  | 269315165  | 77034511  
    l1d_cache_refill:u | 167        | 240198857  | 65567150   | 235678533  | 152       
    l1d_tlb:u          | 1805086114 | 532911238  | 191951567  | 487787914  | 77049503  
    l1d_tlb_refill:u   | 150        | 258000139  | 34016702   | 211480065  | 64        
    l2d_cache:u        | 6348       | 719229850  | 408916624  | 622709478  | 1396      
    l2d_cache_refill:u | 936        | 186026839  | 177713218  | 97635943   | 868       
    l2d_tlb:u          | 175        | 258003016  | 34016965   | 211614551  | 285       
    l2d_tlb_refill:u   | 5          | 41         | 161        | 41         | 13        
    ll_cache:u         | 327        | 186024700  | 177701874  | 97634382   | 288       
    ll_cache_miss:u    | 106        | 2600       | 238085     | 5577       | 31        
combined_orders:
    id        | modules                                                                                                                                                             
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_indir_p1_lp1_r1000+mix_b128_ld2_pshuf_p128_lp1_r1000+mix_b128_ld1_pshuf_p512_lp4_r1000+mix_b64_ld4_indir_p128_lp4_r1000+mix_b64_ld1_xpage_p1_lp1_r1000
    shuffle   | mix_b128_ld2_pshuf_p128_lp1_r1000+mix_b128_ld1_pshuf_p512_lp4_r1000+mix_b64_ld4_indir_p128_lp4_r1000+mix_b64_ld1_xpage_p1_lp1_r1000+mix_b128_ld14_indir_p1_lp1_r1000
    sum       | mix_b128_ld14_indir_p1_lp1_r1000+mix_b128_ld2_pshuf_p128_lp1_r1000+mix_b128_ld1_pshuf_p512_lp4_r1000+mix_b64_ld4_indir_p128_lp4_r1000+mix_b64_ld1_xpage_p1_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 28382875140 | 31215286421 | 24980949723
    instructions:u     | 8377077103  | 8377076927  | 8377319350 
    br_retired:u       | 40013197    | 40013173    | 40024683   
    br_mis_pred:u      | 8290        | 6558        | 13046      
    l1i_cache:u        | 1074267448  | 1074437243  | 1073106710 
    l1i_cache_refill:u | 184026      | 190288      | 20326      
    l1i_tlb:u          | 1074267448  | 1074437243  | 1073106710 
    l1i_tlb_refill:u   | 75          | 65          | 221        
    l2i_cache:u        | 184186      | 190386      | 20359      
    l2i_cache_refill:u | 23678       | 25211       | 3834       
    l2i_tlb:u          | 130         | 809         | 650        
    l2i_tlb_refill:u   | 58          | 50          | 92         
    l1d_cache:u        | 2561540367  | 2561564812  | 2561612790 
    l1d_cache_refill:u | 550302888   | 546449602   | 541444859  
    l1d_tlb:u          | 3095423906  | 3095636697  | 3094786336 
    l1d_tlb_refill:u   | 503444971   | 503474027   | 503497120  
    l2d_cache:u        | 1791898458  | 1865406231  | 1750863696 
    l2d_cache_refill:u | 538784629   | 595238596   | 461377804  
    l2d_tlb:u          | 504098351   | 503745471   | 503634992  
    l2d_tlb_refill:u   | 2979        | 2342        | 261        
    ll_cache:u         | 538745652   | 595198195   | 461361571  
    ll_cache_miss:u    | 755515      | 1896143     | 246399     

== combo_061_s5 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld2_indir_p1_lp1_r1000  
    s1 | mix_b128_ld2_pshuf_p512_lp1_r1000
    s2 | mix_b64_ld7_xpage_p512_lp4_r1000 
    s3 | mix_b128_ld4_lin_p512_lp1_r1000  
    s4 | mix_b64_ld2_lin_p512_lp1_r1000   
single_counts:
    metric             | s0         | s1          | s2          | s3          | s4        
    -------------------+------------+-------------+-------------+-------------+-----------
    cpu-cycles:u       | 1042104542 | 10904415458 | 20015739403 | 21708108905 | 5469031930
    instructions:u     | 2085064014 | 2085063795  | 1061063801  | 2085064018  | 1061063795
    br_retired:u       | 8004982    | 8004922     | 8004920     | 8004976     | 8004922   
    br_mis_pred:u      | 2480       | 2125        | 3303        | 2274        | 2665      
    l1i_cache:u        | 266057943  | 267124263   | 137211154   | 267752650   | 137106989 
    l1i_cache_refill:u | 1487       | 9264        | 7161        | 16067       | 2360      
    l1i_tlb:u          | 266057943  | 267124263   | 137211154   | 267752650   | 137106989 
    l1i_tlb_refill:u   | 43         | 47          | 48          | 54          | 44        
    l2i_cache:u        | 1490       | 9287        | 7176        | 16115       | 2367      
    l2i_cache_refill:u | 596        | 745         | 1377        | 928         | 611       
    l2i_tlb:u          | 97         | 138         | 363         | 133         | 127       
    l2i_tlb_refill:u   | 11         | 31          | 25          | 41          | 23        
    l1d_cache:u        | 269038126  | 269070980   | 461156042   | 525881621   | 141065536 
    l1d_cache_refill:u | 181        | 252056588   | 447892183   | 512433437   | 127556930 
    l1d_tlb:u          | 269065412  | 533333223   | 915408708   | 1048497112  | 276897542 
    l1d_tlb_refill:u   | 72         | 258021093   | 450098821   | 514322163   | 130017577 
    l2d_cache:u        | 2125       | 1102453236  | 1798731458  | 2023322032  | 514439802 
    l2d_cache_refill:u | 815        | 531975184   | 906154036   | 1024495494  | 256126607 
    l2d_tlb:u          | 96         | 258029243   | 450107230   | 514414435   | 130027552 
    l2d_tlb_refill:u   | 6          | 197         | 847         | 696         | 227       
    ll_cache:u         | 222        | 531963209   | 906144592   | 1024485692  | 256123843 
    ll_cache_miss:u    | 36         | 6967325     | 6200729     | 59534       | 1904      
combined_orders:
    id        | modules                                                                                                                                                          
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld2_indir_p1_lp1_r1000+mix_b128_ld2_pshuf_p512_lp1_r1000+mix_b64_ld7_xpage_p512_lp4_r1000+mix_b128_ld4_lin_p512_lp1_r1000+mix_b64_ld2_lin_p512_lp1_r1000
    shuffle   | mix_b128_ld4_lin_p512_lp1_r1000+mix_b64_ld7_xpage_p512_lp4_r1000+mix_b64_ld2_lin_p512_lp1_r1000+mix_b128_ld2_indir_p1_lp1_r1000+mix_b128_ld2_pshuf_p512_lp1_r1000
    sum       | mix_b128_ld2_indir_p1_lp1_r1000+mix_b128_ld2_pshuf_p512_lp1_r1000+mix_b64_ld7_xpage_p512_lp4_r1000+mix_b128_ld4_lin_p512_lp1_r1000+mix_b64_ld2_lin_p512_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum        
    -------------------+--------------+--------------+------------
    cpu-cycles:u       | 101429041673 | 101517374359 | 59139400238
    instructions:u     | 8377077083   | 8377077040   | 8377319423 
    br_retired:u       | 40013194     | 40013189     | 40024722   
    br_mis_pred:u      | 13367        | 13397        | 12847      
    l1i_cache:u        | 1073868826   | 1073824000   | 1075252999 
    l1i_cache_refill:u | 315947       | 312948       | 36339      
    l1i_tlb:u          | 1073868826   | 1073824000   | 1075252999 
    l1i_tlb_refill:u   | 76           | 73           | 236        
    l2i_cache:u        | 316026       | 313056       | 36435      
    l2i_cache_refill:u | 32075        | 26480        | 4257       
    l2i_tlb:u          | 260          | 212          | 858        
    l2i_tlb_refill:u   | 69           | 70           | 131        
    l1d_cache:u        | 1667849802   | 1666312225   | 1666212305 
    l1d_cache_refill:u | 1348771292   | 1343008598   | 1339939319 
    l1d_tlb:u          | 3066540296   | 3046179781   | 3043201997 
    l1d_tlb_refill:u   | 1357458249   | 1352533240   | 1352459726 
    l2d_cache:u        | 5388250681   | 5362444214   | 5438948653 
    l2d_cache_refill:u | 2699870915   | 2695307411   | 2718752136 
    l2d_tlb:u          | 1359936541   | 1352646128   | 1352578556 
    l2d_tlb_refill:u   | 2153854      | 2166084      | 1973       
    ll_cache:u         | 2699776866   | 2695215749   | 2718717558 
    ll_cache_miss:u    | 28233995     | 27118191     | 13229528   

== combo_062_s5 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld14_pshuf_p1_lp1_r1000     
    s1 | mix_b128_ld14_xpage_p1_lp1_r1000    
    s2 | mix_b128_ld14_pshuf_p512_lp4_r1000  
    s3 | mix_b128_ld1_pshuf_p524288_lp1_r1000
    s4 | mix_b64_ld14_lin_p128_lp4_r1000     
single_counts:
    metric             | s0         | s1         | s2          | s3         | s4         
    -------------------+------------+------------+-------------+------------+------------
    cpu-cycles:u       | 3602135718 | 7186358531 | 60096317743 | 5409774228 | 14716648947
    instructions:u     | 1061063792 | 2085063792 | 2085065052  | 2085063795 | 1061063795 
    br_retired:u       | 8004919    | 8004919    | 8005191     | 8004922    | 8004922    
    br_mis_pred:u      | 2560       | 2922       | 3373        | 2371       | 3100       
    l1i_cache:u        | 138056215  | 266068156  | 267347735   | 266546511  | 137728060  
    l1i_cache_refill:u | 1828       | 6181       | 43884       | 5500       | 5328       
    l1i_tlb:u          | 138056215  | 266068156  | 267347735   | 266546511  | 137728060  
    l1i_tlb_refill:u   | 56         | 49         | 44          | 59         | 44         
    l2i_cache:u        | 1838       | 6195       | 43981       | 5510       | 5336       
    l2i_cache_refill:u | 602        | 695        | 9515        | 842        | 974        
    l2i_tlb:u          | 204        | 107        | 135         | 640        | 97         
    l2i_tlb_refill:u   | 21         | 12         | 27          | 54         | 12         
    l1d_cache:u        | 909038299  | 1805038572 | 1807827634  | 141165383  | 909837438  
    l1d_cache_refill:u | 183        | 225        | 574165359   | 24724339   | 217333789  
    l1d_tlb:u          | 909084605  | 1805086007 | 2454312543  | 142399296  | 1209236960 
    l1d_tlb_refill:u   | 103        | 124        | 450573816   | 394322     | 226159389  
    l2d_cache:u        | 2378       | 6390       | 7156631103  | 546393652  | 2776548028 
    l2d_cache_refill:u | 837        | 940        | 3130260791  | 226734654  | 544972201  
    l2d_tlb:u          | 136        | 145        | 450708731   | 395158     | 226209366  
    l2d_tlb_refill:u   | 6          | 3          | 432         | 236794     | 11         
    ll_cache:u         | 277        | 296        | 3129868513  | 226577332  | 544939284  
    ll_cache_miss:u    | 49         | 38         | 113113242   | 207894074  | 5288248    
combined_orders:
    id        | modules                                                                                                                                                                 
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_pshuf_p1_lp1_r1000+mix_b128_ld14_xpage_p1_lp1_r1000+mix_b128_ld14_pshuf_p512_lp4_r1000+mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld14_lin_p128_lp4_r1000
    shuffle   | mix_b128_ld14_xpage_p1_lp1_r1000+mix_b128_ld14_pshuf_p512_lp4_r1000+mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld14_pshuf_p1_lp1_r1000+mix_b64_ld14_lin_p128_lp4_r1000
    sum       | mix_b64_ld14_pshuf_p1_lp1_r1000+mix_b128_ld14_xpage_p1_lp1_r1000+mix_b128_ld14_pshuf_p512_lp4_r1000+mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld14_lin_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 98818478748 | 99466813846 | 91011235167
    instructions:u     | 8377077049  | 8377077076  | 8377320226 
    br_retired:u       | 40013190    | 40013194    | 40024873   
    br_mis_pred:u      | 13321       | 13061       | 14326      
    l1i_cache:u        | 1072742001  | 1075170298  | 1075746677 
    l1i_cache_refill:u | 373172      | 375146      | 62721      
    l1i_tlb:u          | 1072742001  | 1075170298  | 1075746677 
    l1i_tlb_refill:u   | 887         | 802         | 252        
    l2i_cache:u        | 373395      | 375260      | 62860      
    l2i_cache_refill:u | 91075       | 69905       | 12628      
    l2i_tlb:u          | 1771        | 1726        | 1183       
    l2i_tlb_refill:u   | 882         | 797         | 126        
    l1d_cache:u        | 5573186540  | 5573073753  | 5572907326 
    l1d_cache_refill:u | 841577062   | 840709830   | 816223895  
    l1d_tlb:u          | 6498474294  | 6503407822  | 6520119411 
    l1d_tlb_refill:u   | 677225888   | 677197928   | 677127754  
    l2d_cache:u        | 10354582394 | 10340647600 | 10479581551
    l2d_cache_refill:u | 4026191120  | 3997767424  | 3901969423 
    l2d_tlb:u          | 677560836   | 677489333   | 677313536  
    l2d_tlb_refill:u   | 707557      | 712632      | 237246     
    ll_cache:u         | 4025108468  | 3996815345  | 3901385702 
    ll_cache_miss:u    | 906816393   | 862164645   | 326295651  

== combo_063_s5 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld14_lin_p524288_lp1_r1000 
    s1 | mix_b128_ld1_lin_p1_lp1_r1000      
    s2 | mix_b128_ld4_lin_p1_lp1_r1000      
    s3 | mix_b64_ld1_pshuf_p524288_lp1_r1000
    s4 | mix_b64_ld14_xpage_p128_lp1_r1000  
single_counts:
    metric             | s0          | s1         | s2         | s3         | s4         
    -------------------+-------------+------------+------------+------------+------------
    cpu-cycles:u       | 37168170793 | 530118203  | 2067391467 | 2670638198 | 23663472421
    instructions:u     | 1061065053  | 2085064014 | 2085064014 | 1061063795 | 1061064012 
    br_retired:u       | 8005190     | 8004982    | 8004982    | 8004922    | 8004978    
    br_mis_pred:u      | 3299        | 2294       | 2406       | 2050       | 3470       
    l1i_cache:u        | 139723370   | 266041425  | 265113563  | 137300950  | 138459931  
    l1i_cache_refill:u | 12971       | 1032       | 2358       | 1528       | 8095       
    l1i_tlb:u          | 139723370   | 266041425  | 265113563  | 137300950  | 138459931  
    l1i_tlb_refill:u   | 236         | 40         | 46         | 43         | 50         
    l2i_cache:u        | 12997       | 1036       | 2359       | 1534       | 8114       
    l2i_cache_refill:u | 1802        | 596        | 615        | 605        | 799        
    l2i_tlb:u          | 505         | 818        | 104        | 458        | 181        
    l2i_tlb_refill:u   | 232         | 12         | 11         | 39         | 16         
    l1d_cache:u        | 910243507   | 141033865  | 525081940  | 77106597   | 909060395  
    l1d_cache_refill:u | 170017895   | 151        | 187        | 12298056   | 860318430  
    l1d_tlb:u          | 917032006   | 141048042  | 525135868  | 77747697   | 1814357311 
    l1d_tlb_refill:u   | 2749189     | 83         | 93         | 197573     | 898017413  
    l2d_cache:u        | 3797727167  | 1867       | 3038       | 276035229  | 2554716201 
    l2d_cache_refill:u | 1561888871  | 950        | 924        | 114235014  | 746982795  
    l2d_tlb:u          | 2761814     | 116        | 148        | 197607     | 898021662  
    l2d_tlb_refill:u   | 1673047     | 3          | 7          | 117897     | 118        
    ll_cache:u         | 1560975656  | 297        | 270        | 114164793  | 746973963  
    ll_cache_miss:u    | 1423210500  | 39         | 39         | 104711991  | 27292      
combined_orders:
    id        | modules                                                                                                                                                             
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_lin_p524288_lp1_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b128_ld4_lin_p1_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld14_xpage_p128_lp1_r1000
    shuffle   | mix_b128_ld1_lin_p1_lp1_r1000+mix_b64_ld14_lin_p524288_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000+mix_b128_ld4_lin_p1_lp1_r1000+mix_b64_ld14_xpage_p128_lp1_r1000
    sum       | mix_b64_ld14_lin_p524288_lp1_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b128_ld4_lin_p1_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld14_xpage_p128_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 68253437841 | 66734976404 | 66099791082
    instructions:u     | 7353077076  | 7353077089  | 7353320888 
    br_retired:u       | 40013194    | 40013194    | 40025054   
    br_mis_pred:u      | 13226       | 12885       | 13519      
    l1i_cache:u        | 948151467   | 948367627   | 946639239  
    l1i_cache_refill:u | 199449      | 212380      | 25984      
    l1i_tlb:u          | 948151467   | 948367627   | 946639239  
    l1i_tlb_refill:u   | 987         | 981         | 415        
    l2i_cache:u        | 199943      | 212501      | 26040      
    l2i_cache_refill:u | 13905       | 13637       | 4417       
    l2i_tlb:u          | 1774        | 1608        | 2066       
    l2i_tlb_refill:u   | 983         | 977         | 310        
    l1d_cache:u        | 2564037030  | 2562629114  | 2562526304 
    l1d_cache_refill:u | 1040945810  | 1042292597  | 1042634719 
    l1d_tlb:u          | 3479464472  | 3475870692  | 3475320924 
    l1d_tlb_refill:u   | 901969577   | 900997883   | 900964351  
    l2d_cache:u        | 6564912033  | 6701315244  | 6628483502 
    l2d_cache_refill:u | 2356897679  | 2514533167  | 2423108554 
    l2d_tlb:u          | 902043347   | 901029037   | 900981347  
    l2d_tlb_refill:u   | 2251267     | 2252814     | 1791072    
    ll_cache:u         | 2355839216  | 2513511286  | 2422114979 
    ll_cache_miss:u    | 1522653263  | 1522161656  | 1527949861 

== combo_064_s5 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld2_indir_p1_lp1_r1000     
    s1 | mix_b128_ld1_xpage_p128_lp4_r1000  
    s2 | mix_b64_ld1_indir_p1_lp4_r1000     
    s3 | mix_b64_ld1_lin_p524288_lp1_r1000  
    s4 | mix_b64_ld7_xpage_p524288_lp1_r1000
single_counts:
    metric             | s0         | s1         | s2         | s3         | s4          
    -------------------+------------+------------+------------+------------+-------------
    cpu-cycles:u       | 530949647  | 3319091208 | 274096986  | 2683850571 | 113266064849
    instructions:u     | 1061064014 | 2085063795 | 1061064170 | 1061063801 | 1061065100  
    br_retired:u       | 8004982    | 8004922    | 8005003    | 8004920    | 8005197     
    br_mis_pred:u      | 2320       | 2078       | 2002       | 2060       | 3529        
    l1i_cache:u        | 138086645  | 265274101  | 138042775  | 138264773  | 140561280   
    l1i_cache_refill:u | 731        | 3231       | 708        | 1515       | 37476       
    l1i_tlb:u          | 138086645  | 265274101  | 138042775  | 138264773  | 140561280   
    l1i_tlb_refill:u   | 40         | 48         | 40         | 40         | 364         
    l2i_cache:u        | 732        | 3246       | 708        | 1519       | 37585       
    l2i_cache_refill:u | 514        | 622        | 547        | 585        | 4032        
    l2i_tlb:u          | 82         | 341        | 74         | 753        | 434         
    l2i_tlb_refill:u   | 10         | 14         | 10         | 38         | 359         
    l1d_cache:u        | 141053000  | 141097443  | 77033536   | 77105795   | 463736219   
    l1d_cache_refill:u | 162        | 116901448  | 146        | 12377082   | 447707422   
    l1d_tlb:u          | 141095222  | 277701288  | 77047680   | 77742962   | 918708628   
    l1d_tlb_refill:u   | 66         | 130000075  | 65         | 197955     | 439254206   
    l2d_cache:u        | 1380       | 408495629  | 1234       | 274622834  | 1872999107  
    l2d_cache_refill:u | 801        | 80675309   | 812        | 113579523  | 984023594   
    l2d_tlb:u          | 188        | 130029421  | 441        | 197986     | 439290501   
    l2d_tlb_refill:u   | 5          | 13         | 3          | 117972     | 4871669     
    ll_cache:u         | 251        | 80673846   | 269        | 113511748  | 983807009   
    ll_cache_miss:u    | 23         | 7230       | 30         | 104179342  | 976158645   
combined_orders:
    id        | modules                                                                                                                                                              
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld2_indir_p1_lp1_r1000+mix_b128_ld1_xpage_p128_lp4_r1000+mix_b64_ld1_indir_p1_lp4_r1000+mix_b64_ld1_lin_p524288_lp1_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000
    shuffle   | mix_b64_ld2_indir_p1_lp1_r1000+mix_b64_ld1_lin_p524288_lp1_r1000+mix_b128_ld1_xpage_p128_lp4_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000+mix_b64_ld1_indir_p1_lp4_r1000
    sum       | mix_b64_ld2_indir_p1_lp1_r1000+mix_b128_ld1_xpage_p128_lp4_r1000+mix_b64_ld1_indir_p1_lp4_r1000+mix_b64_ld1_lin_p524288_lp1_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 121286127769 | 121221874159 | 120074053261
    instructions:u     | 6329077083   | 6329077110   | 6329320880  
    br_retired:u       | 40013194     | 40013198     | 40025024    
    br_mis_pred:u      | 12835        | 7308         | 11989       
    l1i_cache:u        | 824261593    | 820453131    | 820229574   
    l1i_cache_refill:u | 235320       | 233205       | 43661       
    l1i_tlb:u          | 824261593    | 820453131    | 820229574   
    l1i_tlb_refill:u   | 1262         | 1132         | 532         
    l2i_cache:u        | 236263       | 233867       | 43790       
    l2i_cache_refill:u | 31092        | 43377        | 6300        
    l2i_tlb:u          | 1870         | 1753         | 1684        
    l2i_tlb_refill:u   | 1257         | 1128         | 431         
    l1d_cache:u        | 901633396    | 898868530    | 900025993   
    l1d_cache_refill:u | 578631858    | 575649963    | 576986260   
    l1d_tlb:u          | 1493399681   | 1486110198   | 1492295780  
    l1d_tlb_refill:u   | 569546988    | 567356018    | 569452367   
    l2d_cache:u        | 2557143170   | 2551860917   | 2556120184  
    l2d_cache_refill:u | 1179002961   | 1182744570   | 1178280039  
    l2d_tlb:u          | 569786652    | 567486260    | 569518537   
    l2d_tlb_refill:u   | 6494486      | 5659842      | 4989662     
    ll_cache:u         | 1178649835   | 1182359367   | 1177993123  
    ll_cache_miss:u    | 1074292187   | 1079203619   | 1080345270  

== combo_065_s5 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b128_ld4_lin_p1_lp1_r1000      
    s1 | mix_b64_ld4_indir_p524288_lp1_r1000
    s2 | mix_b128_ld7_pshuf_p128_lp1_r1000  
    s3 | mix_b64_ld1_pshuf_p512_lp4_r1000   
    s4 | mix_b128_ld1_lin_p1_lp1_r1000      
single_counts:
    metric             | s0         | s1          | s2          | s3         | s4        
    -------------------+------------+-------------+-------------+------------+-----------
    cpu-cycles:u       | 2066904524 | 64759618678 | 20436539462 | 2692489769 | 530106738 
    instructions:u     | 2085064020 | 1061065116  | 2085063801  | 1061063795 | 2085064014
    br_retired:u       | 8004980    | 8005198     | 8004920     | 8004922    | 8004982   
    br_mis_pred:u      | 2424       | 2416        | 3170        | 2038       | 2266      
    l1i_cache:u        | 266060598  | 140431040   | 265399014   | 138301559  | 265039151 
    l1i_cache_refill:u | 2203       | 21919       | 15702       | 1476       | 1034      
    l1i_tlb:u          | 266060598  | 140431040   | 265399014   | 138301559  | 265039151 
    l1i_tlb_refill:u   | 45         | 302         | 50          | 40         | 42        
    l2i_cache:u        | 2211       | 21971       | 15738       | 1477       | 1035      
    l2i_cache_refill:u | 617        | 1969        | 962         | 880        | 609       
    l2i_tlb:u          | 252        | 375         | 167         | 146        | 825       
    l2i_tlb_refill:u   | 13         | 298         | 17          | 23         | 14        
    l1d_cache:u        | 525038837  | 270422685   | 909561898   | 77113958   | 141033897 
    l1d_cache_refill:u | 192        | 256099429   | 858905107   | 34426206   | 141       
    l1d_tlb:u          | 525084477  | 535256586   | 1814614172  | 105214294  | 141048107 
    l1d_tlb_refill:u   | 99         | 250939971   | 898381606   | 17500303   | 76        
    l2d_cache:u        | 2950       | 1049531615  | 2384307764  | 203668561  | 1918      
    l2d_cache_refill:u | 871        | 544694927   | 590735577   | 88882552   | 1003      
    l2d_tlb:u          | 129        | 251176735   | 898397684   | 17500413   | 101       
    l2d_tlb_refill:u   | 5          | 2756236     | 24          | 497        | 5         
    ll_cache:u         | 252        | 544585270   | 590732782   | 88877078   | 347       
    ll_cache_miss:u    | 44         | 536035993   | 34881       | 152753     | 59        
combined_orders:
    id        | modules                                                                                                                                                           
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld4_lin_p1_lp1_r1000+mix_b64_ld4_indir_p524288_lp1_r1000+mix_b128_ld7_pshuf_p128_lp1_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b128_ld1_lin_p1_lp1_r1000
    shuffle   | mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b64_ld4_indir_p524288_lp1_r1000+mix_b128_ld4_lin_p1_lp1_r1000+mix_b128_ld7_pshuf_p128_lp1_r1000
    sum       | mix_b128_ld4_lin_p1_lp1_r1000+mix_b64_ld4_indir_p524288_lp1_r1000+mix_b128_ld7_pshuf_p128_lp1_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b128_ld1_lin_p1_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 96755862477 | 98523649524 | 90485659171
    instructions:u     | 8377077073  | 8377077143  | 8377320746 
    br_retired:u       | 40013193    | 40013202    | 40025002   
    br_mis_pred:u      | 7476        | 13614       | 12314      
    l1i_cache:u        | 1077295744  | 1076925989  | 1075231362 
    l1i_cache_refill:u | 283693      | 300856      | 42334      
    l1i_tlb:u          | 1077295744  | 1076925989  | 1075231362 
    l1i_tlb_refill:u   | 877         | 847         | 479        
    l2i_cache:u        | 283949      | 300969      | 42432      
    l2i_cache_refill:u | 43429       | 45562       | 5037       
    l2i_tlb:u          | 1472        | 1204        | 1765       
    l2i_tlb_refill:u   | 870         | 841         | 365        
    l1d_cache:u        | 1923122531  | 1923541664  | 1923171275 
    l1d_cache_refill:u | 1158350963  | 1154620346  | 1149431075 
    l1d_tlb:u          | 3120090471  | 3121517524  | 3121217636 
    l1d_tlb_refill:u   | 1166335814  | 1166664752  | 1166822055 
    l2d_cache:u        | 3733888749  | 3720445617  | 3637512808 
    l2d_cache_refill:u | 1312270599  | 1305775099  | 1224314930 
    l2d_tlb:u          | 1166625813  | 1166954902  | 1167075062 
    l2d_tlb_refill:u   | 5279939     | 4565888     | 2756767    
    ll_cache:u         | 1312088961  | 1305581769  | 1224195729 
    ll_cache_miss:u    | 530401071   | 530661841   | 536223730  

== combo_066_s5 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld4_xpage_p524288_lp4_r1000
    s1 | mix_b128_ld7_xpage_p512_lp4_r1000   
    s2 | mix_b64_ld4_indir_p524288_lp4_r1000 
    s3 | mix_b128_ld4_xpage_p512_lp4_r1000   
    s4 | mix_b64_ld14_pshuf_p512_lp4_r1000   
single_counts:
    metric             | s0           | s1          | s2          | s3          | s4         
    -------------------+--------------+-------------+-------------+-------------+------------
    cpu-cycles:u       | 129184304313 | 39620409235 | 65367757339 | 22983949366 | 30893103413
    instructions:u     | 2085065076   | 2085065123  | 1061065073  | 2085064018  | 1061065096 
    br_retired:u       | 8005194      | 8005199     | 8005193     | 8004976     | 8005195    
    br_mis_pred:u      | 3009         | 3188        | 2474        | 2349        | 3249       
    l1i_cache:u        | 270681420    | 265481353   | 141553448   | 267726267   | 138343030  
    l1i_cache_refill:u | 97053        | 29067       | 21665       | 17528       | 10740      
    l1i_tlb:u          | 270681420    | 265481353   | 141553448   | 267726267   | 138343030  
    l1i_tlb_refill:u   | 470          | 49          | 328         | 52          | 53         
    l2i_cache:u        | 97304        | 29118       | 21717       | 17612       | 10753      
    l2i_cache_refill:u | 5578         | 2120        | 3398        | 2045        | 5127       
    l2i_tlb:u          | 531          | 99          | 432         | 102         | 93         
    l2i_tlb_refill:u   | 464          | 30          | 323         | 26          | 25         
    l1d_cache:u        | 526869370    | 909367574   | 270639381   | 525907272   | 910628733  
    l1d_cache_refill:u | 512992489    | 897078892   | 256975555   | 507254770   | 289357963  
    l1d_tlb:u          | 1042265284   | 1812347329  | 535791589   | 1048635825  | 1231857977 
    l1d_tlb_refill:u   | 499303833    | 898265369   | 251086407   | 514305446   | 226323668  
    l2d_cache:u        | 2066010932   | 3547037754  | 1032347637  | 2178212606  | 3535160117 
    l2d_cache_refill:u | 1060442143   | 1795291734  | 519110207   | 1042533805  | 1543676976 
    l2d_tlb:u          | 499599489    | 898288561   | 251354179   | 514382332   | 226341299  
    l2d_tlb_refill:u   | 4465388      | 345         | 2778552     | 254         | 304        
    ll_cache:u         | 1060174564   | 1795269183  | 518637244   | 1042514355  | 1543490208 
    ll_cache_miss:u    | 1052159914   | 14569173    | 510349562   | 11313604    | 27137103   
combined_orders:
    id        | modules                                                                                                                                                                       
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld4_xpage_p524288_lp4_r1000+mix_b128_ld7_xpage_p512_lp4_r1000+mix_b64_ld4_indir_p524288_lp4_r1000+mix_b128_ld4_xpage_p512_lp4_r1000+mix_b64_ld14_pshuf_p512_lp4_r1000
    shuffle   | mix_b128_ld7_xpage_p512_lp4_r1000+mix_b64_ld4_indir_p524288_lp4_r1000+mix_b128_ld4_xpage_p512_lp4_r1000+mix_b64_ld14_pshuf_p512_lp4_r1000+mix_b128_ld4_xpage_p524288_lp4_r1000
    sum       | mix_b128_ld4_xpage_p524288_lp4_r1000+mix_b128_ld7_xpage_p512_lp4_r1000+mix_b64_ld4_indir_p524288_lp4_r1000+mix_b128_ld4_xpage_p512_lp4_r1000+mix_b64_ld14_pshuf_p512_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 289998056115 | 289713361140 | 288049523666
    instructions:u     | 8377077388   | 8377077388   | 8377324386  
    br_retired:u       | 40013246     | 40013246     | 40025757    
    br_mis_pred:u      | 13996        | 12539        | 14269       
    l1i_cache:u        | 1085033777   | 1085173167   | 1083785518  
    l1i_cache_refill:u | 597662       | 596000       | 176053      
    l1i_tlb:u          | 1085033777   | 1085173167   | 1083785518  
    l1i_tlb_refill:u   | 2004         | 2140         | 952         
    l2i_cache:u        | 597903       | 596247       | 176504      
    l2i_cache_refill:u | 83560        | 83552        | 18268       
    l2i_tlb:u          | 2952         | 2297         | 1257        
    l2i_tlb_refill:u   | 1998         | 2135         | 868         
    l1d_cache:u        | 3143143534   | 3143140074   | 3143412330  
    l1d_cache_refill:u | 2466160550   | 2469402847   | 2463659669  
    l1d_tlb:u          | 5677882839   | 5678680514   | 5670898004  
    l1d_tlb_refill:u   | 2389221519   | 2389214231   | 2389284723  
    l2d_cache:u        | 12233092005  | 12174209549  | 12358769046 
    l2d_cache_refill:u | 6015692436   | 5941283649   | 5961054865  
    l2d_tlb:u          | 2389974391   | 2389971472   | 2389965860  
    l2d_tlb_refill:u   | 13144787     | 13641505     | 7244843     
    ll_cache:u         | 6014273248   | 5939913830   | 5960085554  
    ll_cache_miss:u    | 1974631205   | 1916488062   | 1615529356  

== combo_067_s5 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b64_ld14_indir_p512_lp4_r1000    
    s1 | mix_b128_ld2_pshuf_p128_lp1_r1000    
    s2 | mix_b128_ld7_xpage_p512_lp1_r1000    
    s3 | mix_b128_ld4_pshuf_p524288_lp1_r1000 
    s4 | mix_b128_ld14_pshuf_p524288_lp1_r1000
single_counts:
    metric             | s0          | s1         | s2          | s3          | s4         
    -------------------+-------------+------------+-------------+-------------+------------
    cpu-cycles:u       | 40168809167 | 7428053354 | 37592965655 | 21809028008 | 74257811434
    instructions:u     | 1061065069  | 2085063801 | 2085065123  | 2085064018  | 2085065022 
    br_retired:u       | 8005191     | 8004920    | 8005199     | 8004976     | 8005186    
    br_mis_pred:u      | 3315        | 2081       | 3372        | 3104        | 3362       
    l1i_cache:u        | 140135377   | 265736101  | 265358814   | 267422177   | 267793159  
    l1i_cache_refill:u | 13078       | 7026       | 27916       | 23472       | 56872      
    l1i_tlb:u          | 140135377   | 265736101  | 265358814   | 267422177   | 267793159  
    l1i_tlb_refill:u   | 51          | 45         | 48          | 212         | 369        
    l2i_cache:u        | 13089       | 7030       | 27945       | 23510       | 56933      
    l2i_cache_refill:u | 1475        | 766        | 1481        | 1483        | 3164       
    l2i_tlb:u          | 91          | 126        | 100         | 541         | 635        
    l2i_tlb_refill:u   | 31          | 16         | 24          | 208         | 368        
    l1d_cache:u        | 910999410   | 269056954  | 909363533   | 525716029   | 1806961391 
    l1d_cache_refill:u | 890664051   | 240141295  | 896041509   | 96040401    | 338941342  
    l1d_tlb:u          | 1770724966  | 533458427  | 1812344258  | 529811599   | 1819496312 
    l1d_tlb_refill:u   | 851449081   | 258000131  | 898267585   | 1574059     | 5490637    
    l2d_cache:u        | 3429328222  | 717801790  | 3538987457  | 2249077543  | 7571701690 
    l2d_cache_refill:u | 1647620559  | 178585048  | 1791774321  | 928364459   | 3105977166 
    l2d_tlb:u          | 851540288   | 258433565  | 898290525   | 1582857     | 5508189    
    l2d_tlb_refill:u   | 271         | 35         | 302         | 959500      | 3328049    
    ll_cache:u         | 1647550462  | 178583607  | 1791759339  | 927861796   | 3104161236 
    ll_cache_miss:u    | 7357420     | 1700       | 139809      | 845900917   | 2830931319 
combined_orders:
    id        | modules                                                                                                                                                                         
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_indir_p512_lp4_r1000+mix_b128_ld2_pshuf_p128_lp1_r1000+mix_b128_ld7_xpage_p512_lp1_r1000+mix_b128_ld4_pshuf_p524288_lp1_r1000+mix_b128_ld14_pshuf_p524288_lp1_r1000
    shuffle   | mix_b128_ld2_pshuf_p128_lp1_r1000+mix_b128_ld4_pshuf_p524288_lp1_r1000+mix_b64_ld14_indir_p512_lp4_r1000+mix_b128_ld14_pshuf_p524288_lp1_r1000+mix_b128_ld7_xpage_p512_lp1_r1000
    sum       | mix_b64_ld14_indir_p512_lp4_r1000+mix_b128_ld2_pshuf_p128_lp1_r1000+mix_b128_ld7_xpage_p512_lp1_r1000+mix_b128_ld4_pshuf_p524288_lp1_r1000+mix_b128_ld14_pshuf_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 204341332518 | 205658543132 | 181256667618
    instructions:u     | 9401077133   | 9401077096   | 9401323033  
    br_retired:u       | 40013208     | 40013205     | 40025472    
    br_mis_pred:u      | 13955        | 14879        | 15234       
    l1i_cache:u        | 1208154899   | 1207520856   | 1206445628  
    l1i_cache_refill:u | 582610       | 552661       | 128364      
    l1i_tlb:u          | 1208154899   | 1207520856   | 1206445628  
    l1i_tlb_refill:u   | 1880         | 1879         | 725         
    l2i_cache:u        | 582709       | 553589       | 128507      
    l2i_cache_refill:u | 62125        | 52664        | 8369        
    l2i_tlb:u          | 2721         | 2805         | 1493        
    l2i_tlb_refill:u   | 1876         | 1871         | 647         
    l1d_cache:u        | 4423390063   | 4423212379   | 4422097317  
    l1d_cache_refill:u | 2465417868   | 2467626514   | 2461828598  
    l1d_tlb:u          | 6471984720   | 6469832619   | 6465835562  
    l1d_tlb_refill:u   | 2015653935   | 2015695424   | 2014781493  
    l2d_cache:u        | 17505843366  | 17512845399  | 17506896702 
    l2d_cache_refill:u | 7683376152   | 7692744359   | 7652321553  
    l2d_tlb:u          | 2016273395   | 2015874869   | 2015355424  
    l2d_tlb_refill:u   | 6952881      | 6962718      | 4288157     
    ll_cache:u         | 7680857336   | 7690314319   | 7649916440  
    ll_cache_miss:u    | 3711675469   | 3712114468   | 3684331165  

== combo_068_s6 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld1_indir_p1_lp4_r1000  
    s1 | mix_b64_ld14_pshuf_p1_lp4_r1000  
    s2 | mix_b64_ld2_lin_p524288_lp1_r1000
    s3 | mix_b64_ld4_xpage_p512_lp4_r1000 
    s4 | mix_b64_ld14_pshuf_p1_lp1_r1000  
    s5 | mix_b128_ld7_pshuf_p128_lp4_r1000
single_counts:
    metric             | s0         | s1         | s2         | s3          | s4         | s5         
    -------------------+------------+------------+------------+-------------+------------+------------
    cpu-cycles:u       | 530120910  | 3602145944 | 5485728895 | 11868623786 | 3602130746 | 17760193040
    instructions:u     | 2085064023 | 1061063801 | 1061063795 | 1061063795  | 1061063786 | 2085063795 
    br_retired:u       | 8004983    | 8004920    | 8004922    | 8004922     | 8004921    | 8004922    
    br_mis_pred:u      | 2259       | 2532       | 2319       | 2221        | 2576       | 3354       
    l1i_cache:u        | 266044465  | 138058465  | 137504776  | 138164114   | 138060024  | 265973359  
    l1i_cache_refill:u | 1060       | 1773       | 2469       | 4493        | 1974       | 14142      
    l1i_tlb:u          | 266044465  | 138058465  | 137504776  | 138164114   | 138060024  | 265973359  
    l1i_tlb_refill:u   | 44         | 44         | 60         | 45          | 55         | 47         
    l2i_cache:u        | 1060       | 1778       | 2474       | 4501        | 1980       | 14175      
    l2i_cache_refill:u | 627        | 538        | 658        | 868         | 582        | 872        
    l2i_tlb:u          | 88         | 310        | 246        | 380         | 152        | 147        
    l2i_tlb_refill:u   | 12         | 14         | 54         | 29          | 32         | 17         
    l1d_cache:u        | 141033581  | 909036637  | 141192516  | 269657528   | 909036690  | 910025795  
    l1d_cache_refill:u | 153        | 179        | 24328407   | 255777607   | 175        | 306110637  
    l1d_tlb:u          | 141047273  | 909082008  | 142343871  | 536079353   | 909082137  | 1242524997 
    l1d_tlb_refill:u   | 72         | 97         | 394597     | 258446952   | 104        | 226182711  
    l2d_cache:u        | 1602       | 2697       | 563166194  | 1053827449  | 2511       | 2951328652 
    l2d_cache_refill:u | 860        | 803        | 231369626  | 532690680   | 815        | 458756197  
    l2d_tlb:u          | 95         | 117        | 395405     | 258519816   | 133        | 226253638  
    l2d_tlb_refill:u   | 3          | 9          | 237679     | 169         | 3          | 20         
    ll_cache:u         | 254        | 272        | 231227134  | 532680724   | 274        | 458728528  
    ll_cache_miss:u    | 50         | 37         | 210918026  | 10787755    | 74         | 1680033    
combined_orders:
    id        | modules                                                                                                                                                                                             
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld1_indir_p1_lp4_r1000+mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b64_ld2_lin_p524288_lp1_r1000+mix_b64_ld4_xpage_p512_lp4_r1000+mix_b64_ld14_pshuf_p1_lp1_r1000+mix_b128_ld7_pshuf_p128_lp4_r1000
    shuffle   | mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b128_ld1_indir_p1_lp4_r1000+mix_b64_ld14_pshuf_p1_lp1_r1000+mix_b64_ld4_xpage_p512_lp4_r1000+mix_b128_ld7_pshuf_p128_lp4_r1000+mix_b64_ld2_lin_p524288_lp1_r1000
    sum       | mix_b128_ld1_indir_p1_lp4_r1000+mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b64_ld2_lin_p524288_lp1_r1000+mix_b64_ld4_xpage_p512_lp4_r1000+mix_b64_ld14_pshuf_p1_lp1_r1000+mix_b128_ld7_pshuf_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 50973367226 | 46764895719 | 42848943321
    instructions:u     | 8414080049  | 8414079974  | 8414382995 
    br_retired:u       | 48015190    | 48015180    | 48029590   
    br_mis_pred:u      | 14186       | 14505       | 15261      
    l1i_cache:u        | 1087016242  | 1086837788  | 1083805203 
    l1i_cache_refill:u | 243975      | 218960      | 25911      
    l1i_tlb:u          | 1087016242  | 1086837788  | 1083805203 
    l1i_tlb_refill:u   | 619         | 606         | 295        
    l2i_cache:u        | 244057      | 219059      | 25968      
    l2i_cache_refill:u | 31719       | 33026       | 4145       
    l2i_tlb:u          | 1595        | 1147        | 1323       
    l2i_tlb_refill:u   | 613         | 602         | 158        
    l1d_cache:u        | 3279937234  | 3279936604  | 3279982747 
    l1d_cache_refill:u | 602025910   | 560742345   | 586217158  
    l1d_tlb:u          | 3873405713  | 3898906728  | 3880159639 
    l1d_tlb_refill:u   | 485126093   | 485133243   | 485024533  
    l2d_cache:u        | 4534819253  | 5343581799  | 4568329105 
    l2d_cache_refill:u | 1200287721  | 1400387679  | 1222818981 
    l2d_tlb:u          | 485237254   | 485267594   | 485169204  
    l2d_tlb_refill:u   | 700952      | 693408      | 237883     
    ll_cache:u         | 1200023739  | 1400034508  | 1222637186 
    ll_cache_miss:u    | 280300503   | 409945183   | 223385975  

== combo_069_s6 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld14_pshuf_p512_lp4_r1000   
    s1 | mix_b128_ld4_indir_p524288_lp4_r1000
    s2 | mix_b64_ld14_indir_p512_lp4_r1000   
    s3 | mix_b64_ld14_lin_p524288_lp4_r1000  
    s4 | mix_b128_ld2_lin_p128_lp1_r1000     
    s5 | mix_b64_ld2_indir_p512_lp1_r1000    
single_counts:
    metric             | s0          | s1           | s2          | s3          | s4         | s5        
    -------------------+-------------+--------------+-------------+-------------+------------+-----------
    cpu-cycles:u       | 30377382727 | 130503812927 | 37656044577 | 90387956844 | 6280661718 | 5548918753
    instructions:u     | 1061065096  | 2085065022   | 1061065072  | 1061065116  | 2085063801 | 1061063795
    br_retired:u       | 8005195     | 8005186      | 8005192     | 8005198     | 8004920    | 8004922   
    br_mis_pred:u      | 3200        | 3275         | 3108        | 3470        | 2834       | 2694      
    l1i_cache:u        | 139566616   | 271205924    | 138841565   | 140144728   | 266108409  | 137121789 
    l1i_cache_refill:u | 10513       | 98660        | 12325       | 29370       | 5730       | 2550      
    l1i_tlb:u          | 139566616   | 271205924    | 138841565   | 140144728   | 266108409  | 137121789 
    l1i_tlb_refill:u   | 47          | 469          | 48          | 340         | 46         | 53        
    l2i_cache:u        | 10521       | 98889        | 12347       | 29440       | 5747       | 2559      
    l2i_cache_refill:u | 4689        | 6621         | 1484        | 5209        | 776        | 668       
    l2i_tlb:u          | 105         | 541          | 115         | 517         | 92         | 168       
    l2i_tlb_refill:u   | 25          | 464          | 24          | 335         | 15         | 19        
    l1d_cache:u        | 910683694   | 527083293    | 910971153   | 910764292   | 269063150  | 141074943 
    l1d_cache_refill:u | 293720438   | 513995146    | 892785495   | 209066279   | 244749769  | 127415154 
    l1d_tlb:u          | 1241701936  | 1042761443   | 1777310540  | 914015732   | 533423592  | 276929306 
    l1d_tlb_refill:u   | 226334840   | 499304995    | 856054677   | 705449      | 258000125  | 130021804 
    l2d_cache:u        | 3544955773  | 2063253607   | 3438733085  | 3480600533  | 727589158  | 514543596 
    l2d_cache_refill:u | 1548748274  | 1037487451   | 1656771699  | 2027001592  | 188396863  | 257660762 
    l2d_tlb:u          | 226348184   | 499646202    | 856179642   | 724426      | 258347142  | 130035658 
    l2d_tlb_refill:u   | 284         | 4437065      | 299         | 457600      | 17         | 189       
    ll_cache:u         | 1548563850  | 1036913131   | 1656707144  | 2026446689  | 188395785  | 257657636 
    ll_cache_miss:u    | 21634670    | 1019781091   | 9068677     | 1937234451  | 747        | 1333001   
combined_orders:
    id        | modules                                                                                                                                                                                                     
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_pshuf_p512_lp4_r1000+mix_b128_ld4_indir_p524288_lp4_r1000+mix_b64_ld14_indir_p512_lp4_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b128_ld2_lin_p128_lp1_r1000+mix_b64_ld2_indir_p512_lp1_r1000
    shuffle   | mix_b64_ld2_indir_p512_lp1_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b64_ld14_pshuf_p512_lp4_r1000+mix_b64_ld14_indir_p512_lp4_r1000+mix_b128_ld4_indir_p524288_lp4_r1000+mix_b128_ld2_lin_p128_lp1_r1000
    sum       | mix_b64_ld14_pshuf_p512_lp4_r1000+mix_b128_ld4_indir_p524288_lp4_r1000+mix_b64_ld14_indir_p512_lp4_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b128_ld2_lin_p128_lp1_r1000+mix_b64_ld2_indir_p512_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 312432144359 | 316153917844 | 300754777546
    instructions:u     | 8414080306   | 8414080328   | 8414387902  
    br_retired:u       | 48015235     | 48015238     | 48030613    
    br_mis_pred:u      | 19155        | 19153        | 18581       
    l1i_cache:u        | 1095772163   | 1094500863   | 1092989031  
    l1i_cache_refill:u | 598829       | 570344       | 159148      
    l1i_tlb:u          | 1095772163   | 1094500863   | 1092989031  
    l1i_tlb_refill:u   | 2083         | 2087         | 1003        
    l2i_cache:u        | 599300       | 571489       | 159503      
    l2i_cache_refill:u | 110999       | 101456       | 19447       
    l2i_tlb:u          | 2768         | 2792         | 1538        
    l2i_tlb_refill:u   | 2076         | 2083         | 882         
    l1d_cache:u        | 3669326279   | 3672668691   | 3669640525  
    l1d_cache_refill:u | 2272936680   | 2272087103   | 2281732281  
    l1d_tlb:u          | 5786604551   | 5793112722   | 5786142549  
    l1d_tlb_refill:u   | 1969850310   | 1970085716   | 1970421890  
    l2d_cache:u        | 14061870100  | 14190742552  | 13769675752 
    l2d_cache_refill:u | 7035352104   | 7167942609   | 6716066641  
    l2d_tlb:u          | 1970493147   | 1970727822   | 1971281254  
    l2d_tlb_refill:u   | 9092738      | 9051748      | 4895454     
    ll_cache:u         | 7033363009   | 7165930733   | 6714684235  
    ll_cache_miss:u    | 3543313216   | 3677588110   | 2989052637  

== combo_070_s6 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b128_ld7_lin_p128_lp4_r1000  
    s1 | mix_b128_ld7_pshuf_p512_lp1_r1000
    s2 | mix_b128_ld1_pshuf_p128_lp1_r1000
    s3 | mix_b128_ld4_indir_p512_lp4_r1000
    s4 | mix_b128_ld4_pshuf_p128_lp1_r1000
    s5 | mix_b64_ld4_lin_p128_lp1_r1000   
single_counts:
    metric             | s0          | s1          | s2         | s3          | s4          | s5        
    -------------------+-------------+-------------+------------+-------------+-------------+-----------
    cpu-cycles:u       | 15051217194 | 37571612258 | 4054993024 | 22177876648 | 14215214228 | 7242130920
    instructions:u     | 2085063795  | 2085065072  | 2085063795 | 2085064012  | 2085063795  | 1061063795
    br_retired:u       | 8004922     | 8005192     | 8004922    | 8004978     | 8004922     | 8004922   
    br_mis_pred:u      | 2385        | 3522        | 2026       | 2367        | 2349        | 2119      
    l1i_cache:u        | 267488681   | 266473773   | 265225443  | 267733063   | 267055196   | 137771878 
    l1i_cache_refill:u | 12238       | 27337       | 3940       | 16657       | 10474       | 3221      
    l1i_tlb:u          | 267488681   | 266473773   | 265225443  | 267733063   | 267055196   | 137771878 
    l1i_tlb_refill:u   | 58          | 50          | 47         | 45          | 51          | 51        
    l2i_cache:u        | 12256       | 27384       | 3946       | 16679       | 10506       | 3231      
    l2i_cache_refill:u | 1240        | 1540        | 639        | 1349        | 786         | 652       
    l2i_tlb:u          | 123         | 98          | 91         | 159         | 173         | 235       
    l2i_tlb_refill:u   | 33          | 24          | 16         | 29          | 14          | 17        
    l1d_cache:u        | 909308516   | 909396238   | 141037505  | 525883331   | 525767897   | 269372035 
    l1d_cache_refill:u | 216175074   | 896107696   | 120971988  | 509969052   | 489842543   | 245449787 
    l1d_tlb:u          | 1226530730  | 1812255525  | 278848029  | 1022194415  | 1048858356  | 534860373 
    l1d_tlb_refill:u   | 227051154   | 898291041   | 130000062  | 488341945   | 514312559   | 258146702 
    l2d_cache:u        | 2853689386  | 3539131903  | 378116715  | 1951614991  | 1435783235  | 721622946 
    l2d_cache_refill:u | 548699163   | 1793111740  | 108009175  | 936359283   | 392435166   | 208788627 
    l2d_tlb:u          | 227140731   | 898310871   | 130000477  | 488428449   | 514696492   | 258258741 
    l2d_tlb_refill:u   | 14          | 310         | 82         | 194         | 16          | 20        
    ll_cache:u         | 548665729   | 1793098151  | 108007881  | 936321183   | 392430140   | 208784626 
    ll_cache_miss:u    | 4194692     | 160303      | 1500       | 3261892     | 16464       | 1432      
combined_orders:
    id        | modules                                                                                                                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld7_lin_p128_lp4_r1000+mix_b128_ld7_pshuf_p512_lp1_r1000+mix_b128_ld1_pshuf_p128_lp1_r1000+mix_b128_ld4_indir_p512_lp4_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b64_ld4_lin_p128_lp1_r1000
    shuffle   | mix_b128_ld7_pshuf_p512_lp1_r1000+mix_b64_ld4_lin_p128_lp1_r1000+mix_b128_ld7_lin_p128_lp4_r1000+mix_b128_ld1_pshuf_p128_lp1_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b128_ld4_indir_p512_lp4_r1000
    sum       | mix_b128_ld7_lin_p128_lp4_r1000+mix_b128_ld7_pshuf_p512_lp1_r1000+mix_b128_ld1_pshuf_p128_lp1_r1000+mix_b128_ld4_indir_p512_lp4_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b64_ld4_lin_p128_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 150610627653 | 142075856766 | 100313044272
    instructions:u     | 11486080056  | 11486080080  | 11486384264 
    br_retired:u       | 48015190     | 48015193     | 48029858    
    br_mis_pred:u      | 17605        | 16578        | 14768       
    l1i_cache:u        | 1473347715   | 1472496767   | 1471748034  
    l1i_cache_refill:u | 656094       | 588427       | 73867       
    l1i_tlb:u          | 1473347715   | 1472496767   | 1471748034  
    l1i_tlb_refill:u   | 90           | 88           | 302         
    l2i_cache:u        | 656290       | 588736       | 74002       
    l2i_cache_refill:u | 65180        | 63276        | 6206        
    l2i_tlb:u          | 367          | 337          | 879         
    l2i_tlb_refill:u   | 88           | 84           | 133         
    l1d_cache:u        | 3281968479   | 3282304190   | 3280765522  
    l1d_cache_refill:u | 2485692184   | 2483177121   | 2478516140  
    l1d_tlb:u          | 5927265684   | 5934736925   | 5923547428  
    l1d_tlb_refill:u   | 2515625148   | 2515678148   | 2516143463  
    l2d_cache:u        | 10714853847  | 10786130361  | 10879959176 
    l2d_cache_refill:u | 3984443330   | 4129961642   | 3987403154  
    l2d_tlb:u          | 2516761629   | 2516372875   | 2516835761  
    l2d_tlb_refill:u   | 1188960      | 1187384      | 636         
    ll_cache:u         | 3984236377   | 4129753390   | 3987307710  
    ll_cache_miss:u    | 152212168    | 170563242    | 7636283     

== combo_071_s6 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b128_ld7_lin_p524288_lp4_r1000
    s1 | mix_b64_ld14_xpage_p128_lp1_r1000 
    s2 | mix_b128_ld1_indir_p512_lp1_r1000 
    s3 | mix_b64_ld1_indir_p128_lp4_r1000  
    s4 | mix_b128_ld14_pshuf_p128_lp4_r1000
    s5 | mix_b128_ld14_indir_p1_lp1_r1000  
single_counts:
    metric             | s0          | s1          | s2         | s3         | s4          | s5        
    -------------------+-------------+-------------+------------+------------+-------------+-----------
    cpu-cycles:u       | 90444573703 | 22972052159 | 5744862446 | 1417358972 | 33709237885 | 7186341476
    instructions:u     | 2085065100  | 1061064012  | 2085063795 | 1061064029 | 2085065123  | 2085063792
    br_retired:u       | 8005197     | 8004978     | 8004922    | 8004981    | 8005199     | 8004919   
    br_mis_pred:u      | 3394        | 3614        | 2053       | 1915       | 3493        | 3066      
    l1i_cache:u        | 268048493   | 137120929   | 265596347  | 138177216  | 267477209   | 265065950 
    l1i_cache_refill:u | 84022       | 7773        | 5124       | 1041       | 25275       | 6201      
    l1i_tlb:u          | 268048493   | 137120929   | 265596347  | 138177216  | 267477209   | 265065950 
    l1i_tlb_refill:u   | 413         | 46          | 48         | 43         | 49          | 50        
    l2i_cache:u        | 84140       | 7788        | 5135       | 1044       | 25333       | 6215      
    l2i_cache_refill:u | 15675       | 858         | 697        | 594        | 1938        | 672       
    l2i_tlb:u          | 541         | 93          | 97         | 94         | 123         | 92        
    l2i_tlb_refill:u   | 408         | 15          | 28         | 14         | 18          | 18        
    l1d_cache:u        | 910750133   | 909090967   | 141054905  | 77053751   | 1806821728  | 1805039254
    l1d_cache_refill:u | 222558581   | 865927578   | 127996373  | 60520555   | 611253194   | 187       
    l1d_tlb:u          | 914335127   | 1813498281  | 276650950  | 136989668  | 2510595173  | 1805089362
    l1d_tlb_refill:u   | 705367      | 898038528   | 130007208  | 54127569   | 450368350   | 122       
    l2d_cache:u        | 3237646423  | 2407452831  | 505250428  | 164422680  | 5870235359  | 5949      
    l2d_cache_refill:u | 1829623606  | 614772306   | 256118511  | 37170471   | 960400421   | 926       
    l2d_tlb:u          | 724500      | 898047421   | 130007782  | 54204119   | 450475957   | 396       
    l2d_tlb_refill:u   | 457169      | 32          | 239        | 16         | 20          | 4         
    ll_cache:u         | 1829133202  | 614768575   | 256115000  | 37168993   | 960335408   | 282       
    ll_cache_miss:u    | 1735131470  | 18453       | 3129       | 18624      | 2844884     | 98        
combined_orders:
    id        | modules                                                                                                                                                                                                    
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld7_lin_p524288_lp4_r1000+mix_b64_ld14_xpage_p128_lp1_r1000+mix_b128_ld1_indir_p512_lp1_r1000+mix_b64_ld1_indir_p128_lp4_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld14_indir_p1_lp1_r1000
    shuffle   | mix_b128_ld7_lin_p524288_lp4_r1000+mix_b128_ld1_indir_p512_lp1_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b64_ld14_xpage_p128_lp1_r1000+mix_b128_ld14_indir_p1_lp1_r1000+mix_b64_ld1_indir_p128_lp4_r1000
    sum       | mix_b128_ld7_lin_p524288_lp4_r1000+mix_b64_ld14_xpage_p128_lp1_r1000+mix_b128_ld1_indir_p512_lp1_r1000+mix_b64_ld1_indir_p128_lp4_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld14_indir_p1_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 165101253917 | 162565366317 | 161474426641
    instructions:u     | 10462080046  | 10462080116  | 10462385851 
    br_retired:u       | 48015189     | 48015198     | 48030196    
    br_mis_pred:u      | 11702        | 13030        | 17535       
    l1i_cache:u        | 1343309497   | 1340847538   | 1341486144  
    l1i_cache_refill:u | 564329       | 544801       | 129436      
    l1i_tlb:u          | 1343309497   | 1340847538   | 1341486144  
    l1i_tlb_refill:u   | 1256         | 1253         | 649         
    l2i_cache:u        | 564838       | 545301       | 129655      
    l2i_cache_refill:u | 112433       | 105613       | 20434       
    l2i_tlb:u          | 2135         | 1704         | 1040        
    l2i_tlb_refill:u   | 1249         | 1239         | 501         
    l1d_cache:u        | 5650297227   | 5650270830   | 5649810738  
    l1d_cache_refill:u | 1854334757   | 1875003437   | 1888256468  
    l1d_tlb:u          | 7475382242   | 7468445952   | 7457158561  
    l1d_tlb_refill:u   | 1533825765   | 1538464449   | 1533247144  
    l2d_cache:u        | 11975018640  | 12120509455  | 12185013670 
    l2d_cache_refill:u | 3548625178   | 3679373314   | 3698086241  
    l2d_tlb:u          | 1534006429   | 1538900578   | 1533460175  
    l2d_tlb_refill:u   | 1357328      | 1360352      | 457480      
    ll_cache:u         | 3548028692   | 3678894674   | 3697521460  
    ll_cache_miss:u    | 1828976403   | 1855103950   | 1738016658  

== combo_072_s6 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld14_indir_p524288_lp1_r1000
    s1 | mix_b64_ld14_indir_p1_lp1_r1000     
    s2 | mix_b64_ld4_xpage_p524288_lp1_r1000 
    s3 | mix_b64_ld14_pshuf_p1_lp4_r1000     
    s4 | mix_b128_ld2_lin_p1_lp4_r1000       
    s5 | mix_b128_ld7_indir_p524288_lp1_r1000
single_counts:
    metric             | s0           | s1         | s2          | s3         | s4         | s5          
    -------------------+--------------+------------+-------------+------------+------------+-------------
    cpu-cycles:u       | 226552609376 | 3602141038 | 64762797048 | 3602140292 | 1042114487 | 226464243847
    instructions:u     | 1061065039   | 1061063792 | 1061065089  | 1061063795 | 2085064029 | 2085065117  
    br_retired:u       | 8005196      | 8004919    | 8005194     | 8004922    | 8004981    | 8005207     
    br_mis_pred:u      | 3361         | 2559       | 2501        | 2548       | 2469       | 3977        
    l1i_cache:u        | 138933418    | 137056252  | 140624420   | 138056255  | 266061659  | 268102778   
    l1i_cache_refill:u | 67659        | 1995       | 21339       | 1946       | 1405       | 161428      
    l1i_tlb:u          | 138933418    | 137056252  | 140624420   | 138056255  | 266061659  | 268102778   
    l1i_tlb_refill:u   | 426          | 44         | 299         | 45         | 47         | 528         
    l2i_cache:u        | 67801        | 1997       | 21378       | 1953       | 1405       | 161732      
    l2i_cache_refill:u | 4534         | 539        | 1877        | 543        | 622        | 6385        
    l2i_tlb:u          | 483          | 133        | 400         | 231        | 114        | 736         
    l2i_tlb_refill:u   | 421          | 12         | 295         | 11         | 13         | 524         
    l1d_cache:u        | 909374960    | 909038290  | 270616612   | 909038246  | 269037689  | 911280504   
    l1d_cache_refill:u | 895907774    | 166        | 256793635   | 186        | 154        | 897195268   
    l1d_tlb:u          | 1794234296   | 909084827  | 535493861   | 909084689  | 269072811  | 1800479092  
    l1d_tlb_refill:u   | 870382661    | 102        | 251028707   | 102        | 76         | 871623109   
    l2d_cache:u        | 3557281171   | 2419       | 1020794415  | 2487       | 2326       | 3566963353  
    l2d_cache_refill:u | 1807693137   | 818        | 518916583   | 764        | 942        | 1812155455  
    l2d_tlb:u          | 870434212    | 123        | 251265582   | 130        | 98         | 871703630   
    l2d_tlb_refill:u   | 7680673      | 3          | 2493719     | 4          | 6          | 10185952    
    ll_cache:u         | 1807395268   | 265        | 518828167   | 289        | 282        | 1811855183  
    ll_cache_miss:u    | 1800506616   | 55         | 515027822   | 113        | 55         | 1802425979  
combined_orders:
    id        | modules                                                                                                                                                                                                    
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_indir_p524288_lp1_r1000+mix_b64_ld14_indir_p1_lp1_r1000+mix_b64_ld4_xpage_p524288_lp1_r1000+mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b128_ld2_lin_p1_lp4_r1000+mix_b128_ld7_indir_p524288_lp1_r1000
    shuffle   | mix_b64_ld14_indir_p524288_lp1_r1000+mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b128_ld2_lin_p1_lp4_r1000+mix_b64_ld14_indir_p1_lp1_r1000+mix_b64_ld4_xpage_p524288_lp1_r1000+mix_b128_ld7_indir_p524288_lp1_r1000
    sum       | mix_b64_ld14_indir_p524288_lp1_r1000+mix_b64_ld14_indir_p1_lp1_r1000+mix_b64_ld4_xpage_p524288_lp1_r1000+mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b128_ld2_lin_p1_lp4_r1000+mix_b128_ld7_indir_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 526216257542 | 525860596088 | 526026046088
    instructions:u     | 8414080327   | 8414080327   | 8414386861  
    br_retired:u       | 48015237     | 48015237     | 48030419    
    br_mis_pred:u      | 16941        | 17950        | 17415       
    l1i_cache:u        | 1095348968   | 1095441507   | 1088834782  
    l1i_cache_refill:u | 785075       | 783918       | 255772      
    l1i_tlb:u          | 1095348968   | 1095441507   | 1088834782  
    l1i_tlb_refill:u   | 3085         | 3137         | 1389        
    l2i_cache:u        | 785427       | 784317       | 256266      
    l2i_cache_refill:u | 103712       | 119504       | 14500       
    l2i_tlb:u          | 3967         | 3707         | 2097        
    l2i_tlb_refill:u   | 3081         | 3131         | 1276        
    l1d_cache:u        | 4180976654   | 4181083401   | 4178386301  
    l1d_cache_refill:u | 2051550713   | 2050368465   | 2049897183  
    l1d_tlb:u          | 6228908122   | 6233473260   | 6217449576  
    l1d_tlb_refill:u   | 1995404521   | 1995411586   | 1993034757  
    l2d_cache:u        | 8165309884   | 8230082705   | 8145046171  
    l2d_cache_refill:u | 4148790173   | 4201138091   | 4138767699  
    l2d_tlb:u          | 1995796077   | 1995824854   | 1993403775  
    l2d_tlb_refill:u   | 25378464     | 29640026     | 20360357    
    ll_cache:u         | 4147797049   | 4200101564   | 4138079454  
    ll_cache_miss:u    | 4124229168   | 4167813707   | 4117960640  

== combo_073_s6 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b128_ld7_xpage_p1_lp4_r1000      
    s1 | mix_b128_ld14_xpage_p524288_lp4_r1000
    s2 | mix_b64_ld1_lin_p524288_lp4_r1000    
    s3 | mix_b128_ld1_indir_p524288_lp1_r1000 
    s4 | mix_b128_ld4_lin_p524288_lp1_r1000   
    s5 | mix_b64_ld7_xpage_p524288_lp1_r1000  
single_counts:
    metric             | s0         | s1           | s2         | s3          | s4          | s5          
    -------------------+------------+--------------+------------+-------------+-------------+-------------
    cpu-cycles:u       | 3602115558 | 452271798958 | 6848168343 | 32395462425 | 21947429551 | 113256769300
    instructions:u     | 2085063801 | 2085065381   | 1061063795 | 2085065123  | 2085064018  | 1061065092  
    br_retired:u       | 8004920    | 8005245      | 8004922    | 8005199     | 8004976     | 8005195     
    br_mis_pred:u      | 2652       | 5573         | 2807       | 3093        | 3039        | 3222        
    l1i_cache:u        | 266061765  | 266091329    | 137304578  | 266727832   | 267435402   | 139489096   
    l1i_cache_refill:u | 3327       | 272265       | 2938       | 28277       | 23561       | 36081       
    l1i_tlb:u          | 266061765  | 266091329    | 137304578  | 266727832   | 267435402   | 139489096   
    l1i_tlb_refill:u   | 42         | 594          | 72         | 251         | 220         | 370         
    l2i_cache:u        | 3337       | 273120       | 2942       | 28339       | 23599       | 36184       
    l2i_cache_refill:u | 576        | 12227        | 909        | 2475        | 1406        | 4183        
    l2i_tlb:u          | 258        | 1051         | 278        | 664         | 465         | 431         
    l2i_tlb_refill:u   | 11         | 588          | 67         | 246         | 215         | 360         
    l1d_cache:u        | 909037945  | 1805264793   | 77063957   | 141073753   | 525151898   | 462896742   
    l1d_cache_refill:u | 158        | 1792251454   | 18298541   | 127715737   | 96250498    | 446973091   
    l1d_tlb:u          | 909086657  | 3569532086   | 77260638   | 275428412   | 529053721   | 911548597   
    l1d_tlb_refill:u   | 94         | 1737812685   | 51655      | 126096025   | 1572784     | 437455142   
    l2d_cache:u        | 3634       | 7118251512   | 207004244  | 558611054   | 2250588056  | 1870338658  
    l2d_cache_refill:u | 876        | 3613777465   | 112929837  | 294461596   | 930432636   | 983963115   
    l2d_tlb:u          | 119        | 1737893345   | 53478      | 126110900   | 1581651     | 437514847   
    l2d_tlb_refill:u   | 5          | 19846424     | 34337      | 1267515     | 959016      | 3913376     
    ll_cache:u         | 274        | 3612996013   | 112898436  | 294388676   | 929888790   | 983734860   
    ll_cache_miss:u    | 64         | 3605449881   | 108324293  | 287269092   | 849550439   | 977572782   
combined_orders:
    id        | modules                                                                                                                                                                                                            
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld7_xpage_p1_lp4_r1000+mix_b128_ld14_xpage_p524288_lp4_r1000+mix_b64_ld1_lin_p524288_lp4_r1000+mix_b128_ld1_indir_p524288_lp1_r1000+mix_b128_ld4_lin_p524288_lp1_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000
    shuffle   | mix_b64_ld1_lin_p524288_lp4_r1000+mix_b128_ld1_indir_p524288_lp1_r1000+mix_b128_ld4_lin_p524288_lp1_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000+mix_b128_ld7_xpage_p1_lp4_r1000+mix_b128_ld14_xpage_p524288_lp4_r1000
    sum       | mix_b128_ld7_xpage_p1_lp4_r1000+mix_b128_ld14_xpage_p524288_lp4_r1000+mix_b64_ld1_lin_p524288_lp4_r1000+mix_b128_ld1_indir_p524288_lp1_r1000+mix_b128_ld4_lin_p524288_lp1_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 631479502066 | 631491102045 | 630321744135
    instructions:u     | 10462080396  | 10462080380  | 10462387210 
    br_retired:u       | 48015247     | 48015246     | 48030457    
    br_mis_pred:u      | 18721        | 19153        | 20386       
    l1i_cache:u        | 1349418280   | 1349387143   | 1343110002  
    l1i_cache_refill:u | 1200127      | 1199633      | 366449      
    l1i_tlb:u          | 1349418280   | 1349387143   | 1343110002  
    l1i_tlb_refill:u   | 5219         | 5147         | 1549        
    l2i_cache:u        | 1201455      | 1201156      | 367521      
    l2i_cache_refill:u | 253518       | 258904       | 21776       
    l2i_tlb:u          | 6171         | 5876         | 3147        
    l2i_tlb_refill:u   | 5215         | 5141         | 1487        
    l1d_cache:u        | 3922033820   | 3923591461   | 3920489088  
    l1d_cache_refill:u | 2481562883   | 2481377211   | 2481489479  
    l1d_tlb:u          | 6299919038   | 6284826597   | 6271910111  
    l1d_tlb_refill:u   | 2307365552   | 2304968002   | 2302988385  
    l2d_cache:u        | 11976437659  | 12006836733  | 12004797158 
    l2d_cache_refill:u | 5909829840   | 5942493153   | 5935565525  
    l2d_tlb:u          | 2307567237   | 2305256705   | 2303154340  
    l2d_tlb_refill:u   | 36594133     | 32214988     | 26020673    
    ll_cache:u         | 5907698621   | 5940326400   | 5933907049  
    ll_cache_miss:u    | 5804485318   | 5833880734   | 5828166551  

== combo_074_s6 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld14_pshuf_p128_lp4_r1000  
    s1 | mix_b128_ld2_xpage_p1_lp4_r1000     
    s2 | mix_b64_ld7_xpage_p524288_lp1_r1000 
    s3 | mix_b64_ld4_lin_p1_lp4_r1000        
    s4 | mix_b64_ld7_xpage_p512_lp4_r1000    
    s5 | mix_b128_ld1_xpage_p524288_lp1_r1000
single_counts:
    metric             | s0          | s1         | s2           | s3         | s4          | s5         
    -------------------+-------------+------------+--------------+------------+-------------+------------
    cpu-cycles:u       | 33807664316 | 1042096793 | 113372988518 | 1043136543 | 19737000493 | 32380763824
    instructions:u     | 2085065005  | 2085064023 | 1061065119   | 1061064029 | 1061063795  | 2085065080 
    br_retired:u       | 8005184     | 8004983    | 8005199      | 8004981    | 8004922     | 8005194    
    br_mis_pred:u      | 3355        | 2442       | 3401         | 1890       | 3489        | 3675       
    l1i_cache:u        | 267397348   | 265058110  | 140562956    | 138080084  | 138205029   | 265259743  
    l1i_cache_refill:u | 24825       | 1291       | 34889        | 979        | 6802        | 28969      
    l1i_tlb:u          | 267397348   | 265058110  | 140562956    | 138080084  | 138205029   | 265259743  
    l1i_tlb_refill:u   | 48          | 41         | 366          | 39         | 45          | 255        
    l2i_cache:u        | 24904       | 1295       | 34947        | 983        | 6814        | 29036      
    l2i_cache_refill:u | 1549        | 594        | 3948         | 534        | 1027        | 1771       
    l2i_tlb:u          | 314         | 154        | 431          | 83         | 111         | 751        
    l2i_tlb_refill:u   | 17          | 10         | 361          | 11         | 27          | 251        
    l1d_cache:u        | 1805059959  | 269037249  | 461144517    | 269045146  | 461150930   | 141045725  
    l1d_cache_refill:u | 612656588   | 169        | 447196352    | 159        | 447492873   | 127880427  
    l1d_tlb:u          | 2473431673  | 269078089  | 908786028    | 269083797  | 915321783   | 275328998  
    l1d_tlb_refill:u   | 450000196   | 77         | 436106081    | 83         | 450095038   | 126060836  
    l2d_cache:u        | 5989245562  | 1977       | 1860894585   | 1751       | 1797654802  | 511131882  
    l2d_cache_refill:u | 956792882   | 860        | 973869409    | 963        | 906535911   | 260744102  
    l2d_tlb:u          | 450003997   | 106        | 436138291    | 125        | 450102499   | 126076193  
    l2d_tlb_refill:u   | 12          | 5          | 5195952      | 21         | 218         | 1272587    
    ll_cache:u         | 956728045   | 238        | 973668667    | 349        | 906524458   | 260635463  
    ll_cache_miss:u    | 63385894    | 23         | 969143219    | 30         | 5925844     | 259148252  
combined_orders:
    id        | modules                                                                                                                                                                                                  
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld2_xpage_p1_lp4_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b64_ld7_xpage_p512_lp4_r1000+mix_b128_ld1_xpage_p524288_lp1_r1000
    shuffle   | mix_b64_ld7_xpage_p524288_lp1_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld2_xpage_p1_lp4_r1000+mix_b128_ld1_xpage_p524288_lp1_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b64_ld7_xpage_p512_lp4_r1000
    sum       | mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld2_xpage_p1_lp4_r1000+mix_b64_ld7_xpage_p524288_lp1_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b64_ld7_xpage_p512_lp4_r1000+mix_b128_ld1_xpage_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 225516599669 | 220017353266 | 201383650487
    instructions:u     | 9438080081   | 9438080135   | 9438387051  
    br_retired:u       | 48015202     | 48015210     | 48030463    
    br_mis_pred:u      | 17603        | 18192        | 18252       
    l1i_cache:u        | 1220138565   | 1220160734   | 1214563270  
    l1i_cache_refill:u | 552475       | 532531       | 97755       
    l1i_tlb:u          | 1220138565   | 1220160734   | 1214563270  
    l1i_tlb_refill:u   | 1982         | 1904         | 794         
    l2i_cache:u        | 552635       | 532670       | 97979       
    l2i_cache_refill:u | 141867       | 146086       | 9423        
    l2i_tlb:u          | 2931         | 3049         | 1844        
    l2i_tlb_refill:u   | 1977         | 1900         | 677         
    l1d_cache:u        | 3412447182   | 3413083276   | 3406483526  
    l1d_cache_refill:u | 1639757163   | 1626376624   | 1635226568  
    l1d_tlb:u          | 5124958914   | 5122239850   | 5111030368  
    l1d_tlb_refill:u   | 1466080727   | 1466273321   | 1462262311  
    l2d_cache:u        | 10150572277  | 10230700165  | 10158930559 
    l2d_cache_refill:u | 3204893460   | 3330288788   | 3097944127  
    l2d_tlb:u          | 1466263225   | 1466450390   | 1462321211  
    l2d_tlb_refill:u   | 10923739     | 11394154     | 6468795     
    ll_cache:u         | 3204233645   | 3329547021   | 3097557220  
    ll_cache_miss:u    | 1440443722   | 1475838431   | 1297603262  

== combo_075_s6 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld2_pshuf_p524288_lp4_r1000
    s1 | mix_b64_ld1_indir_p1_lp4_r1000      
    s2 | mix_b64_ld14_lin_p128_lp4_r1000     
    s3 | mix_b64_ld14_xpage_p524288_lp4_r1000
    s4 | mix_b128_ld1_lin_p524288_lp4_r1000  
    s5 | mix_b64_ld1_pshuf_p512_lp4_r1000    
single_counts:
    metric             | s0          | s1         | s2          | s3           | s4          | s5        
    -------------------+-------------+------------+-------------+--------------+-------------+-----------
    cpu-cycles:u       | 20902855729 | 274097882  | 14291877934 | 225782882912 | 13312140499 | 2726942547
    instructions:u     | 2085064012  | 1061064170 | 1061063801  | 1061065117   | 2085063795  | 1061063795
    br_retired:u       | 8004978     | 8005003    | 8004920     | 8005207      | 8004922     | 8004922   
    br_mis_pred:u      | 3134        | 2125       | 2888        | 3281         | 3223        | 2061      
    l1i_cache:u        | 266556655   | 137041693  | 137780621   | 138876571    | 266695418   | 137305982 
    l1i_cache_refill:u | 23923       | 629        | 5083        | 65977        | 14795       | 1548      
    l1i_tlb:u          | 266556655   | 137041693  | 137780621   | 138876571    | 266695418   | 137305982 
    l1i_tlb_refill:u   | 212         | 38         | 49          | 429          | 135         | 36        
    l2i_cache:u        | 23945       | 630        | 5097        | 66118        | 14821       | 1553      
    l2i_cache_refill:u | 3921        | 524        | 728         | 6246         | 2031        | 892       
    l2i_tlb:u          | 501         | 86         | 93          | 492          | 678         | 91        
    l2i_tlb_refill:u   | 207         | 11         | 15          | 423          | 129         | 25        
    l1d_cache:u        | 269224983   | 77033974   | 909198370   | 909128941    | 141297063   | 77124074  
    l1d_cache_refill:u | 113065944   | 159        | 194683631   | 897215791    | 35394182    | 33293537  
    l1d_tlb:u          | 269876038   | 77048479   | 1236548784  | 1796301859   | 141706167   | 102025274 
    l1d_tlb_refill:u   | 204204      | 73         | 226026986   | 870302197    | 104417      | 17000219  
    l2d_cache:u        | 992231612   | 1406       | 2892434392  | 3567169936   | 409898707   | 207744582 
    l2d_cache_refill:u | 489150061   | 825        | 521417703   | 1811222475   | 226845614   | 89704161  
    l2d_tlb:u          | 212683      | 331        | 226097513   | 870350920    | 110069      | 17000293  
    l2d_tlb_refill:u   | 137568      | 6          | 107         | 10177930     | 71867       | 564       
    ll_cache:u         | 489054487   | 277        | 521386022   | 1811502810   | 226832972   | 89698477  
    ll_cache_miss:u    | 417772386   | 36         | 2218881     | 1805378980   | 217864990   | 159830    
combined_orders:
    id        | modules                                                                                                                                                                                                     
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld2_pshuf_p524288_lp4_r1000+mix_b64_ld1_indir_p1_lp4_r1000+mix_b64_ld14_lin_p128_lp4_r1000+mix_b64_ld14_xpage_p524288_lp4_r1000+mix_b128_ld1_lin_p524288_lp4_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000
    shuffle   | mix_b128_ld1_lin_p524288_lp4_r1000+mix_b64_ld14_xpage_p524288_lp4_r1000+mix_b128_ld2_pshuf_p524288_lp4_r1000+mix_b64_ld14_lin_p128_lp4_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b64_ld1_indir_p1_lp4_r1000
    sum       | mix_b128_ld2_pshuf_p524288_lp4_r1000+mix_b64_ld1_indir_p1_lp4_r1000+mix_b64_ld14_lin_p128_lp4_r1000+mix_b64_ld14_xpage_p524288_lp4_r1000+mix_b128_ld1_lin_p524288_lp4_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 279604586463 | 279857152392 | 277290797503
    instructions:u     | 8414080333   | 8414080333   | 8414384690  
    br_retired:u       | 48015239     | 48015239     | 48029952    
    br_mis_pred:u      | 14601        | 9287         | 16712       
    l1i_cache:u        | 1086334935   | 1086200168   | 1084256940  
    l1i_cache_refill:u | 569225       | 509215       | 111955      
    l1i_tlb:u          | 1086334935   | 1086200168   | 1084256940  
    l1i_tlb_refill:u   | 2435         | 2527         | 899         
    l2i_cache:u        | 569635       | 509535       | 112164      
    l2i_cache_refill:u | 96589        | 99893        | 14342       
    l2i_tlb:u          | 3384         | 3452         | 1941        
    l2i_tlb_refill:u   | 2431         | 2520         | 810         
    l1d_cache:u        | 2382973194   | 2383665581   | 2383007405  
    l1d_cache_refill:u | 1307550444   | 1301001993   | 1273653244  
    l1d_tlb:u          | 3583855720   | 3590514584   | 3623506601  
    l1d_tlb_refill:u   | 1113843723   | 1114138975   | 1113638096  
    l2d_cache:u        | 7876225206   | 7858026453   | 8069480635  
    l2d_cache_refill:u | 3307602489   | 3248803555   | 3138340839  
    l2d_tlb:u          | 1113951645   | 1114266587   | 1113771809  
    l2d_tlb_refill:u   | 14752989     | 13915168     | 10388042    
    ll_cache:u         | 3306731880   | 3247854139   | 3138475045  
    ll_cache_miss:u    | 2660360381   | 2641285667   | 2443395103  

== combo_076_s6 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld4_pshuf_p512_lp4_r1000    
    s1 | mix_b64_ld2_pshuf_p524288_lp1_r1000 
    s2 | mix_b128_ld7_lin_p512_lp1_r1000     
    s3 | mix_b64_ld7_pshuf_p128_lp4_r1000    
    s4 | mix_b128_ld4_indir_p524288_lp4_r1000
    s5 | mix_b64_ld7_lin_p1_lp4_r1000        
single_counts:
    metric             | s0          | s1         | s2          | s3         | s4           | s5        
    -------------------+-------------+------------+-------------+------------+--------------+-----------
    cpu-cycles:u       | 10005997190 | 5444713478 | 37601258381 | 8870847227 | 130569674918 | 1810087844
    instructions:u     | 1061063795  | 1061063795 | 2085065072  | 1061063795 | 2085065046   | 1061064029
    br_retired:u       | 8004922     | 8004922    | 8005192     | 8004922    | 8005189      | 8004981   
    br_mis_pred:u      | 2933        | 2343       | 3540        | 2170       | 2919         | 2435      
    l1i_cache:u        | 138571688   | 138524854  | 265465169   | 138129617  | 270879491    | 137053661 
    l1i_cache_refill:u | 3858        | 2563       | 26263       | 3629       | 96881        | 1263      
    l1i_tlb:u          | 138571688   | 138524854  | 265465169   | 138129617  | 270879491    | 137053661 
    l1i_tlb_refill:u   | 46          | 52         | 46          | 54         | 470          | 38        
    l2i_cache:u        | 3864        | 2568       | 26358       | 3634       | 97045        | 1266      
    l2i_cache_refill:u | 1868        | 685        | 1734        | 1748       | 6461         | 531       
    l2i_tlb:u          | 770         | 157        | 99          | 181        | 574          | 217       
    l2i_tlb_refill:u   | 19          | 46         | 28          | 32         | 466          | 11        
    l1d_cache:u        | 269474665   | 141109397  | 909306146   | 461601243  | 527072110    | 461037778 
    l1d_cache_refill:u | 129900436   | 24229434   | 896052825   | 162570153  | 513439836    | 174       
    l1d_tlb:u          | 366781268   | 142293944  | 1812211887  | 632925106  | 1043691322   | 461083928 
    l1d_tlb_refill:u   | 66082887    | 394256     | 898217608   | 114000100  | 499321988    | 78        
    l2d_cache:u        | 833775617   | 564128040  | 3539168834  | 1431747710 | 2063135934   | 1848      
    l2d_cache_refill:u | 373017163   | 231748046  | 1793949418  | 223991087  | 1037765854   | 830       
    l2d_tlb:u          | 66127082    | 395097     | 898237597   | 114119708  | 499654309    | 143       
    l2d_tlb_refill:u   | 221         | 237961     | 745         | 22         | 5430770      | 9         
    ll_cache:u         | 372989236   | 231607480  | 1793931271  | 223976764  | 1037193704   | 237       
    ll_cache_miss:u    | 1135707     | 211369640  | 100086      | 88370      | 1020088975   | 57        
combined_orders:
    id        | modules                                                                                                                                                                                                
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld4_pshuf_p512_lp4_r1000+mix_b64_ld2_pshuf_p524288_lp1_r1000+mix_b128_ld7_lin_p512_lp1_r1000+mix_b64_ld7_pshuf_p128_lp4_r1000+mix_b128_ld4_indir_p524288_lp4_r1000+mix_b64_ld7_lin_p1_lp4_r1000
    shuffle   | mix_b64_ld4_pshuf_p512_lp4_r1000+mix_b128_ld4_indir_p524288_lp4_r1000+mix_b128_ld7_lin_p512_lp1_r1000+mix_b64_ld7_lin_p1_lp4_r1000+mix_b64_ld7_pshuf_p128_lp4_r1000+mix_b64_ld2_pshuf_p524288_lp1_r1000
    sum       | mix_b64_ld4_pshuf_p512_lp4_r1000+mix_b64_ld2_pshuf_p524288_lp1_r1000+mix_b128_ld7_lin_p512_lp1_r1000+mix_b64_ld7_pshuf_p128_lp4_r1000+mix_b128_ld4_indir_p524288_lp4_r1000+mix_b64_ld7_lin_p1_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 193689623066 | 193500213169 | 194302579038
    instructions:u     | 8414080151   | 8414080081   | 8414385532  
    br_retired:u       | 48015211     | 48015202     | 48030128    
    br_mis_pred:u      | 13220        | 15252        | 16340       
    l1i_cache:u        | 1090717223   | 1090631471   | 1088624480  
    l1i_cache_refill:u | 465746       | 444000       | 134457      
    l1i_tlb:u          | 1090717223   | 1090631471   | 1088624480  
    l1i_tlb_refill:u   | 1676         | 1690         | 706         
    l2i_cache:u        | 465945       | 444754       | 134735      
    l2i_cache_refill:u | 73908        | 74178        | 13027       
    l2i_tlb:u          | 2340         | 2484         | 1998        
    l2i_tlb_refill:u   | 1671         | 1687         | 602         
    l1d_cache:u        | 2769591302   | 2769579765   | 2769601339  
    l1d_cache_refill:u | 1715555012   | 1712968433   | 1726192858  
    l1d_tlb:u          | 4464076822   | 4468735035   | 4458987455  
    l1d_tlb_refill:u   | 1578135650   | 1578128061   | 1578016917  
    l2d_cache:u        | 8529295963   | 8516068735   | 8431957983  
    l2d_cache_refill:u | 3816176558   | 3771850606   | 3660472398  
    l2d_tlb:u          | 1578662759   | 1578645205   | 1578533936  
    l2d_tlb_refill:u   | 8552629      | 9522271      | 5669728     
    ll_cache:u         | 3814994969   | 3770765562   | 3659698692  
    ll_cache_miss:u    | 1366993271   | 1362895776   | 1232782835  

== combo_077_s6 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld7_pshuf_p512_lp4_r1000   
    s1 | mix_b64_ld7_indir_p512_lp4_r1000   
    s2 | mix_b64_ld1_pshuf_p128_lp1_r1000   
    s3 | mix_b128_ld14_lin_p524288_lp1_r1000
    s4 | mix_b128_ld7_xpage_p1_lp4_r1000    
    s5 | mix_b128_ld1_xpage_p128_lp4_r1000  
single_counts:
    metric             | s0          | s1          | s2         | s3          | s4         | s5        
    -------------------+-------------+-------------+------------+-------------+------------+-----------
    cpu-cycles:u       | 16930913164 | 19788487833 | 1979714255 | 74219553432 | 3602121899 | 2815969945
    instructions:u     | 1061063801  | 1061063801  | 1061064029 | 2085065124  | 2085063795 | 2085063795
    br_retired:u       | 8004920     | 8004920     | 8004981    | 8005199     | 8004922    | 8004922   
    br_mis_pred:u      | 2549        | 3061        | 2382       | 3456        | 2830       | 2360      
    l1i_cache:u        | 139410084   | 137747963   | 137083897  | 268684600   | 266064183  | 265113361 
    l1i_cache_refill:u | 5842        | 6853        | 1274       | 55975       | 3484       | 2915      
    l1i_tlb:u          | 139410084   | 137747963   | 137083897  | 268684600   | 266064183  | 265113361 
    l1i_tlb_refill:u   | 43          | 46          | 40         | 366         | 48         | 46        
    l2i_cache:u        | 5857        | 6868        | 1276       | 56085       | 3489       | 2920      
    l2i_cache_refill:u | 2680        | 1100        | 559        | 2662        | 632        | 713       
    l2i_tlb:u          | 97          | 106         | 153        | 681         | 102        | 89        
    l2i_tlb_refill:u   | 21          | 24          | 12         | 362         | 12         | 14        
    l1d_cache:u        | 462151117   | 461669644   | 77049904   | 1807310609  | 909038124  | 141067225 
    l1d_cache_refill:u | 199254398   | 443081301   | 61302835   | 339007097   | 181        | 114793243 
    l1d_tlb:u          | 628753390   | 894874794   | 148579044  | 1819955534  | 909086113  | 277904098 
    l1d_tlb_refill:u   | 114211418   | 428286036   | 66005573   | 5490474     | 103        | 130000068 
    l2d_cache:u        | 1620250920  | 1783753492  | 183961298  | 7567871352  | 3851       | 399953131 
    l2d_cache_refill:u | 700774761   | 863524043   | 55977044   | 3106113019  | 836        | 63144100  
    l2d_tlb:u          | 114287791   | 428325074   | 66005801   | 5508021     | 125        | 130001450 
    l2d_tlb_refill:u   | 426         | 209         | 44         | 3330385     | 9          | 25        
    ll_cache:u         | 700709911   | 863481385   | 55975739   | 3104302373  | 210        | 63142574  
    ll_cache_miss:u    | 6436749     | 19704306    | 252        | 2830589973  | 28         | 5736      
combined_orders:
    id        | modules                                                                                                                                                                                                 
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b64_ld1_pshuf_p128_lp1_r1000+mix_b128_ld14_lin_p524288_lp1_r1000+mix_b128_ld7_xpage_p1_lp4_r1000+mix_b128_ld1_xpage_p128_lp4_r1000
    shuffle   | mix_b64_ld1_pshuf_p128_lp1_r1000+mix_b128_ld14_lin_p524288_lp1_r1000+mix_b128_ld1_xpage_p128_lp4_r1000+mix_b128_ld7_xpage_p1_lp4_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b64_ld7_pshuf_p512_lp4_r1000
    sum       | mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b64_ld1_pshuf_p128_lp1_r1000+mix_b128_ld14_lin_p524288_lp1_r1000+mix_b128_ld7_xpage_p1_lp4_r1000+mix_b128_ld1_xpage_p128_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 137480313815 | 140122325122 | 119336760528
    instructions:u     | 9438080056   | 9438080107   | 9438384345  
    br_retired:u       | 48015190     | 48015197     | 48029864    
    br_mis_pred:u      | 12541        | 16141        | 16638       
    l1i_cache:u        | 1217238854   | 1213954081   | 1214104088  
    l1i_cache_refill:u | 446137       | 442486       | 76343       
    l1i_tlb:u          | 1217238854   | 1213954081   | 1214104088  
    l1i_tlb_refill:u   | 987          | 1017         | 589         
    l2i_cache:u        | 446264       | 442638       | 76495       
    l2i_cache_refill:u | 72388        | 79213        | 8346        
    l2i_tlb:u          | 1663         | 1925         | 1228        
    l2i_tlb_refill:u   | 982          | 1014         | 445         
    l1d_cache:u        | 3858216055   | 3857846555   | 3858286623  
    l1d_cache_refill:u | 1131819269   | 1132382860   | 1157439055  
    l1d_tlb:u          | 4679254613   | 4678810557   | 4679152973  
    l1d_tlb_refill:u   | 744112334    | 743985753    | 743993672   
    l2d_cache:u        | 11610244416  | 11655266597  | 11555794044 
    l2d_cache_refill:u | 4852772955   | 4884669047   | 4789533803  
    l2d_tlb:u          | 744261197    | 744145019    | 744128262   
    l2d_tlb_refill:u   | 5452910      | 5465828      | 3331098     
    ll_cache:u         | 4850674993   | 4882543474   | 4787612192  
    ll_cache_miss:u    | 2910684901   | 2919315857   | 2856737044  

== combo_078_s6 ==
single_modules:
    id | module                           
    ---+----------------------------------
    s0 | mix_b64_ld14_indir_p512_lp1_r1000
    s1 | mix_b64_ld2_indir_p1_lp1_r1000   
    s2 | mix_b128_ld14_lin_p512_lp4_r1000 
    s3 | mix_b64_ld14_xpage_p128_lp4_r1000
    s4 | mix_b128_ld2_pshuf_p128_lp4_r1000
    s5 | mix_b64_ld1_xpage_p128_lp1_r1000 
single_counts:
    metric             | s0          | s1         | s2          | s3          | s4         | s5        
    -------------------+-------------+------------+-------------+-------------+------------+-----------
    cpu-cycles:u       | 37649828864 | 530947316  | 52256348854 | 22624923767 | 4943040942 | 1628972661
    instructions:u     | 1061065029  | 1061064020 | 2085065068  | 1061064018  | 2085063808 | 1061064029
    br_retired:u       | 8005187     | 8004980    | 8005192     | 8004976     | 8004922    | 8004981   
    br_mis_pred:u      | 3170        | 2337       | 3406        | 3365        | 2340       | 1957      
    l1i_cache:u        | 140010766   | 138086781  | 267130606   | 138814204   | 266350050  | 137198874 
    l1i_cache_refill:u | 12093       | 806        | 35798       | 8751        | 4496       | 1229      
    l1i_tlb:u          | 140010766   | 138086781  | 267130606   | 138814204   | 266350050  | 137198874 
    l1i_tlb_refill:u   | 48          | 39         | 49          | 54          | 47         | 47        
    l2i_cache:u        | 12123       | 809        | 35901       | 8763        | 4508       | 1229      
    l2i_cache_refill:u | 1147        | 529        | 2585        | 1137        | 831        | 613       
    l2i_tlb:u          | 163         | 142        | 137         | 299         | 164        | 767       
    l2i_tlb_refill:u   | 30          | 10         | 28          | 44          | 16         | 15        
    l1d_cache:u        | 910991867   | 141052855  | 1807487548  | 909743145   | 269058735  | 77101611  
    l1d_cache_refill:u | 897326708   | 186        | 569439203   | 855229024   | 86092670   | 61489233  
    l1d_tlb:u          | 1817923649  | 141101028  | 2312560476  | 1816051510  | 374564659  | 149096118 
    l1d_tlb_refill:u   | 899578807   | 65         | 451505532   | 898489931   | 66003303   | 66019780  
    l2d_cache:u        | 3544822998  | 1445       | 6013995271  | 2418581330  | 837925960  | 187806752 
    l2d_cache_refill:u | 1796434777  | 765        | 3192219509  | 539041655   | 129225029  | 57993208  
    l2d_tlb:u          | 899742855   | 84         | 451532517   | 898532110   | 66003668   | 66020253  
    l2d_tlb_refill:u   | 420         | 3          | 346         | 7           | 23         | 19        
    ll_cache:u         | 1796417162  | 242        | 3191790648  | 539034987   | 129220442  | 57991677  
    ll_cache_miss:u    | 194898      | 36         | 205039313   | 60189       | 10110      | 2389      
combined_orders:
    id        | modules                                                                                                                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_indir_p512_lp1_r1000+mix_b64_ld2_indir_p1_lp1_r1000+mix_b128_ld14_lin_p512_lp4_r1000+mix_b64_ld14_xpage_p128_lp4_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b64_ld1_xpage_p128_lp1_r1000
    shuffle   | mix_b64_ld14_xpage_p128_lp4_r1000+mix_b64_ld2_indir_p1_lp1_r1000+mix_b64_ld14_indir_p512_lp1_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b128_ld14_lin_p512_lp4_r1000+mix_b64_ld1_xpage_p128_lp1_r1000
    sum       | mix_b64_ld14_indir_p512_lp1_r1000+mix_b64_ld2_indir_p1_lp1_r1000+mix_b128_ld14_lin_p512_lp4_r1000+mix_b64_ld14_xpage_p128_lp4_r1000+mix_b128_ld2_pshuf_p128_lp4_r1000+mix_b64_ld1_xpage_p128_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 151587860407 | 159107213030 | 119634062404
    instructions:u     | 8414080073   | 8414080095   | 8414385972  
    br_retired:u       | 48015193     | 48015196     | 48030238    
    br_mis_pred:u      | 13524        | 14320        | 16575       
    l1i_cache:u        | 1088597404   | 1087443119   | 1087591281  
    l1i_cache_refill:u | 404727       | 395485       | 63173       
    l1i_tlb:u          | 1088597404   | 1087443119   | 1087591281  
    l1i_tlb_refill:u   | 49           | 91           | 284         
    l2i_cache:u        | 404849       | 395607       | 63333       
    l2i_cache_refill:u | 50335        | 50578        | 6842        
    l2i_tlb:u          | 264          | 484          | 1672        
    l2i_tlb_refill:u   | 45           | 83           | 143         
    l1d_cache:u        | 4114225207   | 4116704561   | 4115435761  
    l1d_cache_refill:u | 2439799646   | 2434708492   | 2469577024  
    l1d_tlb:u          | 6663667872   | 6678683013   | 6611297440  
    l1d_tlb_refill:u   | 2380393743   | 2381150817   | 2381597418  
    l2d_cache:u        | 12520800482  | 12774336228  | 13003133756 
    l2d_cache_refill:u | 5556966977   | 5614525265   | 5714914943  
    l2d_tlb:u          | 2380550497   | 2381441926   | 2381831487  
    l2d_tlb_refill:u   | 948744       | 961866       | 818         
    ll_cache:u         | 5556390160   | 5614070039   | 5714455158  
    ll_cache_miss:u    | 789653963    | 255011563    | 205306935   

== combo_079_s6 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b64_ld7_xpage_p1_lp4_r1000       
    s1 | mix_b64_ld4_lin_p1_lp4_r1000         
    s2 | mix_b128_ld4_xpage_p128_lp1_r1000    
    s3 | mix_b64_ld14_indir_p128_lp1_r1000    
    s4 | mix_b128_ld14_indir_p524288_lp1_r1000
    s5 | mix_b128_ld2_indir_p128_lp1_r1000    
single_counts:
    metric             | s0         | s1         | s2          | s3          | s4           | s5        
    -------------------+------------+------------+-------------+-------------+--------------+-----------
    cpu-cycles:u       | 1810089545 | 1043123543 | 13369780342 | 26036867785 | 452988253207 | 7555568197
    instructions:u     | 1061064029 | 1061064023 | 2085063801  | 1061064901  | 2085065405   | 2085063801
    br_retired:u       | 8004981    | 8004983    | 8004920     | 8005169     | 8005248      | 8004920   
    br_mis_pred:u      | 2404       | 1928       | 2337        | 3350        | 5119         | 2878      
    l1i_cache:u        | 138056571  | 137080315  | 266003116   | 139243878   | 267211601    | 265074197 
    l1i_cache_refill:u | 1212       | 925        | 10539       | 8885        | 273951       | 6893      
    l1i_tlb:u          | 138056571  | 137080315  | 266003116   | 139243878   | 267211601    | 265074197 
    l1i_tlb_refill:u   | 39         | 42         | 48          | 51          | 584          | 45        
    l2i_cache:u        | 1212       | 928        | 10571       | 8904        | 274797       | 6915      
    l2i_cache_refill:u | 544        | 501        | 854         | 988         | 11922        | 722       
    l2i_tlb:u          | 159        | 86         | 118         | 305         | 1052         | 142       
    l2i_tlb_refill:u   | 11         | 11         | 18          | 13          | 580          | 18        
    l1d_cache:u        | 461037516  | 269044888  | 525719042   | 909928922   | 1805323671   | 269064210 
    l1d_cache_refill:u | 177        | 153        | 493508571   | 859362124   | 1791495537   | 240908210 
    l1d_tlb:u          | 461083944  | 269083518  | 1048263254  | 1817290016  | 3570253724   | 532738811 
    l1d_tlb_refill:u   | 76         | 70         | 514284248   | 899665542   | 1738139469   | 258000135 
    l2d_cache:u        | 1814       | 1527       | 1459920855  | 2498914933  | 7118532995   | 767447505 
    l2d_cache_refill:u | 802        | 776        | 407151482   | 704743304   | 3614695177   | 228285821 
    l2d_tlb:u          | 92         | 147        | 514553758   | 899717404   | 1738216887   | 258501430 
    l2d_tlb_refill:u   | 9          | 6          | 134         | 35          | 20076196     | 18        
    ll_cache:u         | 236        | 245        | 407148051   | 704736830   | 3614097785   | 228283836 
    ll_cache_miss:u    | 34         | 21         | 15778       | 23455       | 3600352708   | 2963      
combined_orders:
    id        | modules                                                                                                                                                                                                
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_xpage_p1_lp4_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld4_xpage_p128_lp1_r1000+mix_b64_ld14_indir_p128_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000+mix_b128_ld2_indir_p128_lp1_r1000
    shuffle   | mix_b128_ld2_indir_p128_lp1_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b64_ld14_indir_p128_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000+mix_b64_ld7_xpage_p1_lp4_r1000+mix_b128_ld4_xpage_p128_lp1_r1000
    sum       | mix_b64_ld7_xpage_p1_lp4_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld4_xpage_p128_lp1_r1000+mix_b64_ld14_indir_p128_lp1_r1000+mix_b128_ld14_indir_p524288_lp1_r1000+mix_b128_ld2_indir_p128_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 506511315437 | 501770509170 | 502803682619
    instructions:u     | 9438080353   | 9438080423   | 9438385960  
    br_retired:u       | 48015242     | 48015251     | 48030221    
    br_mis_pred:u      | 20747        | 18287        | 18016       
    l1i_cache:u        | 1213884673   | 1213638313   | 1212669678  
    l1i_cache_refill:u | 731520       | 733314       | 302405      
    l1i_tlb:u          | 1213884673   | 1213638313   | 1212669678  
    l1i_tlb_refill:u   | 1408         | 1457         | 809         
    l2i_cache:u        | 732331       | 734032       | 303327      
    l2i_cache_refill:u | 66163        | 66797        | 15531       
    l2i_tlb:u          | 2785         | 2190         | 1862        
    l2i_tlb_refill:u   | 1402         | 1454         | 651         
    l1d_cache:u        | 4239134902   | 4239127085   | 4240118249  
    l1d_cache_refill:u | 3384124898   | 3392758759   | 3385274772  
    l1d_tlb:u          | 7692736572   | 7690748545   | 7698713267  
    l1d_tlb_refill:u   | 3408475339   | 3408629455   | 3410089540  
    l2d_cache:u        | 12013415967  | 12106710771  | 11844819629 
    l2d_cache_refill:u | 5138611935   | 5275046618   | 4954877362  
    l2d_tlb:u          | 3408999994   | 3408950920   | 3410989718  
    l2d_tlb_refill:u   | 16445124     | 16401906     | 20076398    
    ll_cache:u         | 5137898095   | 5274341974   | 4954266983  
    ll_cache_miss:u    | 3608390242   | 3603277708   | 3600394959  

== combo_080_s6 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld1_xpage_p1_lp4_r1000     
    s1 | mix_b128_ld4_xpage_p1_lp1_r1000     
    s2 | mix_b64_ld2_lin_p128_lp4_r1000      
    s3 | mix_b128_ld4_indir_p524288_lp1_r1000
    s4 | mix_b64_ld14_lin_p524288_lp4_r1000  
    s5 | mix_b64_ld2_xpage_p128_lp4_r1000    
single_counts:
    metric             | s0         | s1         | s2         | s3           | s4          | s5        
    -------------------+------------+------------+------------+--------------+-------------+-----------
    cpu-cycles:u       | 530114642  | 2066904667 | 2006329531 | 129367361353 | 90715918799 | 3066844871
    instructions:u     | 2085064023 | 2085064014 | 1061064023 | 2085065076   | 1061065073  | 1061063801
    br_retired:u       | 8004983    | 8004982    | 8004983    | 8005194      | 8005193     | 8004920   
    br_mis_pred:u      | 2297       | 2461       | 2235       | 3312         | 3493        | 2415      
    l1i_cache:u        | 266040487  | 266061936  | 137099659  | 269649610    | 138961070   | 137131733 
    l1i_cache_refill:u | 1063       | 2085       | 1338       | 97286        | 29005       | 1612      
    l1i_tlb:u          | 266040487  | 266061936  | 137099659  | 269649610    | 138961070   | 137131733 
    l1i_tlb_refill:u   | 38         | 46         | 40         | 471          | 336         | 39        
    l2i_cache:u        | 1062       | 2091       | 1340       | 97439        | 29058       | 1615      
    l2i_cache_refill:u | 614        | 644        | 608        | 4447         | 5298        | 577       
    l2i_tlb:u          | 776        | 91         | 314        | 541          | 460         | 91        
    l2i_tlb_refill:u   | 12         | 13         | 14         | 465          | 333         | 11        
    l1d_cache:u        | 141033845  | 525038719  | 141058048  | 526744622    | 913015725   | 141060447 
    l1d_cache_refill:u | 163        | 152        | 26895478   | 512687388    | 208619068   | 116782800 
    l1d_tlb:u          | 141048071  | 525084184  | 194606887  | 1043195833   | 918282774   | 277734261 
    l1d_tlb_refill:u   | 69         | 76         | 34002888   | 498987326    | 706074      | 130000114 
    l2d_cache:u        | 1496       | 2723       | 349004481  | 2038795395   | 3521371645  | 395967767 
    l2d_cache_refill:u | 830        | 921        | 83414757   | 1035759170   | 2052162157  | 82795211  
    l2d_tlb:u          | 104        | 176        | 34005191   | 499272627    | 725049      | 130121930 
    l2d_tlb_refill:u   | 3          | 4          | 111        | 5944549      | 457225      | 100       
    ll_cache:u         | 214        | 280        | 83408963   | 1035558689   | 2051859708  | 82794023  
    ll_cache_miss:u    | 27         | 25         | 77860      | 1029678373   | 1957367606  | 604       
combined_orders:
    id        | modules                                                                                                                                                                                                
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld1_xpage_p1_lp4_r1000+mix_b128_ld4_xpage_p1_lp1_r1000+mix_b64_ld2_lin_p128_lp4_r1000+mix_b128_ld4_indir_p524288_lp1_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b64_ld2_xpage_p128_lp4_r1000
    shuffle   | mix_b128_ld4_xpage_p1_lp1_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b64_ld2_lin_p128_lp4_r1000+mix_b128_ld1_xpage_p1_lp4_r1000+mix_b128_ld4_indir_p524288_lp1_r1000+mix_b64_ld2_xpage_p128_lp4_r1000
    sum       | mix_b128_ld1_xpage_p1_lp4_r1000+mix_b128_ld4_xpage_p1_lp1_r1000+mix_b64_ld2_lin_p128_lp4_r1000+mix_b128_ld4_indir_p524288_lp1_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b64_ld2_xpage_p128_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 230588942272 | 230709090441 | 227753473863
    instructions:u     | 9438080066   | 9438080160   | 9438386010  
    br_retired:u       | 48015200     | 48015212     | 48030255    
    br_mis_pred:u      | 18110        | 16561        | 16213       
    l1i_cache:u        | 1219971474   | 1220462791   | 1214944495  
    l1i_cache_refill:u | 544865       | 540556       | 132389      
    l1i_tlb:u          | 1219971474   | 1220462791   | 1214944495  
    l1i_tlb_refill:u   | 1952         | 1960         | 970         
    l2i_cache:u        | 545575       | 541008       | 132605      
    l2i_cache_refill:u | 103859       | 102401       | 12188       
    l2i_tlb:u          | 3288         | 2702         | 2273        
    l2i_tlb_refill:u   | 1946         | 1957         | 848         
    l1d_cache:u        | 2388009589   | 2388293282   | 2387951406  
    l1d_cache_refill:u | 883558936    | 880568369    | 864985049   
    l1d_tlb:u          | 3094575748   | 3094904476   | 3099952010  
    l1d_tlb_refill:u   | 663968224    | 663927110    | 663696547   
    l2d_cache:u        | 6210746459   | 6206145588   | 6305143507  
    l2d_cache_refill:u | 3255098802   | 3243764731   | 3254133046  
    l2d_tlb:u          | 664337268    | 664573565    | 664125077   
    l2d_tlb_refill:u   | 8066033      | 8497754      | 6401992     
    ll_cache:u         | 3254161940   | 3243109340   | 3253621877  
    ll_cache_miss:u    | 3012137721   | 3004074102   | 2987124495  

== combo_081_s6 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b128_ld4_lin_p524288_lp4_r1000 
    s1 | mix_b128_ld2_xpage_p512_lp4_r1000  
    s2 | mix_b64_ld2_xpage_p524288_lp4_r1000
    s3 | mix_b128_ld7_pshuf_p512_lp4_r1000  
    s4 | mix_b64_ld2_xpage_p1_lp1_r1000     
    s5 | mix_b64_ld2_pshuf_p128_lp4_r1000   
single_counts:
    metric             | s0          | s1          | s2          | s3          | s4         | s5        
    -------------------+-------------+-------------+-------------+-------------+------------+-----------
    cpu-cycles:u       | 53216917147 | 11276386634 | 32361523142 | 31357155761 | 530940045  | 2281192058
    instructions:u     | 2085065092  | 2085063801  | 1061065056  | 2085065072  | 1061064014 | 1061064036
    br_retired:u       | 8005195     | 8004920     | 8005191     | 8005192     | 8004982    | 8004983   
    br_mis_pred:u      | 3149        | 2151        | 3372        | 2626        | 2359       | 2152      
    l1i_cache:u        | 266993289   | 266120788   | 138212993   | 268504781   | 138086261  | 137268573 
    l1i_cache_refill:u | 51366       | 8929        | 12161       | 24268       | 788        | 1311      
    l1i_tlb:u          | 266993289   | 266120788   | 138212993   | 268504781   | 138086261  | 137268573 
    l1i_tlb_refill:u   | 342         | 45          | 229         | 49          | 39         | 44        
    l2i_cache:u        | 51439       | 8958        | 12190       | 24345       | 790        | 1313      
    l2i_cache_refill:u | 10128       | 1031        | 2310        | 5438        | 534        | 658       
    l2i_tlb:u          | 405         | 496         | 290         | 87          | 151        | 403       
    l2i_tlb_refill:u   | 336         | 21          | 224         | 30          | 12         | 14        
    l1d_cache:u        | 525246278   | 269072383   | 141726938   | 910665629   | 141052837  | 141108148 
    l1d_cache_refill:u | 129162600   | 255579517   | 128796740   | 306397059   | 204        | 42526523  
    l1d_tlb:u          | 526381680   | 533231992   | 279394038   | 1246903278  | 141101964  | 192942084 
    l1d_tlb_refill:u   | 406994      | 258021697   | 126458817   | 226305502   | 65         | 34011561  
    l2d_cache:u        | 1752862803  | 1098409008  | 510695334   | 3409643309  | 1436       | 407977128 
    l2d_cache_refill:u | 960644634   | 537022878   | 258424205   | 1483362136  | 750        | 50751036  
    l2d_tlb:u          | 422007      | 258028766   | 126558818   | 226377657   | 95         | 34013874  
    l2d_tlb_refill:u   | 270048      | 199         | 1532853     | 325         | 5          | 17        
    ll_cache:u         | 960398394   | 537006439   | 258363022   | 1483182138  | 228        | 50747966  
    ll_cache_miss:u    | 912773186   | 3556857     | 257262297   | 10602167    | 18         | 136       
combined_orders:
    id        | modules                                                                                                                                                                                                   
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld4_lin_p524288_lp4_r1000+mix_b128_ld2_xpage_p512_lp4_r1000+mix_b64_ld2_xpage_p524288_lp4_r1000+mix_b128_ld7_pshuf_p512_lp4_r1000+mix_b64_ld2_xpage_p1_lp1_r1000+mix_b64_ld2_pshuf_p128_lp4_r1000
    shuffle   | mix_b128_ld2_xpage_p512_lp4_r1000+mix_b64_ld2_pshuf_p128_lp4_r1000+mix_b128_ld7_pshuf_p512_lp4_r1000+mix_b64_ld2_xpage_p524288_lp4_r1000+mix_b128_ld4_lin_p524288_lp4_r1000+mix_b64_ld2_xpage_p1_lp1_r1000
    sum       | mix_b128_ld4_lin_p524288_lp4_r1000+mix_b128_ld2_xpage_p512_lp4_r1000+mix_b64_ld2_xpage_p524288_lp4_r1000+mix_b128_ld7_pshuf_p512_lp4_r1000+mix_b64_ld2_xpage_p1_lp1_r1000+mix_b64_ld2_pshuf_p128_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 131921811370 | 132689213830 | 131024114787
    instructions:u     | 9438080072   | 9438079998   | 9438387071  
    br_retired:u       | 48015193     | 48015183     | 48030463    
    br_mis_pred:u      | 14468        | 9429         | 15809       
    l1i_cache:u        | 1215885962   | 1216081975   | 1215186685  
    l1i_cache_refill:u | 445995       | 424503       | 98823       
    l1i_tlb:u          | 1215885962   | 1216081975   | 1215186685  
    l1i_tlb_refill:u   | 1647         | 1651         | 748         
    l2i_cache:u        | 446296       | 424795       | 99035       
    l2i_cache_refill:u | 96431        | 112242       | 20099       
    l2i_tlb:u          | 2563         | 2132         | 1832        
    l2i_tlb_refill:u   | 1643         | 1647         | 637         
    l1d_cache:u        | 2128850162   | 2128966024   | 2128872213  
    l1d_cache_refill:u | 863594858    | 866349704    | 862462643   
    l1d_tlb:u          | 2923440537   | 2922328234   | 2919955036  
    l1d_tlb_refill:u   | 645218732    | 645250054    | 645204636   
    l2d_cache:u        | 7180343916   | 7176560749   | 7179589018  
    l2d_cache_refill:u | 3360212354   | 3383532910   | 3290205639  
    l2d_tlb:u          | 645436271    | 645473244    | 645401217   
    l2d_tlb_refill:u   | 5156030      | 4886708      | 1803447     
    ll_cache:u         | 3359507869   | 3382872759   | 3289698187  
    ll_cache_miss:u    | 1441646712   | 1452373559   | 1184194661  

== combo_082_s6 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b128_ld1_lin_p524288_lp1_r1000
    s1 | mix_b64_ld7_indir_p512_lp4_r1000  
    s2 | mix_b128_ld1_lin_p512_lp4_r1000   
    s3 | mix_b64_ld14_xpage_p128_lp1_r1000 
    s4 | mix_b128_ld7_indir_p1_lp1_r1000   
    s5 | mix_b64_ld2_pshuf_p512_lp1_r1000  
single_counts:
    metric             | s0         | s1          | s2         | s3          | s4         | s5        
    -------------------+------------+-------------+------------+-------------+------------+-----------
    cpu-cycles:u       | 5327766996 | 18775600582 | 4012248770 | 25089152472 | 3602227001 | 5767115450
    instructions:u     | 2085063801 | 1061063795  | 2085063808 | 1061064012  | 2085063786 | 1061063801
    br_retired:u       | 8004920    | 8004922     | 8004922    | 8004978     | 8004921    | 8004920   
    br_mis_pred:u      | 2371       | 3085        | 2758       | 3161        | 2634       | 2660      
    l1i_cache:u        | 266546825  | 138603500   | 265266188  | 137548408   | 266058101  | 138113695 
    l1i_cache_refill:u | 5136       | 6265        | 3562       | 8325        | 60369      | 14016     
    l1i_tlb:u          | 266546825  | 138603500   | 265266188  | 137548408   | 266058101  | 138113695 
    l1i_tlb_refill:u   | 58         | 46          | 44         | 47          | 51         | 48        
    l2i_cache:u        | 5154       | 6282        | 3563       | 8346        | 60528      | 14067     
    l2i_cache_refill:u | 802        | 1120        | 1120       | 781         | 953        | 1134      
    l2i_tlb:u          | 229        | 124         | 111        | 248         | 106        | 125       
    l2i_tlb_refill:u   | 55         | 18          | 24         | 13          | 12         | 25        
    l1d_cache:u        | 141166354  | 461530652   | 141134580  | 909152894   | 909037937  | 141066174 
    l1d_cache_refill:u | 24596563   | 445202943   | 35603458   | 869513040   | 189        | 127563220 
    l1d_tlb:u          | 142407682  | 892499174   | 181284529  | 1813294304  | 909085215  | 277017893 
    l1d_tlb_refill:u   | 394201     | 426448196   | 34013072   | 898080381   | 103        | 130017264 
    l2d_cache:u        | 545929535  | 1733277295  | 415583961  | 2581720459  | 12517      | 514627311 
    l2d_cache_refill:u | 226328130  | 828402424   | 222769908  | 787733236   | 928        | 255982934 
    l2d_tlb:u          | 395005     | 426471263   | 34013966   | 898085534   | 204        | 130027672 
    l2d_tlb_refill:u   | 237025     | 187         | 159        | 20          | 4          | 374       
    ll_cache:u         | 226193980  | 828370112   | 222739398  | 787728969   | 298        | 255978039 
    ll_cache_miss:u    | 207585536  | 3498938     | 1057874    | 13566       | 96         | 8807      
combined_orders:
    id        | modules                                                                                                                                                                                               
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld1_lin_p524288_lp1_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b128_ld1_lin_p512_lp4_r1000+mix_b64_ld14_xpage_p128_lp1_r1000+mix_b128_ld7_indir_p1_lp1_r1000+mix_b64_ld2_pshuf_p512_lp1_r1000
    shuffle   | mix_b128_ld1_lin_p524288_lp1_r1000+mix_b128_ld1_lin_p512_lp4_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b128_ld7_indir_p1_lp1_r1000+mix_b64_ld14_xpage_p128_lp1_r1000+mix_b64_ld2_pshuf_p512_lp1_r1000
    sum       | mix_b128_ld1_lin_p524288_lp1_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b128_ld1_lin_p512_lp4_r1000+mix_b64_ld14_xpage_p128_lp1_r1000+mix_b128_ld7_indir_p1_lp1_r1000+mix_b64_ld2_pshuf_p512_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 75395966342 | 76508881562 | 62574111271
    instructions:u     | 9438079995  | 9438080076  | 9438383003 
    br_retired:u       | 48015182    | 48015194    | 48029583   
    br_mis_pred:u      | 15919       | 16411       | 16669      
    l1i_cache:u        | 1211892047  | 1211989821  | 1212136717 
    l1i_cache_refill:u | 358480      | 342531      | 97673      
    l1i_tlb:u          | 1211892047  | 1211989821  | 1212136717 
    l1i_tlb_refill:u   | 949         | 898         | 294        
    l2i_cache:u        | 358777      | 342829      | 97940      
    l2i_cache_refill:u | 50017       | 48067       | 5910       
    l2i_tlb:u          | 1541        | 1507        | 943        
    l2i_tlb_refill:u   | 945         | 894         | 147        
    l1d_cache:u        | 2703244905  | 2703050375  | 2703088591 
    l1d_cache_refill:u | 1496780708  | 1483049972  | 1502479413 
    l1d_tlb:u          | 4216516948  | 4216306182  | 4215588797 
    l1d_tlb_refill:u   | 1489148977  | 1488890316  | 1488953217 
    l2d_cache:u        | 5611213743  | 5713090079  | 5791151078 
    l2d_cache_refill:u | 2151002736  | 2211436490  | 2321217560 
    l2d_tlb:u          | 1489212561  | 1488947695  | 1488993644 
    l2d_tlb_refill:u   | 2089520     | 1927158     | 237769     
    ll_cache:u         | 2150662118  | 2210999082  | 2321010796 
    ll_cache_miss:u    | 307575501   | 312315605   | 212164817  

== combo_083_s6 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b64_ld2_xpage_p1_lp4_r1000    
    s1 | mix_b128_ld1_xpage_p512_lp4_r1000 
    s2 | mix_b64_ld7_lin_p524288_lp4_r1000 
    s3 | mix_b128_ld14_pshuf_p128_lp4_r1000
    s4 | mix_b64_ld14_pshuf_p128_lp1_r1000 
    s5 | mix_b128_ld7_pshuf_p1_lp1_r1000   
single_counts:
    metric             | s0         | s1         | s2          | s3          | s4          | s5        
    -------------------+------------+------------+-------------+-------------+-------------+-----------
    cpu-cycles:u       | 530941783  | 6237217333 | 45654134099 | 31964622041 | 25748697854 | 3602112853
    instructions:u     | 1061064023 | 2085063795 | 1061065116  | 2085065069  | 1061064018  | 2085063786
    br_retired:u       | 8004983    | 8004922    | 8005198     | 8005191     | 8004976     | 8004921   
    br_mis_pred:u      | 2397       | 2098       | 3326        | 2857        | 3282        | 2874      
    l1i_cache:u        | 138083263  | 266632616  | 137743636   | 266824481   | 138790883   | 265061487 
    l1i_cache_refill:u | 818        | 5863       | 16373       | 24242       | 9249        | 3298      
    l1i_tlb:u          | 138083263  | 266632616  | 137743636   | 266824481   | 138790883   | 265061487 
    l1i_tlb_refill:u   | 37         | 45         | 261         | 47          | 52          | 55        
    l2i_cache:u        | 819        | 5884       | 16421       | 24383       | 9264        | 3318      
    l2i_cache_refill:u | 525        | 896        | 7813        | 1698        | 1085        | 623       
    l2i_tlb:u          | 91         | 94         | 430         | 173         | 141         | 119       
    l2i_tlb_refill:u   | 11         | 24         | 258         | 16          | 21          | 17        
    l1d_cache:u        | 141053014  | 141220515  | 461514452   | 1806438995  | 909511164   | 909038082 
    l1d_cache_refill:u | 135        | 128442138  | 116562938   | 502555716   | 862662392   | 192       
    l1d_tlb:u          | 141098703  | 280731485  | 463156737   | 2571268012  | 1813819569  | 909085470 
    l1d_tlb_refill:u   | 65         | 131059271  | 356280      | 451277671   | 898365444   | 98        
    l2d_cache:u        | 1496       | 507829577  | 1512350349  | 7163776123  | 2476409846  | 4438      
    l2d_cache_refill:u | 922        | 256403376  | 819871801   | 1200064544  | 682830651   | 1032      
    l2d_tlb:u          | 193        | 131059985  | 370225      | 451412534   | 898371748   | 275       
    l2d_tlb_refill:u   | 4          | 125        | 238128      | 27          | 27          | 21        
    ll_cache:u         | 357        | 256400793  | 819668290   | 1199993834  | 682822647   | 349       
    ll_cache_miss:u    | 63         | 1140534    | 780130798   | 151117124   | 16809       | 47        
combined_orders:
    id        | modules                                                                                                                                                                                                
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld2_xpage_p1_lp4_r1000+mix_b128_ld1_xpage_p512_lp4_r1000+mix_b64_ld7_lin_p524288_lp4_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000+mix_b128_ld7_pshuf_p1_lp1_r1000
    shuffle   | mix_b64_ld7_lin_p524288_lp4_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld1_xpage_p512_lp4_r1000+mix_b128_ld7_pshuf_p1_lp1_r1000+mix_b64_ld2_xpage_p1_lp4_r1000
    sum       | mix_b64_ld2_xpage_p1_lp4_r1000+mix_b128_ld1_xpage_p512_lp4_r1000+mix_b64_ld7_lin_p524288_lp4_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000+mix_b128_ld7_pshuf_p1_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 114099500978 | 108584862351 | 113737725963
    instructions:u     | 9438080126   | 9438080001   | 9438385807  
    br_retired:u       | 48015201     | 48015184     | 48030191    
    br_mis_pred:u      | 12803        | 8598         | 16834       
    l1i_cache:u        | 1215709237   | 1214272074   | 1213136366  
    l1i_cache_refill:u | 397030       | 369987       | 59843       
    l1i_tlb:u          | 1215709237   | 1214272074   | 1213136366  
    l1i_tlb_refill:u   | 923          | 905          | 497         
    l2i_cache:u        | 397721       | 370456       | 60089       
    l2i_cache_refill:u | 86193        | 84470        | 12640       
    l2i_tlb:u          | 1577         | 1616         | 1048        
    l2i_tlb_refill:u   | 919          | 899          | 347         
    l1d_cache:u        | 4369567330   | 4369313085   | 4368776222  
    l1d_cache_refill:u | 1687563212   | 1644133065   | 1610223511  
    l1d_tlb:u          | 6112727548   | 6180445717   | 6179159976  
    l1d_tlb_refill:u   | 1479005636   | 1482857285   | 1481058829  
    l2d_cache:u        | 10131048306  | 11256838348  | 11660371829 
    l2d_cache_refill:u | 2673330247   | 3030181552   | 2959172326  
    l2d_tlb:u          | 1479151330   | 1483076966   | 1481214960  
    l2d_tlb_refill:u   | 727935       | 726477       | 238332      
    ll_cache:u         | 2672923391   | 3029761125   | 2958886270  
    ll_cache_miss:u    | 964294703    | 1070448299   | 932405375   

== combo_084_s7 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld14_lin_p1_lp1_r1000       
    s1 | mix_b64_ld2_pshuf_p128_lp1_r1000    
    s2 | mix_b64_ld4_pshuf_p128_lp4_r1000    
    s3 | mix_b64_ld14_indir_p1_lp4_r1000     
    s4 | mix_b64_ld4_pshuf_p1_lp4_r1000      
    s5 | mix_b128_ld2_indir_p524288_lp4_r1000
    s6 | mix_b64_ld14_lin_p524288_lp1_r1000  
single_counts:
    metric             | s0         | s1         | s2         | s3         | s4         | s5          | s6         
    -------------------+------------+------------+------------+------------+------------+-------------+------------
    cpu-cycles:u       | 3602124081 | 3726924759 | 4402903220 | 3602176826 | 1043125131 | 65284272389 | 37156424231
    instructions:u     | 1061063792 | 1061063795 | 1061063795 | 1061063801 | 1061064031 | 2085065119  | 1061065056 
    br_retired:u       | 8004919    | 8004922    | 8004922    | 8004920    | 8004984    | 8005199     | 8005191    
    br_mis_pred:u      | 2557       | 2560       | 2386       | 2562       | 1884       | 3626        | 3068       
    l1i_cache:u        | 138055920  | 138095490  | 137347332  | 137056959  | 138080341  | 268630475   | 138804472  
    l1i_cache_refill:u | 1798       | 1973       | 1977       | 1757       | 933        | 54969       | 13876      
    l1i_tlb:u          | 138055920  | 138095490  | 137347332  | 137056959  | 138080341  | 268630475   | 138804472  
    l1i_tlb_refill:u   | 43         | 43         | 39         | 42         | 45         | 374         | 228        
    l2i_cache:u        | 1801       | 1973       | 1979       | 1761       | 936        | 55129       | 13911      
    l2i_cache_refill:u | 552        | 591        | 610        | 550        | 523        | 5115        | 1730       
    l2i_tlb:u          | 241        | 86         | 635        | 84         | 124        | 555         | 633        
    l2i_tlb_refill:u   | 11         | 13         | 12         | 12         | 12         | 369         | 222        
    l1d_cache:u        | 909038356  | 141055081  | 269303957  | 909038118  | 269044926  | 270548057   | 910243052  
    l1d_cache_refill:u | 180        | 121725658  | 93938584   | 187        | 159        | 255246398   | 169643397  
    l1d_tlb:u          | 909085014  | 277509872  | 373103409  | 909084775  | 269083502  | 534552898   | 917048986  
    l1d_tlb_refill:u   | 104        | 130000095  | 66046996   | 95         | 71         | 250930255   | 2748995    
    l2d_cache:u        | 2220       | 382662239  | 815498633  | 2484       | 1504       | 1134843528  | 3791192712 
    l2d_cache_refill:u | 818        | 117516697  | 136616058  | 916        | 820        | 608521235   | 1555943935 
    l2d_tlb:u          | 142        | 130298628  | 66120799   | 298        | 154        | 251201396   | 2761621    
    l2d_tlb_refill:u   | 3          | 14         | 11         | 4          | 4          | 2773264     | 1672596    
    ll_cache:u         | 261        | 117515301  | 136610712  | 340        | 289        | 608313680   | 1554992574 
    ll_cache_miss:u    | 30         | 1642       | 842415     | 140        | 41         | 596620070   | 1418039454 
combined_orders:
    id        | modules                                                                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_lin_p1_lp1_r1000+mix_b64_ld2_pshuf_p128_lp1_r1000+mix_b64_ld4_pshuf_p128_lp4_r1000+mix_b64_ld14_indir_p1_lp4_r1000+mix_b64_ld4_pshuf_p1_lp4_r1000+mix_b128_ld2_indir_p524288_lp4_r1000+mix_b64_ld14_lin_p524288_lp1_r1000
    shuffle   | mix_b64_ld14_lin_p1_lp1_r1000+mix_b64_ld2_pshuf_p128_lp1_r1000+mix_b128_ld2_indir_p524288_lp4_r1000+mix_b64_ld14_indir_p1_lp4_r1000+mix_b64_ld14_lin_p524288_lp1_r1000+mix_b64_ld4_pshuf_p1_lp4_r1000+mix_b64_ld4_pshuf_p128_lp4_r1000
    sum       | mix_b64_ld14_lin_p1_lp1_r1000+mix_b64_ld2_pshuf_p128_lp1_r1000+mix_b64_ld4_pshuf_p128_lp4_r1000+mix_b64_ld14_indir_p1_lp4_r1000+mix_b64_ld4_pshuf_p1_lp4_r1000+mix_b128_ld2_indir_p524288_lp4_r1000+mix_b64_ld14_lin_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 119468470457 | 120955899095 | 118817950637
    instructions:u     | 8451083073   | 8451083100   | 8451449389  
    br_retired:u       | 56017193     | 56017197     | 56035057    
    br_mis_pred:u      | 21470        | 18317        | 18643       
    l1i_cache:u        | 1098114071   | 1098150422   | 1096070989  
    l1i_cache_refill:u | 365611       | 350828       | 77283       
    l1i_tlb:u          | 1098114071   | 1098150422   | 1096070989  
    l1i_tlb_refill:u   | 1389         | 1381         | 814         
    l2i_cache:u        | 366108       | 351251       | 77490       
    l2i_cache_refill:u | 108496       | 104722       | 9671        
    l2i_tlb:u          | 2522         | 2121         | 2358        
    l2i_tlb_refill:u   | 1378         | 1379         | 651         
    l1d_cache:u        | 3678163676   | 3678167135   | 3678271547  
    l1d_cache_refill:u | 641989771    | 639652474    | 640554563   
    l1d_tlb:u          | 4191487370   | 4191142243   | 4189468456  
    l1d_tlb_refill:u   | 449766986    | 449777539    | 449726611   
    l2d_cache:u        | 6040729987   | 6037146591   | 6124203320  
    l2d_cache_refill:u | 2402296607   | 2391194865   | 2418600479  
    l2d_tlb:u          | 450108381    | 450119842    | 450383038   
    l2d_tlb_refill:u   | 7153967      | 7381448      | 4445896     
    ll_cache:u         | 2400991881   | 2389752813   | 2417433157  
    ll_cache_miss:u    | 2027129854   | 2032795838   | 2015503792  

== combo_085_s7 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld1_lin_p524288_lp4_r1000  
    s1 | mix_b64_ld7_indir_p524288_lp4_r1000
    s2 | mix_b128_ld2_lin_p1_lp1_r1000      
    s3 | mix_b64_ld1_xpage_p128_lp1_r1000   
    s4 | mix_b64_ld7_xpage_p512_lp4_r1000   
    s5 | mix_b64_ld4_xpage_p128_lp4_r1000   
    s6 | mix_b64_ld14_lin_p512_lp4_r1000    
single_counts:
    metric             | s0         | s1           | s2         | s3         | s4          | s5         | s6         
    -------------------+------------+--------------+------------+------------+-------------+------------+------------
    cpu-cycles:u       | 6845096269 | 114370076987 | 1042117398 | 2032291381 | 19890836267 | 5589361921 | 26318494091
    instructions:u     | 1061063801 | 1061065073   | 2085064014 | 1061064029 | 1061063795  | 1061063795 | 1061065032 
    br_retired:u       | 8004920    | 8005193      | 8004982    | 8004981    | 8004922     | 8004922    | 8005188    
    br_mis_pred:u      | 2701       | 2960         | 2661       | 2061       | 3382        | 2098       | 3317       
    l1i_cache:u        | 138204403  | 143950977    | 265056333  | 137197677  | 138232397   | 138583509  | 138189289  
    l1i_cache_refill:u | 2888       | 36416        | 1730       | 1251       | 6618        | 2441       | 9027       
    l1i_tlb:u          | 138204403  | 143950977    | 265056333  | 137197677  | 138232397   | 138583509  | 138189289  
    l1i_tlb_refill:u   | 70         | 347          | 41         | 56         | 44          | 52         | 45         
    l2i_cache:u        | 2894       | 36506        | 1743       | 1252       | 6632        | 2447       | 9056       
    l2i_cache_refill:u | 878        | 7685         | 607        | 595        | 957         | 631        | 1732       
    l2i_tlb:u          | 624        | 405          | 390        | 89         | 98          | 136        | 102        
    l2i_tlb_refill:u   | 65         | 342          | 12         | 17         | 25          | 37         | 28         
    l1d_cache:u        | 77064004   | 465229380    | 269037610  | 77052510   | 461160477   | 269361160  | 910407487  
    l1d_cache_refill:u | 17804053   | 449500667    | 175        | 60023155   | 448066340   | 244117347  | 291689423  
    l1d_tlb:u          | 77284571   | 917435875    | 269065085  | 149804220  | 915432426   | 535889270  | 1166714389 
    l1d_tlb_refill:u   | 51381      | 439165430    | 90         | 66006250   | 450101577   | 258137596  | 226282959  
    l2d_cache:u        | 205536244  | 1899393970   | 2683       | 182237859  | 1794017326  | 705262972  | 3005650365 
    l2d_cache_refill:u | 112833082  | 987746804    | 923        | 45238851   | 902979055   | 127783624  | 1589747468 
    l2d_tlb:u          | 53202      | 439277360    | 127        | 66008633   | 450111103   | 258748287  | 226288795  
    l2d_tlb_refill:u   | 34249      | 4343678      | 4          | 14         | 228         | 18         | 469        
    ll_cache:u         | 112802562  | 987231560    | 268        | 45237893   | 902970564   | 127781578  | 1589547642 
    ll_cache_miss:u    | 108152471  | 969390206    | 50         | 107        | 3359816     | 373095     | 30359617   
combined_orders:
    id        | modules                                                                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld1_lin_p524288_lp4_r1000+mix_b64_ld7_indir_p524288_lp4_r1000+mix_b128_ld2_lin_p1_lp1_r1000+mix_b64_ld1_xpage_p128_lp1_r1000+mix_b64_ld7_xpage_p512_lp4_r1000+mix_b64_ld4_xpage_p128_lp4_r1000+mix_b64_ld14_lin_p512_lp4_r1000
    shuffle   | mix_b64_ld1_xpage_p128_lp1_r1000+mix_b64_ld4_xpage_p128_lp4_r1000+mix_b64_ld1_lin_p524288_lp4_r1000+mix_b128_ld2_lin_p1_lp1_r1000+mix_b64_ld14_lin_p512_lp4_r1000+mix_b64_ld7_xpage_p512_lp4_r1000+mix_b64_ld7_indir_p524288_lp4_r1000
    sum       | mix_b64_ld1_lin_p524288_lp4_r1000+mix_b64_ld7_indir_p524288_lp4_r1000+mix_b128_ld2_lin_p1_lp1_r1000+mix_b64_ld1_xpage_p128_lp1_r1000+mix_b64_ld7_xpage_p512_lp4_r1000+mix_b64_ld4_xpage_p128_lp4_r1000+mix_b64_ld14_lin_p512_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 179899250897 | 180975593642 | 176088274314
    instructions:u     | 8451083160   | 8451083143   | 8451449539  
    br_retired:u       | 56017212     | 56017211     | 56035108    
    br_mis_pred:u      | 22980        | 22100        | 19180       
    l1i_cache:u        | 1101644455   | 1098090909   | 1099414585  
    l1i_cache_refill:u | 447672       | 435413       | 60371       
    l1i_tlb:u          | 1101644455   | 1098090909   | 1099414585  
    l1i_tlb_refill:u   | 1720         | 1726         | 655         
    l2i_cache:u        | 448676       | 436122       | 60530       
    l2i_cache_refill:u | 116073       | 73572        | 13085       
    l2i_tlb:u          | 2680         | 2425         | 1844        
    l2i_tlb_refill:u   | 1711         | 1722         | 526         
    l1d_cache:u        | 2529170200   | 2526623048   | 2529312628  
    l1d_cache_refill:u | 1468992045   | 1471998887   | 1511201160  
    l1d_tlb:u          | 4035888723   | 4025389075   | 4031625836  
    l1d_tlb_refill:u   | 1439727664   | 1437878868   | 1439745283  
    l2d_cache:u        | 7616587047   | 7528432814   | 7792101419  
    l2d_cache_refill:u | 3792787765   | 3749775279   | 3766329807  
    l2d_tlb:u          | 1440180976   | 1438205666   | 1440487507  
    l2d_tlb_refill:u   | 10240000     | 7733788      | 4378660     
    ll_cache:u         | 3791723987   | 3748766297   | 3765572067  
    ll_cache_miss:u    | 1460347980   | 1483686291   | 1111635362  

== combo_086_s7 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld7_xpage_p128_lp4_r1000   
    s1 | mix_b64_ld1_indir_p128_lp1_r1000    
    s2 | mix_b64_ld14_pshuf_p128_lp1_r1000   
    s3 | mix_b128_ld1_lin_p1_lp1_r1000       
    s4 | mix_b128_ld4_xpage_p524288_lp4_r1000
    s5 | mix_b128_ld4_xpage_p1_lp4_r1000     
    s6 | mix_b64_ld1_pshuf_p524288_lp1_r1000 
single_counts:
    metric             | s0          | s1         | s2          | s3         | s4           | s5         | s6        
    -------------------+-------------+------------+-------------+------------+--------------+------------+-----------
    cpu-cycles:u       | 20628666183 | 1800063189 | 24818441466 | 530115994  | 129149079746 | 2066916626 | 2672454292
    instructions:u     | 2085063808  | 1061064023 | 1061064018  | 2085064014 | 2085065049   | 2085064023 | 1061063795
    br_retired:u       | 8004922     | 8004983    | 8004976     | 8004982    | 8005190      | 8004983    | 8004922   
    br_mis_pred:u      | 2498        | 2427       | 3766        | 2349       | 2869         | 2449       | 2001      
    l1i_cache:u        | 267523992   | 138084636  | 137125650   | 265042902  | 270815666    | 266061833  | 137300060 
    l1i_cache_refill:u | 16158       | 1237       | 8218        | 1118       | 98795        | 2254       | 1700      
    l1i_tlb:u          | 267523992   | 138084636  | 137125650   | 265042902  | 270815666    | 266061833  | 137300060 
    l1i_tlb_refill:u   | 47          | 47         | 54          | 53         | 466          | 48         | 45        
    l2i_cache:u        | 16198       | 1240       | 8233        | 1118       | 99421        | 2256       | 1702      
    l2i_cache_refill:u | 1356        | 587        | 872         | 627        | 6092         | 653        | 639       
    l2i_tlb:u          | 88          | 219        | 300         | 88         | 537          | 95         | 368       
    l2i_tlb_refill:u   | 16          | 12         | 47          | 17         | 461          | 13         | 40        
    l1d_cache:u        | 909887949   | 77054201   | 910059666   | 141035014  | 527016903    | 525038753  | 77105862  
    l1d_cache_refill:u | 874945786   | 61742375   | 868101732   | 179        | 513152915    | 160        | 12368002  
    l1d_tlb:u          | 1814214741  | 149174147  | 1814997033  | 141051156  | 1043800576   | 525084065  | 77750402  
    l1d_tlb_refill:u   | 898568084   | 66001245   | 898788503   | 76         | 499468873    | 78         | 198212    
    l2d_cache:u        | 2278651226  | 184449829  | 2472066350  | 1797       | 2040289340   | 3013       | 274554932 
    l2d_cache_refill:u | 480789594   | 56376091   | 679031666   | 862        | 1036314173   | 1012       | 113551188 
    l2d_tlb:u          | 898645171   | 66001662   | 898814675   | 102        | 499792480    | 98         | 198248    
    l2d_tlb_refill:u   | 18          | 46         | 13          | 5          | 5457890      | 4          | 118283    
    ll_cache:u         | 480784212   | 56374309   | 679029039   | 241        | 1036314238   | 376        | 113484757 
    ll_cache_miss:u    | 32928       | 278        | 10501       | 33         | 1031571451   | 51         | 104144807 
combined_orders:
    id        | modules                                                                                                                                                                                                                                    
    ----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld7_xpage_p128_lp4_r1000+mix_b64_ld1_indir_p128_lp1_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b128_ld4_xpage_p524288_lp4_r1000+mix_b128_ld4_xpage_p1_lp4_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000
    shuffle   | mix_b128_ld4_xpage_p524288_lp4_r1000+mix_b64_ld1_indir_p128_lp1_r1000+mix_b128_ld7_xpage_p128_lp4_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000+mix_b128_ld4_xpage_p1_lp4_r1000
    sum       | mix_b128_ld7_xpage_p128_lp4_r1000+mix_b64_ld1_indir_p128_lp1_r1000+mix_b64_ld14_pshuf_p128_lp1_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b128_ld4_xpage_p524288_lp4_r1000+mix_b128_ld4_xpage_p1_lp4_r1000+mix_b64_ld1_pshuf_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 187806022543 | 183553815203 | 181665737496
    instructions:u     | 11523083187  | 11523083117  | 11523448730 
    br_retired:u       | 56017216     | 56017207     | 56034958    
    br_mis_pred:u      | 17170        | 16413        | 18359       
    l1i_cache:u        | 1484156980   | 1485694740   | 1481954739  
    l1i_cache_refill:u | 723240       | 682815       | 129480      
    l1i_tlb:u          | 1484156980   | 1485694740   | 1481954739  
    l1i_tlb_refill:u   | 2129         | 2096         | 760         
    l2i_cache:u        | 723935       | 683210       | 130168      
    l2i_cache_refill:u | 61416        | 61771        | 10826       
    l2i_tlb:u          | 2910         | 2878         | 1695        
    l2i_tlb_refill:u   | 2123         | 2091         | 606         
    l1d_cache:u        | 3166485975   | 3165489797   | 3167198348  
    l1d_cache_refill:u | 2327939720   | 2342265945   | 2330311149  
    l1d_tlb:u          | 5566582938   | 5575341761   | 5566072120  
    l1d_tlb_refill:u   | 2362509097   | 2365899584   | 2363025071  
    l2d_cache:u        | 7671401579   | 7446193246   | 7250016487  
    l2d_cache_refill:u | 2795180876   | 2556985857   | 2366064586  
    l2d_tlb:u          | 2362929807   | 2366391243   | 2363452436  
    l2d_tlb_refill:u   | 6438346      | 7007628      | 5576259     
    ll_cache:u         | 2794872846   | 2556483928   | 2365987172  
    ll_cache_miss:u    | 1157200611   | 1151575573   | 1135760049  

== combo_087_s7 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b64_ld14_xpage_p128_lp4_r1000 
    s1 | mix_b64_ld2_lin_p524288_lp1_r1000 
    s2 | mix_b64_ld2_lin_p512_lp4_r1000    
    s3 | mix_b64_ld14_xpage_p1_lp4_r1000   
    s4 | mix_b128_ld4_lin_p524288_lp4_r1000
    s5 | mix_b64_ld14_pshuf_p128_lp4_r1000 
    s6 | mix_b64_ld14_pshuf_p512_lp1_r1000 
single_counts:
    metric             | s0          | s1         | s2         | s3         | s4          | s5          | s6         
    -------------------+-------------+------------+------------+------------+-------------+-------------+------------
    cpu-cycles:u       | 18718946651 | 5440109159 | 4787931407 | 3602155802 | 53339781514 | 16875520026 | 39560945432
    instructions:u     | 1061063795  | 1061063801 | 1061063795 | 1061063808 | 2085065073  | 1061063795  | 1061065080 
    br_retired:u       | 8004922     | 8004920    | 8004922    | 8004922    | 8005193     | 8004922     | 8005194    
    br_mis_pred:u      | 3136        | 2298       | 2288       | 2589       | 3140        | 2787        | 3232       
    l1i_cache:u        | 138861366   | 138520187  | 137404502  | 137056682  | 266683665   | 138926790   | 138983661  
    l1i_cache_refill:u | 6755        | 2475       | 2126       | 1860       | 55018       | 5855        | 13397      
    l1i_tlb:u          | 138861366   | 138520187  | 137404502  | 137056682  | 266683665   | 138926790   | 138983661  
    l1i_tlb_refill:u   | 47          | 57         | 53         | 46         | 342         | 46          | 53         
    l2i_cache:u        | 6771        | 2477       | 2132       | 1866       | 55098       | 5870        | 13419      
    l2i_cache_refill:u | 956         | 634        | 1147       | 563        | 8539        | 2648        | 1416       
    l2i_tlb:u          | 98          | 638        | 160        | 169        | 427         | 516         | 225        
    l2i_tlb_refill:u   | 15          | 52         | 46         | 16         | 337         | 13          | 32         
    l1d_cache:u        | 909563000   | 141189613  | 141209040  | 909038008  | 525204277   | 909904917   | 910990169  
    l1d_cache_refill:u | 854408175   | 24316681   | 37079861   | 203        | 128789017   | 309693772   | 896689917  
    l1d_tlb:u          | 1815912778  | 142323679  | 184002935  | 909084166  | 526330511   | 1271036560  | 1817877655 
    l1d_tlb_refill:u   | 898375537   | 394296     | 34023807   | 94         | 407284      | 226173544   | 899573216  
    l2d_cache:u        | 2327270050  | 562175187  | 382663573  | 2459       | 1753199158  | 2974622743  | 3556355354 
    l2d_cache_refill:u | 451859500   | 230723064  | 195671983  | 827        | 959805150   | 466429306   | 1799562605 
    l2d_tlb:u          | 898444240   | 395103     | 34025509   | 122        | 422460      | 226291011   | 899734604  
    l2d_tlb_refill:u   | 160         | 237181     | 465        | 3          | 270913      | 17          | 354        
    ll_cache:u         | 451853803   | 230578423  | 195651729  | 300        | 959773607   | 466403560   | 1799542791 
    ll_cache_miss:u    | 1581827     | 210380748  | 1213823    | 68         | 912478867   | 7979        | 3406761    
combined_orders:
    id        | modules                                                                                                                                                                                                                                  
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_xpage_p128_lp4_r1000+mix_b64_ld2_lin_p524288_lp1_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld14_xpage_p1_lp4_r1000+mix_b128_ld4_lin_p524288_lp4_r1000+mix_b64_ld14_pshuf_p128_lp4_r1000+mix_b64_ld14_pshuf_p512_lp1_r1000
    shuffle   | mix_b64_ld14_pshuf_p128_lp4_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld14_xpage_p1_lp4_r1000+mix_b64_ld14_pshuf_p512_lp1_r1000+mix_b128_ld4_lin_p524288_lp4_r1000+mix_b64_ld14_xpage_p128_lp4_r1000+mix_b64_ld2_lin_p524288_lp1_r1000
    sum       | mix_b64_ld14_xpage_p128_lp4_r1000+mix_b64_ld2_lin_p524288_lp1_r1000+mix_b64_ld2_lin_p512_lp4_r1000+mix_b64_ld14_xpage_p1_lp4_r1000+mix_b128_ld4_lin_p524288_lp4_r1000+mix_b64_ld14_pshuf_p128_lp4_r1000+mix_b64_ld14_pshuf_p512_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 143611187718 | 121844744740 | 142325389991
    instructions:u     | 8451083040   | 8451083091   | 8451449147  
    br_retired:u       | 56017189     | 56017196     | 56034995    
    br_mis_pred:u      | 21310        | 18372        | 19470       
    l1i_cache:u        | 1098187610   | 1096866350   | 1096436853  
    l1i_cache_refill:u | 450784       | 394490       | 87486       
    l1i_tlb:u          | 1098187610   | 1096866350   | 1096436853  
    l1i_tlb_refill:u   | 1564         | 1475         | 644         
    l2i_cache:u        | 451033       | 394678       | 87633       
    l2i_cache_refill:u | 88535        | 71076        | 15903       
    l2i_tlb:u          | 2693         | 2263         | 2233        
    l2i_tlb_refill:u   | 1559         | 1471         | 511         
    l1d_cache:u        | 4446511704   | 4446032180   | 4447099024  
    l1d_cache_refill:u | 2027080423   | 2414361580   | 2250977626  
    l1d_tlb:u          | 6168003655   | 6247953252   | 6666568284  
    l1d_tlb_refill:u   | 1622502437   | 1771289336   | 2058947778  
    l2d_cache:u        | 11375953169  | 10266673253  | 11556288524 
    l2d_cache_refill:u | 4167344398   | 3793363419   | 4104052435  
    l2d_tlb:u          | 1622754185   | 1771455228   | 2059313049  
    l2d_tlb_refill:u   | 1709539      | 1764161      | 509093      
    ll_cache:u         | 4166589949   | 3792746486   | 4103804213  
    ll_cache_miss:u    | 1374481674   | 1226495686   | 1129070073  

== combo_088_s7 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b64_ld1_xpage_p128_lp1_r1000  
    s1 | mix_b64_ld2_indir_p128_lp4_r1000  
    s2 | mix_b64_ld7_indir_p512_lp4_r1000  
    s3 | mix_b128_ld7_xpage_p128_lp1_r1000 
    s4 | mix_b64_ld14_lin_p524288_lp1_r1000
    s5 | mix_b64_ld14_lin_p512_lp1_r1000   
    s6 | mix_b64_ld14_lin_p128_lp4_r1000   
single_counts:
    metric             | s0         | s1         | s2          | s3          | s4          | s5          | s6         
    -------------------+------------+------------+-------------+-------------+-------------+-------------+------------
    cpu-cycles:u       | 2107156247 | 2922694303 | 20655184540 | 22484585653 | 37152891031 | 38282501876 | 14543804140
    instructions:u     | 1061064029 | 1061063801 | 1061063801  | 2085064018  | 1061065056  | 1061065075  | 1061063795 
    br_retired:u       | 8004981    | 8004920    | 8004920     | 8004976     | 8005191     | 8005193     | 8004922    
    br_mis_pred:u      | 2067       | 2485       | 2936        | 3187        | 3185        | 3161        | 3071       
    l1i_cache:u        | 138143659  | 138097730  | 137860720   | 265407403   | 139703574   | 140079597   | 137712385  
    l1i_cache_refill:u | 1393       | 1472       | 6936        | 17116       | 13049       | 12636       | 5094       
    l1i_tlb:u          | 138143659  | 138097730  | 137860720   | 265407403   | 139703574   | 140079597   | 137712385  
    l1i_tlb_refill:u   | 40         | 42         | 48          | 58          | 235         | 46          | 46         
    l2i_cache:u        | 1398       | 1472       | 6945        | 17162       | 13066       | 12661       | 5100       
    l2i_cache_refill:u | 582        | 558        | 1080        | 1117        | 1542        | 1222        | 758        
    l2i_tlb:u          | 169        | 318        | 213         | 249         | 699         | 102         | 80         
    l2i_tlb_refill:u   | 13         | 15         | 27          | 29          | 229         | 26          | 13         
    l1d_cache:u        | 77110198   | 141071889  | 461687739   | 909688460   | 910236370   | 911148978   | 909833917  
    l1d_cache_refill:u | 62412082   | 118471298  | 445924656   | 855866949   | 169611541   | 897445855   | 176737193  
    l1d_tlb:u          | 149247876  | 253485103  | 894942035   | 1813775294  | 917016934   | 1818795621  | 1254818799 
    l1d_tlb_refill:u   | 66022240   | 105265850  | 428290582   | 898473573   | 2748880     | 899705043   | 226157980  
    l2d_cache:u        | 198443650  | 339884327  | 1729691836  | 2480878662  | 3792005569  | 3543973698  | 2987001363 
    l2d_cache_refill:u | 70326043   | 73694371   | 827537510   | 687140611   | 1556513185  | 1796218475  | 594815480  
    l2d_tlb:u          | 66024392   | 105443473  | 428333739   | 898525001   | 2761513     | 899842357   | 226276949  
    l2d_tlb_refill:u   | 16         | 19         | 668         | 166         | 1673373     | 502         | 37         
    ll_cache:u         | 70324877   | 73692569   | 827500982   | 687134783   | 1555587673  | 1796201031  | 594777000  
    ll_cache_miss:u    | 538        | 14359      | 10834023    | 41726       | 1418646725  | 101948      | 5943987    
combined_orders:
    id        | modules                                                                                                                                                                                                                                
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld1_xpage_p128_lp1_r1000+mix_b64_ld2_indir_p128_lp4_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b128_ld7_xpage_p128_lp1_r1000+mix_b64_ld14_lin_p524288_lp1_r1000+mix_b64_ld14_lin_p512_lp1_r1000+mix_b64_ld14_lin_p128_lp4_r1000
    shuffle   | mix_b64_ld14_lin_p512_lp1_r1000+mix_b128_ld7_xpage_p128_lp1_r1000+mix_b64_ld1_xpage_p128_lp1_r1000+mix_b64_ld14_lin_p524288_lp1_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b64_ld14_lin_p128_lp4_r1000+mix_b64_ld2_indir_p128_lp4_r1000
    sum       | mix_b64_ld1_xpage_p128_lp1_r1000+mix_b64_ld2_indir_p128_lp4_r1000+mix_b64_ld7_indir_p512_lp4_r1000+mix_b128_ld7_xpage_p128_lp1_r1000+mix_b64_ld14_lin_p524288_lp1_r1000+mix_b64_ld14_lin_p512_lp1_r1000+mix_b64_ld14_lin_p128_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 153394944803 | 158757622420 | 138148817790
    instructions:u     | 8451083037   | 8451082997   | 8451449575  
    br_retired:u       | 56017188     | 56017183     | 56035103    
    br_mis_pred:u      | 23983        | 21429        | 20092       
    l1i_cache:u        | 1099286016   | 1100433967   | 1097005068  
    l1i_cache_refill:u | 423441       | 427627       | 57696       
    l1i_tlb:u          | 1099286016   | 1100433967   | 1097005068  
    l1i_tlb_refill:u   | 1025         | 1036         | 515         
    l2i_cache:u        | 423713       | 427866       | 57804       
    l2i_cache_refill:u | 57094        | 45902        | 6859        
    l2i_tlb:u          | 2258         | 1938         | 1830        
    l2i_tlb_refill:u   | 1019         | 1034         | 352         
    l1d_cache:u        | 4320834179   | 4321854101   | 4320777551  
    l1d_cache_refill:u | 2785142054   | 2772760599   | 2726469574  
    l1d_tlb:u          | 7044320844   | 7046102828   | 7102081662  
    l1d_tlb_refill:u   | 2626748261   | 2627393080   | 2626664148  
    l2d_cache:u        | 15011370264  | 14729911956  | 15071879105 
    l2d_cache_refill:u | 5839425320   | 5497579817   | 5606245675  
    l2d_tlb:u          | 2627398365   | 2627967005   | 2627207424  
    l2d_tlb_refill:u   | 4013769      | 4025272      | 1674781     
    ll_cache:u         | 5838207901   | 5496387735   | 5605218915  
    ll_cache_miss:u    | 1479786831   | 1537031023   | 1435583306  

== combo_089_s7 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b64_ld2_pshuf_p1_lp4_r1000      
    s1 | mix_b64_ld4_pshuf_p1_lp1_r1000      
    s2 | mix_b64_ld2_xpage_p512_lp1_r1000    
    s3 | mix_b64_ld2_xpage_p128_lp4_r1000    
    s4 | mix_b128_ld2_indir_p524288_lp1_r1000
    s5 | mix_b128_ld4_pshuf_p524288_lp1_r1000
    s6 | mix_b64_ld1_indir_p128_lp4_r1000    
single_counts:
    metric             | s0         | s1         | s2         | s3         | s4          | s5          | s6        
    -------------------+------------+------------+------------+------------+-------------+-------------+-----------
    cpu-cycles:u       | 530951228  | 1042983987 | 5866994159 | 3102427045 | 64716319507 | 21903952702 | 1287981590
    instructions:u     | 1061064029 | 1061064020 | 1061063795 | 1061063801 | 2085065089  | 2085064012  | 1061064023
    br_retired:u       | 8004981    | 8004980    | 8004922    | 8004920    | 8005194     | 8004978     | 8004983   
    br_mis_pred:u      | 2333       | 2341       | 2731       | 2453       | 3591        | 3099        | 1979      
    l1i_cache:u        | 138083778  | 138065913  | 137098330  | 137123548  | 267119786   | 267440450   | 137166945 
    l1i_cache_refill:u | 758        | 987        | 2459       | 1661       | 53035       | 25747       | 1061      
    l1i_tlb:u          | 138083778  | 138065913  | 137098330  | 137123548  | 267119786   | 267440450   | 137166945 
    l1i_tlb_refill:u   | 34         | 52         | 51         | 46         | 394         | 210         | 45        
    l2i_cache:u        | 758        | 991        | 2460       | 1666       | 53229       | 25819       | 1061      
    l2i_cache_refill:u | 512        | 571        | 690        | 579        | 5444        | 1501        | 602       
    l2i_tlb:u          | 73         | 184        | 120        | 87         | 459         | 478         | 734       
    l2i_tlb_refill:u   | 12         | 22         | 41         | 14         | 390         | 206         | 14        
    l1d_cache:u        | 141052749  | 269039147  | 141062788  | 141065331  | 269601150   | 525740534   | 77083166  
    l1d_cache_refill:u | 148        | 159        | 127333029  | 117424054  | 255417403   | 96425322    | 58297756  
    l1d_tlb:u          | 141102926  | 269086515  | 277307770  | 278247439  | 531985071   | 529831839   | 136625761 
    l1d_tlb_refill:u   | 70         | 74         | 130015329  | 130000093  | 250466485   | 1574249     | 53517837  
    l2d_cache:u        | 1382       | 1576       | 515054166  | 401356609  | 1052397284  | 2253132107  | 164400912 
    l2d_cache_refill:u | 833        | 827        | 255277158  | 84631496   | 548971066   | 932762908   | 30868957  
    l2d_tlb:u          | 92         | 125        | 130023236  | 130330616  | 250596460   | 1583042     | 53521793  
    l2d_tlb_refill:u   | 3          | 6          | 377        | 26         | 2272946     | 959732      | 13        
    ll_cache:u         | 287        | 258        | 255274547  | 84630001   | 548861196   | 932219115   | 30868203  
    ll_cache_miss:u    | 49         | 58         | 5119       | 259548     | 541531585   | 850740013   | 433       
combined_orders:
    id        | modules                                                                                                                                                                                                                                   
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld2_pshuf_p1_lp4_r1000+mix_b64_ld4_pshuf_p1_lp1_r1000+mix_b64_ld2_xpage_p512_lp1_r1000+mix_b64_ld2_xpage_p128_lp4_r1000+mix_b128_ld2_indir_p524288_lp1_r1000+mix_b128_ld4_pshuf_p524288_lp1_r1000+mix_b64_ld1_indir_p128_lp4_r1000
    shuffle   | mix_b64_ld4_pshuf_p1_lp1_r1000+mix_b64_ld2_xpage_p128_lp4_r1000+mix_b128_ld4_pshuf_p524288_lp1_r1000+mix_b64_ld2_xpage_p512_lp1_r1000+mix_b64_ld2_pshuf_p1_lp4_r1000+mix_b64_ld1_indir_p128_lp4_r1000+mix_b128_ld2_indir_p524288_lp1_r1000
    sum       | mix_b64_ld2_pshuf_p1_lp4_r1000+mix_b64_ld4_pshuf_p1_lp1_r1000+mix_b64_ld2_xpage_p512_lp1_r1000+mix_b64_ld2_xpage_p128_lp4_r1000+mix_b128_ld2_indir_p524288_lp1_r1000+mix_b128_ld4_pshuf_p524288_lp1_r1000+mix_b64_ld1_indir_p128_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum        
    -------------------+--------------+--------------+------------
    cpu-cycles:u       | 100299681081 | 100649180013 | 98451610218
    instructions:u     | 9475083049   | 9475083076   | 9475448769 
    br_retired:u       | 56017190     | 56017194     | 56034958   
    br_mis_pred:u      | 18746        | 21627        | 18527      
    l1i_cache:u        | 1224250837   | 1224476799   | 1222098750 
    l1i_cache_refill:u | 396832       | 385501       | 85708      
    l1i_tlb:u          | 1224250837   | 1224476799   | 1222098750 
    l1i_tlb_refill:u   | 1407         | 1516         | 832        
    l2i_cache:u        | 397251       | 385889       | 85984      
    l2i_cache_refill:u | 68955        | 77658        | 9899       
    l2i_tlb:u          | 2569         | 2015         | 2135       
    l2i_tlb_refill:u   | 1394         | 1511         | 699        
    l1d_cache:u        | 1564392197   | 1564557537   | 1564644865 
    l1d_cache_refill:u | 651802742    | 652349475    | 654897871  
    l1d_tlb:u          | 2166545179   | 2166978333   | 2164187321 
    l1d_tlb_refill:u   | 565530394    | 565578966    | 565574137  
    l2d_cache:u        | 4455989403   | 4443496524   | 4386344036 
    l2d_cache_refill:u | 1913804034   | 1911952660   | 1852513245 
    l2d_tlb:u          | 565809359    | 565873195    | 566055364  
    l2d_tlb_refill:u   | 6676880      | 6664730      | 3233103    
    ll_cache:u         | 1912814718   | 1910863992   | 1851853607 
    ll_cache_miss:u    | 1424422770   | 1426220942   | 1392536805 

== combo_090_s7 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld1_indir_p524288_lp1_r1000
    s1 | mix_b128_ld2_lin_p524288_lp4_r1000 
    s2 | mix_b128_ld14_pshuf_p128_lp4_r1000 
    s3 | mix_b64_ld1_indir_p512_lp1_r1000   
    s4 | mix_b128_ld2_lin_p524288_lp1_r1000 
    s5 | mix_b64_ld7_xpage_p128_lp4_r1000   
    s6 | mix_b128_ld2_indir_p128_lp4_r1000  
single_counts:
    metric             | s0          | s1          | s2          | s3         | s4          | s5         | s6        
    -------------------+-------------+-------------+-------------+------------+-------------+------------+-----------
    cpu-cycles:u       | 16300310658 | 26440800596 | 34477510760 | 2902263138 | 11025222879 | 9043597676 | 4994597543
    instructions:u     | 1061063795  | 2085065036  | 2085065002  | 1061063808 | 2085063795  | 1061063808 | 2085063801
    br_retired:u       | 8004922     | 8005189     | 8005183     | 8004922    | 8004922     | 8004922    | 8004920   
    br_mis_pred:u      | 3305        | 3096        | 2862        | 2476       | 2759        | 2829       | 2635      
    l1i_cache:u        | 138167440   | 266490519   | 266285528   | 137088448  | 266890015   | 138624865  | 265142876 
    l1i_cache_refill:u | 6167        | 27618       | 24357       | 1792       | 14438       | 3606       | 4028      
    l1i_tlb:u          | 138167440   | 266490519   | 266285528   | 137088448  | 266890015   | 138624865  | 265142876 
    l1i_tlb_refill:u   | 147         | 242         | 46          | 44         | 135         | 43         | 40        
    l2i_cache:u        | 6175        | 27741       | 24427       | 1794       | 14463       | 3616       | 4046      
    l2i_cache_refill:u | 1679        | 5241        | 5344        | 646        | 938         | 602        | 743       
    l2i_tlb:u          | 484         | 541         | 136         | 91         | 599         | 226        | 416       
    l2i_tlb_refill:u   | 140         | 237         | 12          | 17         | 130         | 10         | 14        
    l1d_cache:u        | 77041051    | 269150992   | 1805132208  | 77129253   | 269327120   | 461653042  | 269116368 
    l1d_cache_refill:u | 63184795    | 65961250    | 518776809   | 64023339   | 48402692    | 435606524  | 232946481 
    l1d_tlb:u          | 148776517   | 269769911   | 2544372750  | 152289284  | 271543172   | 917457131  | 483366425 
    l1d_tlb_refill:u   | 64073169    | 206149      | 450000154   | 67028521   | 788582      | 450460730  | 208033904 
    l2d_cache:u        | 288393247   | 841541710   | 7564351461  | 252758119  | 1147934866  | 1151377951 | 655146257 
    l2d_cache_refill:u | 156863792   | 459253590   | 1414709744  | 128040041  | 473779460   | 215508929  | 127066927 
    l2d_tlb:u          | 64082061    | 216167      | 450094955   | 67028804   | 792992      | 450513458  | 208281388 
    l2d_tlb_refill:u   | 708064      | 140535      | 17          | 172        | 480693      | 26         | 15        
    ll_cache:u         | 156749788   | 459129052   | 1414602707  | 128036914  | 473498636   | 215506409  | 127065003 
    ll_cache_miss:u    | 149928213   | 437968505   | 133471515   | 2054       | 431389579   | 4775       | 455       
combined_orders:
    id        | modules                                                                                                                                                                                                                                         
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld1_indir_p524288_lp1_r1000+mix_b128_ld2_lin_p524288_lp4_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b128_ld2_lin_p524288_lp1_r1000+mix_b64_ld7_xpage_p128_lp4_r1000+mix_b128_ld2_indir_p128_lp4_r1000
    shuffle   | mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b128_ld2_lin_p524288_lp4_r1000+mix_b128_ld2_lin_p524288_lp1_r1000+mix_b128_ld2_indir_p128_lp4_r1000+mix_b64_ld1_indir_p524288_lp1_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b64_ld7_xpage_p128_lp4_r1000
    sum       | mix_b64_ld1_indir_p524288_lp1_r1000+mix_b128_ld2_lin_p524288_lp4_r1000+mix_b128_ld14_pshuf_p128_lp4_r1000+mix_b64_ld1_indir_p512_lp1_r1000+mix_b128_ld2_lin_p524288_lp1_r1000+mix_b64_ld7_xpage_p128_lp4_r1000+mix_b128_ld2_indir_p128_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 103487572578 | 106720799322 | 105184303250
    instructions:u     | 11523083107  | 11523083069  | 11523449045 
    br_retired:u       | 56017197     | 56017194     | 56034980    
    br_mis_pred:u      | 20658        | 23860        | 19962       
    l1i_cache:u        | 1481768628   | 1481674747   | 1478689691  
    l1i_cache_refill:u | 599272       | 600474       | 82006       
    l1i_tlb:u          | 1481768628   | 1481674747   | 1478689691  
    l1i_tlb_refill:u   | 2175         | 2174         | 697         
    l2i_cache:u        | 599431       | 601073       | 82262       
    l2i_cache_refill:u | 162013       | 149131       | 15193       
    l2i_tlb:u          | 3017         | 3221         | 2493        
    l2i_tlb_refill:u   | 2170         | 2170         | 560         
    l1d_cache:u        | 3229824396   | 3229989878   | 3228550034  
    l1d_cache_refill:u | 1500326871   | 1495881293   | 1428901890  
    l1d_tlb:u          | 4763660955   | 4748700210   | 4787575190  
    l1d_tlb_refill:u   | 1244847020   | 1239825509   | 1240591209  
    l2d_cache:u        | 10333299310  | 10661914308  | 11901503611 
    l2d_cache_refill:u | 2668936537   | 2695478153   | 2975222483  
    l2d_tlb:u          | 1245051368   | 1240328468   | 1241009825  
    l2d_tlb_refill:u   | 4551283      | 4602702      | 1329522     
    ll_cache:u         | 2668172503   | 2694627920   | 2974588509  
    ll_cache_miss:u    | 1279581327   | 1327339395   | 1152765096  

== combo_091_s7 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b64_ld7_lin_p128_lp4_r1000       
    s1 | mix_b128_ld4_pshuf_p512_lp4_r1000    
    s2 | mix_b64_ld1_xpage_p512_lp1_r1000     
    s3 | mix_b64_ld4_indir_p128_lp1_r1000     
    s4 | mix_b128_ld7_lin_p524288_lp1_r1000   
    s5 | mix_b128_ld14_pshuf_p524288_lp4_r1000
    s6 | mix_b64_ld4_pshuf_p1_lp4_r1000       
single_counts:
    metric             | s0         | s1          | s2         | s3         | s4          | s5           | s6        
    -------------------+------------+-------------+------------+------------+-------------+--------------+-----------
    cpu-cycles:u       | 6645700827 | 19005509163 | 2818957691 | 6284116252 | 37131715208 | 151312758509 | 1043146184
    instructions:u     | 1061063795 | 2085063795  | 1061063801 | 1061063808 | 2085065053  | 2085065143   | 1061064023
    br_retired:u       | 8004922    | 8004922     | 8004920    | 8004922    | 8005190     | 8005202      | 8004983   
    br_mis_pred:u      | 2109       | 2956        | 2455       | 2115       | 3087        | 3532         | 1935      
    l1i_cache:u        | 138787865  | 266934936   | 137090033  | 137607775  | 268122205   | 270434779    | 137080650 
    l1i_cache_refill:u | 2792       | 15369       | 1662       | 2461       | 34567       | 123864       | 1084      
    l1i_tlb:u          | 138787865  | 266934936   | 137090033  | 137607775  | 268122205   | 270434779    | 137080650 
    l1i_tlb_refill:u   | 37         | 44          | 44         | 38         | 285         | 460          | 45        
    l2i_cache:u        | 2793       | 15487       | 1667       | 2463       | 34759       | 124562       | 1086      
    l2i_cache_refill:u | 904        | 3470        | 625        | 579        | 1904        | 25090        | 570       
    l2i_tlb:u          | 122        | 132         | 121        | 184        | 561         | 630          | 84        
    l2i_tlb_refill:u   | 13         | 22          | 20         | 11         | 279         | 450          | 14        
    l1d_cache:u        | 461520334  | 525720348   | 77051831   | 269355373  | 909959009   | 1811355734   | 269045070 
    l1d_cache_refill:u | 98433485   | 223024288   | 63999388   | 240968907  | 171512836   | 582758500    | 154       
    l1d_tlb:u          | 627339960  | 721430148   | 148616490  | 536971919  | 917281206   | 1819241906   | 269083793 
    l1d_tlb_refill:u   | 114000083  | 130127379   | 66006001   | 259155445  | 2749089     | 1389387      | 95        
    l2d_cache:u        | 1437988303 | 1862839731  | 252796015  | 642736771  | 3786210782  | 8252383563   | 1876      
    l2d_cache_refill:u | 223176561  | 803970940   | 128068852  | 116664022  | 1553050603  | 4265096062   | 1008      
    l2d_tlb:u          | 114072066  | 130199530   | 66006281   | 259338345  | 2761740     | 1412205      | 147       
    l2d_tlb_refill:u   | 12         | 277         | 126        | 18         | 1670547     | 881081       | 21        
    ll_cache:u         | 223160631  | 803902638   | 128066793  | 116663070  | 1552135264  | 4264203180   | 397       
    ll_cache_miss:u    | 936713     | 5551559     | 1125       | 1129       | 1415793334  | 3851330291   | 27        
combined_orders:
    id        | modules                                                                                                                                                                                                                                   
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_lin_p128_lp4_r1000+mix_b128_ld4_pshuf_p512_lp4_r1000+mix_b64_ld1_xpage_p512_lp1_r1000+mix_b64_ld4_indir_p128_lp1_r1000+mix_b128_ld7_lin_p524288_lp1_r1000+mix_b128_ld14_pshuf_p524288_lp4_r1000+mix_b64_ld4_pshuf_p1_lp4_r1000
    shuffle   | mix_b128_ld14_pshuf_p524288_lp4_r1000+mix_b128_ld7_lin_p524288_lp1_r1000+mix_b64_ld1_xpage_p512_lp1_r1000+mix_b64_ld7_lin_p128_lp4_r1000+mix_b64_ld4_indir_p128_lp1_r1000+mix_b128_ld4_pshuf_p512_lp4_r1000+mix_b64_ld4_pshuf_p1_lp4_r1000
    sum       | mix_b64_ld7_lin_p128_lp4_r1000+mix_b128_ld4_pshuf_p512_lp4_r1000+mix_b64_ld1_xpage_p512_lp1_r1000+mix_b64_ld4_indir_p128_lp1_r1000+mix_b128_ld7_lin_p524288_lp1_r1000+mix_b128_ld14_pshuf_p524288_lp4_r1000+mix_b64_ld4_pshuf_p1_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 227386417238 | 228620059754 | 224241903834
    instructions:u     | 10499083135  | 10499083124  | 10499449418 
    br_retired:u       | 56017210     | 56017207     | 56035061    
    br_mis_pred:u      | 14977        | 15210        | 18189       
    l1i_cache:u        | 1357769582   | 1356096230   | 1356058243  
    l1i_cache_refill:u | 735596       | 727005       | 181799      
    l1i_tlb:u          | 1357769582   | 1356096230   | 1356058243  
    l1i_tlb_refill:u   | 2084         | 2089         | 953         
    l2i_cache:u        | 736274       | 727825       | 182817      
    l2i_cache_refill:u | 179185       | 180359       | 33142       
    l2i_tlb:u          | 2999         | 2704         | 1834        
    l2i_tlb_refill:u   | 2079         | 2083         | 809         
    l1d_cache:u        | 4319181203   | 4320452001   | 4324007699  
    l1d_cache_refill:u | 1454156576   | 1455354433   | 1380697558  
    l1d_tlb:u          | 5008040178   | 5014835065   | 5039965422  
    l1d_tlb_refill:u   | 572470435    | 572465999    | 573427479   
    l2d_cache:u        | 15864146650  | 15864787207  | 16234957041 
    l2d_cache_refill:u | 7166162013   | 7103469640   | 7090028048  
    l2d_tlb:u          | 572762037    | 573024976    | 573790314   
    l2d_tlb_refill:u   | 5097746      | 5099713      | 2552082     
    ll_cache:u         | 7164426770   | 7101614271   | 7088131973  
    ll_cache_miss:u    | 5283075057   | 5296171886   | 5273614178  

== combo_092_s7 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld14_pshuf_p512_lp1_r1000  
    s1 | mix_b64_ld1_xpage_p1_lp1_r1000      
    s2 | mix_b64_ld4_indir_p1_lp1_r1000      
    s3 | mix_b64_ld4_lin_p524288_lp1_r1000   
    s4 | mix_b128_ld2_lin_p1_lp1_r1000       
    s5 | mix_b128_ld1_pshuf_p524288_lp4_r1000
    s6 | mix_b128_ld7_indir_p524288_lp4_r1000
single_counts:
    metric             | s0          | s1         | s2         | s3          | s4         | s5         | s6          
    -------------------+-------------+------------+------------+-------------+------------+------------+-------------
    cpu-cycles:u       | 75203843486 | 274095754  | 1043133675 | 11130207345 | 1042099368 | 9886383809 | 228609174894
    instructions:u     | 2085065119  | 1061064161 | 1061064014 | 1061063795  | 2085064014 | 2085063801 | 2085065133  
    br_retired:u       | 8005199     | 8005002    | 8004982    | 8004922     | 8004982    | 8004920    | 8005208     
    br_mis_pred:u      | 3218        | 2079       | 1930       | 2736        | 2633       | 2887       | 3939        
    l1i_cache:u        | 269574386   | 138044535  | 137079544  | 137791441   | 266057135  | 266635766  | 267996045   
    l1i_cache_refill:u | 56273       | 796        | 964        | 4771        | 1495       | 10733      | 166430      
    l1i_tlb:u          | 269574386   | 138044535  | 137079544  | 137791441   | 266057135  | 266635766  | 267996045   
    l1i_tlb_refill:u   | 55          | 42         | 43         | 119         | 41         | 111        | 506         
    l2i_cache:u        | 56442       | 796        | 967        | 4778        | 1500       | 10780      | 167991      
    l2i_cache_refill:u | 2760        | 555        | 552        | 805         | 613        | 2109       | 9415        
    l2i_tlb:u          | 113         | 200        | 234        | 243         | 83         | 572        | 790         
    l2i_tlb_refill:u   | 35          | 11         | 11         | 113         | 12         | 104        | 501         
    l1d_cache:u        | 1808650006  | 77034842   | 269044971  | 269448891   | 269037688  | 141208534  | 910821598   
    l1d_cache_refill:u | 1794192502  | 129        | 266        | 48271944    | 282        | 56628334   | 897077420   
    l1d_tlb:u          | 3614738603  | 77050010   | 269083762  | 271539748   | 269065197  | 141644963  | 1798025415  
    l1d_tlb_refill:u   | 1796921426  | 77         | 81         | 788955      | 74         | 107620     | 871421980   
    l2d_cache:u        | 7090659187  | 1438       | 1943       | 1149162405  | 2255       | 483284065  | 3606755090  
    l2d_cache_refill:u | 3586533129  | 933        | 843        | 476941114   | 891        | 228426190  | 1815751798  
    l2d_tlb:u          | 1797190971  | 297        | 107        | 793632      | 110        | 111245     | 871505166   
    l2d_tlb_refill:u   | 562         | 15         | 4          | 481356      | 9          | 67859      | 8546604     
    ll_cache:u         | 3586494361  | 344        | 298        | 476637025   | 235        | 228444951  | 1814546174  
    ll_cache_miss:u    | 139148      | 31         | 20         | 434945417   | 51         | 189383910  | 1786119018  
combined_orders:
    id        | modules                                                                                                                                                                                                                                   
    ----------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_pshuf_p512_lp1_r1000+mix_b64_ld1_xpage_p1_lp1_r1000+mix_b64_ld4_indir_p1_lp1_r1000+mix_b64_ld4_lin_p524288_lp1_r1000+mix_b128_ld2_lin_p1_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000+mix_b128_ld7_indir_p524288_lp4_r1000
    shuffle   | mix_b64_ld4_indir_p1_lp1_r1000+mix_b128_ld2_lin_p1_lp1_r1000+mix_b64_ld4_lin_p524288_lp1_r1000+mix_b64_ld1_xpage_p1_lp1_r1000+mix_b128_ld14_pshuf_p512_lp1_r1000+mix_b128_ld7_indir_p524288_lp4_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000
    sum       | mix_b128_ld14_pshuf_p512_lp1_r1000+mix_b64_ld1_xpage_p1_lp1_r1000+mix_b64_ld4_indir_p1_lp1_r1000+mix_b64_ld4_lin_p524288_lp1_r1000+mix_b128_ld2_lin_p1_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp4_r1000+mix_b128_ld7_indir_p524288_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 325013113761 | 325776606162 | 327188938331
    instructions:u     | 11523083342  | 11523083385  | 11523450037 
    br_retired:u       | 56017240     | 56017245     | 56035215    
    br_mis_pred:u      | 18527        | 21254        | 19422       
    l1i_cache:u        | 1486298271   | 1488716497   | 1483178852  
    l1i_cache_refill:u | 838120       | 835996       | 241462      
    l1i_tlb:u          | 1486298271   | 1488716497   | 1483178852  
    l1i_tlb_refill:u   | 3330         | 3306         | 917         
    l2i_cache:u        | 839181       | 837583       | 243254      
    l2i_cache_refill:u | 131067       | 125273       | 16809       
    l2i_tlb:u          | 4749         | 5373         | 2235        
    l2i_tlb_refill:u   | 3325         | 3301         | 787         
    l1d_cache:u        | 3745536251   | 3747354634   | 3745246530  
    l1d_cache_refill:u | 2786572534   | 2792366105   | 2796170877  
    l1d_tlb:u          | 6442184364   | 6450926319   | 6441147698  
    l1d_tlb_refill:u   | 2669678025   | 2671209969   | 2669240213  
    l2d_cache:u        | 12422608729  | 12399516944  | 12329866383 
    l2d_cache_refill:u | 6172594677   | 6154429533   | 6107654898  
    l2d_tlb:u          | 2670012484   | 2671619579   | 2669601528  
    l2d_tlb_refill:u   | 8527007      | 13602329     | 9096409     
    ll_cache:u         | 6170808816   | 6153011900   | 6106123388  
    ll_cache_miss:u    | 2463114679   | 2445274728   | 2410587595  

== combo_093_s7 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld2_indir_p128_lp1_r1000   
    s1 | mix_b128_ld14_xpage_p512_lp4_r1000  
    s2 | mix_b64_ld14_indir_p512_lp1_r1000   
    s3 | mix_b128_ld2_lin_p128_lp1_r1000     
    s4 | mix_b64_ld4_indir_p512_lp4_r1000    
    s5 | mix_b64_ld7_indir_p128_lp1_r1000    
    s6 | mix_b128_ld1_pshuf_p524288_lp1_r1000
single_counts:
    metric             | s0         | s1          | s2          | s3         | s4          | s5          | s6        
    -------------------+------------+-------------+-------------+------------+-------------+-------------+-----------
    cpu-cycles:u       | 6922364231 | 77398194262 | 37690855244 | 6878354955 | 11313614672 | 12149794712 | 5332422328
    instructions:u     | 2085063801 | 2085065025  | 1061065083  | 2085063795 | 1061063795  | 1061063801  | 2085063801
    br_retired:u       | 8004920    | 8005187     | 8005195     | 8004922    | 8004922     | 8004920     | 8004920   
    br_mis_pred:u      | 2993       | 3232        | 3108        | 2893       | 2186        | 2835        | 2279      
    l1i_cache:u        | 266107849  | 270150812   | 138899649   | 265110011  | 139130350   | 138253218   | 265554957 
    l1i_cache_refill:u | 6258       | 56742       | 12771       | 6264       | 4308        | 4801        | 5285      
    l1i_tlb:u          | 266107849  | 270150812   | 138899649   | 265110011  | 139130350   | 138253218   | 265554957 
    l1i_tlb_refill:u   | 44         | 46          | 51          | 50         | 43          | 54          | 60        
    l2i_cache:u        | 6284       | 57019       | 12802       | 6290       | 4317        | 4809        | 5298      
    l2i_cache_refill:u | 673        | 3150        | 1275        | 793        | 860         | 713         | 752       
    l2i_tlb:u          | 85         | 92          | 182         | 93         | 407         | 126         | 578       
    l2i_tlb_refill:u   | 16         | 24          | 39          | 13         | 18          | 46          | 54        
    l1d_cache:u        | 269056475  | 1808695832  | 911070320   | 269037263  | 269649720   | 461668400   | 141162638 
    l1d_cache_refill:u | 237970219  | 1795660917  | 897568349   | 239489452  | 254733763   | 433529795   | 24665449  
    l1d_tlb:u          | 533628908  | 3619074793  | 1821365037  | 532944212  | 522984347   | 918069034   | 142457043 
    l1d_tlb_refill:u   | 258000099  | 1797960550  | 900630716   | 258000127  | 245410460   | 450514352   | 393795    
    l2d_cache:u        | 692335084  | 7097766801  | 3549435206  | 713376315  | 975140468   | 1173881950  | 546549590 
    l2d_cache_refill:u | 153138465  | 3592871871  | 1797027811  | 174248887  | 466783964   | 270667226   | 226804133 
    l2d_tlb:u          | 258290403  | 1798117149  | 900843165   | 258001059  | 245502612   | 450532730   | 394616    
    l2d_tlb_refill:u   | 24         | 387         | 276         | 19         | 158         | 8           | 237453    
    ll_cache:u         | 153137308  | 3592836864  | 1797009054  | 174246509  | 466766421   | 270665534   | 226669733 
    ll_cache_miss:u    | 1475       | 12480985    | 136002      | 4650       | 1649757     | 111219      | 208002994 
combined_orders:
    id        | modules                                                                                                                                                                                                                                      
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld2_indir_p128_lp1_r1000+mix_b128_ld14_xpage_p512_lp4_r1000+mix_b64_ld14_indir_p512_lp1_r1000+mix_b128_ld2_lin_p128_lp1_r1000+mix_b64_ld4_indir_p512_lp4_r1000+mix_b64_ld7_indir_p128_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp1_r1000
    shuffle   | mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld4_indir_p512_lp4_r1000+mix_b64_ld7_indir_p128_lp1_r1000+mix_b64_ld14_indir_p512_lp1_r1000+mix_b128_ld2_lin_p128_lp1_r1000+mix_b128_ld2_indir_p128_lp1_r1000+mix_b128_ld14_xpage_p512_lp4_r1000
    sum       | mix_b128_ld2_indir_p128_lp1_r1000+mix_b128_ld14_xpage_p512_lp4_r1000+mix_b64_ld14_indir_p512_lp1_r1000+mix_b128_ld2_lin_p128_lp1_r1000+mix_b64_ld4_indir_p512_lp4_r1000+mix_b64_ld7_indir_p128_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 179706397582 | 183774401450 | 157685600404
    instructions:u     | 11523083178  | 11523083124  | 11523449101 
    br_retired:u       | 56017215     | 56017207     | 56034986    
    br_mis_pred:u      | 20391        | 25606        | 19526       
    l1i_cache:u        | 1486654466   | 1482048437   | 1483206846  
    l1i_cache_refill:u | 703002       | 686444       | 96429       
    l1i_tlb:u          | 1486654466   | 1482048437   | 1483206846  
    l1i_tlb_refill:u   | 1264         | 1276         | 348         
    l2i_cache:u        | 703491       | 687087       | 96819       
    l2i_cache_refill:u | 68719        | 77057        | 8216        
    l2i_tlb:u          | 2258         | 2211         | 1563        
    l2i_tlb_refill:u   | 1261         | 1271         | 210         
    l1d_cache:u        | 4130457197   | 4130641807   | 4130340648  
    l1d_cache_refill:u | 3892955794   | 3888771327   | 3883617944  
    l1d_tlb:u          | 8085112881   | 8086645862   | 8090523374  
    l1d_tlb_refill:u   | 3909002463   | 3909093269   | 3910910099  
    l2d_cache:u        | 14892815047  | 14954020483  | 14748485414 
    l2d_cache_refill:u | 6836464148   | 6895002226   | 6681542357  
    l2d_tlb:u          | 3910090067   | 3910147069   | 3911681734  
    l2d_tlb_refill:u   | 2433205      | 2420784      | 238325      
    ll_cache:u         | 6836142040   | 6894550919   | 6681331423  
    ll_cache_miss:u    | 342837069    | 353316215    | 222387082   

== combo_094_s7 ==
single_modules:
    id | module                              
    ---+-------------------------------------
    s0 | mix_b128_ld1_pshuf_p524288_lp1_r1000
    s1 | mix_b64_ld4_lin_p512_lp4_r1000      
    s2 | mix_b128_ld1_lin_p1_lp4_r1000       
    s3 | mix_b128_ld7_xpage_p512_lp4_r1000   
    s4 | mix_b128_ld4_pshuf_p128_lp1_r1000   
    s5 | mix_b128_ld2_indir_p512_lp1_r1000   
    s6 | mix_b64_ld2_lin_p128_lp4_r1000      
single_counts:
    metric             | s0         | s1         | s2         | s3          | s4          | s5          | s6        
    -------------------+------------+------------+------------+-------------+-------------+-------------+-----------
    cpu-cycles:u       | 5341097500 | 7604103316 | 530106572  | 39902955703 | 13631828486 | 10982639483 | 2348194316
    instructions:u     | 2085063795 | 1061063801 | 2085064023 | 2085065053  | 2085063795  | 2085063795  | 1061064029
    br_retired:u       | 8004922    | 8004920    | 8004983    | 8005190     | 8004922     | 8004922     | 8004981   
    br_mis_pred:u      | 2334       | 2629       | 2278       | 3597        | 2218        | 3049        | 2394      
    l1i_cache:u        | 266545794  | 138564998  | 265039478  | 265417875   | 267147667   | 266182664   | 137143259 
    l1i_cache_refill:u | 5568       | 3308       | 888        | 30219       | 10950       | 9392        | 1509      
    l1i_tlb:u          | 266545794  | 138564998  | 265039478  | 265417875   | 267147667   | 266182664   | 137143259 
    l1i_tlb_refill:u   | 61         | 43         | 40         | 45          | 45          | 45          | 47        
    l2i_cache:u        | 5591       | 3317       | 890        | 30329       | 11016       | 9422        | 1510      
    l2i_cache_refill:u | 1393       | 739        | 589        | 2096        | 772         | 774         | 617       
    l2i_tlb:u          | 250        | 118        | 793        | 102         | 288         | 97          | 88        
    l2i_tlb_refill:u   | 56         | 21         | 12         | 28          | 13          | 29          | 15        
    l1d_cache:u        | 141161646  | 269416850  | 141033795  | 909322179   | 525685209   | 269076298   | 141082545 
    l1d_cache_refill:u | 24738056   | 79646808   | 146        | 897015804   | 490626919   | 251862157   | 28093469  
    l1d_tlb:u          | 142315398  | 346929625  | 141048166  | 1812129198  | 1048014385  | 533065652   | 197196918 
    l1d_tlb_refill:u   | 393829     | 66070859   | 66         | 898233328   | 514277563   | 258023248   | 35007787  
    l2d_cache:u        | 546846767  | 869905808  | 1741       | 3545306423  | 1394664849  | 1097718515  | 350478500 
    l2d_cache_refill:u | 227048062  | 462174940  | 918        | 1792761416  | 369241920   | 532510361   | 90523613  
    l2d_tlb:u          | 394651     | 66126003   | 89         | 898251572   | 514424175   | 258030726   | 35016484  
    l2d_tlb_refill:u   | 237149     | 176        | 3          | 767         | 45          | 609         | 19        
    ll_cache:u         | 226917156  | 462116580  | 315        | 1792746414  | 369230364   | 532499859   | 90518128  
    ll_cache_miss:u    | 208240068  | 3277620    | 60         | 6563189     | 10280       | 13892187    | 333429    
combined_orders:
    id        | modules                                                                                                                                                                                                                               
    ----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld4_lin_p512_lp4_r1000+mix_b128_ld1_lin_p1_lp4_r1000+mix_b128_ld7_xpage_p512_lp4_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b128_ld2_indir_p512_lp1_r1000+mix_b64_ld2_lin_p128_lp4_r1000
    shuffle   | mix_b64_ld2_lin_p128_lp4_r1000+mix_b64_ld4_lin_p512_lp4_r1000+mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b128_ld1_lin_p1_lp4_r1000+mix_b128_ld7_xpage_p512_lp4_r1000+mix_b128_ld2_indir_p512_lp1_r1000
    sum       | mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld4_lin_p512_lp4_r1000+mix_b128_ld1_lin_p1_lp4_r1000+mix_b128_ld7_xpage_p512_lp4_r1000+mix_b128_ld4_pshuf_p128_lp1_r1000+mix_b128_ld2_indir_p512_lp1_r1000+mix_b64_ld2_lin_p128_lp4_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 98237238159 | 96462725465 | 80340925376
    instructions:u     | 12547083114 | 12547083067 | 12547448291
    br_retired:u       | 56017199    | 56017193    | 56034840   
    br_mis_pred:u      | 19582       | 21538       | 18499      
    l1i_cache:u        | 1608421136  | 1608371762  | 1606041735 
    l1i_cache_refill:u | 649896      | 592750      | 61834      
    l1i_tlb:u          | 1608421136  | 1608371762  | 1606041735 
    l1i_tlb_refill:u   | 1207        | 1217        | 326        
    l2i_cache:u        | 650332      | 593789      | 62075      
    l2i_cache_refill:u | 68480       | 60799       | 6980       
    l2i_tlb:u          | 1749        | 2145        | 1736       
    l2i_tlb_refill:u   | 1202        | 1211        | 174        
    l1d_cache:u        | 2396680128  | 2396808197  | 2396778522 
    l1d_cache_refill:u | 1757259025  | 1758140476  | 1771983359 
    l1d_tlb:u          | 4208266670  | 4211374875  | 4220699342 
    l1d_tlb_refill:u   | 1771019430  | 1771070011  | 1772006680 
    l2d_cache:u        | 7797756012  | 7853390313  | 7804922603 
    l2d_cache_refill:u | 3562446771  | 3608407074  | 3474261230 
    l2d_tlb:u          | 1771247339  | 1771449414  | 1772243700 
    l2d_tlb_refill:u   | 2264584     | 2290516     | 238768     
    ll_cache:u         | 3562000031  | 3608045430  | 3474028816 
    ll_cache_miss:u    | 341947010   | 319921791   | 232316833  

== combo_095_s7 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld7_pshuf_p512_lp4_r1000   
    s1 | mix_b128_ld1_indir_p1_lp1_r1000    
    s2 | mix_b64_ld7_xpage_p1_lp4_r1000     
    s3 | mix_b64_ld4_lin_p1_lp1_r1000       
    s4 | mix_b128_ld2_xpage_p1_lp4_r1000    
    s5 | mix_b64_ld7_pshuf_p524288_lp4_r1000
    s6 | mix_b128_ld2_xpage_p512_lp1_r1000  
single_counts:
    metric             | s0          | s1         | s2         | s3         | s4         | s5          | s6         
    -------------------+-------------+------------+------------+------------+------------+-------------+------------
    cpu-cycles:u       | 16692689437 | 530111051  | 1810089202 | 1043136115 | 1042110592 | 35713458086 | 10929460765
    instructions:u     | 1061063801  | 2085064014 | 1061064029 | 1061064027 | 2085064029 | 1061065123  | 2085063801 
    br_retired:u       | 8004920     | 8004982    | 8004981    | 8004982    | 8004981    | 8005199     | 8004920    
    br_mis_pred:u      | 2489        | 2286       | 2422       | 1895       | 2523       | 2761        | 2146       
    l1i_cache:u        | 139519160   | 266042119  | 137054153  | 137079492  | 266058237  | 139608060   | 266084635  
    l1i_cache_refill:u | 6120        | 1165       | 1192       | 1005       | 1520       | 13295       | 8801       
    l1i_tlb:u          | 139519160   | 266042119  | 137054153  | 137079492  | 266058237  | 139608060   | 266084635  
    l1i_tlb_refill:u   | 42          | 41         | 36         | 42         | 48         | 242         | 47         
    l2i_cache:u        | 6134        | 1166       | 1195       | 1008       | 1523       | 13324       | 8856       
    l2i_cache_refill:u | 2713        | 611        | 540        | 553        | 634        | 6108        | 811        
    l2i_tlb:u          | 121         | 733        | 82         | 102        | 153        | 336         | 555        
    l2i_tlb_refill:u   | 21          | 14         | 13         | 14         | 15         | 233         | 29         
    l1d_cache:u        | 462146095   | 141033784  | 461037750  | 269045028  | 269037264  | 462105568   | 269080089  
    l1d_cache_refill:u | 199608961   | 185        | 173        | 160        | 167        | 202867413   | 256000991  
    l1d_tlb:u          | 629151248   | 141048041  | 461083859  | 269084181  | 269073979  | 464008718   | 532897254  
    l1d_tlb_refill:u   | 114210426   | 81         | 94         | 75         | 77         | 355087      | 258024449  
    l2d_cache:u        | 1611928808  | 2052       | 1866       | 1663       | 2042       | 1748855033  | 1031105290 
    l2d_cache_refill:u | 697420222   | 958        | 826        | 936        | 883        | 859493087   | 512227878  
    l2d_tlb:u          | 114284364   | 111        | 196        | 156        | 100        | 367245      | 258032106  
    l2d_tlb_refill:u   | 210         | 6          | 7          | 25         | 8          | 234538      | 211        
    ll_cache:u         | 697358666   | 303        | 239        | 298        | 257        | 859523302   | 512221094  
    ll_cache_miss:u    | 1878652     | 43         | 29         | 50         | 11         | 726219958   | 10707      
combined_orders:
    id        | modules                                                                                                                                                                                                                           
    ----------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b128_ld1_indir_p1_lp1_r1000+mix_b64_ld7_xpage_p1_lp4_r1000+mix_b64_ld4_lin_p1_lp1_r1000+mix_b128_ld2_xpage_p1_lp4_r1000+mix_b64_ld7_pshuf_p524288_lp4_r1000+mix_b128_ld2_xpage_p512_lp1_r1000
    shuffle   | mix_b64_ld7_pshuf_p524288_lp4_r1000+mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b64_ld7_xpage_p1_lp4_r1000+mix_b128_ld2_xpage_p512_lp1_r1000+mix_b128_ld2_xpage_p1_lp4_r1000+mix_b64_ld4_lin_p1_lp1_r1000+mix_b128_ld1_indir_p1_lp1_r1000
    sum       | mix_b64_ld7_pshuf_p512_lp4_r1000+mix_b128_ld1_indir_p1_lp1_r1000+mix_b64_ld7_xpage_p1_lp4_r1000+mix_b64_ld4_lin_p1_lp1_r1000+mix_b128_ld2_xpage_p1_lp4_r1000+mix_b64_ld7_pshuf_p524288_lp4_r1000+mix_b128_ld2_xpage_p512_lp1_r1000
combined_counts:
    metric             | canonical   | shuffle     | sum        
    -------------------+-------------+-------------+------------
    cpu-cycles:u       | 68841872014 | 69284019221 | 67761055248
    instructions:u     | 10499083040 | 10499083107 | 10499448824
    br_retired:u       | 56017189    | 56017197    | 56034965   
    br_mis_pred:u      | 16216       | 9149        | 16522      
    l1i_cache:u        | 1353284984  | 1352373067  | 1351445856 
    l1i_cache_refill:u | 385905      | 391802      | 33098      
    l1i_tlb:u          | 1353284984  | 1352373067  | 1351445856 
    l1i_tlb_refill:u   | 827         | 822         | 498        
    l2i_cache:u        | 386301      | 392196      | 33206      
    l2i_cache_refill:u | 77154       | 83643       | 11970      
    l2i_tlb:u          | 1773        | 1212        | 2082       
    l2i_tlb_refill:u   | 823         | 817         | 339        
    l1d_cache:u        | 2333332530  | 2333377770  | 2333485578 
    l1d_cache_refill:u | 669523134   | 659596910   | 658478050  
    l1d_tlb:u          | 2766157853  | 2767199072  | 2766347280 
    l1d_tlb_refill:u   | 372585233   | 372584125   | 372590289  
    l2d_cache:u        | 4282470041  | 4311541955  | 4391896754 
    l2d_cache_refill:u | 2035515903  | 2042418274  | 2069144790 
    l2d_tlb:u          | 372711410   | 372714687   | 372684278  
    l2d_tlb_refill:u   | 1141179     | 1081089     | 235005     
    ll_cache:u         | 2035153405  | 2042239726  | 2069104159 
    ll_cache_miss:u    | 777224556   | 774250582   | 728109450  

== combo_096_s7 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b128_ld4_pshuf_p128_lp4_r1000  
    s1 | mix_b64_ld1_indir_p524288_lp4_r1000
    s2 | mix_b64_ld1_lin_p128_lp4_r1000     
    s3 | mix_b64_ld1_pshuf_p128_lp4_r1000   
    s4 | mix_b128_ld14_indir_p128_lp1_r1000 
    s5 | mix_b128_ld14_xpage_p512_lp1_r1000 
    s6 | mix_b128_ld4_lin_p1_lp1_r1000      
single_counts:
    metric             | s0         | s1          | s2         | s3         | s4          | s5          | s6        
    -------------------+------------+-------------+------------+------------+-------------+-------------+-----------
    cpu-cycles:u       | 8612776759 | 16416533110 | 1227885814 | 1232283098 | 55592868876 | 75263546374 | 2067407103
    instructions:u     | 2085063795 | 1061063795  | 1061064036 | 1061064023 | 2085065095  | 2085065049  | 2085064020
    br_retired:u       | 8004922    | 8004922     | 8004983    | 8004983    | 8005196     | 8005190     | 8004980   
    br_mis_pred:u      | 2388       | 2557        | 2083       | 1975       | 3702        | 3321        | 2443      
    l1i_cache:u        | 266768834  | 138825465   | 137160690  | 137163994  | 266160098   | 269905631   | 265112423 
    l1i_cache_refill:u | 6989       | 6687        | 1137       | 1075       | 41236       | 55258       | 2345      
    l1i_tlb:u          | 266768834  | 138825465   | 137160690  | 137163994  | 266160098   | 269905631   | 265112423 
    l1i_tlb_refill:u   | 42         | 164         | 53         | 35         | 46          | 44          | 42        
    l2i_cache:u        | 7012       | 6698        | 1137       | 1077       | 41430       | 55636       | 2362      
    l2i_cache_refill:u | 872        | 2817        | 630        | 553        | 1176        | 2693        | 618       
    l2i_tlb:u          | 95         | 458         | 110        | 80         | 121         | 101         | 96        
    l2i_tlb_refill:u   | 13         | 162         | 33         | 13         | 18          | 23          | 13        
    l1d_cache:u        | 525494557  | 77237141    | 77070492   | 77075796   | 1806451543  | 1809182801  | 525081705 
    l1d_cache_refill:u | 166101468  | 64386661    | 14982704   | 24404941   | 1714754669  | 1794888138  | 185       
    l1d_tlb:u          | 729528037  | 149251301   | 103487829  | 103735861  | 3609311318  | 3616551154  | 525135509 
    l1d_tlb_refill:u   | 130000101  | 64116639    | 17000172   | 17000128   | 1795047743  | 1797349280  | 93        
    l2d_cache:u        | 1684303170 | 273203130   | 170021276  | 206160101  | 4892411927  | 7097732654  | 3127      
    l2d_cache_refill:u | 269272037  | 142409563   | 40032460   | 32710733   | 1305236426  | 3595486798  | 1014      
    l2d_tlb:u          | 130031462  | 64147671    | 17000272   | 17000858   | 1795088241  | 1797611419  | 129       
    l2d_tlb_refill:u   | 21         | 692851      | 68         | 25         | 24          | 494         | 32        
    ll_cache:u         | 269261571  | 142322458   | 40030334   | 32709038   | 1305214898  | 3595451504  | 313       
    ll_cache_miss:u    | 752105     | 139811546   | 889391     | 50         | 66606       | 1613310     | 51        
combined_orders:
    id        | modules                                                                                                                                                                                                                                  
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld4_pshuf_p128_lp4_r1000+mix_b64_ld1_indir_p524288_lp4_r1000+mix_b64_ld1_lin_p128_lp4_r1000+mix_b64_ld1_pshuf_p128_lp4_r1000+mix_b128_ld14_indir_p128_lp1_r1000+mix_b128_ld14_xpage_p512_lp1_r1000+mix_b128_ld4_lin_p1_lp1_r1000
    shuffle   | mix_b64_ld1_pshuf_p128_lp4_r1000+mix_b64_ld1_indir_p524288_lp4_r1000+mix_b128_ld4_pshuf_p128_lp4_r1000+mix_b128_ld4_lin_p1_lp1_r1000+mix_b128_ld14_xpage_p512_lp1_r1000+mix_b64_ld1_lin_p128_lp4_r1000+mix_b128_ld14_indir_p128_lp1_r1000
    sum       | mix_b128_ld4_pshuf_p128_lp4_r1000+mix_b64_ld1_indir_p524288_lp4_r1000+mix_b64_ld1_lin_p128_lp4_r1000+mix_b64_ld1_pshuf_p128_lp4_r1000+mix_b128_ld14_indir_p128_lp1_r1000+mix_b128_ld14_xpage_p512_lp1_r1000+mix_b128_ld4_lin_p1_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 158206765530 | 167078135727 | 160413301134
    instructions:u     | 11523083049  | 11523083144  | 11523449813 
    br_retired:u       | 56017190     | 56017211     | 56035176    
    br_mis_pred:u      | 23020        | 22761        | 18469       
    l1i_cache:u        | 1483498911   | 1482781894   | 1481097135  
    l1i_cache_refill:u | 649392       | 664245       | 114727      
    l1i_tlb:u          | 1483498911   | 1482781894   | 1481097135  
    l1i_tlb_refill:u   | 1342         | 1387         | 426         
    l2i_cache:u        | 650152       | 664851       | 115352      
    l2i_cache_refill:u | 98662        | 79733        | 9359        
    l2i_tlb:u          | 2338         | 2149         | 1061        
    l2i_tlb_refill:u   | 1336         | 1388         | 275         
    l1d_cache:u        | 4895612897   | 4895541185   | 4897594035  
    l1d_cache_refill:u | 3794941353   | 3762233751   | 3779518766  
    l1d_tlb:u          | 8830683655   | 8831932262   | 8837001009  
    l1d_tlb_refill:u   | 3819105989   | 3819049891   | 3820514156  
    l2d_cache:u        | 14506747411  | 13928239001  | 14323835385 
    l2d_cache_refill:u | 5803964843   | 5135399803   | 5385149031  
    l2d_tlb:u          | 3819423916   | 3819454399   | 3820880052  
    l2d_tlb_refill:u   | 3629747      | 3523040      | 693515      
    ll_cache:u         | 5803642600   | 5135102527   | 5384990116  
    ll_cache_miss:u    | 284976570    | 250315623    | 143133059   

== combo_097_s7 ==
single_modules:
    id | module                               
    ---+--------------------------------------
    s0 | mix_b128_ld14_pshuf_p524288_lp1_r1000
    s1 | mix_b128_ld1_pshuf_p524288_lp1_r1000 
    s2 | mix_b64_ld4_lin_p1_lp4_r1000         
    s3 | mix_b128_ld7_pshuf_p128_lp1_r1000    
    s4 | mix_b128_ld14_pshuf_p1_lp1_r1000     
    s5 | mix_b128_ld1_lin_p1_lp1_r1000        
    s6 | mix_b64_ld14_xpage_p524288_lp4_r1000 
single_counts:
    metric             | s0          | s1         | s2         | s3          | s4         | s5         | s6          
    -------------------+-------------+------------+------------+-------------+------------+------------+-------------
    cpu-cycles:u       | 74289354524 | 5325083816 | 1043131561 | 22005506400 | 7186345872 | 530112066  | 225879993284
    instructions:u     | 2085065119  | 2085063801 | 1061064023 | 2085064018  | 2085063792 | 2085064020 | 1061065160  
    br_retired:u       | 8005199     | 8004920    | 8004983    | 8004976     | 8004919    | 8004980    | 8005212     
    br_mis_pred:u      | 3299        | 2723       | 1901       | 3476        | 2888       | 2294       | 3629        
    l1i_cache:u        | 268866573   | 266377726  | 137080204  | 265535749   | 266061722  | 266043141  | 137822129   
    l1i_cache_refill:u | 59646       | 5292       | 1077       | 17350       | 5558       | 1155       | 66985       
    l1i_tlb:u          | 268866573   | 266377726  | 137080204  | 265535749   | 266061722  | 266043141  | 137822129   
    l1i_tlb_refill:u   | 353         | 57         | 45         | 47          | 39         | 45         | 417         
    l2i_cache:u        | 60139       | 5330       | 1082       | 17417       | 5569       | 1158       | 67078       
    l2i_cache_refill:u | 2573        | 738        | 557        | 1126        | 610        | 628        | 6773        
    l2i_tlb:u          | 691         | 327        | 98         | 274         | 537        | 761        | 505         
    l2i_tlb_refill:u   | 347         | 53         | 14         | 13          | 12         | 11         | 413         
    l1d_cache:u        | 1807135996  | 141166804  | 269045110  | 909775352   | 1805039311 | 141033910  | 909344910   
    l1d_cache_refill:u | 335689044   | 24515392   | 190        | 865265972   | 167        | 163        | 896091277   
    l1d_tlb:u          | 1814800362  | 142411449  | 269083515  | 1814125418  | 1805088013 | 141048187  | 1794752143  
    l1d_tlb_refill:u   | 3740952     | 393965     | 76         | 898567677   | 119        | 79         | 870060949   
    l2d_cache:u        | 7583917663  | 549129830  | 1769       | 2378348768  | 5785       | 1895       | 3561240977  
    l2d_cache_refill:u | 3109786871  | 227942618  | 924        | 584962257   | 865        | 955        | 1810032095  
    l2d_tlb:u          | 3756701     | 394784     | 118        | 898596179   | 502        | 109        | 870113626   
    l2d_tlb_refill:u   | 214142      | 236934     | 8          | 29          | 4          | 5          | 8553903     
    ll_cache:u         | 3107900801  | 227786122  | 321        | 584959887   | 317        | 314        | 1809888820  
    ll_cache_miss:u    | 2832080068  | 209006226  | 64         | 30444       | 110        | 20         | 1805740326  
combined_orders:
    id        | modules                                                                                                                                                                                                                                      
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b128_ld14_pshuf_p524288_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld7_pshuf_p128_lp1_r1000+mix_b128_ld14_pshuf_p1_lp1_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b64_ld14_xpage_p524288_lp4_r1000
    shuffle   | mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b128_ld14_pshuf_p1_lp1_r1000+mix_b64_ld14_xpage_p524288_lp4_r1000+mix_b128_ld7_pshuf_p128_lp1_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b128_ld14_pshuf_p524288_lp1_r1000
    sum       | mix_b128_ld14_pshuf_p524288_lp1_r1000+mix_b128_ld1_pshuf_p524288_lp1_r1000+mix_b64_ld4_lin_p1_lp4_r1000+mix_b128_ld7_pshuf_p128_lp1_r1000+mix_b128_ld14_pshuf_p1_lp1_r1000+mix_b128_ld1_lin_p1_lp1_r1000+mix_b64_ld14_xpage_p524288_lp4_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 341155218941 | 336921938116 | 336259527523
    instructions:u     | 12547083353  | 12547083369  | 12547449933 
    br_retired:u       | 56017242     | 56017243     | 56035189    
    br_mis_pred:u      | 17848        | 21082        | 20210       
    l1i_cache:u        | 1610783465   | 1610397581   | 1607787244  
    l1i_cache_refill:u | 975284       | 971554       | 157063      
    l1i_tlb:u          | 1610783465   | 1610397581   | 1607787244  
    l1i_tlb_refill:u   | 3629         | 3643         | 1003        
    l2i_cache:u        | 976603       | 972857       | 157773      
    l2i_cache_refill:u | 112502       | 106058       | 13005       
    l2i_tlb:u          | 4146         | 4671         | 3193        
    l2i_tlb_refill:u   | 3622         | 3639         | 863         
    l1d_cache:u        | 5982298295   | 5982604484   | 5982541393  
    l1d_cache_refill:u | 2118659625   | 2129072951   | 2121562205  
    l1d_tlb:u          | 7789352147   | 7789517252   | 7781309087  
    l1d_tlb_refill:u   | 1774512603   | 1774857298   | 1772763817  
    l2d_cache:u        | 13994070063  | 14224118023  | 14072646687 
    l2d_cache_refill:u | 5660484836   | 5882530467   | 5732726585  
    l2d_tlb:u          | 1774627891   | 1775055603   | 1772862019  
    l2d_tlb_refill:u   | 14240059     | 15278269     | 9005025     
    ll_cache:u         | 5658128824   | 5879513957   | 5730536582  
    ll_cache_miss:u    | 4841578195   | 4854931522   | 4846857258  

== combo_098_s7 ==
single_modules:
    id | module                            
    ---+-----------------------------------
    s0 | mix_b64_ld14_lin_p524288_lp4_r1000
    s1 | mix_b64_ld1_pshuf_p512_lp4_r1000  
    s2 | mix_b128_ld14_xpage_p1_lp1_r1000  
    s3 | mix_b64_ld14_pshuf_p1_lp4_r1000   
    s4 | mix_b128_ld14_indir_p1_lp1_r1000  
    s5 | mix_b128_ld1_xpage_p128_lp1_r1000 
    s6 | mix_b128_ld7_lin_p128_lp1_r1000   
single_counts:
    metric             | s0          | s1         | s2         | s3         | s4         | s5         | s6         
    -------------------+-------------+------------+------------+------------+------------+------------+------------
    cpu-cycles:u       | 90520222566 | 2537880139 | 7186361271 | 3602156216 | 7186329456 | 3375364539 | 20902815476
    instructions:u     | 1061065143  | 1061064029 | 2085063792 | 1061063795 | 2085063786 | 2085063801 | 2085064025 
    br_retired:u       | 8005202     | 8004981    | 8004919    | 8004922    | 8004921    | 8004920    | 8004978    
    br_mis_pred:u      | 3387        | 2040       | 2927       | 2593       | 2956       | 2149       | 3172       
    l1i_cache:u        | 141202018   | 138306118  | 265063425  | 137057016  | 266064577  | 266219212  | 265534324  
    l1i_cache_refill:u | 44092       | 1524       | 5960       | 2171       | 5868       | 3299       | 15727      
    l1i_tlb:u          | 141202018   | 138306118  | 265063425  | 137057016  | 266064577  | 266219212  | 265534324  
    l1i_tlb_refill:u   | 339         | 45         | 49         | 46         | 52         | 52         | 47         
    l2i_cache:u        | 44280       | 1527       | 5998       | 2178       | 5906       | 3309       | 15775      
    l2i_cache_refill:u | 7895        | 900        | 662        | 586        | 662        | 653        | 1195       
    l2i_tlb:u          | 439         | 276        | 275        | 131        | 137        | 93         | 94         
    l2i_tlb_refill:u   | 336         | 19         | 13         | 14         | 43         | 16         | 14         
    l1d_cache:u        | 909435953   | 77118809   | 1805039122 | 909038309  | 1805039078 | 141087576  | 909773631  
    l1d_cache_refill:u | 210673897   | 33367076   | 213        | 220        | 214        | 122905584  | 858774034  
    l1d_tlb:u          | 911547820   | 103108407  | 1805087260 | 909084934  | 1805086642 | 276901244  | 1814080086 
    l1d_tlb_refill:u   | 705154      | 17000242   | 146        | 104        | 133        | 130000062  | 898532381  
    l2d_cache:u        | 3468808601  | 207081008  | 6894       | 2534       | 6697       | 364070357  | 2207239073 
    l2d_cache_refill:u | 2015464111  | 88664439   | 1111       | 864        | 1070       | 108050699  | 413210008  
    l2d_tlb:u          | 724110      | 17000318   | 178        | 140        | 152        | 130001082  | 898555971  
    l2d_tlb_refill:u   | 457503      | 130        | 8          | 7          | 6          | 115        | 25         
    ll_cache:u         | 2014918340  | 88658466   | 425        | 287        | 298        | 108049181  | 413207755  
    ll_cache_miss:u    | 1928697295  | 99458      | 115        | 53         | 135        | 2725       | 18197      
combined_orders:
    id        | modules                                                                                                                                                                                                                                
    ----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld14_lin_p524288_lp4_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b128_ld14_xpage_p1_lp1_r1000+mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p1_lp1_r1000+mix_b128_ld1_xpage_p128_lp1_r1000+mix_b128_ld7_lin_p128_lp1_r1000
    shuffle   | mix_b128_ld7_lin_p128_lp1_r1000+mix_b128_ld1_xpage_p128_lp1_r1000+mix_b128_ld14_indir_p1_lp1_r1000+mix_b128_ld14_xpage_p1_lp1_r1000+mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b64_ld14_lin_p524288_lp4_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000
    sum       | mix_b64_ld14_lin_p524288_lp4_r1000+mix_b64_ld1_pshuf_p512_lp4_r1000+mix_b128_ld14_xpage_p1_lp1_r1000+mix_b64_ld14_pshuf_p1_lp4_r1000+mix_b128_ld14_indir_p1_lp1_r1000+mix_b128_ld1_xpage_p128_lp1_r1000+mix_b128_ld7_lin_p128_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 137721751736 | 142699453917 | 135311129663
    instructions:u     | 11523083064  | 11523083064  | 11523448371 
    br_retired:u       | 56017192     | 56017192     | 56034843    
    br_mis_pred:u      | 20875        | 20096        | 19224       
    l1i_cache:u        | 1481842328   | 1482357655   | 1479446690  
    l1i_cache_refill:u | 574237       | 570157       | 78641       
    l1i_tlb:u          | 1481842328   | 1482357655   | 1479446690  
    l1i_tlb_refill:u   | 1178         | 1291         | 630         
    l2i_cache:u        | 575153       | 571097       | 78973       
    l2i_cache_refill:u | 112921       | 129687       | 12553       
    l2i_tlb:u          | 2080         | 2203         | 1445        
    l2i_tlb_refill:u   | 1164         | 1287         | 455         
    l1d_cache:u        | 6560038437   | 6556261701   | 6556532478  
    l1d_cache_refill:u | 1230687047   | 1233130047   | 1225721238  
    l1d_tlb:u          | 7630874547   | 7624257860   | 7624896393  
    l1d_tlb_refill:u   | 1046284781   | 1046470420   | 1046238222  
    l2d_cache:u        | 6674656862   | 6702576581   | 6247215164  
    l2d_cache_refill:u | 3015534697   | 3053476513   | 2625392302  
    l2d_tlb:u          | 1046372561   | 1046535716   | 1046281951  
    l2d_tlb_refill:u   | 1214527      | 1211896      | 457794      
    ll_cache:u         | 3014799530   | 3052752334   | 2624834752  
    ll_cache_miss:u    | 1979077634   | 1985301759   | 1928817978  

== combo_099_s7 ==
single_modules:
    id | module                             
    ---+------------------------------------
    s0 | mix_b64_ld4_pshuf_p128_lp1_r1000   
    s1 | mix_b64_ld4_lin_p524288_lp4_r1000  
    s2 | mix_b128_ld7_indir_p128_lp1_r1000  
    s3 | mix_b64_ld2_lin_p128_lp1_r1000     
    s4 | mix_b64_ld7_indir_p128_lp1_r1000   
    s5 | mix_b64_ld2_xpage_p524288_lp1_r1000
    s6 | mix_b64_ld7_indir_p128_lp1_r1000   
single_counts:
    metric             | s0         | s1          | s2          | s3         | s4          | s5          | s6        
    -------------------+------------+-------------+-------------+------------+-------------+-------------+-----------
    cpu-cycles:u       | 6791888374 | 26105900361 | 23213781452 | 3427236630 | 10601329500 | 32405280878 | 9555043950
    instructions:u     | 1061063795 | 1061065009  | 2085064012  | 1061063795 | 1061063801  | 1061065029  | 1061063795
    br_retired:u       | 8004922    | 8005185     | 8004978     | 8004922    | 8004920     | 8005187     | 8004922   
    br_mis_pred:u      | 2236       | 3281        | 3345        | 2571       | 3017        | 3407        | 2949      
    l1i_cache:u        | 138667502  | 138358181   | 265791404   | 137087210  | 138445621   | 138974848   | 137495184 
    l1i_cache_refill:u | 3083       | 9748        | 17653       | 2087       | 3969        | 11999       | 3654      
    l1i_tlb:u          | 138667502  | 138358181   | 265791404   | 137087210  | 138445621   | 138974848   | 137495184 
    l1i_tlb_refill:u   | 44         | 201         | 45          | 47         | 44          | 226         | 44        
    l2i_cache:u        | 3090       | 9777        | 17798       | 2094       | 3976        | 12028       | 3667      
    l2i_cache_refill:u | 649        | 3582        | 889         | 614        | 687         | 2533        | 593       
    l2i_tlb:u          | 226        | 289         | 188         | 96         | 1090        | 283         | 219       
    l2i_tlb_refill:u   | 16         | 198         | 19          | 16         | 19          | 221         | 14        
    l1d_cache:u        | 269451706  | 269138653   | 909827044   | 141056977  | 461197056   | 141434630   | 461370979 
    l1d_cache_refill:u | 245600775  | 69881135    | 857555216   | 121514000  | 430493694   | 128163039   | 431726836 
    l1d_tlb:u          | 536930629  | 269748601   | 1813858215  | 276889930  | 916440259   | 278661212   | 916978097 
    l1d_tlb_refill:u   | 259210424  | 213425      | 898547121   | 130000154  | 450123888   | 126242584   | 450266425 
    l2d_cache:u        | 712307283  | 868345016   | 2531217799  | 366540430  | 1172155277  | 508707070   | 1141222923
    l2d_cache_refill:u | 199689515  | 461056516   | 737573846   | 103458404  | 271670085   | 258050079   | 239312044 
    l2d_tlb:u          | 259286379  | 223491      | 898691088   | 130005678  | 450332649   | 126316407   | 450309332 
    l2d_tlb_refill:u   | 17         | 141323      | 30          | 55         | 115         | 1397711     | 22        
    ll_cache:u         | 199687809  | 460943348   | 737565974   | 103457523  | 271666916   | 258003749   | 239308990 
    ll_cache_miss:u    | 6102       | 434217389   | 21988       | 335        | 12850       | 256683031   | 455367    
combined_orders:
    id        | modules                                                                                                                                                                                                                                  
    ----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    canonical | mix_b64_ld4_pshuf_p128_lp1_r1000+mix_b64_ld4_lin_p524288_lp4_r1000+mix_b128_ld7_indir_p128_lp1_r1000+mix_b64_ld2_lin_p128_lp1_r1000+mix_b64_ld7_indir_p128_lp1_r1000+mix_b64_ld2_xpage_p524288_lp1_r1000+mix_b64_ld7_indir_p128_lp1_r1000
    shuffle   | mix_b64_ld2_xpage_p524288_lp1_r1000+mix_b64_ld4_pshuf_p128_lp1_r1000+mix_b64_ld2_lin_p128_lp1_r1000+mix_b64_ld4_lin_p524288_lp4_r1000+mix_b64_ld7_indir_p128_lp1_r1000+mix_b128_ld7_indir_p128_lp1_r1000+mix_b64_ld7_indir_p128_lp1_r1000
    sum       | mix_b64_ld4_pshuf_p128_lp1_r1000+mix_b64_ld4_lin_p524288_lp4_r1000+mix_b128_ld7_indir_p128_lp1_r1000+mix_b64_ld2_lin_p128_lp1_r1000+mix_b64_ld7_indir_p128_lp1_r1000+mix_b64_ld2_xpage_p524288_lp1_r1000+mix_b64_ld7_indir_p128_lp1_r1000
combined_counts:
    metric             | canonical    | shuffle      | sum         
    -------------------+--------------+--------------+-------------
    cpu-cycles:u       | 119575147664 | 118514115297 | 112100461145
    instructions:u     | 8451083064   | 8451083059   | 8451449236  
    br_retired:u       | 56017192     | 56017191     | 56035036    
    br_mis_pred:u      | 21866        | 21125        | 20806       
    l1i_cache:u        | 1097601450   | 1097039795   | 1094819950  
    l1i_cache_refill:u | 389555       | 353698       | 52193       
    l1i_tlb:u          | 1097601450   | 1097039795   | 1094819950  
    l1i_tlb_refill:u   | 1381         | 1383         | 651         
    l2i_cache:u        | 389716       | 354005       | 52430       
    l2i_cache_refill:u | 82778        | 55860        | 9547        
    l2i_tlb:u          | 2388         | 2463         | 2391        
    l2i_tlb_refill:u   | 1377         | 1378         | 503         
    l1d_cache:u        | 2653117780   | 2653385219   | 2653477045  
    l1d_cache_refill:u | 2304563109   | 2305854267   | 2284934695  
    l1d_tlb:u          | 5007496749   | 5010099081   | 5009506943  
    l1d_tlb_refill:u   | 2313348189   | 2313675744   | 2314604021  
    l2d_cache:u        | 7344688896   | 7403171339   | 7300495798  
    l2d_cache_refill:u | 2295470137   | 2362635454   | 2270810489  
    l2d_tlb:u          | 2313810946   | 2314547473   | 2315165024  
    l2d_tlb_refill:u   | 3614821      | 4073460      | 1539273     
    ll_cache:u         | 2295088053   | 2362315463   | 2270634309  
    ll_cache_miss:u    | 729173190    | 710479015    | 691397062   

