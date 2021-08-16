"""
A competitive runner would like to create a route that starts and ends
at his house, with the condition that the route goes entirely uphill
at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation},
and a dictionary mapping paths between some of these locations to their
corresponding distances, find the length of the shortest route satisfying
the condition above. Assume the runner's home is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.
"""
import sys

def Solution(elevations, paths):
    allRoutes = []
    # Get all routes
    for key, val in paths.items():
        if key[0] == 0:
            getAllRoute(key[1], [], paths, allRoutes)
    #print(allRoutes)
    
    #Check elevation requirement.
    shortestRoute = sys.maxsize
    retVal = None
    for route in allRoutes:
        PossiblePath = True
        uphill = elevations[0] < elevations[route[0]]
        total = paths[(0, route[0])]
        for i in range(1, len(route)):
            if uphill and elevations[route[i - 1]] > elevations[route[i]]:
                uphill = False
            elif not uphill and elevations[route[i - 1]] < elevations[route[i]]:
                PossiblePath = False
                break
            total += paths[(route[i - 1], route[i])]
        if PossiblePath:
            t = min(total, shortestRoute)
            if t < shortestRoute:
                retVal = route
                shortestRoute = t
    if retVal != None:
        return shortestRoute, retVal
    else:
        return False


def getAllRoute(cur, curRoute, paths, allRoutes):
    if cur == 0:
        curRoute.append(cur)
        allRoutes.append(curRoute)
    
    for key, val in paths.items():
        if key[0] == cur and key[1] not in curRoute:
            temp = []
            temp.extend(curRoute)
            temp.append(cur)
            getAllRoute(key[1], temp, paths, allRoutes)
    
    return


# Returns (28, [2,4,0])
elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}
print(Solution(elevations, paths))

# Returns (13, [2,4,5,0])
elevations = {0: 1, 1: 5, 2: 2, 3: 3, 4: 4, 5:5}
paths = {
    (0, 1): 10,
    (0, 2): 5,
    (1, 2): 1,
    (1, 3): 5,
    (2, 3): 10,
    (2, 4): 5,
    (3, 4): 5,
    (4, 5): 2,
    (5, 0): 1
    
}
print(Solution(elevations, paths))

# Returns False.  No routes back to 0.
elevations = {0: 1, 1: 2, 2: 2}
paths = {
    (0, 1): 10,
    (1, 2): 10
}
print(Solution(elevations, paths))

# Returns False.  No routes meet elevation criteria.
elevations = {0: 3, 1: 2, 2: 3, 3:4}
paths = {
    (0, 1): 10,
    (1, 2): 10,
    (2, 3): 10,
    (3, 0): 10
}
print(Solution(elevations, paths))