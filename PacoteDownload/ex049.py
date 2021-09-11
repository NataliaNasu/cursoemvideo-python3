#tabuada

numero = int(input('Qual tabuada você quer saber? '))

soma = 0
for c in range(1, 11):
    soma += numero
    print(f'{numero} x {c} = {soma}')

''' OU '''
print('\n')

for c in range(1, 11):
    print(f'{numero} x {c} = {numero*c}')