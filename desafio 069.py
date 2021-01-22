contmaiores = conthomens = contmulheres = 0
while True:
    idade = int(input('Coloque a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Coloque o sexo [M/F]: ')).upper().strip()[0]
    if idade >= 18:
        contmaiores += 1
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F' and idade < 20:
        contmulheres += 1
    interacao = ' '
    while interacao not in 'SN':
        interacao = str(input('deseja continuar [S/N]? ')).upper()
    if interacao in 'Nn':
        break
print(f'Existem {contmaiores} pessoas maiores de 18 anos, existem {conthomens} homens cadastrados, existem {contmulheres} mulheres com menos de 20 anos cadastradas.')