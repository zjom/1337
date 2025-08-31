# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, arr: list[int]) -> int:
        left,right = 0, len(arr)-1
        max_water = -1

        while left < right:
            max_water = max(max_water, min(arr[left], arr[right]) * (right-left))
            if arr[right] >= arr[left]:
                left+=1
            else:
                right -=1

        return max_water
