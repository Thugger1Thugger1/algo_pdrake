def brute_mult(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def mat_add(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]
    return result

def strassen_mult(A, B):
    if len(A) == 1:
        return brute_mult(A, B)

def get_quadrant(A, vhalf, hhalf):
    """
    :param A: the matrix we're getting a quadrant from
    :param vhalf: vertical half -- 0 for the top half, 1 for the bottom
    :param hhalf: horizontal half -- 0 for left half, 1 for the right
    :return: the indicated submatrix
    
    """
    mid = len(A)//2
    return [row[mid * hhalf:mid * (hhalf + 1)] for row in A[mid * vhalf:mid * (vhalf + 1)]]

    # if vhalf and hhalf:
    #     return [row[mid:] for row in A[mid:]]

    # if not vhalf and hhalf:
    #     return [row[mid:] for row in A[:mid]]
    
    # if vhalf and not hhalf:
    #     return [row[:mid] for row in A[mid:]]

    # if not vhalf and not hhalf:
    #     return [row[:mid:] for row in A[:mid:]]

def assemble(upper_left, upper_right, lower_left, lower_right):
    """"
    upper_left = [[1, 2], 
                   [3, 4]]
     upper_right = [[5, 6], 
                    [7, 8]]
     lower_left = [[9, 10], 
                   [11, 12]]
     lower_right = [[13, 14], 
                    [15, 16]]
    """

    n = len(upper_left)
    result = [[0] * n for _ in range(n * 2)]
    for i in range(n):
        result[i].append(upper_left[i])
            