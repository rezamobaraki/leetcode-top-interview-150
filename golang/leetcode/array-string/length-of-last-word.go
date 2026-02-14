package main

func lengthOfLastWord(s string) int {
	pointer := len(s)
	result := 0
	for pointer > 0 {
		pointer--
		if s[pointer] != ' ' {
			result++
		} else if result > 0 {
			return result
		}
	}
	return result
}

func main() {
	output := lengthOfLastWord("Hello World")
	println(output) // Output: 5

	output = lengthOfLastWord("   fly me   to   the moon  ")
	println(output) // Output: 4

	output = lengthOfLastWord("luffy is still joyboy")
	println(output) // Output: 6
}
