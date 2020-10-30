'''
Given a number represented by a list of digits, find the next greater permutation of a number,
in terms of lexicographic ordering. If there is not greater permutation possible,
return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2].
The list [1,3,2] should return [2,1,3].
The list [3,2,1] should return [1,2,3].
'''

import itertools

def Solution(in1):
    Perm = list(itertools.permutations([1, 2, 3]))
    val = listToInt(in1)
    l = []
    for permutation in Perm:
        l.append(listToInt(permutation))
    l = sorted(l)
    retVal = None
    for num in l:
        if num > val:
            retVal = IntToList(num)
            break
    
    if retVal is None:
        t = IntToList(l[0])
        print(t)
        return t
    print(retVal)
    return retVal
    
def listToInt(val):
    l = len(val)
    retVal = 0
    decimal = 1
    for i in reversed(range(0, l)):
        retVal += val[i] * decimal
        decimal = decimal * 10
    return retVal

def IntToList(val):
    retVal = []
    IntString = str(val)
    for s in IntString:
        retVal.append(int(s))
    return retVal
    
    
in1 = [1,2,3]
Solution(in1)
in1 = [1,3,2]
Solution(in1)
in1 = [3,2,1]
Solution(in1)
