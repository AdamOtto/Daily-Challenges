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

    def Sum(self, key):
        t = 0
        for k, v in self.d.items():
            if key in k:
                t += v
        return t
    
    def Get(self, key):
        if key in self.d:
            return self.d[key]
        return None

# Print nothing if successful.
mapsum = PrefixMapSum()
mapsum.insert("columnar", 3)
assert mapsum.Sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.Sum("col") == 5