// https://leetcode.com/problems/k-closest-points-to-origin/

package kclosestpointstoorigin

import (
	"math"
	"slices"
)

func take[E any, S []E, T any](arr S, n int, f func(el E) T) []T {
	retv := make([]T, 0)

	for i := 0; i < n; i++ {
		retv = append(retv, f(arr[i]))
	}

	return retv
}

func fmap[E any, S []E, T any](arr S, f func(i int, el E) T) []T {
	retv := make([]T, 0)

	for i, el := range arr {
		retv = append(retv, f(i, el))
	}

	return retv
}

func distance(x, y int) float64 {
	return math.Sqrt(math.Pow(float64(x), 2) + math.Pow(float64(y), 2))
}

type distPoint struct {
	dist   float64
	points []int
}

func kClosest(points [][]int, k int) [][]int {
	distPoints := fmap(points, func(_ int, el []int) distPoint {
		return distPoint{
			dist:   distance(el[0], el[1]),
			points: el,
		}
	})

	slices.SortFunc(distPoints, func(a, b distPoint) int {
		if a.dist == b.dist {
			return 0
		} else if a.dist < b.dist {
			return -1
		} else {
			return 1
		}
	})

	return take(distPoints, k, func(el distPoint) []int {
		return el.points
	})
}
