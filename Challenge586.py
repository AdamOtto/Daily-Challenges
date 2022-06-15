"""
You are given a list of (website, user) pairs that
represent users visiting websites.
Come up with a program that identifies the top k pairs
of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:

[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5)
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e': 5), ('e', 6)]

Then a reasonable similarity metric would most likely conclude that
a and e are the most similar, so your program should return [('a', 'e')].
"""

def getWebsiteAndUser(ar):
    userCount = []
    websiteCount = []
    for arg in ar:
        if not arg[0] in websiteCount:
            websiteCount.append(arg[0])
        if not arg[1] in userCount:
            userCount.append(arg[1])
    return userCount, websiteCount
  
def setMatrix(matrix, ar, user, website):
    for arg in ar:
        i1 = website.index(arg[0])
        i2 = user.index(arg[1])
        matrix[i1][i2] = 1
    return
    
 
def Solution(ar, ret):
    user, website = getWebsiteAndUser(ar)
    luser = len(user)
    lweb = len(website)
    
    matrix = [[0 for i in range(luser)] for j in range(lweb)]
    
    setMatrix(matrix, ar, user, website)
    
    relations = []
    
    for i in range(0, lweb - 1):
        for j in range(i + 1, lweb):
            count = 0
            for k in range(0, luser):
                if matrix[i][k] == matrix[j][k]:
                    count += 1
            relations.append( ((website[i], website[j]), count) )
    relations = sorted(relations, key=lambda x: -x[1])
    
    retVal = []
    for i in range(ret):
        retVal.append(relations[i][0])
    return retVal



# Return [('a', 'e')]
in1 = [ ('a', 1), ('a', 3), ('a', 5),
        ('b', 2), ('b', 6),
        ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
        ('d', 4), ('d', 5), ('d', 6), ('d', 7),
        ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
print(Solution(in1, 1))

# Return [('d', 'e'), ('a', 'b')]
in1 = [ ('a', 1), ('a', 2), ('a', 3),
        ('b', 1), ('b', 2),
        ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5), ('c', 6), ('c', 7),
        ('d', 1), ('d', 2), ('d', 3), ('d', 4),
        ('e', 1), ('e', 2), ('e', 3), ('e', 4)]
print(Solution(in1, 2))
