class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_node(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def insert_node(self, value, new_value):
        current = self.head
        while current:
            if current.value == value:
                new_node = Node(new_value)
                new_node.prev = current.prev
                new_node.next = current
                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def is_circular(self):
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def get_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value if slow else None

    def remove_duplicates(self):
        current = self.head
        values_seen = set()
        while current:
            if current.value in values_seen:
                self.delete_node(current.value)
            else:
                values_seen.add(current.value)
            current = current.next

    def reverse_list(self):
        current = self.head
        prev_node = None
        self.tail = current
        while current:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head = prev_node

dll = DoublyLinkedList()
dll.add_node(1)
dll.add_node(2)
dll.add_node(3)
dll.print_list()  

dll.insert_node(2, 1.5)
dll.print_list() 

dll.delete_node(1.5)
dll.print_list() 

dll.add_node(2)
dll.add_node(3)
dll.remove_duplicates()
dll.print_list() 

print("Middle:", dll.get_middle()) 

dll.reverse_list()
dll.print_list() 
