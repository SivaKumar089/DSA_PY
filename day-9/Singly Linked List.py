
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None  


class LinkedList:
    def __init__(self):
        self.head = None

   
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head  
        self.head = new_node       

   
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:         
            self.head = new_node
            return 
        last = self.head
        while last.next:           
            last = last.next
        last.next = new_node


    def delete_node(self, key):
        temp = self.head

        
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

   
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next
        temp = None

   
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")



ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_beginning(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.print_list()      

ll.delete_node(10)
ll.print_list()   
