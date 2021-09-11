#TUPLA = são variáveis compostas, de diferentes tipos. é uma LISTA.
#se identificam por índices. Os valores são IMUTÁVEIS.

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
'''pode ser definida sem nada ou entre parênteses'''

print(lanche)
'''mostra tudo'''

print(lanche[2])
'''mostra: pizza'''

print(lanche[:2])
'''mostra até o 1: hamburguer, suco'''

print(lanche[1:])
'''vai imprimi até o fim: suco, pizza, pudim'''

print(lanche[-1])
'''quando é negativo, imprime do final > início
ou seja, vai mostra: pudim'''
print(lanche[-2])
'''mostra: pizza'''

len(lanche)
'''mostra o tamanho: 4'''

print(lanche)

'''print sem parenteses'''
for i in range(0, len(lanche)):
    print(lanche[i], end=' ')

print('\n')

'''É possível utilizar for SEM RANGE, como em COLEÇÕES, em tuplas'''
for comida in lanche:
    print(comida, end=' ')
print('\n')

'''enumerate: fornece o índice e o valor da tupla'''
for posicao, comida in enumerate(lanche):
    print(f'{posicao}: {comida}')

'''sorted > organiza a tupla, não a altera, só mostra em ordem'''
print(sorted(lanche))

'''a soma de tuplas = concatenação. A ORDEM IMPORTA'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
'''mostra: 2, 5, 4, 3, 8, 1, 2'''
d = b + a
print(d)
'''mostra: 5, 8, 1, 2, 2, 5, 4'''

print(c.count(5))
'''count = mostra qntos 5 tem na tupla c = 2.
se não encontrar devolve 0'''

print(c.index(8))
'''mostra a 1a posição de 8 = 4'''

print(c.index(2, 4))
'''procura a posição do nº2 a partir da posição 4'''

'''TUPLAS SÃO IMUTÁVEIS'''
'''pode-se somente deletá-la'''
pessoa = ('Gustavo', 33, 'M', 98.8)
del(pessoa)
