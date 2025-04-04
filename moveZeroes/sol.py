# https://leetcode.com/problems/move-zeroes/description/
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums:list[int],i:int,j:int):
            nums[i],nums[j] = nums[j],nums[i]

        front = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                swap(nums,i,front)
                front += 1
