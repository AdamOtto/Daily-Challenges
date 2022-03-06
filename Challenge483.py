"""
There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person,
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner
should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions
would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.

[1,2,3,4,5]
"""

def Solution(N, k):
    count = -1
    prisoners = [i + 1 for i in range(N)]
    retVal = []
    # O(logn) time for k == 2.  Eliminate half of prisoners each round.
    if k == 2:
        temp = prisoners[-1]
        # even numbered prisoners will be eliminated on the first round (index 1 and up)
        prisoners = [i for i in prisoners if i not in prisoners[1 :: k]]
        # If the last prisoner survives, the first prisoner (index 0 and up) gets picked off in the next round.
        switch = temp != prisoners[-1]
        while len(prisoners) > 1:
            temp = prisoners[-1]
            # Eliminate half the prisoners
            if switch:
                prisoners = [i for i in prisoners if i not in prisoners[1 :: k]]
            else:
                prisoners = [i for i in prisoners if i not in prisoners[0 :: k]]
            switch = temp != prisoners[-1]
        return prisoners[0]
    # O(n) time for k > 2
    else:
        for i in range(N):
            count += k
            if count >= len(prisoners):
                count = min( count - len(prisoners), len(prisoners) - 1)
            retVal.append(prisoners.pop(count))
            count -= 1
        return retVal[-1]

# Return 3
print(Solution(5,2))

# Return 5
print(Solution(6,2))

# Return 73
print(Solution(100,2))

# Return 24
print(Solution(100,15))