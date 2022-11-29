max = 6

for i in range(0, 7):
    if i == 0: print("*" * 11)
    print("*", " " * max, "*")
    max = max - 1
else:
    max = max + 1
    print("*")
    for i in range(0, 7):
        print("*", " " * max, "*")
        max = max + 1
        if i == 6: print("*" * 11)
