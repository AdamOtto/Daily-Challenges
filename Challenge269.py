'''
You are given an string representing the initial conditions of some dominoes.
Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling.
Note that if a domino receives a force from the left and right side simultaneously,
it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLLL

Given the string ..R...L.L, you should return ..RR.LLLL
'''

def Solution(ar):
    l = len(ar)
    retVal = ""
    oldL = []
    newL = list(ar)
    
    while oldL != newL:
        oldL = newL
        newL = ["."] * l
        for i in range(0, l):
            if i == 0:
                newL[i] = Helper(".", oldL[i], oldL[i+1])
            elif i == l - 1:
                newL[i] = Helper(oldL[i-1], oldL[i], ".")
            else:
                newL[i] = Helper(oldL[i-1], oldL[i], oldL[i+1])
    return retVal.join(newL)
    
def Helper(L, cur, R):
    if L == "." and R ==".":
        return cur
    if L == "L" and R ==".":
        return cur
    if L == "." and R =="L":
        return "L"
    if L == "R" and R ==".":
        return "R"
    if L == "." and R =="R":
        return cur
    if (L == "L" and R =="R") or (L == "R" and R =="L"):
        return cur
    if L == "R" and R == "R":
        return "R"
    if L == "L" and R == "L":
        return "L"

in1 = ".L.R....L"
print(Solution(in1))

in1 = "..R...L.L"
print(Solution(in1))