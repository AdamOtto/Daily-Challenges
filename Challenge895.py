"""
Given a string which we can delete at most k,
return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2,
you could delete f and x to get 'waterretaw'.
"""

def Solution(ar, k):
    i = 0
    j = len(ar) - 1
    removed = 0
    palin = ar
    while i <= j:
        if palin[i] != palin[j]:
            removed += 1
            if findClosestj(palin, i, j) < findClosesti(palin, i, j):
                palin = palin[0:j] + palin[j+1:len(palin)]
            else:
                palin = palin[0:i] + palin[i + 1:len(palin)]
            j -= 1
        else:
            i += 1
            j -= 1
        if removed > k:
            return False
    return palin
    
def findClosestj(ar, i, j):
    for ind in reversed(range(0, j)):
        if ar[i] == ar[ind]:
            return j - ind
    return len(ar)

def findClosesti(ar, i, j):
    for ind in range(i, j):
        if ar[j] == ar[ind]:
            return ind - i
    return len(ar)
 
# Return waterretaw
in1 = 'waterrfetawx'
k = 2
print(Solution(in1, k))

# Return abccba
in1 = 'dcabccba'
k = 100
print(Solution(in1, k))

# Return False
in1 = 'dcabccba'
k = 1
print(Solution(in1, k))

# Return sfjwwjfs
in1 = 'abfkslfjkwwelrjfks'
k = 100
print(Solution(in1, k))