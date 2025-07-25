"""
On our special chessboard, two bishops attack each other if they share the same diagonal.
This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.

You are given N bishops, represented as (row, column) tuples on a M by M chessboard.
Write a function to count the number of pairs of bishops that attack each other.
The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).

For example, given M = 5 and the list of bishops:

(0, 0)
(1, 2)
(2, 2)
(4, 0)
The board would look like this:

[b 0 0 0 0]
[0 0 b 0 0]
[0 0 b 0 0]
[0 0 0 0 0]
[b 0 0 0 0]
You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
"""
def Solution(ar):
    l = len(ar)
    retVal = 0
    for i in range(l):
        for j in range(i + 1, l):
            x = abs(ar[i][0] - ar[j][0])
            y = abs(ar[i][1] - ar[j][1])
            if x == y:
                retVal += 1
    return retVal
    

# return 2
in1 = [ (0, 0), (1, 2), (2, 2), (4, 0)]
print(Solution(in1))