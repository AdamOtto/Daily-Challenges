'''
Given a set of closed intervals, find the smallest set of numbers that covers all the intervals.
If there are multiple smallest sets, return any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set of numbers that covers all these intervals is {3, 6}.
'''

def Solutions(in1):
    
    tlow = in1[0][1]
    thigh = in1[0][0]
    
    for i in in1:
        if i[0] > thigh:
            thigh = i[0]
        if i[1] < tlow:
            tlow = i[1]
    
    if tlow > thigh:
        return (tlow - 1, tlow)
    
    return (tlow, thigh)
    
#in1 = [ (0,3), (2,6), (3,4), (6,9) ]
#in1 = [ (200,300), (0,3),(1,4),(2,5), (57, 94) ]
in1 = [ (1,5),(2,6), (3,5) ]
t = Solutions(in1)
print(t)