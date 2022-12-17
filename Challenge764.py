"""
Given a list of numbers, create an algorithm that arranges them in
order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510.
"""
def Solution(ar):
    ar.sort(key=lambda x: int(str(x)[0]), reverse=True)
    retVal = ""
    for i in ar:
        retVal += str(i)
    return int(retVal)
    
# Return 77641510
print(Solution([10, 7, 76, 415]))
# Return 98765432110
print(Solution([1,2,3,4,5,6,7,8,9,10]))