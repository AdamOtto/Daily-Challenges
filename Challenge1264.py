"""
Given an N by M matrix consisting only of 1's and 0's,
find the largest rectangle containing only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.

Code help from: https://www.geeksforgeeks.org/maximum-size-rectangle-binary-sub-matrix-1s/
"""
def Solution(ar):
    N = len(ar)
    M = len(ar[0])
    retVal = maxHist(ar[0])
    for i in range(1, N):
        for j in range(M):
            if (ar[i][j]):
                ar[i][j] += ar[i - 1][j]
        retVal = max(retVal, maxHist(ar[i]))
    return retVal

def maxHist(ar):
    result = []
    top_val = 0
    max_area = 0
    area = 0
    i = 0
    while i < len(ar):
        if (len(result) == 0) or (ar[result[-1]] <= ar[i]):
            result.append(i)
            i += 1
        else:
            top_val = ar[result.pop()]
            area = top_val * i
            if (len(result)):
                area = top_val * (i - result[-1] - 1)
            max_area = max(area, max_area)
    while (len(result)):
        top_val = ar[result.pop()]
        area = top_val * i
        if (len(result)):
            area = top_val * (i - result[-1] - 1)
        max_area = max(area, max_area)
 
    return max_area

# Return 4
print(Solution([[1, 0, 0, 0],
                [1, 0, 1, 1],
                [1, 0, 1, 1],
                [0, 1, 0, 0]]))
                
# Return 6
print(Solution([[1, 0, 1, 0, 0],
                [1, 0, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 0, 0, 1, 1],
                [1, 0, 0, 0, 0]]))