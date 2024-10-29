package search

func binary(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for l <= r {
		if nums[l] == target {
			return l
		}

		if nums[r] == target {
			return r
		}

		mid := l + (r-l)/2
		if nums[mid] == target {
			return mid
		}

		if nums[mid] < target {
			l = mid + 1
			continue
		}

		if nums[mid] > target {
			r = mid - 1
			continue
		}
	}

	return -1
}
