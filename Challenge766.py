"""
You are given a string consisting of the letters x and y, such as xyxxxyxyy.
In addition, you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this
operation to ensure that all x's come before all y's.
In the preceding example, it suffices to flip the second
and sixth characters, so you should return 2.

Assumption:
Don't need to have the same number of x's and y's after all flips are performed.
"""
def Solution(ar):
    if check(ar):
        return 0
    arl = list(ar)
    retVal = 0
    x = 0
    y = len(ar) - 1
    
    while x < y:
        if arl[x] == "y":
            retVal += 1
            arl[x] = "x"
            if check(arl):
                break
        if arl[y] == "x":
            retVal += 1
            arl[y] = "y"
            if check(arl):
                break
        x += 1
        y -= 1
    return retVal

def check(ar):
    x = 0
    y = len(ar) - 1
    for i in range(len(ar)):
        if ar[x] == "x":
            x += 1
        if ar[y] == "y":
            y -= 1
    if x >= y:
        return True
    return False


# Return 2
print(Solution("xyxxxyxyy"))

# Return 0
print(Solution("xxxyyy"))

# Return 1
print(Solution("xyxyyy"))

# Return 4
print(Solution("yyyyxx"))

# Return 27
print(Solution("xyyxxyxyxxyxyyyxyyyyxxyyyyxyxyxxyxyyyxyxyxyyxyxyyyyyyxyyyxy"))