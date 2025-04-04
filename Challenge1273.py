"""
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
"""
class PrefixMapSum:
    d = None
    def __init__(self):
        self.d = {}
    
    def insert(self, key, value):
        self.d[key] = value
    
    def sum(self, prefix):
        retVal = 0
        for key, val in self.d.items():
            if prefix in key:
                retVal += val
        return retVal

PMS = PrefixMapSum()
PMS.insert("columnar", 3)
# Return 3
print(PMS.sum("col"))
PMS.insert("column", 2)
# Return 5
print(PMS.sum("col"))