from queue import Queue


class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.right_child = None
        self.left_child = None

    """
          BINARY TREE INSERTION IMPLEMENTATION ======================
    """

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def get_right_child(self):
        for node in self.right_child:
            print(node.value)

    """
        DEPTH FIRST SEARCH METHOD IMPLEMENTATION ======================
    """
    def pre_order(self):
        print(self.value)
        if self.left_child:
            self.left_child.pre_order()
        if self.right_child:
            self.right_child.pre_order()

    def in_order(self):

        if self.left_child:
            self.left_child.in_order()

        print(self.value)

        if self.right_child:
            self.right_child.in_order()

    def post_order(self):
        if self.left_child:
            self.left_child.post_order()

        if self.right_child:
            self.right_child.post_order()

        print(self.value)


    """
        BREADTH FIRST SEARCH METHOD IMPLEMENTATION ======================
    """
    def bfs(self):
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            current_node = queue.get()
            print(current_node.value)

            if current_node.left_child:
                queue.put(current_node.left_child)

            if current_node.right_child:
                queue.put(current_node.right_child)

    """
        BINARY SEARCH TREE ======================
    """


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    """
        INSERTING NEW VALUE ======================
    """
    def insert_node(self, value):
        if value <= self.value and self.left_child:
            self.left_child.insert_node(value)
        elif value <= self.value:
            self.left_child = BinarySearchTree(value)
        elif value > self.value and self.right_child:
            self.right_child.insert_node(value)
        else:
            self.right_child = BinarySearchTree(value)

    """
       SEARCHING VALUE IN TREE ======================
    """
    def find_node(self, value):
        if value < self.value and self.left_child:
            return self.left_child.find_node(value)
        if value > self.value and self.right_child:
            return self.right_child.find_node(value)

        return value == self.value

    """
        DELETING FROM BINARY TREE===============
    """
    def remove_node(self, value, parent):
        if value < self.value and self.left_child:
            return self.left_child.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right_child:
            return self.right_child.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left_child is None and self.right_child is None and self == parent.left_child:
                parent.left_child = None
                self.clear_node()
            elif self.left_child is None and self.right_child is None and self == parent.right_child:
                parent.right_child = None
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.left_child:
                parent.left_child = self.left_child
                self.clear_node()
            elif self.left_child and self.right_child is None and self == parent.right_child:
                parent.right_child = self.left_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.left_child:
                parent.left_child = self.right_child
                self.clear_node()
            elif self.right_child and self.left_child is None and self == parent.right_child:
                parent.right_child = self.right_child
                self.clear_node()
            else:
                self.value = self.right_child.find_minimum_value()
                self.right_child.remove_node(self.value, self)

            return True

    def clear_node(self):
        self.value = None
        self.left_child = None
        self.right_child = None


if __name__ == '__main__':
    tree = BinaryTree('a')
    print(tree.value)
    # print(tree.right_child)
    # print(tree.left_child)

    tree.insert_left('b')
    tree.insert_right('c')

    left_tree = tree.left_child
    right_tree = tree.right_child

    left_tree.insert_right('d')
    right_tree.insert_left('e')
    right_tree.insert_right('f')

    # print(left_tree.value)
    # print(right_tree.value)

    d_node = left_tree.right_child
    e_node = right_tree.left_child
    f_node = right_tree.right_child

    # print(d_node.value)
    # print(e_node.value)
    # print(f_node.value)

    print('PRE-ORDER')
    print(tree.pre_order())
    print('IN-ORDER')
    print(tree.in_order())
    print('POST-ORDER')
    print(tree.post_order())
    print('BREADTH FIRST SEARCH')
    print(tree.bfs())

    bst = BinarySearchTree(15)
    bst.insert_node(10)
    bst.insert_node(8)
    bst.insert_node(12)
    bst.insert_node(20)
    bst.insert_node(17)
    bst.insert_node(25)
    bst.insert_node(19)

    print(bst.find_node(15))  # True
    print(bst.find_node(10))  # True
    print(bst.find_node(8))  # True
    print(bst.find_node(12))  # True
    print(bst.find_node(20))  # True
    print(bst.find_node(17))  # True
    print(bst.find_node(25))  # True
    print(bst.find_node(19))  # True
    print(bst.find_node(26))
