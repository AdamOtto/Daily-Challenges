"""
Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], “3”: [“d”, “e”, “f”], …}
then “23” should return
[“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""

def Solution(ar, val):
    retVal = []
    Helper(ar, val, 0, "", retVal)
    return retVal
    

def Helper(ar, val, ind, cur, retVal):
    if ind >= len(val):
        retVal.append(cur)
        return
    for i in range(len(ar[val[ind]])):
        Helper(ar, val, ind + 1, cur + ar[val[ind]][i], retVal)
    return

# Return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
in1 = {"2": ["a", "b", "c"], "3": ["d", "e", "f"]}
print(Solution(in1, "23"))

# Return ['adam', 'adan', 'adap', 'adbm', 'adbn', 'adbp', 'adcm', 'adcn' ... 'cfbp', 'cfcm', 'cfcn', 'cfcp']
in1 = {"1": ["a", "b", "c"], "2": ["d", "e", "f"], "3": ["g", "h", "i"], "4": ["j", "k", "l"], "5": ["m", "n", "p"]}
print(Solution(in1, "1215"))