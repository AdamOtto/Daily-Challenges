'''
Write a function that rotates a list by k elements.
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
Try solving this without creating a copy of the list. How many swap or move operations do you need?
'''

#Solution 1
"""
def Solution(in1, k):
    for i in range(0,k):
        in1.append(in1.pop(0))
    return in1
"""
#Solution 2
"""
def Solution(in1, k):
    t = in1[0:k]
    in1 = in1[k:len(in1)]
    for num in t:
        in1.append(num)
    return in1
"""
#Solution 3, len(in1) % k != 0
def Solution(in1, k):
    if len(in1) % k != 0:
        return None
        
    l = len(in1)
    step = k
    i = 0

    while i < k:
        t = in1[i]
        j = i
        while j + step < l:
            in1[j] = in1[j + step]
            j += step
        in1[j] = t
        i += 1
    return in1

#in1 = [1, 2, 3, 4, 5, 6]
#k = 2
in1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
k = 4
t = Solution(in1,k)
print(t)