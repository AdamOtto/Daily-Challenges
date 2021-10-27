"""
A strobogrammatic number is a positive number that appears
the same after being rotated 180 degrees.

For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

def Solution(N):
    return Helper(N, N)

def Helper(cur, N):
    if cur == 0:
        return [""]
    if cur == 1:
        return ["0", "1", "8"]
    
    mid = Helper(cur - 2, N)
    retVal = []
    
    for i in range(len(mid)):
        if cur < N:
            retVal.append("0" + mid[i] + "0")
        retVal.append("1" + mid[i] + "1")
        retVal.append("8" + mid[i] + "8")
        retVal.append("6" + mid[i] + "9")
        retVal.append("9" + mid[i] + "6")
    return retVal

# Return ['11', '88', '69', '96']
print(Solution(2))
# Return ['101', '808', '609', '906', '111', '818', '619', '916', '181', '888', '689', '986']
print(Solution(3))