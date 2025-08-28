class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        minimums = [n for n in nums]
        min_so_far = 2**31-1 
        for i,n in enumerate(nums):
            if n < min_so_far:
                min_so_far = n
            minimums[i] = min_so_far

        max_so_far = 2**31-1
        maximums = [n for n in nums]
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > max_so_far:
                max_so_far = nums[i]
            maximums[i] = max_so_far

        for i in range(1,len(nums)-1):
            if nums[i] > minimums[i] and nums[i] < maximums[i]:
                return True

        return False
