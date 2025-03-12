# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0]*26
        a = ord('a')
        for c in ransomNote:
            count[ord(c)-a] += 1
        
        for c in magazine:
            count[ord(c)-a] -= 1
            if count[ord(c)-a] < 0:
                return False
        
        return True
