"""
Given a string and a number of lines k, print the string in zigzag form.
In zigzag, characters are printed out diagonally from top left to bottom
right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

t     a     g
 h   s z   a
  i i   i z
   s     g

"""

def Solution(ar, k):
    retVal = [""] * k
    l = len(ar)
    level = 0
    down = True
    for i in range(0, l):
        retVal[level] += ar[i]
        AddSpaces(retVal, level, k)
        if down:
            level += 1
        else:
            level -= 1
        if level < 0 or level >= k:
            down = not down
            if level < 0:
                level = 1
            else:
                level = k - 2

    for val in retVal:
        print(val)


def AddSpaces(ar,level, k):
    for i in range(0, k):
        if i != level:
            ar[i] += " "

in1 = "thisisazigzag"
k = 4
Solution(in1, k)

print()

in1 = "hello world"
k = 3
Solution(in1, k)

print()

in1 = "ThisIsATest"
k = 6
Solution(in1, k)