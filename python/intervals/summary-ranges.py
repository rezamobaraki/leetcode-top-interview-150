from typing import List


def summary_ranges(nums: List[int]) -> List[str]:
    if not nums:
        return []

    res = []
    start = end = nums[0]

    for i in range(1, len(nums)):
        if nums[i] - end == 1:
            end = nums[i]
        else:
            if start == end:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{end}")
            start = end = nums[i]

    if start == end:
        res.append(str(start))
    else:
        res.append(f"{start}->{end}")

    return res


if __name__ == '__main__':
    nums = [0, 1, 2, 4, 5, 7]
    print(summary_ranges(nums))  # ["0->2", "4->5", "7"]

    nums = [0, 2, 3, 4, 6, 8, 9]
    print(summary_ranges(nums))  # ["0", "2->4", "6", "8->9"]

    nums = []
    print(summary_ranges(nums))  # []
