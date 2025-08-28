# https://leetcode.com/problems/move-zeroes
from collections import deque

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        queue:deque[int] = deque()
        for i in range(len(nums)):
            if nums[i] == 0:
                queue.append(i)

            if nums[i] != 0 and queue:
                idx = queue.popleft()
                nums[idx] = nums[i]
                nums[i] = 0
                queue.append(i)
