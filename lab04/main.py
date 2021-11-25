from typing import Any, List, Callable, Union
import queue

class TreeNode:
    value: Any
    children: List['TreeNode']
    def __init__(self, value):
        self.value = value
        self.children = []
    def is_leaf(self) -> bool:
        if len(self.children) != 0:
            return False
        else:
            return True
    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        #odwiedź bieżący wierzchołek i wykonaj na nim funkcję visit (przyjętą w parametrze)
        visit(self)
        #dla wszystkich dzieci bieżącego węzła wykonaj metodę for_each_deep_first()
        for child in self.children:
            child.for_each_deep_first(visit)
    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        # odwiedź bieżący wierzchołek i wykonaj na nim funkcję visit (przyjętą w parametrze)
        visit(self)
        # wszystkie dzieci bieżącego węzła dodaj do pustej kolejki FIFO
        fifo = queue.Queue()
        for child in self.chilren:
            fifo.put(child)
        # dopóki kolejka nie jest pusta, dla każdego pierwszego elementu w kolejce (element)
        while fifo.empty() == False:
            # 1: odwiedź element
            visit(fifo.get())
            #2: dodaj do kolejki wszystkie węzły, których rodzicem jest element
            for child in fifo.get().children:
                fifo.append(child)
    def search(self, value: Any) -> Union['TreeNode', None]:
        if self.for_each_deep_first(visit)
    def print(self):
        print(str(self.value))

class Tree:
    root: TreeNode
    def __init__(self, value):
        self.root = TreeNode(value)

    def add(value: Any, parent_name: Any) -> None:
        #doda nowe dziecko z wartością przekazaną w parametrze value, którego rodzicem będzie węzeł przekazany w parametrze parent_value
        parent_name.



