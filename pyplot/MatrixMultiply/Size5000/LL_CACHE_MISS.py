import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints1 = np.array(np.array([int(x) for x in """0
              0
              0
              326765
              0
              143484
              0
              0
              0
              0
              0
              0
              464576
              99734
              70229
              78698
              50530
              93548
              64971
              10767
              137521
              7028
              132692
              73331
              73142
              0
              138998
              0
              78208
              0
              198635
              0
              126237
              77513
              73931
              72472
              75476
              0
              87771
              88689
              110750
              73056
              70395
              0
              137320
              0
              106593
              0
              113893
              0
              0
              247353
              71688
              0
              0
              0
              306619
              48398
              76920
              72885
              0
              160647
              56256
              58108
              99557
              0
              122549
              79748
              77494
              0
              142310
              0
              131992
              71645
              0
              152255
              73324
              70870
              67944
              72820
              72185
              71309
              70495
              74632
              0
              142266
              15879
              123504
              0
              138605
              70871
              68983
              17283
              125136
              45899
              49622
              62345
              123180
              0
              127536
              83637
              19920
              116609
              23423
              70723
              52828
              88384
              75240
              74572
              15926815
              21348754
              20703968 
              22389062
              20992753
              21657595
              21797899
              21449332
              22178036
              21222075
              20807027
              24825060
              24390913
              27926846
              24373458
              23572469
              21851595
              21905648
              21818847
              24682778
              25138079
              24572099
              22573802
              24027619
              25668582
              23439214
              21842812
              21773955
              21937392
              22182668
              21837997
              22016854
              23966253
              25743918
              22093267
              23362716
              21546631
              23028139
              25033183
              24980317
              24431848
              22165558
              22660672
              22342552
              21674610
              21231647
              23343685
              25355447
              21432591
              15824624
              19407533
              24295429
              22510455
              17120495
              19704211
              20393780
              24520902
              25454814
              22826189
              23197333
              23909896
              24263964
              21327971
              17364694
              15234428
              21608937
              22042900
              24071774
              21218994
              24225649
              24232228
              22718402
              22553169
              24904231
              5354218""".replace('              ',',').replace('\n','').split(",")]))

xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

ypoints = np.array(np.array([int(x) for x in """99132
              38980
              0
              197161
              0
              67519
              0
              140400
              0
              143043
              0
              0
              0
              284282
              0
              140444
              0
              134435
              83831
              50211
              75049
              0
              0
              0
              288554
              74050
              71429
              74809
              73262
              73649
              0
              140714
              70424
              0
              147499
              68600
              81265
              0
              139783
              64799
              0
              151170
              68801
              0
              145452
              0
              125288
              0
              163795
              0
              141640
              73859
              74317
              64148
              0
              136959
              72307
              69894
              77496
              67138
              0
              139846
              70331
              0
              132302
              70375
              0
              84102
              123513
              0
              144565
              3028
              137573
              5823
              71125
              134909
              0
              138289
              0
              134450
              0
              142950
              0
              86537
              111946
              0
              114053
              0
              128592
              91062
              0
              0
              238779
              74466
              70433
              77585
              28764
              73445
              110675
              34944
              106227
              73441
              66853
              38920
              72495
              104062
              11226
              105905
              70625
              56476""".replace('              ',',').replace('\n','').split(",")]))

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

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
plt.title("L1D cache miss read \n ARM Performance counter: L1D_CACHE_LMISS_RD \n each Memory-read operation or Memory-write operation that causes a cache \n access to at least the Level 1 data or unified cache. This includes each complete or partial translation table walk that causes an access to memory, including to data or translation table walk caches. \n Histogram medium")

plt.xlabel("time in seconds")
plt.ylabel("DTLB walks")
# plt.plot(xpoints1, ypoints1)
plt.legend()
plt.show()