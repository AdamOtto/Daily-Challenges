'''
A step word is formed by taking a given word,
adding a letter, and anagramming the result.
For example, starting with the word "APPLE", you can add
an "A" and anagram to get "APPEAL".

Given a dictionary of words and an input word,
create a function that returns all valid step words.
'''

def Solution(ar):
    d = {}
    
    retVal = set()
    
    l = len(ar)
    for i in range(l):
        for j in range(i + 1, l):
            result = None
            if len(ar[i]) <= len(ar[j]):
                result = CheckStepWord(ar[i], ar[j])
            else:
                result = CheckStepWord(ar[j], ar[i])
            
            if result:
                if len(ar[i]) <= len(ar[j]):
                    retVal.add( (ar[i], ar[j]) )
                else:
                    retVal.add( (ar[j], ar[i]) )
    return retVal

def CheckStepWord(w1, w2):
    if len(w1) == len(w2) + 1 or len(w2) == len(w1) + 1:
        d = {}
        for letter in w2:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] += 1
        
        for letter in w1:
            if letter in d:
                d[letter] -= 1

        count = 0
        for key, val in d.items():
            if val < 0:
                return False
            if val >= 1:
                count += val
        
        if count == 1:
            return True
    return False
            


in1 = ["APPLE", "APPEAL", "MICE", "MINCE", "GOAT", "TANGO"]
print(Solution(in1))

in1 = ["00100", "0101010", "010010", "10101", "100100", "111010"]
print(Solution(in1))