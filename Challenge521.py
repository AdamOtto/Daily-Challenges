"""
Given a string and a number of lines k,
print the string in zigzag form.
In zigzag, characters are printed out diagonally
from top left to bottom right until reaching the kth line,
then back up to top right, and so on.

For example, given the sentence "thisisazigzag"
and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g
"""

def Solution(ar, k):
    prtStr = [[" " for i in range(len(ar))] for j in range(k)]
    delta = 1
    curx = 0
    cury = 0
    
    while curx < len(ar):
        prtStr[cury][curx] = ar[curx]
        curx += 1
        cury += delta
        if cury >= k:
            cury -= 2
            delta = delta * -1
        elif cury < 0:
            cury += 2
            delta = delta * -1
    for i in range(len(prtStr)):
        print("".join(prtStr[i]))

Solution("thisisazigzag", 4)
print()
Solution("HelloWorld!", 2)
print()
Solution("abcdefghijklmnopqrstuvwxyz", 7)