"""
Given a string of parentheses, write a function to compute the
minimum number of parentheses to be removed to make the string valid
(i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1.
Given the string ")(", you should return 2,
since we must remove all of them.
"""
def Solution(ar):
    l = len(ar)
    count = 0
    retVal = 0
    for i in range(l):
        if ar[i] == '(':
            count += 1
        elif ar[i] == ')':
            count -= 1
        
        if count < 0:
            retVal += 1
            count = 0
    
    return retVal + abs(count)

# Return 0
print(Solution("()"))
# Return 1
print(Solution("()())()"))
# Return 2
print(Solution(")("))
# Return 3
print(Solution("(()()(("))
# Return 4
print(Solution("())))())"))