# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


print('Введите число')
n = int(input())

# n = int(input())
# list = [round(n*i) for i in range(1, n+1)]
# print(list)

import math
list = [round(math.factorial(i)) for i in range(1, n+1)]
print(list)

# долго с этой задачкой провозился, но результата все таки добился))))) 