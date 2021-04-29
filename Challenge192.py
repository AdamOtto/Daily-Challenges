"""
You are given an array of nonnegative integers.
Let's say you start at the beginning of the array and are trying
to advance to the end. You can advance at most, the number of steps
that you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1],
we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""

def Solution(ar):
    n = len(ar)
    return Helper(ar, 0, n)

def Helper(ar, cur, n):
    if cur == n - 1:
        return True
    temp = []
    for i in range(cur + 1, min(n, cur + ar[cur] + 1)):
        temp.append( (ar[i], i) )
    temp.sort(key = lambda a:a[0], reverse=True)
    #print(temp)
    for t in temp:
        if Helper(ar, t[1], n):
            return True
    return False

#in1 = [1, 3, 1, 2, 0, 1]
in1 = [10,0,2,0,1,3,0,0,0]
print(Solution(in1))