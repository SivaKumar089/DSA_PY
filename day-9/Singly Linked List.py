# Node class
class Node:
    def __init__(self, data):
        self.data = data  # store value
        self.next = None  # pointer to next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  # new node points to old head
        self.head = new_node       # head becomes new node

    # Insert at end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:          # if list empty
            self.head = new_node
            return 
        last = self.head
        while last.next:           # traverse till last node
            last = last.next
        last.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        temp = self.head

        # Case 1: head itself has the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Case 2: search for key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:  # key not found
            return

        prev.next = temp.next
        temp = None

    # Print the linked list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# 🔹 Example usage
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_beginning(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.print_list()      # 20 -> 10 -> 30 -> 40 -> None

ll.delete_node(10)
ll.print_list()      # 20 -> 30 -> 40 -> None
