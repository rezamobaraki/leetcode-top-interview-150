class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"ListNode({self.value})"


def linked_list_reversal(head: ListNode) -> ListNode:
    prev_node, current_node = None, head

    while current_node:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node

def linked_list_recursive(head: ListNode) -> ListNode:

    if not head or not head.next:
        return head

    new_head = linked_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    linked_list_recursive(node1)
