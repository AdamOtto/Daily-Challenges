"""
A step word is formed by taking a given word, adding a letter, and anagramming the result.
For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word,
create a function that returns all valid step words.
"""
def Solution(d, ar):
    l = len(d)
    d1 = {}
    retVal = []
    for a in ar:
        if a not in d1:
            d1[a] = 0
        d1[a] += 1
    
    
    for i in range(l):
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
                    t = val - d1[key]
                    count += t
                else:
                    count += val
            
            if count == 1:
                retVal.append(d[i])
    return retVal

# Return APPEAL
print(Solution(["APPLE", "APPEAL", "BOY", "PAPAL", "PEAR", "POPELA"], "APPLE"))
# Return ['PORK', 'NORK', 'GORK', 'HORK', 'LORK']
print(Solution(["ORC", "PORK", "NORK", "GORK", "HORK", "LORK", "CHORK", "GRORK"], "KRO"))