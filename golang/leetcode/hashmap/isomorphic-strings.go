package main

func isIsomorphic(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	s2t := make(map[byte]byte)
	t2s := make(map[byte]byte)

	for i := 0; i < len(s); i++ {
		charS, charT := s[i], t[i]

		if mappedChar, ok := s2t[charS]; ok {
			if mappedChar != charT {
				return false
			}
		} else {
			s2t[charS] = charT
		}

		if mappedChar, ok := t2s[charT]; ok {
			if mappedChar != charS {
				return false
			}
		} else {
			t2s[charT] = charS
		}
	}
	return true
}

func isIsomorphic2(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	s2t := make(map[byte]byte)
	t2s := make(map[byte]byte)

	for i := 0; i < len(s); i++ {
		charS, charT := s[i], t[i]

		if s2t[charS] != 0 && s2t[charS] != charT || t2s[charT] != 0 && t2s[charT] != charS {
			return false
		}
		s2t[charS] = charT
		t2s[charT] = charS
	}
	return true
}

func main() {
	s := "egg"
	t := "add"
	println(isIsomorphic(s, t)) // true

	s = "foo"
	t = "bar"
	println(isIsomorphic(s, t)) // false

	s = "paper"
	t = "title"
	println(isIsomorphic(s, t)) // true
}
