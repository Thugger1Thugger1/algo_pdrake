# class SuperClass:
#     def __init__(self):
#         self.foo = "spam"
    
#     def print_foo(self):
#         return self.foo

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        indices = {}
        #urr = {}
        length = 0
        longlen = 0
        start = 0

        for i in range(len(s)):

            if s[i] in indices and indices[s[i]] >= start: # Move the start to the right of the last occurrence of s[i]:
                

                start = indices[s[i]] + 1
            
            indices[s[i]] = i
                
                #indices = {s[i]:i}
                #del dict[s[i]] 
                

            longlen = max(longlen, i - start + 1)
        
        return longlen
            
            
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
#abba
#dvdf
        