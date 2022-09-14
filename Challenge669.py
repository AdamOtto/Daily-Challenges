"""
The game of Nim is played as follows.
Starting with three heaps, each containing a variable number of items,
two players take turns removing one or more items from a single pile.
The player who eventually is forced to take the last stone loses.
For example, if the initial heap sizes are 3, 4, and 5, a game could be played as shown below:
  A  |  B  |  C
-----------------
  3  |  4  |  5 <- Start
  3  |  1  |  5 <- P1
  3  |  1  |  3 <- P2
  0  |  1  |  3 <- P1
  0  |  1  |  0 <- P2
  0  |  0  |  0 <- Player 1 loses
In other words, to start, the first player takes three items from pile B.
The second player responds by removing two stones from pile C.
The game continues in this way until player one takes last stone and loses.
Given a list of non-zero starting values [a, b, c],
and assuming optimal play,
determine whether the first player has a forced win.

**Notes**
Optimal play involves balancing the xOr of each row's binary representation.
The game of NIM is mathmatically solved, as such we can determine the winner based on who goes
first and what move they make.
"""
# Brute force 1st turn balance.
def Solution(ar):
    if boardBalance(ar) == 0:
        return False
    
    for i in range(len(ar)):
        temp = []
        temp.extend(ar)
        for j in range(0, ar[i] + 1):
            temp[i] = j
            if boardBalance(temp) == 0:
                return True
    return False
    
def boardBalance(ar):
    xOr = 0
    for num in ar:
        xOr ^= num
    return xOr

# Return True
in1 = [3,4,5]
print(Solution(in1))
# Return True
in1 = [1,2,8]
print(Solution(in1))
# Return True
in1 = [1,3,6,12]
print(Solution(in1))
# Return False
in1 = [4, 4]
print(Solution(in1))