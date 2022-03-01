"""
What does the below code snippet print out?
How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""
# Code only prints 9, should probably print 0 to 9

functions = []
# Need to create new instance of i to print 0 to 9
for i in range(10):
    functions.append(lambda i = i : i)

for f in functions:
    print(f())