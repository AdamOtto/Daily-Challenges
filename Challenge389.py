"""
Explain the difference between composition and inheritance.
In which cases would you use each?
"""

# Inheritance is when another point in data inherits certain attributes of another
# Ex: We have a point called 'Person'.  We want to make it more specific for a school setting so we
# create 2 new points, called 'student' and 'teacher'.  Both of these would inherit traits from 'Person',
# Such as; age, sex, home address, etc.
# Student would inherit all of that, and it would have additional information like; class, attendance, grades, etc.

# Composition is how we model 'has a' relations.  For example, a student 'has a' teacher.
# No information in teacher is modified by this relation.
# Composition is useful as it allows you to add points to other points without needing to inherit anything.