"""
https://neetcode.io/problems/longest-repeating-substring-with-replacement

Longest Repeating Character Replacement

You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4

Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1

Output: 5

Constraints:

    1 <= s.length <= 1000
    0 <= k <= s.length



k = 1
AAABABB
---_-
   _-__
    --

k = 2
AAABABB
---_-_
   ____

longest consecutive sequence with at most k anomalies
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count:dict[str,int] = {}
        res = 0
        
        maxf = 0
        left = 0
        for right in range(len(s)):
            count[s[right]] = 1+count.get(s[right],0)
            maxf = max(maxf, count[s[right]])

            while right-left+1 - maxf > k:
                count[s[left]]-=1
                left += 1
                maxf = max(maxf, count[s[left]])
            res = max(res, right-left+1)
        return res

s = Solution()
assert 5 == s.characterReplacement("AAABABB", 1)
assert 4 == s.characterReplacement("XYYX", 2)
