"""
You are given an unsorted list of 999,000 unique integers,
each from 1 and 1,000,000. Find the missing 1000 numbers.
What is the computational and space complexity of your solution?
"""

# O(N) time and space.
def Solution(ar):
    retVal = []
    temp = [True] * 1000000
    
    for i in range(len(ar)):
        temp[ar[i]] = False
    
    for i in range(len(temp)):
        if temp[i]:
            retVal.append(i)
    
    #print(len(retVal))
    return retVal

in1 = []
for i in reversed(range(0, 1000000)):
    in1.append(i)

for i in range(998000, 999000):
    in1.pop(i)
#print(len(in1))
print(Solution(in1))