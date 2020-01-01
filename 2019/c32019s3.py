#TODO: unfinished

ln1 = input().split()
ln2 = input().split()
ln3 = input().split()

#[col, row]
map = [[ln1[0], ln2[0], ln3[0]],[ln1[1], ln2[1], ln3[1]],[ln1[2], ln2[2], ln3[2]]]
unsolved = []
#x pos
for col in map:
    #y pos
    for tile in col:
        if tile == "X":
            unsolved.append([map.index(col), col.index(tile)])

def find_val(tile):
    tile_x = tile[0]
    tile_y = tile[1]
    #check the column the tile belongs to see if it can be solved
    if (is_col_solveable(tile_x)):
        return solve_trio(map[tile_x])
    #check row
    elif (is_row_solveable(tile_y)):
        return solve_trio([map[0][tile_y], map[1][tile_y], map[2][tile_y]])
    else:
        return False

#return value of unknown tile
def solve_trio(trio):
    if trio[0] == "X":
        return (int(trio[1]) - (int(trio[2]) - int(trio[1])))
    elif trio[1] == "X":
        return (int(trio[2]) - ((int(trio[2]) - int(trio[0])) / 2))
    else:
        return (int(trio[1]) + (int(trio[1]) - int(trio[0])))


def is_col_solveable(col_num):
    knowns = 0
    for tile in map[col_num]:
        if tile != "X":
            knowns += 1
    if knowns > 1:
        return True
    else:
        return False
def is_row_solveable(row_num):
    knowns = 0
    for col in map:
        if col[row_num] != "X":
            knowns += 1
    if knowns > 1:
        return True
    else:
        return False

print(find_val([1, 1]))
