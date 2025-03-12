# https://leetcode.com/problems/daily-temperatures/description/
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack:list[list[int]] = [] # [value, idx]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                idx = stack.pop()[1]
                res[idx] = i - idx
            stack.append([t, i])
        
        return res
