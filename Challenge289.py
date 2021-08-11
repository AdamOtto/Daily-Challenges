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

Example 1:
3 - 011
4 - 100
5 - 101   xOr
------------
    010
    
The optimal play for the above example is to take 2 away from column A on P1's first move.

1 - 001
4 - 100
5 - 101   xOr
------------
    000

So long as P1 can balance the board on the first turn, P1 can win.
When the board is balanced, P2 has no option but to unbalance it again.
P1 will continue to balance the board until one of several instances of a winning pattern is found. (Such as [1,X], X being any integer.  Just remove everything from stack X.)
In this program, I'll assume P1 can recognize them as P1 is playing optimally.
Otherwise, if P1 cannot balance the board, P1 is guaranteed to lose.


Example 2:

1 - 0001
2 - 0010
8 - 1000 xOr
------------
    1011

This can be balanced by removing from 8 until its 3.

1 - 0001
2 - 0010
3 - 0011 xOr
------------
    0000
    
    
Example 3:
6  - 0110
9  - 1001
15 - 1111 xOr
------------
     0000
P1 cannot balance this board on the first turn and has no choice but to unbalance it.
P1 will lose if P2 plays optimally and re-balances the board on their turn.
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

in1 = [3,4,5]
print(Solution(in1))
in1 = [1,2,8]
print(Solution(in1))
in1 = [6,9,15]
print(Solution(in1))