#profs

numero = [[], []]
valor = 0

for c in range(0, 7):
    valor = int(input(f'Digite o {c+1}o valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
numero[0].sort()
numero[1].sort()
print(f'Pares: {numero[0]}')
print(f'Ímpares: {numero[1]}')