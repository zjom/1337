// https://leetcode.com/problems/insert-interval

package insertinterval

func insert(intervals [][]int, newIntv []int) [][]int {
	retv := make([][]int, 0)

	idx := 0

	// Add all intervals before the new interval (non-overlapping)
	for idx < len(intervals) && end(intervals[idx]) < start(newIntv) {
		retv = append(retv, intervals[idx])
		idx++
	}

	// Merge overlapping intervals with the new interval
	for idx < len(intervals) && start(intervals[idx]) <= end(newIntv) {
		newIntv[0] = min(start(newIntv), start(intervals[idx]))
		newIntv[1] = max(end(newIntv), end(intervals[idx]))
		idx++
	}

	// Add the merged new interval
	retv = append(retv, newIntv)

	// Add all intervals after the new interval (non-overlapping)
	for idx < len(intervals) {
		retv = append(retv, intervals[idx])
		idx++
	}

	return retv
}

func between(a, i, j int) bool {
	return i <= a && a <= j
}

func start(intv []int) int {
	return intv[0]
}

func end(intv []int) int {
	return intv[1]
}
