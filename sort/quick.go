package sort

func swap(arr []int, i, j int) {
	arr[j], arr[i] = arr[i], arr[j]
}

func partitition(arr []int, l, r int) int {
	pivot := arr[r]
	i := l - 1

	for j := l; j < r; j++ {
		if arr[j] < pivot {
			i++
			swap(arr, i, j)
		}
	}
	swap(arr, i+1, r)

	return i + 1
}

func quickSort(arr []int, l, r int) {
	if l < r {
		pi := partitition(arr, l, r)
		quickSort(arr, l, pi-1)
		quickSort(arr, pi+1, r)
	}
}
