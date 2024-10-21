from mmult1 import *

def test_brute_mult():
    A = [[1, 2], 
         [5, 3]]
    B = [[4, 2], 
         [1, 6]]
    assert brute_mult(A, B) == [[6, 14], [23, 28]]

def test_mat_add():
    A = [[1, 2], 
         [5, 3]]
    B = [[4, 2], 
         [1, 6]]
    assert mat_add(A, B) == [[5, 4], [6, 9]]

def test_mult_1x1():
    A = [[2]]
    B = [[3]]
    assert strassen_mult(A, B) == [[6]]

def test_gets_quadrant():
    A = [[1, 2, 3, 4], 
         [5, 3, 0, 8],
         [6, 2, 4, 1], 
         [7, 8, 1, 3]]
    assert get_quadrant(A, 0, 1) == [[3, 4], [0, 8]]

def test_assembles_matrix():
     upper_left = [[1, 2], 
                   [3, 4]]
     upper_right = [[5, 6], 
                    [7, 8]]
     lower_left = [[9, 10], 
                   [11, 12]]
     lower_right = [[13, 14], 
                    [15, 16]]
     assert assemble(upper_left, upper_right, lower_left, lower_right) == [[1, 2, 5, 6], [3, 4, 7, 8], [9, 10, 13, 14], [11, 12, 15, 16]]