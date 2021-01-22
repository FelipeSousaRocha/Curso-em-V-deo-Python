from datetime import date
ano = int(input('Qual o seu ano de nascimento? '))

anoatual = date.today().year
idade = anoatual-ano

if idade <= 9:
    print('Você está na Categoria Mirim')
elif idade <= 14:
    print('Você está na Categoria Infantil')
elif idade <= 20:
    print('Você está na Categoria Sênior')
elif idade > 20:
    print('Você está na Categoria Master')
