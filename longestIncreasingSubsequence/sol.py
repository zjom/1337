# https://leetcode.com/problems/longest-increasing-subsequence/description/
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res: list[int] = []

        def bs(res: list[int], n:int):
            left = 0
            right = len(res) -1

            while left <= right:
                mid = left + (right-left)//2
                if res[mid] == n:
                    return mid
                elif res[mid] > n:
                    right = mid -1
                else:
                    left = mid + 1

            return left

        for n in nums:
            if not res or res[-1] < n:
                res.append(n)
            else:
                idx = bs(res,n)
                res[idx] = n

        return len(res)

