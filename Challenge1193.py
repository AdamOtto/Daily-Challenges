"""
Ghost is a two-person word game where players alternate appending letters to a word. The first person who spells out a word, or creates a prefix for which there is no possible continuation, loses. Here is a sample game:

Player 1: g
Player 2: h
Player 1: o
Player 2: s
Player 1: t [loses]
Given a dictionary of words, determine the letters the first player should start with, such that with optimal play they cannot lose.

For example, if the dictionary is ["cat", "calf", "dog", "bear"], the only winning start letter would be b.
"""
class WordTree:
    
    next = None
    val = None
    
    def __init__(self, Value):
        self.val = Value
        self.next = []
        

def printWordTree(tree, curStr = ""):
    if tree is None:
        return
        
    curStr += tree.val

    if len(tree.next) != 0:
        for n in tree.next:
            printWordTree(n, curStr)
    else:
        print(curStr)
    return
    

def CreateTree(word):
    l = len(word)
    retVal = WordTree(word[0])
    temp = retVal.next
    
    for i in range(1, l):
        new = WordTree(word[i])
        temp.append( new )
        temp = new.next
    return retVal

def AppendTree(tree, word):
    temp = tree.next
    l = len(word)
    
    for i in range(1, l):
        ind = CheckNextForLetter(word[i], temp)
        if ind != -1:
            temp = temp[ind].next
        else:
            temp.append(CreateTree(word[i:]))
            return
    return
    
def CheckNextForLetter(letter, tree):
    for i in range(0, len(tree)):
        if tree[i].val == letter:
            return i
    return -1

def Solution(ar):
    arLength = len(ar)
    Trees = {}
    for i in range(arLength):
        if ar[i][0] not in Trees:
            Trees[ar[i][0]] = CreateTree(ar[i])
        else:
            AppendTree(Trees[ar[i][0]], ar[i])
    
    count = 0
    for key, val in Trees.items():
        if opponentTurn(val, False):
            print("Winning move: " + key)
            count += 1
    
    if count == 0:
        print("The only winning move is not to play")
    
    return

def playerTurn(treeCur, thisTurnWin):
    if len(treeCur.next) == 0:
        return thisTurnWin
    
    for t in treeCur.next:
        if WinningMove(t, not thisTurnWin):
            if opponentTurn(t, not thisTurnWin):
                return True
    return False

def opponentTurn(treeCur, thisTurnWin):
    if len(treeCur.next) == 0:
        return thisTurnWin
        
    for t in treeCur.next:
        debug = t.val
        if WinningMoveOpponent(t, not thisTurnWin):
            if not playerTurn(t, not thisTurnWin):
                return False
    return True

def WinningMove(treeCur, thisTurnWin):
    if len(treeCur.next) == 0:
        return thisTurnWin
    
    for t in treeCur.next:
        if WinningMove(t, not thisTurnWin):
            return True
    return False
    
def WinningMoveOpponent(treeCur, thisTurnWin):
    if len(treeCur.next) == 0:
        return thisTurnWin
    
    for t in treeCur.next:
        debug = t.val
        if not WinningMoveOpponent(t, not thisTurnWin):
            return True
    return False


# Should return true: c and b
print("Game1")
in1 = ["cat", "calf", "dog", "bear"]
Solution(in1)

print("\n")

# Should only return b
print("Game2")
in1 = ["cat", "calf", "dog", "bear", "con"]
Solution(in1)

print("\n")

# Should return some true values: b h n
print("Game3")
in1 = ["hair", "hole", "horse", "move", "monkey", "map", "ball", "boar", "boat", "wave", "no", "yes", "harry", "whale", "nose", "nope", "mini"]
Solution(in1)

print("\n")

# Should return c.  Can win if Player1 plays optimally and use 'n' from cant on its turn.
print("Game4")
in1 = ["cat", "car", "cant"]
Solution(in1)

print("\n")

# Player 1 going first is guaranteed to lose if the opponent plays optimally
# (ie, they wont pick 'a' as their first move).
print("Game5")
in1 = ["car", "con", "call"]
Solution(in1)

print("\n")

# Player 1 going first is guaranteed to lose if the opponent plays optimally
# (ie, they wont pick 'a' as their first move).
print("Game6")
in1 = ["ball", "balloon", "blister", "blip", "basket"]
Solution(in1)

print("\n")

# Player 1 has multiple paths to victory, print b
print("Game7")
in1 = ["bop", "but", "bat", "ball", "burn", "boot"]
Solution(in1)