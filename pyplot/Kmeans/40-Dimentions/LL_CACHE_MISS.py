import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array(np.array([int(x) for x in """1147403
              829036
              563124
              979733
              683541
              618378
              905917
              561979
              902313
              823260
              499959
              627898
              915499
              646610
              739437
              945235
              541299
              637887
              842954
              703414
              1291380
              675118
              671111
              585563
              585483
              951820
              791179
              701760
              552971
              696260
              902072
              815292
              826315
              740385
              805546
              736227
              690416
              769363
              825820
              1027783
              797795
              863187
              834350
              548714
              759409
              667769
              840026
              861216
              895136
              719523
              504731
              959369
              1052167
              668707
              558918
              778832
              681806
              1268380
              825940
              874677
              670802
              808349
              653938
              996132
              769110
              1077410
              714249
              660753
              551064
              867647
              556815
              687308
              780915
              604863
              936983
              818984
              697969
              1063845
              722724
              864795
              791971
              489493
              678041
              514280
              784758
              643920
              896146
              567640
              854350
              548957
              583866
              880357
              589791
              604616
              560377
              527240
              673535
              503032
              851726
              484139
              649485
              978010
              641704
              488143
              710347
              808049
              1035491
              695389
              441112
              929079
              622864
              516002
              902311
              783120
              687561
              687898
              525210
              731349
              1332534
              537479
              542351
              511237
              564299
              859176
              713889
              901452
              631327
              681258
              1035948
              634997
              455623
              851931
              612646
              902292
              787158
              660371
              791336
              702494
              644624
              764093
              946863
              984181
              666091
              571202
              590691
              1160676
              624435
              677302
              491699
              870564
              1096683
              701710
              767120
              886663
              847346
              726936
              828216
              731833
              1143815
              893945
              446303""".replace('              ',',').replace('\n','').split(",")]))

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array(np.array([int(x) for x in """1603321
              906001
              831508
              1260778
              874222
              639952
              811423
              876933
              871938
              845695
              811517
              1078035
              1155039
              931630
              734393
              1040144
              897608
              567688
              1017724
              816640
              1156306
              1182610
              2087536
              935131
              564650
              781929
              1032678
              842187
              714283
              1512066
              903441
              821687
              750216
              1623056
              1113602
              602318
              1056833
              829348
              924366
              917254
              1417581
              1056215
              534696
              957581
              873314
              615740
              793892
              1166512
              508943
              509190
              656245
              1304353
              909374
              638685
              1848084
              1067142
              543667
              591408
              1215657
              952755
              1191746
              1779363
              780965
              966607
              618025
              1082331
              1177658
              1136390
              1914232
              570957
              846572
              577331
              1232137
              1037267
              1262158
              1029892
              1122356
              995490
              1174365
              1340139
              1097573
              621145
              649356
              1082100
              792184
              1046410
              1217530
              952589
              634895
              866331
              1560533
              870354
              692937
              1249514
              731255
              899044
              1132861
              871474
              1440239
              1109188
              915075
              1625844
              811510
              845837
              680654
              1527778
              556130
              761597
              1452068
              856231
              729522
              670614
              1449778
              554624
              965716
              1030135
              1018319
              609395
              630688
              1379329
              674255
              808523
              1098093
              1502941
              689121
              901665
              1173878
              637713
              756162
              988917
              959839
              581439
              618517
              1482465
              539794
              982852
              878227
              1259422
              774118
              667883
              1238176
              1393325
              721119
              1185418
              1324310
              605043
              1029433
              1029119
              582207
              1028124
              844517
              1594356
              1175972
              910822
              660335
              973991
              1048600
              521274
              1771930""".replace('              ',',').replace('\n','').split(",")]))

xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

plt.plot(xpoints, ypoints,label='Malloc Physically contigous with bounds')
plt.plot(xpoints1, ypoints1,label='System memory allocator')

'''
L1D_CACHE_LMISS_RD
The counter counts each Memory-read operation to the Level 1 data or unified cache counted by L1D_CACHE that incurs additional latency because it returns data from outside of the Level 1 data or unified cache of this PE.
The event indicates to software that the access missed in the Level 1 data or unified cache and might have a significant performance impact due to the additional latency compared to the latency of an access that hits in the Level 1 data or unified cache.
The counter does not count:
• Accesses where the additional latency is unlikely to be significantly performance-impacting. For example, if the access hits in another cache in the same local cluster, and the additional latency is small when compared to a miss in all Level 1 caches that the access looks up in and results in an access being made to a Level 2 cache or elsewhere beyond the Level 1 data or unified cache.
• A miss that does not cause a new cache refill but is satisfied from a previous miss.
An implementation is not required to measure the latency, nor to track the access to determine whether the additional latency caused a performance impact. An implementation can extend the definition of this event with additional scenarios where an access might have a significant performance impact due to additional latency for the access.
It is IMPLEMENTATION DEFINED whether accesses that result from cache maintenance operations are counted.
If the cache is shared and the Effective value of PMEVTYPER<n>_EL0.MT for the counter is 0, then the counter counts only events Attributable to the PE counting the event. For a multithreaded processor implementation, if the cache is shared by PEs other than the PEs in the multithreaded processor and the Effective value of PMEVTYPER<n>_EL0.MT for the counter is 1, then the counter counts only events Attributable to PEs in the multithreaded processor. In all other cases, it is IMPLEMENTATION DEFINED whether only events Attributable to the PE counting the event or all events are counted, and might depend on the Effective value of PMEVTYPER<n>_EL1.MT.
PMCEID1_EL0[25] reads as 1 if this event is implemented and 0 otherwise. This event must be implemented if FEAT_PMUv3p4 is implemented.
'''
# plt.title("L1D cache miss read \n ARM Performance counter: L1D_CACHE_LMISS_RD \n each Memory-read operation or Memory-write operation that causes a cache \n access to at least the Level 1 data or unified cache. This includes each complete or partial translation table walk that causes an access to memory, including to data or translation table walk caches. \n Kmeans C program with Dimentions size 40")

plt.xlabel("time in seconds")
plt.ylabel("L1 Cache misses")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('ll_tlb_40_dimentions.png')