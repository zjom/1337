# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            area = width * min(height[left], height[right])
            max_area = max(max_area, area)
 
            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
