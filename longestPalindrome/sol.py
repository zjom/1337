from collections import defaultdict
# https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d:defaultdict[str,int] = defaultdict(int)
        for char in s:
            d[char] += 1

        res = 0
        flag = 0
        for value in d.values():
            if value % 2 == 0:
                res += value
            else:
                res += (value - 1)
                flag = 1
        if flag :
            return res + 1
        else:
            return res
