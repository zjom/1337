# https://leetcode.com/problems/pacific-atlantic-water-flow/
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows,cols = len(heights), len(heights[0])

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        def neighbours(row:int,col:int) -> list[list[int]]:
            nei:list[list[int]] = []
            for x,y in dirs:
                next_x,next_y = row+x, col+y
                if next_x > rows-1 or next_x < 0 or next_y > cols -1 or next_y < 0:
                    continue
                nei.append([next_x,next_y])
            return nei

        # starting from pacific
        pacific = set([(0,c) for c in range(cols)])
        pacific.update([(r,0) for r in range(rows)])
        queue = deque[tuple[int,int]]()
        queue.extend(pacific)
        while queue:
            row,col = queue.popleft()
            nei = [(r,c) for r,c in neighbours(row,col) if heights[r][c] >= heights[row][col] and (r,c) not in pacific]
            queue.extend(nei)
            pacific.update(nei)

        # starting from atlantic
        atlantic = set([(rows-1,c) for c in range(cols)])
        atlantic.update([(r,cols-1) for r in range(rows)])
        queue.extend(atlantic)
        while queue:
            row,col = queue.popleft()
            nei = [(r,c) for r,c in neighbours(row,col) if heights[r][c] >= heights[row][col] and (r,c) not in atlantic]
            queue.extend(nei)
            atlantic.update(nei)

        # intersection of both sets
        return [[r,c] for r,c in atlantic if (r,c) in pacific]
