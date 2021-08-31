"""
You are presented with an array representing a Boolean expression.
The elements are of two kinds:

- T and F, representing the values True and False.
- &, |, and ^, representing the bitwise operators for AND, OR, and XOR.

Determine the number of ways to group the array elements using parentheses
so that the entire expression evaluates to True.

For example, suppose the input is ['F', '|', 'T', '&', 'T'].
In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).

**Notes and Assumptions**
Assumption: Multi value evaluations aren't performed.
Ex: T & T & T wouldn't be (T & T & T) but instead T & (T & T) or (T & T) & T


something like ['F', '^', 'T', '|', 'F', '&', 'T'] could return
F ^ ((T | F) & T) or F ^ (T | (T & F)) or (F ^ T) | (T & F), etc
"""

import itertools

def Solution(ar):
    l = len(ar)
    operators = []
    retVal = set()
    for i in range(0, l):
        if ar[i] == '&' or ar[i] == '|' or ar[i] == '^':
            operators.append(i)
    
    perms = list(itertools.permutations(operators))
    for p in perms:
        temp = []
        temp.extend(ar)
        if Solve(temp, list(p), 0):
            temp = []
            temp.extend(ar)
            retVal.add(genStr(temp, list(p)))
    
    for r in retVal:
        print(r)
    
    return len(retVal)

def Solve(ar, p, i):
    operator = ar.pop(p[i])
    left = 'T' == ar.pop(p[i])
    right = 'T' == ar.pop(p[i] - 1)
    if operator == '&':
        t = left and right
        if t:
            t = 'T'
        else:
            t = 'F'
        ar.insert(p[i] - 1, t)
    elif operator == '|':
        t = left or right
        if t:
            t = 'T'
        else:
            t = 'F'
        ar.insert(p[i] - 1, t)
    elif operator == '^':
        t = left != right
        if t:
            t = 'T'
        else:
            t = 'F'
        ar.insert(p[i] - 1, t)
    i += 1
    if i < len(ar):
        for j in range(0, len(p)):
            if p[j] > p[i - 1]:
                p[j] -= 2
        return Solve(ar, p, i)
    else:
        return ar[0] == 'T'

def genStr(ar, p):
    ar.insert(p[0] + 2, ')')
    ar.insert(p[0] - 1, '(')
    for j in range(1, len(p)):
        if p[j] > p[0]:
            p[j] += 2
    
    for i in range(1, len(p) - 1):
        if ar[p[i] + 1] == '(':
            for j in reversed(range(p[i], len(ar))):
                if ar[j] == ')':
                    ar.insert(j, ')')
                    break
        else:
            ar.insert(p[i] + 2, ')')
    
        if ar[p[i] - 1] == ')':
            for j in range(0, p[i]):
                if ar[j] == '(':
                    ar.insert(j, '(')
                    break
        else:
            ar.insert(p[i] - 1, '(')
            
        for j in range(1, len(p)):
            if p[j] > p[i]:
                p[j] += 2

    retVal = ""
    for s in ar:
        retVal += s
    return retVal
    
    
    

# Returns: 2
in1 = ['F', '|', 'T', '&', 'T']
print(Solution(in1))

print()

# Returns: 5
in1 = ['F', '^', 'T', '|', 'F', '&', 'T'] 
print(Solution(in1))

print()

# Returns: 0
in1 = ['F', '|', 'F', '&', 'T'] 
print(Solution(in1))