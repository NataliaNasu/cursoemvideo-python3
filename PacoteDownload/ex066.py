#leia vários números e só pare no 999.
#mostre quantos foram digitados e a soma.

soma = total = 0
while True:
    n = int(input('Digite um nº: [999 encerra o programa] '))
    if n == 999:
        break
    soma += n
    total += 1
print(f'A soma dos {total} valores é igual a {soma}.')
