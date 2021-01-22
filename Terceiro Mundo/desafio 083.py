#expr = str(input('Digite a expressão: '))
#pilha = []
#for símb in expr:
 #   if símb == '(':
   #     pilha.append('(') #coloca parenteses
   # elif símb == ')':
   #     if len(pilha) > 0:
   #         pilha.pop() #tira parenteses
  #      else:
  #          pilha.append(')')
 #           break
#if len(pilha) == 0:
#    print('Sua expressão está válida!')
#else:
#    print('Sua expressão está errada!')

#expr = str(input('Digite uma expressão: '))
#cont = 0
#for indice in expr:
    #if indice == '(':
    #    cont += 1
    #if indice == ')':
    #    cont -= 1
    #if cont < 0:
    #   break
#if cont == 0:
#    print('Sua expressão está válida!')
#else:
#    print('Sua expressão está errada!')

#expr = str(input('Digite a expressão: '))
#pi = expr.count('(')
#pf = expr.count(')')
#if expr.index(')') > expr.index('('):
    #if pi == pf:
        #print('Expressão válida')
    #else:
        #print('Expressão é inválida')
#else:
    #print('Expressão inválida')

expr = str(input("Digite uma expressão:"))
pilha = 0
for cont in expr:
    if cont == "(":
        pilha += 1
    if cont == ")":
        pilha -= 1
    if pilha < 0:
        break
if pilha == 0:
    print("Sua expressão é valida!!!")
else:
    print("Sua expressão é invalida!!!")

