numero = str(input('Digite um número [1111-9999]: '))
tamanho = len(numero)
unidade = numero[tamanho-1]
dezena = numero[tamanho-2]
centena = numero[tamanho-3]
milhar = numero[tamanho-4]
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')