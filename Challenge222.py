"""
Given an absolute pathname that may have . or .. as part of it, return the shortest standardized path.

For example, given "/usr/bin/../bin/./scripts/../", return "/usr/bin/".
"""


def Solution(ar):
    dirs = ar.split("/")
    retVal = []
    #print(dirs)
    for d in dirs:
        if d == "..":
            retVal.pop()
        elif d != ".":
            retVal.append(d)

    s = "/"
    for i in range(len(retVal)):
        if retVal[i] != "":
            s += str(retVal[i]) + "/"
    return s

in1 = "/usr/bin/../bin/./scripts/../"
print(Solution(in1))
in1 = "/Home/Desktop/../Document/Images/../Homework/"
print(Solution(in1))