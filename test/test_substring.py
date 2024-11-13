from substring import Solution

def test_ans1():
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3

def test_ans2():
     s = Solution()
     assert s.lengthOfLongestSubstring(" ") == 1

def test_ans3():
     s = Solution()
     assert s.lengthOfLongestSubstring("au") == 2
def test_ans4():
     s = Solution()
     assert s.lengthOfLongestSubstring("avavbd") == 4
def test_ans5():
     s = Solution()
     assert s.lengthOfLongestSubstring("abba") == 2
def test_ans6():
     s = Solution()
     assert s.lengthOfLongestSubstring("dvdf") == 3