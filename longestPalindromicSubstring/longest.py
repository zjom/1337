class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        res_l = 0
        res_r = 0

        for i in range(len(s)):
            # check odd
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > longest:
                    longest = right-left+1
                    res_l = left
                    res_r = right+1
                left -= 1
                right += 1

            # check even
            left, right = i, i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right-left+1 > longest:
                    longest = right-left+1
                    res_l = left
                    res_r = right+1
                left -= 1
                right += 1

        return s[res_l:res_r]
