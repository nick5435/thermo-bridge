import CoolProp
import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

FLUID = "Water"
NUM_POINTS = 250
COLORMAP = "nipy_spectral"


T = np.linspace(CP.PropsSI(FLUID, "TMIN") + 0.1,
                CP.PropsSI(FLUID, "TMAX") - 0.1, NUM_POINTS)
P = np.linspace(CP.PropsSI(FLUID, "PMIN") + 1000,
                CP.PropsSI(FLUID, "PMAX") - 1000, NUM_POINTS)


# S = CP.PropsSI("S", "T", T, "P", P, FLUID)

data = []

for t in T:
    for p in P:
        data.append([t, p * (10**-5) / 1000,
                     CP.PropsSI("S", "T", t, "P", p, FLUID)])
rawdata = np.asarray(data)
newdata = []
for i, s in enumerate(rawdata[:, 2]):
    if s > 0 and rawdata[i, 1] >= 10**-2 and rawdata[i, 0] > 0:
        newdata.append([rawdata[i, 0], rawdata[i, 1], rawdata[i, 2]])

# newdata = np.asarray(newdata)
frame = pd.DataFrame(newdata, columns=["T", "P", "S"])
# print(frame.head(5))
frame.to_csv("data/TPS.csv")

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.scatter(frame["T"], frame["P"], frame["S"], c=frame[
           "S"], cmap=COLORMAP, edgecolors="none")
# for T, V, S in zip(frame["T"],frame["P"], frame["S"]):
#     ax.scatter(T, V, S)

ax.set_xlabel("T")
ax.set_ylabel("P (kBar)")
ax.set_zlabel("S")
ax.set_title("T and P vs S")
plt.show()
