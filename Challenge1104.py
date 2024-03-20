"""
Given a mapping of digits to letters (as in a phone number), and a digit string,
return all possible letters the number could represent.
You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …}
then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""
def Solution(ar, mapping):
    l = len(mapping)
    if l == 1:
        return ar[mapping]
    retVal = []
    for a in ar[mapping[0]]:
        temp = str(a)
        Helper(ar, mapping, 1, temp, retVal)
    return retVal

def Helper(ar, mapping, ind, cur, retVal):
    if ind >= len(mapping):
        retVal.append(cur)
        return 
    for a in ar[mapping[ind]]:
        Helper(ar, mapping, ind + 1, str(cur + a), retVal)
    return

# Return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
in1 = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}
print(Solution(in1, "23"))

# Return ['ak', 'al', 'bk', 'bl', 'ck', 'cl']
in1 = {'1': ['a', 'b', 'c'], '2': ['d', 'e', 'f', 'g'], '3': ['h', 'i', 'j'], '4' : ['k', 'l']}
print(Solution(in1, '14'))

# Return ['ahdk', 'ahdl', 'ahek', 'ahel', ... 'cjel', 'cjfk', 'cjfl', 'cjgk', 'cjgl']
in1 = {'1': ['a', 'b', 'c'], '2': ['d', 'e', 'f', 'g'], '3': ['h', 'i', 'j'], '4' : ['k', 'l']}
print(Solution(in1, '1324'))

# Return ['a', 'b', 'c']
in1 = {'1': ['a', 'b', 'c'], '2': ['d', 'e', 'f', 'g'], '3': ['h', 'i', 'j'], '4' : ['k', 'l']}
print(Solution(in1, '1'))