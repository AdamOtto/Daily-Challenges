'''
A rule looks like this:
A NE B
This means this means point A is located northeast of point B.

Given a list of rules, check if the sum of the rules validate. For example:
A N B
B NE C
C N A
does not validate, since A cannot be both north and south of C.

Possible Directions:
N E S W NE NW SE SW

'''


#Doesn't work
class Node:
    val = None
    directions = None

    def __init__(self, Point):
        self.val = Point
        self.directions = {}
        self.directions["N"] = None
        self.directions["E"] = None
        self.directions["S"] = None
        self.directions["W"] = None
        self.directions["NE"] = None
        self.directions["NW"] = None
        self.directions["SE"] = None
        self.directions["SW"] = None


class Map:
    d = None
    def __init__(self):
        self.d = {}

    def AddRule(self, Rules):
        Rule = Rules.split(" ")
        if Rule[0] not in self.d:
            self.d[Rule[0]] = Node(Rule[0])
        if Rule[2] not in self.d:
            self.d[Rule[2]] = Node(Rule[2])

        if self.d[Rule[0]].directions[Rule[1]] != None or self.d[Rule[2]].directions[Rule[1]] != None:
            print(False)
            return

        opposite = self.findOpposite(Rule[1])

        self.d[Rule[0]].directions[opposite] =self.d[Rule[2]]
        self.d[Rule[2]].directions[Rule[1]] = self.d[Rule[0]]
        direc = self.getContradictionDirection(Rule[1])
        print(self.findContradiction(self.d[Rule[0]],direc,Rule[2]))
        return

    def findContradiction(self, N, dir, C):
        Q = []

        for d in dir:
            if N.directions[d] is not None:
                Q.append(N.directions[d])

        while len(Q) > 0:
            n = Q.pop(0)
            for d in dir:
                if n.directions[d] is not None:
                    Q.append(n.directions[d])
                    if n.directions[d].val == C:
                        return False
        return True

    def findOpposite(self, dir):
        if dir == "N":
            return "S"
        if dir == "E":
            return "W"
        if dir == "S":
            return "N"
        if dir == "W":
            return "E"

        if dir == "NE":
            return "SW"
        if dir == "NW":
            return "SE"
        if dir == "SE":
            return "NW"
        if dir == "SW":
            return "NE"


    def getContradictionDirection(self, dir):
        if dir == "N":
            return ["S", "SE", "SW", "W", "E"]
        if dir == "E":
            return ["W", "NW", "SW", "N", "S"]
        if dir == "S":
            return ["N", "NE", "NW", "W", "E"]
        if dir == "W":
            return ["E", "NE", "SE", "N", "S"]

        if dir == "NE":
            return ["W", "S", "SW", "NW", "SE"]
        if dir == "NW":
            return ["S", "E", "SE", "NE", "SW"]
        if dir == "SE":
            return ["N", "W", "NW", "NE", "SW"]
        if dir == "SW":
            return ["N", "E", "NE", "NW", "SE"]

m = Map()
m.AddRule("A N B")
m.AddRule("C N A")
m.AddRule("B N C")
m.AddRule("C N A")