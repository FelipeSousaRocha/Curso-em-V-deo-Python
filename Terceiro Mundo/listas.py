#num = (2,5,9,1)  # DA erro , pois tupla é imutavel
#num[2] = 3
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
#num.sort()
num.sort(reverse=True)
num.insert(2,2)
#num.pop()
#num.pop(2)
num.remove(2) #remove a primeira ocorrencia
if 4 in num:
    num.remove(4)
else:
    print('Não achei o 4')
print(num)
print(f'Essa lista tem {len(num)} elementos')
