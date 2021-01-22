n = []
pos_maior_valor = []
pos_menor_valor = []
for c in range(5):
    n.append(int(input(f'Digitem um valor para posição {c}: ')))
for posicao, valores in enumerate(n):
    if valores == max(n):
        pos_maior_valor.append(posicao)
    if valores == min(n):
        pos_menor_valor.append(posicao)
print('=-'*50)
print(f'Você digitou os valores {n}')
print(f"Maior valor digitado: {max(n)} nas posições {pos_maior_valor}")
print(f'Menor valor digitado: {min(n)} nas posições {pos_menor_valor}')


#listanum = []
#mai = 0
#men = 0
#for c in range(0,5):
#   listanum.append(int(input(f'Digite um valor na posição {c}')))
#   if c==0:
#       mai = listanum[c]
#   else:
#       if listanum[c] > mai:
#           mai = listanum[c]
#       if listanum[c] < men:
#           men = listanum[c]
#print('=-'*30)
#print(f'Você digitou os valores {listanum}')
#print(f'O maior valor digitado foi {mai}', end="")
#for i, v in enumerate(listanum):
#   if v==maior:
#       print(f'{i}... ')
print()
#print(f'O menor valor digitado foi o {men}', end="")
#for i, v in enumerate(listanum):
#   if v == men:
#       print(f"{i}... ", end="")
#print()

