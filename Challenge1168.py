"""
The 24 game is played as follows.
You are given a list of four integers, each between 1 and 9, in a fixed order.
By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses,
determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8],
you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.
"""
def Solution(ar):
    hold = []
    hold.extend(ar)
    operators = [1, 3, 5]
    for i in operators:
        hold.insert(i, "+")
    #print(hold)
    ParaCheck(hold)
    for i in range(64):
        ChangeOperators(hold, 1)
        t = ParaCheck(hold)
        if t[0]:
            return listToString(t[1])
    return False

def listToString(ar):
    retVal = ""
    for a in ar:
        retVal += str(a)
    return retVal

def ParaCheck(ar):
    hold = []
    hold.extend(ar)
    openBrac = 0
    closeBrac = 4
    temp = 0
    while closeBrac < len(hold):
        hold.insert(openBrac, "(")
        hold.insert(closeBrac, ")")
        try:
            temp = eval(listToString(hold))
        except:
            temp = 0
        if temp == 24:
            return (True, hold)
        #print(hold)
        hold = []
        hold.extend(ar)
        closeBrac += 2
    
    while openBrac < closeBrac - 2:
        hold.insert(openBrac, "(")
        hold.insert(closeBrac, ")")
        try:
            temp = eval(listToString(hold))
        except:
            temp = 0
        if temp == 24:
            return (True, hold)
        #print(hold)
        hold = []
        hold.extend(ar)
        openBrac += 2
    
    return (False, None)
    
def ChangeOperators(ar, cur):
    if cur >= len(ar):
        return
    
    if ar[cur] == "+":
        ar[cur] = "-"
    elif ar[cur] == "-":
        ar[cur] = "*"
    elif ar[cur] == "*":
        ar[cur] = "/"
    elif ar[cur] == "/":
        ar[cur] = "+"
        ChangeOperators(ar, cur + 2)
    
# Return (5*2-7)*8
print(Solution([5, 2, 7, 8]))

# Return (9+9)*8/6
print(Solution([9, 9, 8, 6]))

# Return (1-1)+1+23
print(Solution([1, 1, 1, 23]))

# Return False
print(Solution([1, 1, 1, 1]))