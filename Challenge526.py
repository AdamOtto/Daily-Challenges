"""
You are given a string of length N and a parameter k.
The string can be manipulated by taking one of the first
k letters and moving it to the end.

Write a program to determine the lexicographically
smallest string that can be created after an unlimited number of moves.

For example, suppose we are given the string daily and k = 1.
The best we can create in this case is ailyd.
"""

def Solution(ar, k):
    arHold = list(ar.lower())
    retVal = ""
    if k > 1:
        arHold = sorted(arHold)
        return retVal.join(arHold)
    if len(arHold) > 2:
        if ord(arHold[0]) > ord(arHold[1]):
            temp = arHold.pop(0)
            arHold.append(temp)
        return retVal.join(arHold)
    else:
        return retVal.join(arHold)


# Return ailyd
print(Solution("daily", 1))

# Return dehllloorw
print(Solution("HelloWorld", 2))