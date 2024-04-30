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

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array([3512147188,
    2931698338,
    3130637973,
    2799013235,
    3256184323,
    2992132432,
    3041359022,
    3094813437,
    3028071885,
    3380696386,
    3018331410,
    2899603552,
    3264907899,
    3002822837,
    3045671887,
    3119204499,
    2953573342,
    2963606839,
    2855193865,
    3043260399,
    2972252469,
    2503069946,
    2958386657,
    3033810534,
    3007362327,
    3026500873,
    3159826130,
    2504328570,
    4058464445,
    3218889301,
    3597912212,
    4181723542,
    3749432601,
    3654586898,
    3557679884,
    3322970044,
    3630597266,
    3130958213,
    1019981557])

xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

plt.plot(xpoints, ypoints,label='Malloc Physically contigous with bounds')
plt.plot(xpoints1, ypoints1,label='System memory allocator')

'''
L1D_TLB
The counter counts each Memory-read operation or Memory-write operation that causes a TLB
access to at least the Level 1 data or unified TLB.
Each access to a TLB entry is counted including multiple accesses caused by single instructions
such as LDM or STM.
'''
plt.title("Level 1 data TLB access, read \n ARM Performance counter: L1D_TLB_RD \n This counter counts each access counted by \n L1D_TLB that is a Memory-read operation. \n Kmeans C program with Cluster size 6")

plt.xlabel("time in seconds")
plt.ylabel("L1 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
plt.show()