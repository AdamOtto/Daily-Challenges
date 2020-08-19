"""
You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and the integer is the height.
Suppose it will rain and all spots between two walls get filled up.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index
(we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
"""
def Solution(in1):
    if len(in1) <= 2:
        return 0
    
    retVal = 0
    prev = in1[0]
    lastHighest = 0
    temp = 0
    
    for i in range(1, len(in1)):
        if prev <= in1[i]:
            prev = in1[i]
            lastHighest = i
            temp = 0
        else:
            retVal += prev - in1[i]
            temp += prev - in1[i]
            
    if lastHighest < len(in1):
        retVal -= temp
        prev = in1[len(in1) - 1]
        for i in range(len(in1) - 1, lastHighest - 1, -1):
            if in1[i] >= prev:
                prev = in1[i]
            else:
                retVal += prev - in1[i]
            
    print(retVal)
    
    
#in1 = [3, 0, 1, 3, 0, 5]
in1 = [1,0,2,0,3,0,4,5,6,0,8]
Solution(in1)