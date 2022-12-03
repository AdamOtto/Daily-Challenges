"""
Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""
def Solution(in1):
    l = len(in1)
    palindromes = []
    for i in range(0,l):
        for j in reversed(range(i, l)):
            if in1[i] == in1[j] and i != j:
                t = findPalindrome(in1,i,j)
                if t is not None:
                    palindromes.append(t)
    
    t = 0
    index = 0
    for i in range(0, len(palindromes)):
        if len(palindromes[i]) > t:
            t = len(palindromes[i])
            index = i
            
    return palindromes[index]
    
    
def findPalindrome(in1,index1,index2):
    i = index1
    j = index2
    
    while i <= j:
        if in1[i] != in1[j]:
            return None
        i += 1
        j -= 1
    return in1[index1:index2 + 1]


# Return bcdcb
print(Solution("aabcdcb"))

# Return anana
print(Solution("bananas"))