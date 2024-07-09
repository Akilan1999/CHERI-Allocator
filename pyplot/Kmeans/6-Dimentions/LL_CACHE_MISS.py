import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array(np.array([int(x) for x in """742051
              559499
              372615
              383619
              428808
              336756
              518580
              390112
              375579
              421849
              381810
              384743
              469525
              421909
              487489
              337821
              469539
              366665
              469249
              509121
              430155
              375011
              462737
              530009
              481996
              427822
              356143
              528752
              542248
              493358
              479450
              425282
              517723
              426863
              540465
              466203
              456952
              499337
              538226""".replace('              ',',').replace('\n','').split(",")]))

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array(np.array([int(x) for x in """736765
              531488
              423974
              374492
              554088
              388215
              374805
              519748
              474860
              534621
              535391
              631809
              496852
              509826
              519247
              471033
              508710
              525277
              501897
              394173
              493662
              375646
              431544
              382177
              630827
              452712
              556464
              510118
              534303
              550329
              574236
              479424
              575782
              428647
              508028
              475290
              491714
              462188
              294159""".replace('              ',',').replace('\n','').split(",")]))

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
# plt.title("L1D cache miss read \n ARM Performance counter: L1D_CACHE_LMISS_RD \n each Memory-read operation or Memory-write operation that causes a cache \n access to at least the Level 1 data or unified cache. This includes each complete or partial translation table walk that causes an access to memory, including to data or translation table walk caches. \n Kmeans C program with Cluster size 6")

plt.xlabel("time in seconds")
plt.ylabel("DTLB walks")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('ll_kmeans_6_dimentions.png')