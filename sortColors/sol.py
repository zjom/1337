# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(arr:list[int], i:int,j:int)->None:
            arr[i], arr[j] = arr[j], arr[i]

        low,high = 0,len(nums)-1
        i = 0
        while i <= high:
            if nums[i] == 0:
                swap(nums, low, i)
                low += 1
                i += 1
            elif nums[i] == 2:
                swap(nums, i, high)
                high -= 1
            else:
                i += 1
