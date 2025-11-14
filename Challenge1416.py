"""
Given a string consisting of parentheses, single digits,
and positive and negative signs, convert the string into
a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.
"""
def evaluate(val1, val2, op):
    if op == "-":
        return val1 - val2
    if op == "+":
        return val1 + val2
    
def Solution(ar):
    ar = ar.replace(" ", "")
    values = []
    operands = []
    i = 0
    while i < len(ar):
        
        if ar[i] == '(':
            operands.append(ar[i])
        elif ar[i].isdigit():
            val = 0
            while (i < len(ar) and ar[i].isdigit()):
             
                val = (val * 10) + int(ar[i])
                i += 1
            values.append(val)
            i -= 1
        elif ar[i] == ')':
            while len(operands) != 0 and operands[-1] != "(":
                val2 = values.pop()
                val1 = values.pop()
                op = operands.pop()
                values.append(evaluate(val1, val2, op))
            operands.pop()
        else:
            operands.append(ar[i])
        i += 1
    
    while len(operands) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = operands.pop()
        values.append(evaluate(val1, val2, op))
    return values[-1]

# Return 2
print(Solution("1+2+1-2"))

# Return 3
print(Solution("1 + (4-2)"))