# https://leetcode.com/problems/is-subsequence/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_pt, t_pt = 0,0
        while s_pt < len(s) and t_pt < len(t):
            s_c = s[s_pt]
            while t_pt < len(t) and t[t_pt] != s_c:
                t_pt += 1
            s_pt += 1
            t_pt += 1

        return s_pt == len(s) and t_pt <= len(t)
