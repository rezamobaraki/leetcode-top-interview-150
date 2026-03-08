from linked_list import ListNode


def delete_node(head: ListNode, target: int) -> ListNode:
	if head.value == target:
		return head.next

	previous = None
	current = head

	while current:
		if current.value == target:
			previous.next = current.next
			break

		previous = current
		current = current.next

	return head


if __name__ == '__main__':
	# Example 1
	head = ListNode(4)
	head.next = ListNode(5)
	head.next.next = ListNode(1)
	head.next.next.next = ListNode(9)
	target = 5
	delete_node(head, target)

	# Example 2
	head = ListNode(4)
	head.next = ListNode(5)
	head.next.next = ListNode(1)
	head.next.next.next = ListNode(9)
	target = 1
	delete_node(head, target)

	# Example 3
	head = ListNode(4)
	head.next = ListNode(5)
	head.next.next = ListNode(1)
	head.next.next.next = ListNode(9)
	target = 4
	delete_node(head, target)
