# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен
# из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100,
# рекомендуется использовать функцию random)
import random

names = ('Альбина, Розалия, Антонина, Поликарп, Ульяна, Венедикт, Любава, Юлий, Николай, Максим, Маргарита, Эльвира, Инга, Назар, Радислав, Дина, Кондрат, Оксана, Артур, Христина')
list_names = names.split(sep = ', ')
print('Входящий список из 20 имён:', list_names)

def list_random_names (list_n=100):
    list_names_new = []
    for i in range(list_n):
        list_names_new.append(random.choice(list_names))
    return list_names_new

list_random_names_var = list_random_names() # Глобальная переменная выходящего списка имен
                                            # введена для того чтобы зафиксирровать созданный
                                            # методом random список

print("Выходящий список из 100 имен:", list_random_names_var)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F

from collections import Counter

def frequent_list_random_names ():
    return Counter(list_random_names_var).most_common(1)[0][0]

print("Самое встречающееся имя в выходящем списке:", frequent_list_random_names())

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F

def rare_letter_list_random_names ():
    list_first_letters = list(map(lambda word: word[0], list_random_names_var))
    return Counter(list_first_letters).most_common()[-1][0]

print("Самая редко встречающаяся буква, в именах выходящего списка:", rare_letter_list_random_names())

# 4.  В файле с логами найти дату самого позднего лога (по метке времени)
from datetime import datetime

with open('log', mode = 'rt', encoding = 'utf-8') as log_file:
    log_text = log_file.read()

list_log_date = []
only_date = []
log_date = log_text.split('\n')

for i in log_date:
    list_log_date = i.split(',')
    only_date.append(list_log_date[0])

only_date.sort(key=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'), reverse=True)

print("Дата и время самого позднего лога: ", only_date[0])
print("Дата самого позднего лога: ", only_date[0].split(' ')[0])

# все