# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


List1 = [2, 3, 5, 9, 3]

print(List1)
list_length = len(List1)
sumOddElements = 0
count = 1
while count < list_length:
    sumOddElements = sumOddElements + List1[count]
    count = count + 2

print(sumOddElements)