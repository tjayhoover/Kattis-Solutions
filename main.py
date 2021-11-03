import sys
stripped = []
lines = sys.stdin.readlines()
#with open("input.txt", "r") as file:
 #   lines = file.readlines()

for l in lines:
    l = l.strip()

for l in lines:
    l = l.strip()
    stripped.append(l.strip())

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