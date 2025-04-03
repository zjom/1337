# https://neetcode.io/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        if len(s) == 2 and s[0] == s[1]:
            return s

        maximum = 0
        res_l = 0
        res_r = 0
        # odd len palindrome
        for i in range(len(s)):
            left,right = i-1,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1

            if  right-left-1 > maximum:
                maximum = right-left-1
                res_l = left+1
                res_r = right-1

        # even len palindrome
        for i in range(len(s)):
            if s[i] != s[i-1]:
                continue
            left,right = i-2,i+1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left-=1
                right+=1

            if  right-left-1 > maximum:
                maximum = right-left-1
                res_l = left+1
                res_r = right-1

        return s[res_l:res_r+1]

sol = Solution()
s = "bb"
print(sol.longestPalindrome(s))
# s = "abbc"
# print(sol.longestPalindrome(s))
# s = "ababd"
# print(sol.longestPalindrome(s))
# s = "racecar"
# print(sol.longestPalindrome(s))
# s = "raceacar"
# print(sol.longestPalindrome(s))
