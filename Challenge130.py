'''
Given an array of numbers representing the stock prices of a company in chronological order and an integer k,
return the maximum profit you can make from k buys and k sells. You must buy the stock before you can sell it,
and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 4.
'''

def Solution(in1, k):
    l = len(in1)
    retVal = 0
    for i in range(0, l):
        retVal = max(retVal, Helper(in1, k, -in1[i], i, (1,0)))
    print(retVal)

def Helper(n, k, val, index, BuySell):
    l = len(in1)
    if BuySell[0] == k and BuySell[1] == k:
        return val
    if index >= l:
        return val
    retVal = val
    for i in range(index, l):
        if BuySell[0] > BuySell[1]:
            tempBuySell = (BuySell[0], BuySell[1] + 1)
            retVal = max(retVal, Helper(in1, k, val + n[i], i, tempBuySell))
        if BuySell[0] < k:
            tempBuySell = (BuySell[0] + 1, BuySell[1])
            retVal = max(retVal, Helper(in1, k, val - n[i], i, tempBuySell))
    return retVal

#in1 = [0, 4]
#k = 1
#in1 = [5, 2, 4, 0, 1]
#k = 2
in1 = [4,3,2,1]
k = 2
Solution(in1,k)