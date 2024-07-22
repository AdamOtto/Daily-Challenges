"""
Given a string, return whether it represents a number.
Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"
"""
def Solution(ar):
    ar = ar.strip().lower()
    l = len(ar)
    if l == 0:
        return False
    if l == 1:
        if ar[0] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
        return True
    
    
    flagDotE = False
    Eind = -1
    Dotind = -1
    Ecount = Dotcount = 0
    for i in range(l):
        if ar[i] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "e", "."]:
            return False
        if ar[i] == ".":
            flagDotE = True
            Dotind = i
            Dotcount += 1
        if ar[i] == "e":
            flagDotE = True
            Eind = i
            Ecount += 1
        if (ar[i] == "+" or ar[i] == "-") and i != 0:
            return False
    
    if Ecount > 1 or Dotcount > 1:
        return False
    
    if flagDotE:
        if Eind != -1 and Dotind != -1:
            if Dotind > Eind:
                return False
        if Eind != -1 and ar[Eind + 1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-"]:
            return False
        if Dotind != -1 and ar[Dotind + 1] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    
    return True    
    

# Return True
print(Solution("+10"))
print(Solution("-10"))
print(Solution("10.1"))
print(Solution("-10.1"))
print(Solution("1e5"))
print(Solution("2.5e2"))

print()

# Return False
print(Solution("a"))
print(Solution("x 1"))
print(Solution("a -2"))
print(Solution("-"))
print(Solution("100-"))
print(Solution("100.1.4"))
print(Solution("10+10"))