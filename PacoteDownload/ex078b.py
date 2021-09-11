#profs

numero = []
maior = menor = 0

for i in range(0, 5):
    numero.append(int(input('Digite um número: ')))
    if i == 0:
        maior = menor = numero[i]
    else:
        if maior < numero[i]:
            maior = numero[i]
        if menor > numero[i]:
            menor = numero[i]

print('Lista de números: ', end='')
for v in numero:
    print(v, end=' ')
print()
print(f'O maior valor digitado foi {maior}'
      f'\ne, se encontra nas posições: ', end='')
for posicao, v in enumerate(numero):
    if v == maior:
        print(f'{posicao+1}', end='... ')
print()
print(f'O menor valor digitado foi {menor}'
      f'\ne, se encontra nas posições: ', end='')
for posicao, v in enumerate(numero):
    if v == menor:
        print(f'{posicao+1}', end='... ')