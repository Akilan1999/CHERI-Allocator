import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([int(x) for x in """32507
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

xpoints = np.array([(i) for i, x in enumerate(ypoints, 1)])

ypoints1 = np.array([int(x) for x in """37838
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

xpoints1 = np.array([(i) for i, x in enumerate(ypoints1, 1)])

plt.plot(xpoints, ypoints,label='Malloc Physically contigous with bounds')
plt.plot(xpoints1, ypoints1,label='System memory allocator')

'''
DTLB_WALK
The counter counts each access counted by L1D_TLB that causes a 
refill of a data or unified 
TLB involving at least one translation table walk access.
This includes each complete or partial translation table walk that causes an 
access to memory, including to data or translation table walk caches.
If Armv8.7 is not implemented, it is IMPLEMENTATION DEFINED whether accesses 
that cause an update of an existing TLB entry involving at least one translation 
table walk access are counted. If Armv8.7 is implemented, these accesses 
are counted.
'''
# plt.title("Data TLB access, read \n ARM Performance counter: DTLB_WALK \n Data TLB access with at least one translation table walk \n This includes each complete or partial translation table walk that causes an access to memory, including to data or translation table walk caches. \n Kmeans C program with Cluster size 40")

plt.xlabel("time in seconds")
plt.ylabel("DTLB walks")
# plt.plot(xpoints1, ypoints1)
plt.legend()
# plt.show()

plt.savefig('d_tlb_walk_40_dimentions.png')