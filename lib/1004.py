# https://leetcode.com/problems/max-consecutive-ones-iii

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        maximum = 0
        left,right = 0,0

        while right < len(nums):
            if nums[right] != 0:
                right +=1
                maximum = max(maximum, right-left)
                continue
            
            if k > 0:
                k -= 1
                right += 1
                maximum = max(maximum, right-left)
                continue
            
            if nums[left] == 0:
                k += 1
            left += 1

        return maximum
