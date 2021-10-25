"""
You have access to ranked lists of songs for various users.
Each song is represented as an integer,
and more preferred songs appear earlier in each list.

For example, the list [4, 1, 7] indicates that a user likes song 4 the best,
followed by songs 1 and 7.

Given a set of these ranked lists,
interleave them to create a playlist that satisfies everyone's priorities.

For example, suppose your input is [[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]].
In this case a satisfactory playlist could be [2, 1, 6, 7, 3, 9, 5].
"""

def Solution(ar):
    maxPref = 0
    l = 0
    for a in ar:
        maxPref = max(len(a), maxPref)
        l += len(a)
    
    d = {}
    for a in ar:
        for i in range(0, len(a)):
            if a[i] in d:
                d[a[i]] += maxPref - i
            else:
                d[a[i]] = maxPref - i
    
    temp = sorted(d.items(), key=lambda x: x[1])
    retVal = []
    for i in reversed(range(len(temp))):
        retVal.append(temp[i][0])
    return retVal
    
    
in1 = [[1, 7, 3], [2, 1, 6, 7, 9], [3, 9, 5]]
print(Solution(in1))