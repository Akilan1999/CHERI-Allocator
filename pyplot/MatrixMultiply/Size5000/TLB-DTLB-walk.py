import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([int(x) for x in """1072
         1566
         0
         775
         564
         574
         0
         0
         1842
         397
         832
         0
         1143
         0
         1132
         0
         0
         3478
         335
         1181
         0
         1451
         0
         0
         2456
         914
         566
         208
         1323
         0
         1341
         0
         0
         0
         2800
         869
         0
         1624
         852
         0
         1444
         78
         0
         1165
         242
         0
         0
         1436
         0
         1656
         1295
         672
         0
         2124
         689
         247
         974
         196
         664
         0
         0
         0
         0
         4571
         411
         1108
         0
         1855
         779
         0
         0
         0
         3973
         0
         0
         2126
         1090
         0
         0
         0
         1455
         868
         834
         0
         2252
         743
         0
         0
         0
         2867
         576
         528
         737
         1279
         753
         0
         0
         1469
         709
         0
         951
         1011
         560
         923
         389
         681
         887
         0
         1091""".replace('         ',',').replace('\n','').split(",")])

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array([int(x) for x in """2077
    0
    2240
    974
    400
    0
    1949
    0
    353
    0
    2136
    1292
    1150
    1080
    1029
    188
    16
    9401
    3108
    0
    12850
    2972
    0
    13417
    4015
    0
    0
    12179
    708
    4434
    5515
    105
    0
    0
    52251
    8327
    0
    0
    0
    7628
    0
    6047
    2796
    2505
    1949
    0
    0
    0
    0
    14301
    0
    5171
    3362
    3772
    0
    27162
    15974
    5284
    11553
    0
    24698
    0
    14835
    0
    21593
    664
    5721
    12945
    0
    13774
    0
    14722
    1465
    0
    27655
    2332
    4084
    33813
    0
    9790
    0
    50326
    5316
    0
    0
    0
    0
    9760
    4192
    1552
    7241
    3216
    4888
    8667
    28500
    8415
    4523
    1449
    4652
    0
    7625
    0
    13775
    0
    1897
    4708
    0
    12225
    4482759
    191711306
    235410343
    173845602
    242711520
    154862574
    192747518
    220667551
    275602208
    184073481
    198073425
    227482742
    187971748
    183689903
    187178845
    186674013
    207741123
    233177167
    221368814
    183933427
    181175654
    204068107
    228269124
    205027178
    209400883
    187840131
    188293011
    221927087
    232807458
    188215220
    180783387
    216711542
    208036998
    214266374
    186414281
    180185139
    185237868
    191677316
    183911791
    183803795
    224964126
    204113022
    210381502
    225585571
    220223453
    226214857
    204932647
    184864540
    217262003
    202414930
    191948700
    193400960
    181280109
    180323521
    184002482
    207777617
    222940234
    189422853
    186182495
    186261124
    181304280
    192816961
    184117119
    209667712
    240951856
    219942014
    221564848
    192926621
    181690338
    183097907
    186087016
    184347616
    180377265
    199009737
    182802614""".replace('    ',',').replace('\n','').split(",")])

xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

plt.plot(xpoints, ypoints,label='Malloc Physically contigous with bounds')
plt.plot(xpoints1, ypoints1,label='System memory allocator')

'''
DTLB_WALK
The counter counts each access counted by L1D_TLB that causes a 
refill of a data or unified 
TLB involving at least one translation table walk access.
This includes each complete or partial translation table walk that causes an 
access to memory, including to data or translation table walk caches.
If Armv8.7 is not implemented, it is IMPLEMENTATION DEFINED whether accesses 
that cause an update of an existing TLB entry involving at least one translation 
table walk access are counted. If Armv8.7 is implemented, these accesses 
are counted.
'''
plt.title("Data TLB access, read \n ARM Performance counter: DTLB_WALK \n Data TLB access with at least one translation table walk \n This includes each complete or partial translation table walk that causes an access to memory, including to data or translation table walk caches. \n Histogram medium")

plt.xlabel("time in seconds")
plt.ylabel("DTLB walks")
# plt.plot(xpoints1, ypoints1)
plt.legend()
plt.show()