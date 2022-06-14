"""
Given an N by M matrix consisting only of 1's and 0's,
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
 
Return 4.
"""

def Solution(ar):
    N = len(ar)
    M = len(ar[0])
    retVal = 0
    
    for x in range(N):
        for y in range(M):
            if ar[x][y] == 1:
                retVal = max(retVal, Helper(ar, x, y))
    
    return retVal
    
def Helper(ar, x, y):
    curx = 1
    cury = 1
    
    while x + curx < len(ar):
        if ar[x + curx][y] == 1:
            curx += 1
        else:
            break
    curx -= 1
    
    while y + cury < len(ar[0]):
        if ar[x][y + cury] == 1:
            cury += 1
        else:
            break
    cury -= 1
    
    if curx == cury:
        curx2 = 1
        cury2 = 1
        
        while y + curx2 < len(ar[0]):
            if ar[x + curx][y + curx2] == 1:
                curx2 += 1
            else:
                break
        curx2 -= 1
            
        while x + cury2 < len(ar):
            if ar[x + cury2][y + cury] == 1:
                cury2 += 1
            else:
                break
        cury2 -= 1 
        
        if curx2 == cury2:
            return (curx + 1) * (cury + 1)
    return -1
    
# Return 4 
in1 = [[1, 0, 0, 0],
[1, 0, 1, 1],
[1, 0, 1, 1],
[0, 1, 0, 0]]

print(Solution(in1))

# Return 9
in1 = [[0,1,1,1,1],
       [1,1,1,1,1],
       [0,1,1,1,0],
       [0,1,0,0,1],
       [0,0,0,0,0]]
print(Solution(in1))