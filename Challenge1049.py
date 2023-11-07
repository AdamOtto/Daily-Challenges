"""
Given an array of a million integers between zero and a billion, out of order,
how can you efficiently sort it?
Assume that you cannot store an array of a billion elements in memory.
"""

# It isn't clear what the question considers to be efficient, so I'll assume
# that "better than bubble sort" is the answer.
# One possible solution is an external insertion sort.  Read one number from the array and store it into
# a file that holds a certain range (ex: 1 - 1000, 1001-2001).
# We insert the numbers into these files such that they are ordered from smallest to largest.
# Once all numbers in the array are read, we merge the files into the array
# starting with the file with the smallest range.

# Complexity O(nlogn), memory O(1) since we only need to hold the current value to insert
# and the value/index of the position in the range files we want to insert.