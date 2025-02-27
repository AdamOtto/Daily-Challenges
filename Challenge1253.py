"""
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""
def Solution(ar):
    stack = []
    l = len(ar)
    for i in range(l):
        if ar[i] == "(" or ar[i] == "{" or ar[i] == "[":
            stack.append(ar[i])
        if ar[i] == ")" or ar[i] == "}" or ar[i] == "]":
            temp = stack.pop()
            if temp != "(" and ar[i] == ")":
                return False
            if temp != "{" and ar[i] == "}":
                return False
            if temp != "[" and ar[i] == "]":
                return False
    if len(stack) == 0:
        return True
    return False

# Return True
print(Solution("([])[]({})"))

# Return False
print(Solution("([)]"))

# Return False
print(Solution("((()"))