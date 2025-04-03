# https://neetcode.io/problems/single-number

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        x = nums[0]
        for n in nums[1:]:
            x ^= n
        return x

s = Solution()
cases = [([3,2,3], 2), ([7,6,6,7,8], 8)]
for inp,exp in cases:
    assert s.singleNumber(inp) == exp
