"""
Given an array of numbers arr and a window of size k,
print out the median of each window of size k starting
from the left and moving right by one position each time.

For example, given the following array and k = 3:

[-1, 5, 13, 8, 2, 3, 3, 1]
Your function should print out the following:

5 <- median of [-1, 5, 13]
8 <- median of [5, 13, 8]
8 <- median of [13, 8, 2]
3 <- median of [8, 2, 3]
3 <- median of [2, 3, 3]
3 <- median of [3, 3, 1]
Recall that the median of an even-sized list is the average of the two middle numbers.
"""
import statistics

def Solution(ar, k):
    sums = 0
    for i in range(k):
        sums += ar[i]
    
    print(statistics.median(ar[0:k]), "<- median of", ar[0:k])
    
    for i in range(k, len(ar)):
        sums -= ar[i - k]
        sums += ar[i]
        print(statistics.median(ar[i - k + 1:i + 1]), "<- median of", ar[i - k + 1:i + 1])
    

Solution([-1, 5, 13, 8, 2, 3, 3, 1], 3)
print()
Solution([1,1,1,2,1,3,1,1,4,1,2,1], 4)
    