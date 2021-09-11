#Leia varios numeros e armazene dentro de uma lista.
#caso o número já exista, não adicione.
#mostre, os valores em ordem crescente.

valores = []

while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado!')
    opcao = input('Deseja continuar? [S/N] ').upper()
    while opcao not in 'NS':
        opcao = input('Deseja continuar? [S/N] ').upper()
    if opcao == 'N':
        break

print(sorted(valores))
#OU valores.sort()
#print(f'{valores}')