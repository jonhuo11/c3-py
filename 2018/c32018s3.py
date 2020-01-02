# can only pass the first test case on DMOJ


# scan for tiles covered by the camera, mark them and if the robot goes there then fail
# run a DFS to each tile, if a conveyor is stepped on then follow it

import sys

ln1 = input().split()
height = int(ln1[0])
width = int(ln1[1])

grid = []
for h in range(height):
    grid.append(list(input()))

# reverse xy for conv
def get(x,y):
    global grid
    return grid[y][x]

dests_l = []
dests = {}
start = (-1, -1)
spawn_on_cam = False
# mark areas under camera to be *
for y in range(height):
    for x in range(width):
        t = get(x,y)
        if t == ".":
            dests_l.append((x, y))
            dests[str(x) + "," + str(y)] = -1
        elif t == "S":
            start = (x, y)
        elif t == "C":
            #scan up
            for i in range(1, y + 1):
                t1 = get(x, y - i)
                if t1 == "S":
                    spawn_on_cam = True
                elif t1 != "W" and t1 != "*" and t1 != "C":
                    grid[y - i][x] = "*"
                else:
                    break
            #scan down
            for i in range(1, height - y):
                t1 = get(x, y + i)
                if t1 == "S":
                    spawn_on_cam = True
                elif t1 != "W" and t1 != "*" and t1 != "C":
                    grid[y + i][x] = "*"
                else:
                    break
            #scan left
            for i in range(1, x + 1):
                t1 = get(x - i, y)
                if t1 == "S":
                    spawn_on_cam = True
                elif t1 != "W" and t1 != "*" and t1 != "C":
                    grid[y][x - i] = "*"
                else:
                    break
            #scan right
            for i in range(1, width - x):
                t1 = get(x + i, y)
                if t1 == "S":
                    spawn_on_cam = True
                elif t1 != "W" and t1 != "*" and t1 != "C":
                    grid[y][x + i] = "*"
                else:
                    break
if spawn_on_cam:
    for i in dests_l:
        print(-1)
    sys.exit()

# return neighbours of tile at xy
def get_links(x, y):
    global width, height
    out = []
    if x + 1 < width:
        out.append((x+1, y))
    if x - 1 > -1:
        out.append((x-1, y))
    if y + 1 < height:
        out.append((x, y + 1))
    if y - 1 > -1:
        out.append((x, y - 1))
    # remove if wall/cam spot
    for o in out:
        t = get(o[0], o[1])
        if t == "W" or t == "*" or t == "C":
            out.remove(o)
    return out

# dfs the graph
visited = []
path = []
current = start
import time
while True:
    ct = get(current[0], current[1])
    key = str(current[0]) + "," + str(current[1])
    dests[key] = len(path)
    links = get_links(current[0], current[1])
    if len(links) > 0:
        can_go = False
        for l in links:
            t = get(l[0], l[1])
            if l not in visited and t == ".":
                can_go = True
                path.append(current)
                visited.append(current)
                current = l
                break
        if can_go:
            continue
        elif current == start:
            break
    path.pop(-1)
    current = path[-1]
for d in dests_l:
    key = str(d[0]) + "," + str(d[1])
    print(dests[key])
