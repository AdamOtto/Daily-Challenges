"""
Given a string, generate all possible subsequences of the string.

For example, given the string xyz, return an array or set with the following strings:


x
y
z
xy
xz
yz
xyz
Note that zx is not a valid subsequence since it is not in the order of the given string.
"""
# Find all substrings (order doesn't matter)
def Solution1(ar):
    l = len(ar)
    for i in range(0, pow(2, l)):
        temp = i
        prVal = ""
        j = 0
        while temp > 0:
            if temp & 1 == 1:
                prVal += ar[j]
            j += 1
            temp >>= 1
        print(prVal)

# Find all substrings (order matters)
def Solution2(ar):
    l = len(ar)
    for i in range(1, l + 1):
        for j in range(i,l + 1):
            temp = ar[j - i: j]
            print(temp)
    
Solution1("xyz")
print()
Solution2("xyz")   
