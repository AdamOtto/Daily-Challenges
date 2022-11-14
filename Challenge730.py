"""
What will this code print out?

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
"""

#Prediction: Code will print out 3
#How to fix, pass i as a variable so each function has its own value.

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i(i):
            print(i)
        flist.append((print_i,i))

    return flist

functions = make_functions()
for f,i in functions:
    f(i)