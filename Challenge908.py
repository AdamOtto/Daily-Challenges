"""
You are given an N by M 2D matrix of lowercase letters.
Determine the minimum number of columns that can be removed
to ensure that each row is ordered from top to bottom lexicographically.
That is, the letter at each column is lexicographically later as you go
down each row. It does not matter whether each row itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center.
We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1,
since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows
are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would
need to remove all the columns to order it.
"""
def Solution(ar):
    y = len(ar)
    if y <= 1:
        return 0
    
    x = len(ar[0])
    retVal = 0
    for i in range(0, x):
        for j in range(1, y):
            if ord(ar[j - 1][i]) > ord(ar[j][i]):
                retVal += 1
                break
    return retVal

# Return 1
in1 = [ ['c','b','a'],
        ['d','a','f'],
        ['g','h','i']]
print(Solution(in1))

# Return 0
in1 = [['a','b','c']]
print(Solution(in1))

# Return 3
in1 = [ ['z','y','x'],
        ['w','v','u'],
        ['t','s','r']]
print(Solution(in1))