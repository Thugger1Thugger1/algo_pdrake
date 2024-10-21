import string
class HorspoolStringMatcher():
    def __init__(self, pattern):
        self.pattern = pattern
        self.T = {}
        for i in range(len(pattern) - 1):
            self.T[pattern[i]] = len(pattern) - 1 - i
        
    
    def _get_shift(self, char):
        return self.T.get(char, len(self.pattern))

#'john' 
    def _compare(self, a, b, lenth):
        i = lenth - 1
        while i >= 0 and a[i] == b[i]:
            i -= 1
        return i == -1


    def match(self, text):
        skip = 0
        patternLen = len(self.pattern)
        textLen = len(text)
        while textLen - skip >= patternLen:
            if self._compare(text[skip:skip + patternLen], self.pattern, patternLen):
                return skip  
            skip += self._get_shift(text[skip + patternLen - 1])

        return -1
