"""
Given a number in the form of a list of digits,
return all possible permutations.

For example, given [1,2,3],
return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""


def Solution(ar):
    if len(ar) <= 0:
        return []
    elif len(ar) == 1:
        return [ar]
    
    retVal = []
    
    for i in range(len(ar)):
        temp = ar[i]
        
        rest = ar[:i] + ar[i+1:]
        
        for r in Solution(rest):
            retVal.append([temp] + r)
    return retVal
        

# Return: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(Solution([1,2,3]))

# Return: [['a', 'b', 'c', 'd'], ['a', 'b', 'd', 'c'], ['a', 'c', 'b', 'd'], ['a', 'c', 'd', 'b'], ['a', 'd', 'b', 'c'], ['a', 'd', 'c', 'b'], ['b', 'a', 'c', 'd'], ['b', 'a', 'd', 'c'], ['b', 'c', 'a', 'd'], ['b', 'c', 'd', 'a'], ['b', 'd', 'a', 'c'], ['b', 'd', 'c', 'a'], ['c', 'a', 'b', 'd'], ['c', 'a', 'd', 'b'], ['c', 'b', 'a', 'd'], ['c', 'b', 'd', 'a'], ['c', 'd', 'a', 'b'], ['c', 'd', 'b', 'a'], ['d', 'a', 'b', 'c'], ['d', 'a', 'c', 'b'], ['d', 'b', 'a', 'c'], ['d', 'b', 'c', 'a'], ['d', 'c', 'a', 'b'], ['d', 'c', 'b', 'a']]
print(Solution(['a', 'b', 'c', 'd']))