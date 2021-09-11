#Variáves compostas > Listas - parte II

dados = list()
dados.append('Pedro')
dados.append(25)
print(dados[0])
#imprimi: Pedro
galera = list()
galera.append(dados) #galera.append(dados[:]) > CÓPIA
'''LIGAÇÃO'''
dados[0] = 'Jose'
dados[1] = 22
galera.append(dados)
print(galera)
'''imprimi: ['jose', 22], ['jose', 22] '''

'''LIGAÇÃO'''
listaA = listaB = []

dados.append('Maria')
dados.append(19)
dados.append('João')
dados.append(32)

'''englobar uma lista em outra: fazer uma CÓPIA, através de fatiamento'''

pessoas = list()
pessoas.append(dados[:])
print(pessoas)
print(pessoas[0][0])

''' OU
É uma lista PESSOAS2 que contém outras 3 listas menores'''

pessoas2 = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas2)
print(pessoas2[0][0])
'''retorna: "Pedro"'''
print(pessoas2[1][1])
'''retorna: 19'''
print(pessoas2[2][0])
'''retorna: "João"'''
print(pessoas2[1])
'''retorna: ['Maria', 19]'''

for p in pessoas2:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera2 = list()
listaTemporaria = list()
for i in range(0, 3):
    listaTemporaria.append(str(input('Nome: ')))
    listaTemporaria.append((int(input('Idade: '))))
    galera2.append(listaTemporaria[:])
    listaTemporaria.clear()
print(listaTemporaria)
print(galera2)
maior = menor = 0
for p in galera2:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'Ao todo, {maior} são maiores e {menor} são menores de idade.')
