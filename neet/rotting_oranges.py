# https://neetcode.io/problems/rotting-fruit

from collections import deque

from icecream import ic
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]

        batch:list[tuple[int,int]] = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    batch.append((i,j))

        q:deque[list[tuple[int,int]]] = deque([batch])

        time = 0
        while q:
            batch:list[tuple[int,int]] = []
            for x,y in q.popleft():
                for dx,dy in dirs:
                    i,j = x+dx,y+dy
                    if i<0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j]!=1:
                        continue
                    grid[i][j] = 2
                    batch.append((i,j))
            if batch:
                time+=1
                q.append(batch)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return time

if __name__ == "__main__":
    s = Solution()
    grid=[[1,1,0],[0,1,1],[0,1,2]]
    ic(s.orangesRotting(grid))
