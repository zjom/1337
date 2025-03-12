# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        natural_sum = n*(n+1)/2
        return int(natural_sum - sum(nums))
