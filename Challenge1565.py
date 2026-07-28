"""
Given a multiset of integers, return whether it can be partitioned
into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35},
which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false,
since we can't split it up into two subsets that add up to the same sum.
"""
def Solution(ar):
    temp = sorted(ar)
    sub1 = []
    sub2 = []
    for i in reversed(range(len(temp))):
        if sum(sub1) <= sum(sub2):
            sub1.append(temp[i])
        else:
            sub2.append(temp[i])
    
    return sum(sub1) == sum(sub2)

# Return True
print(Solution([15, 5, 20, 10, 35, 15, 10]))

# Return False
print(Solution([15, 5, 20, 10, 35]))

# Return True
print(Solution([1, 2, 3, 6]))