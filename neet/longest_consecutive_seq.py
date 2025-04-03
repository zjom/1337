# https://neetcode.io/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for n in nums:
            if n-1 in nums_set:
                continue
            acc = 1
            m = n
            while m in nums_set:
                longest = max(longest,acc)
                m += 1
                acc += 1
        return longest


s = Solution()
cases = [([2,20,4,10,3,4,5],4),([0,3,2,5,4,6,1,1],7)]
for inp,exp in cases:
    assert s.longestConsecutive(inp) == exp
