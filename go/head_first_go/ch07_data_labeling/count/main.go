package main

import (
	"fmt"
	"justcode/go/head_first_go/ch07_data_labeling/datafile"
	"log"
)

func main() {
	lines, err := datafile.GetStrings("go/head_first_go/ch07_data_labeling/count/votes.txt")
	if err != nil {
		log.Fatal(err)
	}
	var names []string
	var counts []int
	for _, line := range lines {
		matched := false
		for i, name := range names {
			if name == line {
				counts[i]++
				matched = true
			}
		}
		if matched == false {
			names = append(names, line)
			counts = append(counts, 1)
		}
	}

	for i, name := range names {
		fmt.Printf("%s: %d\n", name, counts[i])
	}
}
