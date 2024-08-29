"""
Given a string, find the length of the smallest window that contains every distinct character.
Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""
def Solution(ar):
    ar = ar.lower()
    l = len(ar)
    d = {}
    subStrStart = 0
    retVal = 0
    for i in range(l):
        if ar[i] in ar[subStrStart:i]:
            if ar[i] == ar[subStrStart]:
                subStrStart += 1
            else:
                subStrStart = ar[:i].rfind(ar[i]) + 1
        retVal = max(retVal, i - subStrStart + 1)
            
    return retVal

# Return 5
print(Solution("jiujitsu"))
# Return 4
print( Solution("aaaaxyzaaaa") )
# Return 11
print( Solution("Everyone likes me said Caul Shivers the most feared man in the North.") )