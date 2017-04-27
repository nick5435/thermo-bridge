import timeit
from itertools import permutations

import ThermoPyle as TP
import argparse
import pandas as pd


def make_Time(time):
    mins, secs = divmod(time, 60)
    hours, mins = divmod(mins, 60)
    return f"{int(hours)} hours, {int(mins)} minutes, {round(secs, 3)} seconds"


# d_vars = ["U", "T", "P", "S", "D", "G", "H"]
d_vars = ["U", "T", "P", "S", "D", "G"]
newCols = {f"d({z})/d({y})|{x}" for x, y, z in permutations(d_vars, 3)
           }.union(d_vars).difference({"T", "P", "U"}).union({"PHASE"})

newCols = list(newCols)
parser = argparse.ArgumentParser(description="Make some CSV goodness.")

parser.add_argument("--no-write", dest="write", action="store_false")
parser.add_argument("-N", metavar="maxcols", type=int,
                    dest="maxcols", action="store", default=len(newCols))
parser.set_defaults(write=True, maxcols=len(newCols))

args = parser.parse_args()

start = timeit.default_timer()
print("Iteration 0")
print(" " * 4 + "Generating Initial Fluid Object.")
print("======================================================")
gstart = timeit.default_timer()
try:
    myfluid = TP.ThermoFluid(fluid="Water", xvar="T",
                             yvar="P", zvar="U", numPoints=[217, 217])
    print(" " * 4 + "Success!")
except:
    print(" " * 4 + "Failed!")
    Exception("Cannot generate fluid, stopping")
gstop = timeit.default_timer()
print(" " * 4 + f"This Iteration: {make_Time(gstop-gstart)}")
print(" " * 4 + f"Time Elapsed: {make_Time(gstop-gstart)}\n")


print("")
numCols = min([len(newCols), args.maxcols])
itertimes = []
for i, col in enumerate(newCols[:numCols]):
    itertimes.append([timeit.default_timer(), 0, 0])
    print(f"Iteration {i+1} of {numCols}:")
    print(" " * 4 + f"Calculating Column {col}")
    print(
        "=" * (20 + max([4 + len(f"Calculating Column {col}"), len(f"Iteration {i+1} of {numCols}:")])))
    try:
        myfluid.add_column(col)
        print(" " * 4 + "Success!")
    except KeyboardInterrupt:
        raise KeyboardInterrupt("Program Interrupted by User. Stopping")
    except:
        print(" " * 4 + "Failed!")
        pass
    itertimes[-1][1] = timeit.default_timer()
    itertimes[-1][2] = itertimes[-1][1] - itertimes[-1][0]
    print(" " * 4 + f"This Iteration: {make_Time(itertimes[-1][2])}")
    print(" " * 4 + f"Time Elapsed: {make_Time(itertimes[-1][1]-start)}\n")


myfluid.data["V"] = pd.Series(myfluid.M / myfluid.data["D"], index=myfluid.data.index)
myfluid.refresh()
myfluid.clean()

if args.write:
    myfluid.write_data("finalData/", mode="dual",
                       filename="with_derivatives")

stop = timeit.default_timer()
total_time = stop - start

print(f"Total running time: {make_Time(total_time)}.\n")
