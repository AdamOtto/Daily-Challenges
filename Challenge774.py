"""
Using a read7() method that returns 7 characters from a file,
implement readN(n) which reads n characters.
For example, given a file with the content “Hello world”,
three read7() returns “Hello w”, “orld” and then “”.
"""
file = "Hello World"
i = 0

def read7():
    global i
    global file
    print(file[i:max(len(file) - 1, i+7)])
    i += 7

def readN(n):
    t = n
    while t >= 0:
        read7()
        t -= 7

# Return "Hello Worl", "orld", ""
readN(14)