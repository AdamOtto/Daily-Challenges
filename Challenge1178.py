"""
A Collatz sequence in mathematics can be defined as follows.

Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1

It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""
def Solution(ar, d):
    if ar == 1:
        return [1]
    
    temp = ar
    seq = []
    while temp != 1:
        seq.append(temp)
        if temp % 2 == 0:
            temp = int(temp / 2)
        else:
            temp = (3 * temp) + 1
        
        if temp in d:
            seq.extend(d[temp])
            return seq
    return seq

d = {}
longest = 0
for i in range(1, 1000001):
    d[i] = Solution(i, d)
    if len(d[i]) > longest:
        longest = i
print("Longest Collatz sequence for n <= 1000000 is " + str(longest) + ".\nWith a whopping " + str(len(d[longest])) + " steps.")
print()
print(d[longest])