"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
# Runs in O(2n) = O(n) time, with 2n constant space.
def findLargestNonAdjSum(inp):
    # Checks input
    if len(inp) == 1 or len(inp) == 2:
        return 0
    elif len(inp) == 3:
        return max(inp[0] + inp[2], inp[1])
    
    for i in range(0, len(inp)):
        if inp[i] < 0:
            inp[i] = 0
    
    sums = [0] * len(inp)
    sums[0] = inp[0]
    sums[1] = inp[1]
    sums[2] = inp[2] + inp[0]
    
    for i in range(3, len(inp)):
        sums[i] = max(sums[i - 2] + inp[i], sums[i - 3] + inp[i])
    #print(sums)
    return max(sums[len(sums) - 1], sums[len(sums) - 2])
    
    
    """
    # Solution 2: Skip through list by 2s or 3s depending on which value is greatest.
    # Doesn't work for [1,-20,9,15,50,0,0,0,0,4]
    c = len(inp)
    sums1 = i = 0
    sums2 = j = 1
    while i < c:
        sums1 += inp[i]
        if (i + 2 < c):
            if(i + 3 < c):
                if(inp[i + 2] < inp[i + 3] ):
                    i += 3
                    continue
        i += 2
    #print(sums1)
    while j < c:
        sums2 += inp[j]
        if (j + 2 < c):
            if(j + 3 < c):
                if(inp[j + 2] < inp[j + 3] ):
                    j += 3
                    continue
        j += 2
    return max(sums1,sums2)
    """

#in1 = [5,1,1,5] #10
#in1= [1,-20,9,15,50,0,0,0,0,4] #64
in1 = [5, 5, 10, 100, 10, 5] #110
#in1 = [2, 4, 6, 2, 5] #13
#in1 = [1,50,1] #50
#in1 = [1,2,50,4] #51
#in1 = [-30,-20,1,-5,1,50,51,2] #53
print(findLargestNonAdjSum(in1))