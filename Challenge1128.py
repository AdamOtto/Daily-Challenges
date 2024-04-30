"""
Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""
def Solution(ar):
    retVal = []
    for i in range(0, len(ar)):
        Helper([ar[i]], ar, retVal)
    return retVal

def Helper(curList, ar, retVal):
    if len(curList) == len(ar):
        retVal.append(curList)
        return
    
    for i in range(0, len(ar)):
        if ar[i] not in curList:
            temp = curList.copy()
            temp.append(ar[i])
            Helper(temp, ar, retVal)
    return

# Return [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print( Solution([1,2,3]) )
# Return [['w', 'x', 'y', 'z'], ['w', 'x', 'z', 'y'], ['w', 'y', 'x', 'z'] ... ['z', 'y', 'w', 'x'], ['z', 'y', 'x', 'w']]
print( Solution(["w", "x", "y", "z"]) )