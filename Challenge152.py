"""
You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
from random import random


def Solution(num, prob):
    ln = len(num)
    lp = len(prob)

    if ln != lp:
        return False

    t = 0
    for p in prob:
        t += p
    if t != 1:
        return False

    t = random()
    for i in range(0, lp):
        t -= prob[i]
        if t <= 0:
            return num[i]

def TestFrequency(num, prob, NumOfTests):
    count = [0] * len(num)
    for i in range(0, NumOfTests):
        t = Solution(num, prob)
        ti = num.index(t)
        count[ti] += 1

    for i in range(0, len(num)):
        s = str(num[i]) + " = %" + str( (count[i] / NumOfTests) * 100 )
        print(s)

#in1 = [1, 2, 3, 4]
#in2 = [0.1, 0.5, 0.2, 0.2]
#print(Solution(in1, in2))
in1 = [1,2,3,4,5,6,7,8,9,10]
in2 = [0.1,0.05,0.3,0.01,0.04,0.07,0.03,0.1,0.1,0.2]

TestFrequency(in1, in2, 10000)
