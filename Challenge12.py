"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
Given N, write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.
"""

def findSteps(x, Steps):
    d = {}
    d[0] = 1
    d[1] = 1
    d[2] = 2
    
    if x in d:
        return d[x]
        
    for i in range(3, x+1):
        temp = 0
        for step in Steps:
            if i - step in d:
                #print(str(temp) + " += " + "d[" + str(i - step) + "]." + str(d[i - step]))
                temp += d[i - step]
        #print("d[" + str(i) + "] = " + str(temp) + "\n")
        d[i] = temp
        
    return d[x]
    
steps = 4
climb = [1,2]

print(findSteps(steps,climb))