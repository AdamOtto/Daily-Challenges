"""
Given a string of words delimited by spaces, reverse the words in string.
For example, given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""

def Solution(ar):
    return " ".join(list(reversed(ar.split(" "))))


# Return "here world hello"
print(Solution("hello world here"))

# Return "North the in man feared most the Shivers Caul said me likes Everyone"
print(Solution("Everyone likes me said Caul Shivers the most feared man in the North"))