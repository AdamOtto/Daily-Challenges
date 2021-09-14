"""
Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.

For example, given 100, you can reach 1 in five steps with the following route:
100 -> 10 -> 9 -> 3 -> 2 -> 1.
or
100 -> 10 -> 5 -> 4 -> 2 -> 1.
"""

def Solution(ar):
    
    cur = ar
    steps = {}
    steps[1] = ar + 1
    nextStep = []
    
    steps[ar] = 0
    nextStep.append(ar)
    
    while steps[1] == ar + 1 and len(nextStep) >= 1:
        cur = nextStep.pop(0)
        nextCur = cur
        i = 2
        while i * i <= cur:
            if cur % i == 0:
                nextCur = int(min(nextCur, max(i, cur / i)))
            i += 1
        
        if nextCur < cur:
            if nextCur not in steps:
                steps[nextCur] = steps[cur] + 1
            else:
                steps[nextCur] = min(steps[nextCur], steps[cur] + 1)
            nextStep.append(nextCur)
        
        if cur - 1 not in steps:
            steps[cur - 1] = steps[cur] + 1
        else:
            steps[cur - 1] = min(steps[cur - 1], steps[cur] + 1)
        nextStep.append(cur - 1)
    
    return steps[1]

# Return 5
print(Solution(100))
print(Solution(1000))

# Return 8
print(Solution(192993))