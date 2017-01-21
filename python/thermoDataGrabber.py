"""
.. module:: thermoDataGrabber
    :platform: Unix, Windows
    :synopsis: A standalone version of the genericDataGrabber library.

.. moduleauthor:: Nick Meyer <nmeyer5435@gmail.com>


"""
# CoolProp is for getting the thermo data
import CoolProp
import CoolProp.CoolProp as CP
# Matplotlib for making pretty pictures
import matplotlib.pyplot as plt
# Data Storage Containers
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# FLUID: What fluid do we want to use?
# NUM_POINTS: How many gradations are in each linspace
# COLORMAP: What color map should MPL use?


FLUID = "Water"
NUM_POINTS = 250
COLORMAP = "nipy_spectral"

# Linear interpolation between tmin and tmax with NUM_POINTS number of
# points, delta = tmax-min/NUM_POINTS
T = np.linspace(CP.PropsSI("TMIN", FLUID) + 0.1,
                CP.PropsSI("TMAX", FLUID) - 0.1, NUM_POINTS)

# Linear interpolation between pmin and pmax with NUM_POINTS number of
# points, delta = max-min/NUM_POINTS
P = np.linspace(CP.PropsSI("PMIN", FLUID) + 1000,
                CP.PropsSI("PMAX", FLUID) - 1000, NUM_POINTS)

# Create a empty list for storing data
# Then make our data.
data = []

for t in T:
    for p in P:
        data.append([t, p * (10**-5) / 1000,
                     CP.PropsSI("S", "T", t, "P", p, FLUID)])

# rawdata is the numpy array for our data, faster!
# Then create an empty list for storing our data
rawdata = np.asarray(data)
newdata = []

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
