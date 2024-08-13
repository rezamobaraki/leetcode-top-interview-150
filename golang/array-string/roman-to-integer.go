package main

import "fmt"

var ROMAN2INT = map[string]int{
	"I": 1,
	"V": 5,
	"X": 10,
	"L": 50,
	"C": 100,
	"D": 500,
	"M": 1000,
}

func romanToInt(s string) int {

	pointer := len(s) - 1
	result := 0

	for pointer >= 0 {
		if pointer > 0 && ROMAN2INT[string(s[pointer])] > ROMAN2INT[string(s[pointer-1])] {
			result += ROMAN2INT[string(s[pointer])] - ROMAN2INT[string(s[pointer-1])]
			pointer -= 2
		} else {
			result += ROMAN2INT[string(s[pointer])]
			pointer--
		}
	}
	return result
}

func romanToInt2(s string) int {
	result := 0

	for i := range s {
		if i < len(s)-1 && ROMAN2INT[string(s[i])] < ROMAN2INT[string(s[i+1])] {
			result -= ROMAN2INT[string(s[i])]
		} else {
			result += ROMAN2INT[string(s[i])]
		}
	}
	return result
}

func main() {
	output := romanToInt("III")
	fmt.Println(output) // Output: 3

	output = romanToInt("IV")
	fmt.Println(output) // Output: 4

	output = romanToInt("IX")
	fmt.Println(output) // Output: 9

	output = romanToInt("LVIII")
	fmt.Println(output) // Output: 58

	output = romanToInt2("MCMXCIV")
	fmt.Println(output) // Output: 1994
}
