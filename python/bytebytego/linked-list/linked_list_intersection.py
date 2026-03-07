from linked_list import ListNode


def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode | None:
	pointer_A, pointer_B = head_A, head_B

	while pointer_A is not pointer_B:
		pointer_A = pointer_A.next if pointer_A else head_B
		pointer_B = pointer_B.next if pointer_B else head_A

	return pointer_A


def linked_list_intersection_set(head_A: ListNode, head_B: ListNode) -> ListNode | None:
	visited = set()

	current = head_A
	while current:
		visited.add(current)
		current = current.next

	current = head_B
	while current:
		if current in visited:
			return current
		current = current.next

	return None


if __name__ == '__main__':
	linked_list_A = ListNode(1)
	linked_list_A.next = ListNode(2)
	linked_list_A.next.next = ListNode(3)
	linked_list_B = ListNode(4)
	linked_list_B.next = ListNode(5)

	intersection = ListNode(6)

	linked_list_A.next.next.next = intersection
	linked_list_B.next.next = intersection

	result = linked_list_intersection(linked_list_A, linked_list_B)
	print(result.value if result else None)  # Output: 6
