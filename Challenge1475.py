"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings
[dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""
def findPrefix(Qstring,stringSet):
    d = {}
    for x in stringSet:
        temp = x[0:len(Qstring)]
        if temp in d:
            d[temp].append(x)
        else:
            d[temp] = [x]
        
    if Qstring in d:
        return d[Qstring]
    return None

# Return ['deer', 'deal']
print(findPrefix("de", ["dog", "deer", "deal"]))

# Return ['abc', 'abcd', 'abbbaba']
print(findPrefix("ab", ["abc", "abcd", "bcbba", "aa", "abbbaba"]))

# Return None
print(findPrefix("abd", ["abc", "abcd", "bcbba", "aa", "abbbaba"]))