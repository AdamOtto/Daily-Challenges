"""
We have some historical clickstream data gathered from our
site anonymously using cookies.
The histories contain URLs that users have visited in chronological order.

Write a function that takes two users' browsing histories as
input and returns the longest contiguous sequence of URLs that appear in both.

For example, given the following two users' histories:

user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']
You should return the following:

['/login', '/user', '/one']
"""

# O(n*m); n = len(u1), m = len(u2)
def Solution(u1, u2):
    temp = []
    i = 0
    j = i + 1
    retVal = []
    retVal.append(u1[0])
    while i < len(u1):
        temp = u1[i:j + 1]
        if checkSubLst(u2, temp) and j < len(u1):
            j += 1
            if len(temp) > len(retVal):
                retVal = temp
        else:
            i += 1
            j = min(i + 1, len(u1) - 1)
    return retVal

def checkSubLst(u2, checkLs):
    if checkLs[0] not in u2:
        return False
    i = u2.index(checkLs[0])
    if u2[i:i + len(checkLs)] == checkLs:
        return True
    return False

# Return /login, /user, /one
u1 = ['/home', '/register', '/login', '/user', '/one', '/two']
u2 = ['/home', '/red', '/login', '/user', '/one', '/pink']
print(Solution(u1, u2))

# Return 1,2,3
u1 = [9,8,7,6,5,4,3,2,1,2,3]
u2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(Solution(u1, u2))