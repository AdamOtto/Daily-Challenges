"""
The number 6174 is known as Kaprekar's contant,
after the mathematician who discovered an associated property:

for all four-digit numbers with at least two distinct digits,
repeatedly applying a simple procedure eventually results in this value.

The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Write a function that returns how many steps this will take for a given input N.
"""


def Solution(ar):
    s = set()
    for x in str(ar):
        s.add(x)
    if len(s) < 2 or len(str(ar)) != 4:
        return 0
    temp = ar
    count = 0
    while temp != 6174:
        temp = str(temp)
        if len(temp) < 4:
            while len(temp) < 4:
                temp = "0" + temp
        temp = int("".join(sorted([x for x in temp], reverse=True))) - int(
            "".join(sorted([x for x in temp]))
        )
        count += 1
    return count


# Return 3
print(Solution(1234))

# Return 3
print(Solution(9876))

# Return 5
print(Solution(1112))