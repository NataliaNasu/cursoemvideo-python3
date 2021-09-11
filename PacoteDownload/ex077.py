#tupla com várias palavras. mostre as vogais de cada palavra.

palavras = ['palavras', 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito']
print('\n\033[31m ~ VOGAIS ~ \033[m')
for c in palavras:
    print(f'\nEm "{c.upper()}": ', end='')
    for letra in c:
        if letra.lower() in 'aieou':
            print(f'{letra}', end=' ')

        '''if 'a' in (palavras[c]).strip():
            print(f'{i} a', end=' ')
        if 'e' in palavras[c]:
            print('e', end=' ')
        if 'i' in palavras[c]:
           print('i', end=' ')
        if 'o' in palavras[c]:
            print('o', end=' ')
        if 'u' in palavras[c]:
            print('u', end=' ')'''

