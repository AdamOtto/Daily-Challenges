"""
In chess, the Elo rating system is used to calculate player strengths based on game results.
A simplified description of the Elo system is as follows.

Every player begins at the same score. For each subsequent game,
the loser transfers some points to the winner,
where the amount of points transferred depends on how unlikely the win is.

For example, a 1200-ranked player should gain much more points for beating a
2000-ranked player than for beating a 1300-ranked player.
Implement this system.
"""

def Prob(R1, R2):
    return 1 / (1 + pow(10, (R1 - R2) / 400))


def Solution(P1Rating, P2Rating, RatingChangeMax, P1Winner = True):
    P1 = Prob(P2Rating, P1Rating)
    P2 = Prob(P1Rating, P2Rating)
    
    if P1Winner:
        R1 = P1Rating + (RatingChangeMax * (1 - P1))
        R2 = P2Rating + (RatingChangeMax * (0 - P2))
    else:
        R1 = P1Rating + (RatingChangeMax * (0 - P1))
        R2 = P2Rating + (RatingChangeMax * (1 - P2))

    return (R1, R2)

# Return:
# P1:  1800       P2:  1000       Player 1 wins
# P1:  1800.990099009901  P2:  999.009900990099
k = 100
P1 = 1800
P2 = 1000
print("P1: ", P1, "\tP2: ", P2, "\tPlayer 1 wins")
R1, R2 = Solution(P1, P2, k, True)
print("P1: ", R1, "\tP2: ", R2)

print()


# Return:
# P1:  1800       P2:  1000       Player 1 loses
# P1:  1700.990099009901  P2:  1099.009900990099
P1 = 1800
P2 = 1000
print("P1: ", P1, "\tP2: ", P2, "\tPlayer 1 loses")
R1, R2 = Solution(P1, P2, k, False)
print("P1: ", R1, "\tP2: ", R2)