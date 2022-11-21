# словари (dictionaries) - неупорядочные коллекции произвольныхт объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'up': '^',
        'left': 'l' #через запятую
        # 'down'
        # 'right'
    }

print(dictionary) # распечатываем весь словарь
print(dictionary['up']) # распечатываем конкретный символ/объект


print('____')

for k in dictionary.keys(): # распечатаем ключи
    print(k)

print('____')

for v in dictionary.values(): # распечатем символ/объект
    print(v)