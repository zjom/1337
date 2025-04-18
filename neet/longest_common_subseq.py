'''
https://neetcode.io/problems/longest-common-subsequence

Longest Common Subsequence
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

For example, "cat" is a subsequence of "crabt".
A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:

Input: text1 = "cat", text2 = "crabt" 

Output: 3 
Explanation: The longest common subsequence is "cat" which has a length of 3.


Example 2:

Input: text1 = "abcd", text2 = "abcd"

Output: 4


Example 3:

Input: text1 = "abcd", text2 = "efgh"

Output: 0


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.


Summarise
Given 2 strings, return the length of longest substr common to both

Observations
- 0 <= res <= min(len(text1), len(text2))
- ordering matters
- can only remove/ skip characters

At every step i,j we can
- take s[i], s[j]
- take s[i], skip t[j]
- skip s[i], take t[j]
- skip s[i], t[j]
'''


from functools import cache
from icecream import ic

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def aux(i:int,j:int)->int:
            if i == len(text1) or j==len(text2):
                return 0
            if text1[i]==text2[j]:
                return aux(i+1,j+1)+1
            return max(aux(i,j+1), aux(i+1,j))
        return aux(0,0)


s = Solution()
text1 = "cat"
text2 = "crabt" 
assert ic(s.longestCommonSubsequence(text1,text2)) == 3

text1 = "abcd"
text2 = "abcd"
assert ic(s.longestCommonSubsequence(text1,text2)) == 4

text1 = "abcd"
text2 = "efgh"
assert ic(s.longestCommonSubsequence(text1,text2)) == 0

text1="bsbininm"
text2="jmjkbkjkv"
assert ic(s.longestCommonSubsequence(text1,text2)) == 1 
