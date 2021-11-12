"""
Write a function that takes in a number, string, list,
or dictionary and returns its JSON encoding. It should also handle nulls.

For example, given the following input:

[None, 123, ["a", "b"], {"c":"d"}]
You should return the following, as a string:

'[null, 123, ["a", "b"], {"c": "d"}]'
"""

def Solution(ar):
    if ar is None:
        return handleNone()
    elif isinstance(ar, str):
        return handleStr(ar)
    elif isinstance(ar, int):
        return handleInt(ar)
    elif isinstance(ar, int):
        return handleInt(ar)
    elif isinstance(ar, list):
        return handleList(ar)
    elif isinstance(ar, dict):
        return handleDict(ar)
    return None

def handleStr(ar):
    if ar is None:
        return handleNone()
    return "\"" + str(ar) + "\""

def handleInt(ar):
    if ar is None:
        return handleNone()
    return str(ar)

def handleNone():
    return "null"

def handleList(ar):
    retVal = "["
    for i in range(len(ar)):
        temp = ar[i]
        
        if temp is None:
            retVal += handleNone()
        elif isinstance(temp, int):
            retVal += handleInt(temp)
        elif isinstance(temp, str):
            retVal += handleStr(temp)
        elif isinstance(temp, list):
            retVal += handleList(temp)
        elif isinstance(temp, dict):
            retVal += handleDict(temp)
        if i != len(ar) - 1:
            retVal += ", "
    
    retVal += "]"
    return retVal
    
def handleDict(ar):
    c = 0
    l = len(ar)
    retVal = "{"
    for key, val in ar.items():
        if isinstance(key, str):
            retVal += handleStr(key)
        else:
            retVal += handleInt(key)
        retVal += ":"
        if isinstance(val, str):
            retVal += handleStr(val)
        else:
            retVal += handleInt(val)
        
        if c != len(ar) - 1:
            retVal += ", "
        c += 1
    retVal += "}"
    return retVal

# Return '[null, 123, ["a", "b"], {"c":"d"}]'
print(Solution([None, 123, ["a", "b"], {"c":"d"}]))

# Return '[1, 2, "3", [4, 5, 6], {7:8, 9:10}, 11, null, null]'
print(Solution([1,2,"3",[4,5,6], {7:8, 9:10}, 11, None, None]))

# Return '"123"'
print(Solution("123"))

# Return '{"a":1, "b":2, "c":null}'
print(Solution({"a":1, "b":2, "c":None}))