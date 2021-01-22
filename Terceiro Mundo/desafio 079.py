list = []
while True:
    n = int(input('Digite um valor: '))
    if list != n:
        list.append(n)
    else:
        print('Valor Duplicado! Não vou adicionar ...')
    print('Valor adicionado com sucesso...')
    sim = str(input('Deseja Continuar? [S/N]')).upper()[:1]
    if sim in 'Nn':
        print('=-'*30)
        print(f'Você digitou os valores {list.sort()}')
        break