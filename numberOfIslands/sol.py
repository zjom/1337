# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        def dfs(row:int,col:int):
            if row<0 or col<0 or row>num_rows-1 or col>num_cols-1 or grid[row][col]!='1':
                return
            grid[row][col]='0'
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)

        count = 0
        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row,col)

        return count
