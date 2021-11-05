"""
You are given a series of arithmetic equations as a string, such as:

y = x + 1
5 = x + 3
10 = z + y + 2
The equations use addition only and are separated by newlines.
Return a mapping of all variables to their values.
If it's not possible, then return null.

In this example, you should return:
{
  x: 2,
  y: 3,
  z: 5
}
"""

# Can solve if one equation can solve for 1 variable.  All I could do in 1 hour.  May need to revisit.
def Solution(ar):
    equations = {}
    variables = {}
    hold = ar.split("\n")
    for i in range(len(hold)):
        temp = hold[i].split(" ")
        key = None
        if not temp[0].isdigit():
            variables[temp[0]] = None
            equations[temp[0]] = []
            key = temp[0]
        else:
            equations[int(temp[0])] = []
            key = int(temp[0])
        for t in range(1, len(temp)):
            if temp[t].isdigit():
                equations[key].append(int(temp[t]))
            else:
                if temp[t] != "=" and temp[t] != "+":
                    equations[key].append(temp[t])
                    variables[temp[t]] = None
    
    #print(equations)
    #print(variables)
    
    OneSolFound = False
    for key, val in equations.items():
        if oneVarSolver(key, val, variables): 
            OneSolFound = True
    
    i = 0
    if OneSolFound:
        allSolved = False
        while not allSolved and i < 100:
            i += 1
            allSolved = True
            for key, val in equations.items():
                if not oneVarSolver(key, val, variables):
                    allSolved = False
    
    if allSolved:
        return variables
    else:
        return None
    
    
def oneVarSolver(Sum, Operands, var):
    count = 0
    varHolder = ""
    if Sum in var:
        if var[Sum] is None:
            val = 0
            for o in Operands:
                if isinstance(o, str):
                    if var[o] is not None:
                        val += var[o]
                    else:
                        return False
                else:
                    val += o
            var[Sum] = val
        else:
            val = var[Sum]
            for o in Operands:
                if isinstance(o, str):
                    if var[o] is not None:
                        val -= var[o]
                    else:
                        count += 1
                        if count > 1:
                            return False
                        varHolder = o
                else:
                    val -= o
            var[varHolder] = val
    else:
        val = Sum
        for o in Operands:
            if isinstance(o, str):
                if var[o] is not None:
                    val -= var[o]
                else:
                    count += 1
                    if count > 1:
                        return False
                    varHolder = o
            else:
                val -= o
        var[varHolder] = val
    return True
    

ar = "y = x + 1\n5 = x + 3\n10 = z + y + 2"
print(Solution(ar))


ar = "x = 1 + 3\ny = x + z\n10 = y + 2"
print(Solution(ar))
