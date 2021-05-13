"""
You are given an N by M 2D matrix of lowercase letters.
Determine the minimum number of columns that can be removed to ensure
that each row is ordered from top to bottom lexicographically.
That is, the letter at each column is lexicographically later as you go down each row.
It does not matter whether each row itself is ordered lexicographically.
"""

def Solution(ar):
    n = len(ar)
    if n == 0:
        return False
    elif n == 1:
        return 0
    m =len(ar[0])
    count = 0
    for i in range(0, m):
        count += Helper(ar, i, n)
    return count

def Helper(ar, i, n):
    for j in range(1, n):
        if ar[j][i] <= ar[j - 1][i]:
            return 1
    return 0
    
"""
in1 = [ ['c', 'b', 'a'],
        ['d', 'a', 'f'],
        ['g', 'h', 'i']
      ]
"""
#in1 = [ ['a','b','c','d'] ]
in1 = [ ['a', 'a', 'a', 'a', 'h'],
        ['b', 'c', 'e', 'a', 'i'],
        ['c', 'z', 'm', 'a', 'j']
      ]
print(Solution(in1))



