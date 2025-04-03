# https://neetcode.io/problems/min-cost-climbing-stairs
from icecream import ic
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        for i in range(len(cost)-3,-1,-1):
            cost[i] += min(cost[i+1],cost[i+2])

        return min(cost[0],cost[1])

s = Solution()
cost = [1,2,3]
ic(s.minCostClimbingStairs(cost))
