"""
Given a list of numbers, create an algorithm that arranges them in
order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
"""
# Quick solution
def Solution(ar):
    ar.sort(key=lambda x: int(str(x)[0]), reverse=True)
    print(ar)
    retVal = ""
    for i in ar:
        retVal += str(i)
    return int(retVal)

in1 = [10, 7, 76, 415]
print(Solution(in1))
in1 = [1,2,3,4,5,6,7,8,9,10]
print(Solution(in1))