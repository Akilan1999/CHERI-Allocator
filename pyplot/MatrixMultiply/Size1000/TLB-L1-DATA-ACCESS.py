import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([int(x) for x in """0
    0
    3182857841
    2676269451
    3632836262
    5086931936
    4921595689
    2380537223""".replace('    ',',').replace('\n','').split(",")])

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array([int(x) for x in """0
    1662045387
    2568704269
    0
    5404906944
    4946152426
    5097512016
    1934071481""".replace('    ',',').replace('\n','').split(",")])

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
# plt.title("Level 1 data TLB access, read \n ARM Performance counter: L1D_TLB_RD \n This counter counts each access counted by \n L1D_TLB that is a Memory-read operation. \n Matrix multiply size 1000")

plt.xlabel("time in seconds")
plt.ylabel("L1 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('l1_data_1000_MatrixMultiply.png')