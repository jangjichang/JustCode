package main

import "fmt"

func main() {
	price := 100
	fmt.Println("Price is", price, "dollars.")

	taxRate := 0.08
	var tax float64 = float64(price) * taxRate
	fmt.Println("Tax is", tax, "dollars.")

	total := float64(price) + tax
	fmt.Println("total cost is", total, "dollars.")

	availableFunds := 120
	fmt.Println(availableFunds, "dollars available.")
	fmt.Println("Within budget?", total <= float64(availableFunds))
}
