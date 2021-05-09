"""
Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand. Find the minimum element in O(log N) time.
You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""
def Solution(ar):
    l = len(ar)
    left = 0
    right = l - 1

    while left < right:
        midpoint = left + int((right - left) / 2)

        if midpoint > 0 and ar[midpoint] < ar[midpoint - 1]:
            return midpoint
        elif ar[left] <= ar[midpoint] and ar[midpoint] > ar[right]:
            left = midpoint + 1
        else:
            right = midpoint - 1
    return ar[left]

#in1 = [7,1,2,3,4,5,6]
#in1 = [2,3,1]
#in1 = [5, 7, 10, 3, 4]
in1 = []
for i in range(0, 1000):
    in1.append(i)
for i in range(0, 150):
    in1.insert(0, in1.pop())
#print(in1)

print(Solution(in1))