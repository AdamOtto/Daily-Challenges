"""
Given an unordered list of flights taken by someone,
each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary.

If no such itinerary exists, return null.
If there are multiple possible itineraries,
return the lexicographically smallest one.
All flights must be used in the itinerary.

For example,
given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL',
you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
"""
def getLexicographicallySmallest(ar):
    if len(ar) == 0:
        return None
    if len(ar) == 1:
        return 0
    l = len(ar[0])
    for a in ar:
        l = min(len(a), l)
    last = smallest = ord(ar[0][0])
    index = 0
    # Find the first string with the lowest ord for lexicographically smallest
    for i in range(l):
        for j in range(len(ar)):
            if ord(ar[j][i]) < smallest:
                smallest = ord(ar[j][i]) 
                index = j
        if smallest != last:
            return index
        last = smallest
    # If strings are all the same except in length, return shortest string.
    smallest = len(ar[0])
    index = 0
    for i in range(len(ar)):
        if len(ar[i]) < smallest:
            smallest = len(ar[i])
            index = i
    return index

def allFlightsIncluded(d):
    for key, val in d.items():
        if len(val) != 0:
            return False
    return True
           
def Solution(flights, start):
    d = {}
    s = set()
    for i in range(len(flights)):
        if flights[i][0] not in d:
            d[flights[i][0]] = []
        d[flights[i][0]].append(flights[i][1])
        s.add(flights[i][0])
        s.add(flights[i][1])
    l = len(s)
    retVal = []
    retVal.append(start)
    retVal = Helper(d, start, l, retVal)
    return retVal

def Helper(d, cur, l, flightlist):
    if len(flightlist) >= l and allFlightsIncluded(d):
        return flightlist
    
    temp = []
    if cur in d:
        temp.extend(d[cur])
    else:
        return None
    
    while len(temp) > 0:
        nextCur = temp.pop(getLexicographicallySmallest(temp))
        newd = d.copy()
        newd[cur].remove(nextCur)
        nextflightlist = []
        nextflightlist.extend(flightlist)
        nextflightlist.append(nextCur)
        temp2 = Helper(newd, nextCur, l, nextflightlist)
        if temp2 is not None:
            return temp2
    
    return None
    
# Return ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
print(Solution([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))

# Return ['A', 'B', 'C', 'A', 'C']
print(Solution([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))

# Return None
print(Solution([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))