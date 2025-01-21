"""
Gray code is a binary code where each successive value differ in only one bit,
as well as when wrapping around. Gray code is common in hardware so that we don't
see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""
def Solution(ar):
    if ar <= 0:
        return False
    
    gray = ["0", "1"]
    if ar == 1:
        return gray
    
    retVal = []
    
    for i in range(1, ar):
        retVal = []
        l = len(gray)
        for j in range(0, l):
            retVal.append("0" + gray[j])
        for j in reversed(range(0, l)):
            retVal.append("1" + gray[j])
        gray = retVal
    return retVal

# Return ['00', '01', '11', '10']
print(Solution(2))

# Return ['000', '001', '011', '010', '110', '111', '101', '100']
print(Solution(3))

# Return ['0000', '0001', '0011', '0010', '0110', '0111', '0101', '0100', '1100', '1101', '1111', '1110', '1010', '1011', '1001', '1000']
print(Solution(4))