a = [2,4,6]
b = [6,4,8]
# sum(x*y for x, y in zip(a,b))

tot = 0
for i in range(len(a)):
    tot += sum(a[i] * b[i])


    
def mat_mult(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):  #Row in result
        for j in range(n):  #Column in result
            for k in range(n):  #Element in dot product
                result[i][j] += A[i][k] * B[k][j]
    return result

