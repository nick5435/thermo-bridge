"""
.. module:: thermoDataGrabber
    :platform: Unix, Windows
    :synopsis: Uses CoolProp to access thermodynamic data about Fluids.

.. moduleauthor:: Nick Meyer <nmeyer5435@gmail.com>
"""

import copy
import json

import CoolProp.CoolProp as CP
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyrsistent as pyr
from cytoolz import get
from mpl_toolkits.mplot3d import Axes3D

import arrow
from typing import Any, Callable, Dict, List, Text, Tuple, TypeVar, Union

T = TypeVar("ThermoFluid")
C = TypeVar("CSVFluid")

UNITS = {"P":"Pa",
"T":"K","S":"J/kg/K","G":"J/kg","U":"J/kg","D":"kg/m^3","V":"m^3"}



class ThermoFluid():
    """
    A class that will contain the data requested.

    Attributes:
        xvar (str): What variable is on the x-axis
        yvar (str): What variable is on the y-axis
        zvar (str): What variable is on the z-axis, also, what variable is generated by CoolProp
        colorMap (str): What ColorMap Matplotlib uses to make its plot
        vars (List[Text]): a list of xvar, yvar, zvar
        fluid (str): What fluid is being modeled
        data (pandas.DataFrame): The data for the given fluid
        units (List[Text]): the units for xvar, yvar, zvar, in that order.
        numPoints (List[int]): the x-resolution and y-resolution, in that order.
        M (float): the molar mass of the fluid for the system.
        meta (pyrsistent._pmap.PMap): a PMap containing metadata related to the current fluid.

    """

    def __init__(self,
                 fluid: str="Water",
                 var1: str="T",
                 var2: str="P",
                 outvar: str="S",
                 numPoints: Union[List[int], int]=[216, 216],
                 colorMap: str="nipy_spectral") -> None:
        """
        Call the class with these arguments

        Parameters:
            fluid (str): CoolProp Fluid type to use

            var1 (str): x var, normally T, P

            var2 (str): y var, normally P, V

            outvar (str): z var (generated by code), normally S, U

            numPoints (Union[List[int],int]): number of Points for linspaces

            colorMap (str): What color map to use

        """

        self.fluid: str
        self.fluid = fluid
        self.numPoints: Union[List[int], int]
        if type(numPoints) is int:
            self.numPoints = [numPoints, numPoints]
        else:
            self.numPoints = [numPoints[0], numPoints[1]]
        self.colorMap: str
        self.xvar: str
        self.yvar: str
        self.zvar: str
        self.M: float
        self.meta: pyr._pmap.PMap
        self.colorMap = colorMap
        self.xvar = var1
        self.yvar = var2
        self.zvar = outvar
        self.vars = [self.xvar, self.yvar, self.zvar]
        self.M = CP.PropsSI("M", self.fluid)
        if "S" in self.vars[:-1]:
            raise ValueError(
                "S (entropy) is not supported as an input variable, try permuting your inputs until you get something to work!"
            )

        # Linear interpolation between tmin and tmax with NUM_POINTS number of
        # points, delta = tmax-min/NUM_POINTS
        if self.xvar in ["P", "T"]:
            xspace = np.linspace(
                CP.PropsSI(self.xvar + "MIN", self.fluid) + 0.1,
                CP.PropsSI(self.xvar + "MAX", self.fluid) - 0.1,
                self.numPoints[0] + 1)
        elif self.xvar in ["D"] and self.fluid.lower() == "water":
            xspace = np.linspace(0.01, 1200.01, self.numPoints[0] + 1)
        # elif self.xvar in ["S"] and self.fluid.lower() == "water":
        #     xspace = np.linspace(35.0, 393.3, self.numPoints[0])
        elif self.xvar in ["V"]:
            xspace = np.linspace(self.M / 1200.01, self.M / 0.01,
                                 self.numPoints[0] + 1)
        elif self.xvar in ["U"]:
            xspace = np.linspace(9000.0, 6000000.0, self.numPoints[0] + 1)

        # Linear interpolation between pmin and pmax with NUM_POINTS number of
        # points, delta = max-min/NUM_POINTS
        if self.yvar in ["P", "T"]:
            yspace = np.linspace(
                CP.PropsSI(self.yvar + "MIN", self.fluid) + 0.1,
                CP.PropsSI(self.yvar + "MAX", self.fluid) - 0.1,
                self.numPoints[1] + 1)

        elif self.yvar in ["V"]:
            yspace = np.linspace(self.M / 1200.01, self.M / 0.01,
                                 self.numPoints[1] + 1)
        elif self.yvar in ["U"]:
            yspace = np.linspace(9000.0, 6000000.0, self.numPoints[1] + 1)

        # Create a empty list for storing data
        # Then make our data.
        data = []

        if "V" not in self.vars:
            for x in xspace:
                for y in yspace:
                    data.append([
                        x, y, CP.PropsSI(self.zvar, self.xvar, x, self.yvar, y,
                                         self.fluid)
                    ])
        elif self.xvar == "V":
            for x in xspace:
                for y in yspace:
                    data.append([
                        x, y, CP.PropsSI(self.zvar, "D", self.M / x, self.yvar,
                                         y, self.fluid)
                    ])
        elif self.yvar == "V":
            for x in xspace:
                for y in yspace:
                    data.append([
                        x, y, CP.PropsSI(self.zvar, self.xvar, x, "D",
                                         self.M / y, self.fluid)
                    ])
        elif self.zvar == "V":
            for x in xspace:
                for y in yspace:
                    data.append([
                        x, y, self.M /
                        CP.PropsSI("D", self.xvar, x, self.yvar, y, self.fluid)
                    ])

        # Create Pandas Frame of Data
        self.data: pd.DataFrame
        self.data = pd.DataFrame(np.asarray(data), columns=self.vars)
        self.make_units()
        self.clean()
        self.make_meta()

    def make_units(self)-> None:
        """(Re)make the units list"""
        self.units: List[Text]
        self.units = [get(var, UNITS, "UnknownVar") for var in self.vars]

    def make_meta(self) -> None:
        """
        (Re)make the metadata object
        """
        self.make_units()
        self.meta = pyr.pmap({
            "date":
            str(arrow.now("US/Central").format("YYYY-MM-DD @ HH:mm:ss")),
            "fluid": self.fluid,
            "xvar": self.xvar,
            "yvar": self.yvar,
            "zvar": self.zvar,
            "vars": self.vars,
            "numPoints": self.numPoints,
            "colorMap": self.colorMap,
            "units": self.units
        })


    def refresh(self) -> None:
        """
        Refreshes the object, remakes meta, cleans data, remakes units.
        """
        self.units()
        self.clean()
        self.meta()


    def add_column(self, variables: Union[List[Text], Text])-> None:
        """
        Adds a column to the dataframe

        Paramaters:
            variable (Union[List[Text],Text]): What variable(s) to add
        """
        for var in variables:
            try:
                assert var not in self.vars
            except AssertionError:
                print(f"Cannot add column {var}: already in frame")
                return None
            try:
                assert var != "V"
            except AssertionError:
                print(f"Cannot add Volume as a column just yet, TODO")
                return None

        self.vars += variables
        buffer = dict([])
        newcols = {var: (lambda state: CP.PropsSI(var, self.xvar, state[self.xvar], self.yvar, state[self.yvar], self.fluid)) for var in variables}
        for key in newcols:
            buffer[key] = []

        for index, row in self.data.iterrows():
            for key in newcols:
                get(key, buffer).append(get(key, newcols)(row))

        for key in newcols:
            self.data[key] = pd.Series(buffer[key], index=self.data.index)
        self.make_units()
        self.make_meta()

    def clean(self) -> None:
        """Re-cleans data"""
        if "P" in self.vars:
            self.data = self.data[self.data["P"] >=
                                  CP.PropsSI("PMIN", self.fluid) + 1.0]
        if "S" in self.vars:
            self.data = self.data[self.data["S"] > 0.0]
        if "T" in self.vars:
            self.data = self.data[self.data["T"] >=
                                  (CP.PropsSI("TMIN", self.fluid) + 1.0)]
        if "U" in self.vars:
            self.data = self.data[self.data["U"] >= 1.0]
        if "V" in self.vars:
            self.data = self.data[self.data["V"] >= 0.1]


    def write_data(self, path: str) -> None:
        """
        Does what it says on the tin. Makes a CSV and JSON files and saves them to data/FluidName_X-xpoints_Y-ypoints_Z.

        Parameters:
            path (str): path where file should be saved

        """
        self.make_meta()
        middle_string = self.fluid + "_" + "_".join([
            str(varname) + "-" + str(point)
            for (varname, point) in zip(self.vars[:1], self.numPoints)
        ] + [self.vars[2]])
        self.data.to_csv(path + middle_string + ".csv", mode="w+", index=False)
        with open(path + middle_string + ".json", mode="w+") as f:
            json.dump(dict(self.meta), f)

    def copy(self) -> T:
        """
        Returns a copy of itself

        """
        return copy.deepcopy(self)


