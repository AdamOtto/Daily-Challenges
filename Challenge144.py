'''
Given an array of numbers and an index i,
return the index of the nearest larger number of the number at index i,
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.
'''

def Solution(n, i):
    l = len(n)
    iDown = max(0, i - 1)
    iUp = min(l, i + 1)
    while iDown != 0 or iUp != l:
        if n[iDown] > n[i]:
            return abs(iDown - i)
        if n[iUp] > n[i]:
            return abs(iUp - i)
        iDown = max(0, iDown - 1)
        iUp = min(l, iUp + 1)
    return None

#in1 = [4, 1, 3, 5, 6]
#i = 0
in1 = [5,1,1,1,1,4,1,1,1,1,3,1,1,1,1,1,6]
i = 5
print(Solution(in1,i))
