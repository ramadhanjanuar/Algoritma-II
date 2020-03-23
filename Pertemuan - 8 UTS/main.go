package main

import (
	"fmt"
)

type student struct {
	Nim   int
	Kelas int
	Nilai int
}

func main() {
	var data []student
	var inputJumlahMahasiswa int
	var nimMahasiswa []int
	var kelasMahasiswa []int
	var nilaiMahasiswa []int
	var input int

	fmt.Println("Input:")
	fmt.Scan(&inputJumlahMahasiswa)

	for i := 0; i < inputJumlahMahasiswa; i++ {
		fmt.Scan(&input)
		nimMahasiswa = append(nimMahasiswa, input)
	}

	for i := 0; i < inputJumlahMahasiswa; i++ {
		fmt.Scan(&input)
		kelasMahasiswa = append(kelasMahasiswa, input)
	}

	for i := 0; i < inputJumlahMahasiswa; i++ {
		fmt.Scan(&input)
		nilaiMahasiswa = append(nilaiMahasiswa, input)
	}

	for i := 0; i < inputJumlahMahasiswa; i++ {
		data = append(data, student{nimMahasiswa[i], kelasMahasiswa[i], nilaiMahasiswa[i]})
	}

	// Sorting
	sequentialSort(data)

	// Konsolidasi
	consolidation(data)
}

// Sorting Data
func sequentialSort(data []student) {
	var compareVariable = 0
	var tempData student
	for i := 1; i < len(data); i++ {
		if data[compareVariable].Kelas > data[i].Kelas {
			tempData = data[compareVariable]
			data[compareVariable] = data[i]
			data[i] = tempData
			compareVariable++
		} else {
			compareVariable++
		}
	}
}

// Konsolidasi Data
func consolidation(data []student) {
	var dataTemp = data[0]
	var kelasTemp int = dataTemp.Kelas
	var jumlahMahasiswa int = 0
	var rataRataNilaiMahasiswa = 0

	fmt.Println("")
	fmt.Println("Output:")

	for _, datum := range data {
		if kelasTemp == datum.Kelas {
			jumlahMahasiswa++
			rataRataNilaiMahasiswa += datum.Nilai
		} else {
			fmt.Println(kelasTemp, jumlahMahasiswa, rataRataNilaiMahasiswa/jumlahMahasiswa)
			kelasTemp = datum.Kelas
			jumlahMahasiswa = 1
			rataRataNilaiMahasiswa = datum.Nilai
		}
	}
	fmt.Println(kelasTemp, jumlahMahasiswa, rataRataNilaiMahasiswa/jumlahMahasiswa)
}
