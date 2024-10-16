"""
What does the below code snippet print out?
How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""
#Prints only 9
#To print 0 to 9, create new instance of i
functions = []
for i in range(10):
    functions.append(lambda i = i : i)

for f in functions:
    print(f())