"""
Given an array of strings, group anagrams together.

For example, given the following array:

['eat', 'ate', 'apt', 'pat', 'tea', 'now']
Return:

[['eat', 'ate', 'tea'],
 ['apt', 'pat'],
 ['now']]
"""
# O(nlogn)
def Solution(ar):
    retVal = []
    listRetVal = []
    hold = []
    for i in range(len(ar)):
        hold.append( (sorted(ar[i]), i) )
    
    for h in hold:
        if len(retVal) == 0:
            listRetVal.append(h[0])
            retVal.append([])
            retVal[0].append(ar[h[1]])
        else:
            i = 0
            while i < len(listRetVal):
                if h[0] == listRetVal[i]:
                    retVal[i].append(ar[h[1]])
                    break
                i += 1
            if i == len(listRetVal):
                listRetVal.append(h[0])
                retVal.append([])
                retVal[-1].append(ar[h[1]])
    return retVal
                
# Return [['eat', 'ate', 'tea'], ['apt', 'pat'], ['now']]
in1 = ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
print(Solution(in1))

# Return [['dood', 'dodo'], ['mellow', 'lowmel'], ['dirt', 'trid'], ['gosh']]
in1 = ['dood', 'mellow', 'dodo', 'dirt', 'gosh', 'lowmel', 'trid']
print(Solution(in1))