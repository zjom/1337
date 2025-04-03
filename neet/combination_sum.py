# https://neetcode.io/problems/combination-target-sum
from icecream import ic

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res:list[list[int]] = []
        nums.sort()

        def dfs(i:int, cur:list[int], total:int):
            if total == target:
                res.append(cur.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                cur.pop()
        
        dfs(0, [], 0)
        return res


s = Solution()
nums = [2,5,6,9] 
target = 9
assert sorted([[2,2,5],[9]]) == ic(sorted(s.combinationSum(nums,target)))


assert sorted(s.combinationSum(nums,target)) == sorted([[2,2,5],[9]])

nums = [3,4,5]
target = 16
assert sorted(s.combinationSum(nums,target))==sorted([[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]])

nums = [3]
target = 5
assert s.combinationSum(nums,target)==[]
