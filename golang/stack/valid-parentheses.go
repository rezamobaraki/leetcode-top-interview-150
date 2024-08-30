package main

func isValid(s string) bool {
	var stack []rune
	bracketMap := map[rune]rune{')': '(', '}': '{', ']': '['}

	for _, char := range s {
		if closing, exists := bracketMap[char]; exists {
			// Pop the top element if it exists, else assign a dummy value
			if len(stack) > 0 && stack[len(stack)-1] == closing {
				stack = stack[:len(stack)-1]
			} else {
				return false
			}
		} else {
			// It's an opening bracket, push onto the stack
			stack = append(stack, char)
		}
	}

	// If stack is empty, all brackets were matched correctly
	return len(stack) == 0
}

func main() {
	println(isValid("()"))     // Output: true
	println(isValid("()[]{}")) // Output: true
	println(isValid("(]"))     // Output: false
	println(isValid("([)]"))   // Output: false
	println(isValid("{[]}"))   // Output: true
	println(isValid("{"))      // Output: false
	println(isValid("}"))      // Output: false
	println(isValid("()("))    // Output: false
}
