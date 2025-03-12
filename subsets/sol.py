# https://leetcode.com/problems/subsets/description/
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res:list[list[int]] = []
        tmp:list[int] = []
        
        n = len(nums)
        def aux(i:int):
            if i == n:
                res.append(tmp.copy())
                return

            aux(i+1)
            tmp.append(nums[i])
            aux(i+1)
            _=tmp.pop()

        aux(0)
        return res
            
        # return [[nums[j] for j in range(len(nums)) if i & (1 << j)] for i in range(1 << len(nums))]
