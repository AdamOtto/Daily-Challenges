"""
Given a string, find the length of the smallest window that contains every distinct character.
Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""

def Solution(ar):
    d = {}
    for a in ar:
        if a not in d:
            d[a] = 0
    uniqueChar = len(d)
    window = uniqueChar
    
    while window <= len(ar):
        for i in range(window, len(ar) + 1):
            d2 = d.copy()
            #print(ar[i - window: i])
            for j in ar[i - window: i]:
                d2[j] += 1
            if AllThere(d2):
                return len(ar[i - window: i]), ar[i - window: i]
        window += 1
    return False
            
def AllThere(ar):
    for key, val in ar.items():
        if val == 0:
            return False
    return True

# Return 5, 'ujits'
print(Solution("jiujitsu"))

# Return 10, 'helloworld'
print(Solution("helloworld"))

# Return 42, 'yone loves me said caul shivers the most f'
print(Solution("everyone loves me said caul shivers the most feared man in the north"))