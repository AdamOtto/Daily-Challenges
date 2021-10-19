"""
You are given a histogram consisting of rectangles of different heights.
These heights are represented in an input list,
such that [1, 3, 2, 5] corresponds to the following diagram:

      x
      x  
  x   x
  x x x
x x x x
Determine the area of the largest rectangle that can be formed only from the bars of the histogram.
For the diagram above, for example, this would be six, representing the 2 x 3 area at the bottom right.
"""

def Solution(hist):
    stack1 = []
    l = len(hist)
    retVal = 0
    i = 0
    while i < l:
        if len(stack1) == 0 or hist[i] >= hist[stack1[-1]]:
            stack1.append(i)
            i += 1
        elif hist[i] < hist[stack1[-1]]:
            top = stack1.pop()
            retVal = max(retVal, hist[top] * ((i - stack1[-1] - 1) if stack1 else i))
    
    while len(stack1) > 0:
        top = stack1.pop()
        retVal = max(retVal, hist[top] * ((i - stack1[-1] - 1) if stack1 else i))
    return retVal


in1 = [1, 3, 2, 5]
print(Solution(in1))

in1 = [4,4,4,4]
print(Solution(in1))

in1 = [4,4,100,4]
print(Solution(in1))