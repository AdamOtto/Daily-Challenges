"""
Write a program that checks whether an integer is a palindrome.
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome.
Do not convert the integer into a string.
"""

def Solution(ar):
    arCop = ar
    reverseAr = 0
    dividor = 1
    
    while dividor <= ar:
        dividor *= 10
    dividor = dividor / 10
    div2 = 1
    while arCop > 0:
        temp = arCop // dividor
        reverseAr += temp * div2
        arCop -= temp * dividor
        dividor = dividor / 10
        div2 *= 10
    
    if reverseAr == ar:
        return True
    return False

# Return True
print(Solution(11211))

# Return False
print(Solution(123))

# Return True
print(Solution(1234567887654321))