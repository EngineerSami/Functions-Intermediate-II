class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self
    
    def add_to_back(self, val):
        new_node = SLNode(val)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        return self

    def print_values(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

if __name__ == "__main__":
    my_list = SList()
    my_list.add_to_back(30)
    my_list.add_to_back(40)
    my_list.add_to_front(10)
    my_list.add_to_front(20)
    my_list.print_values()