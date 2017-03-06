import timeit
from itertools import permutations

import ThermoPyle as TP


def make_Time(time):
    mins, secs = divmod(time, 60)
    hours, mins = divmod(mins, 60)
    return f"{int(hours)} hours, {int(mins)} minutes, {round(secs, 3)} seconds"


start = timeit.default_timer()
myfluid = TP.ThermoFluid("Water", "T", "P", "U", [216, 216])

d_vars = ["U", "T", "P", "S", "D", "G"]
newCols = {f"d({z})/d({y})|{x}" for x, y, z in permutations(d_vars, 3)
           }.union(d_vars).difference(set(myfluid.vars))

newCols = newCols.union({"PHASE"})

print("")
for i, col in enumerate(list(newCols)):
    istart = timeit.default_timer()
    print(f"Iteration {i+1} of {len(newCols)}:")
    print(" " * 4 + f"Calculating Column {col}")
    print(
        "=" * (20 + max([4 + len(f"Calculating Column {col}"), len(f"Iteration {i+1} of {len(newCols)}:")])))
    try:
        myfluid.add_column(col)
        print(" " * 4 + "Success!")
    except KeyboardInterrupt:
        raise KeyboardInterrupt("Program Interrupted by User. Stopping")
    except:
        print(" " * 4 + "Failed!")
        pass
    istop = timeit.default_timer()
    print(" " * 4 + f"Time: {make_Time(istop-istart)}")
    print(" " * 4 + f"Time Elapsed: {make_Time(istop-start)}\n")

# For Debugging:
# print(newCols)
# for col in newCols:
#     print(
#         f"Calculating Column {col}\n{'='*len(f'Calculating Column {col}')}\n")
#     myfluid.add_column(col)
#     print("\n")


myfluid.clean()
myfluid.write_data("finalData/", mode="dual", filename="with_derivatives")

stop = timeit.default_timer()
total_time = stop - start

print(f"Total running time: {make_Time(total_time)}.\n")
