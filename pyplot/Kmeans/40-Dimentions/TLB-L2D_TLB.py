import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])


ypoints = np.array([int(x) for x in """66540
       7859
       23464
       43214
       27505
       27462
       46371
       10104
       65940
       26508
       18169
       33410
       35932
       31967
       61487
       22289
       61131
       49936
       8378
       70970
       64227
       45327
       14493
       8585
       34713
       62427
       27633
       49391
       28682
       21025
       30477
       19946
       34838
       53935
       51581
       19594
       17913
       33452
       57925
       78362
       9176
       43589
       57070
       23447
       28627
       17297
       54966
       59315
       52363
       50624
       26515
       31190
       106412
       35441
       10280
       21075
       9663
       78816
       48329
       48742
       40940
       40585
       33234
       71473
       21832
       66627
       18375
       18306
       34411
       56034
       24142
       74324
       34921
       10427
       65288
       17961
       30433
       17538
       33052
       63611
       15918
       8983
       47290
       30154
       68913
       30144
       68603
       16772
       76516
       31663
       50528
       36797
       27584
       74728
       9514
       16252
       34017
       39159
       73261
       34238
       9979
       100145
       30276
       32994
       26959
       37082
       82385
       34030
       65503
       24471
       22303
       9260
       24329
       69294
       34741
       23791
       43832
       50302
       98996
       45543
       35170
        9195
        9658
       63685
       21802
       39287
       35287
       8836
       113920
       38764
       23417
       41543
       11622
       45682
       57685
       53500
       13722
       11203
       22599
       92580
       40797
       56990
       81024
       9030
       45653
       65413
       17266
       59900
       33502
       10976
       28385
       33838
       61241
       29094
       36072
       146101
       8552
       30128
       51724
       24090""".replace('       ',',').replace('\n','').split(",")])

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array([int(x) for x in """147309
       24207
       72608
       53185
       29916
       62288
       19733
       20551
       15416
       33266
       38374
       37710
       76787
       38460
       35339
       15569
       43172
       40743
       35956
       52172
       17231
       32107
       66245
       78219
       57454
       37971
       21077
       38089
       16171
       26842
       70623
       61517
       43946
       16101
       64700
       15876
       18604
       52025
       32854
       48066
      110412
       74894
       15982
       16951
       30104
       67263
       97568
       71199
       47570
       60400
      119246
       46025
       39649
       61263
       31674
       18139
       52567
      106665
       28508
       50885
       30868
       64452
       21987
      104550
       60096
       35098
       27626
       26791
       44735
       24076
       53037
       18897
       49820
       44744
       46927
       58569
       17651
       45036
       55358
       31643
       15816
       75636
       62402
       17341
       71459
       41987
       16640
       15786
       79108
       60482
       35872
       21016
       38518
       17325
       16738
       84271
       28477
       52976
       40236
       51622
       19197
       15498
       38114
       34553
       83946
      108452
       44795
       39454
       49442
       22963
       72816
       64652
       74099
       22675
       60850
       76929
       50585
       61838
       41130
       45360
       17933
       70220
       87695
       19565
       64806
       78487
       21187
       56748
       93777
       53159
       19220
       33799
       19743
       31416
       37750
       67563
       53070
       18014
       19133
       39304
       41509
       16661
       81493
       53422
       17376
       15742
       56450
       49720
       34734
       47112
       16915
       17586
       16895
       79737
       48293
       35941
       18742
       54320
       33438""".replace('    ',',').replace('\n','').split(",")])

xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

plt.plot(xpoints, ypoints,label='Malloc Physically contigous with bounds')
plt.plot(xpoints1, ypoints1,label='System memory allocator')

# plt.title("Level 2 data TLB acces, read \n ARM Performance counter: L2D_TLB \n The counter counts each Memory-read operation or Memory-write operation that causes a TLB access to at least the Level 2 data or unified TLB. \n Kmeans C program with Cluster size 40")

plt.xlabel("time in seconds")
plt.ylabel("L2 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('l2_tlb_40_dimentions.png')