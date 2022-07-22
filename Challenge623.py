"""
Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces,
if any, distributed starting from the left.

If you can only fit one word on a line,
then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""
def Solution(ar, k):
    sortedAr = []
    sortedAr.append([])
    cur = 0
    temp = 0
    for i in range(len(ar)):
        temp += len(ar[i]) + 1
        if temp <= k:
            sortedAr[cur].append(ar[i])
            sortedAr[cur].append(" ")
        else:
            sortedAr[cur].pop()
            sortedAr.append([])
            cur += 1
            sortedAr[cur].append(ar[i])
            sortedAr[cur].append(" ")
            temp = len(ar[i])
    sortedAr[cur].pop()
    
    retVal = []
    for i in range(len(sortedAr)):
        retVal.append(justify(sortedAr[i], k))
    return retVal

def justify(ar, k):
    if len(ar) == 1:
        while len(ar[0]) < k:
            ar[0] += " "
        return ar[0]
    retVal = ""
    ind = []
    for i in range(len(ar)):
        if ar[i] == " ":
            ind.append(i)
    cur = 0
    while length(ar) < k:
        ar[ind[cur]] += " "
        cur += 1
        if cur >= len(ind):
            cur = 0
    for i in range(len(ar)):
        retVal += ar[i]
    return retVal

def length(ar):
    retVal = 0
    for i in range(len(ar)):
        retVal += len(ar[i])
    return retVal


# Return ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
print(Solution(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16))

# Return ['hello ', 'world ']
print(Solution(["hello", "world"], 6))

# Return ['Everyone   likes  me', 'said   Caul  Shivers', 'the  most feared man', 'in     the     North']
print(Solution(["Everyone", "likes", "me", "said", "Caul", "Shivers", "the", "most", "feared", "man", "in", "the", "North"], 20))