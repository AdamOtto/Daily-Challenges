"""
A cryptarithmetic puzzle is a mathematical game where the digits
of some numbers are represented by letters. Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
--------
 MONEY
may have the solution:

{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
Given a three-word puzzle like the one above, create an algorithm that finds a solution.
"""

def Solution(cryptarithmetic):
    if len(cryptarithmetic) != 3:
        return False
    d ={}
    letters = ""
    for i in cryptarithmetic[0]:
        if i not in d:
            d[i] = None
            letters += i
    for i in cryptarithmetic[1]:
        if i not in d:
            d[i] = None
            letters += i
    for i in cryptarithmetic[2]:
        if i not in d:
            d[i] = None
            letters += i

    if len(letters) > 10:
        return False

    if Helper(0, letters, d, cryptarithmetic):
        displayResults(cryptarithmetic, d)
        return True
    else:
        return False


def Helper(cur, letters, d, cryptarithmetic):
    if CheckSolution(cryptarithmetic, d):
        return True

    if cur < len(letters):
        for i in range(0, 10):
            if AssignValue(d, letters[cur], i):
                if Helper(cur + 1, letters, d, cryptarithmetic):
                    return True
        d[letters[cur]] = None
    return False

def CheckSolution( cryptarithmetic, d ):
    operand1 = 0
    operand2 = 0
    solution = 0

    l1 = len(cryptarithmetic[0])
    for i in reversed(range(0, l1)):
        if d[cryptarithmetic[0][i]] is not None:
            operand1 += pow(10, l1 - i - 1) * d[cryptarithmetic[0][i]]
        else:
            return False
    l1 = len(cryptarithmetic[1])
    for i in reversed(range(0, l1)):
        if d[cryptarithmetic[1][i]] is not None:
            operand2 += pow(10, l1 - i - 1) * d[cryptarithmetic[1][i]]
        else:
            return False
    l1 = len(cryptarithmetic[2])
    for i in reversed(range(0, l1)):
        if d[cryptarithmetic[2][i]] is not None:
            solution += pow(10, l1 - i - 1) * d[cryptarithmetic[2][i]]
        else:
            return False

    if operand1 + operand2 == solution:
        return True
    return False

def AssignValue(d, ind, val):
    for key, value in d.items():
        if value == val:
            return False
    d[ind] = val
    return True


def displayResults(cryptarithmetic, d):
    operand1 = ""
    operand2 = ""
    solution = ""

    l1 = len(cryptarithmetic[0])
    for i in range(0, l1):
        operand1 += str(d[cryptarithmetic[0][i]])
    l1 = len(cryptarithmetic[1])
    for i in range(0, l1):
        operand2 += str(d[cryptarithmetic[1][i]])
    l1 = len(cryptarithmetic[2])
    for i in range(0, l1):
        solution += str(d[cryptarithmetic[2][i]])

    print(d)
    print( str(cryptarithmetic[0]) + ":\t" + str(operand1))
    print( str(cryptarithmetic[1]) + ":\t" + str(operand2))
    print("\t+__________")
    print( str(cryptarithmetic[2]) + ":\t" + str(solution) + "\n\n")




# SEND + MORE = MONEY -> Return 2817 + 0368 = 03185
in1 = ["SEND", "MORE", "MONEY"]
print(Solution(in1))

# DUDE + HAVE = CLASS -> Return 3034 + 9654 = 12688
in1 = ["DUDE", "HAVE", "CLASS"]
print(Solution(in1))

# I + AM = IRONMAN -> return False
in1 = ["I", "AM", "IRONMAN"]
print(Solution(in1))

# AB + A = C -> return False
in1 = ["AB", "A", "C"]
print(Solution(in1))

# AB + A = BC -> Return 56 + 5 = 61
in1 = ["AB", "A", "BC"]
print(Solution(in1))