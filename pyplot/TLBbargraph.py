import matplotlib.pyplot as plt
import numpy as np

# ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
# xpoints = np.array([5,10,15,20])

# ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
# xpoints1 = np.array([5,10,15,20])

ypoints = np.array([1944100892,
    1929198745,
    2147407618,
    2361683504,
    2229290045,
    1936107919,
    1950196981,
    2316564611,
    2415777784,
    2251930639,
    1917048962,
    2122919883,
    2305445935,
    2216085132,
    2061970506,
    2077573288,
    2415427574])

xpoints = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])

plt.plot(xpoints, ypoints)
# plt.plot(xpoints1, ypoints1)
plt.show()