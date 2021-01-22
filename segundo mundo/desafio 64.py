n = cont = soma = 0
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
#print('acabou voce digitou {} numeros e a soma dos números é {}'.format(cont -1,soma-999))
print('acabou voce digitou {} numeros e a soma dos números é {}'.format(cont -1,soma))