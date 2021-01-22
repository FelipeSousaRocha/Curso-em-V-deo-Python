print('{:=^40}'.format('Loja Do Bsoim'))
preconormal = float(input('Qual o preço do produto? R$ '))
print('digite (1) para pagar com dinheiro ou cheque')
print('digite (2) para pagar no débito')
print('digite (3) para pagar no credito em 2x')
print('digite (4) para pagar no crédito em 3x ou mais')
formadepagamento = int(input('Qual a forma de pagamento? '))



if formadepagamento == 1:
    preconormal = preconormal-(0.10*preconormal)
elif formadepagamento == 2:
    preconormal = preconormal-(0.5*preconormal)
elif formadepagamento == 3:
    preconormal = preconormal
    parcelado = preconormal/2
    print('Serão duas parcelas de R${}'.format(parcelado),end="")
elif formadepagamento == 4:
    preconormal = preconormal+(0.20*preconormal)
    totalparcelas = int(input('Quantas Parcelas? '))
    parcela = preconormal/ totalparcelas

print('O preço fica R${}'.format(preconormal))