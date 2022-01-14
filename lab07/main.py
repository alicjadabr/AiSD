from enum import Enum
from typing import Any, Optional, Dict, List, Callable
from graph.lab2 import Queue


class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int) -> None:
        self.data = data
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.source = source
        self.destination = destination
        self.weight = None
        if weight is not None:
            self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self):
        self.adjacencies: Dict = {}

    def create_vertex(self, data: Any) -> Vertex:
        # doda nowy wierzchołek do słownika adjacencies jako klucz i pustą listę sąsiedztwa jako wartość
        index = len(self.adjacencies)
        vertex: Vertex = Vertex(data, index)
        if vertex in self.adjacencies:
            print('Graf zawiera podany wierzcholek')
        else:
            self.adjacencies[vertex] = []
            return vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge: Edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        edge: Edge = Edge(source, destination, weight)
        self.adjacencies[source].append(edge)
        edge2: Edge = Edge(destination, source, weight)
        self.adjacencies[destination].append(edge2)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == EdgeType(1):
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        first: Vertex = list(self.adjacencies.keys())[0]
        list_of_visited_vertex: List[Vertex] = [first]
        queue = Queue()
        queue.enqueue(first)

        while len(queue) != 0:
            v: Vertex = queue.dequeue()
            visit(v)
            for neighbor in self.adjacencies[v]:
                if neighbor not in list_of_visited_vertex:
                    list_of_visited_vertex.append(neighbor)
                    queue.enqueue(neighbor)

    def __str__(self):
        res: str = ""
        i=0
        for v in self.adjacencies.keys():
            res += str(v.index) + str(v.data) + "--->" + " "
            for n




            curr: Vertex = list(self.adjacencies.keys())[i]
            res += "v" + str(i) + "--->" + "" + str(list(self.adjacencies[curr])) + "\n"

        return res


graph: Graph = Graph()
v0: Vertex = graph.create_vertex("v0")
v1: Vertex = graph.create_vertex("v1")
v2: Vertex = graph.create_vertex("v2")
v3: Vertex = graph.create_vertex("v3")
v4: Vertex = graph.create_vertex("v4")
v5: Vertex = graph.create_vertex("v5")
graph.add_directed_edge(v0, v1)
graph.add_directed_edge(v0, v5)
graph.add_directed_edge(v2, v3)
graph.add_directed_edge(v2, v1)
graph.add_directed_edge(v3, v4)
graph.add_directed_edge(v4, v1)
graph.add_directed_edge(v4, v5)
graph.add_directed_edge(v5, v1)
graph.add_directed_edge(v5, v2)
print(graph)