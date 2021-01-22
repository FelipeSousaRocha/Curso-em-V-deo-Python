'''lista = []
listapar = []
listaimpar = []
for c in range(7):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    lista.clear()
    lista.append(listapar[:])
    lista.append(listaimpar[:])
    listapar.sort()
    listaimpar.sort()
print('-='*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valroes ímpares digitados foram: {lista[1]}')'''

núm = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input('Digite um valor: '))
    if valor %2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
núm[0].sort()
núm[1].sort()
print(f'Os valores pares digitados : {núm[0]}')
print(f'Os valores ímpares digitados: {núm[1]}')
