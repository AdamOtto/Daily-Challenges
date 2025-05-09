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
    t = file[i:min(len(file), i+7)]
    i += 7
    return str(t)

# Return "Hello W", "orld"
print(read7())
print(read7())
print(read7())