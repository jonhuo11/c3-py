import math

class Node:
    def __init__(self, name):
        self.name = name

        self.edges = []
        self.lowest_cost_to = math.inf
        self.prev_node = None
class Edge:
    def __init__(self, to, cost):
        self.to = to
        self.cost = cost
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

def dijkstra (start, end, graph):
    current = start
    current.lowest_cost_to = 0

    unvisited = graph.nodes
    visited = []

    while (True):
        for edge in current.edges:
            node = edge.to
            if node not in visited:
                cost_to = current.lowest_cost_to + edge.cost
                if cost_to < node.lowest_cost_to:
                    node.lowest_cost_to = cost_to
                node.prev_node = current
            else:
                continue

        unvisited.remove(current)
        visited.append(current)

        if len(unvisited) <= 0:
            path = []
            step = end
            while step != start:
                path.append(step)
                step = step.prev_node
            path.append(start)
            return path
        else:
            cheapest = Node("", [])
            for node in unvisited:
                if node.lowest_cost_to < cheapest.lowest_cost_to:
                    cheapest = node
            current = cheapest

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.edges = [Edge(b, 1), Edge(c, 4)]
b.edges = [Edge(e, 10)]
c.edges = [Edge(d, 3), Edge(e, 12)]
d.edges = [Edge(e, 2)]

the_map = Graph([a, b, c, d, e])

output = reversed([x for x in dijkstra(a, e, the_map)])
[print(x.name) for x in output]
