'''
Given an array of numbers, find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.
'''

def Solution(in1):
    retVal = 0
    for i in range(0, len(in1)-1):
        t = 0
        t = helper(in1, i + 1, in1[i]) + 1
        if retVal < t:
            retVal = t
    print(retVal)
    
def helper(in1, cur, last):
    
    if cur == len(in1) - 1:
        if last < in1[cur]:
            return 1
        else:
            return 0
    
    if last < in1[cur]:
        #Case where we use current val in subsequence array
        t1 = helper(in1, cur + 1, in1[cur]) + 1
        #Case where we skip over this, in case of a better subsequence array
        t2 = helper(in1, cur + 1, last)
        #Return whichever is the longest
        return max(t1,t2)
    else:
        t = helper(in1, cur + 1, last)
        return t
        

in1 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Solution(in1)