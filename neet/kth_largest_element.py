# https://neetcode.io/problems/kth-largest-element-in-an-array

from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        ns = [-1*n for n in nums]
        heapify(ns)
        prev = 1001
        while k>=1:
            x = heappop(ns)

            k-=1
            prev = x

        return prev*-1

s = Solution()
nums = [2,3,1,5,4]
k = 2

s.findKthLargest(nums,k)
