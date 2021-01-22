frase = str(input('Veja se a frase é um Palíndromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
'''inverso = '' '''
inverso=junto[::-1]
'''for letra in range(len(junto)-1, -1,-1): #junto -1 pra começar do 19 , -1 até o 0, e tirar-1
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')
