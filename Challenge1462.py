"""
The expression is given as a list of numbers and operands.
For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5,
since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
"""
def Solution(ar):
    retVal = 0
    i = 0
    while i < len(ar):
        if isinstance(ar[i], str):
            temp = Helper(ar[i - 2], ar[i - 1], ar[i])
            ar.pop(i - 2)
            i -= 1
            ar.pop(i - 1)
            i -= 1
            ar.pop(i)
            ar.insert(i, temp)
        i += 1
    return ar[0]
        
def Helper(ar1, ar2, symbol):
    match symbol:
        case '+':
            return ar1 + ar2
        case '-':
            return ar1 - ar2
        case '*':
            return ar1 * ar2
        case '/':
            return ar1 / ar2
    return None

# Return 8
print(Solution([5, 3, '+']))

# Return 100
print(Solution([99, 11, 5, 5, '+', '-', '*', 1, '+']))

# Return 5.0
print(Solution([15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']))