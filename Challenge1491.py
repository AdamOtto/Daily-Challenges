"""
Describe and give an example of each of the following types of polymorphism:

Ad-hoc polymorphism
Parametric polymorphism
Subtype polymorphism
"""

# Ad-hoc polymorphism: Is when a polymorphic functions can be applied to different data types.
# Ex: In python, the '+' operator can be used on ints, floats, strings and lists.
"""
# The + operation handles many different data types.
print(1 + 2)
print(1.1 + 2.2)
print([1,2,3] + [4,5,6])
print("Hello" + " " + "World!")
"""


# Parametric polymorphism: Is when a function can be written genericallly so it can handle values of any type for the same operation.
# Ex: In python, you can add two lists together regardless of the data types contained.
"""
# Both operations handle different data types, but handle them the same way.
in1 = [1,2,3]
in2 = [4,5,6]
print(in1 + in2)

in1 = ['a','b','c']
in2 = ['d','e','f']
print(in1 + in2)
"""

# Subtype polymorphism: Using a data type (subtype) that is related to another datatype (supertype) in a function that expects the supertype.
# Ex: using a supertype called 'Number', whose subtypes are int and floats, in a function.
"""
def maxVal(Number x, Number y):
    if x > y:
        return x
    else:
        return y
"""