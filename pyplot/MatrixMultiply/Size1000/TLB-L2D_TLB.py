import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])


ypoints = np.array([int(x) for x in """13933616 
   0
   0
   55855105
   177840659
   380285140
   292719568
   163746827""".replace('   ',',').replace('\n','').split(",")])

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array([int(x) for x in """0
    0
    48672313
    0
    243876172
    332240431
    283300132
    151566198""".replace('    ',',').replace('\n','').split(",")])

xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

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
# plt.title("Level 2 data TLB acces, read \n ARM Performance counter: L2D_TLB \n The counter counts each Memory-read operation or Memory-write operation that causes a TLB access to at least the Level 2 data or unified TLB. \n Matrix multiply size 1000")

plt.xlabel("time in seconds")
plt.ylabel("L2 DTLB reads")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('l2_tlb_1000_MatrixMultiply.png')