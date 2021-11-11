import sys

lines = sys.stdin.readlines()
#with open("input1.txt", "r") as file:
 #   lines = file.readlines()

lines = [l.strip() for l in lines]

num_ad = lines[0]

lines.remove(lines[0])

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
            if len(backpack) > 0:
                insense = backpack.pop()
                if insense != "|":
                    everyone_happy = False
                    print("NO")
                    break
                else:
                    continue
            elif len(backpack) == 0:
                everyone_happy = False
                print("NO")
                bool = False
                break
        elif x == "j":
            if len(backpack) > 0:
                jewel = backpack.pop()
                if jewel != "*":
                    everyone_happy = False
                    print("NO")
                    break
                else:
                    continue
            elif len(backpack) == 0:
                everyone_happy = False
                print("NO")
                bool = False
                break
        elif x == "b":
            if len(backpack) > 0:
                money = backpack.pop()
                if money != "$":
                    everyone_happy = False
                    print("NO")
                    break
                else:
                    continue
            elif len(backpack) == 0:
                everyone_happy = False
                print("NO")
                bool = False
                break
    if bool and everyone_happy:
        if len(backpack) == 0:
            print("YES")
        else:
            print("NO")