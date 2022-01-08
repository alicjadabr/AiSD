from typing import Any, List


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> 'BinaryNode':
        if self.left_child:
            curr = self
            while curr.left_child:
                curr = curr.left_child
            return curr
        else:
            return self



class BinarySearchTree:
    root: BinaryNode

    def __init__(self, value=None) -> None:
        self.root = BinaryNode(value)

    def insert(self, value: Any) -> None:
        if self.root.value is None:
            self.root.value = value
        else:
            self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any):
        parent = None
        while node:
            parent = node
            if value < node.value:
                node = node.left_child
            else:
                node = node.right_child

        if value < parent.value:
            parent.left_child = BinaryNode(value)
        else:
            parent.right_child = BinaryNode(value)

    def insertlist(self, list: List[Any]) -> None:
        for el in list:
            self.insert(el)

    def contains(self, value: Any) -> bool:
        curr = self.root
        while curr:
            if value == curr.value:
                return True
            elif value < curr.value:
                curr = curr.left_child
            elif value > curr.value:
                curr = curr.right_child
        return False


    def remove(self, value: Any):
        #znalezienie usuwanego wezla(node) i jego rodzica(parent)
        parent = None
        node = self.root
        while node and node.value != value:
            parent = node
            if value < node.value:
                node = node.left_child
            else:
                node = node.right_child
        # usuwanie liscia
        if node.left_child is None and node.right_child is None:
            if node == self.root:
                self.root = None
            else:
                if parent.left_child == node:
                    parent.left_child = None
                else:
                    parent.right_child = None
        # usuwanie node z dwojka dzieci
        elif node.left_child and node.right_child:
            min_right_subtree = node.right_child.min()
            value_min = min_right_subtree.value
            self.remove(value_min)
            node.value = value_min
        else:
        #usuwanie node z 1 dzieckiem
            if parent.left_child == node:
                if node.left_child:
                    parent.left_child = node.left_child
                else:
                    parent.left_child = node.right_child
            else:
                if node.left_child:
                    parent.right_child = node.left_child
                else:
                    parent.right_child = node.right_child


    def print(self, root, space):
        count = [10]
        if (root == None):
            return
        space += count[0]
        self.print(root.right_child, space)
        print()
        for i in range(count[0], space):
            print(end=" ")
        print(root.value)

        self.print(root.left_child, space)

    def show(self, root):
        self.print(root, 0)


tree = BinarySearchTree()
tree.insert(22)
tree.insert(10)
tree.insert(30)
tree.insert(50)
tree.insert(60)
tree.insert(70)
tree.insert(65)
tree.insert(80)
tree.insert(17)
tree.insert(2)
tree.insert(4)
tree.insert(24)
tree.show(tree.root)
tree.remove(10)
tree.show(tree.root)
print(tree.contains(234))


