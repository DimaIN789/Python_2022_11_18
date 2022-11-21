# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23



print('Введите число')
k = int(input())

def sumNumber(num):
	return 0 if num == 0 else int(num % 10) + sumNumber(int(num / 10))

print(sumNumber(k))



