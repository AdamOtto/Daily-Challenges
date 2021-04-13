"""
Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
"""

def Solution(in1):
    retVal = {}
    for key, val in in1.items():
        if type(val) is not dict:
            retVal[key] = val
        else:
            temp = Solution(val)
            for k, v in temp.items():
                s = key + "."
                retVal[s + k] = v
    return retVal


in1 = {"key": 3,
        "foo": {
            "a": 5,
            "bar": {
                "baz": 8
            }
        }
    }

print(Solution(in1))