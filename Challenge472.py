"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable.
For example, '001' is not allowed.
"""

def Solution(ar):
    count = [0] * (len(ar) + 1)
    count[0] = count[1] = 1
    
    for i in range(2, len(ar) + 1):
        if int(ar[i - 1]) > 0:
            count[i] = count[i - 1]
        if (ar[i - 2] == '1' or ar[i-2] == '2') and int(ar[i - 1]) in range(0, 6 + 1):
            count[i] += count[i-2]
    return count[len(ar)]

# Return 3
print(Solution("111"))

# Return 10
print(Solution("261121"))

# Return 34
print(Solution("12122123"))