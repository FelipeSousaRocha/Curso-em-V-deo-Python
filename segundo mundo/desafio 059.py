from time import  sleep

n1 = int(input('Digite o Primeiro valor: '))
n2 = int(input('Digite o Segundo valor: '))
o = 0

while o != 5:
    print('[ 1 ] Para SOMAR')
    print('[ 2 ] Para MULTIPLICAR')
    print('[ 3 ] Para MAIOR')
    print('[ 4 ] Acrescentar NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')
    o = int(input('O que você deseja fazer? '))
    print('CARREGANDO ... ')
    sleep(2)

    if o == 1:
        print('A soma de {} + {} = {}'.format(n1,n2,n1+n2))
    elif o == 2:
        print('A multiplicação de {} * {} = {}'.format(n1,n2,n1*n2))
    elif o == 3:
        if n1>n2:
            print('O maior entre {} e {} é {}'.format(n1,n2,n1))
        else:
            print('O maior entre {} e {} é {}'.format(n1,n2,n2))
    elif o == 4:
        print('Informe os números novamente')
        n1 = int(input('Digite o Primeiro valor: '))
        n2 = int(input('Digite o Segundo valor: '))
    elif o == 5:
        print('FIM')
