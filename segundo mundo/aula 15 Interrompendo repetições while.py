'''cont = 1
#while cont <= 10:
#    print(cont,'-> ',end='')
#    cont += 1
#print('acabou')

while True: #Loop Infinito
    print(cont,'-> ',end='')
    cont += 1
print('acabou')'''

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#print('A soma vale {}'.format(s))
print(f'A soma vale {s:.f} ') #{^-s}

'''cont = 0
while cont < 5:
    n=int(input('Digite um número: '))
    cont += 1'''
