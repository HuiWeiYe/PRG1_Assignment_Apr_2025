with open('level1.txt','r') as file:
    contents = file.readlines()

for column in contents:
    for tile in column:
        print("#",end="")
    print()

print()

for column in contents:
    for tile in column:
        if not tile == " ":
            print(tile,end="")
        else:
            print("#",end="")