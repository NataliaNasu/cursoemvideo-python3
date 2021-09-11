#estruturas de controle

for c in range(0, 6):
    print('Oi')
print('FIM')

for c in range(0, 6):
    print(c)
'''retorna: 0, 1, 2, 3, 4, 5'''

for c in range(1, 6):
    print(c)
'''retorna: 1, 2, 3, 4, 5'''

for c in range(6, 0, -1):
    print(c)
'''Contagem regressiva'''

for c in range(0, 7, 2):
    print(c)
'''mostra o percurso com um salto 2
retorna: 0 2 4 6'''

inicio = int(input('Digite o início do for: '))
fim = int(input('Final do for: '))
salto = int(input('Salto: '))
for c in range(inicio, fim, salto):
    print(c)

'''Entrada de vários valores'''
for c in range(0, 3):
    numero = int(input('Digite um valor: '))

'''Soma de todos os valores'''
soma = 0
for c in range(0, 4):
    numero = int(input('Digite um valor: '))
    soma += numero
print(f'A soma de todos os números é igual a {soma}.')
