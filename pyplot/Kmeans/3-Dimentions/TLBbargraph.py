import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([1944100892,
    1929198745,
    2147407618,
    2361683504,
    2229290045,
    1936107919,
    1950196981,
    2316564611,
    2415777784,
    2251930639,
    1917048962,
    2122919883,
    2305445935,
    2216085132,
    2061970506,
    2077573288,
    2415427574])

xpoints = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

ypoints1 = np.array([2001205195,
    2037350408,
    2077998800,
    2064361816,
    2370004326,
    2366505116,
    2433485997,
    2388982491,
    2622710065,
    2231849577,
    2213896383,
    1971144730,
    2279336623,
    2384236727,
    2159066740,
    1872922315,
    2046840068])

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
# plt.title("Level 1 data TLB access, read \n ARM Performance counter: L1D_TLB_RD \n This counter counts each access counted by \n L1D_TLB that is a Memory-read operation. \n Kmeans C program with Cluster size 3")

plt.xlabel("time in seconds")
plt.ylabel("L1 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('l1_tlb_kmeans_3_dimentions.png')