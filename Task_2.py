from random import randint
sum_of_numbers = int(input('Введите сумму двух чисел: '))
product_of_numbers = int(input('Введите произведение этих чисел: '))
number_one = 1
number_two = 1
while number_one + number_two < sum_of_numbers or number_one * number_two != product_of_numbers:
    number_one = randint(1, sum_of_numbers)
    number_two = sum_of_numbers - number_one
print(number_one)
print(number_two)