package rottingoranges

func orangesRotting(grid [][]int) int {
	q := make([][]int, 0)
	fresh := 0

	for i := range grid {
		for j := range grid[0] {
			v := grid[i][j]
			if v == 2 {
				q = append(q, []int{i, j})
			} else if v == 1 {
				fresh++
			}
		}
	}

	dirs := [][]int{{-1, 0}, {0, -1}, {1, 0}, {0, 1}}
	count := 0
	for len(q) != 0 && fresh > 0 {
		count++
		qlen := len(q)
		for i := 0; i < qlen; i++ {
			curr := q[0]
			q = q[1:]
			for _, dir := range dirs {
				x, y := dir[0]+curr[0], dir[1]+curr[1]
				if x < 0 || y < 0 ||
					x > len(grid)-1 || y > len(grid[0])-1 {
					continue
				}

				if grid[x][y] == 1 {
					grid[x][y] = 2
					fresh--
					q = append(q, []int{x, y})
				}
			}
		}
	}

	if fresh == 0 {
		return count
	}
	return -1
}
