"""
Given a list of integers, write a function that returns the
largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def Solution(ar):
    l = len(ar)
    # Checks input
    if l == 1 or l == 2:
        return 0
    elif l == 3:
        return max(ar[0] + ar[2], ar[1])
    
    for i in range(0, l):
        if ar[i] < 0:
            ar[i] = 0
    
    sums = [0] * l
    sums[0] = ar[0]
    sums[1] = ar[1]
    sums[2] = ar[2] + ar[0]
    
    for i in range(3, l):
        sums[i] = max(sums[i - 2] + ar[i], sums[i - 3] + ar[i])
    #print(sums)
    return max(sums[len(sums) - 1], sums[len(sums) - 2])

# Return 13
print(Solution([2, 4, 6, 2, 5]))

# Return 10
print(Solution([5, 1, 1, 5]))

# Return 137
print(Solution([1,1,1,3,1,4,80,29,10,11,41,12,1,1,1]))