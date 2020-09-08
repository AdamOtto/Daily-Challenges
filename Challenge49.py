'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Do this in O(N) time.
'''

'''
#Solution 1
def Solution(in1):
    l = len(in1)
    sums = [0]*l
    sums[0] = in1[0]
    t = 0
    for i in range(1,l):
        t1 = in1[i]
        t2 = in1[i] + sums[i-1]
        sums[i] = max(t1, t2)
        if sums[i] > t:
            t = sums[i]

    print(t)
'''
#Solution 2
def Solution(in1):
    l = len(in1)
    last = in1[0]
    t = 0
    for i in range(1,l):
        t1 = in1[i]
        t2 = in1[i] + last
        last = max(t1, t2)
        if last > t:
            t = last
    if t > 0:
        print(t)
    else:
        print(0)

#in1 = [1,2,3,4]
#in1 = [1,2,-50,3,4]
#in1 = [34, -50, 42, 14, -5, 86]
#in1 = [-20,-10,-5]
in1 = [5,-1,-1,-1,-1,5,-2,10]
Solution(in1)