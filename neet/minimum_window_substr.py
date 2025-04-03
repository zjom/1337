'''
https://neetcode.io/problems/minimum-window-with-characters

Given two strings s and t, return the shortest substring of s such that every character in t,
including duplicates, is present in the substring.
If such a substring does not exist, return an empty string "".
You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"
Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"
Example 3:

Input: s = "x", t = "xy"

Output: ""

Constraints:

1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
'''

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # REVIEW
        if len(s) < len(t):
            return ""

        t_count:Counter[str] = Counter(t)
        window:dict[str,int] = {}

        res,res_len = [-1,-1],2**31-1
        have,want=0,len(t_count)

        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0)+1
            if c in t_count and t_count[c] == window[c]:
                have+=1

            while have == want:
                if (right-left+1) < res_len:
                    res = [left,right]
                    res_len = right-left+1
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1
                left += 1
        left,right = res
        return s[left:right+1] if res_len != 2**31-1 else ""
