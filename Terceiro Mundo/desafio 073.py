tabeladobrasileirao = ['Atlético Mineiro', 'São Paulo', 'Flamengo', 'Flamengo', 'Internacional', 'Palmeiras', 'Santos', 'Fluminense', 'Grêmio', 'Fortaleza', 'Corinthians', 'Atlético Paranaense', 'Bahia', 'Atlético Goianiense', 'Bragantino', 'Ceará', 'Sport', 'Vasco da Gama', 'Coritiba', 'Botafogo', 'Goiás']
print('Primeiros 5 colocados', tabeladobrasileirao[0:5])
print('-'*100)
print('Útimos 4 colcados', tabeladobrasileirao[-5:])
print('-'*100)
print('Em ordem aldabética', sorted(tabeladobrasileirao))
print('-'*100)
posicaosp = tabeladobrasileirao.index('São Paulo')+1
print(f'Posição do São Paulo, {posicaosp}º colocado')
