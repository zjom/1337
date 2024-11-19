# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150

import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = math.inf
        left = 0
        cur_sum = 0

        for right in range(len(nums)):
            cur_sum += nums[right]

            while cur_sum >= target:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                cur_sum -= nums[left]
                left += 1
        
        return min_len if not math.isinf(min_len) else 0

