'''
Given an array of integers, determine whether it contains a Pythagorean triplet.
Recall that a Pythogorean triplet (a, b, c) is defined by the equation a2+ b2= c2.
'''

# O(n^2)
def Solution(ar):
    l = len(ar)
    if l < 3:
        return False
    retVal = []
    ar = sorted(ar)
    
    for i in reversed(range(1, l)):
        j = 0
        k = i - 1
        while j < k:
            s = pow(ar[j], 2) + pow(ar[k], 2)
            if s == pow(ar[i], 2):
                retVal.append(str(ar[j]) + "^2 + " + str(ar[k]) + "^2 = " + str(ar[i]) + "^2")
                break
            elif s > pow(ar[i], 2):
                k -= 1
            elif s < pow(ar[i], 2):
                j += 1
    
    return retVal

in1 = [1,2,3,4,5]
print(Solution(in1))

in1 = [2,4,6,8,10,12,14,16,18,20]
print(Solution(in1))

in1 = [1,8,9,14,21]
print(Solution(in1))