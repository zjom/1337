package maximumsubarray

func maxSubArray(nums []int) int {
	maxSum := nums[0]
	currSum := 0

	for _, n := range nums {
		if currSum < 0 {
			currSum = 0
		}

		currSum = currSum + n
		maxSum = max(maxSum, currSum)
	}

	return maxSum
}
