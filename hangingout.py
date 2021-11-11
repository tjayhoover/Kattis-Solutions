import sys

lines = sys.stdin.readlines()

stripped = [l.strip() for l in lines]

two_numbers = stripped[0].split()
FSL = int(two_numbers[0])
NOE = int(two_numbers[1])

events = stripped[1:]

on_terrace = 0
rejected = 0

for event in events:
    if event[:5] == "enter":
        if on_terrace + int(event[6:]) <= FSL:
            on_terrace += int(event[6:])
        else:
            rejected += 1
    elif event[:5] == "leave":
        on_terrace -= int(event[6:])

print(rejected)
