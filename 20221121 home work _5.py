# Реализуйте алгоритм перемешивания списка.


import random
list1 = [1, 2, 3, 4, 5]
print (str(list1))

for i in range(len(list1)-1, 0, -1):	
	j = random.randint(0, i + 1)
	list1[i], list1[j] = list1[j], list1[i]
print (str(list1))








