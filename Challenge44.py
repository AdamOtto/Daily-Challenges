'''
We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.
'''

def Solution(in1):
    count = 0
    for i in range(0, len(in1)):
        if i != len(in1):
            for j in range(i + 1, len(in1)):
                if in1[i] > in1[j]:
                    count += 1
                    
    print(count)

#in1 = [2, 4, 1, 3, 5]
in1 = [5,4,3,2,1]
Solution(in1)
