'''
Given an array of integers, write a function to determine whether the array could
become non-decreasing by modifying at most 1 element.
'''

def Solution(in1):
    less = 0
    i = 1
    while i < len(in1) and less < 2:
        if in1[i - 1] >= in1[i]:
            less += 1
        i += 1
    
    if less < 2:
        print(True)
    else:
        print(False)
    

in1 = [10,5,7]
Solution(in1)