"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13,
since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
def Solution(ar):
    l = len(ar)
    temp = [0 for i in range(l)]
    temp[0] = ar[0]
    temp[1] = ar[1]
    
    for i in range(2, l):
        temp[i] = max( max(temp[0:i - 1]) + ar[i], max(temp[0:i - 1]), ar[i])
    
    return max(temp)
    

# Return 13
print(Solution( [2, 4, 6, 2, 5] ))

# Return 10
print(Solution( [5, 1, 1, 5] ))

# Return 8
print(Solution( [3, 1, -2, 0, 3, 5, -1] ))