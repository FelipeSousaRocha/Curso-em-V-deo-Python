from random import randint
soma = 0
win = 0
while True:
    print('-='*20)
    print('Simbora jogar par ou impar')
    print('-='*20)
    computador = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    valor = str(input('Você escolhe par ou impar? ')).strip().upper()
    soma += jogador + computador
    if valor == 'PAR' and soma%2 == 0:
        win += 1
        print(f'O jogador jogou {jogador} e Venceu o computador que jogou {computador}')

    elif valor == 'IMPAR' and soma % 2 != 0:
        win += 1
        print(f'O jogador jogou {jogador} e Venceu o computador que jogou {computador}')
    else:
        print(f'Você Perdeu, pois jogou {jogador} e o computador jogou {computador} você venceu {win} vez(es)')
        break
'''from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo == 'P':
        if total%2 == 0:
            print('Você Venceu')
            v += 1
        else:
            print('Você Perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você Venceu')
            v += 1
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar novamente')
print(f'Game Over! Você venceu {v} vezes')'''


