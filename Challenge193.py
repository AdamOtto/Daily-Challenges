"""
Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock.
You're also given a number fee that represents a transaction fee for each buy and sell transaction.

You must buy before you can sell the stock, but you can make as many transactions as you like.

For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9,
since you could buy the stock at 1 dollar, and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars.
Since we did two transactions, there is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.
"""
# O(n^2log(n))
def Solution(ar, fee):
    t = []
    for i in range(0, len(ar)):
        t.append((ar[i], i))
    t.sort(key = lambda a:a[0], reverse=True)
    retVal = 0
    retVal = Helper(ar, len(ar), t, fee, -1, retVal, False)
    return retVal

def Helper(ar, l, sorAr, fee, cur, retVal, canSell):
    if cur == l - 1:
        return retVal
    temp = retVal
    if canSell:
        for price in sorAr:
            if cur < price[1] and ar[cur] < price[0]:
                temp = max(Helper(ar,l,sorAr,fee, price[1], retVal + price[0] - fee, False), temp)
    else:
        for price in reversed(sorAr):
            if cur < price[1] and ar[cur] > price[0]:
                temp = max(Helper(ar, l, sorAr, fee, price[1], retVal - price[0], True), temp)
    return temp


# Expected value: 9
#in1 = [1, 3, 2, 8, 4, 10]
#fee = 2
# Expected value: 130
#in1 = [0,2,1,1,1,50,1,60,75,40,45]
#fee = 0
# Expected value: 95
in1 = [100, 3, 2, 1, 100]
fee = 4
print(Solution(in1, fee))