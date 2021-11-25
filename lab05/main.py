from typing import Any, Callable


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

    def traverse_in_order(self, node):
        if node is not None:
            self.traverse_in_order(node.left_child)
            print(node.value)
            self.traverse_in_order(node.right_child)

    def traverse_post_order(self, node):
        if node is not None:
            self.traverse_post_order(node.left_child)
            self.traverse_post_order(node.right_child)
            print(node.value)

    def traverse_pre_order(self, node):
        if node is not None:
            print(node.value)
            self.traverse_pre_order(node.left_child)
            self.traverse_pre_order(node.right_child)

    def print(self):
        print(str(self.value))


class BinaryTree:
    root: BinaryNode

    def __init__(self, value):
        self.root = BinaryNode(value)

    def traverse_in_order(self, root: BinaryNode):
        if root is not None:
            self.traverse_in_order(root.left_child)
            print(root.value),
            self.traverse_in_order(root.right_child)

    def traverse_post_order(self, root: BinaryNode):
        if root is not None:
            self.traverse_post_order(root.left_child)
            self.traverse_post_order(root.right_child)
            print(root.value)

    def traverse_pre_order(self, root: BinaryNode):
        if root is not None:
            print(root.value)
            self.traverse_pre_order(root.left_child)
            self.traverse_pre_order(root.right_child)



tree = BinaryTree(55)
tree.root.add_left_child(12)
tree.root.add_right_child(4)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(18)
tree.root.right_child.add_left_child(20)
tree.root.right_child.add_right_child(22)
tree.root.right_child.traverse_pre_order(tree.root.right_child)



assert tree.root.value == 55
assert tree.root.right_child.value == 4
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True





