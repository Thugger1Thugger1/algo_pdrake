import random

def bubble_sort(ls, key = None):
    swaps = True

    if key == 'len':
        while swaps:
            swaps = False
            for i in range(len(ls) - 1):
                if len(ls[i]) > len(ls[i + 1]):
                    ls[i], ls[i + 1] = ls[i + 1], ls[i]
                    swaps = -1
                

    if key == 'lex':
        while swaps:
            swaps = False
            for i in range(len(ls) - 1):
                if ord(ls[i[0]]) > ord(ls[i + 1[0]]):
                    ls[i], ls[i + 1] = ls[i + 1], ls[i]
                    swaps = True
                

    else:
        while swaps:
            swaps = False
            for i in range(len(ls) - 1):
                if ls[i] > ls[i + 1]:
                    ls[i], ls[i + 1] = ls[i + 1], ls[i]
                    swaps = True
                
ls = [1,4,3,12,5,6,2,7,8,9]
bubble_sort(ls)
print(ls)
