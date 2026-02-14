package main

func CanConstruct(ransomNote string, magazine string) bool {
	magazineCount := map[rune]int{}
	for _, char := range magazine {
		magazineCount[char]++
	}

	for _, char := range ransomNote {
		if magazineCount[char] == 0 {
			return false
		}
		magazineCount[char]--
	}
	return true
}

func main() {

	ransomNote := "aa"
	magazine := "aab"
	println(CanConstruct(ransomNote, magazine)) // true

	ransomNote = "aa"
	magazine = "ab"
	println(CanConstruct(ransomNote, magazine)) // false
}
