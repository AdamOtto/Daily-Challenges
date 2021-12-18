"""
The "look and say" sequence is defined as follows:
beginning with the term 1, each subsequent term visually describes
the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

def Solution(N):
    cur = "1"
    d = {}
    d["1"] = "11"
    d["11"] = "21"
    if N == 1:
        return cur
    
    for i in range(2,N+1):
        ind1 = 0
        ind2 = 0
        next = ""
        while ind1 < len(cur) and ind2 < len(cur):
            if cur[ind1] == cur[ind2]:
                ind2 += 1
                continue
            else:
                if cur[ind1:ind2] not in d:
                    d[cur[ind1:ind2]] = getLooknSay(cur[ind1:ind2])
                next += d[cur[ind1:ind2]]
                ind1 = ind2
                ind2 += 1
                continue
        if cur[ind1:ind2] not in d:
            d[cur[ind1:ind2]] = getLooknSay(cur[ind1:ind2])
        next += d[cur[ind1:ind2]]
        cur = next 
    return next

def getLooknSay(ar):
    if len(ar) == 1:
        return "1" + ar
    return str(len(ar)) + ar[0]

print(Solution(1))
print(Solution(2))
print(Solution(3))
print(Solution(4))
print(Solution(5))
print(Solution(6))
print(Solution(7))