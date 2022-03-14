"""
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888.
678 is not a palindrome.
Do not convert the integer into a string.
"""

def Solution(ar):
    temp = ar
    digits = []
    i = 1
    while i < temp:
        i *= 10
    i /= 10
    
    while i > 0.1:
        t = int(temp / i)
        digits.append(t)
        temp -= t * i
        i /= 10
    
    i = 0
    j = len(digits) - 1
    while i < j:
        if digits[i] != digits[j]:
            return False
        i += 1
        j -= 1
    return True


# Return True
print(Solution(121))

# Return True
print(Solution(888))

# Return False
print(Solution(122))

# Return False
print(Solution(678))

# Return True
print(Solution(21200010101000212))