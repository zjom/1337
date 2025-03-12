# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow,fast = nums[0],nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow
