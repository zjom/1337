# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
# pyright: basic

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        acc_s = {}
        acc_t = {}

        for i,c in enumerate(s):
            if (c in acc_s and acc_s[c] != t[i]):
                return False

            if (t[i] in acc_t and acc_t[t[i]] != c):
                return False
            acc_s[c] = t[i]
            acc_t[t[i]] = c

        return True
