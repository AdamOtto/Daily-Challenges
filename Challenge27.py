"""
Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.
"""

def Solution(in1):
    curly1 = 0
    curly2 = 0
    square1 = 0
    square2 = 0
    round1 = 0
    round2 = 0
    for i in in1:
        if i == '(':
            round1 += 1
        elif i == ')':
            round2 += 1
        elif i == '[':
            square1 += 1
        elif i == ']':
            square2 += 1
        elif i == '{':
            curly1 += 1
        elif i == '}':
            curly2 += 1
    if round1 == round2 and square1 == square2 and curly1 == curly2:
        print(True)
    else:
        print(False)
    
in1 = "([a])[a]({a})"
Solution(in1)