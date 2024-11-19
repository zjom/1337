# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left,right = 0, len(nums)-1
        while left < right:
            curr = nums[left]+nums[right]
            if curr == target:
                return [left+1, right+1]
            elif curr < target:
                left += 1
                continue
            else:
                right -= 1

        return []
