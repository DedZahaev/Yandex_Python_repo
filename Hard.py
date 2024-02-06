full_list = []
while True:
    text = input()
    comm = text.find("#")
    if comm != -1:
        full_list.append(text[:comm])
    else:
        full_list.append(text)
    if text == "":
        break

for i in range(len(full_list)):
    if full_list[i] == "":
        continue
    else:
        print(full_list[i])
'''
Формат ввода
Вводятся строки программы.
Признаком остановки является пустая строка.

Формат вывода
Каждую строку нужно очистить от комментариев.
А если комментарий — вся строка, то выводить её не надо.
'''