import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([2100870,19384360])

xpoints = ["Malloc Physically contigous with bounds","System memory allocator"]

# ypoints1 = np.array([19384360])

# xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

plt.bar(xpoints, ypoints)
# plt.bar(xpoints1, ypoints1,label='System memory allocator')

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
# plt.title("L1D cache miss read \n ARM Performance counter: L1D_CACHE_LMISS_RD \n each Memory-read operation or Memory-write operation that causes a cache \n access to at least the Level 1 data or unified cache. This includes each complete or partial translation table walk that causes an access to memory, including to data or translation table walk caches. \n Histogram medium")

plt.xlabel("time in seconds")
plt.ylabel("L1D cache misses")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('ll_histogram_small.png')