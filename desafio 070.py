tg = contp = menor = cont = 0
nomeb = ' '
while True:
    nome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço do produto: '))
    cont += 1
    tg += preco
    if preco > 1000:
        contp += 1
    if cont == 1:
        menor = preco
        nomeb = nome
    else:
        if preco < menor:
            menor = preco
            nomeb = nome
    interacao = ' '
    while interacao not in 'SN':
        interacao = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if interacao == 'N':
        break
print(f'Total de gastos {tg}, {contp} produtos custam mais de R$1000, {nomeb} é o produto mais barato.')