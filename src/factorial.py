def getFactorial(n):
    if n < 2:
        return 1
    else:
         return n * getFactorial(n-1)

def getAdd(n):
    print(n)
    if n < 2:
        return 1
    else:
        return n + getAdd(n-1)