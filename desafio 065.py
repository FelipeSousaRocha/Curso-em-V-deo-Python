s = q = media = maior = menor = 0
d = 'S'
while d in 'Ss':
    n = int(input('Digite um número: '))
    s += n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    d = str(input('Deseja continuar? [S/N]')).upper().strip()

media = s/q
print('A média é {:.2f} o maior numero é {} o menor é {}'.format(media,maior,menor))