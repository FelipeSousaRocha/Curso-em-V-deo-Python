'''import random
from time import  sleep
num = random.randint(0,10)
n = int(input("Adivinhe o valor que o pc pensou entre 0 e 10: "))
cont = 0
while n != num:
    n = int(input('Tente acertar o número novamente: '))
    cont += 1
print('Carregando... ')
sleep(2)
print('Você acertou a reposta Após {} tentativas'.format(cont))
'''

from  random import randint
computador = randint(0,10)
print('Sou seu computador ... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
print("Acertou, você tentou {} vezes".format(palpites))
