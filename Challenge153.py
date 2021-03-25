"""
Find the smallest distance (measured in number of words)
between any two given words in a string.

For example, given words "hello", and "world" and a text content of
"dog cat hello cat dog dog hello cat world", return 1 because there's
only one word "cat" in between the two words.
"""

def Solution(w1, w2, text):

    txt = text.split(" ")
    l = len(txt)
    d = {}
    d[w1] = []
    d[w2] = []

    for i in range(0, l):
        if txt[i] == w1:
            d[w1].append(i)
        if txt[i] == w2:
            d[w2].append(i)

    if len(d[w1]) == 0 or len(d[w2]) == 0:
        return False

    shortestDist = abs(d[w1][0] - d[w2][0]) - 1

    for i in d[w1]:
        for j in d[w2]:
            t = abs(i - j) - 1
            if t < shortestDist:
                shortestDist = t
            if shortestDist == 0:
                break

    return shortestDist



in1 = "hello"
in2 = "world"
#in3 = "dog cat hello cat dog dog hello cat world"
in3 = "hello little cat who is always doing silly things like programming a replica of the world"
print(Solution(in1, in2, in3))
