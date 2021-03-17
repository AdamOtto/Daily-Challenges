"""
You're given a string consisting solely of (, ), and *.
* can represent either a (, ), or an empty string.
Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""

def Solution(arr):
    if arr == "":
        return True

    l = len(in1)

    parenCountHigh = 0
    parenCountLow = 0

    for i in range(0,l):
        if arr[i] == '(':
            parenCountHigh += 1
            parenCountLow += 1
        elif arr[i] == ')':
            parenCountHigh -= 1
            if parenCountLow > 0:
                parenCountLow -= 1
        elif arr[i] == '*':
            parenCountHigh += 1
            if parenCountLow > 0:
                parenCountLow -= 1

        if parenCountHigh < 0:
            return False

    if parenCountLow == 0:
        return True
    else:
        return False




#in1 = "(()*"
#in1 = ")*("
#in1 = "***)*("
#in1 = ""
in1 = "()()(()()*"
print(Solution(in1))