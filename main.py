from random import randrange

N = randrange(4, 31)
print("В куче лежит", N, "камней")
while N > 0:
    print("Выберете количество камней от 1 до 3")
    try:
        player = int(input())
    except ValueError:
        print("Вы ввели не целое число")
        break
    if player < 1 or player > 3:
        print("введите числа 1, 2 или 3")
        break
    while N - player < 1:
        print("количество камней в кучке не может быть отрицательным и 0")
        player = int(input())
        continue
    N = N - player
    if N == 1:
        print("Вы победили")
        break
    print("После вашего ход в кучке осталось", N)
    computer = randrange(1, 4)
    print("компьютер выбрал", computer, "камней")
    while N - computer < 1:
        computer = randrange(1, 4)
        continue
    N = N - computer
    print("После хода компьютера осталось", N)
    if N == 1:
        print("Компьютер победил")
        break
