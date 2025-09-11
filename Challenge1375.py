"""
Given a list of words, determine whether the words can be chained to form a circle.
A word X can be placed in front of another word Y in a circle if the
last character of X is same as the first character of Y.

For example, the words ['chair', 'height', 'racket', 'touch', 'tunic']
can form the following circle:
chair --> racket --> touch --> height --> tunic --> chair.
"""

def Solution(ar):
    d = {}

    for a in ar:
        if a[0] not in d:
            d[a[0]] = []
        d[a[0]].append(a)
    
    for a in ar:
        if a[-1] in d:
            for b in d[a[-1]]:
                temp = Helper(d, b, a, [b])
                if temp[0]:
                    print([a] + temp[0])
                    return
    print([None])
            
def Helper(d, cur ,start, path):
    if cur == start:
        return (path, True)
    if cur[-1] in d:
        for word in d[cur[-1]]:
            temp = []
            temp.extend(path)
            temp.append(word)
            if word not in path:
                temp2 = Helper(d, word, start, temp)
                if temp2[1]:
                    return temp2
    return (None, False)

# Return ['chair', 'racket', 'touch', 'height', 'tunic', 'chair']
Solution(['chair', 'height', 'racket', 'touch', 'tunic'])

# Return [None]
Solution(['air', 'bear', 'chair', 'lair', 'snare', 'care', 'hair', 'dare'])

# Return ['air', 'race', 'ella', 'air']
Solution(['air', 'bear', 'chair', 'lair', 'snare', 'care', 'hair', 'dare', 'race', 'ella'])