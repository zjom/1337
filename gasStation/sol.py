# https://leetcode.com/problems/gas-station/description/

class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        fuelLeft, globalFuelLeft, start = 0,0,0

        for i in range(n):
            globalFuelLeft += gas[i] - cost[i]
            fuelLeft += gas[i] - cost[i]
            if fuelLeft < 0:
                start = i + 1
                fuelLeft = 0

        if globalFuelLeft < 0:
            return -1

        return start
