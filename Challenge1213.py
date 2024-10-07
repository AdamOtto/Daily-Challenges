"""
The stable marriage problem is defined as follows:

Suppose you have N men and N women, and each person has ranked their
prospective opposite-sex partners in order of preference.

For example, if N = 3, the input could be something like this:

guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

gal_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
Write an algorithm that pairs the men and women together in such a way
that no two people of opposite sex would both rather be with each other than with their current partners.
"""

def Solution(N, men, women):
    wPartner = {}
    for key, val in women.items():
        wPartner[key] = ""
        
    MFree = {}
    for key, val in men.items():
        MFree[key] = False
    free = len(MFree)

    while free > 0:
        m = ""
        for key, val in MFree.items():
            if not val:
                m = key
                break
            
        f = 0
        mPref = men[m]
        for w in mPref:
            if wPartner[w] == "":
                wPartner[w] = m
                MFree[m] = True
                free -= 1
                break
            else:
                curPartner = wPartner[w]
                if fPrefersM1overM2(women[w], m, curPartner):
                    wPartner[w] = m
                    MFree[m] = True
                    MFree[curPartner] = False
                    break
                    
        
    for key, val in wPartner.items():
        print(key, val)
    return
            
def fPrefersM1overM2(womenPref, m1, m2):
    for i in range(0, len(womenPref)):
        if womenPref[i] == m1:
            return True
        if womenPref[i] == m2:
            return False
            

# Expected results m1 w1, m2 w2
N = 2
guy_preferences = {
    "m1":["w1", "w2"],
    "m2":["w1", "w2"]}
    
girl_preferences = {
    "w1":["m1", "m2"],
    "w2":["m1", "m2"]}
Solution(N, guy_preferences, girl_preferences)

print()

# Expected results: betty chester, abigail andrew, caroline bill
N = 3
guy_preferences = {
    'andrew': ['caroline', 'abigail', 'betty'],
    'bill': ['caroline', 'betty', 'abigail'],
    'chester': ['betty', 'caroline', 'abigail'],
}

girl_preferences = {
    'abigail': ['andrew', 'bill', 'chester'],
    'betty': ['bill', 'andrew', 'chester'],
    'caroline': ['bill', 'chester', 'andrew']
}
Solution(N, guy_preferences, girl_preferences)