// https://leetcode.com/problems/course-schedule/description/
package courseschedule

func canFinish(numCourses int, prerequisites [][]int) bool {
	// preM stores course and its prerequisites
	preM := make(map[int][]int)
	for i := 0; i < numCourses; i++ {
		preM[i] = make([]int, 0) // initialise the values of the map as empty slice
	}

	for _, preqs := range prerequisites {
		course, preq := preqs[0], preqs[1]
		preM[course] = append(preM[course], preq) // add prerequisites to map
	}

	// seen keeps track of which nodes we have visited on a dfs basis
	// if we see a repeat node in a single dfs, we have a loop
	seen := make(map[int]struct{})
	var dfs func(course int) bool
	dfs = func(course int) bool {
		if _, ok := seen[course]; ok {
			return false
		}
		if len(preM[course]) == 0 {
			return true
		}

		seen[course] = struct{}{}
		for _, pre := range preM[course] {
			if !dfs(pre) {
				return false
			}
		}

		delete(seen, course)
		preM[course] = make([]int, 0)

		return true
	}

	for course := 0; course < numCourses; course++ {
		if !dfs(course) {
			return false
		}
	}

	return true
}
