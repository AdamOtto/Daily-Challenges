"""
There are M people sitting in a row of N seats, where M < N.
Your task is to redistribute people such that there are no gaps between any of them,
while keeping overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1],
where 0 represents an empty seat and 1 represents a person.
In this case, one solution would be to place the person on the right in the fourth seat.
We can consider the cost of a solution to be the sum of the absolute distance each person must move,
so that the cost here would be five.

Given an input such as the one above, return the lowest
possible cost of moving people to remove all gaps
"""
def Solution(N):
    l = len(N)
    positions = []
    M = 0
    retVal = 0
    
    # Get the position of all ones.
    for i in range(0, l):
        if N[i] == 1:
            positions.append(i)
            M += i
    
    AlreadySolved = True
    for i in range(1, len(positions)):
        if positions[i - 1] + 1 != positions[i]:
            AlreadySolved = False
            break
    
    if AlreadySolved:
        return 0
    
    #Find the average of all 1s
    median = M // len(positions)
    
    # Relocate median to the closest 1 if its not already.
    diff = l + 1
    newMed = 0
    if N[median] == 0:
        for p in positions:
            if abs(p - median) < diff:
                newMed = p
                diff = abs(p - median)
        median = newMed
    
    
    # Go through the list and move 1s closer to the median.
    low = 0
    high = l - 1
    while low != high:
        if median - low < high - median:
            if N[high] == 1:
                for i in range(median, high):
                    if N[i] == 0:
                        N[i] = 1
                        N[high] = 0
                        retVal += abs(i - high)
                        break
            high -= 1
        else:
            if N[low] == 1:
                for i in reversed(range(low, median + 1)):
                    if N[i] == 0:
                        N[i] = 1
                        N[low] = 0
                        retVal += abs(i - low)
                        break
            low += 1
        
        if CheckSolution(N, len(positions)):
            break
    if CheckSolution(N, len(positions)):
        return retVal
    return False

def CheckSolution(ar, M):
    oneFound = False
    count = 0
    for i in range(0,len(ar)):
        if ar[i] == 1:
            oneFound = True
            count += 1
        elif ar[i] == 0 and oneFound:
            break
    return count == M


# Return 5
print(Solution([0, 1, 1, 0, 1, 0, 0, 0, 1]))

# Return 1
print(Solution([0, 1, 0, 1]))

# Return 0
print(Solution([0, 1, 1, 0]))