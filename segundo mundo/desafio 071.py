'''print('-='*20)
print('Bem Vindo ao Banco BS')
print('-='*20)
while True:
    vs = int(input('Qual será o valor a ser sacado ?'))
    print('-='*20)
    cinquenta = vs/50
    restoc = vs%50
    vinte = restoc/20
    restov = restoc%20
    dez = restov/10
    restod = restov%10
    um = restod/1
    break
print(f'Cédulas de cinquenta {cinquenta}')
print(f'Cédulas de vinte {vinte}')
print(f'Cédulas de dez {dez}')
print(f'Cédulas de um {um}')'''
print('='*30)
print('{:~30}'.format('Banco CEV'))
print('='*30)
valor = int(input('Que valor você quer sacar ? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= ced
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd ==20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total ==0:
            break
print('='*30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')
