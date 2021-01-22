valorcasa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))

salario30 = 0.30*salario
prestacao = valorcasa/(anos*12)

if prestacao <= salario30:
    print('Para pagar uma casa de R${} Valor em {} anos,O Valor a Pagar Mensalmente será R${:.2f}'.format(valorcasa,anos,prestacao))
else:
    print('O valor excedeu 30% do seu salário e não será possível pagar')
