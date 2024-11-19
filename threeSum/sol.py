# https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        retv:list[list[int]] = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1
            while left < right:
                leftVal = nums[left]
                rightVal = nums[right]
                sum = leftVal+rightVal+n
                if sum < 0:
                    left += 1
                    continue
                if sum > 0:
                    right -= 1
                    continue
                retv.append([n,leftVal,rightVal])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1

        return retv