class CSVFluid():
    """
    A class that will help work with ThermoFluid data contained in CSV/JSON files.

    Attributes:
        data (pandas.DataFrame): The data as read by pandas for the given fluid

        columns (List[Text]): What variable is on the y-axis

        zvar (str): What variable is on the z-axis, also, what variable is generated by CoolProp

        colorMap (str): What ColorMap Matplotlib uses to make its plot

        vars (List[Text]): a list of xvar, yvar, zvar

        fluid (str): What fluid is being modeled

        data (pandas.DataFrame):

        units (List[Text]): the units for xvar, yvar, zvar, in that order.

        numPoints (List[int]): the x-resolution and y-resolution, in that order.

        M (float): the molar mass of the fluid for the system.

        meta (pyrsistent._pmap.PMap): a PMap containing metadata related to the current fluid.

    """

    def __init__(self, pathToFile: str) -> None:
        """
        Call the class with these arguments

        Parameters:
            pathToFile (str): The name of the files you want to use, NOT the path. Must have both a json and a CSV file for this purpose.

        """
        self.meta: pyr._pmap.PMap
        self.data: pd.DataFrame
        self.fluid: str
        self.numPoints: Union[List[int], int]
        self.colorMap: str
        self.xvar: str
        self.yvar: str
        self.zvar: str
        self.M: float
        self.vars: List[Text]
        with open(pathToFile + ".json", mode="r+") as jf:
            self.meta = pyr.pmap(json.loads(jf.read()))
        with open(pathToFile + ".csv", mode="r+") as cf:
            self.data = pd.read_csv(cf)
        self.colorMap = self.meta["colorMap"]
        self.xvar = self.meta["xvar"]
        self.yvar = self.meta["yvar"]
        self.zvar = self.meta["zvar"]
        self.vars = self.meta["vars"]
        self.fluid = self.meta["fluid"]
        self.colorMap = self.meta["colorMap"]
        self.numPoints = self.meta["numPoints"]
        self.units = self.meta["units"]

    def changeOrder(self, order: List[int]) -> None:
        """
        Changes order of the columns:

        Parameters:
            order (List[int]): is a permutation on {0,1,2}.

        """

        self.data = self.data[[self.vars[i] for i in order]]
        self.vars = [self.vars[i] for i in order]
        self.xvar = self.vars[0]
        self.yvar = self.vars[1]
        self.zvar = self.vars[2]
        self.units = [self.units[i] for i in order]

    def copy(self) -> C:
        """
        Returns a copy of itself

        """
        return copy.deepcopy(self)


