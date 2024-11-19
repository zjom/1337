# https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        m = defaultdict[str,int](int)
        for c in s:
            m[c] += 1
        
        for c in t:
            m[c] -= 1
        
        for v in m.values():
            if v != 0:
                return False
        return True
