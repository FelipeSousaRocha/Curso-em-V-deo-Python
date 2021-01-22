nome = str(input("Qual seu nome? "))
if nome == 'Felipe':
    print("Seu nome é perfeito")
elif nome=='José' or nome=='Maria' or nome=='João':
    print("Seu nome é comum")
elif nome in 'Ana Cláudia Elen Jéssica Juliana ':
    print('Belo nome moça')
else:
    print('Nome legal')
print("Tenha um bom dia",nome)