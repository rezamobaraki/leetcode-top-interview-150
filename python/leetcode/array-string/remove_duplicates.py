def remove_duplicates(nums: List[int]) -> int:
	n = len(nums)
	if n <= 2:
		return n

	i = 2
	for j in range(2, n):
		if nums[j] != nums[i - 2]:
			nums[i] = nums[j]
			i += 1

	return i


if __name__ == '__main__':
	nums = [1, 1, 1, 2, 2, 3]
	print(remove_duplicates(nums))
