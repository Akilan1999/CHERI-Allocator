import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([78303,
       34734,
      129682,
       93214,
       59616,
      111134,
       75559,
       85767,
       96804,
       87956,
       83874,
       72777,
       80302,
       59289,
      105762,
       62793,
       78365,
       77091])

xpoints = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

ypoints1 = np.array([69789,
       98176,
       84635,
      120922,
       64256,
       76703,
       73646,
      113839,
       61033,
       77009,
       75661,
       93193,
      120468,
      106568,
       93912,
      151603,
      138165,
      22468])

xpoints1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

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