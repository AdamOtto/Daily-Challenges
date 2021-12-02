"""
You are given a list of jobs to be done, where each job is
represented by a start time and end time.
Two jobs are compatible if they don't overlap.
Find the largest subset of compatible jobs.

For example, given the following jobs (there is no guarantee that jobs will be sorted):

[(0, 6),
(1, 4),
(3, 5),
(3, 8),
(4, 7),
(5, 9),
(6, 10),
(8, 11)]
Return:

[(1, 4),
(4, 7),
(8, 11)]

Note:
Help from https://cppcodingzen.com/?p=319
"""

def Solution(ar):
    ar = sorted(ar, key=lambda x:x[0])
    table = []
    next = []
    for i in range(len(ar)):
        table.append(1)
        next.append(i)
        
    highest = 1
    bestStart = 0
    for i in reversed(range(len(ar) - 2)):
        for j in range(i + 1, len(ar)):
            if rangeIn(ar[i], ar[j]):
                continue
            if table[j] + 1 > table[i]:
                table[i] = table[j] + 1
                next[i] = j
            if table[i] > highest:
                highest = table[i]
                bestStart = i
    
    retVal = []
    cur = bestStart
    for i in range(highest):
        retVal.append(ar[cur])
        cur = next[cur]
    return retVal

def rangeIn(rng1, rng2):
    t = range(rng1[0], rng1[1])
    if rng2[0] in t or rng2[1] in t:
        return True
    return False
    
# Return [(1, 4), (4, 7), (8, 11)]
in1 = [(0, 6),(1, 4),(3, 5),(3, 8),(4, 7),(5, 9),(6, 10),(8, 11)]
print(Solution(in1))
