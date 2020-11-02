'''
Given a list of integers and a number K, return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
'''

#O(n^2) Solution
def Solution(in1, k):
    for i in range(0, len(in1)):
        s = 0
        for j in range(i, len(in1)):
            s += in1[j]
            if s == k:
                return in1[i:j+1]
    return None

#O(n) Solution
def Solution2(in1, k):
    val = []
    for i in range(0, len(in1)):
        valSum = sum(val)
        if valSum > k:
            val.pop(0)
            valSum = sum(val)
        if valSum == k:
            return val
        val.append(in1[i])
    return None

#in1 = [1, 2, 3, 4, 5]
#k = 9
in1 = [4,2,4,5,6]
k = 11
t  = Solution(in1, k)
print(t)
t = Solution2(in1, k)
print(t)