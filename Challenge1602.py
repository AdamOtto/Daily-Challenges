"""
You are given a string consisting of the letters x and y, such as xyxxxyxyy.
In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to
ensure that all x's come before all y's.
In the preceding example, it suffices to flip the second and sixth characters, so you should return 2.
"""
def Solution(ar):
    lastx = len(ar)
    xCount = 0
    
    for i in reversed(range(0, len(ar))):
        if ar[i] == 'x':
            lastx = i
            break
    
    if lastx == len(ar):
        return 1
    
    retVal = 0
    for i in range(0, lastx):
        if ar[i] == 'y':
            retVal += 1
    return retVal

# Return 2
print(Solution('xyxxxyxyy'))
# Return 1
print(Solution('yyy'))
# Return 3
print(Solution('yyyxyyy'))
# Return 6
print(Solution('xxyxxxxyyxyyyxxyyyyy'))
# Return 6
print(Solution('yyyxyyyxy'))
# Return 0
print(Solution('xxxyyy'))
# Return 4
print(Solution("yyyyxx"))
# Return 1
print(Solution("xyxyyy"))