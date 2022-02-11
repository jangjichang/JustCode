// average 프로그램은 숫자들의 평균을 계산합니다.
package main

import (
	"fmt"
	floats "justcode/go/head_first_go/ch06_slice/datafile"
	"log"
)

func main() {
	numbers, err := floats.GetFloats("go/head_first_go/ch06_slice/data.txt")
	if err != nil {
		log.Fatal(err)
	}

	var sum float64 = 0
	for _, number := range numbers {
		sum += number
	}
	sampleCount := float64(len(numbers))
	fmt.Printf("Average: %0.2f\n", sum/sampleCount)
}
