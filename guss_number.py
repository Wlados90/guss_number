from random import randint


number = randint(1, 100)

print('Угодайте число от 1 до 100')

while True:
    guess = int(input('Введите число: ')) 

    if guess < number:
        print('Ваше число меньше того что загаданно: ')

    if guess > number:
        print('Ваше число больше того что загаданно')

    if guess == number:

        break
print('Отличная интуиция! Вы угодали число :)')