#from math import factorial
#f = factorial(num)
num = int(input('Informe o número que você deseja verificar o fatorial: '))
n = num
resultado = 1
print('Calculando {}! '.format(n),end='')
while n > 0:
    print('{} '.format(n),end='')
    print('x ' if n > 1 else '=',end='')
    resultado *= n
    n -= 1

print(' {}'.format(resultado))