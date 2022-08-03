"""
Implement regular expression matching with the following special characters:
    . (period) which matches any single character
    * (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and
returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray",
your function should return true. The same regular expression on the string "raymond"
should return false.
"""

def Solution(regex, str):
    m = len(regex)
    n = len(str)

    if m == 0:
        return n == 0

    lookup = [ [False for i in range(m + 1)] for j in range(n + 1) ]

    lookup[0][0] = True

    for i in range(1, m + 1):
        if regex[i - 1] == '*':
            lookup[0][i] = lookup[0][i - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if regex[j - 1] == '*':
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]
            elif regex[j - 1] == "." or str[i - 1] == regex[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1]
            else:
                lookup[i][j] = False

    return lookup[n][m]

# Return True
print(Solution("al*a", "alllllllla"))
# Return False
print(Solution("a*f", "alllllllla"))
# Return True
print(Solution("a....", "abcde"))
# Return False
print(Solution("a....", "abcdef"))
# Return True
print(Solution("Hel*W*or..", "HelloWorld"))

