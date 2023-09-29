"""
Given a list, sort it using this method:
reverse(lst, i, j), which reverses lst from i to j.
"""
def reverse(lst, i, j):
    start = i
    end = j
    while start < end:
        temp = lst[start]
        lst[start] = lst[end]
        lst[end] = temp
        start += 1
        end -= 1
    return lst
    


# Return 
print(reverse([1,2,3,4,5,6,7,8,9,10], 3, 6))