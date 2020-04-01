package main

import "fmt"

func main() {
	fmt.Println("Insertion Sort")

	var arr = []int{46, 52, 21, 22, 11, 13, 60, 80, 100, 1}

	fmt.Println("Before")
	fmt.Println(arr)
	fmt.Println("")
	InsertionSort(&arr)

	fmt.Println("After")
	fmt.Println(arr)
}

// InsertionSort for insertion sort
func InsertionSort(a *[]int) {
	var arr []int = *a
	var n int = len(arr)

	for i := 0; i < n; i++ {
		for j := i; j > 0; j-- {
			if arr[j] < arr[j-1] {
				temp := arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = temp
			}
		}
	}
}
