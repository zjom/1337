# https://neetcode.io/problems/house-robber

from icecream import ic

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <2:
            return nums[0]
        nums[1] = max(nums[0],nums[1])
        for i in range(2, len(nums)):
            nums[i] = max(nums[i-1],nums[i]+nums[i-2])

        return nums[-1]

nums=[5,1,2,10,6,2,7,9,3,1]
s = Solution()
ic(s.rob(nums))
