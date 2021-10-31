"""
Given a string s, rearrange the characters so that any
two adjacent characters are not the same.
If this is not possible, return null.

For example, if s = yyz then return yzy.
If s = yyy then return null.
"""

def Solution(s):
    
    d = {}
    ar = list(s)
    l = len(ar)
    largest = None
    for i in range(l):
        if ar[i] in d:
            d[ar[i]] += 1
        else:
            d[ar[i]] = 1
    largest = getLargest(d)
    retVal = [None] * l
    i = 0
    while i < l and d[largest] > 0:
        retVal[i] = largest
        d[largest] -= 1
        i += 2
    
    if i < l:
        newLargest = getLargest(d)
        while i < l and d[newLargest] > 0:
            retVal[i] = newLargest
            d[newLargest] -= 1
            i += 2
    
    i = 1
    while i < l:
        largest = getLargest(d)
        d[largest] -= 1
        retVal[i] = largest
        i += 2
    
    for i in range(1, l):
        if retVal[i] == None:
            return None
        if retVal[i - 1] == retVal[i]:
            return None
    return "".join(retVal)
  
def getLargest(d):
    largest = None
    largestCount = 0
    for key, val in d.items():
            if val > largestCount:
                largestCount = val
                largest = key
    return largest
 
# Return yxy
print(Solution("yyx"))

# Return None
print(Solution("yyyx"))

# Return bcbdbabcbda
print(Solution("abbcbddbabc"))
