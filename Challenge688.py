"""
A Boolean formula can be said to be satisfiable if there is a way to assign truth
values to each variable such that the entire formula evaluates to true.
For example, suppose we have the following formula,
where the symbol - is used to denote negation:
(-c OR b) AND (b OR c) AND (-b OR c) AND (-c OR -a)
One way to satisfy this formula would be to let a = False, b = True, and c = True.
This type of formula, with AND statements joining tuples
containing exactly one OR, is known as 2-CNF.
Given a 2-CNF formula, find a way to assign truth values to satisfy it,
or return False if this is impossible.
"""

class Or:
    left = None
    right = None
    
    def __init__(self, leftSide, rightSide):
        self.left = leftSide
        self.right = rightSide
    
    def evaluate(self, values):
        return self.value(values) or self.value(values, False)
    
    def value(self, values, leftSide = True):
        if leftSide:
            if "-" in self.left:
                return not values[self.left[1:]]
            else:
                 return values[self.left]
        else:
            if "-" in self.right:
                return not values[self.right[1:]]
            else:
                 return values[self.right]

def Solution(ar):
    ar = ar.replace(" ", "")
    ar = ar.replace("(", "")
    ar = ar.replace(")", "")
    ar = ar.split("AND")
    #print(ar)
    equations = []
    variables = []
    for i in range(len(ar)):
        temp = ar[i].split("OR")
        equations.append(Or(temp[0], temp[1]))
        if "-" in temp[0]:
            temp[0] = temp[0].replace("-", "")
        if "-" in temp[1]:
            temp[1] = temp[1].replace("-", "")
        
        if temp[0] not in variables:
            variables.append(temp[0])
        if temp[1] not in variables:
            variables.append(temp[1])
    
    #print(variables)
    l = pow(2, len(variables))
    #print(l)
    values = {}
    for i in range(0, l):
        values = helper(variables, i)
        AllTrue = True
        for i in range(len(equations)):
            if not equations[i].evaluate(values):
                AllTrue = False
        if AllTrue:
            return values
    return False

def helper(variables, num):
    d = {}
    for i in reversed(range(len(variables))):
        if num & 1 == 1:
            d[variables[i]] = True
        else:
            d[variables[i]] = False
        num >>= 1
    return d
    
    

# Return a=false, b=true, c=true
in1 = "(-c OR b) AND (b OR c) AND (-b OR c) AND (-c OR -a)"
print(Solution(in1))

# Return a=false, b=true, c=false, d=true, e=true, f=true
in1 = "(a OR b) AND (c OR d) AND (-d OR e) AND (-e OR f) AND (-f OR -a)"
print(Solution(in1))