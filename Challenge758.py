"""
Write a function that rotates a list by k elements.
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
Try solving this without creating a copy of the list.
How many swap or move operations do you need?
"""
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

# [5, 6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4]
print(Solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],4))