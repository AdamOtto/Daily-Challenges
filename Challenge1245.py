"""
Write an algorithm to justify text.
Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces,
if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""
def Solution(ar, k):
    retVal = []
    temp = ""
    for i in range(len(ar)):
        if len(temp) + 1 + len(ar[i]) <= k:
            if temp != "":
                temp += " "
            temp += ar[i]
        else:
            temp = padWithSpaces(temp, k)
            retVal.append(temp)
            temp = ""
            temp += ar[i]
    temp = padWithSpaces(temp, k)
    retVal.append(temp)
    return retVal

def padWithSpaces(t, k):
    spaces = []
    for i in range(len(t)):
        if t[i] == " ":
            spaces.append(i)
    
    if len(spaces) == 0:
        while len(t) < k:
            t += " "
        return t
    
    i = 0
    while len(t) < k:
        l = len(t)
        if t[spaces[i]] != " ":
            spaces[i] += 1
        else:
            temp = list(t)
            temp.insert(spaces[i], " ")
            t = ''.join(temp)
            i += 1
            if i >= len(spaces):
                i = 0
    return t
    
# Return ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
print(Solution(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16))

# Return ['Everyone   likes  me', 'said   Caul  Shivers', 'the  most feared man', 'in     the     North']
print(Solution(["Everyone", "likes", "me", "said", "Caul", "Shivers", "the", "most", "feared", "man", "in", "the", "North"], 20))

print(Solution(["Hello", "World"], 8))