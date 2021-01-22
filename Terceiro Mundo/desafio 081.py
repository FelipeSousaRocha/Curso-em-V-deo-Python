list = []
while True:
    n = int(input('Digite um valor: '))
    list.append(n)
    sim = str(input('Deseja continuar? [S/N]'))[:1]
    if sim in 'Nn':
        break
print('-='*30)
print(len(list))
list.sort(reverse=True)
print(f'Os valores em ordem descrescente são {list}')
if 5 in list:
    print(f'O 5 está na lista e está na posição {list.index(5)}')
else:
    print('O 5 não está na lista')

