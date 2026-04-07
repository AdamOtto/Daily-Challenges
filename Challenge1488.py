"""
We're given a hashmap associating each courseId key with a list of courseIds values,
which represents that the prerequisites of courseId are courseIds.
Return a sorted ordering of courses such that we can finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []},
should return ['CSC100', 'CSC200', 'CSCS300'].
"""
# O(n^2) Solution
def Solution(ar):
    emptyFound = False
    courses = []
    d = set()
    retVal = []
    for key, val in ar.items():
        if len(val) == 0:
            emptyFound = True
            d.add(key)
            retVal.append(key)
        else:
            courses.append(key)
    if not emptyFound:
        return None
    
    count = len(courses)
    while len(courses) > 0 and count > 0:
        hold = []
        for i in range(len(courses)):
            addToHold = True
            for c in ar[courses[i]]:
                if c not in d:
                    addToHold = False
                    break
            if addToHold:
                hold.append(courses[i])
        
        for h in hold:
            retVal.append(courses.pop(courses.index(h)))
            d.add(retVal[-1])
        
        count -= 1
    
    if count < 0:
        return None
    return retVal

# Return ['CSC100', 'CSC200', 'CSC300']
print(Solution({'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}))

# Return ['d', 'f', 'g', 'h', 'j', 'k', 'e', 'i', 'b', 'c', 'a']
print(Solution({'a': ['b', 'c', 'd'], 'b': ['e', 'f', 'g'], 'c': ['h', 'i', 'j'], 'd':[],  'e': ['k'], 'f':[], 'g':[], 'h':[], 'i':['k'], 'j':[], 'k':[]}))