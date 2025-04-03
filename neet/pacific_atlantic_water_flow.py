# Pacific Atlantic Water Flow
# https://neetcode.io/problems/pacific-atlantic-water-flow
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific:set[tuple[int,int]] = set()
        q:deque[tuple[int,int]] = deque()
        q.extend([(0,i) for i in range(num_cols)])
        q.extend([(i,0) for i in range(num_rows)])
        while q:
            i,j = q.popleft()
            if (i,j) in pacific:
                continue
            pacific.add((i,j))
            for x,y in dirs:
                r,c = i+x,y+j
                if (r<0 or c < 0
                    or r >= num_rows
                    or c >= num_cols
                    or heights[i][j] > heights[r][c]):
                    continue
                q.append((r,c))


        atlantic:set[tuple[int,int]] = set()
        q.extend([(num_rows-1,i) for i in range(num_cols)])
        q.extend([(i,num_cols-1) for i in range(num_rows)])
        while q:
            i,j = q.popleft()
            if (i,j) in atlantic:
                continue
            atlantic.add((i,j))
            for x,y in dirs:
                r,c = i+x,y+j
                if (r<0 or c < 0
                    or r >= num_rows
                    or c >= num_cols
                    or heights[i][j] > heights[r][c]):
                    continue
                q.append((r,c))


        return [[x,y] for x,y in atlantic if (x,y) in pacific]
