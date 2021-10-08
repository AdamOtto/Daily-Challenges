"""
You are given a set of synonyms, such as (big, large) and (eat, consume).
Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

"He wants to eat food."
"He wants to consume food."
Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c):
consider the case of (coach, bus) and (coach, teacher).
"""

def Solution(synonyms, sen1, sen2):
    s1 = sen1.split(" ")
    s2 = sen2.split(" ")
    l = len(s1)
    if l != len(s2):
        return False
    
    for i in range(l):
        if s1[i] != s2[i]:
            if s1[i] not in synonyms or s2[i] not in synonyms:
                return False
    return True


in1 = ["eat", "consume"]
in2 = "He wants to eat food."
in3 = "He wants to consume food."
print(Solution(in1, in2, in3))

in1 = ["big", "large"]
in2 = "Whales are big"
in3 = "Whales are large"
print(Solution(in1, in2, in3))

in1 = ["big", "huge"]
in2 = "Whales are big"
in3 = "Whales are large"
print(Solution(in1, in2, in3))