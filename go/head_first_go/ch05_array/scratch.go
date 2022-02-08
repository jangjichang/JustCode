package main

import "fmt"

func main() {
	notes := [7]string{"do", "re", "mi", "fa", "so", "la", "ti"}
	primes := [5]int{2, 3, 5, 7, 11}

	fmt.Println(len(notes))
	fmt.Println(len(primes))

	for _, note := range notes {
		fmt.Println(note)
	}
}
