"""
You are given n numbers as well as n probabilities that sum up to 1.
Write a function to generate one of the numbers with its corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities [0.1, 0.5, 0.2, 0.2],
your function should return 1 10% of the time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.
"""
import random

def Solution(nums, prob):
    t = 0
    for p in prob:
        t += p
    if t != 1:
        return False
    
    t = random.uniform(0, 1)
    i = 0
    while t >= 0:
        if t > prob[i]:
            t -= prob[i]
        else:
            break
        i += 1
    return nums[min(i, len(nums) - 1)]

d = {1:0, 2:0, 3:0, 4:0}
upper = 10000
for i in range(0, upper):
    d[Solution([1, 2, 3, 4], [0.1, 0.5, 0.2, 0.2])] += 1

for key, val in d.items():
    print(str(key) + ": " + str(val / upper))