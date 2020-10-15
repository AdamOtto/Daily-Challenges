'''
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed
to make the string valid (i.e. each open parenthesis is eventually closed).
'''

def Solution(parentheses):
    count = 0
    lp = 0
    rp = 0
    for p in parentheses:
        if p is ')':
            rp += 1
            if rp > lp:
                rp -= 1
                count += 1
        elif p is '(':
            lp += 1

    if lp != rp:
        count += abs(lp - rp)
    print(count)

in1 = "(()())(()()"
Solution(in1)