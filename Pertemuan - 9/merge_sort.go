package main

import "fmt"

func main() {
	fmt.Println("Merge Sort")
	var arr = []int{32, 45, 67, 2, 7}
	var len int = len(arr)

	fmt.Printf("Given array: \n")
	fmt.Println(arr)
	fmt.Println("")

	MergeSort(&arr, 0, len -1)

	fmt.Println("Sorted array: ")
	fmt.Println(arr)
}

func merge(a *[]int, p int, q int, r int) {
	var arr []int = *a
	var b [5]int	
	var k int = 0
	var i int = p 
	var j int = q + 1

	for (i <= q && j <=r) {
		if arr[i] < arr[j] {
			b[k] = arr[i]
			k++; i++
		} else {
			b[k] = arr[j]
			k++; j++
		}
	}

	for (i <= q) {
		b[k] = arr[i]
		k++; i++
	}

	for (j <= r) {
		b[k] = arr[j]
		k++; j++
	}

	for i=r; i >= p; i-- {
		k--
		arr[i] = b[k]
	}
} 

// MergeSort for merge sort
func MergeSort(a *[]int, p int, r int) {
	if (p < r) {
		q := (p + r) / 2
		MergeSort(a, p, q)
		MergeSort(a, q+1, r)
		merge(a, p, q, r)
	}
}
