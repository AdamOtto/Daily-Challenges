"""
You're given a string consisting solely of (, ), and *.
* can represent either a (, ), or an empty string.
Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""

def Solution(ar):
    if ar == "":
        return True

    l = len(ar)

    parenCountHigh = 0
    parenCountLow = 0

    for i in range(0,l):
        if ar[i] == '(':
            parenCountHigh += 1
            parenCountLow += 1
        elif ar[i] == ')':
            parenCountHigh -= 1
            if parenCountLow > 0:
                parenCountLow -= 1
        elif ar[i] == '*':
            parenCountHigh += 1
            if parenCountLow > 0:
                parenCountLow -= 1

        if parenCountHigh < 0:
            return False

    if parenCountLow == 0:
        return True
    else:
        return False

# Return True
print(Solution("(()*"))

# Return True
print(Solution("(*)"))

# Return False
print(Solution(")*("))