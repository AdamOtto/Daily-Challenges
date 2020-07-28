"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable. For example, '001' is not allowed.
"""

# Initial solution.  Exponential time O(n^2).
"""
def decode(message, index = 0, count = 0):
    
    if(index + 1 >= len(message)):
        return 1
    
    count = decode(message, index+1, count)
    if (message[index] == '1' and int(message[index + 1]) in range(0,9+1)):
        count += decode(message, index + 2, count)
    elif (message[index] == '2' and int(message[index + 1]) in range(0,6+1)):
        count += decode(message, index + 2, count)
    return count;
        
message = "1131"
print(decode(message))
"""

# Second solution.  O(n) time
def decode(message):
    count = [0] * (len(message) + 1)
    count[0] = 1
    count[1] = 1

    for i in range(2, len(message) + 1):
        if (int(message[i - 1]) > 0):  
            count[i] = count[i - 1]; 

        if (message[i - 2] == '1') or (message[i - 2] == '2' and int(message[i - 1]) in range(0,6+1)):
            count[i] += count[i-2]
    return count[len(message)]

message = "1131"
print(decode(message)) 