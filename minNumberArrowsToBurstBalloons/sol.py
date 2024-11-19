# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])

        count = 0
        i = 0
        while i < len(points):
            curr = points[i][1]
            while i < len(points)-1 and curr >= points[i+1][0]:
                i += 1
            count += 1
            i += 1

        return count
