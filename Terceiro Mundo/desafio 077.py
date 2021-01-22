palavras = ('jegue','urubu','camelo','vaca','tartaruga','gato','peixe','cachorro')
for vezes in palavras:
    print(f'\nNa palavra {vezes.upper()} temos ', end='') #quebra linha \n
    for letra in vezes:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
