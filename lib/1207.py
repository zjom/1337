# https://leetcode.com/problems/unique-number-of-occurrences/class Solution:

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = Counter(arr)

        occurrences:set[int] = set()
        for v in counts.values():
            if v in occurrences:
                return False
            occurrences.add(v)
        return True
