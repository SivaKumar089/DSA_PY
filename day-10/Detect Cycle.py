class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # move 1 step
        fast = fast.next.next     # move 2 steps

        if slow == fast:          # cycle detected
            return True
    return False


# -------------------- Testing --------------------

# Example 1: Linked List without cycle
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(3)

print("Cycle in List 1:", has_cycle(head1))  # False

# Example 2: Linked List with cycle
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
head2.next.next.next = Node(4)
head2.next.next.next.next = head2.next  # cycle created

print("Cycle in List 2:", has_cycle(head2))  # True
