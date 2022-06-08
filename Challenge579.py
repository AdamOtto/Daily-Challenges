"""
Starting from 0 on a number line, you would like
to make a series of jumps that lead to the integer N.

On the ith jump, you may move exactly i
places to the left or right.

Find a path with the fewest number of
jumps required to get from 0 to N.
"""
import sys

def Solution(N):
    q = []
    q.append( (0, 1) )
    retVal = sys.maxsize
    
    while retVal == sys.maxsize:
        cur, jump = q.pop(0)
        
        if cur == N:
            retVal = jump - 1
        
        q.append( (cur + jump, jump + 1) )
        q.append( (cur - jump, jump + 1) )
    
    return retVal

# Return 2.  0 -> 1, jump 1 -> 3, jump 2
print(Solution(3))

# Return 7
print(Solution(14))

# Return 15
print(Solution(100))