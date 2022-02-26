"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations,
that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""
# O(1) time
def Solution(n):
    coins = [25,10,5,1]
    retVal = 0
    for i in range(len(coins)):
        retVal += int(n / coins[i])
        n = int(n % coins[i])
        if n == 0:
            break
    return retVal
    
# Return 3
print(Solution(16))

# Return 5
print(Solution(101))

# Return 81018
print(Solution(2025406))