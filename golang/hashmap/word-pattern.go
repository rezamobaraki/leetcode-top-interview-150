package main

import "strings"

/* 290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
*/

func wordPattern(pattern string, s string) bool {
	words := strings.Split(s, " ")

	if len(pattern) != len(words) {
		return false
	}

	charToWord := make(map[byte]string)
	wordToChar := make(map[string]byte)

	for i := 0; i < len(pattern); i++ {
		char, word := pattern[i], words[i]

		if mappedWord, exists := charToWord[char]; exists {
			if mappedWord != word {
				return false
			}
		} else {
			charToWord[char] = word
		}

		if mappedChar, exists := wordToChar[word]; exists {
			if mappedChar != char {
				return false
			}
		} else {
			wordToChar[word] = char
		}
	}

	return true
}

func main() {
	pattern := "abba"
	s := "dog cat cat dog"
	println(wordPattern(pattern, s)) // true

	pattern = "abba"
	s = "dog cat cat fish"
	println(wordPattern(pattern, s)) // false

	pattern = "aaaa"
	s = "dog cat cat dog"
	println(wordPattern(pattern, s)) // false
}
