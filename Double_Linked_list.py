
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data)
        temp = self.head
        temp.prev = node
        node.next = temp
        self.head = node
        node.prev = None

    def insert_at_last(self, data):
        node = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = node
        node.prev = temp
        node.next = None

    def insert_at_between(self, data, index):
        node = Node(data)
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        node.data = data
        node.next = temp.next
        temp.next = node

    def remove_at_beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def remove_at_last(self):
        temp = self.head.next
        prev = self.head
        while(temp.next != None):
            temp = temp.next
            prev = prev.next
        prev.next = None

    def remove_in_between(self, index):
        temp = self.head.next
        prev = self.head
        for i in range(index-1):
            prev = prev.next
            temp = temp.next
        prev.next = temp.next

    def print_list(self):
        itr = self.head
        while(itr):
            print(itr.data, end="-><-")
            itr = itr.next
        print()


if __name__ == '__main__':
    ll = linked_list()
    n1 = Node(20)
    ll.head = n1
    n2 = Node(40)
    n2.prev = n1
    n1.next = n2
    n2.next = None
    print("This is our Double linked list: ")
    ll.print_list()
    print()

    print("Elements added at beginning: ")
    ll.insert_at_beginning(30)
    ll.insert_at_beginning(10)
    ll.print_list()

    print("Elements added at last: ")
    ll.insert_at_last(50)
    ll.insert_at_last(60)
    ll.print_list()
    
    print("Elements added in between: ")
    ll.insert_at_between(10000, 2)
    ll.print_list()

    print("Now element will be deleted from beginning: ")
    ll.remove_at_beginning()
    ll.print_list()

    print("Now element will be deleted from last: ")
    ll.remove_at_last()
    ll.print_list()

    print("Now element will be deleted from between: ")
    ll.remove_in_between(1)
    ll.print_list()
