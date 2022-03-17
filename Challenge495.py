"""
Given a stream of elements too large to store in memory,
pick a random element from the stream with uniform probability.
"""


#Pseudocode
def Solution(ar):
    firstAddress = getMemory(ar, first = True, last = False)
    lastAddress = getMemory(ar, first = False, last = True)
    
    toGet = convertToAddressByte(random.uniform(firstAddress, lastAddress))
    
    return getElement(toGet)