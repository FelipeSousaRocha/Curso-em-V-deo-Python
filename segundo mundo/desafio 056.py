mediaidade = 0
hv = 0
idademulher = 0
maioridadehome=0
for c in range(1,5):
    nome = str(input('Nome da {}ª pessoa: '.format(c)))
    idade = int(input('idade da {}ª pessoa: '.format(c)))
    sexo = str(input('Sexo da {}ª pessoa  M/F: '.format(c)))
    mediaidade += idade
    mi = mediaidade/5
    if c ==1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        idademulher += 1
print('A média de idade é {}'.format(mi))
print('O homem mais velho é o {}'.format(nomevelho))
print('Existem {} mulheres menores que 20 anos'.format(idademulher))