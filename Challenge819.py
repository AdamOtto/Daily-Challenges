"""
Given a array of numbers representing the stock prices of a company
in chronological order, write a function that calculates the maximum
profit you could have made from buying and selling that stock once.
You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5,
since you could buy the stock at 5 dollars and sell it at 10 dollars.
"""
def Solution(ar):
    l = len(ar)
    if l < 2:
        return None
    retVal = 0
    for i in range(l):
        for j in range(i + 1, l):
            retVal = max(retVal, ar[j] - ar[i])
    return retVal

# Return 5
print(Solution([9, 11, 8, 5, 7, 10]))

# Return 7
print(Solution([8, 15,2,4]))

# Return 0
print(Solution([10,9,8,7,6,5,4,3,2,1,0]))