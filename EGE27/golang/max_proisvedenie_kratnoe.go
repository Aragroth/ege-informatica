/*
Найти в последовательнсоти пару чисел, чтобы их произведение
было максимальным и при этом кратно 26
*/

package main

// TODO дописать комментарии

import (
	"os"
	"fmt"
	"bufio"
	"strconv"
)

var (
	max_not int
	max2	int
	max13	int
	max26	int
	answer	int
)

func main() {
	file, err := os.Open("../data/27988_B.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()

	for scanner.Scan() {
		num, err := strconv.Atoi(scanner.Text())
		if err != nil {
			panic(err)
		}

		if num % 26 == 0 && num > max26 {
			max26 = num
		} else if num % 13 == 0 && num > max13 {
			max13 = num
		} else if num % 2 == 0 && num > max2 {
			max2 = num
		} else if num > max_not {
			max_not = num
		}
	}

	if err := scanner.Err(); err != nil{
		panic(err)
	}

	if max13 * max2 > answer {
		answer = max13 * max2
	}
	if max_not * max26 > answer {
		answer = max_not * max26
	}

	fmt.Println(answer)
}


