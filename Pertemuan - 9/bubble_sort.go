package main

import "fmt"

func main() {
	fmt.Println("Selection Sort")

	var arr = []int{46, 52, 21, 22, 11}

	fmt.Println("Before")
	fmt.Println(arr)
	fmt.Println("")
	BubbleSort(&arr)

	fmt.Println("After")
	fmt.Println(arr)
}

// BubbleSort for bubble sort
func BubbleSort(a *[]int) {
	var arr = *a
	var n int = len(arr)

	for i := 0; i < n; i++ {
		for j := n - 1; j > 0; j-- {
			if arr[j] < arr[j-1] {
				temp := arr[j-1]
				arr[j-1] = arr[j]
				arr[j] = temp
			}
		}
	}
}
