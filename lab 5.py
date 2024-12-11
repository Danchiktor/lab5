import re

# Чтение файла task1_ru.txt
with open('task1-ru.txt', encoding='utf-8') as f:
    content = f.read()

# Регулярные выражения
numbers = re.findall(r'\b\d+\.\d+|\b\d+\b', content)  # Все числа (целые и дробные)
six_eight_letter_words = re.findall(r'\b\w{6}\b|\b\w{8}\b', content)  # Слова на 6 и 8 букв

print("1)Числа (целые и дробные):", numbers)
print("Слова на 6 и 8 букв:", six_eight_letter_words)


# Чтение файла task2.html
with open('task2.html', encoding='utf-8') as f:
    html_content = f.read()

# Регулярные выражения
content_values = re.findall(r'content="(.*?)"', html_content)  # Все строки из атрибута content

print("2)Значения из атрибута content:", content_values)


import re
import csv

with open('task3.txt', encoding='utf-8') as f:
    data = f.read()

elements = data.split()

emails = [el for el in elements if re.match(r'[\w\.-]+@[\w\.-]+\.\w+', el)]
dates = [el for el in elements if re.match(r'\d{4}-\d{2}-\d{2}', el)]
websites = [el for el in elements if re.match(r'http[s]?://', el)]
ids = [el for el in elements if re.match(r'^\d+$', el)]
last_names = [el for el in elements if re.match(r'^[A-Z][a-z]+$', el)]

min_length = min(len(emails), len(dates), len(websites), len(ids), len(last_names))


emails = emails[:min_length]
dates = dates[:min_length]
websites = websites[:min_length]
ids = ids[:min_length]
last_names = last_names[:min_length]


rows = zip(ids, last_names, emails, dates, websites)


with open('task3_normalized.csv', mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Фамилия', 'Электронная почта', 'Дата регистрации', 'Сайт'])
    writer.writerows(rows)

print("Данные успешно записаны в task3_normalized.csv")