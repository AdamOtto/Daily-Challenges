"""
Given a list of points, a central point, and an integer k,
find the nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)],
the central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""
import math

class FindClosestPoint:

    track = None
    cenPon = None

    def __init__(self, centralPoint):
        self.track = []
        self.cenPon = centralPoint

    def pythag(self, p, k):
        return math.sqrt( pow(p[0] - k[0],2) + pow(p[1] - k[1],2) )

    def retLowestK(self, k):
        retVal = []
        for i in range(0, k):
            retVal.append( self.track[i][1] )
        print(self.track)
        return retVal

    def push(self, point):
        c = self.pythag(point, self.cenPon)
        #print(c)
        self.addToTrack(point, c)

    def addToTrack(self, point, c):
        l = len(self.track)
        if l == 0:
            self.track.append( (c, point) )
            return
        if c <= self.track[0][0]:
            self.track.insert(0, (c, point))
            return
        if c >= self.track[l - 1][0]:
            self.track.insert(l, (c, point))
            return

        for i in range(1, l - 1):
            if self.track[i - 1][0] <= c and self.track[i + 1][0] >= c:
                self.track.insert(i+1, (c, point))
                return

def Solution(in1, cenPon, k):
    l = len(in1)
    fcp = FindClosestPoint(cenPon)
    for i in range(0, l):
        fcp.push(in1[i])
    return fcp.retLowestK(k)


#in1 = [(0, 0), (5, 4), (3, 1)]
#centralPoint = (1, 2)
#k = 2

in1 = [(1,0), (2, 2), (4, 4), (-4, 8), (0, 1), (3, -2), (6,1), (-2,1)]
centralPoint = (0, 0)
k = 5

print( Solution(in1, centralPoint, k) )

