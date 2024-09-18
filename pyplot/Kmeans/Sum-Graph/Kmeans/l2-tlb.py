import matplotlib.pyplot as plt
import numpy as np

dim3_physically_contigous = np.array([78303,
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

dmin_3_physically_contigous = sum(dim3_physically_contigous)

dim3_regular = np.array([127978,
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

dmin_3_regular = sum(dim3_regular)

dim6_contigous = np.array([72589,
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

dim_6_contigous = sum(dim6_contigous)

dim6_regular = np.array([132941,
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

dim_6_regular = sum(dim6_regular)

dim40_contigous = np.array([int(x) for x in """66540
       7859
       23464
       43214
       27505
       27462
       46371
       10104
       65940
       26508
       18169
       33410
       35932
       31967
       61487
       22289
       61131
       49936
       8378
       70970
       64227
       45327
       14493
       8585
       34713
       62427
       27633
       49391
       28682
       21025
       30477
       19946
       34838
       53935
       51581
       19594
       17913
       33452
       57925
       78362
       9176
       43589
       57070
       23447
       28627
       17297
       54966
       59315
       52363
       50624
       26515
       31190
       106412
       35441
       10280
       21075
       9663
       78816
       48329
       48742
       40940
       40585
       33234
       71473
       21832
       66627
       18375
       18306
       34411
       56034
       24142
       74324
       34921
       10427
       65288
       17961
       30433
       17538
       33052
       63611
       15918
       8983
       47290
       30154
       68913
       30144
       68603
       16772
       76516
       31663
       50528
       36797
       27584
       74728
       9514
       16252
       34017
       39159
       73261
       34238
       9979
       100145
       30276
       32994
       26959
       37082
       82385
       34030
       65503
       24471
       22303
       9260
       24329
       69294
       34741
       23791
       43832
       50302
       98996
       45543
       35170
        9195
        9658
       63685
       21802
       39287
       35287
       8836
       113920
       38764
       23417
       41543
       11622
       45682
       57685
       53500
       13722
       11203
       22599
       92580
       40797
       56990
       81024
       9030
       45653
       65413
       17266
       59900
       33502
       10976
       28385
       33838
       61241
       29094
       36072
       146101
       8552
       30128
       51724
       24090""".replace('       ',',').replace('\n','').split(",")])

dim_40_contigous = sum(dim40_contigous)

dim40_regular = np.array([int(x) for x in """147309
       24207
       72608
       53185
       29916
       62288
       19733
       20551
       15416
       33266
       38374
       37710
       76787
       38460
       35339
       15569
       43172
       40743
       35956
       52172
       17231
       32107
       66245
       78219
       57454
       37971
       21077
       38089
       16171
       26842
       70623
       61517
       43946
       16101
       64700
       15876
       18604
       52025
       32854
       48066
      110412
       74894
       15982
       16951
       30104
       67263
       97568
       71199
       47570
       60400
      119246
       46025
       39649
       61263
       31674
       18139
       52567
      106665
       28508
       50885
       30868
       64452
       21987
      104550
       60096
       35098
       27626
       26791
       44735
       24076
       53037
       18897
       49820
       44744
       46927
       58569
       17651
       45036
       55358
       31643
       15816
       75636
       62402
       17341
       71459
       41987
       16640
       15786
       79108
       60482
       35872
       21016
       38518
       17325
       16738
       84271
       28477
       52976
       40236
       51622
       19197
       15498
       38114
       34553
       83946
      108452
       44795
       39454
       49442
       22963
       72816
       64652
       74099
       22675
       60850
       76929
       50585
       61838
       41130
       45360
       17933
       70220
       87695
       19565
       64806
       78487
       21187
       56748
       93777
       53159
       19220
       33799
       19743
       31416
       37750
       67563
       53070
       18014
       19133
       39304
       41509
       16661
       81493
       53422
       17376
       15742
       56450
       49720
       34734
       47112
       16915
       17586
       16895
       79737
       48293
       35941
       18742
       54320
       33438""".replace('    ',',').replace('\n','').split(",")])

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
categories = ['3 dimentions', '6 dimentions', '40 dimentions']
group_1 = [dmin_3_physically_contigous, dim_6_contigous, dim_40_contigous]
group_2 = [dmin_3_regular, dim_6_regular, dim_40_regular]

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
plt.xlabel('Number of dimentions COZ kmeans', fontweight='bold')
plt.xticks([r + bar_width for r in range(n)], categories)

# Add labels and title
plt.ylabel('DTLB L2 reads', fontweight='bold')
plt.title('Sum of DTLB L2 read')

# Add a legend
plt.legend()

# Show the plot
# plt.show()
plt.savefig('l2-tlb-kmeans.png')