'''
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
'''

#Naive solution
def Solution(in1, inpStr):
    r = len(in1)
    l = len(inpStr)
    pos = []
    for i in range(0, l):
        if inpStr[i] in in1:
            tempLi = []
            tempLi.append(inpStr[i])
            for j in range(i, l):
                if inpStr[j] in in1 and inpStr[j] not in tempLi:
                    tempLi.append(inpStr[j])
                    if len(tempLi) == r:
                        pos.append(inpStr[i:j+1])
                        break
            
    if len(pos) == 0:
        return None
        
    t = len(pos[0])
    ret = pos[0]
    for i in range(1, len(pos)):
        if len(pos[i]) < t:
            ret = pos[i]
            t = len(pos[i])
            
    return ret
    
in1 = {"a", "e", "i"}
s = "figehaeci"
t = Solution(in1,s)
print(t)