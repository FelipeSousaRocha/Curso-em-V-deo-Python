nota1 = float(input('Digite sua primeria nota: '))
nota2 = float(input('Digite sua segunda nota: '))

nota = (nota1+nota2)/2

if nota < 5:
    print('\033[31mReprovado')
elif nota >= 5 and nota <= 6.9:
    print('\033[33mRecuperação')
elif nota >= 7:
    print('\033[32mAprovado')
