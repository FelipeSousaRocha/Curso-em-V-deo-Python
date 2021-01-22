peso = float(input('Coloque seu peso: '))
altura = float(input('Coloque sua altura: '))

IMC = peso/(altura**2)

if IMC < 18.5:
    print('Você está abaixo do peso')
elif IMC >= 18.5 < 25:
    print('Você está no peso ideal')
elif IMC >= 25 <30:
    print('Sobrepeso')
elif IMC >=30 <= 40:
    print('obesidade')
elif IMC > 40:
    print('Obesidade Morbida')