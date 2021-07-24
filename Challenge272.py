'''
Write a function, throw_dice(N, faces, total),
that determines how many ways it is possible to throw N dice
with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.
'''
import time

# Brute force method. O(N*M)
def throw_dice_BF(N, faces, total):
    retVal = 0
    dice = [1] * N
    dice[0] = 0
    while addVal(0, dice, N, faces):
        if sum(dice) == total:
            retVal += 1
    return retVal
    
def addVal(cur, dice, N, faces):
    if cur >= N:
        return False
    
    dice[cur] += 1
    
    if dice[cur] <= faces:
        return True
    else:
        dice[cur] = 1
        return addVal(cur + 1, dice, N, faces)


# Efficient Solution
def throw_dice(N, faces, total):
    mem = [[0 for i in range(total+1)] for j in range(N+1)]
    mem[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(1, total + 1):
            mem[i][j] = mem[i][j - 1] + mem[i - 1][j - 1]
            if j - faces - 1 >= 0:
                mem[i][j] -= mem[i - 1][j - faces - 1]
    
    return mem[N][total]

t1 = time.time()
print(throw_dice_BF(3, 6, 7))
t2 = time.time()
print("Time elapsed: " + str(t2 - t1))
t1 = time.time()
print(throw_dice(3, 6, 7))
t2 = time.time()
print("Time elapsed: " + str(t2 - t1))

print("\n")

t1 = time.time()
print(throw_dice_BF(4, 8, 18))
t2 = time.time()
print("Time elapsed: " + str(t2 - t1))
t1 = time.time()
print(throw_dice(4, 8, 18))
t2 = time.time()
print("Time elapsed: " + str(t2 - t1))

print("\n")

t1 = time.time()
print(throw_dice_BF(10, 12, 54))
t2 = time.time()
print("Time elapsed: " + str(t2 - t1))
t1 = time.time()
print(throw_dice(10, 12, 54))
t2 = time.time()
print("Time elapsed: " + str(t2 - t1))
