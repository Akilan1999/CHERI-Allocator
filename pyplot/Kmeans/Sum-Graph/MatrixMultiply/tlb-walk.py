import matplotlib.pyplot as plt
import numpy as np

dim3_physically_contigous = np.array([26005])

dmin_3_physically_contigous = sum(dim3_physically_contigous)

dim3_regular = np.array([8517])

dmin_3_regular = sum(dim3_regular)

dim6_contigous = np.array([int(x) for x in """0
       2722
       0
       0
       84290
       185921
       251521
       356452""".replace('       ',',').replace('\n','').split(",")])

dim_6_contigous = sum(dim6_contigous)

dim6_regular = np.array([int(x) for x in """1310
       1658
       86
       0
       73097
       171472
       237158
       161478""".replace('       ',',').replace('\n','').split(",")])


dim_6_regular = sum(dim6_regular)

dim40_contigous = np.array([int(x) for x in """1072
         1566
         0
         775
         564
         574
         0
         0
         1842
         397
         832
         0
         1143
         0
         1132
         0
         0
         3478
         335
         1181
         0
         1451
         0
         0
         2456
         914
         566
         208
         1323
         0
         1341
         0
         0
         0
         2800
         869
         0
         1624
         852
         0
         1444
         78
         0
         1165
         242
         0
         0
         1436
         0
         1656
         1295
         672
         0
         2124
         689
         247
         974
         196
         664
         0
         0
         0
         0
         4571
         411
         1108
         0
         1855
         779
         0
         0
         0
         3973
         0
         0
         2126
         1090
         0
         0
         0
         1455
         868
         834
         0
         2252
         743
         0
         0
         0
         2867
         576
         528
         737
         1279
         753
         0
         0
         1469
         709
         0
         951
         1011
         560
         923
         389
         681
         887
         0
         1091""".replace('         ',',').replace('\n','').split(",")])
dim_40_contigous = sum(dim40_contigous)

dim40_regular = np.array([int(x) for x in """2077
    0
    2240
    974
    400
    0
    1949
    0
    353
    0
    2136
    1292
    1150
    1080
    1029
    188
    16
    9401
    3108
    0
    12850
    2972
    0
    13417
    4015
    0
    0
    12179
    708
    4434
    5515
    105
    0
    0
    52251
    8327
    0
    0
    0
    7628
    0
    6047
    2796
    2505
    1949
    0
    0
    0
    0
    14301
    0
    5171
    3362
    3772
    0
    27162
    15974
    5284
    11553
    0
    24698
    0
    14835
    0
    21593
    664
    5721
    12945
    0
    13774
    0
    14722
    1465
    0
    27655
    2332
    4084
    33813
    0
    9790
    0
    50326
    5316
    0
    0
    0
    0
    9760
    4192
    1552
    7241
    3216
    4888
    8667
    28500
    8415
    4523
    1449
    4652
    0
    7625
    0
    13775
    0
    1897
    4708
    0
    12225
    4482759
    191711306
    235410343
    173845602
    242711520
    154862574
    192747518
    220667551
    275602208
    184073481
    198073425
    227482742
    187971748
    183689903
    187178845
    186674013
    207741123
    233177167
    221368814
    183933427
    181175654
    204068107
    228269124
    205027178
    209400883
    187840131
    188293011
    221927087
    232807458
    188215220
    180783387
    216711542
    208036998
    214266374
    186414281
    180185139
    185237868
    191677316
    183911791
    183803795
    224964126
    204113022
    210381502
    225585571
    220223453
    226214857
    204932647
    184864540
    217262003
    202414930
    191948700
    193400960
    181280109
    180323521
    184002482
    207777617
    222940234
    189422853
    186182495
    186261124
    181304280
    192816961
    184117119
    209667712
    240951856
    219942014
    221564848
    192926621
    181690338
    183097907
    186087016
    184347616
    180377265
    199009737
    182802614""".replace('    ',',').replace('\n','').split(",")])

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
plt.savefig('tlb-walk-matrixmultiply.png')