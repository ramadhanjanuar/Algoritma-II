package main

import "fmt"

func main() {
	fmt.Println("Selection Sort")

	var arr = []int{46, 52, 21, 22, 11}
	var n int = len(arr)

	fmt.Println("Before")
	fmt.Println(arr)
	fmt.Println("")
	SelectionSort(&arr, n)

	fmt.Println("After")
	fmt.Println(arr)
}

func swap(arr *[]int, firstIndex int, secondIndex int) {
	var tempArray []int = *arr
	var temp int = tempArray[firstIndex]

	tempArray[firstIndex] = tempArray[secondIndex]
	tempArray[secondIndex] = temp
}

func indexOfMinimum(arr *[]int, startIndex int, n int) int {
	var tempArr []int = *arr
	var minValue int = tempArr[startIndex]
	var minIndex int = startIndex

	for i := minIndex + 1; i < n; i++ {
		if tempArr[i] < minValue {
			minIndex = i
			minValue = tempArr[i]
		}
	}
	return minIndex
}

// SelectionSort for selection sort
func SelectionSort(arr *[]int, n int) {
	for i := 0; i < n; i++ {
		index := indexOfMinimum(arr, i, n)
		swap(arr, i, index)
	}
}
