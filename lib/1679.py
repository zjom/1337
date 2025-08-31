# https://leetcode.com/problems/max-number-of-k-sum-pairs

from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums_count = Counter(nums)
        n_ops = 0
        for n in nums:
            if nums_count.get(k-n, 0)>0 and nums_count.get(n,0)>0:
                if n == k-n and nums_count[n] < 2:
                    continue

                nums_count[n]-=1
                nums_count[k-n]-=1
                n_ops += 1

        return n_ops

s = Solution()
assert s.maxOperations([1,2,3,4], 5) == 2
assert s.maxOperations([3,1,3,4,3], 6) == 1
