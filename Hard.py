c = []
count = 0
while True:
    a = input()
    if a == "":
        break
    if a.find("##") != -1 and a.endswith("@@@") is not True:
        c.append(a.lstrip("##"))
    elif a.endswith("@@@") is True:
        c = c
    else:
        c.append(a) 
for letter in (c):
    print(letter)



