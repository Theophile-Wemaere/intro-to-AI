#!/bin/python

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np


# create model
bayesNet = BayesModel()

# set nodes
bayesNet.add_node("N")
bayesNet.add_node("L")
bayesNet.add_node("S")
bayesNet.add_node("I")
bayesNet.add_node("R")

# set edges
bayesNet.add_edge("L", "N")
bayesNet.add_edge("I", "N")
bayesNet.add_edge("S", "N")
bayesNet.add_edge("S", "R")
bayesNet.add_edge("R", "N")
