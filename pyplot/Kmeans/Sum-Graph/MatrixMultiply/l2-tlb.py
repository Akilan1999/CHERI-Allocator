import matplotlib.pyplot as plt
import numpy as np

dim3_physically_contigous = np.array([3013349])

dmin_3_physically_contigous = sum(dim3_physically_contigous)

dim3_regular = np.array([2946541])

dmin_3_regular = sum(dim3_regular)

dim6_contigous = np.array([int(x) for x in """13933616 
   0
   0
   55855105
   177840659
   380285140
   292719568
   163746827""".replace('   ',',').replace('\n','').split(",")])

dim_6_contigous = sum(dim6_contigous)

dim6_regular = np.array([int(x) for x in """0
    0
    48672313
    0
    243876172
    332240431
    283300132
    151566198""".replace('    ',',').replace('\n','').split(",")])


dim_6_regular = sum(dim6_regular)

dim40_contigous = np.array([int(x) for x in """11074868
    17796846
    0
    42335753
    0
    42578037
    17369088
    0
    0
    0
    82499577
    0
    0
    0
    82928349
    19903822
    20322217
    20196113
    20575304
    19769508
    0
    40692176
    0
    35388820
    0
    46400139
    20884653
    0
    40479127
    20938047
    20020758
    21590212
    17955844
    1895112
    24707564
    35247723
    19854386
    19994871
    0
    0
    39958384
    39619071
    19821971
    0
    39754647
    0
    39873651
    19521815
    20209862
    20048932
    20231348
    20214678
    0
    41152963
    6223168
    16818928
    37877594
    12893970
    21214360
    0
    32124557
    20718531
    0
    40755758
    35334046
    0
    41293476
    20648826
    0
    20479335
    21645864
    28444433
    0
    34204784
    36576871
    0
    0
    0
    76911224
    20723929
    14021956
    28392009
    26330087
    0
    41195363
    9598203
    28499682
    0
    34404203
    29859217
    20539283
    20714755
    20553408
    0
    20889230
    32963850
    7949901
    33765967
    28019151
    13062566
    26967792
    0
    0
    62723768
    15030483
    20277594
    0
    41160435
    0
    28127160""".replace('    ',',').replace('\n','').split(",")])

dim_40_contigous = sum(dim40_contigous)

dim40_regular = np.array([int(x) for x in """2780755
   0
   40650126
   19973207
   0
   45212438
   14734736
   21512132
   20024828
   17015744
   21012868
   24889120
   0
   40307315
   0
   40543393
   19447333
   16752820
   19802564
   19717349
   0
   32838418
   7313016
   36828882
   19421922
   19221311
   0
   36504040
   19221867
   19111822
   4391041
   32495439
   0
   23803968
   18651515
   0
   37881224
   29985095
   4176134
   18086488
   18628963
   0
   0
   0
   77724802 
   0
   37326656
   0
   37118376
   17904262
   19199261
   19094655
   18162476
   19841950
   18493958
   19955899
   15237090
   18940111
   16777309
   19653443
   17616389
   1417668
   23258907
   0
   38260471
   22608071
   13460148
   19002183
   16931931
   19518969
   12655691
   18821392
   19084457
   0
   38850414
   0
   38673127
   0
   39578640
   0
   38841607
   0
   38340444
   0
   0
   59014396
   13524903
   19465492
   25539086
   19637297
   5254742
   27355676
   24079140
   19975996
   19226004
   16878651
   0
   0
   62518013
   0
   0
   39742980
   39872968
   18698312
   19633681
   19652322
   18131608
   0
   39807132
   84805863
   205063169
   207026601
   207353408
   208077229
   223112773
   232033395
   210898122
   200158459
   203639347
   230644673
   237184228
   230544844
   234041882
   225077016
   208652470
   206710725
   207688549
   208921986
   237145817
   216789158
   207248978
   206867158
   226521698
   243656316
   236022389
   216914633
   207163647
   207752568
   206269550
   207422862
   240605554
   220855937
   207420877
   210468984
   207768015
   250267485
   212878277
   209949240
   207411078
   208223656
   210492256
   224683374
   242489309
   231567088
   211246599
   208066123
   208277683
   228206741
   229508886
   207161109
   206156489
   214927236
   231786596
   232625811
   230571602
   209516467
   219150327
   228216552
   206438524
   220447351
   219045513
   230838177
   216657765
   205321014
   207699856
   219191131
   236171517
   225724156
   208329895
   210489462
   211206457
   207353005
   230789569
   231425162
   43897100""".replace('   ',',').replace('\n','').split(",")])

dim_40_regular = sum(dim40_regular)

# dimentions = ("3-dementions", "6-dementions", "40-dementions")
# comparitors = {
#     'FAT-Pointer based range address': (dmin_3_physically_contigous, dim_6_contigous, dim_40_contigous),
#     'System Allocator': (dmin_3_regular, dim_6_regular, dim_40_regular),
# }

# x = np.arange(len(dimentions))  # the label locations
# width = 0.25  # the width of the bars
# multiplier = 0

# fig, ax = plt.subplots(layout='constrained')

# for attribute, measurement in comparitors.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     ax.bar_label(rects, padding=3)
#     multiplier += 1

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('DTLB L1 reads')
# ax.set_title('L1D_TLB')
# ax.set_xticks(x + width, dimentions)
# ax.legend(loc='upper left', ncols=2)
# ax.set_ylim(0, 250)

# plt.show()

# Sample data
categories = ['Size 200', 'Size 10000']
group_1 = [dmin_3_physically_contigous, dim_6_contigous]
group_2 = [dmin_3_regular, dim_6_regular]

# Number of categories
n = len(categories)

# Create a bar width
bar_width = 0.25

# Create an array with the positions of the bars on the x-axis
r1 = np.arange(n)
r2 = [x + bar_width for x in r1]
# r3 = [x + bar_width for x in r2]

# Create the grouped bar graph
plt.bar(r1, group_1, color='b', width=bar_width, edgecolor='grey', label='FAT-Pointer based range based addresses')
plt.bar(r2, group_2, color='g', width=bar_width, edgecolor='grey', label='System memory allocator')
# plt.bar(r3, group_3, color='r', width=bar_width, edgecolor='grey', label='Group 3')

# Add xticks on the middle of the grouped bars
plt.xlabel('Size of Matrix COZ MatrixMultiply', fontweight='bold')
plt.xticks([r + bar_width for r in range(n)], categories)

# Add labels and title
plt.ylabel('DTLB L2 reads', fontweight='bold')
plt.title('Sum of DTLB L2 reads')

# Add a legend
plt.legend()

# Show the plot
# plt.show()
plt.savefig('l2-tlb-matrixmultiply.png')