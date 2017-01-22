# Thermodynamic Surface Generation in Python -- Physics Bridge
## Nick Meyer and Dr. Aaron Wangberg, Winona State University

## Why Python?

We chose to use **Python** as the main programming language for this project for several reasons.

### Libraries

Our primary concern for chosing a language of operation was the availiability of decent libraries suitable for handling large datasets, and interacting with such datasets. First, we needed a way to acquire data from NIST's REFPROP, which we did by way of [coolProp]. CoolProp allowed us to make requests for data, given certain inputs, in several different ways, which will be discussed later.

Next, we needed a way to store and manage the data inside of the program, that's where [Pandas] comes in. Pandas is based (in-part) on [NumPy], a highly efficient numerical computing library for Python. Pandas allows us to store our data in efficient n-dimensional arrays called `DataFrame`s, and access the data in them using their optimized methods. We also chose Pandas as it provides an easy way to generate CSV files from our DataFrames.

Then, we needed a way to visualize our data, to get a preiew of the surface before sending it off to be rendered. We chose the stock-standard library, [Matplotlib]. Matplotlib is easy-to-use, simply pass it three columns of a Pandas DataFrame, and it can produce a beautiful 3-D scatterplot of our data. Another reason we chose Matplotlib is its inclusion in [SageMath].

### Ease of Use

Python is a **_very_** easy to use language. There's no required typings, no pointers, and most importantly, **no compilation!** We believe that Python is easy enough to learn, that someone with minimal programming experience could learn Python in less than a month.

Python is more than just easy to use, it's enjoyable to use. Compared with languages like Java, C++, or Go, writing code in Python feels like writing down a recipie for a cookie, rather than writing instructions for how to assemble a cookie, atom by atom. Python's simple syntax and verbose error statements make it easy to figure out and debug your code. Python is also highly readable, as it prefers to use full words as its keywords, rather than archaic abbreviations. For example, compare Python's `print` to Java's `System.out.println`.

## Why CoolProp?

_Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum._

## Implementation & Use

_Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum._

## Future Work

_Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum._


## References

[SageMath]: http://sagemath.org "SageMath"
[CoolProp]: http://coolprop.org "CoolProp"
[Matplotlib]: http://matplotlib.org/ "Matplotlib"
[Pandas]: http://Pandas.pydata.org/ "Pandas"
[NumPy]: http://numpy.org "NumPy"

[flowchart] https://github.com/nick5435/thermo-bridge/raw/master/data_flow.png "Flowchart of Data for `thermoDataGrabber.py`"
[plot-TPS]: https://github.com/nick5435/thermo-bridge/raw/master/plots/TPS.png "Plot of Temperature, Pressure, and Entropy for Water"

Copyright (c) 2017 PhysicsBridge Project, All Rights Reserved.
