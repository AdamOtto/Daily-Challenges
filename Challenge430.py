"""
Given a string of parentheses, find the balanced
string that can be produced from it using the minimum number
of insertions and deletions. If there are multiple solutions,
return any of them.

For example, given "(()", you could return "(())".
Given "))()(", you could return "()()()()".
"""

#O(n)
def Solution(par):

    openPar = 0
    closePar = 0
    balancedPar = par
    # Fill in open parentheses
    for p in balancedPar:
        if p == '(':
            openPar += 1
        elif p == ')' and closePar < openPar:
            closePar += 1
    for i in range(0, openPar - closePar):
        balancedPar += ")"

    # Fill in closed parentheses
    openPar = 0
    closePar = 0
    i = 0
    while i < len(balancedPar):
        if balancedPar[i] == ')':
            closePar += 1
        elif balancedPar[i] == '(':
            openPar += 1

        if closePar > openPar:
            balancedPar = balancedPar[0:i] + "(" + balancedPar[i:len(balancedPar)]
            openPar += 1
            i += 1
        i += 1
    print(balancedPar)

# Return (())
in1 = "(()"
Solution(in1)

# Return ()()()()
in1 = "))()("
Solution(in1)

# Return (()()())()
in1 = "(()()()))"
Solution(in1)