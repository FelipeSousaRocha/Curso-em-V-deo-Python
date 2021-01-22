c = 0
while True:
    n = int(input('Digite a tabuada que você deseja ver[digite número negativo para parar]: '))
    if n < 0:
        break
    for c in range(0, 11):
        print(f'{n} x {c} = {c*n}')

