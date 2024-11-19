# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                x = 1
                while num + x in num_set:
                    x += 1
                longest = max(longest, x)
        return longest
