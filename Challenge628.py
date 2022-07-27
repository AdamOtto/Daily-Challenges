"""You are given a circular lock with three wheels,
each of which display the numbers 0 through 9 in order.
Each of these wheels rotate clockwise and counterclockwise.

In addition, the lock has a certain number of "dead ends",
meaning that if you turn the wheels to one of these combinations,
the lock becomes stuck in that state and cannot be opened.

Let us consider a "move" to be a rotation of a single wheel by one digit,
in either direction. Given a lock initially set to 000, a target combination,
and a list of dead ends, write a function that returns the minimum number
of moves required to reach the target state, or None if this is impossible.
"""
import sys

def listToStr(l):
    res = "".join(map(str, l))
    return res

def getDelta(cur, goal, i):
    decCount = 0
    incCount = 0
    j = cur[i]
    while j != goal[i]:
        j -= 1
        decCount += 1
        if j == -1:
            j = 9
    j = cur[i]
    while j != goal[i]:
        j += 1
        incCount += 1
        if j == 10:
            j = 0
    if incCount <= decCount:
        return 1
    else:
        return -1


def Solution(goal, lock):
    start = [0,0,0]
    t = HelperGreedy(goal, lock, start, start)
    if t == sys.maxsize:
        return None
    return t
    
def HelperGreedy(goal, lock, cur, last):
    if cur == goal:
        return 0
    count = sys.maxsize
    
    # First, be greedy and move the wheels towards their goal
    for i in range(0, 3):
        temp = []
        temp.extend(cur)
        temp[i] += getDelta(cur, goal, i)
        if temp[i] == -1:
            temp[i] = 9
        if temp[i] == 10:
            temp[i] = 0
        if listToStr(temp) not in lock and listToStr(temp) != listToStr(last) and cur[i] != goal[i]:
            count = min(count, 1 + HelperGreedy(goal, lock, temp, cur))
    
    # If none of the greedy options work, be anti-greedy and move away from the goal.
    if count == sys.maxsize:
        for i in range(0, 3):
            temp = []
            temp.extend(cur)
            temp[i] -= getDelta(cur, goal, i)
            if temp[i] == -1:
                temp[i] = 9
            if temp[i] == 10:
                temp[i] = 0
            if listToStr(temp) not in lock and listToStr(temp) != listToStr(last) and cur[i] != goal[i]:
                count = min(count, 1 + HelperGreedy(goal, lock, temp, cur))
    
    # Return the lowest count
    return count


# Return 6
goal = [1,2,3]
lock = {"100","010","110","101", "011"}
print(Solution(goal, lock))

# Return None
goal = [2,2,2]
lock = {"100", "010", "001", "900", "090", "009"}
print(Solution(goal, lock))

# Return 11
goal = [8,4,5]
lock = {"001", "010", "011", "100", "101", "110", "111", "900", "090", "990"}
print(Solution(goal, lock))