package main

import "fmt"

func mostCommonPrefix(strs []string) string {
	prefix := strs[0]
	prefixLength := len(prefix)

	for _, s := range strs[1:] {
		for prefixLength > len(s) || prefix != s[0:prefixLength] {
			prefixLength--
			if prefixLength == 0 {
				return ""
			}
			prefix = prefix[0:prefixLength]
		}
	}
	return prefix

}

func main() {
	strs := []string{"flower", "flow", "flight"}
	fmt.Println(mostCommonPrefix(strs))
}
