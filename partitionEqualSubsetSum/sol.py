# https://leetcode.com/problems/partition-equal-subset-sum/description/
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        n = sum(nums)
        if n%2:
            return False

        target = n // 2
        dp = set([0])

        for i in range(len(nums)-1,-1,-1):
            nextDP = dp.copy()
            for t in dp:
                if (t+nums[i]) == target:
                    return True
                nextDP.add(t+nums[i])
            dp = nextDP

        return True if target in dp else False
