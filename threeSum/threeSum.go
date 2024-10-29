package threesum

import "slices"

func threeSum(nums []int) [][]int {
	retv := make([][]int, 0)
	if len(nums) < 3 {
		return retv
	}

	slices.Sort(nums)

	for i, n := range nums {
		if i > 0 && n == nums[i-1] {
			continue
		}

		l, r := i+1, len(nums)-1
		for l < r {
			sum := n + nums[l] + nums[r]
			if sum > 0 {
				r--
			}
			if sum < 0 {
				l++
			}
			if sum == 0 {
				retv = append(retv, []int{n, nums[l], nums[r]})
				l++
				for nums[l] == nums[l-1] && l < r {
					l++
				}
			}
		}
	}

	return retv
}
