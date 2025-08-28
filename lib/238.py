# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        preceding = [1 for _ in range(len(nums))]
        for i in range(len(nums)-1):
            preceding[i+1] = nums[i] * preceding[i]
        post = [1 for _ in range(len(nums))]

        for i in range(len(nums)-1,0,-1):
            post[i-1] = nums[i] * post[i]

        return [preceding[i] * post[i] for i in range(len(preceding))]

