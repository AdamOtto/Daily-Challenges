"""
Write an algorithm that computes the reversal of a directed graph.
For example, if a graph consists of A -> B -> C, it should become A <- B <- C.
"""
# O(n) space and speed
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
    print(s)

in1 = { 'A':'B', 'B':'C', 'C':None }
start = 'A'
printDG(in1, start)
in1, start = Solution(in1, start)
printDG(in1, start)

print()

in1 = {'1':'2', '2':'3', '3':'4', '4':'5', '5':'6', '6':None}
start = '1'
printDG(in1, start)
in1, start = Solution(in1, start)
printDG(in1, start)