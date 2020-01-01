'''
def parse(inp):
    input_arr = list(inp)
    input_arr.append(" ")
    output = ""
    prev = input_arr[0]
    count = 0
    for char in input_arr:
        #if char is not the same as prev, write down count + char
        if (char != prev):
            output = "{} {} {}".format(output, count, prev)
            count = 1
        #otherwise add to count
        else:
            count += 1
        prev = char
    return output

n = int(input())
inp = ""
for i in range(n):
    inp += input()
print(parse(inp))
'''
