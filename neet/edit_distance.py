# https://neetcode.io/problems/edit-distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        def aux(w1:str,w2:str)->int:
            if not w1 and not w2:
                return 0
            if not w2:
                return len(w1)
            if not w1:
                return len(w2)
            if w1[0] == w2[0]:
                return aux(w1[1:], w2[1:])
            return min(aux(w1[1:], w2), # del
                        aux(w2[0]+w1[1:],w2), # replace
                        aux(w2[0]+w1,w2)) +1 # insert
        return aux(word1,word2)

s = Solution()
word1 = "monkeys"
word2 = "money"
assert s.minDistance(word1,word2) == 2



word1 = "neatcdee"
word2 = "neetcode"
assert s.minDistance(word1,word2) == 3
