"""
Given two sorted iterators, merge it into one iterator.

For example, given these two iterators:

foo = iter([5, 10, 15])
bar = iter([3, 8, 9])
You should be able to do:

for num in merge_iterators(foo, bar):
    print(num)

# 3
# 5
# 8
# 9
# 10
# 15
"""

def Solution(iter1, iter2):
    l1 = list(iter1)
    l2 = list(iter2)
    retVal = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            retVal.append(l1[i])
            i += 1
        elif l1[i] >= l2[j]:
            retVal.append(l2[j])
            j += 1
    
    if j == len(l2):
        while i < len(l1):
            retVal.append(l1[i])
            i += 1
    elif i == len(l1):
        while j < len(l2):
            retVal.append(l2[i])
            j += 1
    
    return iter(retVal)
    
in1 = iter([5, 10, 15])
in2 = iter([3, 8, 9])
for num in Solution(in1, in2):
    print(num)
