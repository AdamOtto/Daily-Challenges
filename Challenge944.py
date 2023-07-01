"""
Given an integer, find the next permutation of it in absolute order.
For example, given 48975, the next permutation would be 49578.
"""
def Solution(ar):
    arStr = str(ar)
    l = len(arStr)
    for i in reversed(range(1, l - 1)):
         if arStr[i] > arStr[i-1]:
             break
    
    if i == 1 and arStr[i] <= arStr[i-1]:
         return None
    
    x = arStr[i-1]
    smallest = i
    for j in range(i+1,l):
        if arStr[j] > x and arStr[j] < arStr[smallest]:
            smallest = j

    arStr = list(arStr)  
    arStr[smallest],arStr[i-1] = arStr[i-1], arStr[smallest]
    arStr = arStr[:i] + sorted(arStr[i:])
    
    return int("".join(arStr))

# Return 49578
print(Solution(48975))

# Return None
print(Solution(100))

# Return 31777
print(Solution(17737))