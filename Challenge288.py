'''
The number 6174 is known as Kaprekar's contant, after the mathematician who
discovered an associated property: for all four-digit numbers with at least
two distinct digits, repeatedly applying a simple procedure eventually results
in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in
ascending and descending order.
Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Write a function that returns how many steps this will take for a given input N.
'''

def Solution(ar):
    largeNum = genDescNum(ar)
    smallNum = genAscNum(ar)
    Kaprekar = largeNum - smallNum
    count = 1
    #print(Kaprekar)
    
    while Kaprekar != 6174:
        largeNum = genDescNum(Kaprekar)
        smallNum = genAscNum(Kaprekar)
        Kaprekar = largeNum - smallNum
        count += 1
        #print(Kaprekar)
    return count



def genAscNum(ar):
    res = [int(x) for x in str(ar)]
    res.sort()
    retVal = 0
    while len(res) > 0:
        l = len(res)
        retVal += pow(10, l - 1) * res.pop(0)
    return retVal
    
def genDescNum(ar):
    res = [int(x) for x in str(ar)]
    res.sort(reverse = True)
    retVal = 0
    while len(res) > 0:
        l = len(res)
        retVal += pow(10, l - 1) * res.pop(0)
    return retVal



print("Solution return value: " + str(Solution(1324)))

print("Solution return value: " + str(Solution(1010)))

print("Solution return value: " + str(Solution(1024)))

print("Solution return value: " + str(Solution(9876)))