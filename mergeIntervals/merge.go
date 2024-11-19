// https://leetcode.com/problems/merge-intervals/description/
package mergeintervals

import "slices"

func shouldMerge(a, b []int) bool {
	if b[0] <= a[1] {
		return true
	}

	return false
}

func mergeTwo(a, b []int) []int {
	return []int{min(a[0], b[0]), max(a[1], b[1])}
}

func aux(ls [][]int, prev []int, acc [][]int) [][]int {
	if len(ls) == 0 {
		return append(acc, prev)
	}

	hd := ls[0]
	tl := ls[1:]

	if shouldMerge(prev, hd) {
		return aux(tl, mergeTwo(prev, hd), acc)
	}

	return aux(tl, hd, append(acc, prev))
}

func merge(intervals [][]int) [][]int {
	slices.SortFunc(intervals, func(a, b []int) int {
		if a[0] < b[0] {
			return -1
		}
		if a[0] == b[0] {
			return 0
		}
		return 1
	})
	hd := intervals[0]
	tl := intervals[1:]

	return aux(tl, hd, [][]int{})
}
