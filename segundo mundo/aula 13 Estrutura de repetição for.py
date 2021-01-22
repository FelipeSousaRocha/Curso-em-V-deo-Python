for c in range(0,6):
    print('OI')
print('FIM')

for a in range(6,0, -1): #regressiva
    print(a)
print('FIM')

for b in range(0,7,2):
    print(b)
n = int(input('Digite um número: '))

for d in range(0, n+1): #conta até o número digitado
    print(d)
print('fim')

i=int(input('Inicio: '))
f=int(input('Fim: '))
p=int(input('Passo: '))
for e in range(i, f+1, p):
    print(e)
print('FIM')

s = 0
for f in range(0,4):
    n= int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))