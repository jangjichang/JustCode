package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println(reflect.TypeOf(25))      // int
	fmt.Println(reflect.TypeOf(true))    // bool
	fmt.Println(reflect.TypeOf(5.2))     // float64
	fmt.Println(reflect.TypeOf(1))       // int
	fmt.Println(reflect.TypeOf(false))   // bool
	fmt.Println(reflect.TypeOf(1.0))     // float64
	fmt.Println(reflect.TypeOf("hello")) // string
}
