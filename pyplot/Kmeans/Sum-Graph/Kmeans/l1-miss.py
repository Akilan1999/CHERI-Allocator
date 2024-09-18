import matplotlib.pyplot as plt
import numpy as np

dim3_physically_contigous = np.array(np.array([int(x) for x in """836772
              495429
              446419
              366613
              397234
              505776
              356928
              449455
              480582
              427964
              400058
              420493
              452870
              499538
              419145
              443761
              417189
              370320""".replace('              ',',').replace('\n','').split(",")]))

dmin_3_physically_contigous = sum(dim3_physically_contigous)

dim3_regular = np.array(np.array([int(x) for x in """723197
              556124
              352857
              538444
              628566
              751980
              602713
              550526
              530137
              529691
              430821
              390686
              418356
              520712
              515506
              676283
              659655
              523928""".replace('              ',',').replace('\n','').split(",")]))

dmin_3_regular = sum(dim3_regular)

dim6_contigous = np.array(np.array([int(x) for x in """742051
              559499
              372615
              383619
              428808
              336756
              518580
              390112
              375579
              421849
              381810
              384743
              469525
              421909
              487489
              337821
              469539
              366665
              469249
              509121
              430155
              375011
              462737
              530009
              481996
              427822
              356143
              528752
              542248
              493358
              479450
              425282
              517723
              426863
              540465
              466203
              456952
              499337
              538226""".replace('              ',',').replace('\n','').split(",")]))

dim_6_contigous = sum(dim6_contigous)

dim6_regular = np.array(np.array([int(x) for x in """736765
              531488
              423974
              374492
              554088
              388215
              374805
              519748
              474860
              534621
              535391
              631809
              496852
              509826
              519247
              471033
              508710
              525277
              501897
              394173
              493662
              375646
              431544
              382177
              630827
              452712
              556464
              510118
              534303
              550329
              574236
              479424
              575782
              428647
              508028
              475290
              491714
              462188
              294159""".replace('              ',',').replace('\n','').split(",")]))

dim_6_regular = sum(dim6_regular)

dim40_contigous = np.array(np.array([int(x) for x in """1147403
              829036
              563124
              979733
              683541
              618378
              905917
              561979
              902313
              823260
              499959
              627898
              915499
              646610
              739437
              945235
              541299
              637887
              842954
              703414
              1291380
              675118
              671111
              585563
              585483
              951820
              791179
              701760
              552971
              696260
              902072
              815292
              826315
              740385
              805546
              736227
              690416
              769363
              825820
              1027783
              797795
              863187
              834350
              548714
              759409
              667769
              840026
              861216
              895136
              719523
              504731
              959369
              1052167
              668707
              558918
              778832
              681806
              1268380
              825940
              874677
              670802
              808349
              653938
              996132
              769110
              1077410
              714249
              660753
              551064
              867647
              556815
              687308
              780915
              604863
              936983
              818984
              697969
              1063845
              722724
              864795
              791971
              489493
              678041
              514280
              784758
              643920
              896146
              567640
              854350
              548957
              583866
              880357
              589791
              604616
              560377
              527240
              673535
              503032
              851726
              484139
              649485
              978010
              641704
              488143
              710347
              808049
              1035491
              695389
              441112
              929079
              622864
              516002
              902311
              783120
              687561
              687898
              525210
              731349
              1332534
              537479
              542351
              511237
              564299
              859176
              713889
              901452
              631327
              681258
              1035948
              634997
              455623
              851931
              612646
              902292
              787158
              660371
              791336
              702494
              644624
              764093
              946863
              984181
              666091
              571202
              590691
              1160676
              624435
              677302
              491699
              870564
              1096683
              701710
              767120
              886663
              847346
              726936
              828216
              731833
              1143815
              893945
              446303""".replace('              ',',').replace('\n','').split(",")]))

dim_40_contigous = sum(dim40_contigous)

dim40_regular = np.array(np.array([int(x) for x in """1603321
              906001
              831508
              1260778
              874222
              639952
              811423
              876933
              871938
              845695
              811517
              1078035
              1155039
              931630
              734393
              1040144
              897608
              567688
              1017724
              816640
              1156306
              1182610
              2087536
              935131
              564650
              781929
              1032678
              842187
              714283
              1512066
              903441
              821687
              750216
              1623056
              1113602
              602318
              1056833
              829348
              924366
              917254
              1417581
              1056215
              534696
              957581
              873314
              615740
              793892
              1166512
              508943
              509190
              656245
              1304353
              909374
              638685
              1848084
              1067142
              543667
              591408
              1215657
              952755
              1191746
              1779363
              780965
              966607
              618025
              1082331
              1177658
              1136390
              1914232
              570957
              846572
              577331
              1232137
              1037267
              1262158
              1029892
              1122356
              995490
              1174365
              1340139
              1097573
              621145
              649356
              1082100
              792184
              1046410
              1217530
              952589
              634895
              866331
              1560533
              870354
              692937
              1249514
              731255
              899044
              1132861
              871474
              1440239
              1109188
              915075
              1625844
              811510
              845837
              680654
              1527778
              556130
              761597
              1452068
              856231
              729522
              670614
              1449778
              554624
              965716
              1030135
              1018319
              609395
              630688
              1379329
              674255
              808523
              1098093
              1502941
              689121
              901665
              1173878
              637713
              756162
              988917
              959839
              581439
              618517
              1482465
              539794
              982852
              878227
              1259422
              774118
              667883
              1238176
              1393325
              721119
              1185418
              1324310
              605043
              1029433
              1029119
              582207
              1028124
              844517
              1594356
              1175972
              910822
              660335
              973991
              1048600
              521274
              1771930""".replace('              ',',').replace('\n','').split(",")]))

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
plt.ylabel('L1 cache miss', fontweight='bold')
plt.title('Sum of L1 cache misses')

# Add a legend
plt.legend()

# Show the plot
# plt.show()
plt.savefig('l1-miss-kmeans.png')