from typing import List


def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
	if not nums:
		return 0

	num_set = set(nums)
	longest_chain = 0

	for num in num_set:

		if num - 1 not in num_set:
			current_num = num
			current_chain = 1

			while current_num + 1 in num_set:
				current_num += 1
				current_chain += 1

			longest_chain = max(longest_chain, current_chain)

	return longest_chain


if __name__ == '__main__':
	print(longest_chain_of_consecutive_numbers([100, 4, 200, 1, 3, 2]))  # 4: [1,2,3,4]
	print(longest_chain_of_consecutive_numbers([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
