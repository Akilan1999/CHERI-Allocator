import matplotlib.pyplot as plt
import numpy as np

dim3_physically_contigous = np.array([3625,
         1016,
         1546,
         1556,
         1424,
         1382,
         1598,
         1544,
         1369,
         1301,
         1410,
         1415,
         1520,
         1291,
         1425,
         1653,
         1496,
         951])

dmin_3_physically_contigous = sum(dim3_physically_contigous)

dim3_regular = np.array([6798,
         2144,
         2327,
         2234,
         2779,
         3046,
         2824,
         2762,
         2857,
         2404,
         3236,
         2473,
         2517,
         2558,
         3065,
         3222,
         3235,
         4939])

dmin_3_regular = sum(dim3_regular)

dim6_contigous = np.array([12140,
         7054,
         3621,
         5391,
         6391,
         6235,
         4067,
         4433,
         5248,
         3321,
         4790,
         4832,
         5783,
         3709,
         6746,
         4699,
         4452,
         6665,
         3209,
         7217,
         3974,
         5167,
         6708,
         4311,
         5803,
         5319,
         5280,
         6898,
         3960,
         5857,
         3792,
         6350,
         5911,
         4862,
         5997,
         7540,
         4661,
         6060,
         4739
         ])

dim_6_contigous = sum(dim6_contigous)

dim6_regular = np.array([12300,
         8615,
         6314,
         6995,
         4796,
        10032,
         4414,
         8960,
         7265,
         8670,
         5075,
         8384,
         5986,
         8500,
         7639,
         8565,
         7414,
         5646,
         9956,
         4638,
         8766,
         5357,
        13762,
         6227,
        12425,
         7081,
        11306,
         8253,
         8411,
         6267,
        15571,
         5383,
        11586,
         8497,
        11189,
         7123,
         7342,
         6345,
         5933])

dim_6_regular = sum(dim6_regular)

dim40_contigous = np.array([int(x) for x in """32507
        4034
        27922
        22075
        45252
        6514
        45268
        20768
        78216
        5116
        4901
        24579
        30668
        4423
        12543
        16230
        20602
        23792
        29764
        35176
        22257
        21233
        22759
        41562
         5007
        40803
        15581
        18344
         4326
        25407
        37615
        25375
        19009
        43028
        31940
        25065
        20590
        3655
        39584
        11664
        16350
        18779
        3277
        5144
        26088
        10985
        25409
        38962
        19469
        11783
        24724
        18592
        31519
        18800
        10576
        33770
        11064
        71505
        8464
        4462
        22492
        33959
        4642
        34880
        4680
        32584
        4644
        16117
        21607
        4376
        4792
        30989
        18197
        13420
        27542
        21644
        22988
        41102
        37441
        34021
        13875
        17100
        43959
        10988
        25154
        32953
        18680
        11657
        37957
        18279
        26901
        36833
        10165
        15802
        23218
        4811
        26871
        22496
        12986
        24293
        16020
        37425
        17160
        5464
        54857
        37666
        30590
        4896
        4561
        17568
        15857
        4497
        33919
        11669
        19176
        53357
        12422
        13431
        21433
        4551
        20220
        11167
        4747
        7006
        24694
        24494
        52551
        11999
        80094
        18621
        9625
        19697
        18924
        5664
        39953
        5258
        9940
        21864
        4681
        60347
        4316
        18867
        17767
        18939
        13191
        15379
        4516
        15721
        19535
        19272
        44248
        18811
        21077
        54181
        29909
        32954
        12046
        17235
        37583
        15340""".replace('        ',',').replace('\n','').split(",")])

dim_40_contigous = sum(dim40_contigous)

dim40_regular = np.array([int(x) for x in """37838
        4375
        4755
        13395
        4663
        17351
        35495
        41361
        14851
        3678
        9728
        7058
        18282
        34639
        31071
        4249
        20021
        3460
        14453
        12527
        21730
        39797
        40936
        3952
        3572
        35124
        3157
        24017
        17363
        14283
        41690
        3627
        30967
        10083
        17288
        8446
        18369
        12531
        15990
        22124
        63165
        11521
        18297
        30464
        26297
        4068
        5461
        62879
        4968
        25299
        50562
        4084
        4528
        4962
        59035
        4958
        21144
        35628
        4261
        4349
        14859
        36841
        8263
        17753
        12513
        15457
        18778
        4148
        25284
        18899
        28869
        16736
        26025
        7030
        4598
        13422
        14592
        14660
        26539
        23846
        22503
        3771
        8567
        31149
        7480
        19305
        10491
        4415
        20470
        15658
        17870
        11822
        19760
        22506
        17256
        18958
        18275
        26096
        3780
        20019
        44296
        27396
        13735
        24572
        12058
        4065
        13409
        18858
        63139
        41617
        4256
        16795
        69961
        8029
        22993
        82166
        3994
        4724
        5504
        28454
        17037
        29973
        41238
        18465
        9060
        4665
        34217
        5250
        41130
        36820
        16737
        4086
        21270
        55031
        3988
        25838
        26389
        38865
        6083
        23834
        34979
        3616
        15021
        4614
        25599
        18673
        4572
        18720
        4562
        38451
        19787
        32943
        4457
        4577
        10062
        34287
        7733
        21443
        21917""".replace('        ',',').replace('\n','').split(",")])

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
plt.ylabel('DTLB walks', fontweight='bold')
plt.title('Sum of DTLB walks')

# Add a legend
plt.legend()

# Show the plot
# plt.show()

plt.savefig('tlb-walk-kmeans.png')