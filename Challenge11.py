"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string 'de' and the set of strings [dog, deer, deal], return [deer, deal].
"""

def findPrefix(Qstring,stringSet):
    d = {}
    for x in stringSet:
        temp = x[0:len(Qstring)]
        if temp in d:
            d[temp].append(x)
        else:
            d[temp] = [x]
        
    #print(d)
    return d[Qstring]

#strSet = ["dog", "deer", "deal"]
#strQuery = "de"
strSet = ["abc", "abcd", "aa", "abbbaba"]
strQuery = "ab"
print(findPrefix(strQuery, strSet))