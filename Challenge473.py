"""
Write an algorithm that computes the reversal of a directed graph.
For example, if a graph consists of A -> B -> C,
it should become A <- B <- C.
"""

def Solution(ar, start):
    prev = start
    next = ''
    cur = ar[start]
    ar[start] = None
    while cur is not None:
        next = ar[cur]
        ar[cur] = prev
        prev = cur
        cur = next
    return ar, prev

def printDG(ar, start):
    s = ""
    cur = start
    while cur is not None:
        s += str(cur)
        cur = ar[cur]
        if cur is not None:
            s += " -> "
    return s

in1 = { 'A':'B', 'B':'C', 'C':None }
start = 'A'
t1 = printDG(in1, start)
in1, start = Solution(in1, start)
t2 = printDG(in1, start)
print(t1, ", becomes: ", t2)


in1 = { 1:2, 2:3, 3:4, 4:5, 5:6, 6:7, 7:8, 8:9, 9:10, 10:None }
start = 1
t1 = printDG(in1, start)
in1, start = Solution(in1, start)
t2 = printDG(in1, start)
print(t1, ", becomes: ", t2)