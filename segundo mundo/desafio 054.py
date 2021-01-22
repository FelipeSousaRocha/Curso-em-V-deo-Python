from datetime import date
anoatual = date.today().year
count = 0

for c in range(0,7):
    ano = int(input('Em que ano a {} nasceu?  '.format(c+1)))
    calculo = anoatual - ano
    if calculo >= 18:
        count += 1
print('Número de pessoas maiores de idade {}'.format(count))

