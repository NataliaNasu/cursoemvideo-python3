#Listas parte 1 = []
#tuplas = () ou sem nada
lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

'''LISTAS são variáveis compostas
a únca diferença pra tupla é que elas SÃO MUTÁVEIS'''
lanche[0] = 'agua'
'''mostra > lanche = [agua, suco, pizza, pudim]'''

'''Adicionar'''
lanche.append('cookie')

'''Adicionar em uma determinada posição, os outros tb mudam de índice.
lista.insert(posição, valor)'''
lanche.insert(0, 'cachorro-quente')

'''apagar o elemento da posição especificada'''
del lanche[4]

'''geralmente, o pop é utilizado para apagar a última posição, 
nesse caso, n se atribui nenhum parâmetro'''
lanche.pop()

'''Mas é possível apagar em uma posição específica'''
lanche.pop(0)

'''remove > apaga o 1o valor/conteúdo passado como parâmetro'''
lanche.remove('suco')

'''Em todas essas operações de deleção, se NÃO for encontrada a posição 
ou o valor, o python retorna erro. pra corrigir: '''

if 'pizza' in lanche:
    lanche.remove('pizza')
    print('pizza foi removida com sucesso!')

#if lanche[3] in range(0, len(lanche)):
#    del lanche[3]
#    print('Valor da posição 2, foi deletada!')

'''Criação de listas através de RANGE, com a função LIST()'''

lista = list(range(4, 11))
'''imprimi: 0:4, 1:5, 2:6, 3:7, 4:8, 5:9, 6:10 > deixa em ordem'''

'''deixar em ORDEM:'''
valores = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
'''em ordem decrescente: '''
valores.sort(reverse=True)

'''tamanho: vai imprimir 7'''
len(valores)

if 5 in valores:
    valores.remove(5)
else:
    print('Não achei o número 5.')

valores = list() #ou valores =[]
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)

for v in valores:
    print(v, end=' ')
print('\n')
for i, val in enumerate(valores):
    print(f'Na posição {i}: {val}')

''' OU inserir pelo teclado: '''

num = []
for c in range(0, 3):
    num.append(int(input('Digite um valor: ')))

'''peculiaridade do python: qndo se iguala uma lista na outra, cria-se uma
LIGAÇÃO entre elas, então, qlqr mudança feita em uma, ocorre o mesmo na outra,
sendo assim, ocorre uma ligação e não uma cópia'''
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
'''imprimi: 
Lista A: [2, 3, 8, 7]
Lista B: [2, 3, 8, 7]
a alteração ocorre nas duas listas'''

'''Mas é possível criar uma CÓPIA: com FATIAMENTO'''
c = [1, 4, 7, 9]
d = c[:]
d[2] = 5
print(f'Lista A: {c}')
print(f'Lista B: {d}')
'''imprimi:
Lista c: [1, 4, 7, 9]
Lista d: [1, 4, 5, 9]'''