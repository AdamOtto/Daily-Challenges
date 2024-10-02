"""
Given a binary search tree, find the floor and ceiling of a given integer.
The floor is the highest element in the tree less than or equal to an integer,
while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.
"""
import sys

def Solution(tree, head, ar):
    q = []
    q.append(head)
    Floor = -sys. maxsize - 1
    Ceiling = sys. maxsize
    while len(q) >= 1:
        temp = q.pop(0)
        if temp is not None:
            if temp <= ar:
                Floor = max(temp, Floor)
            if temp >= ar:
                Ceiling = min(temp, Ceiling)
            q.append(tree[temp][0])
            q.append(tree[temp][1])
    return (Floor, Ceiling)

# Return (3, 3)
d = { 1 : [None,None],
      2 : [1,3],
      3 : [None,None],
      4 : [2,6],
      5 : [None,None],
      6 : [5, 7],
      7 : [None,None]
}
print(Solution(d, 4, 3))


# Return (15, 20)
d = { 10 : [None,None],
      12 : [10,None],
      15 : [12,20],
      20 : [None,24],
      24 : [None,None],
      29 : [15, 36],
      31 : [None,33],
      33 : [None,None],
      36 : [31,40],
      38 : [None,None],
      40 : [38,None]
}
print(Solution(d, 29, 18))