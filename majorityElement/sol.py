# https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c = 0
        m = 0

        for n in nums:
            if c == 0:
                c = 1
                m = n
            elif m == n:
                c += 1
            else:
                c -= 1

        return m
