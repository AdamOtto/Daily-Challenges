"""
Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""
import numpy as n

in1 = [1,2,3,4,5]

"""
#solutions 1 = with division
tot = n.prod(in1)
out = []
for x in in1:
    out.append(tot/x)

print(out)
"""

length = len(in1)
temp = 1
out1 = [0]*length

for i in range(0, length):
    out1[i] = temp
    temp *= in1[i]
    
temp = 1
out2 = [0]*length 
for i in reversed( range(0,length) ):
    out2[i] = temp
    temp *= in1[i]

out = []
for i in range(0,length):
    out.append(out1[i] * out2[i])
    
print(out)