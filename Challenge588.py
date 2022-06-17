"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""

class SparseArray:

    sparseArrayDic = {}

    def __init__(self, arr, size):
        sparseArrayDic = {}
        for i in range(0, size):
            if arr[i] != 0:
                self.sparseArrayDic[i] = arr[i]

    def set(self, i, val):
        if val == 0 and i in self.sparseArrayDic:
            self.sparseArrayDic.pop(i)
        else:    
            self.sparseArrayDic[i] = val

    def get(self, i):
        if i in self.sparseArrayDic:
            return self.sparseArrayDic[i]
        else:
            return 0


SA = SparseArray([0] * 1000, 1000)
SA.set(101, 1)
SA.set(442, 2)
# Return 1
print(SA.get(101))
# Return 0
print(SA.get(102))
# Return 0
print(SA.get(441))
# Return 2
print(SA.get(442))

# Return 0
SA.set(101, 0)
print(SA.get(101))