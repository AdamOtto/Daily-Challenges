"""
Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list.
If there is more than one possible reconstruction, return any of them.
If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox',
and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
"""
import hashlib as h

def findStr(ind, ins):
    retVal = []
    #wstart = 0
    wend = 0
    for i in range(0, len(ins) + 1):
        if ins[wend:i] in ind:
            retVal.append(ins[wend:i])
            wend = i
            
    if len(retVal) == 0:
        return None
    return retVal
    
    
#in1 = {'quick':'quick', 'brown':'brown', 'the':'the', 'fox':'fox'}
#in2 = "thequickbrownfox"

in1 = ['the', 'quick', 'brown', 'fox']
in2 = "thequickbrownfox"
d = {}
for i in in1:
    d[i] = i

print(findStr(d, in2))