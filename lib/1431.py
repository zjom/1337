# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maximum_candies = max(candies)
        return [c+extraCandies >= maximum_candies for c in candies]
