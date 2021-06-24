"""
Given a list of words, determine whether the words can be chained to form a circle.
A word X can be placed in front of another word Y in a circle if the last character of
X is same as the first character of Y.

For example, the words
['chair', 'height', 'racket', touch', 'tunic']
can form the following circle:
chair --> racket --> touch --> height --> tunic --> chair.
"""
def Solution(ar):
    N = len(ar)
    firstLetter = {}
    for argument in ar:
        if argument[0] not in firstLetter:
            firstLetter[argument[0]] = argument
        else:
            if type(firstLetter[argument[0]]) is list:
                firstLetter[argument[0]].append(argument)
            else:
                firstLetter[argument[0]] = [firstLetter[argument[0]], argument]

    for argument in ar:
        if argument[len(argument) - 1] in firstLetter:
            if Helper(argument, firstLetter, N, firstLetter[argument[len(argument) - 1]], []):
                return True
    return False

def Helper(firstWord, firstLetterDict, N, CurrentWord, UsedWords):
    if CurrentWord == firstWord:
        return True
    if len(UsedWords) >= N:
        return False

    if type(CurrentWord) is list:
        for word in CurrentWord:
            if word not in UsedWords:
                t = []
                t.extend(UsedWords)
                t.append(word)
                if word[len(word) - 1] in firstLetterDict:
                    if Helper(firstWord, firstLetterDict, N, firstLetterDict[word[len(word) - 1]], t):
                        return True
    else:
        if CurrentWord not in UsedWords:
            t = []
            t.extend(UsedWords)
            t.append(CurrentWord)
            if CurrentWord[len(CurrentWord) - 1] in firstLetterDict:
                if Helper(firstWord, firstLetterDict, N, firstLetterDict[CurrentWord[len(CurrentWord) - 1]], t):
                    return True
    return False



# Solution: True
in1 = ['chair', 'height', 'racket', 'touch', 'tunic']
print(Solution(in1))

# Solution: False
in1 = ['hello', 'world']
print(Solution(in1))

# Solutions: True world -> drow -> world
in1 = ['hello', 'world', 'oswald', 'drow']
print(Solution(in1))

# Solution: False
in1 = ['large', 'word', 'molten', 'garage', 'gilded', 'danger', 'spirit', 'close', 'elephant', 'tusk']
print(Solution(in1))

# Solution: True elephant -> tusk -> karate -> elephant
in1 = ['large', 'word', 'molten', 'garage', 'gilded', 'danger', 'spirit', 'close', 'elephant', 'tusk', 'karate']
print(Solution(in1))