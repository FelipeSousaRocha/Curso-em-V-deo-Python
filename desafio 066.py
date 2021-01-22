c = s = 0
while True:
    n = int(input("Digite o valor [Para parar digite 999] : "))
    if n == 999:
        break
    s += n
    c += 1
print(f'A soma dos {c} valores é {s}')