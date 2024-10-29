// https://leetcode.com/problems/coin-change/
package coinchange

func coinChange(coins []int, amount int) int {
	dp := make([]int, amount+1)
	for i := range dp {
		dp[i] = amount + 1 // not found
	}
	dp[0] = 0 // base case

	for _, c := range coins {
		for a := c; a <= amount; a++ {
			if (a - c) >= 0 {
				dp[a] = min(dp[a], 1+dp[a-c])
			}
		}
	}

	// combination not found
	if dp[amount] > amount {
		return -1
	}

	return dp[amount]
}
