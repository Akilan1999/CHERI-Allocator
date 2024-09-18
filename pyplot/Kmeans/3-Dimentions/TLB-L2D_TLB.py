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

ypoints1 = np.array([127978,
       79046,
       67101,
       99081,
      186824,
      111734,
      120426,
       65293,
      112589,
      113350,
      110875,
       74596,
       86142,
       77054,
      106211,
      133301,
      109764,
      68751])

xpoints1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])

plt.plot(xpoints, ypoints,label='Malloc Physically contigous with bounds')
plt.plot(xpoints1, ypoints1,label='System memory allocator')

'''
DTLB_WALK
The counter counts each Memory-read operation or Memory-write operation that causes a 
TLB access to at least the Level 2 data or unified TLB.
Each access to a TLB entry is counted including refills 
of Level 1 TLBs.
The counter does not count the access if the access i
s due to a TLB maintenance instruction.
'''
# plt.title("Level 2 data TLB acces, read \n ARM Performance counter: L2D_TLB \n The counter counts each Memory-read operation or Memory-write operation that causes a TLB access to at least the Level 2 data or unified TLB. \n Kmeans C program with Cluster size 3")

plt.xlabel("time in seconds")
plt.ylabel("L2 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('l2_tlb_kmeans_3_dimentions.png')