# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0]*26
        for c in ransomNote:
            count[ord(c)] += 1
        
        for c in magazine:
            count[ord(c)] -= 1
        
        for c in count:
            if c > 0:
                return False
        
        return True
