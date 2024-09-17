"""
You come across a dictionary of sorted words in a language you've never seen before.
Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
you should return ['x', 'z', 'w', 'y'].
"""

def Solution(ar):
    l = len(ar)
    alphabet = []
    for i in range(l):
        for j in range(len(ar[i])):
            if ar[i][j] not in alphabet:
                alphabet.append(ar[i][j])
    
    for i in range(1, l):
        j = 0
        while j < len(ar[i - 1]) or j < len(ar[i]):
            if ar[i - 1][j] == ar[i][j]:
                j += 1
            else:
                let1ComesBeforelet2(alphabet, ar[i - 1][j], ar[i][j])
                break
    
    return alphabet
    

def let1ComesBeforelet2(alphabet, let1, let2):
    #i1 = alphabet.index(let1)
    #i2 = alphabet.index(let2)
    if alphabet.index(let1) > alphabet.index(let2):
        alphabet.pop(alphabet.index(let1))
        alphabet.insert(alphabet.index(let2), let1)
    return

# Return ['x', 'z', 'w', 'y']
print(Solution(['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']))

# Return ['c', 'a', 'b']
print(Solution(["caa", "aaa", "aab"]))