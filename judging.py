from collections import Counter
import sys
lines = sys.stdin.readlines()

lines = [f.strip() for f in lines]

number = int(lines[0])
del(lines[0])

dom = Counter(lines[:number])
kat = Counter(lines[number:])

a = dom-kat
b = dom-a

print(sum(b.values()))
