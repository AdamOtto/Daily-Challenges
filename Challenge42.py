'''
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''
def Solution(l, k):
    l.sort(reverse = True)
    #print(l)
    t = 0
    retVal = []
    for i in l:
        if i + t <= k:
            t = t + i
            retVal.append(i)
            if t == k:
                return retVal
    return None

#in1 = [12, 1, 61, 5, 9, 2]
#k = 24
in1 = [7,6,5,4,3,2,2,1]
k = 3
print(Solution(in1, k))