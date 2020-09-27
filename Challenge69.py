'''
Given a list of integers
return the largest product that can be made by multiplying any three integers.

You can assume the list has at least three integers.
'''


def Solution(in1):
    products = []

    for h in range(0, len(in1) - 2):
        for i in range(h+1, len(in1) - 1):
            for j in range(i+1, len(in1)):
                products.append(in1[h] * in1[i] * in1[j])

    print(max(products))


in1 = [-10, 10, 5, 2]
Solution(in1)