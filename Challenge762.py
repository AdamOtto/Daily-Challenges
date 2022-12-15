"""
Find an efficient algorithm to find the smallest distance
(measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of
"dog cat hello cat dog dog hello cat world", return 1 because
there's only one word "cat" in between the two words.

Assumptions:
commas, periods, etc are not appearing in the strings
The words can appear more than once.
"""
# O(n)
def Solution(w1, w2, text):
    w1h = hash(w1)
    w2h = hash(w2)
    ar = text.lower().split(" ")
    l = len(ar)
    w1FoundFirst = None
    retVal = l + 1
    start = 0
    
    for i in range(l):
        if hash(ar[i]) == w1h:
            w1FoundFirst = True
            start = i
            break
        elif hash(ar[i]) == w2h:
            w1FoundFirst = False
            start = i
            break
    ind = start
    
    for i in range(start, l):
        if w1FoundFirst:
            if hash(ar[i]) == w1h:
                ind = i
            elif hash(ar[i]) == w2h:
                return abs(ind - i) - 1
        else:
            if hash(ar[i]) == w1h:
                return abs(ind - i) - 1
            elif hash(ar[i]) == w2h:
                ind = i
    return None

# Return 1
print(Solution("hello", "world", "dog cat hello cat dog dog hello cat world"))

# Return 0
print(Solution("cat", "dog", "dog cat hello cat dog dog hello cat world"))

# Return None
print(Solution("the", "dog", "Everyone likes me said Caul Shivers the most feared man in the North"))

# Return 7
print(Solution("caul", "north", "Everyone likes me said Caul Shivers the most feared man in the North"))