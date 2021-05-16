"""
Write a program that computes the length of the longest common subsequence of three given strings.
For example, given "epidemiologist", "refrigeration", and "supercalifragilisticexpialodocious",
it should return 5, since the longest common subsequence is "eieio".
"""

def Solution(X, Y, Z):
    lx = len(X)
    ly = len(Y)
    lz = len(Z)
    #print("lx = " + str(lx) + ", ly = " + str(ly) + ", lz = " + str(lz))

    retVal = [[[0 for i in range(lz + 1)] for j in range(ly + 1)] for k in range(lx+1)]
    #print("retVal = " + str(len(retVal) ) + ", retVal[0] = " + str(len(retVal[0])) + ", retVal[0][0] = " + str(len(retVal[0][0])))

    for x in range(lx + 1):
        for y in range(ly + 1):
            for z in range(lz + 1):
                if x == 0 or y == 0 or z == 0:
                    retVal[x][y][z] = 0
                elif X[x - 1] == Y[y - 1] and X[x - 1] == Z[z - 1]:
                    retVal[x][y][z] = retVal[x - 1][y - 1][z - 1] + 1
                else:
                    retVal[x][y][z] = max( max(retVal[x - 1][y][z], retVal[x][y - 1][z]), retVal[x][y][z-1])
    return retVal[lx][ly][lz]

"""
in1 = "epidemiologist"
in2 = "refrigeration"
in3 = "supercalifragilisticexpialodocious"
print(Solution(in1, in2, in3))
"""
in1 = "helloworld"
in2 = "firsthelloworldsecond"
in3 = "hellocombobreakerworld"
print(Solution(in1, in2, in3))
