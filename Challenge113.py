'''
Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"
'''

def Solution(inpStr):
    st = inpStr.split(" ")
    retVal = ""
    for s in reversed(st):
        retVal += s + " "
    return retVal[0:len(retVal) - 1]
    

in1 = "hello world here"
t = Solution(in1)
print("\"" + t + "\"")