"""
PageRank is an algorithm used by Google to rank the importance of different websites.
While there have been changes over the years, the central idea is to assign each site
a score based on the importance of other pages that link to that page.

More mathematically, suppose there are N sites, and each site i has a certain count
Ci of outgoing links. Then the score for a particular site Sj is defined as :

score(Sj) = (1 - d) / N + d * (score(Sx) / Cx+ score(Sy) / Cy+ ... + score(Sz) / Cz))

Here, Sx, Sy, ..., Sz denote the scores of all the other sites that have outgoing links to Sj,
and d is a damping factor, usually set to around 0.85,
used to model the probability that a user will stop searching.

Given a directed graph of links between various websites,
write a program that calculates each site's page rank.

Assumption: If Cx == 0, where Cx is the outgoing links of Sx, then only return (1 - d) / N.
"""

def Solution(ar):
    l = len(ar)
    retVal1 = []
    retVal2 = []
    for key, val in ar.items():
        retVal1.append(key)
        retVal2.append(0)
    
    for i in range(l):
        retVal2[i] = getScore(ar, retVal1[i])
    
    return retVal1, retVal2
    
    
def getScore(ar, cur):
    BaseScore = ((1 - 0.85) / len(ar))
    if len(ar[cur]) == 0:
        return BaseScore
    score = 0
    for val in ar[cur]:
        if len(ar[val]) != 0:
            score += getScore(ar, val) / len(ar[val])
        else:
            score += getScore(ar, val)
    return score + 0.85 * BaseScore

# Return ([0, 1, 2, 3], [0.208125, 0.069375, 0.069375, 0.037500000000000006])
in1 = { 0:[1,2,3],
        1:[3],
        2:[3],
        3:[]
}
print(Solution(in1))