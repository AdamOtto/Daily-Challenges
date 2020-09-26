'''
On our special chessboard, two bishops attack each other if they share the same diagonal.
This includes bishops that have another bishop located between them
i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
Write a function to count the number of pairs of bishops that attack each other.
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
'''

#Solution 1: Very inefficient
"""
def Solution(bishops, M):

    results = []

    for key, val in bishops.items():
        x = key[0]
        y = key[1]
        #look down right
        while x <= M and y <= M:
            x += 1
            y += 1
            if (x,y) in bishops:
                t = ()
                if bishops[key] > bishops[(x,y)]:
                    t = (val,  bishops[(x,y)])
                else:
                    t = (bishops[(x, y)], val)

                if t not in results:
                    results.append(t)
        x = key[0]
        y = key[1]
        # look up left
        while x >= 0 and y >= 0:
            x -= 1
            y -= 1
            if (x, y) in bishops:
                t = ()
                if bishops[key] > bishops[(x, y)]:
                    t = (val, bishops[(x, y)])
                else:
                    t = (bishops[(x, y)], val)

                if t not in results:
                    results.append(t)

        x = key[0]
        y = key[1]
        # look up right
        while x <= M and y >= 0:
            x += 1
            y -= 1
            if (x, y) in bishops:
                t = ()
                if bishops[key] > bishops[(x, y)]:
                    t = (val, bishops[(x, y)])
                else:
                    t = (bishops[(x, y)], val)

                if t not in results:
                    results.append(t)

        x = key[0]
        y = key[1]
        # look down left
        while x >= 0 and y >= 0:
            x -= 1
            y += 1
            if (x, y) in bishops:
                t = ()
                if bishops[key] > bishops[(x, y)]:
                    t = (val, bishops[(x, y)])
                else:
                    t = (bishops[(x, y)], val)

                if t not in results:
                    results.append(t)
    print(results)
"""

# Solution 2: O(n^2)
def Solution(bishops, M):
    l = len(bishops)
    results = []
    for i in range(l):
        for j in range(i + 1, l):
            if abs( bishops[i][0] - bishops[j][0] ) == abs( bishops[i][1] - bishops[j][1] ):
                results.append( (i + 1,  j + 1) )
    print(results)


#in1 = {(0, 0): 1, (1, 2): 2, (2, 2): 3, (4, 0): 4}
in1 = [(0, 0), (1, 2), (2, 2), (4, 0)]
M = 5
Solution(in1, M)