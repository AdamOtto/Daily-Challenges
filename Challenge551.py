"""
Assume you have access to a function toss_biased()
which returns 0 or 1 with a probability that's not 50-50
(but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""
import random

def toss_biased():
    bias = random.randint(-10, 40)
    r = random.randint(0, 100) + bias
    if r > 50:
        return 1
    return 0

tests = 1000
count0 = count1 = 0
for i in range(tests):
    if toss_biased() == 1:
        count1 += 1
    else:
        count0 += 1

print("Zeros counted in", tests,"tests:", count0)
print("Ones counted in", tests,"tests:", count1)



