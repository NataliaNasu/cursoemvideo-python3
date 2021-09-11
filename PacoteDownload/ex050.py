#ler 6 numeros, somar somente os que forem pares.

soma = total = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c}o número: '))
    if numero % 2 == 0:
        soma += numero
        total += 1
print(f'A soma dos {total} números pares foi {soma}.')