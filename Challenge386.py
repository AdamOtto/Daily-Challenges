"""
Given a string, sort it in decreasing order based on
the frequency of characters. If there are multiple
possible solutions, return any of them.

For example, given the string tweet,
return tteew. eettw would also be acceptable.
"""


def Solution(ar):
    d = {}
    for i in ar:
        if i not in d:
            d[i] = 0
        d[i] += 1
    temp = []
    for key, val in d.items():
        temp.append( (key, val) )
    temp = sorted(temp, key=lambda x: x[1], reverse=True)
    retVal = ""

    for i in range(len(temp)):
        for j in range(temp[i][1]):
            retVal += temp[i][0]
    return retVal

print(Solution("tweet"))