extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
n = int(input('Digite um número entre 0 e 20: '))
while True:
    n = int(input('Desculpe ,digite um número novamente entre 0 e 20: '))
    if n <= 20:
        print(f'\033[31m{extenso[n]}')
        break
