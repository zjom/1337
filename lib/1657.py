# https://leetcode.com/problems/determine-if-two-strings-are-close

from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s1_count = Counter(word1)
        s2_count = Counter(word2)

        return set(s1_count.keys()) == set(s2_count.keys()) and sorted(s1_count.values()) == sorted(s2_count.values())

