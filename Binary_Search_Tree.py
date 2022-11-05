

class Binary_tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = Binary_tree(data)
        if data > self.data:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = Binary_tree(data)

    def search(self, value):
        if value == self.data:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)

            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements = elements + self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements = elements + self.right.in_order_traversal()
        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements = elements + self.left.in_order_traversal()
        if self.right:
            elements = elements + self.right.in_order_traversal()
        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements = elements + self.left.in_order_traversal()
        if self.right:
            elements = elements + self.right.in_order_traversal()
        elements.append(self.data)
        return elements


def build_tree(elements):
    print("building tree with these elements: ", elements)
    root = Binary_tree(elements[3])
    for i in range(len(elements)):
        root.add_child(elements[i])
    return root


if __name__ == '__main__':
    number_tree = build_tree([17, 4, 1, 12, 25, 4, 34, 20, 9, 23, 18, 34])
    print()
    print("In-order Traversal: ", number_tree.in_order_traversal())
    print()
    print("Pre-order Traversal: ", number_tree.pre_order_traversal())
    print()
    print("Post-order Traversal: ", number_tree.post_order_traversal())
    print("Is number 100 is in the list? ", number_tree.search(100))
