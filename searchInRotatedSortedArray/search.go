// https://leetcode.com/problems/search-in-rotated-sorted-array/description/

package searchinrotatedsortedarray

func search(nums []int, target int) int {
	l, r := 0, len(nums)-1

	for l <= r {
		mid := (l + r) / 2
		if nums[mid] == target {
			return mid
		}

		if nums[l] == target {
			return l
		}

		if nums[r] == target {
			return r
		}

		if nums[mid] > nums[l] {
			if target > nums[mid] || target < nums[l] {
				l = mid + 1
			} else {
				r = mid - 1
			}
		} else {
			if nums[mid] > target || target > nums[r] {
				r = mid - 1
			} else {
				l = mid + 1
			}
		}
	}

	return -1
}
