"""
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
"""


def Solution(num):
    reversedCopy = 0
    temp = num
    deci = 1
    deciCopy = 1
    #print(int(temp / deci))
    while int(temp / deci) != 0:
        deci *= 10
    deci = deci / 10
    #print(int(temp / deci))

    while temp != 0:
        reversedCopy += int(temp / deci) * deciCopy
        temp -= int(temp / deci) * deci
        deci = deci / 10
        deciCopy *= 10

    if num == reversedCopy:
        return True
    return False



print(Solution(8827288))
print(Solution(123))
print(Solution(12321))
print(Solution(1001))