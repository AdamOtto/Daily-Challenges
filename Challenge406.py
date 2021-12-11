"""
You are presented with an array representing a
Boolean expression. The elements are of two kinds:

T and F, representing the values True and False.
&, |, and ^, representing the bitwise operators for AND, OR, and XOR.
Determine the number of ways to group the array elements
using parentheses so that the entire expression evaluates to True.

For example, suppose the input is ['F', '|', 'T', '&', 'T'].
In this case, there are two acceptable groupings:
(F | T) & T and F | (T & T).
So you should return 2

Note:
Help from
https://www.geeksforgeeks.org/boolean-parenthesization-problem-dp-37/
"""


def Solution(ar):
    symbols = ""
    operators = ""
    
    for a in ar:
        if a == 'T' or a == 'F':
            symbols += a
        else:
            operators += a
    
    n = len(symbols)
    F = [[0 for i in range(n + 1)] for i in range(n + 1)]
    T = [[0 for i in range(n + 1)] for i in range(n + 1)]
    
    for i in range(n):
        if symbols[i] == 'F':
            F[i][i] = 1
        else:
            F[i][i] = 0
        
        if symbols[i] == 'T':
            T[i][i] = 1
        else:
            T[i][i] = 0 

    for gap in range(1, n):
        i = 0
        for j in range(gap, n):
            T[i][j] = F[i][j] = 0
            for g in range(gap):
                k = i + g
                
                tik = T[i][k] + F[i][k]
                tkj = T[k + 1][j] + F[k + 1][j]
                
                if operators[k] == '&':
                    T[i][j] += T[i][k] * T[k + 1][j]
                    F[i][j] += (tik * tkj - T[i][k] * T[k + 1][j])
                if operators[k] == '|':
                    F[i][j] += F[i][k] * F[k + 1][j]
                    T[i][j] += (tik * tkj - F[i][k] * F[k + 1][j])
                if operators[k] == '^':
                    T[i][j] += (F[i][k] * T[k + 1][j] + T[i][k] * F[k + 1][j])
                    F[i][j] += (T[i][k] * T[k + 1][j] + F[i][k] * F[k + 1][j]) 
            i += 1
    return T[0][n - 1]

# Return 2
in1 = ['F', '|', 'T', '&', 'T']
print(Solution(in1))

# Return 4
in1 = ['T', '|', 'T', '&', 'F', '^', 'T']
print(Solution(in1))

# Return 0
in1 = ['T', '&', 'F', '&', 'F', '^', 'T', '&', 'F']
print(Solution(in1))