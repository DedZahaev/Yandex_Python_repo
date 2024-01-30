L = int(input())
N = int(input())
a = []
for i in range(N):
    a.append(input())  
for item in a:
    lenth = len(item)
    if lenth > L:
        print(item[:L - 3] + "...")
    else:
        print(item)
    

 
