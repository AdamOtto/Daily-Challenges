'''
Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less.
You must break it up so that words don't break across lines.
Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
'''

def Solution(in1, k):
    words = in1.split(" ")
    wrdCnt = []
    for i in words:
        wrdCnt.append(len(i))
    cur = words[0]
    retVal = []
    for i in range(1, len(wrdCnt)):
        
        if len(words[i]) > k:
            print("null")
            return
        
        if len(cur) > k or len(cur + " " + words[i]) > k:
            retVal.append(cur)
            cur = words[i]
        else:
            cur += " " + words[i]
    retVal.append(cur)
    
    print(retVal)
    


in1 = "the quick brown fox jumps over the lazy dog"
k = 10
#in1 = "Hello World"
#k = 4
Solution(in1, k)