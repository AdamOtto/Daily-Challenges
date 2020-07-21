def findTwoSum(l, k):
    cnt = len(l)
    if cnt == 0:
        return "False"
    h = {}
    h[l[0]] = l[0]
    for i in range(1, cnt):
        if k - l[i] in h:
            return "True"
        else:
            h[l[i]] = l[i]
    return "False"


in1 = [1,3,5,7,9,11]
in2 = 14
print(findTwoSum(in1,in2))
