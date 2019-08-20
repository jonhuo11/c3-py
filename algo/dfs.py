class Node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []

def dfs (start, end):
    return dfs_helper(start, end, start, [], [])

def dfs_helper (start, end, current, path, visited):
    visited.append(current)
    path.append(current)

    if current == end:
        return path
    else:
        for adj in current.neighbours:
            if adj not in visited:
                return dfs_helper(start, end, adj, path, visited)
        if current == start:
            return "couldn't find a path to " + end.name
        else:
            path.remove(current)
            return dfs_helper(start, end, adj, path, visited)

a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")

a.neighbours = [b, c]
b.neighbours = [e]
c.neighbours = [d, e]
d.neighbours = [e]

output = dfs(a, e)
[print(x.name) for x in output]
