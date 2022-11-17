# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


# !!! Не достаточные условия постановки задачи: необходимо вывести таблицу предикат или проверить на ложь/истину?

print('Введите координаты X, Y и Z')
x = int(input())
y = int(input())
z = int(input())

# for x in [True,False]:
#     for y in [True,False]:
#         for z in [True,False]:
#             print(x,'AND',y,'OR',z,'=',x and y or z)

for x in range (2):
        for y in range (2):
            for z in range (2):
                print(not (x or y or z) == (not x and not y and not z))
                print (x, y, z)




