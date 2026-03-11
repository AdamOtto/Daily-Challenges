"""
Given a sorted list of integers of length N, determine if an
element x is in the list without performing any
multiplication, division, or bit-shift operations.

Do this in O(log N) time.
"""

def Solution(ar, x):
    l = len(ar)
    powersOfTwo = [1]
    
    while powersOfTwo[len(powersOfTwo) - 1] < l:
        powersOfTwo.append(powersOfTwo[len(powersOfTwo) - 1] + powersOfTwo[len(powersOfTwo) - 1])
     
    ind = 0  
    for i in reversed(powersOfTwo):
        if i + ind < l and x >= ar[ind + i]:
            ind += i
    
    return ar[ind] == x


# Return True
print(Solution([1,2,3,4,5,6,7,8,9,10],3))

# Return False
print(Solution([1, 3, 5, 12, 14, 167, 1323, 5445, 145665],20))