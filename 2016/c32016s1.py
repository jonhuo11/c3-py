'''
str_a = input()
str_b = input()

from sets import Set
import sys

chars = Set([char for char in str_a])

wc_count = 0
for char in str_b:
    if char in chars:
        chars.remove(char)
    elif char == '*':
        wc_count += 1
    elif '\n' in chars:
        chars.remove('\n')
    else:
        print("N")
        sys.exit()

for i in range(0, wc_count):
    try:
        chars.pop()
    except Exception:
        print("N")
        sys.exit()

print("N")
'''
