'''
At a popular bar, each customer has a set of favorite drinks,
and will happily accept any drink among this set.
For example, in the following situation,
customer 0 will be satisfied with drinks 0, 1, 3, or 6.

preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
A lazy bartender working at this bar is trying to reduce his
effort by limiting the drink recipes he must memorize.
Given a dictionary input such as the one above,
return the fewest number of drinks he must learn in order to satisfy all customers.

For the input above, the answer would be 2, as drinks 1 and 5 will satisfy everyone.
'''

import itertools

def Solution(pref):
    prefl = len(pref)
    drinks = {}
    uniqDrinks = []
    
    for key, val in pref.items():
        for v in val:
            if v not in drinks:
                drinks[v] = set()
                uniqDrinks.append(v)
    uniqDrinks = sorted(uniqDrinks)
    l = len(uniqDrinks)
    #print(uniqDrinks)
    
    for dkey, dval in drinks.items():
        for key, val in pref.items():
            if dkey in val:
                dval.add(key)
    #print(drinks)
    
    for i in range(1, l + 1):
        subs = getSubsets(uniqDrinks, i)
        for s in subs:
            drinkSet = set()
            for j in range(0, i):
                drinkSet = drinkSet.union( drinks[s[j]] )
            if len(drinkSet) == prefl:
                return (i, s)
    return False    
    
def getSubsets(ls, n):
    return list(itertools.combinations(ls, n))

# Should return (2, (1, 5))
preferences = {
    0: [0, 1, 3, 6],
    1: [1, 4, 7],
    2: [2, 4, 7, 5],
    3: [3, 2, 5],
    4: [5, 8]
}
print(Solution(preferences))

# Should return (3, (0, 2 ,4))
preferences = {
    0: [0, 1],
    1: [1, 2],
    2: [2, 3],
    3: [3, 4],
    4: [4, 5],
    5: [0, 5]
}
print(Solution(preferences))

# Should return (3, (0, 1, 2))
preferences = {
    0: [0],
    1: [1],
    2: [2],
}
print(Solution(preferences))

# Should return False
preferences = {
    0: [],
    1: [],
    2: [],
}
print(Solution(preferences))