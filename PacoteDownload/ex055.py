#leia o peso de 5 pessoas, mostre ql foi o maior e o menor peso.

for c in range(0, 5):
    peso = float(input(f'Digite o peso da {c+1}a pessoa: '))
    if c == 0:
        maior = peso
        menor = peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso:
            menor = peso

print(f'Entre todas as 5 pessoas:'
      f'\nO maior peso foi {maior} kg'
      f'\nE o menor foi {menor} kg.')