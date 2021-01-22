from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1,10),randint(1,10), )
print('Os valores sorteado foram:')
for c in n:
    print(f'{c} ', end='')
print(f'\nMaior número :{min(n)}')
print(f'Menor número: {max(n)}')



