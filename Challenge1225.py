"""
Given a string of parentheses, write a function to compute the minimum number
of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2, since we must remove all of them.
"""

def Solution(ar):
    openPar = 0
    closePar = 0
    l = len(ar)
    returnVal = 0
    for i in range(l):
        if ar[i] == '(':
            openPar += 1
        elif ar[i] == ')':
            closePar += 1
        else:
            return None
        
        if closePar > openPar:
            returnVal += 1
            closePar -= 1
    
    return (openPar - closePar) + returnVal

# Return 1
print(Solution("()())()"))

# Return 0
print(Solution("()()()"))

# Return 2
print(Solution(")("))

# Return 0
print(Solution("((())())"))