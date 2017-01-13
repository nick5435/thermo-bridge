import CoolProp
import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt
import matplotlib.ticker
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

FLUID = "Water"
NUM_POINTS = 250


T = np.linspace(CP.PropsSI(FLUID, "TMIN") + 0.1,
                CP.PropsSI(FLUID, "TMAX") - 0.1, NUM_POINTS)
P = np.linspace(CP.PropsSI(FLUID, "PMIN") + 1,
                CP.PropsSI(FLUID, "PMAX") - 1, NUM_POINTS)


# S = CP.PropsSI("S", "T", T, "P", P, FLUID)

data = []

for t in T:
    for p in P:
        data.append([t, p, CP.PropsSI("S", "T", t, "P", p, FLUID)])
rawdata = np.asarray(data)

newdata = []
for i, s in enumerate(rawdata[:, 2]):
    if s > 0:
        newdata.append([rawdata[i, 0], rawdata[i, 1], np.log10(rawdata[i, 2])])

newdata = np.asarray(newdata)
frame = pd.DataFrame(newdata, columns=['T', 'P', 'S'])

frame.to_CSV("data/TPS.csv")