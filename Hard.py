N = input()
a = []
b = []
lenth = len(N) 
for i in range(0, lenth):
    if i < lenth // 2:
        a.append(N[i])
    elif lenth % 2 != 0 and i == lenth // 2:
        a.append(N[i])
        b.append(N[i])
    else:
        b.append(N[i])

b = b[::-1]
if a == b:
    print("YES")
else:
    print("NO")


