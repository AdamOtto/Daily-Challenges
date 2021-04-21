"""
Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""

def Solution(in1):
    d = {}

    for i in range(0, len(in1)):
        d[in1[i]] = 0
        for j in range(0, len(in1)):
            if in1[j] % in1[i] == 0:
                d[in1[i]] += 1
    retVal = None
    count = None
    for key, val in d.items():
        if retVal is None or count < val:
            count = val
            retVal = key
    return retVal



in1 = [42, 56, 14]
print(Solution(in1))