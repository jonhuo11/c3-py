# solution runs overtime on DMOJ

'''
#for each node in the triangle, check to see if a subtriangle can be created from it
#create a function that computes the maximum element of a subtriangle

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

#array of rows of nodes, the i'th row has i nodes
rows = []
nodes = []

#build triangle
ln1 = input().split()
triangle_size = int(ln1[0])
subtriangle_size = int(ln1[1])

#for each following line of input, add it to the ith row
for i in range(triangle_size):
    ln = input().split()
    row = []
    for n in ln:
        obj = Node(int(n), [])
        row.append(obj)
        nodes.append(obj)
    rows.append(row)

#build a triangle data structure, each node shares one common child with its neighbour
#first check if rows has only 1 row, then return its value
if (len(rows) <= 1):
    print(rows[0][0])
    exit()

#starting on the second node of the second row, add them as children of the parent node

#loop for rows
for i in range(1, len(rows)):
    current_row = rows[i]
    prev_row = rows[i-1]
    #loop for items in a row
    for j in range(1, len(current_row)):
        #add current item plus the previous item as a child to the node in the previous row
        current_node = current_row[j]
        prev_row[j - 1].children.append(current_node)
        prev_row[j - 1].children.append(current_row[j - 1])
root = rows[0][0]

#find all subtriangles of given size

#get max out of array of nodes
def get_max_val(nodes):
    max = nodes[0]
    for node in nodes:
        if node.val > max.val:
            max = node
    return max.val

#subtriangle solver function
def solve_subtriangle(base, size):
    #starting at the base, go down the children and add them to an array of nodes in the subtriangle
    if size <= 1:
        return get_max_val([base])
    else:
        level = 1
        row = [base]
        next_row = []
        sub_nodes = row.copy()
        while(level < size):
            for node in row:
                for child in node.children:
                    if(child not in next_row) and (child not in sub_nodes):
                        next_row.append(child)
                        sub_nodes.append(child)
            row = next_row.copy()
            next_row = []
            #if row is empty, it means the bottom level is reached so return -1
            if (len(row) <= 0):
                return -1
            level += 1
        return get_max_val(sub_nodes)

sum = 0
for node in nodes:
    ret = solve_subtriangle(node, subtriangle_size)
    if (ret > -1):
        sum += ret
print(sum)
'''
