"""
Create an algorithm to efficiently compute the approximate median of a list of numbers.

More precisely, given an unordered list of N numbers,
find an element whose rank is between N / 4 and 3 * N / 4,
with a high level of certainty, in less than O(N) time.
"""
def Solution(ar):
    l = len(ar)
    largest = ar[0]
    lowest = ar[0]
    average = 0
    
    for i in range(0, l):
        if ar[i] < lowest:
            lowest = ar[i]
        if ar[i] > largest:
            largest = ar[i]
        average += ar[i]
    average = average / l
    median = (largest + lowest) / 2
    
    if largest == lowest:
        return ar[int(l / 2)]
    
    
    avgDiff = largest
    closestAverage = 0
    medDiff = largest
    closestMedian = 0
    for i in range(0, l):
        if abs(ar[i] - average) < avgDiff:
            closestAverage = i
            avgDiff = abs(ar[i] - average)
        if abs(ar[i] - median) < medDiff:
            closestMedian = i
            medDiff = abs(ar[i] - median)
    
    if avgDiff <= medDiff:
        return ar[closestAverage]
    return ar[closestMedian]

# Return 10
in1 = [2,4,6,8,10,12,14,16,18,20]
print(Solution(in1))

# Return 5
in1 = [0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,10,0,0,0,0,0,0,0,0,0,0,0]
print(Solution(in1))