import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([19636392729, 9856229208,9445728437,5148906386])
xpoints = np.array([5,10,15,20])

ypoints1 = np.array([10062197042, 9873241615,12034929886,5118684853])
xpoints1 = np.array([5,10,15,20])

plt.plot(xpoints, ypoints)
plt.plot(xpoints1, ypoints1)
plt.show()