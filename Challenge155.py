"""
Given a list of elements, find the majority element,
which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""
import math

# Solution 1.  O(n) time, O(1) space.  Doesn't always work.
"""
def findCandidate(arr):
    max_index = 0
    count = 2
    for i in range(0, len(arr)):
        if arr[i] == arr[max_index]:
            count += 1
        else:
            count -= 1

        if count <= 0:
            max_index = i
            count = 2
    return arr[max_index]

def isMajority(arr, cand):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == cand:
            count += 1

    if count >= math.floor(len(arr) / 2.0):
        return True
    return False

def Solution(arr):
    cand = findCandidate(arr)
    #print(cand)
    if isMajority(arr, cand):
        print(cand)
    else:
        print("No majority element")

in1 = [1, 2, 1, 1, 3, 4, 0, 2, 2, 1, 1]
Solution(in1)
"""

#Solution 2.  O(n) time, O(n) space.  Guaranteed to work.
def Solution(arr):
    d = {}
    for i in range(0, len(arr)):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] += 1

    half = math.floor(len(arr) / 2.0)
    for key,value in d.items():
        if value >= half:
            print(key)
            return
    print("No majority element")

#in1 = [1, 2, 1, 1, 3, 4, 0]
in1 = [1, 2, 1, 1, 3, 4, 0, 2, 2, 1, 1, 2, 2, 2, 2]
Solution(in1)