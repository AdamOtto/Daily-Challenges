"""
Given a string and a set of delimiters,
reverse the words in the string while maintaining the relative order of the delimiters.
For example, given "hello/world:here", return "here/world:hello"

Follow-up: Does your solution work for the following cases:
"hello/world:here/", "hello//world:here"
"""

def Solution(ar):
    l = len(ar)
    words = []
    delimiters = []
    start = 0
    for i in range(l):
        if ord(ar.lower()[i]) <= ord('a') or ord(ar.lower()[i]) >= ord('z'):
                words.append(ar[start:i])
                start = i+1
                i = getDelimiters(ar, i, delimiters)
    if ord(ar.lower()[i]) >= ord('a') and ord(ar.lower()[i]) <= ord('z'):
        words.append(ar[start:i + 1])
    
    l = len(words)
    j = 0
    retVal = ""
    for i in reversed(range(l)):
        retVal += str(words[i])
        if j < len(delimiters):
            retVal += delimiters[j]
        j += 1
    
    return retVal

def getDelimiters(ar, i, delimiters):
    l = len(ar)
    deStart = i
    while ord(ar.lower()[i]) <= ord('a') or ord(ar.lower()[i]) >= ord('z'):
        i += 1
        if i >= l:
            break
    delimiters.append(ar[deStart:i])
    return min(i, l - 1)

# Return here/world:hello
print(Solution("hello/world:here"))

# Return here/world:hello/
print(Solution("hello/world:here/"))

# Return here//world:hello
print(Solution("hello//world:here"))