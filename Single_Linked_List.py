

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_last(self, data):
        node = Node(data)
        last = self.head
        while (last.next):
            last = last.next
        last.next = node

    def insert_in_between(self, data, index):
        temp = self.head
        node = Node(data)
        for i in range(index-1):
            temp = temp.next
        node.data = data
        node.next = temp.next
        temp.next = node

    def remove_at_first(self):
        temp = self.head
        self.head = temp.next

    def remove_at_last(self):
        prev = self.head
        temp = self.head.next
        while(temp.next != None):
            temp = temp.next
            prev = prev.next
        prev.next = None

    def remove_in_between(self, index):
        temp = self.head.next
        prev = self.head
        for i in range(index-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next

    def print_list(self):
        itr = self.head
        while(itr):
            print(itr.data, end="->")
            itr = itr.next
        print()


if __name__ == '__main__':
    ll = linked_list()
    print("This is our linked list:")
    n1 = Node(8)
    ll.head = n1
    n2 = Node(10)
    n1.next = n2
    n3 = Node(12)
    n2.next = n3
    ll.print_list()
    
    print("Now the element will be added at beginning: ")
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(2)
    ll.print_list()

    print("Now the element will be added at last: ")
    ll.insert_at_last(14)
    ll.insert_at_last(16)
    ll.print_list()

    print("Now the element will be added in between: ")
    ll.insert_in_between(100, 3)
    ll.print_list()

    print("Now the first element will be deleted:")
    ll.remove_at_first()
    ll.print_list()

    print(" Now the last element will be deleted:")
    ll.remove_at_last()
    ll.print_list()

    print("Now element from middle will be deleted:")
    ll.remove_in_between(2)
    ll.print_list()
