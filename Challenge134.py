"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

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
        self.sparseArrayDic[i] = val

    def get(self, i):
        if i in self.sparseArrayDic:
            return self.sparseArrayDic[i]
        else:
            return 0

arr = [1,0,0,0,0,0,0,0,0,0,0,0,23,0,0,0,0,0,5,0,0,0,0,0,0,0,0,10,11,12,13,0,0,0,0,0,0,0,0]
x = SparseArray(arr, len(arr))
print("get(0) = " + str(x.get(0)))
print("get(12) = " + str(x.get(12)))
print("get(18) = " + str(x.get(18)))
print("get(27) = " + str(x.get(27)))
print("get(31) = " + str(x.get(31)))
x.set(31, 31)
print("get(31) = " + str(x.get(31)))
