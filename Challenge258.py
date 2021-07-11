"""
In Ancient Greece, it was common to write text with the first line going left to right,
the second line going right to left, and continuing to go back and forth.
This style was called "boustrophedon".

Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

For example, given the following tree:

       1
    /     \
  2         3
 / \       / \
4   5     6   7

You should return [1, 3, 2, 4, 5, 6, 7].
"""

class Tree:
    l = None
    r = None
    val = None

    def __init__(self, value, left = None, right = None):
        self.l = left
        self.r = right
        self.val = value

def Solution(bt):
    layer = 1
    count = 0
    printStr = []
    hold = []
    queue = []
    queue.append(bt)
    reverse = False

    while len(queue) != 0:

        if queue[0] is not None:
            hold.append(queue[0].val)
            queue.append(queue[0].l)
            queue.append(queue[0].r)

        queue.pop(0)
        count += 1
        if count == layer:
            layer = len(queue)
            count = 0
            if reverse:
                hold = hold[::-1]
            reverse = not reverse
            printStr.extend(hold)
            hold = []
    print(printStr)


in1 = Tree(1, Tree(2, Tree(4), Tree(5)), Tree(3, Tree(6), Tree(7)))
Solution(in1)

in1 = Tree(1, Tree(2, None, Tree(5)), Tree(3, Tree(6)))
Solution(in1)