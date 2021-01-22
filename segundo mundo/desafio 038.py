from datetime import date
ano = int(input('Qual o seu ano de nascimento? '))

anoatual = date.today().year
idade = anoatual-ano
falta = 18-idade
passou = idade-18

if idade == 18:
    print('Está na hora de se alistar')
elif idade < 18:
    print('Falta {} anos para você se alistar'.format(falta))
elif idade > 18:
    print('Já se passou {} anos do tempo de se alistar'.format(passou))
