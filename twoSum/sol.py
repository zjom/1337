# https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150
#pyright:basic

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m:dict[int,int] = {}

        res = []
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in m:
                return [i,m[diff]]
            m[nums[i]] = i

        return res
