# кортеж (tuple)- неизменяемый список

t = ()
print(type(t)) # tuple

t = (1,)
print(type(t)) # tuple

t = (1)
print(type(t)) # int

t = (28, 9, 1990)
print(type(t)) # tuple

colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']

t = tuple(colors)
print(t) # ('red', 'green', 'blue')

print('____')


a = (3, 1, 5, 4)
print(a)
print(a[-1])

print('____')

a = (3, 4, 5)
for item in a:
    print(item)

print('____')

# распакопвка кортежа в три самостоятельных переменных
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red, g:green, b:blue


