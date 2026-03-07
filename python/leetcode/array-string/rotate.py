def rotate(nums: list[int], k: int) -> list[int]:
	n = len(nums)
	k %= n

	def reverse(start: int, end: int):
		while start < end:
			nums[start], nums[end] = nums[end], nums[start]
			start += 1
			end -= 1

	reverse(0, n - 1)
	reverse(0, k - 1)
	reverse(k, n - 1)

	return nums


def rotate_v2(nums: list[int], k: int) -> None:
	n = len(nums)
	k = k % n
	nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
	nums = [1, 2, 3, 4, 5, 6, 7]
	k = 3
	rotate(nums, k)
	print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
