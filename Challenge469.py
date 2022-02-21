"""
Mastermind is a two-player game in which the first player attempts
to guess the secret code of the second. In this version,
the code may be any six-digit number with all distinct digits.

Each turn the first player guesses some number,
and the second player responds by saying how many digits in this
number correctly matched their location in the secret code.
For example, if the secret code were 123456, then a guess of 175286 would score two,
since 1 and 6 were correctly placed.

Write an algorithm which, given a sequence of guesses and their scores,
determines whether there exists some secret code that could have produced them.

For example, for the following scores you should return True,
since they correspond to the secret code 123456:
{175286: 2, 293416: 3, 654321: 0}

However, it is impossible for any key to result in the following scores,
so in this case you should return False:
{123456: 4, 345678: 4, 567890: 4}
"""

# Brute force solution, O(N)
def Solution(ar):
    l = len(ar)
    for i in range(999999 + 1):
        matches = 0
        t1 = str(i)
        if len(t1) < 6:
            while len(t1) < 6:
                t1 = '0' + t1
        for key, val in ar.items():
            count = 0
            t2 = str(key)
            for j in range(6):
                if t1[j] == t2[j]:
                    count += 1
            if count == val:
                matches += 1
        if matches == l:
            return True
    return False

# Return True
print(Solution({175286: 2, 293416: 3, 654321: 0}))
# Return False
print(Solution({123456: 4, 345678: 4, 567890: 4}))
# Return True
print(Solution({'000000':0, 111111: 0, 222222: 0, 333333: 0, 444444:0, 555555:0, 666666:0, 777777:0, 888888:0, 999999:6}))
# Return False
print(Solution({'000000':0, 111111: 0, 222222: 0, 333333: 0, 444444:0, 555555:0, 666666:0, 777777:0, 888888:0, 999999:5}))