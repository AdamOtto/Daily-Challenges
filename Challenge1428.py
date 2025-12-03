"""
Given an array of positive integers, divide the array into two subsets
such that the difference betweenthe sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25],
return the sets {10, 25} and {5, 15, 20},
which has a difference of 5, which is the smallest possible difference.
"""
def Solution(ar):
    temp = sorted(ar)
    ret1 = []
    ret2 = []
    for i in reversed(range(len(ar))):
        if sum(ret1) <= sum(ret2):
            ret1.append(ar[i])
        else:
            ret2.append(ar[i])
    return ret1, ret2, abs(sum(ret1) - sum(ret2))

# Return ([25, 10, 5], [20, 15], 5)
print(Solution([5, 10, 15, 20, 25]))

# Return ([85, 45, 40, 30], [80, 60, 35], 25)
print(Solution([30, 35, 40, 45, 60, 80, 85]))