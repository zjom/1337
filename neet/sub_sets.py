# https://neetcode.io/problems/subsets

from icecream import ic

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res:list[list[int]]=[]
        subset:list[int]=[]

        def dfs(i:int):
            if i >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

s = Solution()
assert [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]  == ic(s.subsets([1,2,3]))
