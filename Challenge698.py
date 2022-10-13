"""
You are given a 2-d matrix where each cell consists of either /, \, or an empty space.
Write an algorithm that determines into how many regions the slashes divide the space.

For example, suppose the input for a three-by-six grid is the following:

\    /
 \  /
  \/
Considering the edges of the matrix as boundaries, this divides the
grid into three triangles, so you should return 3.


**Assumption**
forward slashes and back slashes connect, so long as they form a complete cut.
so for example:
\ 2 /
 \ / 3
1 \
There wouldn't be a gap, so there would be three areas.
Whereas
    \
 1 /
  /  1
Would not connect as they do not cleanly cut the region, so there is only 1 area.
"""
def Solution(ar):
    
    l1 = len(ar)
    l2 = len(ar[0])
    count = 0
    
    for i in range(0, l1):
        for j in range(0, l2):
            if ar[i][j] == "\\" or ar[i][j] == "/":
                determineSlash(i, j, l1, l2, ar, ar[i][j])
    
    #Edge cases
    if ar[0][0] == "/":
        count += 1
    if ar[0][l2 - 1] == "\\":
        count += 1
    if ar[l1 - 1][l2 - 1] == "/":
        count += 1
    if ar[l1 - 1][0] == "\\":
        count += 1
    
    for i in range(0, l1):
        for j in range(0, l2):
            if ar[i][j] == "":
                count += 1
                fill(i, j, l1, l2, count, ar)
    return count

#Follow each dash to see if it goes out of bounds.  If not, remove it, as it wont count as a split area.
def determineSlash(i, j, l1, l2, ar, sym):
    if outOfBounds(i, j, l1, l2):
        return True
    if ar[i][j] != sym:
        return False
    
    if sym == "\\":
        t1 = determineSlashHelper(i, j, -1, -1, l1, l2, ar, sym)
        t2 = determineSlashHelper(i, j, 1, 1, l1, l2, ar, sym)
        if t1 and t2:
            return True
        else:
            ar[i][j] = ""
    elif sym == "/":
        t1 = determineSlashHelper(i, j, -1, 1, l1, l2, ar, sym)
        t2 = determineSlashHelper(i, j, 1, -1, l1, l2, ar, sym)
        if t1 and t2:
            return True
        else:
            ar[i][j] = ""
    else:
        return False
        

def determineSlashHelper(i, j, deltai, deltaj, l1, l2, ar, sym):
    if outOfBounds(i, j, l1, l2):
        return True
    if sym == "\\" and ar[i][j] == "/":
        return True
    elif sym == "/" and ar[i][j] == "\\":
        return True
    elif ar[i][j] != sym:
        return False
    return determineSlashHelper(i + deltai, j + deltaj, deltai, deltaj, l1, l2, ar, sym)

def fill(i, j, l1, l2, count, ar):
    if outOfBounds(i, j, l1, l2):
        return
    if ar[i][j] != "":
        return

    ar[i][j] = count
    fill(i + 1, j, l1, l2, count, ar)
    fill(i - 1, j, l1, l2, count, ar)
    fill(i, j + 1, l1, l2, count, ar)
    fill(i, j - 1, l1, l2, count, ar)
    return

def outOfBounds(i, j, l1, l2):
    if i < 0:
        return True
    elif i >= l1:
        return True
    if j < 0:
        return True
    elif j >= l2:
        return True
    return False



# Return 3
in1 = [ ["\\", "", "", "", "", "/"],
        ["", "\\", "", "", "/", ""],
        ["", "", "\\", "/", "", ""]]
print(Solution(in1))

# Return 5
in1 = [ ["","/","","","\\",""],
        ["/","","","","","\\"],
        ["\\","","","","","/"],
        ["","\\","","","/",""]]
print(Solution(in1))

# Return 5
in1 = [ ["/","","","","","\\"],
        ["","","","","",""],
        ["","","","","",""],
        ["\\","","","","","/"]]
print(Solution(in1))

# Return 1.
in1 = [ ["","","","","\\",""],
        ["","","","/","",""],
        ["","","/","","",""],
        ["","/","","","",""]]
print(Solution(in1))

# Return 1
in1 = [ ["","","","","\\",""],
        ["","","","\\","",""],
        ["","","/","","",""],
        ["","/","","","",""]]
print(Solution(in1))

# Return 2
in1 = [ ["","","","","/",""] ]
print(Solution(in1))

# Return 4
in1 = [ ["","","","/","","\\"],
        ["","","/","","",""],
        ["","/","","\\","",""],
        ["/","","","","\\",""]]
print(Solution(in1))