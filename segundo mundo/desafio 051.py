
primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primeirotermo + (10-1)*razao
for c in range(primeirotermo,decimo+razao, razao):
    print('{}'.format(c),end=' -> ')
print('acabou')

#pt = int(input('1° termo: '))
#r = int(input('Razão: '))
#for c in range(pt , pt + 10 * r, r):
#    print(c, end=' ')
