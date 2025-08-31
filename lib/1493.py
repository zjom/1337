# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        maximum = 0
        left,right = 0,0
        
        zero_found = False
        while right < len(nums):
            if nums[right] != 0:
                right += 1
                maximum = max(maximum, right-left-1)
                continue
            
            if zero_found:
                if nums[left] == 0:
                    zero_found = False
                left += 1
                continue
            
            zero_found = True
            right +=1
            maximum = max(maximum, right-left-1)
            
        return maximum
