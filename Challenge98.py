"""
Given a 2D board of characters and a word,
find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true,
exists(board, "SEE") returns true,
exists(board, "ABCB") returns false.
"""

class grid:
    
    d = None
    g = None

    def __init__(self, arGrid):
        self.g = arGrid
        self.d = {}
        
        for i in range(len(arGrid)):
            for j in range(len(arGrid[i])):
                if arGrid[i][j] not in self.d:
                    self.d[arGrid[i][j]] = [ (i, j) ]
                else:
                    self.d[arGrid[i][j]].append( (i, j) )
    
    def exists(self, word):
        l = len(word)
        if l > 0 and word[0] in self.d:
            for val in self.d[word[0]]:
                prevVisited = []
                prevVisited.append( (val[0], val[1]) )
                if self.helper(1, word, val[0], val[1], prevVisited):
                    return True
        return False
        
    def helper(self, cur, word, i, j, prevVisited):
        if cur >= len(word):
            return True
        
        for deltaI in range(-1, 2):
            for deltaJ in range(-1, 2):
                if deltaI != 0 or deltaJ != 0:
                    if self.gridNext(i + deltaI , j + deltaJ, word[cur], prevVisited):
                        temp = []
                        temp.extend(prevVisited)
                        temp.append( (i + deltaI , j + deltaJ) )
                        if self.helper(cur + 1, word, i + deltaI , j + deltaJ, temp):
                            return True
        return False

    def gridNext(self, i, j, letter, prevVisited):
        if (i, j) in prevVisited:
            return False
        
        li = len(self.g)
        lj = len(self.g[0])
        
        if i < 0 or i >= li:
            return False
        if j < 0 or j >= lj:
            return False
        
        return self.g[i][j] == letter

in1 =   [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
        ]
g = grid(in1)
print(g.exists("ABCCED"))
print(g.exists("SEE"))
print(g.exists("ABCB"))
print(g.exists("DEE"))
print(g.exists("CCESEEDASABF"))
print(g.exists("CCESEEDASABFC"))
print(g.exists("HELLOWORLD"))