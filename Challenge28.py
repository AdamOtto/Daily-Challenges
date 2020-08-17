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
"""

def Solution(in1, k):
    c = k
    last = 0
    retVal = []
    for i in range(0, len(in1)):
        if len(in1[i]) <= c:
            c -= len(in1[i]) + 1 #+1 for at least 1 space
            #print(c)
        else:
            retVal.append(helper(in1[last:i], c + 1))
            last = i
            c = k - len(in1[i]) - 1
            #print("k - len(" + in1[i] + ") + 1 = c = "+str(c))
    retVal.append(helper(in1[last:len(in1) + 1], c + 1))
    print(retVal)


def helper(words, spaces):
    #print(words)
    #print(spaces)
    if len(words) == 1:
        temp = words[0]
        for i in range(0, spaces):
            temp += " "
        return temp
        
    #lengthSp = len(words) - 1
    sp = [] * (len(words) - 1)

    for i in range(0,len(words) - 1):
        sp.append(" ")
    #print(sp)
    #print(len(sp))
    i = 0
    for x in range(0,spaces):
        #print(i)
        sp[i] += " "
        i += 1
        if i >= (len(words) - 1):
            i = 0
    
    retVal = ""
    for i in range(0,len(words)):
        if i - 1 >= 0 and i <= len(sp):
            #print(i)
            retVal += sp[i-1]
        retVal += words[i]
    #print(retVal)
    return retVal
        
#Result: ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
#in1 = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
#k =16
#Result: ['snap    ', 'into   a', 'slim jim']
in1 = ["snap", "into", "a", "slim", "jim"]
k = 8
Solution(in1,k)