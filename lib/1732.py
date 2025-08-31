# https://leetcode.com/problems/find-the-highest-altitude

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        max_altitude = 0
        cur_altitude = 0
        for delta in gain:
            cur_altitude += delta
            max_altitude = max(cur_altitude, max_altitude)

        return max_altitude
