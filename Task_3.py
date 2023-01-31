limit = int(input('Введите число: '))
degree = 0
while degree < limit:
    number = 2 ** degree
    degree += 1
    if number <= limit:
        print(number)
    else:
        break