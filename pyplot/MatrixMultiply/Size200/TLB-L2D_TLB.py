import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])


ypoints = np.array([3013349,2946541])

xpoints = ["Malloc Physically contigous with bounds","System memory allocator"]

plt.bar(xpoints, ypoints)

'''
The counter counts each Memory-read operation or Memory-write operation that causes a 
TLB access to at least the Level 2 data or unified TLB.
Each access to a TLB entry is counted including refills 
of Level 1 TLBs.
The counter does not count the access if the access i
s due to a TLB maintenance instruction.
'''
# plt.title("Level 2 data TLB acces, read \n ARM Performance counter: L2D_TLB \n The counter counts each Memory-read operation or Memory-write operation that causes a TLB access to at least the Level 2 data or unified TLB. \n Matrix Multiply size 200")

plt.xlabel("time in seconds")
plt.ylabel("L2 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('l2_tlb_200_MatrixMultiply.png')