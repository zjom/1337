package permutations

func slice(s []int, i int) []int {
	retv := make([]int, len(s)-1)
	copy(retv, s[:i])
	copy(retv[i:], s[i+1:])
	return retv
}

func permutations(nums []int) [][]int {
	if len(nums) == 0 {
		return nil
	}
	if len(nums) == 1 {
		return [][]int{nums}
	}

	res := make([][]int, 0)

	for i := range nums {
		// Get the current element
		current := nums[i]
		// Slice the rest of the array without the current element
		remaining := slice(nums, i)
		// Get permutations of the remaining elements
		for _, perm := range permutations(remaining) {
			// Prepend the current element to each permutation
			res = append(res, append([]int{current}, perm...))
		}
	}

	return res
}
