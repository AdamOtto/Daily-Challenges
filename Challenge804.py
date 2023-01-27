"""
You are given a huge list of airline ticket prices between different
cities around the world on a given day. These are all direct flights.
Each element in the list has the format (source_city, destination, price).
Consider a user who is willing to take up to k connections from their
origin city A to their destination B. Find the cheapest fare possible
for this journey and print the itinerary for that journey.
For example, our traveler wants to go from JFK to LAX with up to 3 connections,
and our input flights are as follows:
[
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
Due to some improbably low flight prices, the cheapest itinerary would be
JFK -> ATL -> ORD -> LAX
costing $440.
"""
import sys

def Solution(ar, k, start, end):
    gr = {}
    visitedPrice = {}
    visitedConnection = {}
    
    for i in range(len(ar)):
        if ar[i][0] not in gr:
            gr[ar[i][0]] = []
        if ar[i][1] not in gr:
            gr[ar[i][1]] = []
        gr[ar[i][0]].append(ar[i][1])

    for key, val in gr.items():
        visitedPrice[key] = sys.maxsize
        visitedConnection[key] = None
    visitedPrice[start] = 0
    visitedConnection[start] = 0
    
    next = []
    for n in gr[start]:
        next.append( (start, n) )
    
    last = None
    visited = set()

    while len(next) != 0:
        temp = next.pop(0)
        last = temp[0]
        cur = temp[1]
        price = getPrice(cur, last, ar)
        visited.add( (last, cur) )
        
        if visitedConnection[last] + 1 <= k:
            if visitedConnection[cur] is None:
                visitedConnection[cur] =  visitedConnection[last] + 1
                visitedPrice[cur] = price + visitedPrice[last]
            else:
                if visitedPrice[last] + price < visitedPrice[cur]:
                    visitedConnection[cur] =  visitedConnection[last] + 1
                    visitedPrice[cur] = price + visitedPrice[last]
        
            for n in gr[cur]:
                if (cur, n) not in visited:
                    next.append( (cur, n) )

    if visitedConnection[end] is not None:
        return (visitedPrice[end], visitedConnection[end])
    else:
        return (None, None)
    
def getPrice(cur, last, ar):
    for i in ar:
        if i[0] == last and i[1] == cur:
            return i[2]
    return sys.maxsize

# Return (440, 3)  
in1 = [
    ('JFK', 'ATL', 150),
    ('ATL', 'SFO', 400),
    ('ORD', 'LAX', 200),
    ('LAX', 'DFW', 80),
    ('JFK', 'HKG', 800),
    ('ATL', 'ORD', 90),
    ('JFK', 'LAX', 500),
]
k = 3
start = 'JFK'
end = 'LAX'
t = Solution(in1, k, start, end)
print("End price: ", t[0], ", Total connections: ", t[1])


# Return (250, 3)
in1 = [
    (1,2,100),
    (1,3,200),
    (2,3,50),
    (3,4,100),
    (4,5,100),
    (5,6,100),
    (6,1,100)
]
k = 3
start = 1
end = 4
t = Solution(in1, k, start, end)
print("End price: ", t[0], ", Total connections: ", t[1])

# Return (None, None)
in1 = [
    (1,2,100),
    (1,3,200),
    (2,3,50),
    (3,4,100),
    (4,5,100),
    (5,6,100),
    (6,1,100)
]
k = 3
start = 1
end = 6
t = Solution(in1, k, start, end)
print("End price: ", t[0], ", Total connections: ", t[1])