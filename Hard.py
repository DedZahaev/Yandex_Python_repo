N = int(input())
letters = []
letters2 = []
for i in range(N):
    a = input()
    letters.append(a)

b = input()

for i in range(len(letters)):  
    if letters[i].lower().count(b.lower()) != 0:
        letters2.append(letters[i])

for i in range(len(letters2)):
    print(letters2[i])

'''
Формат ввода
Вводится натуральное число 
�
N — количество страниц, среди которых требуется произвести поиск.
В каждой из последующих 
�
N строк записаны заголовки страниц.
В последней строке записан поисковый запрос.

Формат вывода
Вывести все заголовки страниц, в которых присутствует поисковый запрос (регистр не имеет значения).
Порядок заголовков должен сохраниться.
'''