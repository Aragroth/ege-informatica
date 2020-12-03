/*
Найти сколько пар чисел делятся на 62 из вводимой последовательности (?)
*/

package main

// TODO написать комментарии

import (
	"os"
	"fmt"
	"bufio"
	"strconv"
)

var (
	n2	int
	n31	int
	n62	int
)

func main() {
	file, err := os.Open("data/27990_B.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	scanner.Scan()
	total, _ := strconv.Atoi(scanner.Text())

	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}
		if num % 62 == 0 {
			n62 += 1
		} else if num % 31 == 0 {
			n31 += 1
		} else if num % 2 == 0 {
			n2 += 1
		}
	}
	
	if err := scanner.Err(); err != nil{
		panic(err)
	}

	fmt.Println(n62 * (n62 - 1) / 2 + n62 * (total - n62) + n31 * n2)
}
