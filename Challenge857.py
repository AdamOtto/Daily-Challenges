"""
You are given a binary tree in a peculiar string representation.
Each node is written in the form (lr), where l corresponds to the left child
and r corresponds to the right child.

If either l or r is null, it will be represented as a zero.
Otherwise, it will be represented by a new (lr) pair.

Here are a few examples:

A root node with no children: (00)
A root node with two children: ((00)(00))
An unbalanced tree with three consecutive left children: ((((00)0)0)0)

Given this representation, determine the depth of the tree.
"""
def findBrackets(ar):
    f = FindOpeningBracket(ar)
    l = None
    if f is not False:
        l = findClosingBracket(ar, f)
    else:
        return False
    if l  is not False:
        return (f, l)
    else:
        return False

def findBracketsReverse(ar):
    openBrac = 0
    closedBrac = 1
    for i in reversed(range(len(ar) - 1)):
        if ar[i] == "(":
            openBrac += 1
        elif ar[i] == ")":
            closedBrac += 1
        if openBrac == closedBrac:
            return (i, len(ar) - 1)
    return False
    

def findClosingBracket(ar, firstBracket):
    openBrac = 1
    closedBrac = 0
    for i in range(firstBracket + 1, len(ar)):
        if ar[i] == "(":
            openBrac += 1
        elif ar[i] == ")":
            closedBrac += 1
        if openBrac == closedBrac:
            return i
    return False

def FindOpeningBracket(ar):
    for i in range(len(ar)):
        if ar[i] == "(":
            return i
    return False

def Solution(ar):
    bracs = findBrackets(ar)
    cur = ar[bracs[0] + 1: bracs[1]]
    l = 0
    r = 0
    if cur[0] != "0":
        bracs = findBrackets(cur)
        l = Solution(cur[bracs[0]: bracs[1] + 1])
    if cur[-1] != "0":
        bracs = findBracketsReverse(cur)
        r = Solution(cur[bracs[0]: bracs[1] + 1])
    return max(l, r) + 1


# Return 1
print(Solution("(00)"))
# Return 2
print(Solution("((00)(00))"))
# Return 4
print(Solution("((((00)0)0)0)"))
# Return 3
print(Solution("(((00)(00))((00)(00)))"))