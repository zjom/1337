# https://leetcode.com/problems/equal-row-and-column-pairs

from collections import Counter
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_counts = Counter([",".join([str(el) for el in row]) for row in grid])

        res = 0
        for c in range(len(grid)):
            col = ",".join(str(row[c]) for row in grid)
            res += row_counts.get(col, 0)
        
        return res
