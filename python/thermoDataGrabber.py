import CoolProp
import CoolProp.CoolProp as CP
# CoolProp is for getting the thermo data
import matplotlib.pyplot as plt
#
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# FLUID: What fluid do we want to use?
# NUM_POINTS: How many gradations are in each linspace
# COLORMAP: What color map should MPL use?


FLUID = "Water"
NUM_POINTS = 250
COLORMAP = "nipy_spectral"


T = np.linspace(CP.PropsSI(FLUID, "TMIN") + 0.1,
                CP.PropsSI(FLUID, "TMAX") - 0.1, NUM_POINTS)  # Linear interpolation between tmin and tmax with NUM_POINTS number of points, delta = max-min/NUM_POINTS
P = np.linspace(CP.PropsSI(FLUID, "PMIN") + 1000,
                CP.PropsSI(FLUID, "PMAX") - 1000, NUM_POINTS)  # Linear interpolation between pmin and pmax with NUM_POINTS number of points, delta = max-min/NUM_POINTS

data = []  # Create a empty list for storing data

for t in T:
    for p in P:
        data.append([t, p * (10**-5) / 1000,
                     CP.PropsSI("S", "T", t, "P", p, FLUID)])
rawdata = np.asarray(data)  # rawdata is the numpy array for our data, faster!
newdata = []  # Create a empty list for storing data
# we iterate over our array, getting our Z data and its index
for i, s in enumerate(rawdata[:, 2]):
    # make sure Z>0, X, Y are allowed values
    if s > 0 and rawdata[i, 1] >= 10**-2 and rawdata[i, 0] > 0:
        newdata.append([rawdata[i, 0], rawdata[i, 1], rawdata[i, 2]])

# frame is a pandas data frame (nice access to our data, named columns,
# etc.) with our good data
frame = pd.DataFrame(newdata, columns=["T", "P", "S"])
# print(frame.head(5)) # get the first 5 datapoints
frame.to_csv("data/TPS.csv")  # save our data to the data folder


# Plotting:
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")  # we want 3D plots
ax.scatter(frame["T"], frame["P"], frame["S"], c=frame[
           "S"], cmap=COLORMAP, edgecolors="none")  # Plot the data
# Set the Labels
ax.set_xlabel("T")
ax.set_ylabel("P (kBar)")
ax.set_zlabel("S")
ax.set_title("T and P vs S")
plt.show()
