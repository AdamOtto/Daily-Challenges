"""
Given a string and a set of delimiters, reverse the words in
the string while maintaining the relative order of the delimiters.

For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases:
"hello/world:here/", "hello//world:here"
"""
#O(n)
def Solution(ar, delim):
    l = len(ar)
    delimHold = []
    wordHold = []
    wordFirst = ar[0] not in delim
    last = 0
    retVal = ""
    
    for i in range(l):
        if ar[i] in delim:
            if len(ar[last:i]) > 0:
                wordHold.append(ar[last:i])
                delimHold.append(ar[i])
                last = i + 1
            else:
                if len(delimHold) > 0:
                    delimHold[-1] += ar[i]
                else:
                    delimHold.append(ar[i])
                last = i + 1
    if ar[-1] not in delim:
        wordHold.append(ar[last:])
    
    while len(delimHold) > 0 and len(wordHold) > 0:
        if wordFirst:
            retVal += str(wordHold.pop(-1)) + str(delimHold.pop(0))
        else:
            retVal += str(delimHold.pop(0)) + str(wordHold.pop(-1))
            
    if len(delimHold) > 0:
        retVal += str(delimHold.pop(0))
    elif len(wordHold) > 0:
        retVal += str(wordHold.pop(0))
    return retVal

# Return here/world:hello
print(Solution("hello/world:here", ["/", ":"]))

# Return here/world:hello/
print(Solution("hello/world:here/", ["/", ":"]))

# Return here//world:hello
print(Solution("hello//world:here", ["/", ":"]))

# Return //test4//test3//:/test2/test1/
print(Solution("//test1//test2//:/test3/test4/", ["/", ":"]))