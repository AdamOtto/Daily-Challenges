"""
Given a list of strictly positive integers,
partition the list into 3 contiguous partitions which
each sum up to the same value. If not possible, return null.

For example, given the following list:

[3, 5, 8, 0, 8]
Return the following 3 partitions:

[[3, 5], [8, 0], [8]]
Which each add up to 8.
"""
# O(n)
def Solution(ar):
    left = int(len(ar) / 3)
    right = int(2 * len(ar) / 3)
    """
    print("Left:", left, ", right:", right)
    print(ar[0:left])
    print(ar[left:right])
    print(ar[right:])
    """
    for i in range(len(ar)):
        l = sum(ar[0:left])
        m = sum(ar[left:right])
        r = sum(ar[right:])
        if l == m and m == r:
            return [ar[0:left], ar[left:right], ar[right:]]
        if l < m and r < m:
            if l < m:
                left += 1
                left = max(0, left)
            else:
                right -= 1
        elif l > m:
            left -= 1
        elif r > m:
            right += 1
            right = min(right, len(ar) - 1)
    return False

#Return [[3, 5], [8], [0, 8]]
print(Solution([3, 5, 8, 0, 8]))

#Return False
print(Solution([1,2,3,3,2,1]))

#Return [[1, 2, 3, 0, 0, 0, 0, 2, 1], [1, 2, 3, 2, 0, 0, 1], [1, 2, 0, 3, 2, 1]]
print(Solution([1,2,3,0,0,0,0,2,1,1,2,3,2,0,0,1,1,2,0,3,2,1]))

#Return [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [1], [1]]
print(Solution([0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]))