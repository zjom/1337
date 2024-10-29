package matrix

import "math"

func push(q [][]int, v []int) [][]int {
	return append(q, v)
}

func shift(q [][]int) ([][]int, int, int, int) {
	v := q[0]
	return q[1:], v[0], v[1], v[2]
}

func updateMatrix(mat [][]int) [][]int {
	// store x,y,dist from zero
	q := [][]int{}
	for i := range mat {
		for j := range mat[0] {
			if mat[i][j] != 0 {
				mat[i][j] = math.MaxInt
				continue
			}

			q = push(q, []int{i, j, 0})
		}
	}

	dirs := [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

	// bfs
	var (
		x    int
		y    int
		dist int
	)
	for len(q) != 0 {
		q, x, y, dist = shift(q)

		if mat[x][y] > dist {
			mat[x][y] = dist
		}

		for _, dir := range dirs {
			nextX, nextY, nextVal := x+dir[0], y+dir[1], dist+1
			if (nextX < 0 || nextX > len(mat)-1) || (nextY < 0 || nextY > len(mat[0])-1) {
				continue
			}

			if mat[nextX][nextY] == math.MaxInt {
				q = push(q, []int{nextX, nextY, nextVal})
			}
		}
	}

	return mat
}
