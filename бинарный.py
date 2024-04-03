import random

a = random.randint(1, 100)
i = 0

while True:
    b = int(input('введите число: '))
    i += 1
    if b > a:
        print('загаданное число меньше')
        continue
    if b < a:
        print('загаданное число больше')
        continue
    else:
        print('ВЫ ОТГАДАЛИ ЧИСЛО')
    break
print('количество попыток: ', i)