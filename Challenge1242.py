"""
Given a start word, an end word, and a dictionary of valid words,
find the shortest transformation sequence from start to end such
that only one letter is changed at each step of the sequence,
and each transformed word exists in the dictionary.
If there is no possible transformation, return null.
Each word in the dictionary have the same length as start and end and is lowercase.

For example, given start = "dog", end = "cat",
and dictionary = {"dot", "dop", "dat", "cat"},
return ["dog", "dot", "dat", "cat"].

Given start = "dog", end = "cat",
and dictionary = {"dot", "tod", "dat", "dar"},
return null as there is no possible transformation from dog to cat.
"""
def Solution(start, end, d):

    Relation = {}
    Relation[start] = findSimilarWords(d, start)
    Relation[start] = reversed(sorted(Relation[start], key=lambda elem: (RelationSort(elem, end))))
    for word in d:
        Relation[word] = findSimilarWords(d, word)
        Relation[word] = reversed(sorted(Relation[word], key=lambda elem: (RelationSort(elem, end))))
    retVal = []
    #print(Relation)
    SolutionHelper(Relation, start, end, retVal)
    retVal.insert(0, start)
    return retVal

def SolutionHelper(d, word, end, retVal):

    if word == end:
        return True

    for related in d[word]:
        if related not in retVal:
            retVal.append(related)
            if SolutionHelper(d, related, end, retVal):
                return True
            else:
                retVal.pop()
    return False

def RelationSort(word, end):
    count = 0
    l = len(end)
    for i in range(0, l):
        if word[i] == end[i]:
            count += 1
    return count


def findSimilarWords(d, word):
    retVal = []
    for w in d:
        diffWordCount = 0
        for i in range(0, len(w)):
            if w[i] != word[i]:
                diffWordCount += 1
        if diffWordCount == 1:
            retVal.append(w)
    return retVal


# Return ['dog', 'dot', 'dat', 'cat']
print(Solution("dog", "cat", {"dot", "tod", "dat", "dar", "cat"}))

# Return ['nope', 'nepe', 'neae', 'neah', 'yeah']
print(Solution("nope", "yeah", {"nape", "nype", "nepe", "neap", "neae", "nypo", "nyao", "neah", "nate", "naoe", "yeah"}))