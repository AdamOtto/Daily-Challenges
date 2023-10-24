"""
Implement an efficient string matching algorithm.

That is, given a string of length N and a pattern of length k,
write a program that searches for the pattern in the string with
less than O(N * k) worst-case time complexity.

If the pattern is found, return the start index of its location.
If not, return False.
"""
# O(n)
def Solution(ar, pattern):
    la = len(ar)
    lp = len(pattern)
    patHash = hash(pattern)
    subStrHash = []
    retVal = []
    for i in range(0, la - lp + 1):
        if patHash == hash(ar[i:i+lp]):
            retVal.append(i)
    return retVal

in1 = "AABAABBAA"
pat = "AA"
print(Solution(in1, pat))

in1 = "10010110110111011011101010100010101011011101101110101011001010001011"
pat = "101101"
print(Solution(in1, pat))