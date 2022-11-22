"""
Given a string s and an integer k, break up the string into multiple lines such
that each line has a length of k or less. You must break it up so that words don't
break across lines. Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there
is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
No string in the list has a length of more than 10.
"""
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
        
        if len(cur) > k or len(cur) + 1 + len(words[i]) > k:
            retVal.append(cur)
            cur = words[i]
        else:
            cur += " " + words[i]
    retVal.append(cur)
    
    return retVal

# Return ['the quick', 'brown fox', 'jumps over', 'the lazy', 'dog']
print(Solution("the quick brown fox jumps over the lazy dog", 10))

# Return ['Everyone likes me', 'said Caul Shivers', 'the most feared man', 'in the North']
print(Solution("Everyone likes me said Caul Shivers the most feared man in the North", 20))