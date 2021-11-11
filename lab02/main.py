from typing import List
from typing import Any

class Node:
    data: Any
    next: 'Node'

    def __init__(self, data=None) -> None:
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data: Any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node

    def node(self, at: int) -> Node:
        n = self.head
        for x in range(at):
            n = n.next
        return n


    def insert(self, data: Any, after: Node) -> None:
        n = self.head
        while n.next is not None:
            if after == n:
                break
            n = n.next
        if n.next is None:
            pass
        else:
            new_node = Node(data)
            new_node.next = n.next
            n.next = new_node

    def pop(self) -> Any:
        ret_pop = self.head.data
        self.head = self.head.next
        return ret_pop

    def remove_last(self) -> Any:
        if self.head is None:
            pass
        elif self.head.next is None:
            remove_el = self.head.data
            self.head = None
            return remove_el
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            remove_el = n.next.data
            n.next = None
            return remove_el


    def remove(self, after: Node) -> Any:
        if self.head is None:
            pass
        n = self.head
        while n.next is not None:
            if after == n:
                break
            n = n.next
        n.next = n.next.next

    def __str__(self) -> str:
        if self.head is None:
            return str(None)
        else:
            n = self.head
            li = ""
            while n is not None:
                li += str(n.data)
                if n.next != None:
                    li += " -> "
                n = n.next
            return li

    def __len__(self) -> int:
        if self.head is None:
            return 0
        n = self.head
        len = 0
        while n:
            len += 1
            n = n.next
        return len


l1 = LinkedList()
assert l1.head == None

l1.push(1)
l1.push(0)
assert str(l1) == '0 -> 1'

l1.append(9)
l1.append(10)
assert str(l1) == '0 -> 1 -> 9 -> 10'

middle_node = l1.node(at=1)
l1.insert(5, after=middle_node)

assert str(l1) == '0 -> 1 -> 5 -> 9 -> 10'

first_element = l1.node(at=0)
returned_first_element = l1.pop()

assert first_element.data == returned_first_element

last_element = l1.node(at=3)
returned_last_element = l1.remove_last()

assert last_element.data == returned_last_element
assert str(l1) == '1 -> 5 -> 9'

second_node = l1.node(at=1)
l1.remove(second_node)

assert str(l1) == '1 -> 5'


class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def push(self, data: Any) -> None:
        self._storage.append(data)

    def pop(self) -> Any:
        return self._storage.remove_last()

    def __str__(self) -> str:
        if self._storage.head is None:
            return str(None)
        else:
            n = self._storage.head
            li = ""
            reverse = LinkedList()
            while n is not None:
                reverse.push(n.data)
                n = n.next
            n = reverse.head
            while n is not None:
                li += (str(n.data) + '\n')
                n = n.next
            return li

    def __len__(self) -> int:
        return self._storage.__len__()


s = Stack()

assert len(s) == 0

s.push(3)
s.push(10)
s.push(1)

assert len(s) == 3

top_value = s.pop()

assert top_value == 1

assert len(s) == 2

class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head.data

    def enqueue(self, data: Any) -> None:
        self._storage.append(data)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __str__(self) -> str:
        return self._storage.__str__().replace(" -> ", ", ")
    def __len__(self) -> int:
        return self._storage.__len__()

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')

assert str(queue) == 'klient1, klient2, klient3'


client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2













