"""
Given a positive integer N, find the smallest number of steps it will take to reach 1.

There are two kinds of permitted steps:

You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route:
100 -> 10 -> 9 -> 3 -> 2 -> 1.
"""
def Solution(ar):
    q = []
    d = {}
    retVal = ar
    q.append( (ar - 1, 1) )
    d[ar - 1] = 1
    Helper(ar, q, 0, d)
    
    while len(q) > 0:
        temp = q.pop(0)
        if temp[0] == 1:
            retVal = min(retVal, temp[1])
            continue
        if temp[0] - 1 not in d or d[temp[0] - 1] > temp[1] + 1:
            q.append( (temp[0] - 1, temp[1] + 1) )
            d[temp[0] - 1] = temp[1] + 1
        Helper(temp[0], q, temp[1], d)
    return retVal
    
def Helper(ar, q, step, d):
    for i in range(2, ar):
        if ar % i == 0:
            temp = max(i, int(ar / i) )
            if temp not in d or d[temp] > step + 1:
                q.append( (temp, step + 1) )
                d[temp] = step + 1
            
# Return 5
print(Solution(100))

# Return 4
print(Solution(256))

# Return 7
print(Solution(877))