"""
In academia, the h-index is a metric used to calculate the impact of a researcher's papers.
It is calculated as follows:

A researcher has index h if at least h of her N papers have h citations each.
If there are multiple h satisfying this formula, the maximum is chosen.

For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5].
Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.

Given a list of paper citations of a researcher, calculate their h-index.
"""

def Solution(N, papers):
    if N != len(papers):
        return False
    papers.sort()

    for i in range(0, N):
        if papers[i] >= N - i:
            return papers[i]

    return False



N = 5
in1 = [4, 3, 0, 1, 5]
print(Solution(N, in1))

N = 10
in1 = [10,3,4,6,0,5,1,2,3,5]
print(Solution(N, in1))