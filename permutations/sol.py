# https://leetcode.com/problems/permutations/description/
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def aux(nums: list[int]) -> list[list[int]]:
            if len(nums) == 1:
                return [nums]

            result: list[list[int]] = []
            for i,curr in enumerate(nums):
                rest = nums[:i]
                rest.extend(nums[i+1:])
                for perms in aux(rest):
                    res = [curr]
                    res.extend(perms)
                    result.append(res)
            return result

        return aux(nums)
