"""
Given a multiset of integers, return whether it can
be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into
{15, 5, 10, 15, 10} and {20, 35},which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
"""

def Solution(ar):
    sum1 = 0
    sum2 = 0
    sum1Ls = []
    sum2Ls = []
    l = len(ar)
    ar = sorted(ar, reverse = True)
    
    for i in range(l):
        if sum1 <= sum2:
            sum1 += ar[i]
            sum1Ls.append(ar[i])
        else:
            sum2 += ar[i]
            sum2Ls.append(ar[i])
    if sum1 == sum2:
        return [sum1Ls, sum2Ls]
    return False
# Return [[35, 15, 5], [20, 15, 10, 10]]
print(Solution([15, 5, 20, 10, 35, 15, 10]))

# Return False
print(Solution([1,1,1,1,1,3,4,1,1,3,1,1]))

# Return False
print(Solution([15, 5, 20, 10, 35]))

# Return [[4, 1, 1, 1, 1, 1], [3, 3, 1, 1, 1]]
print(Solution([1,1,1,1,1,3,4,1,1,3,1]))