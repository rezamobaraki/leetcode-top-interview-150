

def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # Start from the end of both arrays
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


def merge_v2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    while p2 >= 0:
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1


if __name__ == '__main__':
    nums1 = [2, 3, 4, 0, 0, 0]
    m = 3
    nums2 = [1, 5, 6]
    n = 3
    # merge(nums1, m, nums2, n)
    merge_v2(nums1, m, nums2, n)
    print(nums1)  # Output: [1, 2, 2, 3, 5, 6]
