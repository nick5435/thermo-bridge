# Thermodynamic Surface Generation in Python -- Physics Bridge
Nick Meyer and Dr. Aaron Wangberg, Winona State University

## Problem
*   Realistic models for thermo systems
*   Physical models based on Real Data → Plastic surfaces
*   Once we have the data, we need to make a real surface → smooth, based on discrete data
*   ID Constraints, assumptions, what variables.

In most traditional undergraduate Thermodynamics courses, students are simply taught about Maxwell Relations, Partition Functions, Entropy, Enthalpy, and Heat. We often find that students' understanding of these concepts is extremely lacking, even if they understand the mathematics behind it all. Our goal with this project is to create realistic physical models, called _surfaces_, created using NIST data on thermodynamic systems.

To create these surfaces, we first need to obtain data. This is the main goal of this document, and the process for this is contained within.

To do this, we have made the following assumptions:

*   We will be modeling a fluid supported by [coolProp][]
*   We will be using x and y variables supported by [coolProp][]
*   The user is using [Python 3.6+.][Python]

## Why Python?

We chose to use **[Python][]** as the main programming language for this project for several reasons.

### Libraries

Our primary concern for chosing a language of operation was the availiability of decent libraries suitable for handling large datasets, and interacting with such datasets. First, we needed a way to acquire data from NIST's REFPROP, which we did by way of [coolProp][]. CoolProp allowed us to make requests for data, given certain inputs, in several different ways, which will be discussed later.

Next, we needed a way to store and manage the data inside of the program, that's where [Pandas][] comes in. Pandas is based (in-part) on [NumPy][], a highly efficient numerical computing library for Python. Pandas allows us to store our data in efficient n-dimensional arrays called `DataFrame`s, and access the data in them using their optimized methods. We also chose Pandas as it provides an easy way to generate CSV files from our DataFrames.

Then, we needed a way to visualize our data, to get a preiew of the surface before sending it off to be rendered. We chose the stock-standard library, [Matplotlib][]. Matplotlib is easy-to-use, simply pass it three columns of a Pandas DataFrame, and it can produce a beautiful 3-D scatterplot of our data. Another reason we chose Matplotlib is its inclusion in [SageMath][].

### Ease of Use

Python is a **_very_** easy to use language. There's no required typings, no pointers, and most importantly, **no compilation!** We believe that Python is easy enough to learn, that someone with minimal programming experience could learn Python in less than a month.

Python is more than just easy to use, it's enjoyable to use. Compared with languages like Java, C++, or Go, writing code in Python feels like writing down a recipie for a cookie, rather than writing instructions for how to assemble a cookie, atom by atom. Python's simple syntax and verbose error statements make it easy to figure out and debug your code. Python is also highly readable, as it prefers to use full words as its keywords, rather than archaic abbreviations. For example, compare Python's `print` to Java's `System.out.println`.

## Technical Requirements:

The following software and packages are required:

*   [Python 3][Python]
*   [CoolProp][]
*   [Matplotlib][]
*   [Numpy][]
*   [Pandas][]
*   [Sphinx][]
*   [sphinx_bootstrap_theme][]
*   [sphinx-autodoc-typehints][]
*   [Recommonmark][]
*   [Sphinx-Autobuild][]
*   [Typings][]
*   [Arrow][]
*   [Pyrsistent][]

All of these packages, save for Python itself, can be installed with `pip`.


### Data Cleaning

CoolProp, as simple to use as it may be, has its downsides. One of such downsides is that it will still produce data in unphysical regions, i.e. where $S\leq 0$ or where $U \lt 0$. To counteract this, we made the following choices:

* Only keep rows where `S > 0` (The Second Law)
* Only keep rows where `U > 0` (Need a Physical Regime)
* Only keep rows where `P-1 > P_min`, and likewise for `T`.

This final assumption was made to avoid regions where the derivatives are very steep, which would not have worked to create a physical surface.

## Future Work

Future work for this software would be to implement the functionality of CoolProp on our own, as CoolProp's lack of a Volume variable was hard to work around. We would also like to eventually work in regions that CoolProp could not, which includes the low-temperature limit and the high-pressure limit.


## References

1.  [Arrow][]
2.  [CoolProp][]
3.  [Matplotlib][]
4.  [NumPy][]
5.  [Pandas][]
6.  [Pyrsistent][]
7.  [Python][]
8.  [Recommonmark][]
9.  [Sphinx][]
10. [Sphinx-Autobuild][]
11. [sphinx-autodoc-typehints][]
12. [sphinx_bootstrap_theme]
13. [Typings][]



[Pyrsistent]: https://github.com/tobgu/pyrsistent
[Arrow]: http://crsmithdev.com/arrow/
[SageMath]: http://sagemath.org "SageMath"
[CoolProp]: http://coolprop.org "CoolProp"
[Matplotlib]: http://matplotlib.org/ "Matplotlib"
[Pandas]: http://Pandas.pydata.org/ "Pandas"
[NumPy]: http://numpy.org "NumPy"
[Recommonmark]: https://github.com/rtfd/recommonmark "Recommonmarl"
[Sphinx]: https://github.com/rtfd/recommonmark "Sphinx"
[Python]: https://python.org "Python"
[Sphinx-Autobuild]: https://github.com/GaretJax/sphinx-autobuild "Sphinx-Autobuild"
[Typings]: https://docs.python.org/3/library/typing.html "Typings"
[sphinx_bootstrap_theme]: http://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html "Sphinx Bootstrap Theme"
[sphinx-autodoc-typehints]: https://github.com/agronholm/sphinx-autodoc-typehints "Sphinx Autodoc Typehints"
