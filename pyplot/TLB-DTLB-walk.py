import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([3625,
         1016,
         1546,
         1556,
         1424,
         1382,
         1598,
         1544,
         1369,
         1301,
         1410,
         1415,
         1520,
         1291,
         1425,
         1653,
         1496,
         951])

xpoints = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

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

xpoints1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

plt.plot(xpoints, ypoints,label='Malloc Physically contigous with bounds')
plt.plot(xpoints1, ypoints1,label='System memory allocator')

'''
L1D_TLB
The counter counts each Memory-read operation or Memory-write operation that causes a TLB
access to at least the Level 1 data or unified TLB.
Each access to a TLB entry is counted including multiple accesses caused by single instructions
such as LDM or STM.
'''
plt.title("DTLB walk access, read \n ARM Performance counter: L1D_TLB_RD \n This counter counts each access counted by \n L1D_TLB that is a Memory-read operation. \n Kmeans C program with Cluster size 3")

plt.xlabel("time in seconds")
plt.ylabel("L1 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
plt.show()