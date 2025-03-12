# https://leetcode.com/problems/squares-of-a-sorted-array/description/
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0]*n
        left,right,i = 0, n-1, n-1

        while left <= right:
            leftVal = nums[left]*nums[left]
            rightVal = nums[right]*nums[right]

            if leftVal >= rightVal:
                res[i] = leftVal
                left += 1
            else:
                res[i] = rightVal
                right -= 1
            
            i -= 1

        return res
