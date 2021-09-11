distancia = int(input('Qual a distância da sua viagem em Km? '))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'Com uma distância de {distancia}Km,')
print(f'o preço da passagem é igual a R${preco:.2f} reais.')