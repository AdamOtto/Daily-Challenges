"""
You are given an N by M matrix of 0s and 1s.
Starting from the top left corner,
how many ways are there to reach the bottom right corner?

You can only move right and down.
0 represents an empty space while 1 represents a wall you cannot walk through.
"""


def Solution(arr):
    x = len(arr)
    y = len(arr[0])
    ar = [ [0]*y for _ in range(x) ]
    for i in range(0, x):
        ar[i][0] = 1
    for i in range(0,y):
        ar[0][i] = 1
    #print(ar)
    for i in range(1,x):
        for j in range(1,y):
            #print("x = " + str(i) + ", y = " + str(j))
            if arr[i][j] == 0:
                #t = getPrevNodes(ar, arr, i, j)
                #print("t = " + str(t))
                ar[i][j] = getPrevNodes(ar, arr, i, j)
    #print(ar)
    return ar[x-1][y-1]

def getPrevNodes(ar, arr, x, y):
    t = 0

    if arr[x - 1][y] == 0:
        t += ar[x - 1][y]
    if arr[x][y - 1] == 0:
        t += ar[x][y - 1]
    return t


"""
in1 = [[0, 0, 1],
       [0, 0, 1],
       [1, 0, 0]]
"""
in1 = [[0,0,0,0],
       [0,0,1,0],
       [0,1,1,0],
       [0,1,0,0],
       [0,0,1,0],
       [0,0,0,0]]

print(Solution(in1))