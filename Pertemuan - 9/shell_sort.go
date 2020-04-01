package main

import "fmt"

func main() {
	fmt.Println("Shell Sort")
	var arr = []int{12, 34, 54, 2, 3}
	var n int = len(arr)

	fmt.Println("Before")
	fmt.Println(arr)
	fmt.Println("")
	ShellSort(&arr, n)

	fmt.Println("After")
	fmt.Println(arr)
}

// ShellSort for shell sort
func ShellSort(arr *[]int, n int) {
	tempArray := *arr
	for gap := n / 2; gap > 0; gap /= 2 {
		for i := gap; i < n; i++ {
			temp := tempArray[i]
			var j int
			for j = i; j >= gap && tempArray[j-gap] > temp; j -= gap {
				tempArray[j] = tempArray[j-gap]
			}
			tempArray[j] = temp
		}
	}
	*arr = tempArray
}
