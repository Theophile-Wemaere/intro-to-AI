#!/bin/python

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
import numpy as np


# create model
bayesNet = BayesianNetwork()

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
bayesNet.add_edge("N", "R")

cpd_I = TabularCPD(variable="I", variable_card=2, values=[[0.21],[0.79]])

cpd_L = TabularCPD(variable="L", variable_card=2, values=[[0.08],[0.92]])

cpd_S = TabularCPD(variable="S", variable_card=2, values=[[0.12],[0.88]])

cpd_R = TabularCPD(variable="R", variable_card=2, evidence=["S", "N"], evidence_card=[2, 2],
                  values=[[0.38,0.08,0.16,0.05],[0.62,0.92,0.84,0.95]])

cpd_N = TabularCPD(variable="N", variable_card=2, evidence=["L", "S", "I"], evidence_card=[2, 2, 2],
                  values=[[0.92, 0.88, 0.79, 0.73, 0.22, 0.08, 0.17, 0.03],
                          [0.08, 0.12, 0.21, 0.27, 0.78, 0.92, 0.83, 0.97]])

bayesNet.add_cpds(cpd_I, cpd_L, cpd_S, cpd_R, cpd_N)

bayesNet.check_model()

solver = VariableElimination(bayesNet)

# # Question 2
# result = solver.query(variables=['N'])
# print("P(N) :")
# print(result)

# # Question 3
# result = solver.query(variables=['N'], evidence={'L': 0})
# print("P(N|L) :")
# print(result)

# Question 4
print("(in)dependencies of variables :")
print(bayesNet.get_independencies())