"""
A strobogrammatic number is a positive number that appears
the same after being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

def Solution(N):
    cur = [""]
    if N % 2 != 0:
        cur = ["8", "0", "1"]
    next = []
    
    while len(str(cur[0])) != N:
        for i in range(len(cur)):
            next.append( "6" + cur[i] + "9" )
            next.append( "9" + cur[i] + "6" )
            next.append( "1" + cur[i] + "1" )
            next.append( "8" + cur[i] + "8" )
            if len(str(cur[0])) < N - 2:
                next.append( "0" + cur[i] + "0" )
        cur = next
        next = []
    return cur

# Return ['689', '986', '181', '888', '609', '906', '101', '808', '619', '916', '111', '818']
print(Solution(3))
# Return ['69', '96', '11', '88']
print(Solution(2))
# Return ['6699', '9696', '1691', '8698', '6969', '9966', '1961', '8968', '6119', '9116', '1111', '8118', '6889', '9886', '1881', '8888', '6009', '9006', '1001', '8008']
print(Solution(4))