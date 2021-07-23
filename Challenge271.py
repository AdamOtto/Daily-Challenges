'''
Given a sorted list of integers of length N,
determine if an element x is in the list without
performing any multiplication, division, or bit-shift operations.

Do this in O(log N) time.
'''


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

# Should return True
in1 = [1,2,3,4,5,6,7,8,9,10]
x = 3
print(Solution(in1,x))

# Should return false
in1 = [1, 4, 5, 9, 11, 14, 17, 18, 21, 40]
x = 19
print(Solution(in1,x))

# Should return True
in1 = [1, 4, 5, 9, 11, 14, 17, 18, 21, 40]
x = 21
print(Solution(in1,x))