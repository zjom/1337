# https://neetcode.io/problems/house-robber-ii

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def aux(ns: list[int])->int:
            one,two = 0,0
            for n in ns:
                tmp = max(one+n, two)
                one = two
                two = tmp
            return two
        return max(aux(nums[1:]), aux(nums[:-1]))

nums = [2,9,8,3,6]
s = Solution()
print(s.rob(nums))
