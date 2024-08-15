package main

import (
	"fmt"
	"unicode"
)

func isPalindrome(s string) bool {
	lPointer, rPointer := 0, len(s)-1
	for lPointer < rPointer {
		// Skip non-alphanumeric characters on the left
		if !unicode.IsLetter(rune(s[lPointer])) && !unicode.IsDigit(rune(s[lPointer])) {
			lPointer++
			continue
		}
		// Skip non-alphanumeric characters on the right
		if !unicode.IsLetter(rune(s[rPointer])) && !unicode.IsDigit(rune(s[rPointer])) {
			rPointer--
			continue
		}
		// Compare characters (ignoring case)
		if unicode.ToLower(rune(s[lPointer])) != unicode.ToLower(rune(s[rPointer])) {
			return false
		}
		lPointer++
		rPointer--
	}
	return true
}

func isPalindrome2(s string) bool {
	var cleanedStr []rune
	for _, c := range s {
		if unicode.IsLetter(c) || unicode.IsDigit(c) {
			cleanedStr = append(cleanedStr, unicode.ToLower(c))
		}
	}

	n := len(cleanedStr)
	for i := 0; i < n/2; i++ {
		if cleanedStr[i] != cleanedStr[n-i-1] {
			return false
		}
	}
	return true
}

func main() {
	s := "A man, a plan, a canal: Panama"
	fmt.Println(isPalindrome(s))
	s = "race a car"
	fmt.Println(isPalindrome(s))

	s = "A man, a plan, a canal: Panama"
	fmt.Println(isPalindrome2(s))

	s = "race a car"
	fmt.Println(isPalindrome2(s))
}
