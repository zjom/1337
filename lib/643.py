# https://leetcode.com/problems/maximum-average-subarray-i
from icecream import ic

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = sum(nums[:k])
        maximum = cur_sum
        for i in range(len(nums)-k):
            cur_sum -= nums[i]
            cur_sum += nums[i+k]
            maximum = max(cur_sum, maximum)

        return maximum/k



s = Solution()
assert ic(s.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4)) == 12.75000
assert ic(s.findMaxAverage(nums = [0,1,1,3,3], k = 4)) == 2.00000

