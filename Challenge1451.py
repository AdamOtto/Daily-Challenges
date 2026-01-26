"""
Given a number represented by a list of digits, find the next greater permutation of a number,
in terms of lexicographic ordering. If there is not greater permutation possible,
return the permutation with the lowest value/ordering.

For example, the list [1,2,3] should return [1,3,2].
The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory (disregarding the input memory)?
"""
# O(1) space and O(n) time
def Solution(ar):
    l = len(ar)
    i = l - 1
    while i > 0 and ar[i - 1] >= ar[i]:
        i -= 1
    
    if i <= 0:
        return list(reversed(ar))
    
    j = l - 1
    while ar[j] <= ar[i - 1]:
        j -= 1
    
    temp = ar[i - 1]
    ar[i - 1] = ar[j]
    ar[j] = temp
    
    j = l - 1
    while i < j:
        temp = ar[i]
        ar[i] = ar[j]
        ar[j] = temp
        i += 1
        j -= 1
    
    return ar

"""
Return:
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
[1, 2, 3]
"""
t = [1,2,3]
for i in range(7):
    print(t)
    t = Solution(t)

print()

"""
Return:
[1, 2, 5, 6]
[1, 2, 6, 5]
[1, 5, 2, 6]
[1, 5, 6, 2]
...
[6, 2, 5, 1]
[6, 5, 1, 2]
[6, 5, 2, 1]
[1, 2, 5, 6]
"""
t = [1,2,5,6]
for i in range(25):
    print(t)
    t = Solution(t)