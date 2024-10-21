
def find(string, val):
    for i in range(len(string)):
        for j in range(len(val)):
            if i + j >= len(string) or string[i+j] != val[j]:
                break
            if j == len(val) - 1:
                return i
    return -1