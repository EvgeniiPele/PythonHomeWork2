from random import randint
coins = int(input('Введите требуемое кол-во монет: '))
heads = 0
tails = 0
for _ in range(coins):
    heads_or_tails = randint(0, 1)
    print(f'сторона {heads_or_tails}')
    if heads_or_tails == 1:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(tails)
else:
    print(heads)