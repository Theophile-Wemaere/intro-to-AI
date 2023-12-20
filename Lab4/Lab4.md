<html>
	<center>Introduction to AI, M. MATEI</center>
	<center>ISEP - December 2023</center>
	<center style="font-style:italic">by Theophile Wemaere</center>
</html>

Source code and markdown source file can be found [here](https://github.com/Theophile-Wemaere/intro-to-AI/tree/main/Lab3)
or at [github.com/Theophile-Wemaere/intro-to-ai](https://github.com/Theophile-Wemaere/intro-to-ai) 

### Part A

**Question 1**

Bayes' theorem is a fundamental formula in probability theory that relates the conditional probability of an event to the probability of one event given another. It is commonly used to update our beliefs about the probability of an event based on new evidence. However, Bayes' theorem can only be applied to independent events.

Independence between random variables means that the occurrence of one event does not affect the probability of the occurrence of another event. This is a crucial assumption for Bayes' theorem because it ensures that the updating of our beliefs is not circular. If events are not independent, then our updated belief about one event could potentially affect our belief about the other event, which would lead to an infinite regress of updates.

To illustrate this, consider the following example:

Suppose we are given the following information:

- There is a 50% probability that a patient has the flu.
- If a patient has the flu, there is a 90% probability that they will test positive for the flu.
- If a patient does not have the flu, there is a 5% probability that they will test positive for the flu.

In this example, the events of being diagnosed with the flu and testing positive for the flu are independent. This is because the occurrence of one event (being diagnosed with the flu) does not affect the probability of the occurrence of the other event (testing positive for the flu). Therefore, Bayes' theorem can be applied to accurately update our beliefs about the probability of having the flu based on the new evidence of a positive test result.

**Question 2**

Independence and conditional independence are both concepts in probability theory that relate the probabilities of events. However, they differ in their scope and how they are defined.

**Independence:**

Events are considered independent if the occurrence of one event does not affect the probability of the occurrence of another event. Mathematically, this is represented by the formula:
```
P(A ∩ B) = P(A) * P(B)
```

where:
- A and B are events
- P(A ∩ B) is the probability of both events occurring simultaneously
- P(A) is the probability of event A occurring
- P(B) is the probability of event B occurring

**Conditional independence:**

Events are considered conditionally independent given a third event C if the occurrence of one event (A) does not affect the probability of the occurrence of another event (B) given that the third event (C) has already occurred. Mathematically, this is represented by the formula:
```
P(A | B ∩ C) = P(A | C)
```

where:
- A and B are events
- C is a third event
- P(A | B ∩ C) is the conditional probability of event A occurring given that both events B and C have already occurred
- P(A | C) is the conditional probability of event A occurring given that event C has already occurred

In summary:
independence is a broader concept that applies to any two events, regardless of the presence of other events. Conditional independence is a more specific concept that applies to two events when a third event is considered. It states that the relationship between the two events is independent of the third event.

**Question 3**
###### 1°/
```
You have three coins in your pocket: 
1. Coin 1 is a fair coin that comes up heads with probability 1/2. 
2. Coin 2 is a biased coin that comes up heads with probability 1/4. 
3. Coin 3 is a biased coin that comes up heads with probability 3/4. 

1°/. Suppose you pick one of the coins uniformly at random and flip it three times. If you ob- serve the sequence HHT (where H stands for heads and T stands for tails), what is the probability that you chose Coin 3?
```
We note C3 the event where the Coin 3 is choosed and Cx the event when the coin X is choosed.

We are looking for `P(C3|HHT)`.
Using [Bayes theorem]([Bayes' theorem - Wikipedia](https://en.wikipedia.org/wiki/Bayes%27_theorem)) : $$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$We can find :
$$P(C3|HTT) = \frac{P(HTT|C3)P(C3)}{P(HTT)} = \frac{P(HHT|C3)P(C3)}{\sum_{x=1}^{3}P(HHT|Cx)P(Cx)} = \frac{P(HHT|C3)}{\sum_{x=1}^{3}P(HHT|Cx)} $$
N.B : P(Cx) = 1/3 so P(C3) and P(Cx) cancel each other

Using the probability of head for each coin, we get :
$$P(C3|HTT) = \frac{3/4\times3/4\times1/4}{(1/2\times1/2\times1/2)+(1/4\times1/4\times3/4)+(3/4\times3/4\times1/4)} = 9/20$$
###### 2°/
```
2°/ Suppose X and Y are independent random variables over the domain 1, 2, 3 with P (X = 3) = 1/6. Given the following partially specified joint distribution, what are the remaining values? Write your answers as simplified fractions in the blanks.
```
![[fractions.png]]

As P(X) and P(Y) are independant, we have : $$P(X,Y) = P(X) \times P(Y)$$
First we need to find every value for P(X) (we know that P(X=3) = 1/6 ):
$$
\frac{P(X=1,Y=1)}{P(X=2,Y=1)} = \frac{1/4}{1/6}
$$
$$
\frac{P(X=1,Y=1)}{P(X=2,Y=1)} = \frac{P(X=1)P(Y=1)}{P(X=2)P(Y=1)} = \frac{P(X=1)}{P(X=2)} = 3/2
$$
$$
P(X=1) = 3/2 \times P(X=2)
$$
Using the general probability rule that "For S the sample space of all possibilities, P(S) = 1", we have :
$$
P(X=1)+P(X=2)+P(X=3) = 1
$$
$$
3/2 \times P(X=2) + P(X=2) + 1/6 = 5/2 \times P(X=2) + 1/6 = 1
$$
$$
P(X=2) = 1/3
$$
So P(X=2) = 1/3 and P(X=3) = 1/6, we can deduce :
$$
P(X=1)+P(X=2)+P(X=3) = 1 \rightarrow P(X=1) = 1/2
$$

Now we can find every value of P(Y):
$$
P(X=1,Y=1) = P(X=1)P(Y=1)=1/2\times P(Y=1) = 1/4
$$
$$
P(X=1,Y=2) = P(X=1)P(Y=2) = 1/2\times P(Y=2) = 1/16
$$
So we find P(Y=1) = 1/2 and P(Y=2) = 1/8
Using the same rule as before, we get :
$$
P(Y=1)+P(Y=2)+P(Y=3)=1 \rightarrow P(Y=3) = 3/8
$$
Now we can find the remaining values :
$$
P(X=1,Y=3) = P(X=1)P(Y=3) = 1/2 \times 3/8 = 3/16
$$
$$
P(X=2,Y=3)=P(X=2)P(Y=3)=1/3\times 3/8= 1/8
$$
$$
P(X=3,Y=1) = P(X=3)P(Y=1) = 1/6 \times 1/2 = 1/12 
$$
$$
P(X=3,Y=2) = P(X=3)P(Y=2) = 1/6\times 1/8=1/48
$$
$$
P(X=3,Y=3) = P(X=3)P(Y=3) = 1/6\times 3/8=1/16
$$
Soit :
![[fractions_solved.png]]
### Part B

**Question 1**
The following python code is the implementation of the Bayesian Model using the `pgmpy` library :
```python
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

# Question 2
result = solver.query(variables=['N'])
print("P(N) :")
print(result)

# Question 3
result = solver.query(variables=['N'], evidence={'L': 0})
print("P(N|L) :")
print(result)

# Question 4
print("(in)dependencies of variables :")
print(bayesNet.get_independencies())
```

**Question 2**
Computing the probability of "Project should be not considered (not scored)" equal to compute the probability of P(N).

Using the BayesianModel implementation in python :
```python
solver = VariableElimination(bayesNet)
result = solver.query(variables=['N'])
print(result)
```
We get :
![[output_1.png]]
So P(N) = 0.12

**Question 3**
Computing the probability of "Project should not be considered (not scored) given the ML signaled it" equal to compute to probability of P(N|L).

Using the BayesianModel implementation in python :
```python
solver = VariableElimination(bayesNet)
result = solver.query(variables=['N'], evidence={'L': 0})
print(result)
```
We get :
![[output_2.png]]
So P(N|L) = 0.76

**Question 4**
We can find the dependencies between the variables using the method `get_independencies()` of the `BayesianNetwork` class :
```python
dependencies = bayesNet.get_independencies()
print(dependencies)
```
We get :
![[output_3.png]]