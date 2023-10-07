"""
Given a linked list, remove all consecutive nodes that sum to zero.
Print out the remaining nodes.

For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6.
In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.
"""

class LL:
    val = None
    n = None
    def __init__(self, value, next = None):
        self.val = value
        self.n = next

    def printLL(self):
        retVal = ""
        retVal += str(self.val) + ", "
        temp = self.n
        while temp is not None:
            retVal += str(temp.val) + ", "
            temp = temp.n
        retVal += "None"
        print(retVal)

def Solution(ar):
    root = LL(0, ar)
    d = {}
    d[0] = root
    curSum = 0
    temp = ar
    while temp is not None:
        curSum += temp.val
        
        if curSum in d:
            prev = d[curSum]
            start = prev
            
            aux = curSum
            curSum = 0
            
            while prev != temp:
                prev = prev.n
                aux += prev.val
                if prev != temp:
                    d.pop(aux)
            start.n = temp.n
        else:
            d[curSum] = temp
        
        temp = temp.n
    
    return root.n
    
    
# Return 5, None
in1 = LL(3, LL(4, LL(-7, LL(5, LL(-6, LL(6))))))
in1.printLL()
Solution(in1).printLL()

print()

# Return original ll
in1 = LL(1, LL(2, LL(3, LL(4, LL(5, LL(6))))))
in1.printLL()
Solution(in1).printLL()

print()

# Return None
in1 = LL(1, LL(2, LL(3, LL(4, LL(5, LL(-15))))))
in1.printLL()
print(Solution(in1))