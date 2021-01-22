lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    nao = str(input('Deseja Continuar? [S/N]'))[:1]
    if nao in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de ímpares é {listaimpar}')
