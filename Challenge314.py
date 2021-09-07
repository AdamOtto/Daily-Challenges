"""
You are the technical director of WSPT radio, serving listeners nationwide.
For simplicity's sake we can consider each listener to live along a horizontal
line stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers,
each placed at various locations along this line,
determine what the minimum broadcast range would have to be
in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20],
and towers = [4, 8, 15]. In this case the minimum range would be 5,
since that would be required for the tower at position 15 to reach the listener at position 20.
"""
import sys

# O(N*M)
def Solution1(N, M):
    minRange = [sys.maxsize] * len(N)
    
    for i in range(0, len(N)):
        for j in range(0, len(M)):
            minRange[i] = min(minRange[i], abs(N[i] - M[j]))
    
    retVal = 0
    
    for i in range(0, len(minRange)):
        retVal = max(retVal, minRange[i])
    return retVal

# O(N+M)
def Solution2(N, M):
    N = sorted(N)
    M = sorted(M)
    rightTower = 0
    leftTower = 0
    i = 0
    j = 0
    retVal = 0
    
    while i < len(N):
        if N[i] < M[rightTower]:
            retVal = max(retVal, min(abs(N[i] - M[rightTower]), abs(N[i] - M[leftTower])))
            i += 1
        else:
            if rightTower != len(M) - 1:
                rightTower = min(rightTower + 1, len(M) - 1)
                leftTower = max(rightTower - 1, 0)
            else:
                retVal = max(retVal, min(abs(N[i] - M[rightTower]), abs(N[i] - M[leftTower])))
                i += 1
    
    return retVal


# Return 5
N = [1, 5, 11, 20]
M = [4,8,15]
print(Solution1(N, M))
print(Solution2(N, M))

# Return 100
N = [0,10,50,110,400,220,600,756,100]
M = [100,300,500,700,900]
print(Solution1(N, M))
print(Solution2(N, M))

# Return 5
N = [1,2,3,4,5,6,7,8,9,10]
M = [5]
print(Solution1(N, M))
print(Solution2(N, M))

# Return 400
N = [500]
M = [10,20,30,40,50,60,70,80,90,100]
print(Solution1(N, M))
print(Solution2(N, M))