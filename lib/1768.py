# https://leetcode.com/problems/merge-strings-alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        def merge(s1:str,s2:str)->str:
            if not s1:
                return s2
            if not s2:
                return s1

            return s1[0]+s2[0]+merge(s1[1:], s2[1:])

        return merge(word1,word2)
