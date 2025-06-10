"""
We say a number is sparse if there are no adjacent ones in its binary representation.
For example, 21 (10101) is sparse, but 22 (10110) is not.
For a given input N, find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.
"""
def Solution(ar):
    temp = number_to_bit_array(ar)
    for i in reversed(range(len(temp) - 1)):
        if temp[i] == 1 and temp[i + 1] == 1:
            if i != 0:
                temp[i - 1] = 1
                for j in range(i, len(temp)):
                    temp[j] = 0
            else:
                temp = [0 for _ in temp]
                temp.insert(0,1)
    
    return list_to_binary(temp)
    
def number_to_bit_array(number):
    binary_string = bin(number)[2:]
    bit_array = [int(bit) for bit in binary_string]
    return bit_array

def list_to_binary(binary_list):
    binary_string = "".join(map(str, binary_list))
    decimal_value = int(binary_string, 2)
    return decimal_value

# Return 32
print(Solution(22))
# Return 21
print(Solution(21))
# Return 128
print(Solution(100))
# Return 64
print(Solution(50))