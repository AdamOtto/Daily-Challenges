"""
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox',
and the string "thequickbrownfox", you should return
['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',
and the string "bedbathandbeyond", return either
['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""
def Solution(d, words):
    retVal = []
    wend = 0
    words = words.lower()
    dic = {}
    for i in range(len(d)):
        dic[d[i].lower()] = d[i].lower()
    
    while wend < len(words) + 1:
        for i in range(0, len(words) + 1):
            if words[wend:i] in dic:
                retVal.append(words[wend:i])
                wend = i
        wend += 1
            
    if len(retVal) == 0:
        return None
    return retVal

# Return ['the', 'quick', 'brown', 'fox']
in1 = ['the', 'quick', 'brown', 'fox']
in2 = "thequickbrownfox"
print(Solution(in1, in2))

# Return ['bed', 'bath', 'and', 'beyond']
in1 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
in2 = "bedbathandbeyond"
print(Solution(in1, in2))

# Return ['bed', 'and', 'bath', 'and', 'beyond']
in1 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
in2 = "BEDandBATHandOHNOTHISCANTBEHEREbeyond"
print(Solution(in1, in2))