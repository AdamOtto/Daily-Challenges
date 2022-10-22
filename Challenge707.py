"""
You are the technical director of WSPT radio, serving listeners nationwide.
For simplicity's sake we can consider each listener to live along a horizontal
line stretching from 0 (west) to 1000 (east).

Given a list of N listeners, and a list of M radio towers,
each placed at various locations along this line,
determine what the minimum broadcast range would have to be
in order for each listener's home to be covered.

For example, suppose listeners = [1, 5, 11, 20], and towers = [4, 8, 15].
In this case the minimum range would be 5, since that would be required for
the tower at position 15 to reach the listener at position 20.
"""
def Solution(N, M):
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
print(Solution([1, 5, 11, 20], [4,8,15]))

# Return 25
print(Solution([5, 25, 50, 75], [0, 30, 100]))

# Return 925
print(Solution([1000, 1], [25, 50, 75]))