n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')),)
print(f'Você digitou: {n}')
print(f'Possui: {n.count(9)} número(s) 9')
if 3 in n:
    print(f'O primeiro número 3 foi digitado na posição: {n.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram:', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
