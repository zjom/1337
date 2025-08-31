# https://leetcode.com/problems/find-the-difference-of-two-arrays
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        

        return [[n for n in nums1_set if n not in nums2_set], [n for n in nums2_set if n not in nums1_set]]
