class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next         
        fast = fast.next.next    

        if slow == fast:          
            return True
    return False



head1.next = Node(2)
head1.next.next = Node(3)

print("Cycle in List 1:", has_cycle(head1)) 


head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
head2.next.next.next = Node(4)
head2.next.next.next.next = head2.next  

print("Cycle in List 2:", has_cycle(head2)) 
