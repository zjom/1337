# https://neetcode.io/problems/coin-change

class Solution:
    def coinChange(self,coins:list[int], amount:int)->int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a],dp[a-c]+1)
        return dp[amount] if dp[amount] != amount+1 else -1


s = Solution()

coins = [1,5,10]
amount = 12
assert s.coinChange(coins, amount) == 3

coins = [2]
amount = 3
assert s.coinChange(coins, amount) == -1

coins = [1]
amount = 0
assert s.coinChange(coins, amount) == 0
