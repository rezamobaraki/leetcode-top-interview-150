package main

func isSubsequence(s string, t string) bool {
	sPointer, tPointer := 0, 0

	for sPointer < len(s) && tPointer < len(t) {
		if s[sPointer] == t[tPointer] {
			sPointer++
		}
		tPointer++
	}
	return sPointer == len(s)
}

func main() {
	s, t := "abc", "ahbgdc"
	println(isSubsequence(s, t)) // True

	s, t = "axc", "ahbgdc"
	println(isSubsequence(s, t)) // False

}
