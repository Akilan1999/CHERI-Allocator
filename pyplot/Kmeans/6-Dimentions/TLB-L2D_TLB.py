import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])


ypoints = np.array([72589,
      169120,
       35199,
       71459,
       55242,
       83325,
      144975,
       55231,
       73573,
      103593,
      122123,
       88845,
       99314,
       32081,
      130112,
      117455,
       73731,
       90279,
       93552,
      136261,
       35079,
       81254,
       93388,
       79594,
      173510,
       51158,
      140234,
       64106,
       45336,
      178182,
       38224,
      101736,
      104410,
       57382,
      141596,
       59233,
       84714,
       74438,
       55860])

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array([132941,
       85450,
       47978,
      100585,
      137429,
       65503,
       46820,
       57147,
       94444,
      112309,
       62289,
       91219,
       34585,
       89262,
       68500,
       77858,
       41711,
       53555,
       43719,
      122750,
       57234,
      139151,
       58964,
       85669,
       50914,
       75187,
       80292,
      126473,
      102653,
      104636,
      123366,
       79591,
       63819,
       55965,
      106456,
       34263,
      113263,
       71477])

xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

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
# plt.title("Level 2 data TLB acces, read \n ARM Performance counter: L2D_TLB \n The counter counts each Memory-read operation or Memory-write operation that causes a TLB access to at least the Level 2 data or unified TLB. \n Kmeans C program with Cluster size 6")

plt.xlabel("time in seconds")
plt.ylabel("L2 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('l2_tlb_6_dimentions.png')