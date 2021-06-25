"""
Given an arithmetic expression in Reverse Polish Notation,
write a program to evaluate it.

The expression is given as a list of numbers and operands.
For example: [5, 3, '+'] should return 8, as 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
should return 5,
since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.
"""

def Solution(ar):
    t = []
    t.extend(ar)

    while len(t) > 1:
        i = findOperand(t)
        op = t.pop(i)
        val1 = t.pop(i - 1)
        val2 = t.pop(i - 2)
        t.insert(i - 2, Compute(op, val2, val1))
    return t[0]

def findOperand(ar):
    for i in range(0, len(ar)):
        if ar[i] == '+' or ar[i] == '-' or ar[i] == '/' or ar[i] == '*':
            return i

def Compute(operand, val1, val2):
    if operand == "+":
        return val1 + val2
    elif operand == "-":
        return val1 - val2
    elif operand == "/":
        return val1 / val2
    elif operand == "*":
        return val1 * val2

in1 = [4,5,3,'+','-']
print(Solution(in1))

in1 = [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
print(Solution(in1))