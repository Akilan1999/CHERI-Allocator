import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([12140,
         7054,
         3621,
         5391,
         6391,
         6235,
         4067,
         4433,
         5248,
         3321,
         4790,
         4832,
         5783,
         3709,
         6746,
         4699,
         4452,
         6665,
         3209,
         7217,
         3974,
         5167,
         6708,
         4311,
         5803,
         5319,
         5280,
         6898,
         3960,
         5857,
         3792,
         6350,
         5911,
         4862,
         5997,
         7540,
         4661,
         6060,
         4739
         ])

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array([6798,
         2144,
         2327,
         2234,
         2779,
         3046,
         2824,
         2762,
         2857,
         2404,
         3236,
         2473,
         2517,
         2558,
         3065,
         3222,
         3235,
         4939])

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
plt.title("Data TLB access, read \n ARM Performance counter: DTLB_WALK \n Data TLB access with at least one translation table walk \n This includes each complete or partial translation table walk that causes an access to memory, including to data or translation table walk caches. \n Kmeans C program with Cluster size 3")

plt.xlabel("time in seconds")
plt.ylabel("DTLB walks")
# plt.plot(xpoints1, ypoints1)
plt.legend()
plt.show()