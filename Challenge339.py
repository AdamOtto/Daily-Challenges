"""
Given an array of numbers and a number k, determine if there are three
entries in the array which add up to the specified number k.
For example, given [20, 303, 3, 4, 25] and k = 49,
return true as 20 + 4 + 25 = 49.
"""

def Solution(ar, k):
    ar = sorted(ar, reverse=True)
    l = len(ar)
    
    for i in range(l):
        count = ar[i]
        for j in range(i + 1, l):
            if count + ar[j] <= k:
                count += ar[j]
                if count == k:
                    return True
    return False
    
    

in1 = [20, 303, 3, 4, 25]
print(Solution(in1, 49))

in1 = [200,301,2,304,29,31,47,13,14,46,193,20,50,24]
print(Solution(in1, 237))