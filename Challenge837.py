"""
Create a basic sentence checker that takes in a stream of characters
and determines whether they form valid sentences.
If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

1. The sentence must start with a capital letter, followed by a lowercase letter or a space.
2. All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
3. There must be a single space between each word.
4. The sentence must end with a terminal mark immediately following a word.
"""
def Solution(ar):
    #1. Check capital at beginning.
    if not Rule1Checker(ar[0]):
        return False

    #2. All other characters must be lowercase.
    if not Rule2Checker(ar[1:]):
        return False

    #3. Single space between words.
    t = ar.split(" ")
    if not Rule3Checker(t):
        return False

    #4. Check last word and period.
    if not Rule4Checker(t[len(t) - 1]):
        return False

    return True


def Rule1Checker(ar):
    #print(str(ord("A")))
    #print(str(ord("Z")))
    if ord("A") <= ord(ar) and ord(ar) <= ord("Z"):
        return True
    return False

def Rule2Checker(ar):
    for c in ar:
        #print( str(ord("a")) + " < " + str(c) + "(" + str(ord(c)) + ")" + " < " + str(ord("z")) )
        if ord("a") > ord(c) or ord(c) > ord("z"):
            if (ord(c) != ord(",") and ord(c) != ord(" ") and ord(c) != ord(";") and ord(c) != ord(":") and
                    ord(c) != ord(".") and ord(c) != ord("?") and ord(c) != ord("!")):
                return False
    return True

def Rule3Checker(ar):
    hold = []
    for word in ar:
        if "," in word:
            hold.append((word, ","))
        if ":" in word:
            hold.append((word, ":"))
        if ";" in word:
            hold.append((word, ";"))
        if "." in word:
            hold.append((word, "."))
        if "?" in word:
            hold.append((word, "?"))
        if "!" in word:
            hold.append((word, "!"))
    retVal = True
    for i in hold:
        if not Rule3CheckerHelper(i[0], i[1]):
            retVal = False
    return retVal

def Rule3CheckerHelper(ar, symbol):
    i = ar.find(symbol)
    if i == len(ar) - 1:
        return True
    return False

def Rule4Checker(ar):
    l = len(ar)
    if ar[l - 1] != ".":
        return False
    return Rule4CheckerHelper(ar[:l -1])

def Rule4CheckerHelper(ar):
    if len(ar) == 0:
        return False
    retVal = True
    for letter in ar:
        if ord("a") > ord(letter) or ord(letter) > ord("z"):
            retVal = False
    return retVal

# Return True
in1 = "This is a successful test."
print(Solution(in1))

# Return False
in1 = "Thisisanunsuccessfultest."
print(Solution(in1))

# Return False
in1 = "this is an unsuccessful test."
print(Solution(in1))

# Return False
in1 = "This iS an unsuccessfUl test."
print(Solution(in1))

# Return False
in1 = "This,is an unsuccessful test."
print(Solution(in1))

# Return False
in1 = "This is an unsuccessful test ."
print(Solution(in1))