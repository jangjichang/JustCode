package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.Open("data.txt") // 열린 파일을 나타내는 os.File에 값에 대한 포인터와 에러를 반환
	if err != nil {
		log.Fatal(err)
	}

	scanner := bufio.NewScanner(file) // 파일에 대한 Scanner를 생성한다. 파일로부터 데이터를 읽는다.
	for scanner.Scan() {              // 파일로부터 한 줄의 텍스트를 읽어온다. 읽기에 성공하면 true, 실패하면 false를 반환한다.
		fmt.Println(scanner.Text())
	}
	err = file.Close()
	if err != nil {
		log.Fatal(err)
	}

	if scanner.Err() != nil {
		log.Fatal(scanner.Err())
	}
}
