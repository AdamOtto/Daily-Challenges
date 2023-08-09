"""
This problem was asked by Microsoft.

Implement a URL shortener with the following methods:

shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
Hint: What if we enter the same URL twice?
"""

def shorten(url):
    map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    retVal = ""
    
    while url > 0:
        retVal += map[url % 62]
        url //= 62
    return retVal[len(retVal): : -1]

def restore(ar):
    id = 0
    for i in ar:
        val_i = ord(i)
        if(val_i >= ord('a') and val_i <= ord('z')):
            id = id*62 + val_i - ord('a')
        elif(val_i >= ord('A') and val_i <= ord('Z')):
            id = id*62 + val_i - ord('A') + 26
        else:
            id = id*62 + val_i - ord('0') + 52
    return id

# Return 23451699527
print(restore("zLg6wl"))
# Return zLg6wl
print(shorten(23451699527))