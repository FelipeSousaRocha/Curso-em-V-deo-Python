from random import randint
from time import sleep
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-='*20)
print('O computador escolheu {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*20)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('\033[33mEMPATE')

    elif jogador == 1:
        print('\033[32mJOGADOR VENCEU')

    elif jogador == 2:
        print('\033[31mJOGADOR PERDEU')

    else:
        print('\033[31mJOGADA INVÁLIDA')

elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('\033[31mJOGADOR PERDEU')

    elif jogador == 1:
        print('\033[33mEMPATE')

    elif jogador == 2:
        print('\033[32mJOGADOR VENCEU')

    else:
        print('\033[31mJOGADA INVÁLIDA')

elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('\033[32mJOGADOR VENCEU')

    elif jogador == 1:
        print('\033[31mJOGADOR PERDEU')

    elif jogador == 2:
        print('\033[33mEMPATE')

    else:
        print('\033[31mJOGADA INVÁLIDA')

