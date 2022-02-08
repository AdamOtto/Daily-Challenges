"""
Conway's Game of Life takes place on an infinite two-dimensional board of square cells.
Each cell is either dead or alive, and at each tick, the following rules apply
    - Any live cell with less than two live neighbours dies.
    - Any live cell with two or three live neighbours remains living.
    - Any live cell with more than three live neighbours dies.
    - Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""
import random as r

class Conway:
    map = []
    steps = 0
    dim = ()
    def __init__(self, inp, dimensions, st):
        self.steps = st
        self.dim = dimensions
        self.map = [ ['.']*dimensions[0] for i in range(dimensions[1])]
        for i in inp:
            self.map[i[0]][i[1]] = '*'

    def game(self):
        self.printMap()
        print("")
        print("")
        for i in range(0, self.steps):
            self.step()

    def step(self):
        x = self.dim[0]
        y = self.dim[1]
        newMap = [ ['.']*x for i in range(dimensions[1])]
        for i in range(0, x):
            for j in range(0, y):
                newMap[i][j] = self.lifeOrDeath((i, j))
        self.map = newMap
        self.printMap()
        print("")
        print("")

    def lifeOrDeath(self, coor):
        count = 0
        x = coor[0]
        y = coor[1]
        count += self.checkNeighboor((x - 1,y - 1))
        count += self.checkNeighboor((x - 1, y + 1))
        count += self.checkNeighboor((x + 1, y - 1))
        count += self.checkNeighboor((x + 1, y + 1))
        count += self.checkNeighboor((x - 1, y ))
        count += self.checkNeighboor((x, y - 1))
        count += self.checkNeighboor((x + 1, y))
        count += self.checkNeighboor((x, y + 1))

        if self.map[x][y] == '.':
            if count == 3:
                return '*'
            else:
                return '.'
        elif self.map[x][y] == '*':
            if count < 2 or count >= 4:
                return '.'
            else:
                return '*'


    def checkNeighboor(self, coor):
        if self.isValid(coor):
            if self.map[coor[0]][coor[1]] == '*':
                return 1
        return 0


    def isValid(self, coor):
        if  0 <= coor[0] and coor[0] < self.dim[0]:
            if 0 <= coor[1] and coor[1] < self.dim[1]:
                return True
        return False

    def printMap(self):
        for i in reversed(range(0, self.dim[0])):
            s = ""
            for j in range(0, self.dim[1]):
                s += self.map[j][i]
            print(s)


#in1 = [(0,0), (1,2), (3,1), (1,1), (3,2), (0,3)]
#dimensions = (5,5)
#steps = 6
in1 = []
for i in range(0,25):
    in1.append( (r.randint(0, 9),  r.randint(0, 9)) )
dimensions = (10,10)
steps = 20
print(in1)
t = Conway(in1, dimensions, steps)
t.game()