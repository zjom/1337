# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        seen: set[str] = set()
        left = 0
        right = 1
        while right < len(s) :
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            if res < right-left+1:
                res = right-left+1

        return res
