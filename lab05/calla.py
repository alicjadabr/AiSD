from typing import Any, Callable
from binarytree import build

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        else:
            return False

    def add_left_child(self, value: Any):
        if self.left_child is None:
            self.left_child = BinaryNode(value)
        else:
            pass

    def add_right_child(self, value: Any):
        if self.right_child is None:
            self.right_child = BinaryNode(value)
        else:
            pass

    def traverse_in_order(self, visit: Callable[[Any], None]):
        #jeżeli bieżący węzeł ma lewe dziecko, to wykonaj na nim metodę in_order
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        #odwiedź bieżący węzeł
        visit(self)
        #jeżeli bieżący węzeł ma prawe dziecko, to wykonaj na nim metodę in_order
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        #jeżeli bieżący węzeł ma lewe dziecko, to wykonaj na nim metodę post_order
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        #jeżeli bieżący węzeł ma prawe dziecko, to wykonaj na nim metodę post_order
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        # odwiedź bieżący węzeł
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        # odwiedź bieżący węzeł
        visit(self)
        # jeżeli bieżący węzeł ma lewe dziecko, to wykonaj na nim metodę pre_order
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        # jeżeli bieżący węzeł ma prawe dziecko, to wykonaj na nim metodę pre_order
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def print(self):
        print(str(self.value))


class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        values = [55, 12, 14, 1, 18, 20, 22]
        root = build(values)
        print(root)


tree = BinaryTree(55)
tree.root.add_left_child(12)
tree.root.add_right_child(14)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(18)
tree.root.right_child.add_left_child(20)
tree.root.right_child.add_right_child(22)
tree.show()


assert tree.root.value == 55
assert tree.root.right_child.value == 14
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True