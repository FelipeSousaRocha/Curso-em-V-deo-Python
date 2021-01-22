nomeprecos = ('Pão',1,'Leite',3.50,'Queijo',5,'Mortadela',2.5)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}') #centralizar em 40 caracteres
print('-'*40) #repetir 40x
for pos in range(0,len(nomeprecos)):
    if pos % 2 == 0:
        print(f'{nomeprecos[pos]:.<30}', end='') #alinhar a esquerda e esqrever em 30 caracteres
    else:
        print(f'R$ {nomeprecos[pos]:>3.2f}') #alinhei a direita em 3 caracteres e em float de 2
print('-'*40)