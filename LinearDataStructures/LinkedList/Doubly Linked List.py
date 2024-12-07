class Node:
    
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

dll = DoublyLinkedList()

dll.insert_at_beginning(10)
dll.insert_at_beginning(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.display()  

dll.display_reverse()  

print(dll.search(30))  
print(dll.search(50)) 
