"""
Word sense disambiguation is the problem of determining which sense
a word takes on in a particular setting, if that word has multiple meanings.
For example, in the sentence "I went to get money from the bank",
bank probably means the place where people deposit money,
not the land beside a river or lake.

Suppose you are given a list of meanings for several words,
formatted like so:

{
    "word_1": ["meaning one", "meaning two", ...],
    ...
    "word_n": ["meaning one", "meaning two", ...]
}

Given a sentence, most of whose words are contained in the meaning list above,
create an algorithm that determines the likely sense of each possibly ambiguous word.
"""

def Solution(ar, words):
    ar = ar.lower()
    spl = ar.split(" ")
    retVal = {}
    for s in spl:
        if s in words:
            retVal[s] = ""
    
    
    for s in spl:
        if s in words and s in ar:
            meaningCount = [0] * len(words[s])
            for i in range(0, len(words[s])):
                meanSpl = words[s][i].split(" ")
                for m in meanSpl:
                    if m in ar:
                        meaningCount[i] += 1
            maxVal = 0
            for i in range(len(meaningCount)):
                if meaningCount[i] > maxVal:
                    maxVal = meaningCount[i]
                    retVal[s] = words[s][i]
    return retVal
    
# Return {'bank': 'money deposit withdraw loan'}
words = {"bank": ["land river lake", "money deposit withdraw loan"]}
ar = "I went to get money from the bank"
print(Solution(ar, words))

# Return {'delta': 'triangle land river water flow', 'bank': 'land river lake water'}
words = {"bank": ["land river lake water", "money deposit withdraw loan"],
         "delta": ["triangle land river water flow", "change math"]
}
ar = "you can see the river flow across the delta from the bank we're on."
print(Solution(ar, words))