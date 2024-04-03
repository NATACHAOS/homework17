import random

a = random.randint(1, 100)

while True:
    b = int(input('введите число: '))
    if b > a:
        print('загаданное число меньше')
        continue
    if b < a:
        print('загаданное число больше')
        continue
    else:
        print('ВЫ ОТГАДАЛИ ЧИСЛО')
    break
