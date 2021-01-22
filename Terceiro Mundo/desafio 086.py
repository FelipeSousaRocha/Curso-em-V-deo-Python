'''linha1 = [[], [], []]
while True:
    for c in range(3):
        n = int(input(f'Digite um valor para [0, {c}]: '))
        linha1[0].append(n)
    for c in range(3):
        n = int(input(f'Digite um valor para [1, {c}]: '))
        linha1[1].append(n)
    for c in range(3):
        n = int(input(f'Digite um valor para [2, {c}]: '))
        linha1[2].append(n)
    print('-='*40)
    for pos, valor in enumerate(linha1[0]):
        print(f'[  {valor}  ]', end='')
    print()
    for pos, valor in enumerate(linha1[1]):
        print(f'[  {valor}  ]', end='')
    print()
    for pos, valor in enumerate(linha1[2]):
        print(f'[  {valor}  ]', end='')
    break'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-='*30)
for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()