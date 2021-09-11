#leia o ano de nascimento de 7 pessoas.
# indique quem é maior de idade e quem não.
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    anoN = int(input(f'Digite o ano de nascimento da {c}a pessoa: '))
    idade = date.today().year - anoN
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print(f'Entre as 7 pessoas:')
print(f'{maior} são maiores de idade.')
print(f'E, {menor} são menores...')
