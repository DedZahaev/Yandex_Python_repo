N = int(input()) 
flag = "YES"
for i in range(N):
    b = input()
    if b[0] != "а" and b[0] != "б" and b[0] != "в":
        flag = "NO"
print(flag)
 
