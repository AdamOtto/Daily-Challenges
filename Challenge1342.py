"""
You are given an N by N matrix of random letters and a dictionary of words. Find the maximum number of words that can be packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:

It can be found in the dictionary
It can be constructed from untaken letters by other words found so far on the board
The letters are adjacent to each other (vertically and horizontally, not diagonally).
Each tile can be visited only once by any word.

For example, given the following dictionary:

{ 'eat', 'rain', 'in', 'rat' }
and matrix:

[['e', 'a', 'n'],
 ['t', 't', 'i'],
 ['a', 'r', 'a']]
Your function should return 3, since we can make the words 'eat', 'in', and 'rat' without them touching each other. We could have alternatively made 'eat' and 'rain', but that would be incorrect since that's only 2 words.
"""
def Solution(ar, wordDict):
    N = len(ar)
    d = {}
    wordDict.sort(key=lambda s: len(s))
    
    for i in range(N):
        for j in range(N):
            if ar[i][j] not in d:
                d[ar[i][j]] = []
            d[ar[i][j]].append( (i, j) )
    count = 0
    visited = set()
    for word in wordDict:
        for cur in d[word[0]]:
            if Helper(word, 1, cur, d, visited):
                count += 1
    return count

def Helper(word, letter, cur, d, visited):
    if letter >= len(word):
        return True
    
    for w in d[word[letter]]:
        if w[0] == cur[0] - 1 or w[0] == cur[0] + 1 or w[0] == cur[0]:
            if w[1] == cur[1] - 1 or w[1] == cur[1] + 1 or w[1] == cur[1]:
                if w not in visited:
                    if Helper(word, letter + 1, w, d, visited):
                        visited.add(w)
                        return True
    return False

# Return 3
in1 = [ ['e', 'a', 'n'],
        ['t', 't', 'i'],
        ['a', 'r', 'a']]
in2 = [ 'eat', 'rain', 'in', 'rat' ]
print(Solution(in1, in2))

# Return 5
in1 = [ ['a', 'e', 'n', 'y'],
        ['t', 't', 'i', 't'],
        ['a', 'r', 'a', 'r'],
        ['n', 'a', 'p', 'y']]
in2 = [ 'in', 'eat', 'tan', 'trap', 'rat', 'pain', 'train', 'pan', 'net', 'party', 'pyra']
print(Solution(in1, in2))