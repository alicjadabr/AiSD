from typing import Any, Callable, List

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

    def print(self, root, space):
        count = [11]
        if (root == None):
            return
        space += count[0]
        self.print(root.right_child, space)
        print()
        for i in range(count[0], space):
            print(end=" ")
        print(root.value)

        self.print(root.left_child, space)

    def print_tree(self, root):
        self.print(root, 0)



def right_line(tree: BinaryTree) -> List[BinaryNode]:
    root = tree.root
    if root is None:
        return

    list = []
    q = []
    q.append(root)
    while (len(q) != 0):
        # n - liczba wezlow na danym poziomie
        n = len(q)
        # przechodzenie po kazdym wezle danego poziomu
        for i in range(1, n+1):
            curr = q[0]
            q.pop(0)
            # dodanie do listy skrajnego prawego elementu drzewa
            if (i == n):
                list.append(curr.value)
            if (curr.left_child is not None):
                q.append(curr.left_child)
            if (curr.right_child is not None):
                q.append(curr.right_child)
    return list


tree = BinaryTree(1)
tree.root.add_left_child(2)
tree.root.add_right_child(3)
tree.root.left_child.add_left_child(4)
tree.root.left_child.add_right_child(5)
tree.root.right_child.add_right_child(7)
tree.root.left_child.left_child.add_left_child(8)
tree.root.left_child.left_child.add_right_child(9)
tree.print_tree(tree.root)
def print_traverse(node: BinaryNode):
    print(node.value)
#tree.traverse_pre_order(print_traverse)
print(right_line(tree))


assert tree.root.value == 1
assert tree.root.right_child.value == 3
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 4
assert tree.root.left_child.left_child.left_child.is_leaf() is True