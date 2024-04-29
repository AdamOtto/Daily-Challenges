"""
Given a string, find the length of the smallest window that contains
every distinct character. Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""
def Solution(ar):
    chars = set()
    l = len(ar)
    
    for i in range(l):
        chars.add(ar[i].lower())
        
    window = len(chars)
    
    while window < len(ar):
        
        for i in range(0, l):
            newSet = set()
            for a in ar[i:window + i]:
                newSet.add(a)
            if len(newSet) == len(chars):
                return window
        
        window += 1
    
    return len(ar)

    
# Return 5
print( Solution("jiujitsu") )
# Return 4
print( Solution("aaaaaxyzaaaaa") )
# Return 37
print( Solution("Everyone likes me said Caul Shivers the most feared man in the North.") )