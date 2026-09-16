"""
A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node.
The following tree is an example:
        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.
"""


class Tree:
    val = None
    Child = None

    def __init__(self, Value, Children = None):
        self.val = Value
        self.Child = Children

# O(n) time and space.
def Solution(ar):
    curLevel = []
    curLevel.append(ar)

    while len(curLevel) != 0:
        nextLevel = []
        i = 0
        j = len(curLevel) - 1
        while i <= j:
            if curLevel[i].val == curLevel[j].val and ChildChecker(curLevel[i].Child, curLevel[j].Child):
                if i == j:
                    if curLevel[i].Child is not None:
                        nextLevel.extend(curLevel[i].Child)
                else:
                    if curLevel[i].Child is not None:
                        nextLevel.extend(curLevel[i].Child)
                    if curLevel[j].Child is not None:
                        nextLevel.extend(curLevel[j].Child)
                i += 1
                j -= 1
            else:
                return False
        curLevel = nextLevel
    return True

def ChildChecker(child1, child2):
    if child1 is None and child2 is None:
        return True
    elif type(child1) is list and type(child2) is list:
        if len(child1) == len(child2):
            return True
    return False

# Return True
in1 = Tree(4, [ Tree(3, [Tree(9)]), Tree(5), Tree(3, [Tree(9)]) ])
print(Solution(in1))
# Return False
in1 = Tree(4, [ Tree(3, [Tree(9), Tree(10)]), Tree(5), Tree(3, [Tree(9), Tree(10)]) ])
print(Solution(in1))
# Return True
in1 = Tree(4, [ Tree(3, [Tree(9), Tree(10)]), Tree(5), Tree(3, [Tree(10), Tree(9)]) ])
print(Solution(in1))