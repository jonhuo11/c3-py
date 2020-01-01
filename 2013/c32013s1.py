def find_next(year):
    if (is_unique(year) == False):
        return find_next(year + 1)
    else:
        return year
def is_unique(year):
    y_list = list(str(year))
    added = []
    for digit in y_list:
        if (digit in added):
            return False
        else:
            added.append(digit)
    return True
def run(year):
    return find_next(year + 1)

print(run(int(input())))
