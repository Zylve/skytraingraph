class Node:
    name = ""

    edges = []

    def __init__(self, name) -> None:
        self.name = name

    def add_edge(self, edge) -> None:
        self.edges.append(edge)

    def get_edges(self) -> list:
        return self.edges

class Edge:
    start = None
    end = None
    cost = 0

    def __init__(self, start, end, cost) -> None:
        self.start = start
        self.end = end
        self.cost = cost

class Graph:
    nodes = []
    edges = []

    def __init__(self) -> None:
        pass

    def add_node(self, node) -> None:
        if not any(n.name == node.name for n in self.nodes):
            self.nodes.append(node)

    def add_edge(self, start, end, cost) -> None:
        startstn = next(n for n in self.nodes if n.name == start)
        endstn = next(n for n in self.nodes if n.name == end)

        edge = Edge(startstn, endstn, cost)

        self.edges.append(edge)
        startstn.add_edge(edge)
