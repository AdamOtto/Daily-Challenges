"""
A girl is walking along an apple orchard with a bag in each hand.
She likes to pick apples from each tree as she goes along,
but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order,
determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.
"""
def Solution(ar):
    l = len(ar)
    apples = []
    apples.append(ar[0])
    highestCount = 0
    start = 0
    count = 1
    
    # Find the first 2 different numbers to add into 'apples'
    for i in range(1, l):
        count += 1
        if ar[i] not in apples:
            start = i + 1
            apples.append(ar[i])
            break

    # Array is all the same number.
    if start == 0:
        return l
    highestCount = count
    offset = 0
    
    # Go through the rest of the list finding the longest subset of 2 unique numbers.
    for i in range(start, l):
        if ar[i] not in apples:
            apples.pop(0)
            apples.append(ar[i])
            highestCount = max(highestCount, count)
            count = 2
            if offset > 0:
                count += offset
                offset = 0
        else:
            # Keeps the most recent apple at position 1.
            if ar[i] != apples[1]:
                apples.pop(0)
                apples.append(ar[i])
            # If several of the same numbers appear in a row, we'll need an offset when a different number is found.
            else:
                offset += 1
            count += 1
    return max(highestCount, count)

# Returns 4
apples = [2, 1, 2, 3, 3, 1, 3, 5]
print(Solution(apples))

# Returns 3
apples = [1, 2, 3, 4, 3, 2, 1, 1]
print(Solution(apples))

# Returns 6
apples = [3, 1, 1, 2, 1, 1, 1]
print(Solution(apples))