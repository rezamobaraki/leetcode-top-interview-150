def next_lexicographical_sequence(s: str) -> str:
	letters = list(s)
	pivot = len(letters) - 2

	while pivot >= 0 and letters[pivot] >= letters[pivot + 1]:
		pivot -= 1

	if pivot == -1:
		return ''.join(letters[::-1])

	successor = len(letters) - 1
	while letters[successor] <= letters[pivot]:
		successor -= 1

	letters[pivot], letters[successor] = letters[successor], letters[pivot]
	letters[pivot + 1:] = reversed(letters[pivot + 1:])

	return ''.join(letters)


if __name__ == '__main__':
	s = 'abcd'
	print(next_lexicographical_sequence(s))
