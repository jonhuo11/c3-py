class Node:
    def __init__(self, name):
        self.name = name

        self.neighbours = []
        self.prev = None

def bfs (start, end):
    visited = []
    seen = [start]

    while len(seen) > 0:
        for seen_node in seen:
            for adj in seen_node.neighbours:
                if adj not in visited:
                    seen.append(adj)
                    adj.prev = seen_node

                    if adj == end:
                        path = []
                        step = end
                        while step != start:
                            path.append(step)
                            step = step.prev
                        path.append(start)
                        return reversed(path)
            seen.remove(seen_node)
            visited.append(seen_node)

    return "couldn't find a path to " + end.name

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.neighbours = [b]
b.neighbours = [c]
c.neighbours = [b, d]
d.neighbours = [e]

output = bfs(a, e)
[print(x.name) for x in output]
