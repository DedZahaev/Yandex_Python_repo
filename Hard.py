N = int(input())
count = 0

for i in range(N):
    a = input()
    a = a.split()
    for i in range(len(a)):
        if a[i] == "зайка":
            count += 1
print(count)
    