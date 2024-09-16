"""
There are N couples sitting in a row of length 2 * N.
They are currently ordered randomly, but would like to
rearrange themselves so that each couple's partners can sit side by side.

What is the minimum number of swaps necessary for this to happen?
"""
import sys

def Solution(N, pairs, order):
    return Helper(0, N, pairs, order)

def Helper(cur, N, pairs, order):
    if cur >= N * 2:
        return 0

    if CheckPair(order[cur], order[cur + 1], pairs):
        return Helper(cur + 2, N, pairs, order)

    temp = ReOrder(cur, order, pairs)
    a = Helper(cur + 2, N, pairs, temp)
    temp = ReOrder(cur + 1, order, pairs)
    b = Helper(cur + 2, N, pairs, temp)
    return 1 + min(b, a)

def ReOrder(cur, order, pairs):
    curPartnerIndex = 0
    if cur % 2 == 0:
        curPartnerIndex = cur + 1
    else:
        curPartnerIndex = cur - 1

    curPair = order.index( pairs[order[cur]] )
    temp = []
    temp.extend(order)
    temp[curPartnerIndex], temp[curPair] = temp[curPair], temp[curPartnerIndex]
    return temp

def CheckPair(p1, p2, pairs):
    if pairs[p1] == p2:
        return True
    return False


# Return 2
N = 3
pairs = { 1:2, 2:1, 3:4, 4:3, 5:6, 6:5 }
order = [1,6,4,5,3,2]
print(Solution( N, pairs, order ))

# Return 1
N = 4
pairs = { 1:2, 2:1, 3:4, 4:3, 5:6, 6:5, 7:8, 8:7 }
order = [7,8,1,3,2,4,6,5]
print(Solution( N, pairs, order ))

# Return 3
N = 4
pairs = { 1:2, 2:1, 3:4, 4:3, 5:6, 6:5, 7:8, 8:7 }
order = [8,1,3,6,4,7,2,5]
print(Solution( N, pairs, order ))