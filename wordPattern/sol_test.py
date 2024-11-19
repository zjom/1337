from sol import Solution
def test_one():
    pattern = "abba"
    s = "dog cat cat dog"
    assert Solution().wordPattern(pattern, s)
