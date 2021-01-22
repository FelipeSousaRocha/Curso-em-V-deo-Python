soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += cont + 1
print('A soma de todos os {} números pares dos 6 digitados é {}'.format(cont,soma))
