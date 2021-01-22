#tabuada = int(input('Tabuada do: '))
#for c in range(0,11):
  #  resultado = tabuada*c
  #  print('{} x {} = {}'.format(tabuada,c,resultado))
num = int(input('Quero a tabuada do: '))
for c in range(0,11):
    print('{} x {:2} = {}'.format(num,c,num*c))