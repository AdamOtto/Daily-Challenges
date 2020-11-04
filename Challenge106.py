'''
Given an integer list where each number represents the number of hops you can make,
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.
'''

#Solution 1
'''
def Solution(in1):
    return Helper(0,in1)
    
    
def Helper(cur, in1):
    
    if cur > len(in1) - 1:
        return False
    if cur == len(in1) - 1:
        return True
        
    for i in range(1, in1[cur] + 1):
        if Helper(cur + i, in1):
            return True
    return False
'''
#Solution 2
def Solution(in1):
    n = len(in1)
    jumps = [0] * n
    
    if in1[0] == 0:
        return False
    
    for i in range(1, n): 
        jumps[i] = float('inf') 
        for j in range(i):
            if (i <= j + in1[j]) and (jumps[j] != float('inf')): 
                jumps[i] = min(jumps[i], jumps[j] + 1) 
                break
    if jumps[n-1] == float('inf'):
        return False
    else:
        return True

in1 = [1,3,0,2,0,2,0,1,1]
print(Solution(in1))