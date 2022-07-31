"""
You are given an array of length N, where each element i represents
the number of ways we can produce i units of change. For example,
[1, 0, 1, 1, 2] would indicate that there is only one way to make 0, 2, or 3 units,
and two ways of making 4 units.

Given such an array, determine the denominations that must be in use.
In the case above, for example, there must be coins with value 2, 3, and 4.
"""
def Solution(ar):
    l = len(ar)
    retVal = []
    
    for i in range(1, l):
        if ar[i] <= 0:
            continue
        retVal.append(i)
        val = i
        mult = 2
        while val * mult < l:
            ar[val * mult] -= 1
            mult += 1
    
    return retVal

# Return [2, 3, 4]
in1 = [1, 0, 1, 1, 2]
print(Solution(in1))

# Return [1, 4]
in1 = [1, 1, 1, 1, 2]
print(Solution(in1))

# Return [1]
in1 = [1, 1, 1, 1, 1]
print(Solution(in1))

# Return [2, 3, 4, 10]
in1 = [1, 0, 1, 1, 2, 0, 1, 0, 1, 1, 2]
print(Solution(in1))