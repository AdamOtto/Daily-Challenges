"""
The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""
def Solution(in1):
    lenPow = int(pow(2, len(in1)))
    s = set()
    retVal = []
    for i in range(lenPow):
        for j in range(len(in1)):
            if i & (1 << j):
                s.add(in1[j])
        retVal.append(list(s))
        s.clear()
    return retVal

# Return [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
print(Solution([1,2,3]))

# Return [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]
print(Solution([1,2,3,4]))