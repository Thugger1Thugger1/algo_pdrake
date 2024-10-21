def intconvert(n):
    ans = bin(n)
    
print(intconvert(5))



def binary(n):
    if n>=1:
        return binary(n // 2)
        print(n % 2)

def dec2bin(n):
    if n < 0:
        return 'Must be a positive integer'
    elif n == 0:
        return '0'
    else:
        print(n%2)
        return dec2bin(n//2) + str(n%2)
        

class BitVector:
    def __init__(self, bits = 0) -> None:
        self.bits = bits

    def get(self, i):
        return (self.bits >> i) & 1

    def set(self, i, b):
        self.bits = (self.bits & ~(1 << i)) | (b << i)
    
    def union(self, other):
        return BitVector(self.bits | other.bits)

    def __repr__(self):
        return str(self)
    
    def __str__(self):
        for number in sys.getlength:
            return f'<{self.get(1)}'