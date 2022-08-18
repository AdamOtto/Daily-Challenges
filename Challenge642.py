"""
A step word is formed by taking a given word,
adding a letter, and anagramming the result.

For example, starting with the word "APPLE",
you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word,
create a function that returns all valid step words.
"""

def Solution(d, ar):
    ar = ar.upper()
    l = len(d)
    retVal = []
    d1 = {}
    
    for i in range(len(ar)):
        if ar[i] not in d1:
            d1[ar[i]] = 1
        else:
            d1[ar[i]] += 1
    
    
    for i in range(l):
        d[i] = d[i].upper()
        d2 = {}
        if len(d[i]) == len(ar) + 1:
            for j in range(len(d[i])):
                if d[i][j] not in d2:
                    d2[d[i][j]] = 1
                else:
                    d2[d[i][j]] += 1
            count = 0
            for key,val in d2.items():
                if key in d1:
                    val = abs(val - d1[key])
                count += val
            
            if count == 1:
                retVal.append(d[i])
    return retVal
    


# Return ['APPEAL']
print(Solution(["ARGON", "AXE", "APPEAL", "READY", "HIPPO"], "APPLE"))

# Return ['SMELL', 'SWELL', 'SHELL', 'ELLAS']
print(Solution(["SMELL", "SWELL", "QUELL", "SHELL", "TELL", "ELLAS"], "SELL"))