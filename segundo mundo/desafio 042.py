reta1 = int(input())
reta2 = int(input())
reta3 = int(input())

if reta1+reta2> reta3 and reta1+reta3>reta2 and reta2+reta3>reta1:
    print('Forma um triangulo',end='')
    if reta1 == reta2 == reta3:
        print(' Equilátero')
    if reta1 != reta2 != reta3 != reta1:
        print(' Escaleno')
    else:
        print('Isósceles')
else:
    print('Não forma um triângulo')
