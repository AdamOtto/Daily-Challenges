"""
Given a list of words, return the shortest unique prefix of each word. For example, given the list:
dog
cat
apple
apricot
fish

Return the list:
d
c
app
apr
f
"""

class Tree:

    d = None

    def __init__(self):
        self.d = {}

    # Creates a tree from the word. Branches are made when different characters are found.
    def addWord(self, word):
        nav = self.d
        for s in word:
            if s not in nav:
                nav[s] = Tree()
                nav = nav[s].d
            else:
                nav = nav[s].d

    # Creates a return array and starts the getPrefixHelper function.
    def getPrefix(self):
        retVal = []
        self.getPrefixHelper(self.d, "", retVal)
        return retVal

    # Parses the tree to find the shortest prefix for each word in the tree.
    def getPrefixHelper(self, dval, s, retVal):
        # If only one element, dig down.
        if len(dval) == 1:
            for key, val in dval.items():
                s += key
                return self.getPrefixHelper(val.d, s, retVal)
        # If more than one element
        else:
            for key, val in dval.items():
                #Check if branch is a linear.  If it is, add it as a prefix.
                if self.getPrefixHelperFindBranch(val.d):
                    retVal.append(s + key)
                # Else, get the prefix of the branch below this branch.
                else:
                    self.getPrefixHelper(val.d, s + key, retVal)

        return retVal

    def getPrefixHelperFindBranch(self, dval):
        if len(dval) == 0:
            return True
        if len(dval) == 1:
            for key, val in dval.items():
                return self.getPrefixHelperFindBranch(val.d)
        else:
            return False


def Solution(in1):
    t = Tree()

    for i in in1:
        t.addWord(i)
    return t.getPrefix()

#in1 = ["dog", "cat", "apple", "apricot", "fish"]
in1 = ["there", "their", "them", "this", "that", "thick"]
print(Solution(in1))