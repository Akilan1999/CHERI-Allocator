import matplotlib.pyplot as plt
import numpy as np

dim3_physically_contigous = np.array([92265])

dmin_3_physically_contigous = sum(dim3_physically_contigous)

dim3_regular = np.array([94650])

dmin_3_regular = sum(dim3_regular)

dim6_contigous = np.array(np.array([int(x) for x in """0
              0
              202420
              108748
              7366843
              12350564
              13586069
              6779734
              56950""".replace('              ',',').replace('\n','').split(",")]))

dim_6_contigous = sum(dim6_contigous)

dim6_regular = np.array(np.array([int(x) for x in """105883
            0
            135218
            0
            8322082
            12700590
            12017926
            6160362
            134527""".replace('            ',',').replace('\n','').split(",")]))
dim_6_regular = sum(dim6_regular)

dim40_contigous = np.array([int(x) for x in """0
    0
    4417755799
    0
    2587126745
    0
    1907452696
    0
    4470211896
    1490535856
    1488268722
    1492406027
    0
    0
    3020774732
    1502998186
    1495229685
    1513519294
    2943026264
    1500269058
    52149259
    1496657426
    2937658244
    1494297672
    74030192
    1501455826
    1495883230
    2888428091
    1482110806
    150844250
    2836859365
    0
    2995913912
    0
    2986402746
    0
    1637257243
    2848563352
    336366333
    0
    2955346561
    1582901866
    1494805041
    1486848958
    1575414883
    0
    3006540619
    1651961484
    1495211562
    1418961073
    2413046393
    0
    2310831892
    1545685148
    1494591413
    1494394190
    1495772460
    1497140001
    1506995279
    1502064624
    1503212470
    1494161247
    1496442614
    1494353921
    1496910315
    1490640984
    2120990326
    1496964537
    1503480472
    0
    2487680099
    1511772203
    1990506585
    1085
    1495006176
    2981033808
    1497807398
    1499905019
    0
    2992809338
    1499678220
    1503422919
    1432738350
    1572013300
    1488687745
    1491956406
    1493056793
    1490487590
    1494885596
    0
    2981312602
    1495995022
    1494473531
    91287100
    2756251323
    230008646
    1491190180
    1430538651
    1583249575
    1576908184
    1332064486
    0
    3175178358
    0
    3080574208
    2649916724
    1275899646
    0
    2878955633""".replace('    ',',').replace('\n','').split(",")])

dim_40_contigous = sum(dim40_contigous)

dim40_regular = np.array([int(x) for x in """0
    2873345808
    0
    0
    4568364039
    0
    2962578326
    1482026881
    1482959662
    1283314470
    1696338408
    1493064117
    1496278352
    1493690192
    1490808431
    1482241102
    1485073059
    1493488736
    1493734395
    1494051944
    1491925626
    1490400073
    1492918850
    0
    2989795422
    0
    2981131303
    1490971079
    1490457922
    0
    2972098981
    148614774
    0
    0
    4865632909
    1257951927
    1588161938
    1785512571
    0
    0
    0
    6770405012
    0
    2348949300
    0
    0
    4570645310
    0
    2824636217
    1762646952
    0
    2891891542
    1579360612
    0
    0
    4915926092
    1496744037
    1495870886
    1497206544
    1287107800
    0
    3203518565
    0
    2992849786
    0
    2975114733
    1481666721
    686803
    2988542677
    1496054096
    1496578264
    1491746836
    1492851059
    1497143785
    1495192565
    1500194130
    0
    1637919784
    2854243731
    0
    2366222238
    2128844017
    0
    1818736204
    2676149826
    1497854865
    962431460
    0
    3539793686
    1024018613
    1489816277
    0
    3158434789
    1369912046
    1491311601
    1575013089
    0
    0
    4446661541
    1416884482
    1710611180
    1757241245
    1233889541
    1437873524
    0
    3280246404
    0
    2995489571
    1541069762
    3930514690
    3863607919
    3597368896
    3734892809
    3944232184
    3709601722
    3642560210
    3625597517
    3920215743
    3927141046
    4000023820
    3916655686
    3951797607
    3952120224
    3689180680
    3587372425
    3615616989
    3726388814
    3929746604
    3929801334
    3942019114
    3648646073
    3944755905
    3929255746
    3668055728
    3672894376
    3844013718
    3910779810
    3940544740
    4006830187
    3928198267
    3531412165
    3818215173
    3738150454
    3604332393
    3650311511
    3807369864
    3826302554
    3775371186
    3710423568
    3934761097
    3925844952
    3602607914
    3741857686
    3732482931
    3729783593
    3635250094
    3706648118
    3853167484
    3916845229
    3983629794
    3943670196
    3867725730
    3548946522
    3696888472
    3729664873
    3750609657
    3702688827
    3994465571
    3666995886
    3881628312
    3720334387
    3933568515
    3693178186
    3888954122
    3961471376
    3937112215
    3936691623
    3915403037
    3693727226
    3917170944
    3930555435
    3933184551
    3931662845
    3940295083
    1033014609""".replace('    ',',').replace('\n','').split(",")])

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
plt.ylabel('DTLB L1 reads', fontweight='bold')
plt.title('Sum of DTLB L1 reads')

# Add a legend
plt.legend()

# Show the plot
# plt.show()
plt.savefig('l1-miss-matrixmultiply.png')