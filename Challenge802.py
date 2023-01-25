"""
You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
import random
def Solution(nNum, nProb):
    if sum(nProb) != 1 or len(nNum) != len(nProb):
        return False
    l = len(nNum)
    temp = random.uniform(0, 1)
    i = 0
    while i < l:
        temp -= nProb[i]
        if temp < 0:
            break
        i += 1
    return nNum[i]

# Should return probabilities close to the input.
in1 = [0,0,0,0]
for i in range(1000):
    temp = Solution([1,2,3,4], [0.1, 0.5, 0.2, 0.2])
    in1[temp - 1] += 1

print("1:", in1[0] / 1000)
print("2:", in1[1] / 1000)
print("3:", in1[2] / 1000)
print("4:", in1[3] / 1000)