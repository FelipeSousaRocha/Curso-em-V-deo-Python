n = int(input('Qual será o número? '))
print('[1] Binário')
print('[2] octal')
print('[3] Hexedacimal')
basedeconversao = int(input('Ecolha a base para converter: '))


conversao = 0

if basedeconversao == 1:
    conversao = bin(n)

elif basedeconversao == 2:
    conversao = oct(n)

elif basedeconversao == 3:
    conversao = hex(n)

print('O número convertido é {}'.format(conversao[2:])) #[2:] para retirar os dois primeiros caracteres
