from linked_list import ListNode


def linked_list_loop(head: ListNode) -> bool:
	slow = fast = head

	while fast and fast.next:
		slow, fast = slow.next, fast.next.next
		if fast == slow: return True

	return False


if __name__ == '__main__':
	# Example 1
	head = ListNode(3)
	head.next = ListNode(2)
	head.next.next = ListNode(0)
	head.next.next.next = ListNode(-4)
	head.next.next.next.next = head.next
	print(linked_list_loop(head))  # Output: True

	# Example 2
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = head
	print(linked_list_loop(head))  # Output: True

	# Example 3
	head = ListNode(1)
	print(linked_list_loop(head))  # Output: False
