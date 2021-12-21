"""
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock.
You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9,
since you could buy the stock at 1 dollar, and sell at 8 dollars,
and then buy it at 4 dollars and sell it at 10 dollars.
Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit
minus 4 dollars of fees.
"""

def Solution(ar, fee):
    retVal = 0
    l = len(ar)
    i = 0
    while i < l:
        localMin = findLocalMin(ar, i)
        localMax = findLocalMax(ar, localMin)
        while ar[localMax] - ar[localMin] - fee <= 0 and localMax < len(ar) - 1:
            localMax = findLocalMax(ar, localMax)
        i = localMax + 1
        retVal += ar[localMax] - ar[localMin] - fee
    if retVal >= 0:
        return retVal
    else:
        return False

def findLocalMin(ar, start):
    for i in range(start,len(ar) - 1):
        if ar[i] < ar[i+1]:
            return i
    return len(ar) - 1

def findLocalMax(ar, localMin):
    for i in range(localMin + 1, len(ar) - 1):
        if ar[i] > ar[i+1]:
            return i
    return len(ar) - 1
    
# Return 9
in1 = [1, 3, 2, 8, 4, 10]
fee = 2
print(Solution(in1, fee))

# Return False
in1 = [6,5,4,3,2,1]
fee = 1
print(Solution(in1, fee))

# Return 5
in1 = [1, 3, 2, 4, 1, 2, 3, 1, 1, 4]
fee = 1
print(Solution(in1, fee))