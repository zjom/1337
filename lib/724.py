# https://leetcode.com/problems/find-pivot-index
from itertools import accumulate

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_to_right = [0] + list(accumulate(nums))[:-1]
        right_to_left = list(accumulate(nums[::-1]))[::-1][1:]+[0]

        print(left_to_right,right_to_left)
        for i in range(len(nums)):
            if left_to_right[i] == right_to_left[i]:
                return i

        return -1

s = Solution()
assert s.pivotIndex(nums = [1,7,3,6,5,6]) == 3
assert s.pivotIndex(nums = [2,1,-1]) == 0

