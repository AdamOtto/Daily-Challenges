"""
An XOR linked list is a more memory efficient doubly linked list.
Instead of each node holding next and prev fields,
it holds a field named both, which is an XOR of the next node and the previous node.
Implement an XOR linked list; it has an add(element) which adds the element
to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python),
you can assume you have access to get_pointer and dereference_pointer
functions that converts between nodes and memory addresses.
"""

# I'll use a dict as a substitute for pointers.  The key will be the location in memory
# and an array [both, index] will hold address xor and the index value.

# Simple XOR calculator for a string of binary characters.
def XORStringOfBinaryCharacters(A, B):
    retval = ""
    if (len(A) != len(B)):
        return False
    for i in range (0, len(A)):
        if (A[i] == '0' and B[i] == '0') or (A[i] == '1' and B[i] == '1'):
            retval += "0"
        if (A[i] == '1' and B[i] == '0') or (A[i] == '0' and B[i] == '1'):
            retval += "1"
    return retval

# Class that contains my XOR linked list
class XorLinkedList():
    dictLinkedList = {}
    FirstAddress = ""
    prevAddress = ""
    currentAddress = ""

    def __init__(self, FirstAddress, FirstVal):
        self.FirstAddress = FirstAddress
        self.prevAddress = FirstAddress
        self.currentAddress = FirstAddress
        self.dictLinkedList[FirstAddress] = ["", FirstVal]


    def addVal(self, address, val):
        # Check to see if address exists in linked list
        if address in self.dictLinkedList:
            return "Address is occupied."
        # Reset 'pointer' to start of LL
        self.currentAddress = self.FirstAddress
        self.prevAddress = self.FirstAddress

        # If theres only 1 element in the linked list, add it.
        if self.dictLinkedList[self.FirstAddress][0] == "":
            # First element 'Both' points to itself and the second element.
            self.dictLinkedList[self.FirstAddress][0] = XORStringOfBinaryCharacters(self.FirstAddress, address)
            # Second element points to the first element.  Think of this as a one way round robin linked list.
            self.dictLinkedList[address] = [XORStringOfBinaryCharacters(self.FirstAddress, self.FirstAddress), val]
            return

        # Iterate to the second element in the list
        self.Next()
        # The last element in the list has a 'Both' value of prevAddress and the First Address.
        # Checks for this to determine if we reached the last element in the linked list.
        # Otherwise iterates to next element.
        while self.dictLinkedList[self.currentAddress][0] !=  XORStringOfBinaryCharacters(self.prevAddress, self.FirstAddress):
            self.Next()
        # Reset last element 'Both' value to point to new element.
        self.dictLinkedList[self.currentAddress][0] = XORStringOfBinaryCharacters(self.prevAddress, address)
        # Set new element to point to current element and first element in the list.
        self.dictLinkedList[address] = [XORStringOfBinaryCharacters(self.currentAddress, self.FirstAddress), val]

        return

    def Next(self):
        temp = self.currentAddress
        self.currentAddress = XORStringOfBinaryCharacters(self.dictLinkedList[self.currentAddress][0], self.prevAddress)
        self.prevAddress = temp
        return

    def get(self, index):
        # Make sure index is within bounds
        if (index < 0):
            return "index must be greater than 0"
        # Reset 'pointer' to start of linked list
        self.currentAddress = self.FirstAddress
        self.prevAddress = self.FirstAddress
        count = 0
        # Iterate until we reach the index
        while count != index:
            self.Next()
            count += 1
            # Because this is a pseudo round robin, if the index is higher than the length of the linked list we'll
            # just keep going around with this check.
            if (self.currentAddress == self.FirstAddress):
                self.prevAddress = self.FirstAddress
        # Return value at index.
        return self.dictLinkedList[self.currentAddress][1]


ll = XorLinkedList("1010", "1,2,3")
ll.addVal("0101", "4,5,6")
ll.addVal("0111", "5,6,7")
ll.addVal("0110", "7,8,9")
ll.addVal("0011","10,11,12")
ll.addVal("1011","13,14,15")
ll.addVal("1110","16,17,18")
print(ll.dictLinkedList)
print(ll.get(5))