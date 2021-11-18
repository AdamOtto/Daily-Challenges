"""
You are given an array of integers representing coin denominations and a total amount of money.
Write a function to compute the fewest number of coins needed to make up that amount.
If it is not possible to make that amount, return null.

For example, given an array of [1, 5, 10] and an amount 56, return 7 since we can use 5 dimes, 1 nickel, and 1 penny.

Given an array of [5, 8] and an amount 15, return 3 since we can use 5 5-cent coins.
"""
import sys

def Solution(coins, ar):
    temp = sorted(coins, reverse=True)
    retVal = Helper(temp, ar)
    if retVal == sys.maxsize:
        return None
    return retVal

def Helper(coins, val):
    if val == 0:
        return 0
    retVal = sys.maxsize
    for i in range(len(coins)):
        if val - coins[i] >= 0:
            retVal = min(retVal, Helper(coins, val - coins[i]))
            if retVal != sys.maxsize:
                return retVal + 1
    return retVal

# Return 7
print(Solution([1,5,10], 56))
# Return 3
print(Solution([5, 8], 15))
# Return None
print(Solution([5,10,25], 116))