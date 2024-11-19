package maxmovesingrid

func maxMoves(grid [][]int) int {
	retv := 0
	m := len(grid)
	n := len(grid[0])
	visited := make([][]bool, m)
	for i := range m {
		visited[i] = make([]bool, n)
	}

	var dfs func(i, j, prev int)
	dfs = func(i, j, prev int) {
		if i < 0 || j < 0 || i > m-1 || j > n-1 || visited[i][j] || prev >= grid[i][j] {
			retv = max(retv, j-1)
			return
		}

		visited[i][j] = true
		dfs(i-1, j+1, grid[i][j])
		dfs(i, j+1, grid[i][j])
		dfs(i+1, j+1, grid[i][j])
		return
	}

	for i := 0; i < m; i++ {
		if !visited[i][0] {
			dfs(i, 0, 0)
		}
	}

	return retv
}