def fluid_plot(fluid: Union[CSVFluid, ThermoFluid]) -> None:
    """
    Does what it says on the tin. Makes a 3D Scatter Plot of the dataframe.

    Parameters:
        fluid (Union[CSVFluid, ThermoFluid]): Which fluid object to make a plot for.

    """

    # Plotting:
    fig = plt.figure()

    # we want 3D plots
    ax = fig.add_subplot(111, projection="3d")

    # Plot the data
    ax.scatter(
        fluid.data[fluid.xvar],
        fluid.data[fluid.yvar],
        fluid.data[fluid.zvar],
        c=fluid.data[fluid.zvar],
        cmap=fluid.colorMap,
        edgecolors="none")

    # Set the Labels
    ax.set_xlabel("{0} [{1}]".format(fluid.vars[0], fluid.units[0]))
    ax.set_ylabel("{0} [{1}]".format(fluid.vars[1], fluid.units[1]))
    ax.set_zlabel("{0} [{1}]".format(fluid.vars[2], fluid.units[2]))
    ax.set_title("{0} and {1} vs {2} of {3}".format(*fluid.vars, fluid.fluid))
    plt.show()


def rescale(oldrange: List[Union[float, int]],
            newrange: List[Union[float, int]]) -> Callable[[Union[float, int]],
                                                           Union[float, int]]:
    """
    Creates a function that transforms a single variable from oldrange to newrange. Use it with map or Pandas.DataFrame.apply

    Parameters:
        oldrange (List[Union[float, int]]): The old range of the data, [min, max]
        newrange (List[Union[float, int]]): The new range of the data, [min, max]

    """
    return lambda x: (newrange[1] - newrange[0]) / (oldrange[1] - oldrange[0]) * (x - oldrange[0]) + newrange[0]
