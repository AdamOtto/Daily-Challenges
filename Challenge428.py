"""
You have N stones in a row, and would like to create from them a pyramid.
This pyramid should be constructed such that the height of each stone
increases by one until reaching the tallest stone, after which the heights
decrease by one. In addition, the start and end stones of the pyramid
should each be one stone high.

You can change the height of any stone by paying a cost of 1 unit to lower
its height by 1, as many times as necessary. Given this information,
determine the lowest cost method to produce this pyramid.

For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is
to pay 2 to create [0, 1, 2, 3, 2, 1].
"""

import sys

def Solution(ar):
    l = len(ar)
    count = 0
    
    # Find max element in array
    maxElem = max(ar)
    
    # Find a potential site for the peak
    peakInd = []
    while len(peakInd) == 0:
        for i in range(1, l - 1):
            if ar[i] == maxElem:
                if (ar[i] - ar[i - 1] == 1 or  ar[i] - ar[i - 1] == 0) and (ar[i] - ar[i + 1] == 1 or  ar[i] - ar[i + 1] == 0):
                    peakInd.append(i)
        # If no suitable peaks found, reduce the max element and try again.
        if len(peakInd) == 0:
            for i in range(l):
                if ar[i] == maxElem:
                    ar[i] -= 1
                    count += 1
            maxElem -= 1
        
    retVal = sys.maxsize
    retPyramid = None
    # Take all possible peaks and create a pyramid.  Save the lowest count.
    for peak in peakInd:
        temp = []
        temp.extend(ar)
        tempCount = Helper(temp, peak, l) + count
        if Validate(temp):
            t = min(retVal, tempCount)
            if t < retVal:
                retVal = t
                retPyramid = temp
            #print(temp)
    if retVal == sys.maxsize:
        return None
    return (retVal, temp)
    
def Helper(ar, peak, l):
    low = peak - 1
    hi = peak + 1
    count = 0
    while low >= 0 and hi < l:
        # reduce each stone to the left.
        if ar[low] != 0:
            if ar[low + 1] - ar[low] < 0:
                t = ar[low] - (ar[low + 1] - 1)
                ar[low] -= t
                count += t
            elif ar[low + 1] - ar[low] == 0:
                ar[low] -= 1
                count += 1
            elif ar[low + 1] - ar[low] > 1:
                ar[peak] -= 1
                count += 1
                low = peak - 1
                hi = peak + 1
                continue
        
        # reduce each stone to the right.
        if ar[hi] != 0:
            if ar[hi - 1] - ar[hi] < 0:
                t = ar[hi] - (ar[hi - 1] - 1)
                ar[hi] -= t
                count += t
            elif ar[hi - 1] - ar[hi] == 0:
                ar[hi] -= 1
                count += 1
            elif ar[hi - 1] - ar[hi] > 1:
                ar[peak] -= 1
                count += 1
                low = peak - 1
                hi = peak + 1
                continue
        
        if ar[low] < 0:
            count += ar[low]
            ar[low] = 0
        if ar[hi] < 0:
            count += ar[hi]
            ar[hi] = 0
        
        low -= 1
        hi += 1
        
    if hi >= l:
        for i in range(0, low + 1):
            count += ar[i]
            ar[i] -= ar[i]
    elif low <= 0:
        for i in range(hi, l):
            count += ar[i]
            ar[i] -= ar[i]
    return count
    
def Validate(pyramid):
    l = len(pyramid)
    peak = max(pyramid)
    peakFound = False
    for i in range(1, l):
        if not peakFound:
            if pyramid[i] != 0:
                if pyramid[i] - pyramid[i - 1] != 1:
                    return False
        if pyramid[i] == peak:
            peakFound = True
            continue
        if peakFound:
            if pyramid[i] != 0:
                if pyramid[i - 1] - pyramid[i] != 1:
                    return False
    return True


# Returns 2
in1 = [1, 1, 3, 3, 2, 1]
print(Solution(in1))

# Returns 7
in1 = [1, 3, 5, 5, 5, 3, 1]
print(Solution(in1))

# Returns 12
in1 = [2,1,3,4,5,4,2,3,4]
print(Solution(in1))

# Returns 20
in1 = [10,0,0,0,1,0,0,0,10]
print(Solution(in1))

# Returns 10
in1 = [10,0,0,0,0,0,0,0,0]
print(Solution(in1))

# Returns 7
in1 = [2,0,0,2,0,0,2,0,2]
print(Solution(in1))

# Returns 73
in1 = [9,2,3,1,4,5,6,4,6,1,2,4,1,2,1,6,5,6,4,3,4,2,8]
print(Solution(in1))