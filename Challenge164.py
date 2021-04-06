"""
You are given an array of length n + 1 whose elements belong to the set
{1, 2, ..., n}. By the pigeonhole principle,
there must be a duplicate. Find it in linear time and space.
"""

def Solution(in1):
    l = len(in1)
    xorCount = 0
    xorList = 0

    for i in range(1, l):
        xorCount = xorCount ^ i

    for i in range(0, l):
        xorList = xorList ^ in1[i]

    return xorCount ^ xorList



#in1 = [1,4,3,2,5,9,8,7,9,6]
#in1 = [1,2,3,4,5,6,6]
in1 = []
for i in range(1, 1001):
    in1.append(i)
in1.insert(500, 999)

print(Solution(in1))