# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random 

#Gпросим пользователя ввести длинну списков
size_1 = int(input('Введите размер первого списка: '))
size_2 = int(input('Введите размер второго списка: '))

list_1 = []
list_2 = []

# Заполняем списки рандомным числами
for i in range(size_1):
    list_1.append(random.randint(1, 10))

for i in range(size_2):
    list_2.append(random.randint(1, 10))

#Выводим два сформированых списка списка
print(list_1)
print(list_2)

#Сравниваем значения двух списков между собой
same_list = []
for x in list_1:
    for y in list_2:
        if x == y:
            same_list.append(x)
# Сортируем одинаковые значения убираем повторяющееся цифры и сохранием их в списке темп

temp = [] 
[temp.append(x) for x in same_list if x not in temp]          
temp.sort()
print(temp)


