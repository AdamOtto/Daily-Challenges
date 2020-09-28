'''
A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
'''

def Solution(n):
    sn = str(n)
    t = 0
    for c in sn:
        t += int(c)
        
    if 10 - t == 0:
        print(n)
        return
    elif 10 - t > 0:
        sn += str(10 - t)
        print(sn)
        return
    else:
        Solution(n+1)
        


Solution(109)