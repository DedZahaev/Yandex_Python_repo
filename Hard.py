text2 = ""
letter_max = 0
count = ""
while True:
    text = input()
    text2 += text
    
    if text == "ФИНИШ":
        break
text2 = text2.lower().replace(' ', '')

for i, char in enumerate(text2):
    count = text2[i]
    letters = text2.count(char)

    if letters > letter_max:
        letter_max = letters
        s = char
    elif letters == letter_max:
        if char < s:
            s = char
        
print(s)
'''
Формат ввода
Вводятся строки, пока не будет введена строка «ФИНИШ».

Формат вывода
Выводится один символ в нижнем регистре — наиболее часто встречающийся.

Примечания
Пробелы в анализе не участвуют.
Если в результате анализа получено несколько ответов, следует вывести первый по алфавиту
'''