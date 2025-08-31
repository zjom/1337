# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
from icecream import ic

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i','o','u'}
        cur_count = len([c for c in s[:k] if c in vowels])
        max_count = cur_count

        for i in range(len(s)-k):
            cur_count -= 1 if s[i] in vowels else 0
            cur_count += 1 if s[i+k] in vowels else 0
            max_count = max(max_count,cur_count)

        return max_count

s = Solution()
assert ic(s.maxVowels( "abciiidef",  3)) == 3
assert ic(s.maxVowels(s = "aeiou", k = 2)) == 2
assert ic(s.maxVowels(s = "leetcode", k = 3)) == 2


