"""
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map.
If the key already exists, overwrite the value.

sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
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

in1 = PrefixMapSum()
in1.insert("Column", 1)
in1.insert("Columns", 2)
in1.insert("ColumnsAreCool", 3)

print(in1.Sum("ColumnsAre"))
print(in1.Sum("Col"))