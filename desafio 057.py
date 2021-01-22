sexo = str(input('Digite seu sexo [M/f]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Digite seu sexo novamente [M/f]: ')).upper().strip()[0]
print('Fim')
