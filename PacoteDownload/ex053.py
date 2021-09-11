#leia uma frase, verificar se é um palíndromo.

frase = str(input('Digite uma frase: ')).strip().upper()
print(f'Você digitou a frase: {frase}.')
palavras = frase.split()
junto = ''.join(palavras)
espaco = frase.count(' ')
tamanho = len(frase) - espaco

inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}. \nPortanto: ')
if junto == inverso:
    print('A frase É um palíndromo!')
else:
    print('A frase NÃO é um palíndromo...')

''' OU ~> com FATIAMENTO'''
print('\n')

f = str(input('Digite outra frase: ')).strip().upper()
p = f.split()
j = ''.join(p)
inv = j[::-1]
print(f'O inverso de {j} é {inv}. \nPortanto: ')
if inv == j:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo')
