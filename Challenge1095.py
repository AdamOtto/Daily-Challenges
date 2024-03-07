"""
You are given given a list of rectangles represented by min and max x- and y-coordinates.
Compute whether or not a pair of rectangles overlap each other.
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return true as the first and third rectangle overlap each other.
"""
class Rectangle:

    x = None
    y = None
    dx = None
    dy = None

    def __init__(self, topLeft, dimensions):
        self.x = topLeft[0]
        self.y = topLeft[1]
        self.dx = dimensions[0]
        self.dy = dimensions[1]

    def topRight(self):
        return (self.x + self.dx, self.y)
    def topLeft(self):
        return (self.x, self.y)
    def bottomRight(self):
        return (self.x + self.dx, self.y + self.dy)
    def bottomLeft(self):
        return (self.x, self.y + self.dy)


def Overlap(r1, r2):
    overlapX = max(0, min(r1.topRight()[0], r2.topRight()[0]) - max(r1.topLeft()[0], r2.topLeft()[0]))
    overlapY = max(0, min(r1.bottomRight()[1], r2.bottomRight()[1]) - max(r1.topLeft()[1], r2.topLeft()[1]))
    return overlapY * overlapX

def Solution(rl):
    l = len(rl)
    for i in range(0, l):
        for j in range(i + 1, l):
            if Overlap( rl[i], rl[j] ):
                return True
    return False

# Return True
in1 = []
t = Rectangle( (1,4), (3,3) )
in1.append(t)
t = Rectangle( (-1,3), (2,1) )
in1.append(t)
t = Rectangle( (0,5), (4,3) )
in1.append(t)
print(Solution(in1))

# Return False
in1 = []
t = Rectangle( (1,4), (3,3) )
in1.append(t)
t = Rectangle( (-1,3), (2,1) )
in1.append(t)
print(Solution(in1))