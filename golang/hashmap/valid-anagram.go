package main

/*
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.


Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
*/

import "fmt"

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	freqS := make(map[rune]int)
	freqT := make(map[rune]int)

	for _, char := range s {
		freqS[char]++
	}
	for _, chage := range t {
		freqT[chage]++
	}

	for char, count := range freqS {
		if freqT[char] != count {
			return false
		}
	}
	return true
}

func isAnagram2(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	lettersCount := make(map[rune]int)

	for _, ch := range s {
		lettersCount[ch]++
	}

	for _, ch := range t {
		if lettersCount[ch] == 0 {
			return false
		}

		lettersCount[ch]--
	}
	return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram")) // Output: true
	fmt.Println(isAnagram("rat", "car"))         // Output: false

	fmt.Println(isAnagram2("anagram", "nagaram")) // Output: true

}
