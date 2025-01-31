"""
Given a sorted list of integers, square the elements and give the output in sorted order

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""
def Solution(ar):
    return sorted([i ** 2 for i in ar])


# Return [0, 4, 4, 9, 81]
print(Solution([-9, -2, 0, 2, 3]))

# Return [4, 4, 25, 25]
print(Solution([-5, -2, 2, 5]))