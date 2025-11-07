"""
Given a string and a set of characters, return the shortest substring containing all the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""
import sys

def Solution(string, pat):
    l1 = len(string)
    l2 = len(pat)
    
    if l1 < l2:
        return None
    
    hash_pat = [0] * 256
    hash_str = [0] * 256
    
    for i in range(l2):
        hash_pat[ord(pat[i])] += 1
    
    start = count = 0
    starti = -1
    min_len = sys.maxsize
    
    for i in range(l1):
        hash_str[ord(string[i])] += 1
        if hash_str[ord(string[i])] <= hash_pat[ord(string[i])]:
            count += 1
        
        if count == l2:
            while hash_str[ord(string[start])] > hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0:
                if hash_str[ord(string[start])] > hash_pat[ord(string[start])]:
                    hash_str[ord(string[start])] -= 1
                start += 1
            window = i - start + 1
            if min_len > window:
                min_len = window
                starti = start
        
    if starti == -1:
        return None
    return string[starti: starti + min_len]   


print(Solution("figehaeci", ['a', 'e', 'i']))