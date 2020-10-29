'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.
'''


def Solution(in1):
    in1 = sorted(in1)
    r = []
    r.append(in1[0])
    for i in range(1,len(in1)):
        add = False
        for j in range(0, len(r)):
            if type(r[j]) is tuple:
                if r[j][0] - 1 == in1[i]:
                    t = r[j][1]
                    r[j] = (in1[i], t)
                    add = False
                    break
                elif r[j][1] + 1 == in1[i]:
                    t = r[j][0]
                    r[j] = (t, in1[i])
                    add = False
                    break
                else:
                    add = True
            elif type(r[j]) is int:
                t = r[j]
                if t - 1 == in1[i]:
                    r[j] = (in1[i], t)
                    add = False
                    break
                elif t + 1 == in1[i]:
                    r[j] = (t, in1[i])
                    add = False
                    break
                else:
                    add = True
        if add:
            r.append(in1[i])
    
    retValTup = 0
    print(r)
    for ran in r:
        if type(ran) is tuple:
            retValTup = max(retValTup, len(range( ran[0], ran[1] )) + 1)
            
    if retValTup != 0:
        print(retValTup)
        return
    else:
        print(1)
        return 1
    
    

in1 = [100, 4, 200, 1, 3, 2, 101]
#in1 = [1,2,5,6,7,8,3]
Solution(in1)