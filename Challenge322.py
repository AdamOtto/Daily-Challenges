"""
Starting from 0 on a number line, you would like to make a series of jumps that lead to the integer N.

On the ith jump, you may move exactly i places to the left or right.

Find a path with the fewest number of jumps required to get from 0 to N.
"""
import sys

def Solution(ar):
    if ar == 0:
        return 0
    nextStep = []
    visited = {}
    visited[0] = 1
    nextStep.append( (1,0) )

    while ar not in visited and len(nextStep) > 0:
        cur = nextStep.pop(0)
       
        if cur[0] not in visited:
           visited[cur[0]] = 1 + visited[cur[1]]
           visited[-cur[0]] = 1 + visited[cur[1]]
        else:
           visited[cur[0]] = min(visited[cur[0]], 1 + visited[cur[1]])
           visited[-cur[0]] = visited[cur[0]]
           
        
        if cur[0] + visited[cur[0]] not in visited and cur[0] + visited[cur[0]] >= 0:
            nextStep.append( (cur[0] + visited[cur[0]], cur[0]) )
        if cur[0] - visited[cur[0]] not in visited and cur[0] + visited[cur[0]] >= 0:
            nextStep.append( (cur[0] - visited[cur[0]], cur[0]) )
    
    return visited[ar] - 1

# Return 4: 0, 1, 3, 6, 10
print(Solution(10))

# Return 6: 0, 1, 3, 6, 10, 5, 11
print(Solution(11))

# Return 8: 0, 1, 3, 6, 10, 5, 11, 4, 12
print(Solution(12))

# Return 48
print(Solution(1000))

# Return 60
print(Solution(1500))