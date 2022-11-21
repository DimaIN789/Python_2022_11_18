# работа с файлами
# a - открытие для добавления данных
# r - открытие для чтения данных
# w - открытие дял чтения данных
# w+, r+


colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')
data.writelines(colors) # разделетилей не будет
data.write('\nLINE 121\n')
data.write('LINE 1233\n')

data.close()

exit()


