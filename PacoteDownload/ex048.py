#encontre a soma dos ímpares,
#que sejam múltiplos de 3, entre 1-500

soma = 0
total = 0
for c in range(0, 500):
    if c % 2 != 0:
        if c % 3 == 0:
            soma += c
            total += 1

print(f'No intervalo de 1 a 500,'
      f'\nTêm-se {total} números ímpares múltiplos de 3.'
      f'\nE, a soma de todos os valores é igual a {soma}.')