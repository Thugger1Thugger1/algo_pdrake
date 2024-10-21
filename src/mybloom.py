class BloomFilter():
    pass

    def __init__(self) -> None:
        self.bits = 0

    def __hash__(self, key):
        h = abs(hash(key)) % (2 ** 32)
        lower = h % (2 ** 16)
        upper = (h >> 16) % (2 ** 16)
        return [lower, upper]

    def add(self):
        for h in self.__hash__:
            pass
            


    def might_contain(self):
        pass


    def _true_bits(self):
        pass

