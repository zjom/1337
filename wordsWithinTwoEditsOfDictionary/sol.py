# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

class Solution:
    def twoEditWords(self, queries: list[str], dictionary: list[str]) -> list[str]:
        def within_two_edits(word1:str,word2:str)->bool:
            if len(word1)!=len(word2):
                return False
            diffs = sum([1 for a,b in zip(word1,word2) if a != b]) 
            return diffs <= 2

        result:list[str] = []

        for query in queries:
            for word in dictionary:
                if within_two_edits(query, word):
                    result.append(query)
                    break

        return result
