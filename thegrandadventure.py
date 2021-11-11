import sys

lines = sys.stdin.readlines()
lines = [l.strip() for l in lines]

num_ad = lines.pop(0)

for l in lines:
    bool = True
    everyone_happy = True
    backpack = []
    for x in l:
        if x ==".":
            continue
        elif x in ['$', '|', '*']:
            backpack.append(x)
        elif x == "t":
            if len(backpack):
                insense = backpack.pop()
                if insense != "|":
                    everyone_happy = False
                    print("NO")
                    break
            elif not len(backpack):
                everyone_happy = False
                print("NO")
                bool = False
                break
        elif x == "j":
            if len(backpack):
                jewel = backpack.pop()
                if jewel != "*":
                    everyone_happy = False
                    print("NO")
                    break
            elif not len(backpack):
                everyone_happy = False
                print("NO")
                bool = False
                break
        elif x == "b":
            if len(backpack):
                money = backpack.pop()
                if money != "$":
                    everyone_happy = False
                    print("NO")
                    break
            elif not len(backpack):
                everyone_happy = False
                print("NO")
                bool = False
                break
    if bool and everyone_happy:
        if len(backpack) == 0:
            print("YES")
        else:
            print("NO")
