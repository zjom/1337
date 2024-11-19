# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        i = 0
        for c in t:
            if c == s[i]:
                i += 1
            if i == len(s):
                return True

        return False
