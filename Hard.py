n = int(input())

count = 0
max_numbers = 0
mazday = 0

for i in range(2, 11):
    conclusion1 = n
    count = 0 
    while True:
        conclusion2 = conclusion1 % i
        conclusion1 = conclusion1 // i
         
        if conclusion1 == 0: 
            count += conclusion2
            if max_numbers < count:
                max_numbers = count
                mazday = i
            elif mazday != 0 and max_numbers == count and mazday > i:
                mazday = i
            break
        else:
            count += conclusion2
print(mazday)