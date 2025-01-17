"""
Given a string, find the palindrome that can be made by inserting the fewest number
of characters as possible anywhere in the word.
If there is more than one palindrome of minimum length that can be made,
return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace",
since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters,
but "ecarace" comes first alphabetically.

As another example, given the string "google",
you should return "elgoogle".
"""

def Solution(ar):
    subStrPalindromes = []
    l = len(ar)
    for i in range(l):
        temp = findPalindromes(ar, i)
        if temp is not None:
            subStrPalindromes.append(temp)
    
    #If no palindromes found, add n - 1 to the substring and find lexicographically earliest one.
    if len(subStrPalindromes) == 0:
        return getWorstCasePalindromes(ar)
    else:
        palindromes = []
        for s in subStrPalindromes:
            pal = ""
            for i in range(s[0][0], l):
                if i >= s[0][0] and i <= s[0][1]:
                    pal += ar[i]
                elif i > s[0][0] and i > s[0][1]:
                    pal = ar[i] + pal + ar[i]
            pal = ar[0:s[0][0]] + pal + "".join(reversed(ar[0:s[0][0]]))
            if ar in pal:
                palindromes.append(pal)
        if len(palindromes) == 0:
            return getWorstCasePalindromes(ar)
        palindromes = sorted(palindromes, key=len)
        temp2 = []
        l2 = len(palindromes[0])
        for i in palindromes:
            if len(i) == l2:
                temp2.append(i)
        temp2 = sorted(temp2)
        return temp2[0]

def getWorstCasePalindromes(ar):
    l = len(ar)
    str1 = str2 = ar
    for i in range(1,l):
        str1 = ar[i] + str1
    for i in reversed(range(0, l - 1)):
        str2 = str2 + ar[i]
    if ord(str1[0]) < ord(str2[0]):
        return str1
    return str2
        
def findPalindromes(ar, cur):
    low = cur
    high = len(ar) - 1 
    possiblePalindromeFound = False
    retVal = None
    while low < high:
        if ar[low] == ar[high]:
            if not possiblePalindromeFound:
                retVal = (low, high)
            possiblePalindromeFound = True
            low += 1
        else:
            possiblePalindromeFound = False
        high -= 1
    if possiblePalindromeFound:
        return (retVal, ar[retVal[0]: retVal[1] + 1])
    return None

#Return ecarace
print(Solution("race"))

#Return elgoogle 
print(Solution("google"))
print(Solution("elgoog"))

#Return awselleswa 
print(Solution("awselle"))
print(Solution("elleswa"))
print(Solution("selleswa"))

#Return agooglelgooga
print(Solution("agoogle"))