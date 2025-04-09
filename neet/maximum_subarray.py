# https://neetcode.io/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=max(nums[i], nums[i]+nums[i-1])
        return max(nums)


s = Solution()
nums = [2,-3,4,-2,2,1,-1,4]
assert s.maxSubArray(nums) == 8


nums = [-1]
assert s.maxSubArray(nums) == -1

nums=[-2,1,-3,4,-1,2,1,-5,4]
assert s.maxSubArray(nums) == 6
