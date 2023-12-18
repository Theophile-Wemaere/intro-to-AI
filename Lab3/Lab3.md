<html>
	<center>Introduction to AI, M. MATEI</center>
	<center>ISEP - December 2023</center>
	<center style="font-style:italic">by Theophile Wemaere</center>
</html>

## Bayesian Inference

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

[0.92,0.88,0.79,0.73,0.22,0.08,0.17,0.03]
[0.08,0.12,0.21,0.27,0.78,0.92,0.83,0.97]
### Part B


$$A = \pi r^2$$

