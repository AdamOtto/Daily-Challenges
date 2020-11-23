'''
You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down,
find the maximum number of coins you can collect by the bottom right corner.
'''

#O(n^2)
def Solution(in1):
    l = len(in1)
    w = len(in1[0])
    steps = []
    for y in range(l):
        steps.append([])
        for x in range(w):
            steps[y].append(0)
    #print(steps)
    steps[0][0] = in1[0][0]
    nextStep = [(0,0)]
    
    while len(nextStep) != 0:
        cur = nextStep
        nextStep = []
        for c in cur:
            x, y = c
            
            if x + 1 < w:
                steps[y][x+1] = max(steps[y][x+1], in1[y][x+1] + steps[y][x])
                if (x+1, y) not in nextStep:
                    nextStep.append((x+1, y))
            if y + 1 < l:
                steps[y+1][x] = max(steps[y+1][x], in1[y+1][x] + steps[y][x])
                if (x, y+1) not in nextStep:
                    nextStep.append((x, y+1))
    #print(steps)
    return steps[l-1][w-1]

"""
in1 = [
    [0, 3, 1, 1],
    [2, 0, 0, 4],
    [1, 5, 3, 1]]
"""
in1 = [
    [1,1,1,1,1],
    [0,0,0,0,1],
    [0,9,0,0,1],
    [0,0,1,40,1]
    ]

t = Solution(in1)
print(t)