"""
Describe an algorithm to compute the longest increasing
subsequence of an array of numbers in O(n log n) time.
"""
def Solution(ar):
    l = len(ar)
    tail = [0] * l
    tail[0] = ar[0]
    cur = 1
    for i in range(1, l):
        if ar[i] < tail[0]:
            tail[0] = ar[i]
        elif ar[i] > tail[cur - 1]:
            tail[cur] = ar[i]
            cur += 1
        else:
            tail[Helper(tail, -1, cur-1, ar[i])] = ar[i]
    return cur

def Helper(tail, l, cur, ar):
    while cur - l > 1:
        temp = l + (cur - l) // 2
        if tail[temp] >= ar:
            cur = temp
        else:
            l = temp
    return cur
        

# Return 4 [0,1,2,3]
ar = [0,3,2,1,2,3]
print(Solution(ar))

# Return 100
ar = [i for i in range(0,100)]
print(Solution(ar))

# Return 19 [1:20] but missing 10
ar = [i for i in range(1,21)]
ar[10] = 0
print(Solution(ar))