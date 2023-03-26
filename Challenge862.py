"""
A bridge in a connected (undirected) graph is an edge that if removed
causes the graph to become disconnected. Find all the bridges in a graph.
"""
def Solution(ar):
    l = len(ar)
    retVal = set()
    solved = set()

    for i in range(l):
        for j in range(len(ar[i])):
            t = ar[i][j]
            if ( min(i, t), max(i, t)) not in solved:
                ar[i][j] = None
                s = set()
                Helper(i, ar, s)
                if len(s) != l:
                    retVal.add( ( min(i, t), max(i, t)) )
                solved.add( ( min(i, t), max(i, t)) )
                ar[i][j] = t

    return retVal

def Helper(cur, ar, s):
    if cur in s:
        return
    s.add(cur)

    for i in range(len(ar[cur])):
        if ar[cur][i] is not None:
            Helper(ar[cur][i], ar, s)
    return

# Return {(1, 3)}
in1 = [
    [1,2],
    [0,2,3],
    [0,1],
    [1]
    ]
print(Solution(in1))

# Return {(4, 6), (3, 4), (1, 5)}
in1 = [
    [1,2],      #0
    [0,2,3,5],  #1
    [0,1,3],    #2
    [1,2,4],    #3
    [3,6],      #4
    [1],        #5
    [4,7,8],    #6
    [6,8,9],    #7
    [6,7,9],    #8
    [7,8]       #9
    ]
print(Solution(in1))