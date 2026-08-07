"""
Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …}
then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""
def Solution(ar, d):
    if len(ar) == 1:
        return d[ar]
    retVal = []
    for val in d[ar[0]]:
        Helper(ar, d, 1, val, retVal)
    return retVal
    
def Helper(ar, d, cur, curStr, retVal):
    if cur >= len(ar):
        retVal.append(curStr)
        return
    for val in d[ar[cur]]:
        temp = str(curStr)
        temp += val
        Helper(ar, d, cur + 1, temp, retVal)
    return
    

d = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}

# Return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
print(Solution("23", d))

# return pizza
print(Solution("74992", d)[141])
