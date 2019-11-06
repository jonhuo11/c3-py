#combining riceballs
riceball_count = int(input())
riceballs = [int(x) for x in input().split()]

def find_all_riceballs(initial):
    solutions = []
    for p in initial:
        solutions.append(find_subpaths(p))
    return solutions
    #array of possible next riceball arrays
    def find_subpaths(possible):
        for sp in possible:
            if len(sp) == 1:
                return sp[0]
            else:
                combinations = find_combinations(sp)
                #if the search is not a dead end, look for more
                if len()
                    return find_subpaths(combinations)
                else:


def find_combinations(rb):
    pass
