from icecream import ic


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            if i+1 < len(s) and s[i] in ['1','2'] and s[i+1] in [str(n) for n in range(7)]:
                dp[i]+=dp[i+2]

        return dp[0]


s = Solution()
# 2 20 6
# 2 20 6
ic(s.numDecodings("2206"))
