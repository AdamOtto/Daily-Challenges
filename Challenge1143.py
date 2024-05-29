"""
Given k singly linked lists,
write a function to merge all the lists
into one singly linked list.
"""

class LL:
    val = None
    n = None
    
    def __init__(self, Value, Next = None):
        self.val = Value
        self.n = Next

def printLL(ar):
    retVal = ""
    temp = ar
    while temp is not None:
        retVal += str(temp.val) + " -> "
        temp = temp.n
    retVal += "None"
    print(retVal)

def Solution(ar, k):
    if k == 0:
        return None
    if k == 1:
        return ar[0]
    count = 1
    retVal = ar[0]
    while retVal.n is not None:
        retVal = retVal.n
    
    while count < k:
        retVal.n = ar[count]
        while retVal.n is not None:
            retVal = retVal.n 
        count += 1
    return ar[0]

# Return 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> None
in1 = LL(1, LL(2, LL(3)))
in2 = LL(4, LL(5, LL(6)))
in3 = LL(7, LL(8, LL(9)))

retVal = Solution([in1, in2, in3], 3)
printLL(retVal)

# Return a -> b -> c -> d -> e -> f -> g -> h -> i -> j -> k -> l -> None
in1 = LL('a', LL('b', LL('c', LL('d'))))
in2 = LL('e')
in3 = LL('f', LL('g', LL('h')))
in4 = LL('i', LL('j', LL("k", LL("l"))))
retVal = Solution([in1, in2, in3, in4], 4)
printLL(retVal)