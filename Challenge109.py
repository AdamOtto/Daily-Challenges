'''
Given an unsigned 8-bit integer, swap its even and odd bits.
The 1st and 2nd bit should be swapped, the 3rd and 4th bit should be swapped,
and so on.

For example, 10101010 should be 01010101.
11100010 should be 11010001.
'''


def Solution(in1):
    bits = ""
    bits = str(in1)
    if len(bits) == 7:
        bits = "0" + bits

    oddBit = []
    evenBit = []

    for i in range(0, len(bits)):
        if (i + 1) % 2 > 0:
            oddBit.append(int(bits[i]))
            evenBit.append(0)
        else:
            evenBit.append(int(bits[i]))
            oddBit.append(0)

    evenBit.pop(0)
    evenBit.append(0)
    oddBit.pop(len(bits) - 1)
    oddBit.insert(0, 0)

    combo = ""

    for i in range(0, len(bits)):
        combo += str(evenBit[i] | oddBit[i])
    print(combo)


in1 = 10101010
Solution(in1)

in1 = 11100010
Solution(in1)

in1 = 1010101  # 01010101
Solution(in1)